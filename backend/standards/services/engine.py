from __future__ import annotations
import datetime as dt
from typing import Optional
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from standards.knowledge_data import (
    FAMILIES, STANDARDS, EDGES, CERTS, PARAMS,
    ALLOWED_HALLMARK_KARATS, SCHEME_LABELS, LAST_VERIFIED,
)
from standards.services.extraction import run_extraction

DISCLAIMER = (
    "Decision-support only. This is a prototype covering a small hand-curated set of product families. "
    "Always verify against the official BIS Manak portal (https://standards.bis.gov.in/website/know-your-standards) "
    "and the relevant Ministry/DPIIT notification before finalising any tender or specification."
)

_STD_BY_KEY = {s['key']: s for s in STANDARDS}
_STD_BY_ISNO: dict[str, list[dict]] = {}
for _s in STANDARDS:
    _STD_BY_ISNO.setdefault(_s['is_number'], []).append(_s)

def _display_no(s: dict) -> str:
    n = s['is_number']
    if s['part']: n += f" ({s['part']})"
    if s['year']: n += f":{s['year']}"
    return n

def _std_out(s: dict, role: str = 'primary', mandatory: bool = True,
             condition: str = '', reason: str = '') -> dict:
    return {
        'is_number': s['is_number'], 'part': s['part'], 'year': s['year'],
        'display_number': _display_no(s), 'title': s['title'],
        'std_type': s['std_type'], 'status': s['status'], 'role': role,
        'mandatory': mandatory, 'condition': condition,
        'reason': reason or f"Matched product family.",
        'amendments': s['amendments'],
        'amendment_note': s.get('amendment_note', ''),
        'notes': s.get('notes', ''),
        'source_url': s['source_url'],
        'verification': s['verification'],
        'last_verified': s.get('last_verified', LAST_VERIFIED).isoformat(),
        'replaced_by': s['replaced_by'],
        'triggers': s.get('triggers', []),
    }

def _parse_date(v) -> Optional[dt.date]:
    if v is None or v == '': return None
    if isinstance(v, dt.date): return v
    try: return dt.date.fromisoformat(str(v))
    except ValueError: return None

def recommendations_for_family(family_slug: str, text: str = '') -> list[dict]:
    primary_keys = {
        'tmt-steel-bars':     ['IS 1786||2008'],
        'cement-opc':         ['IS 269||2015'],
        'gold-hallmarking':   ['IS 1417||2016'],
        'aluminium-utensils': ['IS 1660||2024'],
        'led-lamps-crs':      ['IS 16102|1|2012'],
    }
    out = []
    for key in primary_keys.get(family_slug, []):
        s = _STD_BY_KEY.get(key)
        if s:
            out.append(_std_out(s, 'primary', True, '', f"Primary standard for '{family_slug.replace('-', ' ')}'."))

    if not out: return out

    text_l = text.lower()
    src_keys = {o['is_number'] + '|' + (o['part'] or '') + '|' + str(o['year'] or '')
                for o in out}
    seen_dst = set()
    for edge in EDGES:
        if edge['src'] not in src_keys: continue
        dst = _STD_BY_KEY.get(edge['dst'])
        if not dst: continue
        if dst['key'] in seen_dst: continue
        if dst.get('triggers'):
            if not any(t.lower() in text_l for t in dst['triggers']):
                continue
        seen_dst.add(dst['key'])
        out.append(_std_out(dst, edge['edge_type'], edge['mandatory'],
                            edge.get('condition', ''), edge.get('evidence', '')))
    return out

def cert_verdicts(family_slug: str, tender_date: dt.date, delivery_date: Optional[dt.date],
                  enterprise_size: str) -> dict:
    rules = [c for c in CERTS if c['family'] == family_slug]
    if not rules:
        return {'schemes': [], 'note': 'No certification rule curated for this family yet.'}

    by_scheme: dict[str, list] = {}
    for r in rules:
        by_scheme.setdefault(r['scheme'], []).append(r)

    horizon = delivery_date or tender_date
    schemes_out = []
    for scheme, srules in by_scheme.items():
        srules_for_size = [r for r in srules if r['enterprise_size'] in (enterprise_size, 'all')]
        if not srules_for_size:
            srules_for_size = srules

        history = []
        for r in sorted(srules_for_size, key=lambda x: (x['effective_date'] is None, x['effective_date'] or dt.date(9999,1,1))):
            history.append({
                'order_ref': r['order_ref'],
                'is_number': r['is_number'],
                'effective_date': r['effective_date'].isoformat() if r['effective_date'] else None,
                'since_year': r.get('since_year'),
                'enterprise_size': r['enterprise_size'],
                'state': r['state'],
                'notes': r['notes'],
                'source_url': r['source_url'],
                'verification': r['verification'],
                'last_verified': r['last_verified'].isoformat() if r.get('last_verified') else None,
            })

        dated_active = [r for r in srules_for_size
                        if r['effective_date'] and r['state'] not in ('superseded', 'deferred', 'revoked')]
        undated_active = [r for r in srules_for_size
                          if not r['effective_date'] and r['state'] not in ('superseded', 'deferred', 'revoked')]

        controlling = None
        for r in sorted(dated_active, key=lambda x: x['effective_date']):
            if r['effective_date'] <= horizon:
                controlling = r
        upcoming = sorted([r for r in dated_active if r['effective_date'] > horizon],
                          key=lambda x: x['effective_date'])

        if controlling:
            verdict = 'mandatory_now' if controlling['effective_date'] <= tender_date else 'mandatory_by_delivery'
            leading = controlling
        elif upcoming:
            verdict = 'upcoming_after_delivery'; leading = upcoming[0]
        elif undated_active:
            verdict = 'mandatory_historical_verify_date'; leading = undated_active[0]
        else:
            verdict = 'deferred_or_revoked'; leading = srules_for_size[-1]

        newer_undated = [r for r in undated_active if r is not leading]
        caveat = None
        if newer_undated:
            refs = '; '.join(r['order_ref'] for r in newer_undated)
            caveat = (f"A later order exists whose exact effective date for this enterprise size was not confirmed: "
                      f"{refs}. Verify directly with BIS / DPIIT.")
        if verdict == 'mandatory_historical_verify_date' and leading.get('since_year'):
            caveat = (f"This scheme has been mandatory since approximately {leading['since_year']} but the exact "
                      f"notification date was not confirmed in the sources reviewed. Verify before finalising.")

        ctrl_out = {
            'order_ref': leading['order_ref'],
            'is_number': leading['is_number'],
            'effective_date': leading['effective_date'].isoformat() if leading['effective_date'] else None,
            'notes': leading['notes'],
            'source_url': leading['source_url'],
        }
        schemes_out.append({
            'scheme': scheme,
            'scheme_label': SCHEME_LABELS.get(scheme, scheme),
            'verdict': verdict,
            'controlling_order': ctrl_out,
            'caveat': caveat,
            'order_history': history,
        })
    return {'schemes': schemes_out, 'note': None}

def _param_findings(family_slug: str, grade: Optional[str],
                    extracted_params, text: str = '') -> list[dict]:
    findings = []
    if family_slug == 'gold-hallmarking':
        for p in extracted_params:
            if p.name == 'fineness_karat':
                k = int(p.value)
                if k not in ALLOWED_HALLMARK_KARATS:
                    findings.append({
                        'type': 'param_conflict', 'severity': 'high',
                        'message': (f"{k} karat is not among the caratages currently covered by mandatory "
                                    f"hallmarking ({sorted(ALLOWED_HALLMARK_KARATS)}). "
                                    "Confirm with BIS whether this caratage is eligible."),
                        'is_number': 'IS 1417',
                        'detail': {'stated_karat': k, 'allowed_karats': sorted(ALLOWED_HALLMARK_KARATS)},
                    })
        return findings

    family_params = [p for p in PARAMS if p['family'] == family_slug]
    for ep in extracted_params:
        for r in family_params:
            applies = (r['grade'] is None or r['grade'] == '' or r['grade'] == grade)
            if not applies: continue
            if r['param'] != ep.name: continue
            if ep.unit not in (r['unit'], 'MPa'): continue
            ok = True
            if r['operator'] == 'min' and ep.value < r['value']: ok = False
            elif r['operator'] == 'max' and ep.value > r['value']: ok = False
            elif r['operator'] == 'equal' and ep.value != r['value']: ok = False
            if not ok:
                g_txt = f"Grade {grade} " if grade else ""
                std = _STD_BY_KEY.get(r['std_key'], {})
                findings.append({
                    'type': 'param_conflict', 'severity': 'high',
                    'message': (f"{g_txt}requires {r['param'].replace('_', ' ')} "
                                f"{r['operator']} {r['value']} {r['unit']} "
                                f"({r['clause_ref']}), but the description states {ep.value} {ep.unit}."),
                    'is_number': r['std_key'].split('|')[0],
                    'detail': {
                        'param': r['param'], 'required_operator': r['operator'],
                        'required_value': r['value'], 'stated_value': ep.value,
                        'unit': r['unit'], 'clause_ref': r['clause_ref'],
                        'source_url': r['source_url'], 'verification': r['verification'],
                    },
                })
    return findings

def _citation_audit(cited_stds, family_slug: Optional[str],
                    recommended_primary_isnos: set, text: str = '') -> list[dict]:
    findings = []
    cited_isnos = set()
    for c in cited_stds:
        cited_isnos.add(c.is_number)
        matches = _STD_BY_ISNO.get(c.is_number, [])
        if not matches:
            findings.append({
                'type': 'not_covered', 'severity': 'info',
                'message': (f"{c.raw} is not in this prototype's curated database "
                            "(only 5 product families are covered in this MVP). Verify manually on the BIS Manak portal."),
                'is_number': c.is_number, 'detail': {},
            })
            continue
        best = None
        if c.year:
            best = next((s for s in matches if s['year'] == c.year), None)
        if not best:
            best = sorted(matches, key=lambda s: (s['year'] or 0), reverse=True)[0]
        if best['status'] in ('withdrawn', 'superseded'):
            repl = best['replaced_by']
            repl_txt = ''
            if repl:
                rk = _STD_BY_KEY.get(repl)
                repl_txt = f" Replaced by {_display_no(rk)}." if rk else f" Replaced by {repl}."
            findings.append({
                'type': 'withdrawn_citation' if best['status'] == 'withdrawn' else 'superseded_citation',
                'severity': 'high',
                'message': (f"{_display_no(best)} is {best['status']}.{repl_txt}"),
                'is_number': best['is_number'],
                'detail': {'status': best['status'], 'replaced_by': repl},
            })
        elif c.year and best['year'] and c.year != best['year']:
            findings.append({
                'type': 'year_mismatch', 'severity': 'medium',
                'message': (f"The text cites the {c.year} edition; the latest curated edition is {best['year']}."),
                'is_number': best['is_number'],
                'detail': {'cited_year': c.year, 'current_year': best['year']},
            })
        if family_slug and best.get('family') and best['family'] != family_slug:
            findings.append({
                'type': 'possible_wrong_standard', 'severity': 'medium',
                'message': (f"{_display_no(best)} belongs to the '{best['family']}' product family, "
                            f"which does not match the detected family '{family_slug}'. Check this citation."),
                'is_number': best['is_number'],
                'detail': {'cited_family': best['family'], 'detected_family': family_slug},
            })
    if family_slug and recommended_primary_isnos and not (recommended_primary_isnos & cited_isnos):
        findings.append({
            'type': 'missing_primary_standard', 'severity': 'high',
            'message': (f"The description does not cite {', '.join(sorted(recommended_primary_isnos))}, "
                        f"which this system recommends for '{family_slug}'."),
            'is_number': None,
            'detail': {'recommended': sorted(recommended_primary_isnos)},
        })
    return findings

def analyze(description: str, tender_date=None, delivery_date=None,
            delivery_period_days=None, enterprise_size='large') -> dict:
    tender_date = _parse_date(tender_date) or dt.date.today()
    delivery_date = _parse_date(delivery_date)
    if delivery_date is None and delivery_period_days:
        try: delivery_date = tender_date + dt.timedelta(days=int(delivery_period_days))
        except (TypeError, ValueError): pass

    extraction = run_extraction(description)
    fm = extraction.family_match

    result: dict = {
        'input_summary': {
            'characters': len(description),
            'lines': len([l for l in description.splitlines() if l.strip()]),
            'tender_date': tender_date.isoformat(),
            'delivery_date': delivery_date.isoformat() if delivery_date else None,
            'enterprise_size': enterprise_size,
        },
        'family_detection': {
            'abstained': fm.abstained,
            'abstain_reason': fm.abstain_reason,
            'detected_family': fm.family['slug'] if fm.family else None,
            'detected_family_name': fm.family['name'] if fm.family else None,
            'confidence_band': ('high' if fm.score >= 3 else ('medium' if fm.score >= 1 else 'none')),
            'matched_keywords': fm.matched_keywords,
            'detected_language': extraction.detected_language,
            'was_expanded': getattr(fm, 'was_expanded', False),
            'all_family_scores': {
                slug: d['score'] for slug, d in fm.all_scores.items()
            },
        },
        'extracted_grade': extraction.grade,
        'extracted_params': [
            {'name': p.name, 'value': p.value, 'unit': p.unit, 'raw_context': p.raw_context}
            for p in extraction.params
        ],
        'cited_standards': [
            {'raw': c.raw, 'is_number': c.is_number, 'part': c.part, 'year': c.year}
            for c in extraction.cited
        ],
        'recommendations': [],
        'certifications': {'schemes': [], 'note': None},
        'findings': [],
        'data_as_of': LAST_VERIFIED.isoformat(),
        'disclaimer': DISCLAIMER,
    }

    if fm.abstained or not fm.family:
        result['findings'].append({
            'type': 'abstained', 'severity': 'info',
            'message': fm.abstain_reason, 'is_number': None, 'detail': {},
        })
        result['findings'].extend(_citation_audit(extraction.cited, None, set(), description))
        return result

    slug = fm.family['slug']
    recs = recommendations_for_family(slug, description)
    result['recommendations'] = recs
    primary_isnos = {r['is_number'] for r in recs if r['role'] == 'primary'}

    result['certifications'] = cert_verdicts(slug, tender_date, delivery_date, enterprise_size)
    result['findings'].extend(_param_findings(slug, extraction.grade, extraction.params, description))
    result['findings'].extend(_citation_audit(extraction.cited, slug, primary_isnos, description))

    sev = {'high': 0, 'medium': 1, 'low': 2, 'info': 3}
    result['findings'].sort(key=lambda f: sev.get(f['severity'], 9))
    return result
