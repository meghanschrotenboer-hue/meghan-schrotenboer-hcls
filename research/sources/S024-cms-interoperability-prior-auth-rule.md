---
id: S024
title: "CMS Interoperability and Prior Authorization Final Rule (CMS-0057-F)"
publisher: "Centers for Medicare & Medicaid Services"
authors: "CMS"
date_published: 2024-01-17
date_added: 2026-10-23
url: "https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f"
type: standard
access: partial                   # fact sheet via search excerpts
value_chain: [payer, provider]
intention_matrix: [automate-optimize, augment-optimize]
stack_layer: [data-semantics, governance-trust]
players: [buyer]
themes: [T4]
signal: medium
---

# S024 · CMS-0057-F: Payers' Forcing Function (APIs by Jan 2027)

**Why I saved it:** The library's thesis leaned on a pharma deadline (EMA PMS). This is the payer-side equivalent, and payer is one of your three buyer seats. Found during the gap audit ([A003](../analyses/A003-thesis-gap-audit.md)).

## TL;DR
- CMS finalized the rule on **Jan 17, 2024**. Operational provisions generally begin **Jan 1, 2026**; **API development and enhancement requirements generally begin Jan 1, 2027**, with dates varying by payer type.
- Adding prior authorization information (excluding drugs) to the **Patient Access API** is due **Jan 1, 2027**.
- Secondary sources disagree on some API dates. Check the rule text before quoting specifics. **[verify]**

## What the source says
- Impacted payers (Medicare Advantage, Medicaid and CHIP managed care, and QHP issuers on federally facilitated exchanges, among others) must meet API requirements generally beginning Jan 1, 2027; operational provisions generally from Jan 1, 2026. ([CMS fact sheet](https://www.cms.gov/files/document/fact-sheet-cms-interoperability-and-prior-authorization-final-rule-cms-0057-f.pdf); [CMS press release](https://www.cms.gov/newsroom/press-releases/cms-finalizes-rule-expand-access-health-information-and-improve-prior-authorization-process))

## Our read

**Same pattern as EMA PMS and BCBS 239 ([S016](S016-bcbs-239-risk-data-aggregation.md)):** a regulator mandates standardized, exchangeable data (here, FHIR-based APIs), a deadline creates budget (T4), and the semantic and data-quality work underneath becomes the durable services market. The deadline is **~14 months away**, so for payers this is active budget now, not a post-deadline reuse story.

**Rebalances the thesis toward your strengths.** Most library evidence is pharma R&D. Payer and provider are where you've personally been the buyer (Priority Health, Corewell). A payer version of the thesis (prior auth data, FHIR APIs, governed data on Snowflake, AI-assisted prior auth with escalation) may be faster to sell than the pharma ontology story.

## Open questions
- Exact API dates by payer type (from the rule text).
- Which payers run their interoperability and analytics data on Snowflake?
- How far along are payers, and where are they stuck (data quality, mapping, workflow)?

## Related
- [S016 · BCBS 239](S016-bcbs-239-risk-data-aggregation.md) · [S003 · EMA PMS](S003-pistoia-idmp-o-info-sheet.md) · [A003](../analyses/A003-thesis-gap-audit.md)
