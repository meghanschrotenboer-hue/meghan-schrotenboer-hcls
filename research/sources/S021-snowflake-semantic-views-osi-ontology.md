---
id: S021
title: "Snowflake's semantic layer: Semantic Views, Open Semantic Interchange (OSI), and ontology-grounded Cortex agents"
publisher: "Snowflake engineering blog; third-party coverage (Atlan, Prologika, Datus, Dawiso)"
authors: "Snowflake; various"
date_published: 2026                # Semantic View Autopilot GA 2026-02-03; OSI launched 2025-09
date_added: 2026-10-22
url: "https://www.snowflake.com/en/blog/engineering/ontology-grounded-cortex-agents/"
type: article
access: partial                     # pages not fetchable here; details via search excerpts, mostly third-party
value_chain: [cross-cutting]
intention_matrix: [augment-optimize, automate-optimize]
stack_layer: [data-semantics, models]
players: [platform, isv]
themes: [T1, T7, T9]
signal: high
---

# S021 · Snowflake Moves into the Semantic and Ontology Layer

**Why I saved it:** To test whether Pistoia's semantic work and Snowflake's platform overlap. They do. Evidence for [A002](../analyses/A002-pistoia-vs-snowflake-si-world.md).

> ⚠️ **Partial read.** Mostly third-party descriptions via search. Snowflake's own docs and engineering blog weren't fetchable here. Details marked **[verify]**.

## TL;DR
- **Semantic Views** are a native Snowflake object encoding business logic (logical tables, relationships, facts, dimensions, metrics, synonyms, verified queries). **Cortex Analyst** reads them to turn plain-English questions into governed SQL. **Semantic View Autopilot** reached GA on **Feb 3, 2026** **[verify]**.
- **Open Semantic Interchange (OSI):** launched **Sept 2025** by Snowflake, Salesforce, dbt Labs, BlackRock, and RelationalAI as a **vendor-neutral spec for exchanging semantic metadata**. So far it covers tables, relationships, and metrics. **Ontology isn't part of it yet.**
- **Ontology-grounded Cortex agents:** Snowflake's engineering blog describes a knowledge graph built on top of semantic views (node and edge tables, multi-hop traversal). One report cites a **biomedical benchmark** improving from **50.0% → 78.2%** with ontology grounding **[verify]**.

## What the source says
- Semantic views as the "foundation of relational constructs (entities, relations, metrics, dimensions), with a knowledge graph built on top," using KG_NODE and KG_EDGE tables and recursive CTEs for multi-hop traversal. ([Snowflake engineering blog](https://www.snowflake.com/en/blog/engineering/ontology-grounded-cortex-agents/); [Atlan](https://atlan.com/know/ai-agent/ontology/extending-ontology-beyond-snowflake/))
- Biomedical benchmark (22 questions): 50.0% semantic-view baseline → 78.2% with the ontology layer, as reported by Atlan **[verify against Snowflake]**.
- OSI origin, partners, and scope (tables, relationships, metrics; ontology not yet defined). ([Prologika](https://prologika.com/osi/)) Reported renaming of OSI procedures to "Ossie" in Snowflake docs **[verify]**. ([Datus](https://datus.ai/blog/what-is-snowflake-osi/))
- Semantic views and Cortex Analyst definitions. ([Dawiso](https://www.dawiso.com/glossary/snowflake-semantic-views))
- Limit: semantic views are warehouse-bounded and see only Snowflake data. ([Atlan](https://atlan.com/know/ontology-vs-semantic-layer/))

## Our read

**Snowflake is building toward the same conclusion Pistoia reached: AI needs grounded semantics.** PGO-T says "AI requires a common data language" and promises "RAG & LLM grounding" ([S015](S015-pistoia-pgo-terminology-bioit-2026.md)). Snowflake's engineering team shows ontology grounding lifting a *biomedical* agent benchmark. Same thesis, from opposite ends: the consortium defines the meaning; the platform executes on it.

**But they work at different layers, which is why they complement rather than compete.** Your brief's four-capability split ([S019](S019-hcls-data-customer-journey-brief.md)) makes this precise:
- **Snowflake semantic views and OSI = the *semantic (metrics) layer*:** how a business question is calculated.
- **Pistoia PGO-T, IDMP-O, ClinOps = the *ontology/domain model*:** what concepts exist across companies and how they relate.
- Snowflake's ontology-grounded agent pattern is a **container** for domain ontologies. It doesn't supply pharma's ontology. Pistoia's open-licensed standards are natural **content** for it.

**OSI's "no ontology yet" is a gap a life-sciences voice could fill.** OSI is vendor-neutral, like Pistoia. If OSI extends toward ontology, pharma's standards (PGO-T via LinkML, IDMP-O via OWL) are the obvious first domain to test.

**So what for services:** The bridge offer is "load the industry's open standards into Snowflake's semantic constructs." Map PGO-T and IDMP-O concepts into semantic views and KG tables so Cortex agents ground on pharma-standard meaning, not one-off synonyms. That's a credible, evidence-backed specialty for a Snowflake SI with HCLS depth.

**So what for frontier labs:** Models running inside Cortex inherit Snowflake's grounding. Standards-grounded semantic layers make lab models more accurate in regulated pharma questions without fine-tuning.

## Open questions
- Is the biomedical benchmark public? Which ontology did it use? **[verify]**
- OSI roadmap: is ontology on it? Is any life-sciences organization involved?
- Can Snowflake semantic views or KG tables import OWL or LinkML directly, or is mapping manual?

## Related
- [A002](../analyses/A002-pistoia-vs-snowflake-si-world.md) · [S015 · PGO-T](S015-pistoia-pgo-terminology-bioit-2026.md) · [S019 · four-capability split](S019-hcls-data-customer-journey-brief.md) · [S020 · Benchling × Snowflake](S020-benchling-snowflake-direct-data-share.md)
