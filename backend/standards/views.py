import json
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from standards.models import Feedback, ProductFamily, Standard
from standards.services.document_reader import DocumentReadError, extract_text
from standards.services.engine import analyze
from standards.services.examples import EXAMPLES

MIN_LINES = 5
MIN_CHARS = 300

def _err(msg, status=400):
    return JsonResponse({'error': msg}, status=status)

@require_GET
def health(request):
    return JsonResponse({
        'status': 'ok',
        'data_as_of': settings.DATA_AS_OF,
        'families_seeded': ProductFamily.objects.count(),
        'standards_seeded': Standard.objects.count(),
    })

@require_GET
def families_view(request):
    return JsonResponse({
        'families': [
            {'slug': f.slug, 'name': f.name, 'description': f.description}
            for f in ProductFamily.objects.all()
        ]
    })

@require_GET
def examples_view(request):
    return JsonResponse({'examples': EXAMPLES})

@csrf_exempt
@require_POST
def analyze_view(request):
    description = ''
    tender_date = delivery_date = delivery_period_days = None
    enterprise_size = 'large'
    ct = request.content_type or ''
    if ct.startswith('multipart/form-data'):
        uploaded = request.FILES.get('file')
        if uploaded:
            try:
                description = extract_text(uploaded)
            except DocumentReadError as exc:
                return _err(str(exc))
        description = (description + '\n' + request.POST.get('description', '')).strip()
        tender_date = request.POST.get('tender_date') or None
        delivery_date = request.POST.get('delivery_date') or None
        delivery_period_days = request.POST.get('delivery_period_days') or None
        enterprise_size = request.POST.get('enterprise_size') or 'large'
    else:
        try:
            body = json.loads(request.body or '{}')
        except json.JSONDecodeError:
            return _err('Request body must be valid JSON.')
        description = body.get('description', '') or ''
        tender_date = body.get('tender_date') or None
        delivery_date = body.get('delivery_date') or None
        delivery_period_days = body.get('delivery_period_days') or None
        enterprise_size = body.get('enterprise_size') or 'large'

    description = description.strip()
    lines = len([l for l in description.splitlines() if l.strip()])
    if lines < MIN_LINES and len(description) < MIN_CHARS:
        return _err(
            f'Please provide at least {MIN_LINES} lines or {MIN_CHARS} characters of detail, '
            f'or upload a document. Received {lines} line(s), {len(description)} character(s).'
        )
    if enterprise_size not in ('all', 'large', 'small', 'micro'):
        return _err("enterprise_size must be one of: all, large, small, micro.")
    try:
        result = analyze(
            description=description, tender_date=tender_date,
            delivery_date=delivery_date, delivery_period_days=delivery_period_days,
            enterprise_size=enterprise_size,
        )
    except ValueError as exc:
        return _err(f'Could not parse a provided date: {exc}')
    result['data_as_of'] = settings.DATA_AS_OF
    return JsonResponse(result)

@csrf_exempt
@require_POST
def feedback_view(request):
    try:
        body = json.loads(request.body or '{}')
    except json.JSONDecodeError:
        return _err('Request body must be valid JSON.')
    is_number = body.get('is_number')
    action = body.get('action')
    if not is_number or action not in ('accept', 'reject', 'flag'):
        return _err("is_number and action ('accept'|'reject'|'flag') are required.")
    Feedback.objects.create(
        analysis_id=body.get('analysis_id', ''),
        is_number=is_number, action=action, note=body.get('note', ''),
    )
    return JsonResponse({'status': 'recorded'})
