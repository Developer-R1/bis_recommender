# Data provenance — read this before quoting any number from this MVP in a real tender

This is a hackathon prototype. **None of the curated data here should be
treated as a substitute for the official BIS Manak portal or the actual
gazette notification.** Every row in the database carries a `verification`
field:

- `official_verified` — checked directly against an official BIS/gazette
  document. (This MVP currently has none marked this way — see below.)
- `public_data` — sourced from public secondary references (industry
  compliance blogs, engineering-reference sites, news coverage of a QCO).
  Directionally correct, cross-checked against 2–3 sources where possible,
  but **not** independently confirmed against the primary gazette text.
  **This is the label on every row seeded for this MVP.**
- `demo` — placeholder, not to be trusted at all (not currently used, but
  the field exists for future test fixtures).

## Why this matters for the pitch

Being explicit about `public_data` vs `official_verified` is itself the
trust-layer story: a system that quietly presents secondary-source figures
as gazette-certain is worse than one that shows its homework. Every standard
card and certification card in the UI displays this label and a source
link, so a judge (or an officer) can click through and check.

## Specific things that are genuinely uncertain in this seed data

- **IS 1660:2024 QCO, 2026 order, small-enterprise effective date**: not
  confirmed from the sources reviewed at seed time (27 Sep 2026). The engine
  deliberately returns `date_unconfirmed_verify_source` with a caveat for
  this case rather than guessing a date. Confirmed bookends: large
  enterprises 1 Oct 2026, micro enterprises 1 Apr 2027.
- **IS 1786:2008 latest amendment number**: public summaries mention
  amendments "through 2024" without a definitive latest amendment number —
  verify on the BIS Manak portal before citing an amendment number in a
  real tender.
- **Allied/normative standard lists** (e.g. which exact test-method
  standards IS 1660:2024 references) are **not seeded** for the aluminium
  family, specifically because they were not independently confirmed —
  we chose to show nothing rather than fabricate a plausible-looking list.
  This is intentional and worth pointing out in a demo: the absence of a
  claim is safer than an unverified one.

## Sources used (by family)

**TMT / reinforcement steel (IS 1786:2008)**
- https://services.bis.gov.in/tmp/SR1786.pdf (BIS preview PDF)
- https://infralens.in/code/IS-1786, https://infralens.in/term/yield-strength, https://infralens.in/term/fy
- https://lims.bis.gov.in/home_lab_scope/573

**Cement (IS 269:2015)**
- https://infralens.in/code/IS-269-2015, https://infralens.in/code/IS-269

**Gold hallmarking (IS 1417:2016)**
- https://services.bis.gov.in/php/BIS_2.0/BISBlog/?p=560
- https://en.vikaspedia.in/viewcontent/social-welfare/social-awareness/consumer-education/hallmarking-of-gold-jewellery-consumer-education-1/hallmarking-of-gold-jewellery
- https://www.tribuneindia.com/news/business/sale-of-gold-jewellery-hallmarked-without-6-digit-code-to-be-banned-after-march-31-14980

**Aluminium utensils QCO (IS 1660:2024)**
- https://www.alcircle.com/news/a-fresh-qco-puts-aluminium-cans-and-cookware-under-the-compliance-spotlight-116959 (2026 order)
- https://www.intertek.com/products-retail/insight-bulletins/2026/1518-india-published-the-cookware-utensils-and-cans-for-foods-and-beverages-quality-control-order-2026/ (2026 order detail)
- https://alephindia.in/bis-qco-for-the-wrought-aluminium-utensils.php (2025 extension order)
- https://absoluteveritas.com/bis-qco-for-wrought-aluminium-utensils/ (2024 order, MSME phase-in dates)

## Before the finale

Re-verify every row against the BIS Manak portal / DPIIT gazette directly
and flip `verification` to `official_verified` as you confirm each one.
That flip, visible in the UI, is a good thing to show a judge as evidence
of a real verification pass rather than a claim.
