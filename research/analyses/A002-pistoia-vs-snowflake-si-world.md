# A002 · Is the Pistoia research mutually exclusive from the Snowflake and SI world?

*Question from 2026-10-22, prompted by throughlines you noticed (IQVIA, Benchling). Evidence: S002, S007, S011, S014, S015, S018, S019, S020, S021, S022. v1.*

## Bottom line

**No. They aren't mutually exclusive; they're different layers of the same stack, and they're converging.**

- **Pistoia defines what pharma data *means*** (PGO-T, IDMP-O, ClinOps, FAIR maturity). It's precompetitive, vendor-neutral, and open-licensed.
- **Snowflake is where that data increasingly *lives, is shared, and is used by AI*** (data sharing, Marketplace, semantic views, Cortex agents).
- **SIs are *how* the meaning gets applied** to the data on the platform.

The same companies sit in all three worlds. **Accenture** is a Pistoia member *and* Snowflake's 2026 HCLS Services Partner of the Year. **Cognizant**, **ZS**, and **EPAM** are active in Pistoia and in Snowflake's partner ecosystem. **Benchling** and **IQVIA** take part in Pistoia *and* pipe their data into customers' Snowflake accounts.

**What keeps them structurally separate:** Pistoia won't endorse a platform, and Snowflake isn't a member (no evidence found). The connection runs **through members, data, and standards**, not through a formal partnership. That gap is exactly where an SI adds value.

**Confidence: high** on "not mutually exclusive" (direct evidence of shared companies and converging technical direction). **Medium** on "white space for evolv" (large SIs already straddle both; no public example yet of Pistoia standards loaded into Snowflake semantic constructs).

---

## The stack: who does what

Using the four-capability split from your brief ([S019](../sources/S019-hcls-data-customer-journey-brief.md)), plus maturity:

| Capability | What Pistoia contributes | What Snowflake contributes | Who bridges today |
|---|---|---|---|
| **Integration** (combine records) | Not its role | Data sharing, Marketplace, connectors: **Benchling Direct Data Share** ([S020](../sources/S020-benchling-snowflake-direct-data-share.md)); **IQVIA OneKey** on Marketplace ([S022](../sources/S022-snowflake-hcls-partner-ecosystem.md)) | Data vendors, SIs |
| **Identity / MDM** (which real entity?) | Identifiers: **IDMP-O** for products ([S002](../sources/S002-pistoia-idmp-o-github.md)); **PGO-T URIs** for core concepts ([S015](../sources/S015-pistoia-pgo-terminology-bioit-2026.md)) | Tables and governance; partner MDM products | IQVIA DaaS+, Accurids ([S014](../sources/S014-accurids.md)) |
| **Semantic layer** (how a metric is calculated) | Not its role | **Semantic Views**, Cortex Analyst, **Open Semantic Interchange** ([S021](../sources/S021-snowflake-semantic-views-osi-ontology.md)) | SIs |
| **Ontology / domain model** (what concepts exist and relate) | **PGO-T, IDMP-O, ClinOps, CMC-PO**: open licenses, pharma-funded | A **container**: knowledge-graph pattern for **ontology-grounded Cortex agents**, with a biomedical benchmark gain reported **[verify]** ([S021](../sources/S021-snowflake-semantic-views-osi-ontology.md)) | **No public example found → white space** |
| **Maturity and value** | FAIR Maturity Matrix, UXLS, use-case database, polls ([S007](../sources/S007-fair-maturity-matrix.md), [S011](../sources/S011-pistoia-nlp-llm-use-case-collection.md), [S018](../sources/S018-pistoia-london-2026-conference-poll.md)) | Not its role | SIs (Thoughtworks sponsored a poll) |

**Read across the rows:** Pistoia and Snowflake rarely do the same job. Where they meet (the ontology row), Pistoia supplies **content** and Snowflake supplies a **container**. That's complementarity, not competition.

## The throughlines (evidence)

| Company | In the Pistoia world | In the Snowflake world |
|---|---|---|
| **Accenture** | Member | **2026 HCLS Services Partner of the Year** |
| **Cognizant** | Member | **2025 Global Data Cloud Services Implementation Partner of the Year** |
| **ZS** | CMC ontology workshop host; Phase 3 supporter | **Premier** partner |
| **EPAM** | Member | Snowflake Summit 2026 sponsor |
| **IQVIA** | FAIR Maturity Matrix contributor | Marketplace data provider; 2022 Marketplace HCLS Partner of the Year; you note it's a customer |
| **Benchling** | Member | **Direct Data Share** with Snowflake (Oct 2026) |
| **Sanofi** | Membership not confirmed | Chose Snowflake for AI-powered drug development (June 2026) |
| **Snowflake** | **No evidence of participation** | — |

Full sourcing in [S022](../sources/S022-snowflake-hcls-partner-ecosystem.md).

## The convergence (same thesis, opposite ends)

- **Pistoia:** "AI requires a common data language"; PGO-T enables "RAG & LLM grounding" that "reduces hallucination risk" ([S015](../sources/S015-pistoia-pgo-terminology-bioit-2026.md)).
- **Snowflake:** ontology-grounded Cortex agents; a reported jump on a biomedical benchmark from adding an ontology layer **[verify]** ([S021](../sources/S021-snowflake-semantic-views-osi-ontology.md)).
- **Pistoia's own example** is a data-sharing scenario: "A CRO delivers a data product tagged with PGO-T URIs… the receiving pharma company's knowledge graph ingests it directly." Snowflake's sharing and Marketplace are built for data-product exchange between organizations.

## Where they genuinely don't overlap (be precise about this)

1. **Pistoia won't pick platforms.** Anything presented inside Pistoia must be platform-neutral (see [A001](A001-evolv-pistoia-snowflake-si.md)).
2. **Snowflake's semantic views are a metrics layer, not a domain ontology.** They're also warehouse-bounded. Calling a semantic view an "ontology" will lose credibility with Pistoia's ontologists.
3. **Ontologies are authored elsewhere** (OWL, LinkML). Snowflake is where they're *applied*, not *written*.
4. **OSI doesn't cover ontology yet.** The vendor-neutral semantic standard and the pharma ontologies haven't met.

## What it means for evolv

**The opportunity is the bridge:** taking pharma's open standards (PGO-T, IDMP-O, ClinOps) and making them work inside Snowflake, in semantic views, knowledge-graph tables, and shared data products, so Cortex agents and analytics ground on industry-standard meaning.

| Current state | Future state | Gap (the offer) |
|---|---|---|
| Benchling, IQVIA, and other vendor data lands in Snowflake with each vendor's own vocabulary | Shared data tagged to PGO-T / IDMP-O identifiers on arrival | Standards mapping for shared data products |
| Semantic views built per project with local synonyms | Semantic views and KG tables seeded from open pharma standards | "Standards-grounded semantic layer" accelerator |
| Cortex agents grounded on one company's terms | Agents grounded on industry-standard concepts (portable across partners and CROs) | Ontology-grounded agent pattern for HCLS |
| Pistoia work and Snowflake work in separate conversations | One story: "industry meaning, on your platform" | Positioning and a neutral reference pattern |

**The caution:** Accenture and Cognizant already straddle both worlds. evolv wins by being **narrower and deeper**: buyer-side HCLS experience, hands-on Snowflake delivery, and real fluency in the standards. Lead with one concrete, timely use case (e.g., Benchling Direct Data Share → PGO-T-tagged R&D data → grounded Cortex agent) rather than a broad transformation pitch.

**How to say it:**
> "Pistoia defines what pharma data means. Snowflake is where that data now lives and where AI runs on it. We connect the two: industry-standard meaning, applied on the platform you already use."

## What would change this answer
- Snowflake joins Pistoia or launches an HCLS ontology offering itself (the bridge becomes a product, and SI value shifts to implementation).
- Accenture or Cognizant publishes a PGO-T / IDMP-O-on-Snowflake accelerator first (white space closes).
- Pharma buyers say standards and platform decisions are made by separate teams that don't talk (the bridge is real but harder to sell).

## Next steps
1. **Verify the two weakest links:** Snowflake's ontology-grounded agent benchmark (primary blog), and the current IQVIA–Snowflake relationship.
2. **Test the bridge with one Benchling + Snowflake customer:** do they need shared identifiers when joining Benchling data with other domains? (Discovery question from [S019](../sources/S019-hcls-data-customer-journey-brief.md): "Can two results be compared scientifically after accounting for method, sample lineage, units, and experimental conditions?")
3. **Ask your Snowflake HCLS contacts** whether anyone has loaded PGO-T or IDMP-O into semantic views or Cortex knowledge graphs.
4. **Prototype quietly:** map the 17 PGO-T Phase 1 concepts into a Snowflake semantic view and KG tables. It's small, uses open-licensed content, and becomes the demo for both worlds.
