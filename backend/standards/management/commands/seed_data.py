import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
import datetime as dt
from django.core.management.base import BaseCommand
from standards.models import (
    ProductFamily, Standard, StandardEdge, CertificationRule, ParamRule
)
from standards.knowledge_data import (
    FAMILIES, STANDARDS, EDGES, CERTS, PARAMS, LAST_VERIFIED
)

class Command(BaseCommand):
    help = 'Seed the curated knowledge base (idempotent).'

    def handle(self, *args, **options):
        self.stdout.write('Seeding families...')
        fam_objs = {}
        for f in FAMILIES:
            obj, _ = ProductFamily.objects.update_or_create(
                slug=f['slug'],
                defaults={'name': f['name'], 'description': f['description'], 'keywords': f['keywords']},
            )
            fam_objs[f['slug']] = obj

        self.stdout.write('Seeding standards...')
        std_objs = {}
        for s in STANDARDS:
            fam_obj = fam_objs.get(s['family']) if s['family'] else None
            replaced_by_key = s.get('replaced_by')
            obj, _ = Standard.objects.update_or_create(
                is_number=s['is_number'], part=s['part'] or '', year=s['year'],
                defaults={
                    'title': s['title'],
                    'family': fam_obj,
                    'std_type': s['std_type'],
                    'status': s['status'],
                    'amendments': s['amendments'],
                    'amendment_note': s.get('amendment_note', ''),
                    'source_url': s['source_url'],
                    'verification': s['verification'],
                    'notes': s.get('notes', ''),
                    'last_verified': s.get('last_verified', LAST_VERIFIED),
                    'triggers': s.get('triggers', []),
                },
            )
            std_objs[s['key']] = obj

        self.stdout.write('Resolving replaced_by links...')
        for s in STANDARDS:
            if s.get('replaced_by'):
                obj = std_objs.get(s['key'])
                target = std_objs.get(s['replaced_by'])
                if obj and target and obj.replaced_by_id != target.pk:
                    obj.replaced_by = target
                    obj.save(update_fields=['replaced_by'])

        self.stdout.write('Seeding edges...')
        for e in EDGES:
            src = std_objs.get(e['src'])
            dst = std_objs.get(e['dst'])
            if not src or not dst:
                self.stdout.write(self.style.WARNING(f"  skipping edge {e['src']} -> {e['dst']}: not found"))
                continue
            StandardEdge.objects.update_or_create(
                src=src, dst=dst, edge_type=e['edge_type'],
                defaults={
                    'mandatory': e['mandatory'],
                    'condition': e.get('condition', ''),
                    'evidence': e.get('evidence', ''),
                    'source_url': e.get('source_url', ''),
                },
            )

        self.stdout.write('Seeding certification rules...')
        for c in CERTS:
            fam_obj = fam_objs.get(c['family'])
            if not fam_obj:
                continue
            CertificationRule.objects.update_or_create(
                family=fam_obj,
                order_ref=c['order_ref'],
                enterprise_size=c['enterprise_size'],
                defaults={
                    'is_number': c['is_number'],
                    'scheme': c['scheme'],
                    'effective_date': c.get('effective_date'),
                    'since_year': c.get('since_year'),
                    'state': c['state'],
                    'notes': c['notes'],
                    'source_url': c['source_url'],
                    'verification': c['verification'],
                    'last_verified': c.get('last_verified', LAST_VERIFIED),
                },
            )

        self.stdout.write('Seeding parameter rules...')
        for p in PARAMS:
            fam_obj = fam_objs.get(p['family'])
            std_obj = std_objs.get(p['std_key'])
            if not fam_obj or not std_obj:
                continue
            ParamRule.objects.update_or_create(
                family=fam_obj, standard=std_obj,
                grade=p['grade'] or '', param=p['param'],
                defaults={
                    'operator': p['operator'],
                    'value': p['value'],
                    'unit': p['unit'],
                    'clause_ref': p['clause_ref'],
                    'source_url': p['source_url'],
                    'verification': p['verification'],
                },
            )

        self.stdout.write(self.style.SUCCESS(
            f'Done. {len(fam_objs)} families, {len(std_objs)} standards seeded.'
        ))
