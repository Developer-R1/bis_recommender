from __future__ import annotations
import re
import unicodedata
from dataclasses import dataclass, field
from typing import Optional
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from standards.knowledge_data import (
    FAMILIES, STANDARDS, HINDI_SYNONYMS, LANG_PATTERNS,
    DEVANAGARI_RANGE, TAMIL_RANGE, TELUGU_RANGE,
    KANNADA_RANGE, GUJARATI_RANGE,
)

def _word_boundary_re(phrase: str) -> re.Pattern:
    parts = phrase.strip().split()
    escaped = r'\s+'.join(re.escape(p) for p in parts)
    return re.compile(r'(?<![A-Za-z0-9])' + escaped + r'(?![A-Za-z0-9])', re.IGNORECASE)

_FAMILY_PATTERNS: dict[str, list[re.Pattern]] = {}
for _fam in FAMILIES:
    _FAMILY_PATTERNS[_fam['slug']] = [
        _word_boundary_re(kw.strip())
        for kw in _fam['keywords'].split(',') if kw.strip()
    ]

_TITLE_BOOST: dict[str, list[re.Pattern]] = {
    'tmt-steel-bars': [
        re.compile(r'\bFe\s*-?\s*(415|500|550|600|650|700)\s*[DS]?\b', re.I),
        re.compile(r'\bHYSD\b|\bdeformed\s+bar\b|\brebar\b|\breinforcement\s+bar\b', re.I),
        re.compile(r'\bribbed\s+(bar|steel|rod)\b|\bCTD\s+bar\b|\btor\s+(steel|bar)\b', re.I),
        re.compile(r'\bsteel\s+(bar|rod)\s+(for\s+)?(reinforc|concrete|RCC|slab|column|beam)\b', re.I),
        re.compile(r'\b(concrete|slab|column|beam|RCC|foundation)\s+(reinforc|bar|rod)\b', re.I),
    ],
    'cement-opc': [
        re.compile(r'\b(33|43|53)\s*[-\s]?grade\b', re.I),
        re.compile(r'\bOPC\b|\bpozzolana\b|\bslag\s+cement\b', re.I),
        re.compile(r'\bcementitious\b|\bhydraulic\s+cement\b|\bbinding\s+material\b', re.I),
        re.compile(r'\bmortar\b|\bconcrete\s+mix\b|\bconcrete\s+work\b', re.I),
    ],
    'gold-hallmarking': [
        re.compile(r'\b\d{2}\s*(k|karat|carat)\b', re.I),
        re.compile(r'\bHUID\b|\bhallmark', re.I),
        re.compile(r'\bgold\s+(chain|ring|bangle|coin|bar|bullion|necklace|bracelet|earring)\b', re.I),
        re.compile(r'\bassaying\s+centre\b|\bhallmarking\s+centre\b|\bfineness\b', re.I),
    ],
    'aluminium-utensils': [
        re.compile(r'\b(wrought|cast)\s+alumin', re.I),
        re.compile(r'\balumini\w+\s+(utensil|cookware|pan|pot|vessel|tray|plate|bowl)\b', re.I),
        re.compile(r'\banodiz\w+\s+alumin|\bpressure\s+cooker\b', re.I),
        re.compile(r'\baluminium\s+(bartan|kadai|handi|tiffin|mess|canteen)\b', re.I),
    ],
    'led-lamps-crs': [
        re.compile(r'\bLED\s+(lamp|bulb|light|luminaire|tube|batten|panel|strip)\b', re.I),
        re.compile(r'\bself.?ballasted\b|\bgeneral\s+lighting\b|\bsolid\s+state\s+lighting\b', re.I),
        re.compile(r'\benergy\s+(saving|efficient)\s+(lamp|light|bulb)\b', re.I),
        re.compile(r'\bLED\s+driver\b|\bLED\s+module\b|\bLED\s+fitting\b', re.I),
    ],
}


def _has_script_range(text: str, lo: str, hi: str) -> bool:
    return any(lo <= ch <= hi for ch in text)


def detect_language(text: str) -> str:
    if _has_script_range(text, DEVANAGARI_RANGE[0], DEVANAGARI_RANGE[1]):
        return 'hi'
    if _has_script_range(text, TAMIL_RANGE[0], TAMIL_RANGE[1]):
        return 'ta'
    if _has_script_range(text, TELUGU_RANGE[0], TELUGU_RANGE[1]):
        return 'te'
    if _has_script_range(text, KANNADA_RANGE[0], KANNADA_RANGE[1]):
        return 'kn'
    if _has_script_range(text, GUJARATI_RANGE[0], GUJARATI_RANGE[1]):
        return 'gu'
    text_l = text.lower()
    for lang, terms in LANG_PATTERNS.items():
        if any(t.lower() in text_l for t in terms if not any(lo <= t[0] <= hi for lo, hi in [
            (DEVANAGARI_RANGE), (TAMIL_RANGE), (TELUGU_RANGE), (KANNADA_RANGE), (GUJARATI_RANGE)
        ])):
            return lang
    return 'en'


_IS_NUMBER_MASK_RE = re.compile(r'\bIS\s*[:\-]?\s*\d{3,6}\b', re.I)
_NUM_MASK_RE = re.compile(r'\b(Fe\s*\d{3}|OPC\s*\d{2}|\d{2}\s*(karat|carat|k\b)|\d+\s*MPa|\d+\s*mm)\b', re.I)


def _mask_technical(text: str) -> tuple[str, list[str]]:
    tokens = []
    def _replace(m):
        tokens.append(m.group(0))
        return f'__TOKEN{len(tokens)-1}__'
    masked = _IS_NUMBER_MASK_RE.sub(_replace, text)
    masked = _NUM_MASK_RE.sub(_replace, masked)
    return masked, tokens


def _unmask(text: str, tokens: list[str]) -> str:
    for i, tok in enumerate(tokens):
        text = text.replace(f'__TOKEN{i}__', tok)
    return text


def expand_synonyms(text: str) -> str:
    masked, tokens = _mask_technical(text)
    text_l = masked.lower()
    additions = []
    sorted_synonyms = sorted(HINDI_SYNONYMS.items(), key=lambda kv: len(kv[0]), reverse=True)
    for native, english in sorted_synonyms:
        native_l = native.lower()
        is_ascii = all(ord(c) < 128 for c in native)
        if is_ascii:
            pattern = _word_boundary_re(native)
            matched = bool(pattern.search(text_l))
        else:
            matched = native_l in masked.lower() or native in masked
        if matched and english not in text_l:
            additions.append(english)
    expanded = masked
    if additions:
        expanded = masked + ' ' + ' '.join(additions)
    return _unmask(expanded, tokens)


def normalize_input(text: str) -> tuple[str, str]:
    lang = detect_language(text)
    expanded = expand_synonyms(text)
    return expanded, lang


@dataclass
class FamilyMatch:
    family: Optional[dict]
    score: int
    second_score: int
    matched_keywords: list
    all_scores: dict
    abstained: bool
    abstain_reason: Optional[str]
    detected_language: str = 'en'
    was_expanded: bool = False


def detect_family(text: str, normalized_text: Optional[str] = None) -> FamilyMatch:
    text_norm = ' '.join((normalized_text or text).split())
    scores: dict[str, dict] = {}
    for fam in FAMILIES:
        slug = fam['slug']
        matched = [pat.pattern for pat in _FAMILY_PATTERNS[slug] if pat.search(text_norm)]
        score = len(matched)
        for pat in _TITLE_BOOST.get(slug, []):
            if pat.search(text_norm):
                score += 2
        scores[slug] = {'score': score, 'matched_keywords': matched, 'family': fam}
    ranked = sorted(scores.values(), key=lambda d: d['score'], reverse=True)
    if not ranked or ranked[0]['score'] == 0:
        return FamilyMatch(None, 0, 0, [], scores, True,
            "No product-family keywords were recognised. Please add specific product or material terms "
            "(e.g. 'TMT reinforcement bar', 'OPC cement', 'LED lamp', 'gold jewellery', 'aluminium cookware').")
    top = ranked[0]
    second = ranked[1]['score'] if len(ranked) > 1 else 0
    if top['score'] == second and second > 0:
        tied = [d['family']['name'] for d in ranked if d['score'] == top['score']]
        return FamilyMatch(None, top['score'], second, top['matched_keywords'], scores, True,
            f"Description matches more than one family equally ({', '.join(tied)}). Add a distinguishing detail.")
    return FamilyMatch(top['family'], top['score'], second, top['matched_keywords'], scores, False, None)


_GRADE_RE = {
    'tmt-steel-bars': re.compile(r'\bFe\s*-?\s*(415|500|550|600|650|700)\s*(D|S)?\b', re.I),
    'cement-opc': re.compile(r'\b(?:OPC\s*-?\s*)?(33|43|53)\s*[Ss]?\b(?:\s*[-\s]?grade\b)?', re.I),
    'gold-hallmarking': re.compile(r'\b(\d{2})\s*(?:k\b|karat|carat)', re.I),
}


def extract_grade(text: str, family_slug: str) -> Optional[str]:
    pat = _GRADE_RE.get(family_slug)
    if not pat:
        return None
    m = pat.search(text)
    if not m:
        return None
    if family_slug == 'tmt-steel-bars':
        suffix = (m.group(2) or '').upper()
        return f"Fe {m.group(1)}{suffix}"
    if family_slug == 'cement-opc':
        return m.group(1)
    if family_slug == 'gold-hallmarking':
        return m.group(1)
    return m.group(0)


_PARAM_CTX_RE = re.compile(
    r'(?P<ctx>[A-Za-z0-9 .%/\-]{0,50}?)\s*(?P<val>\d{1,5}(?:\.\d+)?)\s*'
    r'(?P<unit>MPa|N/mm2|N/mm²|mm|micron|%)',
    re.I,
)
_KARAT_RE = re.compile(r'\b(?P<val>\d{2})\s*(?:k\b|karat|carat)', re.I)

_PARAM_MAP = {
    'yield': 'yield_strength', 'proof stress': 'yield_strength',
    '0.2%': 'yield_strength', 'tensile': 'ultimate_tensile_strength',
    'compressive': 'compressive_strength_28d', 'compression': 'compressive_strength_28d',
    'sheet thickness': 'sheet_thickness', 'wall thickness': 'sheet_thickness',
    'thickness': 'sheet_thickness',
}


@dataclass
class ExtractedParam:
    name: str
    value: float
    unit: str
    raw_context: str


def extract_params(text: str) -> list[ExtractedParam]:
    out: list[ExtractedParam] = []
    for m in _PARAM_CTX_RE.finditer(text):
        ctx = m.group('ctx').lower()
        unit = m.group('unit')
        val = float(m.group('val'))
        canonical = 'unspecified'
        for kw, key in _PARAM_MAP.items():
            if kw in ctx:
                canonical = key
                break
        if 'MPa' in unit or 'N/mm' in unit:
            unit = 'MPa'
        out.append(ExtractedParam(canonical, val, unit, m.group('ctx').strip()))
    for m in _KARAT_RE.finditer(text):
        out.append(ExtractedParam('fineness_karat', float(m.group('val')), 'karat', 'karat'))
    return out


_IS_CITE_RE = re.compile(
    r'\bIS\s*[:\-]?\s*(?P<num>\d{3,6})'
    r'(?:\s*\(\s*[Pp]art\s*-?\s*(?P<part>[0-9A-Za-z/]+)\s*\))?'
    r'(?:[:\s\-]+(?P<year>(?:19|20)\d{2}))?',
)


@dataclass
class CitedStandard:
    raw: str
    is_number: str
    part: Optional[str]
    year: Optional[int]


def extract_cited(text: str) -> list[CitedStandard]:
    out, seen = [], set()
    for m in _IS_CITE_RE.finditer(text):
        num = m.group('num')
        part = m.group('part')
        year = int(m.group('year')) if m.group('year') else None
        is_no = f"IS {num}"
        key = (is_no, part, year)
        if key not in seen:
            seen.add(key)
            out.append(CitedStandard(m.group(0).strip(), is_no, part, year))
    return out


@dataclass
class Extraction:
    family_match: FamilyMatch
    grade: Optional[str]
    params: list = field(default_factory=list)
    cited: list = field(default_factory=list)
    detected_language: str = 'en'
    normalized_text: str = ''


def run_extraction(text: str) -> Extraction:
    normalized, lang = normalize_input(text)
    fm = detect_family(text, normalized_text=normalized)
    fm.detected_language = lang
    fm.was_expanded = (normalized.strip() != text.strip())
    grade = extract_grade(text, fm.family['slug']) if fm.family else None
    return Extraction(fm, grade, extract_params(text), extract_cited(text),
                      detected_language=lang, normalized_text=normalized)
