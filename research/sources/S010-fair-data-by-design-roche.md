---
id: S010
title: "FAIR data by design (Roche Dataset Portal), Pistoia FAIR Toolkit use case"
publisher: "Pistoia Alliance FAIR Toolkit"
authors: "Roche [verify named authors]"
date_published: 2024-04          # approximate; search listed the page ~912 days old [verify]
date_added: 2026-10-22
url: "https://fairtoolkit.pistoiaalliance.org/use-cases/fair-data-by-design/"
type: report
access: partial                   # fairtoolkit.pistoiaalliance.org blocked here; details from search excerpts and a related Roche deck
value_chain: [discovery, clinical]
intention_matrix: [automate-optimize]
stack_layer: [data-semantics, workflow-ux, governance-trust]
players: [buyer, consortium, services]
themes: [T1, T4, T5, T7]
signal: medium
---

# S010 · FAIR Data by Design: Roche Dataset Portal (case study)

**Why I saved it:** This case study. *(expand in your words)*

> ⚠️ **Partial read.** fairtoolkit.pistoiaalliance.org was blocked in this environment on 2026-10-22. Details come from search excerpts of the case and a related Roche presentation. Note that this is Roche's own write-up, so it describes intended design rather than independent evaluation.

## TL;DR
- Roche built the **Roche Dataset Portal (RDP)**: one entry point for researchers to discover and access datasets instead of searching multiple interfaces.
- The design goal is **full FAIR compliance across the portal application, its API, and the datasets it exposes**, enabling "**transformationless data integration**" and "**automated FAIR assessment**."
- Datasets can be **automatically tagged with rich metadata**. FAIRness is measured with maturity indicators, reportedly including a **five-star rating** **[verify]**.

## What the source says
- **Problem:** researchers searched multiple interfaces to find and access data.
- **Solution:** RDP, a single portal with automated rich metadata tagging; FAIR compliance built into the application, API, and datasets.
- **Measurement:** FAIR maturity indicators, including a five-star rating. **[verify]**
- **Related Roche material:** a Roche presentation ("Data First!", Martin Romacker and Nick Perry, OntoCommons, 2023) describes "no more transformation" between certain data layers, with FAIRification only in specific layers, and "FAIR by Design: Reference by Global Unique Persistent & Resolvable Identifiers (GUPRI)." It also lists a FAIR assessment and FAIR maturity component. ([deck PDF](https://ontocommons.eu/sites/default/files/2023-06/Martin%20Romacker_Nick%20Perry_FAIR%20Principles%20implementation%20at%20Roche.pdf))
- **Other Roche toolkit cases:** [FAIRification of clinical trial data](https://fairtoolkit.pistoiaalliance.org/use-cases/fairification-of-clinical-trial-data-roche/) (studies mapped to FAIR form and published in a DCAT-annotated catalogue) and [prospective FAIRification on the EDISON platform](https://fairtoolkit.pistoiaalliance.org/use-cases/prospective-fairification-of-data-on-the-edison-platform-roche/) (data blueprints and early quality checks).
- **Corroborating principle:** a separate Zenodo document on FAIRification lessons concludes that FAIR-by-design is highly preferred over FAIRification after data generation. ([Zenodo](https://zenodo.org/record/6799039))

## Our read

**"By design" beats "after the fact," and that's an economic claim.** The FAIR Maturity Matrix ([S007](S007-fair-maturity-matrix.md)) puts the shift to FAIR-from-the-start at L3, where organizations "begin to reduce efforts required by retrospective FAIRification." Roche's progression (retrospective clinical-trial FAIRification → prospective EDISON blueprints → FAIR by design in RDP) is a real-world walk up that ladder. It's the same logic as IDMP-O's "interoperability by design" ([S002](S002-pistoia-idmp-o-github.md)).

**Automated FAIR assessment is a machine-checkable acceptance test.** Like IDMP-O's SHACL shapes, automated FAIR scoring lets machines verify data readiness without human review, a precondition for agents consuming data autonomously (T7).

**Reference account signal.** Roche publishes repeatedly through Pistoia's toolkit. That's a public, high-maturity exemplar you can cite with buyers ("here's what L3+ looks like at a top-10 pharma") and a sign that Roche's data leadership is active in the precompetitive community.

**So what for services:** Sell "by design" over "remediation." For clients still FAIRifying retrospectively, the offer is a blueprint-first data intake (identifiers, metadata, quality checks at the point of creation) plus an automated FAIR scorecard. That's less glamorous than AI, but it's what makes AI cheap later.

**So what for frontier labs:** Single, FAIR-compliant data portals with APIs are the ideal integration surface for agents. Labs should prioritize connectors to catalog and portal layers like this rather than to the many raw sources behind them.

**Job to be done (R&D data platform lead):** When every new study or dataset needs costly cleanup before anyone can reuse it, I want data to be FAIR from the moment it's created, so I can stop paying the remediation tax and make reuse (and AI) the default.

| Current state | Future state | Gap (the offer) |
|---|---|---|
| Retrospective FAIRification, project by project | FAIR by design: blueprints, identifiers, and metadata at creation | Data intake blueprint design; identifier policy |
| Many portals and interfaces | One FAIR-compliant catalog and API | Catalog/portal architecture; agent-ready API layer |
| Manual FAIR reviews | Automated FAIR assessment scorecards | FAIR scorecard automation |

## Open questions
- What were the measured outcomes (time to find data, reuse rates, cost avoided)? Not visible in the excerpts.
- Is RDP exposed to AI agents or LLM-based search today? **[research: recent Roche talks]**

## Related
- [S007 · FAIR Maturity Matrix](S007-fair-maturity-matrix.md): L3 business value, by-design vs. retrospective
- [S002 · IDMP-O](S002-pistoia-idmp-o-github.md): interoperability by design
