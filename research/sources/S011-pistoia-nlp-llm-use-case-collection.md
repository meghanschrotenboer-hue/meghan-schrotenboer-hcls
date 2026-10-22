---
id: S011
title: "Pistoia Alliance NLP and LLM Use Case Collection (Supplementary Table S2), with companion paper 'Why do AI projects fail in drug development and pharma?'"
publisher: "Pistoia Alliance · LLM and NLP Use Case Database project; paper in Journal of Computer-Aided Molecular Design"
authors: "Pistoia Alliance project members; paper by Makarov et al."
date_published: 2026-08-06       # paper publication date; dataset projects span 2018–2025
date_added: 2026-10-22
url: "https://link.springer.com/article/10.1007/s10822-026-00894-3"
type: dataset
access: read-in-full              # spreadsheet uploaded and analyzed; paper abstract only
value_chain: [discovery, clinical, manufacturing-supply, regulatory-cmc, commercial-medical, cross-cutting]
intention_matrix: [augment-satisfice, automate-satisfice, augment-optimize]
stack_layer: [models, workflow-ux, governance-trust, commercial-model]
players: [buyer, consortium, services, frontier-labs]
themes: [T1, T2, T3, T4, T6, T8]
signal: high
---

# S011 · Pistoia NLP and LLM Use Case Collection (67 pharma projects)

**Why I saved it:** *(add your line)*

> **Provenance and privacy.** Analyzed from the uploaded workbook *"S2. Pistoia Alliance NLP and LLM use case collection"* (sheet `harmonized_data`, 67 projects, company names redacted). The file name suggests it is **Supplementary Table S2** of the 2026 paper below **[verify]**. Older working tabs in the workbook name companies and individuals. This note reports **aggregates only** and doesn't attribute projects to companies or people. The workbook itself is not stored in this repository.

## TL;DR
- **67 real pharma NLP/LLM projects**, coded by area, maturity (1–10), PoC vs. production, business success, build vs. buy, data issues, and lessons learned. It's the closest thing in the library to **first-party buyer evidence**.
- The companion paper's headline: **project maturity was the strongest predictor of business success; technical factors such as data sources or model types showed no significant association on their own.** High strategic demand for AI collides with low organizational maturity.
- **Half the projects can't say whether they worked.** 38 of 67 record no clear answer on business success.
- **Pharma builds; it rarely buys:** 35 projects recommend build vs. 5 buy.

## What the source says

**Companion paper** ([Springer](https://link.springer.com/article/10.1007/s10822-026-00894-3) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/42563013/)): *Why do AI projects fail in drug development and pharma? Insights from multi-year Pistoia Alliance studies*, Makarov et al., J Comput Aided Mol Des 40, art. 197, published 6 Aug 2026. From the abstract:
- Methods: senior-professional workshops, a global executive survey, and statistical analysis of Pistoia AI/ML use cases.
- "High strategic importance and demand for AI contrast with low organizational maturity, resulting in limited success rates for production deployments."
- "Business success is associated with dimensions of organizational capability maturity, most notably project maturity." Technical factors (data sources, model types) showed no significant association on their own.
- AI projects follow the same success drivers as other complex engineering efforts: **organizational readiness, change management, stakeholder alignment.**
- **Trustworthiness** (reproducibility, explainability, governance) is a limiting factor for adoption, especially in high-risk domains.

**Our aggregate analysis of the workbook (n = 67)**

| Dimension | Finding |
|---|---|
| Technology | 59 classic NLP, **8 LLM (12%)**. Start years cluster 2020–2023 (50 of 67); only 5 began in 2024–25 |
| Stage | 31 PoC · 26 production · 2 in planning · 8 unknown |
| Area | Research 27 · Clinical 11 · Manufacturing 8 · Regulatory compliance 6 · Platform/base 6 · G&A 3 · Social listening 3 · other 3 |
| Maturity (mean, 1–10) | **Regulatory compliance 8.5** (n=6) · Clinical 6.8 (n=11) · Research 5.8 (n=24) · Manufacturing 5.7 (n=7). LLM projects 5.75 (n=8) vs. non-LLM 6.51 (n=53) |
| Business success | 23 yes · 6 no · **38 no clear answer**. Of the 29 with an answer, 79% say yes |
| Business support × success | Business support = yes: 19 succeeded, 3 didn't (known outcomes). Business support = no: 1 succeeded, 2 didn't. Small n; directional |
| Build vs. buy | **35 build · 5 buy** · 27 unknown |
| Tasks | Entity recognition (27 mentions) · relationship extraction (21) · text classification (14) · information extraction (6) · topic modeling (5) · semantic search (3) · summarization and generative (4) |
| Taxonomies/ontologies | **55 of 67 report none or unknown.** Named: MeSH 5, custom synonyms 5, RxNorm 4; MedDRA, UMLS, EMTREE, UniProt 1 each |
| Data | Private 32 · public 18. On-premise 24 · cloud 19 |
| Business goal | "Operational efficiency" dominates (~17 explicit, ~8 more time/cost/productivity) |
| LLM projects | 6 research, 1 clinical, 1 G&A; mostly PoCs (literature classification, document Q&A, patent Q&A, RAG chatbot, plain-language summaries, data-model generation). **None yet records business success** |

**Lessons learned, in practitioners' words** (anonymized)
- Data, next time: the most common answer family is **standardization upstream**: "standardize data," "standardize language," "language harmonization," "uniform standards," "clear definition" (6 of 22 substantive answers).
- One respondent: "standardization at time of data creation would be helpful; splitting of notes into separate, targeted fields at time of data creation would be helpful."
- Another: "Need clear definition of what should be extracted (Target Model)." And: "Unsupervised and rule-based approaches quickly reach their limits."
- Algorithms, next time: LLMs, GPT-4, RAG, or generative models appear in ~8 of 31 answers.
- The workbook's own test of developer support vs. success shows no significant association (χ² ≈ 0.42 vs. 3.84 critical). "Would the business owner do it again" correlates strongly with overall success (r ≈ 0.55–0.79 across tabs).

## Quotable
> "High strategic importance and demand for AI contrast with low organizational maturity, resulting in limited success rates for production deployments." (paper abstract)

> "standardization at time of data creation would be helpful" (anonymized respondent)

## Our read

**This is the strongest evidence in the library, and it reorders the themes.** It's empirical, multi-year, and drawn from buyer-side projects. Its headline (organizational and project maturity beat technical choices) **strongly supports T6** and the adoption half of **T2**.

**It also pushes back on T1, which is healthy.** "Data sources" showed no significant association with success on their own. Two caveats keep T1 alive: (1) *data source* (public vs. private) isn't the same as *data semantics*; and (2) 55 of 67 projects didn't report any taxonomy use, so the dataset can't test whether ontology grounding helps. Meanwhile the practitioners' own top lesson is **standardize upstream** ("FAIR by design," [S010](S010-fair-data-by-design-roche.md)). Net: semantics look like a *necessary foundation*, but **maturity is the binding constraint on success.** Sell them together.

**The measurement gap is an offer.** When 57% of projects can't say whether they delivered business value, no one can make the case for scaling. Value definition and benefits tracking up front (what the FAIR Maturity Matrix places at L3, "value begins to be tracked") is a concrete, fundable service. That's new theme **T8**.

**Regulatory compliance projects are the most mature (8.5).** It's small n, but consistent with **T4**: regulated deadlines force clarity of scope, data, and success criteria.

**Build-dominant buyers favor services over software.** A 7:1 build-to-buy ratio means pharma NLP teams assemble solutions in-house. That points to build partners, accelerators, and components (models and APIs) rather than packaged applications. Caveat: the dataset is mostly pre-generative-AI (2020–2023), and LLM-era buying may shift toward platforms.

**So what for services:** Lead with **project and organizational maturity**, not models: stakeholder alignment, change management, value definition, governance and trustworthiness. The paper is citable proof that this is where success comes from.

**So what for frontier labs:** Model choice isn't what's holding pharma back. Labs that ship **maturity scaffolding** (evaluation harnesses, reproducibility, explainability, governance tooling) and back partner-led change management will convert more PoCs to production. Trustworthiness is the named adoption limiter in high-risk domains.

**Job to be done (pharma head of AI / digital R&D):** When half my AI portfolio can't show business value and PoCs stall before production, I want a repeatable way to raise project maturity and prove value, so I can scale what works and stop funding what doesn't.

| Current state | Future state | Gap (the offer) |
|---|---|---|
| 57% of projects can't state business outcome | Value hypotheses and KPIs defined at intake; benefits tracked | AI value realization office; portfolio benefits tracking |
| PoCs stall; maturity low; trust is the adoption limiter | Stage-gated path to production with governance, reproducibility, explainability | Project maturity framework; trustworthy AI controls |
| Lessons point to upstream standardization, rarely done | Standardization at data creation (FAIR by design) | Data intake standards; controlled vocabularies in workflow |
| Built in-house, one-off | Reusable components and accelerators across projects | Build-partner model with shared accelerators |

## Open questions
- **Get the full paper** (upload the PDF): sample sizes, which maturity dimensions matter most, and whether LLM-era cases differ.
- Is this workbook exactly the paper's Supplementary S2? **[verify]**
- Pistoia's public NLP and LLM Use Case Database (Confluence, updated June 2026) may hold newer LLM-era cases.

## Related
- [S007 · FAIR Maturity Matrix](S007-fair-maturity-matrix.md): L3 "value begins to be tracked"
- [S010 · FAIR data by design](S010-fair-data-by-design-roche.md): practitioners' top lesson, standardize upstream
- [S005 · UXLS Maturity Model](S005-uxls-maturity-model.md): includes a UX metrics and analytics dimension
- [Pistoia LLM and NLP Use Case Database project](https://pistoiaalliance.org/project/llm-nlp-use-case-database/)
