# From connected data to dependable decisions
## Healthcare and life sciences customer journey: evidence for semantic and master-data needs

Prepared October 22, 2026. Source window: January 1, 2025–October 22, 2026.

## Executive perspective

The most useful buying signal is a decision the enterprise cannot make consistently: how much it spends on the same item across facilities; whether an alternative product is appropriate; which operating activities explain margin; or whether evidence from different laboratories can be compared.

The cases below support three distinct investment needs. CHS describes establishing an enterprise item master. Piramal explicitly embeds MDM in business transformation. The Pistoia Alliance identifies inconsistent definitions of core concepts even within companies. These are related needs, but they should not be collapsed into a generic data-quality problem. [1–4, 12]

A second pattern is that integration is an intermediate achievement. Pacesetter already had a functioning financial warehouse but needed a broader clinical and operational model. Medline connects supply visibility to substitution and approval workflows. Bayer describes harmonization of laboratory and partner data for scientific use. The next investment depends on the decision that remains difficult after data is connected. [6–8]

These examples establish customer problems, investments, and reported progress. They do not establish that every named organization has an unresolved gap today, or that buying a separate ontology or MDM platform would be appropriate. Several are examples of needs already being addressed.

## What the three capabilities mean in this brief

| Capability | Question it answers | Example | Boundary |
|---|---|---|---|
| Integration | Can we access and combine the relevant records? | Move acquisition-era ERP and EHR data into a common environment. | Connecting records does not establish their identity or meaning. |
| Master data management | Which real entity is this, and which attributes and relationships are authoritative? | Resolve supplier aliases, product identifiers, sites, legal entities, and organizational hierarchies. | MDM includes stewardship and lifecycle controls; it is more than deduplication. |
| Semantic layer | How should a business question be calculated consistently? | Define worked hours, net revenue, contract compliance, or service-line contribution margin, including grain and time basis. | A shared metric does not repair incorrect source identities. |
| Ontology/domain model | What concepts exist, how are they related, and what contextual rules matter? | Relate product to procedure, approved substitute, facility, contract, and clinical restriction. | An ontology is broader than a BI metrics layer. A formal knowledge graph is not required for every problem. |

These are working analytical distinctions, not claims that the cited implementations use a particular architecture. The Pistoia project provides direct contemporary evidence for the core-concept and definition problem. [12]

## The data customer journey

The following is a synthesis of the cases, not a published maturity standard or a claim that companies move through fixed stages. Different business domains can occupy different stages simultaneously.

| Customer situation | Business experience | IT/data experience | What must become dependable | Evidence anchor |
|---|---|---|---|---|
| 1. Local processes work; enterprise questions do not | Local leaders can explain their own numbers, but corporate comparison takes reconciliation. | Acquired systems, different schemas, incomplete cross-functional coverage. | Access, lineage, and an explicit map of sources and owners. | Pacesetter [6]; Advocate [5] |
| 2. The enterprise consolidates | Finance wants a faster close; procurement wants total purchasing visibility. | ERP/EHR consolidation exposes conflicting identifiers and hierarchies. | Entity identity, reference data, effective dates, accountable stewardship. | CHS [1–2]; Piramal [3] |
| 3. Connected records still require interpretation | Teams dispute what a result means or whether two observations are comparable. | Repeated mappings, inconsistent concepts, context lost at system boundaries. | Shared definitions, relationships, units, time basis, and permitted variation. | Aurobindo [4]; Pistoia [12] |
| 4. Trusted analysis becomes part of daily work | Leaders want decisions without learning the source schema; scientists need usable partner data. | Reusable models and governed access replace repeated preparation. | Reproducible answers with sufficient context and provenance. | Pacesetter [6]; Bayer [8]; Boehringer [10] |
| 5. Answers drive coordinated action | Supply teams must approve substitutions; clinical research leaders want staff time back. | Recommendations need permissions, workflow state, rules, and escalation. | Authorized actions, exception handling, and evidence of operational benefit. | Medline [7]; Parexel [9] |
| 6. The capability survives change | Growth, divestiture, new products, and new markets must not recreate fragmentation. | Mastering and semantic rules need versioning, ownership, and onboarding processes. | Repeatable integration and governed change after go-live. | CHS [1–2]; Piramal [3]; Aurobindo [4] |

The trust transition is a proposed interpretation: reliance moves from a person who knows how to reconcile the numbers toward an institutionally owned capability that can explain and reproduce them. This is not measured by the cited sources.

## Ten evidence cases

### 1. CHS: finance modernization becomes enterprise purchasing visibility

**Subindustry / voices:** For-profit provider network; Jason Johnson, EVP and CFO; Kevin Hammons, CEO. **Sources:** December 18, 2025 interview and February 24, 2026 reporting. [1–2]

**Executive excerpt:** Johnson describes the post-implementation priority as “maturing and optimizing both our use of Oracle and our shared operations model.”

**Observed journey:** CHS completed its cloud ERP deployment on January 1, 2025. Johnson describes common finance, supply-chain, and workforce processes and dashboards for expense analysis. Hammons reports an approximately 10% reduction in monthly close time. Subsequent reporting describes the first enterprise-wide item master, replacing purchasing aggregation across multiple systems. CHS reported approximately $50 million in 2025 ERP-related savings; that is a combined transformation outcome, not an isolated MDM benefit.

**Interpretation:** Strong, explicit evidence of an item-master need being addressed. The semantic extension is a discovery hypothesis: linking purchasing and utilization to care setting, procedure, and financial performance. Portfolio divestitures also make effective-dated organizational mappings important.

**Question to test:** Can operators explain a supply-expense variance as price, quantity, product mix, care mix, or portfolio change without rebuilding the analysis?

### 2. Piramal Pharma: MDM is part of scaling the operating model

**Subindustry / voice:** Pharmaceutical manufacturing and services; Viral Gandhi, President and Group CIO, Piramal Group. **Source:** Interview updated March 2, 2026. [3]

**Executive excerpt:** “A comprehensive master data management approach ensures accuracy, consistency, lineage and accountability across systems”.

**Observed journey:** Gandhi describes Catalyst NxGen as a business transformation spanning manufacturing, quality, finance, supply chain, and shared services. He connects it to delivery performance, batch-release cycles, equipment reliability, and working-capital discipline. He characterizes the organization as institutionalizing and scaling its digital capabilities. The interview offers directional benefits rather than independently verified effect sizes.

**Interpretation:** Explicit MDM investment, not merely a suspected gap. Potential semantic work lies in consistent interpretation of delivery performance, batch status, quality events, inventory, and financial results across functions. The source does not establish deployment of a distinct semantic layer.

**Question to test:** When manufacturing, quality, and finance discuss a released batch or an on-time order, are they referencing the same entity, event, timestamp, and inclusion rules?

### 3. Aurobindo Pharma: an unusually direct description of both gaps

**Subindustry / voice:** Pharmaceutical manufacturing; Chitti Babu, Group CIO. **Source:** CIONOW interview, 2026. [4]

**Executive excerpts:** “master data drifts from operational reality”; “OT and IT assign different meanings to the same events”.

**Observed journey:** Babu describes recurring transformation failure modes: software follows the standard process while staff handle exceptions, and accountability disappears across application boundaries. He advocates enduring business ownership, decision rights, and a common core that includes the data model, chart of accounts, master data, and controls.

**Interpretation:** Direct evidence for the distinction between identity/attribute governance and shared meaning. Importantly, he is discussing patterns he sees in transformations; this is not a disclosed audit finding that Aurobindo currently has those failures.

**Question to test:** Which operational events have different meanings in manufacturing systems and enterprise reporting, and who has authority to resolve the difference?

**Date note:** Search indexing identifies September 17, 2026; the retrieved page displays October 21, 2026. Both meet the cutoff; no precise original publication day is asserted here.

### 4. Advocate Health: merger scale creates a cross-functional platform requirement

**Subindustry / voice:** Integrated nonprofit health system; Dr. Bobbie Byrne, CIO. **Source:** November 6, 2025 announcement. [5]

**Executive excerpt:** “the reliability, performance, and data quality we need”.

**Observed journey:** Following the combination of Advocate Aurora Health and Atrium Health, Advocate sought to connect workforce, finance, and procurement data across more than 60 hospitals and over 1,000 care sites. The announcement reports a completed Workday deployment spanning these functions. It describes financial visibility and inventory improvements without quantifying independently verified results.

**Interpretation:** Explicit evidence of consolidation after a merger. Common worker, facility, supplier, and cost-center identities are relevant discovery domains, but the release does not diagnose particular duplicate masters or conflicting metrics. An external semantic layer is not automatically required if the native application model serves the decisions adequately.

**Question to test:** Which executive questions still require reconciliation between the consolidated back office and clinical systems?

### 5. Pacesetter Health: the warehouse existed, but the operating picture was incomplete

**Subindustry / voice:** Acquisition-driven podiatry practice platform; Rami Nofal, CFO. **Source:** Focus HCS customer case, 2026. [6]

**Executive excerpt:** “We really just wanted the data stored in a way we could report on it.”

**Observed journey:** The case describes 38 locations and nine EHRs across eleven instances. Pacesetter already had a functioning warehouse for production, revenue-cycle, collections, and financial reporting. Clinical, scheduling, and other operational dimensions remained difficult to access. The engagement combined migration with a structured reporting model; the case reports full ModMed consolidation by February 2026.

**Interpretation:** Strong evidence that financial aggregation alone did not provide a complete operating model. Reusable semantics and cross-domain relationships are plausible needs; specific patient/provider mastering defects are not established. The documented engineering gap must not be relabeled as an ontology failure.

**Question to test:** Can finance trace a performance change back to provider capacity, scheduling, clinical activity, and collections using consistent definitions?

**Date/evidence note:** The page has no visible exact publication date; search indexes place it in 2026, and its content reports February 2026 completion. It is a supplier-authored customer case, not an independent evaluation.

### 6. Medline: from infrastructure capacity to product-substitution decisions

**Subindustry / voices:** Med-surg manufacturing and distribution; Marshall Lancaster, CIO; Marc Phillips, SVP, Supply Chain Solutions. **Sources:** September 22, 2025 customer story; May 4, 2026 launch release. [7a–7b]

**Business excerpt:** Phillips says customers needed “better visibility, simpler workflows and smarter tools”.

**IT excerpt:** Lancaster describes “building practical solutions in close collaboration with partners and customers”.

**Observed journey:** The earlier account describes SAP capacity and maintenance constraints and migration to Azure. The later Mpower release describes supply/demand visibility, product alternatives, and clinical approval workflows. Medline reports early substitution-workflow efficiency improvements above 50% against a five-to-seven-day baseline. The release does not provide enough measurement detail for an independent ROI calculation.

**Interpretation:** Infrastructure, data integration, and decision context are different parts of this journey. Substitution decisions plausibly require governed product identity plus relationships among specifications, use, availability, and approvals. That is a strong domain-model use case, not proof that Mpower uses an ontology or that Medline has an unresolved MDM defect.

**Question to test:** Is an alternative merely commercially available, or approved for this particular clinical use and facility?

### 7. Bayer: contextual scientific data spans instruments and external partners

**Subindustry / voice:** Pharmaceutical R&D and external CRO/CDMO collaboration; Linus Goerlitz, Regulatory Science Transformation Lead. **Source:** November 20, 2025 release. [8]

**Leader excerpt:** “The platform's audit capabilities have streamlined our regulatory preparation processes.”

**Observed journey:** Bayer expanded TetraScience to harmonize instrument data and data from CRO/CDMO partners. The supplier reports contextualized access and same-day analysis that previously required weeks of integration. The announcement covers both pharma and crop science, so the improvement cannot be assigned solely to pharmaceutical operations.

**Interpretation:** Explicit harmonization and provenance need; strong alignment with semantic context. Candidate relationships include sample, experiment, method/version, instrument, material, result, and partner. These are proposed discovery objects, not a published description of Bayer's actual ontology. The release does not demonstrate a separate MDM deployment.

**Question to test:** Can two results be compared scientifically after accounting for method, sample lineage, units, and experimental conditions?

### 8. Parexel: modernization must preserve history and reduce human burden

**Subindustry / voice:** Contract research organization; Jonathan Shough, CIO. **Source:** June 26, 2025 podcast transcript. [9]

**Executive excerpt:** “it's a journey, not an event.”

**Observed journey:** Shough explains that historical and safety requirements can keep legacy environments in use for up to ten years. He describes modernization requiring partnership with finance, executive leadership, and business units. His clinical-monitor example is a goal: reduce travel and administrative work so monitors regain time. It is not a measured time-saving result.

**Interpretation:** Strong evidence for incremental modernization and workflow-centered value. Semantic and master-data needs are hypotheses, not disclosed diagnoses. Useful candidates are stable study, site, investigator, and participant identifiers and preservation of historical definitions and provenance across systems.

**Question to test:** Where do staff repeatedly re-enter or reinterpret information as it passes between trial systems, monitoring workflows, and sponsor deliverables?

### 9. Boehringer Ingelheim: product mastering and common reporting across markets

**Subindustry / voice:** Global biopharma commercial operations; Justin Gale, Global Head of Data Excellence. **Source:** January 29, 2026 announcement. [10]

**Executive excerpt:** “seamless ingestion of our global commercial data sets into a unified platform”.

**Observed journey:** Boehringer selected IQVIA DaaS+ for commercial data harmonization. The announced scope includes an industry data model, global product mastering, and market, brand, and franchise reporting across 59 countries. The objective is to scale data products across regions and therapeutic areas. These are announced capabilities and intentions, not demonstrated realized benefits.

**Interpretation:** Explicit evidence for product mastering and harmonized reporting. The semantic discovery question concerns how local products, brands, markets, and franchises relate and how performance measures remain comparable. The source does not establish that acquisition activity caused this need.

**Question to test:** Can the same product's regional presentations and market definitions be reconciled into a defensible global commercial view?

### 10. Centers for Dialysis Care: procurement wants consistent answers across facilities

**Subindustry / voice:** Multisite dialysis provider; Michael Humphrey, Director of Procurement and Supply Chain Management. **Source:** February 3, 2026 announcement of a September 2025 agreement. [11]

**Business-leader excerpt:** “standardization, pricing transparency and consistent product availability across our locations”.

**Observed journey:** The agreement provides access to Medline analytics across 25 locations, covering item use, contract compliance, pricing, and category spending. The source reports the agreement and intended capabilities, not quantified realized savings.

**Interpretation:** A credible purchasing-visibility use case with potential master-data and semantic dependencies. Candidate controls include item identity, units of measure, facility attribution, contract applicability, and category definitions. Nothing in the announcement proves duplicates, erroneous pricing, or uncontrolled masters at the provider.

**Question to test:** Does a price or usage comparison account for pack size, contract period, product equivalence, and the activity at each facility?

## Direct corroboration for the ontology need

The Pistoia Alliance's July 16, 2025 Pharma General Ontology Phase 1 material states that companies can define similar core concepts differently, producing extensive mapping work even internally. The program seeks agreement on core entities and controlled terminologies. Participants listed include data and semantics leaders from AstraZeneca, Roche, Merck Group, Pfizer, GSK, Chiesi, and Novo Nordisk. [12]

This is unusually direct evidence that harmonization includes agreement about meaning, not just moving data. It is a program description, not a quotation attributable to every listed participant. It also does not establish that every participant has the same maturity level or that PGO addresses all finance and supply-chain requirements.

## How to qualify the actual gap

The examples in this table are proposed discovery tests, not additional findings about the organizations above.

| Signal heard from a customer | Leading hypothesis | Evidence to request | What would weaken the hypothesis |
|---|---|---|---|
| The same supplier/product/provider appears differently across businesses. | MDM | Crosswalks, duplicate rates, ownership, merge rules, effective-dated hierarchies. | Identities reconcile correctly; the real problem is data latency or missing access. |
| Finance and operations get different answers from the same records. | Semantic definition or modeling | Calculation logic, grain, time windows, units, inclusions, and allocation rules. | A source defect or permissions difference explains the entire discrepancy. |
| We cannot compare an acquired operation with the rest of the enterprise. | Both, plus integration | Account mappings, entity hierarchies, service/product definitions, acquisition dates, and reporting policies. | Comparable entities and metrics already exist; remaining delay is pipeline capacity. |
| Our model finds alternatives, but users cannot approve them confidently. | Domain context and workflow | Equivalence criteria, restrictions, approval authority, policy versions, and evidence trails. | Context is complete; the bottleneck is staffing or approval turnaround. |
| Scientists repeatedly prepare partner data before analysis. | Integration and scientific semantics; possibly MDM | Sample and study IDs, methods, units, provenance, schema mappings, and partner handoffs. | Formatting alone explains the work, with no ambiguity in identity or interpretation. |
| Results change after a reorganization. | Effective-dated MDM and semantic rules | Historical hierarchy versions and explicit as-was versus as-is reporting logic. | The change is intentional and correctly explained by approved policy. |

## What this means for the commercial conversation

Lead with a decision and an owner. For a CFO, begin with close-cycle reconciliation, unexplained variance, working capital, or comparability after a transaction. For a supply-chain leader, begin with aggregated spend, substitutions, contract performance, or availability. For a CRO or R&D leader, begin with handoffs, historical continuity, comparability, and evidence preparation.

Then trace one decision through its dependencies: source access → entity identity → shared meaning → business rules → authorized action. This is an investigation sequence, not a requirement to purchase five platforms.

For an initial assessment, choose a small set of live questions rather than an enterprise-wide ontology exercise. Examine actual source records and current reporting logic. Quantify reconciliation effort, unmapped entities, disputed definitions, and decision delay. Attribute value only to the component that changes: total ERP-program savings should not be repackaged as MDM ROI, and a harmonization outcome should not be presented as proof of a specific ontology implementation.

The strongest positioning supported by this evidence is: **make the organization's important decisions reproducible across functions, systems, and changes in the business.** Mastering provides dependable identity; semantic modeling provides consistent interpretation; workflow and ownership turn that foundation into operating value.

## Evidence and scope notes

- Dates refer to publication or the identified 2026 version, not necessarily the date when the underlying business event occurred. Older events recounted in a new source are identified as historical.
- Direct executive interviews and first-person transcripts are distinguished from supplier-authored cases and announcements. Supplier performance claims have not been independently audited.
- Titles reflect the source at publication. Directors and functional leaders are identified accurately rather than represented as C-suite executives.
- The evidence covers integrated providers, specialty practices, dialysis, med-surg, pharmaceutical manufacturing/services, biopharma commercial operations, scientific R&D, and CRO/CDMO interfaces. It is a qualitative selection, not a representative industry survey. It does not establish separate conclusions for payers, every medical-device category, or every CRO operating model.
- The strongest direct MDM evidence is CHS, Piramal, and Boehringer. The strongest direct semantic evidence is the Aurobindo interview's general observations and Pistoia's program rationale. The other mappings are deliberately qualified hypotheses.
- Undated legacy customer stories and older material surfaced during research were excluded. Pacesetter's exact publication day remains unspecified; its 2026 content and indexing satisfy the requested year window.

## Source register

1. Becker's Hospital Review, **December 18, 2025**. First-person CEO/CFO interview: [How CHS is tackling debt — and redefining itself as a healthcare company](https://www.beckershospitalreview.com/hospital-management-administration/how-chs-is-tackling-debt-and-redefining-itself-as-a-healthcare-company/).
2. Becker's Hospital Review, **February 24, 2026**. Executive reporting: [How CHS is using AI and ERP to protect margins](https://www.beckershospitalreview.com/finance/how-chs-is-using-ai-and-erp-to-protect-margins/).
3. Financial Express, **updated March 2, 2026**; first uploaded March 1. CIO interview: [Taking a structured approach to AI scaling](https://www.financialexpress.com/business/news/taking-a-structured-approach-to-ai-scaling-viral-gandhi-president-amp-group-cio-piramal-group/4159491/).
4. CIONOW, **2026**, date discrepancy explained in case. CIO interview: [Go-Live is the Beginning, Not the End](https://cionow.in/go-live-is-the-beginning-not-the-end-chitti-babu-group-cio-aurobindo-pharma/).
5. Workday, **November 6, 2025**. Supplier announcement quoting customer CIO: [Advocate Health Elevates Employee and Patient Experience with Workday](https://newsroom.workday.com/2025-11-06-Advocate-Health-Elevates-Employee-and-Patient-Experience-with-Workday).
6. Focus HCS, **2026**, no exact date displayed. Supplier case quoting customer CFO: [How a 38-location podiatry group got to one source of truth](https://focushcs.com/results/case-studies/how-a-38-location-podiatry-group-unified-its-data-across-9-emrs-and-11-instances/).
7. Medline journey: **(a) September 22, 2025**, Microsoft customer story, [Medline sparks a revolution in healthcare supply chain management with SAP on Azure](https://www.microsoft.com/en/customers/story/25243-medline-azure); **(b) May 4, 2026**, company announcement, [Medline officially launches Mpower](https://newsroom.medline.com/releases/official-launch-mpower/).
8. TetraScience, **November 20, 2025**. Supplier announcement quoting Bayer leader: [TetraScience and Bayer Expand Partnership to Advance Scientific Data Management](https://www.tetrascience.com/news/tetrascience-bayer-expand-partnership-to-advance-scientific-data-management). Page publication date is November 20; body dateline says November 19.
9. What's New in Data / Striim, **June 26, 2025**. Interview transcript: [From Compliance to Catalyst: How Parexel's CIO Builds for Impact](https://www.buzzsprout.com/1889937/episodes/17394594-from-compliance-to-catalyst-how-parexel-s-cio-builds-for-impact). Relevant chapter starts: modernization 17:53; patient/workflow discussion 30:50. Transcript includes automated transcription artifacts.
10. IQVIA, **January 29, 2026**. Collaboration announcement quoting customer data leader: [IQVIA and Boehringer Ingelheim announce strategic long-term global commercial data foundation transformation collaboration](https://www.iqvia.com/newsroom/2026/01/iqvia-and-boehringer-ingelheim-announce-strategic-long-term-collaboration).
11. Medline, **February 3, 2026**. Agreement announcement quoting procurement leader: [Centers for Dialysis Care awards Prime Vendor status to Medline](https://newsroom.medline.com/releases/centers-for-dialysis-care-pv/).
12. Pistoia Alliance, **July 16, 2025**. Consortium program material: [Pharma General Ontology Phase 1](https://pistoiaalliance.org/resource-library/pharma-general-ontology-pgo-phase-1/).
