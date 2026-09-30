# Architecture

```
 Officer input (text / .txt / .docx / .pdf)
            │
            ▼
 ┌─────────────────────────┐
 │ document_reader.py       │  extracts plain text from an upload (no LLM)
 └────────────┬─────────────┘
              ▼
 ┌─────────────────────────┐
 │ extraction.py             │  REGEX + KEYWORDS ONLY:
 │  - detect_family()        │   • product-family keyword scoring
 │  - extract_grade()        │   • per-family grade regex (Fe500D, 43 grade, 22 karat…)
 │  - extract_params()       │   • "<number> MPa/karat" with nearby-word context
 │  - extract_cited_standards│   • "IS 1786:2008" style citation regex
 └────────────┬─────────────┘
              ▼
 ┌─────────────────────────────────────────────────────────────┐
 │ engine.py — everything below is plain Python + SQL lookups,   │
 │ never a model call. This is the whole "zero hallucination"    │
 │ guarantee: every IS number in the response was SELECTed from  │
 │ the Standard table, never generated as text.                  │
 │                                                                │
 │  _recommendations_for_family()  → Standard + StandardEdge join │
 │  certification_verdicts()       → CertificationRule date logic │
 │  _param_findings()              → ParamRule min/max/equal check│
 │  _citation_findings()           → audit cited vs curated        │
 └────────────┬───────────────────────────────────────────────────┘
              ▼
        JSON response  →  frontend renders cards, timeline, findings
```

## Why no LLM is required for correctness

A model is very good at understanding messy language and very bad at
reliably reproducing exact registry numbers, dates and legal thresholds. So
the split here is:

- **Language understanding** (does this sentence mean "Fe 500D"?) →
  currently regex, because the vocabulary for these 4 families is small and
  well-defined. This is the natural place to add an LLM later for messier,
  longer, more free-form tenders — but only to fill in the *same* structured
  fields, never to invent an IS number directly.
- **Facts** (is this standard current? is this certification mandatory by
  this date? does this number satisfy this grade's minimum?) → always a
  database lookup or arithmetic comparison. This part must never involve a
  model, in this MVP or any future version.

One consequence: this backend runs correctly with **no API key configured
at all** — there's nothing to configure. That's also why it's cheap and
reliable to host on a free tier: no rate limits, no per-request cost, no
risk of an LLM outage breaking the demo mid-judging.

## Data model

See `backend/standards/models.py` for the authoritative schema (it's short
and commented). In one line each:

- `ProductFamily` — one of the 4 curated product categories + its keyword list.
- `Standard` — one IS number/edition: title, status, amendments, source, `verification` honesty label.
- `StandardEdge` — a typed link from one standard to an allied one (test method, code of practice, …), with a `mandatory` flag.
- `CertificationRule` — one row in a certification scheme's order history (QCO/Hallmarking/ISI), with effective date, enterprise size and state.
- `ParamRule` — one numeric requirement (e.g. "Fe 500D → yield strength ≥ 500 MPa").
- `Feedback` — accept/reject/flag clicks, logged for a future eval story.
- `TestQuery` — the benchmark set (`docs/EVAL_QUERIES.csv` is the human-editable version).
