# Lenses: How Every Source Gets Tagged

Every source note is tagged with the same five lenses. That consistency is what turns a pile of links into themes: once 30 sources carry the same tags, patterns show up on their own (for example, "every high-signal source this month sits in Regulatory/CMC and the Data & Semantics layer").

---

## Lens 1 · AI Intention Matrix (augment ↔ automate × satisfice ↔ optimize)

*Origin: [S004](sources/S004-ai-intention-matrix.md), Richard Yang / UX Collective, May 2025.*

Two questions for any AI use case:

1. **How involved does the human stay?** *Augmentation* (human in the loop, AI assists) ↔ *Automation* (AI acts, human audits by exception).
2. **How good does the output need to be?** *Satisficing* (good enough to move the work forward) ↔ *Optimizing* (best possible, because the cost of error is high).

Satisficing is Herbert Simon's decision-theory term (satisfy + suffice): stop searching once an option clears the bar. Yang's point is economic as much as experiential. Defaulting every feature to full-automation, maximum-precision mode burns tokens and compute on outputs users neither need nor trust.

### HCLS overlay (our read, not from the source)

| Quadrant | Plain-English job | HCLS examples | Who tends to capture the value |
|---|---|---|---|
| **Augment + Optimize** · *High-stakes co-pilot* | "Help me make a better decision I still own." | Clinical decision support, PV case causality review, regulatory submission QC, protocol design | **Services-heavy.** Validation, SME-in-the-loop design, change management, audit trail |
| **Augment + Satisfice** · *Everyday assistant* | "Get me to a decent first draft or answer, fast." | Literature triage, internal knowledge search, med-info response drafts, AI-enabled BI Q&A | **Lab/product-led.** Services play is adoption and enablement |
| **Automate + Optimize** · *Autonomous precision* | "Do it exactly right, every time, and prove it." | IDMP/SPOR data normalization, controlled-vocabulary mapping, batch genealogy reconciliation | **Joint.** Needs machine-checkable rules (ontologies, SHACL, competency questions) before anyone trusts it |
| **Automate + Satisfice** · *Autonomous utility* | "Just handle it; I'll spot-check." | Document classification and routing, metadata enrichment, transcription cleanup, de-duplication | **Product-led.** Low services margin unless bundled |

> **Data nuance (from [S007](sources/S007-fair-maturity-matrix.md)):** the FAIR Maturity Matrix applies the same idea to data with **"FAIR Enough"**: not all data needs to be fully FAIR. Match data investment to the quadrant. *Satisfice* quadrants rarely justify deep interoperability work; *automate + optimize* almost always needs it.

> **Regulated-industry nuance:** in GxP and clinical settings, "satisficing" never means sloppy. "Good enough" has to be a *documented acceptance threshold tied to intended use*. That threshold is itself a deliverable, and often a services deliverable.

> **Runtime nuance (from [S006](sources/S006-journey-mapping-ai-agents.md)):** the quadrant isn't always fixed per use case. An agent can run in *automate* mode until confidence or risk crosses a threshold, then escalate to a human, which moves that one decision into *augment* mode. Escalation rules are where the quadrant boundary actually lives.

Tag values: `augment-optimize` · `augment-satisfice` · `automate-optimize` · `automate-satisfice`

---

## Lens 2 · Value chain stage

| Tag | Covers |
|---|---|
| `discovery` | Target ID, chemistry, biology, preclinical, lab informatics |
| `clinical` | Trial design, site/patient ops, clinical data management, biostats |
| `regulatory-cmc` | Submissions, RIM, IDMP/SPOR, labeling, CMC, quality, PV |
| `manufacturing-supply` | Batch/lot, MES, serialization, supply chain, distribution |
| `commercial-medical` | Field, market access, HEOR, medical affairs, med info |
| `provider` | Health systems: clinical ops, revenue cycle, workforce, CDS |
| `payer` | Plans: member experience, UM/prior auth, risk adjustment, cost transparency |
| `cross-cutting` | Applies across the chain (e.g., UX practice, data governance) |

---

## Lens 3 · Stack layer

Where in the stack does the source's insight sit?

`data-semantics` → `models` → `workflow-ux` → `governance-trust` → `commercial-model`

The early hypothesis worth testing: in HCLS, PMF is gated **above** and **below** the model layer, by governed data on one side and workflow/role design on the other. Models are increasingly table stakes.

---

## Lens 4 · Player

Whose strategy does this source inform most?

`services` (SIs, consultancies, boutiques) · `frontier-labs` (model builders and their enterprise/vertical arms) · `isv` (vertical software) · `consortium` (Pistoia, CDISC, HL7, etc.) · `buyer` (pharma, provider, payer)

---

## Lens 5 · Buyer and job to be done

Name the persona and their job in one line: *"When [situation], I want to [motivation], so I can [outcome]."*

Common HCLS personas to reuse:
- **CDO / CDAO / Chief Analytics Officer:** owns data as an asset; measured on reuse and trust
- **Head of Regulatory Operations / RIM:** owns submission readiness; measured on deadlines and findings
- **R&D IT / Scientific Informatics lead:** owns the lab and research stack; measured on scientist productivity
- **Quality / CSV lead:** owns validation; measured on audit outcomes
- **UX / Digital Experience lead:** owns adoption; measured on usage and satisfaction
- **CMIO / CNIO (provider):** owns clinical workflow; measured on safety, burden, outcomes
- **VP Member Experience / Product (payer):** owns the digital front door; measured on engagement, cost, stars

---

## Signal strength

| Tag | Meaning |
|---|---|
| `high` | Primary source, specific data, directly informs a PMF hypothesis |
| `medium` | Credible and relevant, but secondary, directional, or adjacent |
| `low` | Interesting context; keep for color, don't build on it alone |
