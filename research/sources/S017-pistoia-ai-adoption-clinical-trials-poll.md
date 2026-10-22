---
id: S017
title: "AI Adoption in Clinical Trials: Pistoia Alliance poll (Clinical Trials Technology Congress, London, May 2026)"
publisher: "Pistoia Alliance"
authors: "Pistoia Alliance"
date_published: 2026-06-01       # results published; poll taken late May 2026
date_added: 2026-10-22
url: "https://pistoiaalliance.org/resource-library/ai-adoption-in-clinical-trials/"
type: report
access: partial                   # resource page blocked here; results from Pistoia news and trade coverage
value_chain: [clinical]
intention_matrix: [augment-optimize, augment-satisfice]
stack_layer: [governance-trust, workflow-ux, data-semantics]
players: [buyer, consortium, services]
themes: [T1, T2, T3, T8]
signal: medium
---

# S017 · AI Adoption in Clinical Trials (Pistoia Poll, May 2026)

**Why I saved it:** For any evidence on whether evolv could contribute to something like this as a Snowflake SI. See [A001](../analyses/A001-evolv-pistoia-snowflake-si.md).

> ⚠️ **Partial read.** The resource page and poll PDF were blocked in this environment. The headline (50%) is confirmed by Pistoia's own news release. Other figures come from trade coverage and are marked **[verify]** until checked against the poll PDF.

## TL;DR
- Polled at the **Clinical Trials Technology Congress (London, May 2026)**: **trust and regulatory uncertainty** are the biggest barriers to AI in clinical trials, cited by **half of respondents (50%)**.
- Early value is appearing: **42%** see early signs of ROI and another **23%** expect it but haven't realized it yet **[verify]**.
- Expected impact over 3–5 years: **data cleaning, analysis, and insight generation (48%)**, ahead of patient sourcing and engagement (22%) **[verify]**.

## What the source says
- Poll covered AI and real-world data in clinical trials, including social media listening. ([Pistoia news](https://pistoiaalliance.org/news/half-of-clinical-trial-professionals-cite-trust-and-regulatory-gaps-as-barrier-to-ai-adoption-pistoia-alliance-poll-finds/))
- **Barrier:** trust and regulatory uncertainty, 50%.
- **ROI:** 42% early signs; 23% expected but not realized **[verify]**. ([News-Medical](https://www.news-medical.net/news/20260529/Half-of-clinical-trial-professionals-cite-trust-and-regulatory-gaps-as-barrier-to-AI-adoption-Pistoia-Alliance-poll-finds.aspx))
- **Impact area:** data cleaning, analysis, and insight generation 48%; sourcing and engaging patients 22% **[verify]**.
- The results were shown live to a panel of regulators. Pistoia's president said agencies aren't opposed to AI but want to understand how it's used and ensure adoption is "safe, controlled, and explainable," and called for regulators and pharma to engage early. ([Clinical Leader](https://www.clinicalleader.com/doc/what-pistoia-alliance-s-ai-poll-reveals-about-industry-readiness-and-regulatory-confidence-0001); [Clinical Trials Arena](https://www.clinicaltrialsarena.com/news/clinical-trial-experts-cite-trust-and-regulatory-uncertainty-as-ai-barriers/))

## Our read

**Clinical trials AI is a data problem first, then a trust problem.** The top expected impact is data cleaning, analysis, and insight. That's the data-platform layer, not exotic AI. The top barrier is trust and regulatory clarity, which is governance, explainability, and validation (T3, T2).

**"Safe, controlled, explainable" is a requirements list.** Lineage, audit trails, reproducible pipelines, and access controls on a governed data platform are how you make clinical AI explainable to a regulator. That's where a data-platform SI earns a seat.

**ROI is early, so measurement matters.** 42% see early signs and 23% are still waiting. Without metrics (see [S018](S018-pistoia-london-2026-conference-poll.md): 69% lack them), early signs won't become budget. Another T8 signal.

**So what for services:** A clinical "trusted data foundation for AI" offer: governed trial data products, data quality automation, lineage and audit for explainability, plus value metrics. Lead with the regulator-facing story.

**So what for frontier labs:** Clinical buyers' barrier isn't capability; it's trust and regulatory clarity. Labs need partner-delivered explainability, validation, and regulator engagement to unlock the segment.

**Job to be done (Head of Clinical Data Management):** When we want AI to clean, reconcile, and analyze trial data faster, I want it running on governed, auditable data with explainable outputs, so I can use it in regulated work without inspection risk.

| Current state | Future state | Gap (the offer) |
|---|---|---|
| Trial data cleaning manual and slow | AI-assisted cleaning on a governed clinical data platform | Clinical data products, quality automation |
| Regulators unsure how AI is used | Lineage, audit, and explainability built in | Explainability and audit design; regulator-ready documentation |
| Early ROI anecdotes | Measured cycle-time and quality gains | Value metrics for clinical AI |

## Open questions
- Sample size and respondent mix (sponsors, CROs, vendors)? **[get poll PDF]**
- Is Pistoia launching a clinical-trials AI project or community off the back of this poll?

## Related
- [S018 · London 2026 conference poll](S018-pistoia-london-2026-conference-poll.md)
- [S015 · PGO-T](S015-pistoia-pgo-terminology-bioit-2026.md) and the [Clinical Operations Ontology](https://pistoiaalliance.org/project/clinical-operations-ontology/)
- [A001 · Could evolv contribute as a Snowflake SI?](../analyses/A001-evolv-pistoia-snowflake-si.md)
