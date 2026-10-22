---
id: S002
title: "Pistoia Alliance Ontologies: IDMP-O (GitHub repository and release notes)"
publisher: "Pistoia Alliance; maintenance by Accurids"
authors: "IDMP-O project team; recent releases engineered by Accurids"
date_published: 2026-10-10       # latest release noted (1.8.0); repository HEAD 2026-10-13
date_added: 2026-10-22
url: "https://github.com/Pistoia-Alliance-Inc/Pistoia-Alliance-Ontologies/tree/main/IDMP-O"
type: dataset
access: read-in-full              # README and release notes 0.1.0 → 1.8.0
value_chain: [regulatory-cmc, manufacturing-supply]
intention_matrix: [automate-optimize]
stack_layer: [data-semantics, governance-trust]
players: [consortium, buyer, isv, services]
themes: [T1, T3, T4, T5]
signal: high
---

# S002 · IDMP Ontology (IDMP-O): The Repository

**Why I saved it:** *(add your line)*

## TL;DR
- IDMP-O is a **vendor-neutral, machine-readable model of the ISO IDMP standards** for identifying medicinal products, built so product data is "interoperable by design" rather than reconciled after the fact.
- It is moving from standards project to **operational infrastructure**: quarterly releases since 2022, a v1.8.0 release on 2026-10-10, real use cases (EMA PMS, cross-jurisdiction reporting, batch tracking), and automated validation.
- The **staged access model** (funders first, members six months later, public one year later) makes membership a real information advantage.

## What the source says

**Purpose and scope**
- ISO IDMP aligns industry on product and substance data, driven by regulation. The project argues IDMP's potential depends on *self-describing data* to counter "diverse, non-standard IDMP implementations," so it adds an ontology for "deep, semantic interoperability based on FAIR principles."
- Stated payoff for early adopters: "competitive advantage in innovation, drug safety and overall operational efficiency."
- Scope: ISO 11238 (substances), 11239 (dose forms, units of presentation, routes, packaging), 11240 (units of measurement), 11615 (medicinal products), 11616 (pharmaceutical products), plus ISO 21090 (harmonized data types).
- Intent: submit the finished ontology to ISO, directly or via the ISO PAS process through the Object Management Group (OMG).
- Positioned as "solution agnostic technology for the data fabric" across biomedical data environments.

**Access model (from the release notes)**
- "Funding members receive each release immediately. All Pistoia Alliance members receive access six months later, and the release becomes publicly available in this GitHub repository one year after its initial release."
- As of 2026-10-22, the public folder holds release artifacts for 1.2.0, 1.3.0, and 1.4.0. Release notes run through 1.8.0.

**Release trajectory (a roadmap of buyer use cases)**

| Release | Date | Focus |
|---|---|---|
| 0.1.0 MVP | 2022-10-03 | First release |
| 1.0.0 | 2024-01-05 | Substances (11238) and medicinal products (11615) coverage; real-world examples; document/label linking |
| 1.1.0 | 2024-04-10 | Biologics (organisms, herbal taxonomy); indications, contraindications, population |
| 1.2.0 | 2024-07-12 | Simplification; groundwork for the **EMA PMS Data Alignment PoC** |
| 1.3.0 | 2025-02-18 (Q3 2024 work) | Marketing and manufacturing authorizations for the **EMA SPOR PMS** use case |
| 1.4.0 | 2025-02-24 (Q4 2024 work) | Supply chain and manufacturing; **batch tracking**; notes the need to map "across complex ERP, regulatory reporting and other systems" |
| 1.5.0 | 2025-12-12 | Two use cases "driven by steering committee members with real data": **cross-jurisdiction regulatory reporting** and **multi-manufacturer batch tracking** |
| 1.6.0 | 2026-05-12 | Mapping to BFO, FIBO, IOF, and Pistoia's CMC process ontology |
| 1.7.0 | 2026-07-10 | **Packaging and pack size** per EMA/ISO guidance; units of presentation mapped to **EMA SPOR RMS** |
| 1.8.0 | 2026-10-10 | Lean, self-contained Core; licensing/metadata per Pistoia Ontology Design Principles; change reports |

**1.8.0 by the numbers**
- Core artifact holds **351 external terms**, down from **~4,600** in 1.7.0, in one self-contained file checked for consistency by a reasoner (Pellet).
- **548 classes**, **256 object properties**, **98 datatype properties**, **1,630 individuals**, **78 modules**; 874 active classes and properties now carry creator metadata.
- Three deliverables: **Core**, **Full**, **Examples**, plus an automated change report against the prior release.
- Validation: **SHACL shapes**, **competency questions**, hygiene queries, and a retention check: "The build fails when a released term disappears."
- Worked examples reference real molecules (Amlodipine, Terlipressin, Linagliptin).

## Quotable
> "Realization of the full potential of IDMP depends on self-describing data to counteract diverse, non-standard IDMP implementations."

> "...enable early adopters to gain a competitive advantage in innovation, drug safety and overall operational efficiency."

## Our read

**The signal underneath the release notes:** the use-case sequence (EMA PMS → cross-jurisdiction reporting → batch tracking → packaging) shows where pharma regulatory and supply chain teams are spending. The engineering focus (lean core, SHACL, change reports, retention checks) is what you build when people run this in production pipelines, not slide decks.

**Why this matters for AI specifically:** SHACL shapes and competency questions are *machine-checkable acceptance criteria*. That is the missing ingredient for moving regulated data work from **augment** to **automate** on the Intention Matrix ([S004](S004-ai-intention-matrix.md)). An LLM that maps source-system product data into IDMP-O can be checked by rules, not just by reviewers. The ontology also gives agents a shared vocabulary to ground on, which cuts ambiguity in a domain where "pack size" alone needs four worked examples.

**So what for services:**
- Implementation work is real and specific: mapping RIM, ERP, MES, and labeling systems into IDMP-O; standing up knowledge graphs; building validation pipelines; designing data stewardship operating models.
- The ontology is free; the integration, mapping, governance, and change management are not. That is a classic services wedge.
- Pairs naturally with Snowflake-style data platforms: governed product master data as the foundation for regulatory AI.

**So what for frontier labs:**
- Ontologies like IDMP-O are high-value **grounding context** for agents doing regulatory work (e.g., exposed as tools or knowledge sources). Labs that ship reference integrations with industry standards earn credibility with regulatory buyers.
- Precompetitive standards are where labs can show up as neutral contributors instead of vendors.

**Job to be done (Head of Regulatory Ops / RIM):** When regulators require structured, standardized product data across jurisdictions, I want one semantic model my systems and vendors all map to, so I can meet each deadline once and reuse the data instead of rebuilding it per submission.

| Current state | Future state | Gap (the offer) |
|---|---|---|
| Product data duplicated across RIM, ERP, labeling; each regulator's format handled as a one-off project | One governed product knowledge graph aligned to IDMP-O feeding every submission | Source-to-ontology mapping, validation pipeline, data ownership model |
| Validation by manual review | Rule-based validation (SHACL / competency questions) with human review by exception | Automated QC design; AI-assisted mapping with rule-based acceptance |
| Compliance treated as cost | Same data reused for supply chain traceability, safety, and AI | Value-reuse roadmap and business case |

## Open questions
- Which of the "more than 10" adopting companies ([S003](S003-pistoia-idmp-o-info-sheet.md)) are public, and who owns IDMP-O inside them (regulatory, data office, or IT)?
- Is anyone publicly pairing IDMP-O with LLMs or agents yet? Pistoia's event title "Navigating the New IDMP Era: Data Quality, Ontologies, and AI-Powered Compliance" suggests the narrative is forming. **[find recording/slides]**
- How does IDMP-O relate to HL7 FHIR medication resources used for EU/US exchange?

## Related
- [S003 · IDMP-O Information Sheet and June 2026 announcement](S003-pistoia-idmp-o-info-sheet.md)
- [S004 · AI Intention Matrix](S004-ai-intention-matrix.md): rule-based acceptance enables automate + optimize
