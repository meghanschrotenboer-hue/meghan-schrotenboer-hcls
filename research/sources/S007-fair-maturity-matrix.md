---
id: S007
title: "FAIR Maturity Matrix (v1.1): dimensions, levels, strategy, resources and lexicon"
publisher: "Pistoia Alliance · FAIR-for-Pharma Community of Experts"
authors: "20+ experts from AstraZeneca, Bristol Myers Squibb, CSL Behring, Curlew Research, Elsevier, ELIXIR Europe, Exponent AI, FAQIR Foundation, GO FAIR Foundation, IQVIA, Novo Nordisk, Ontoforce, ORCID, Perdl, The Hyve, Pistoia Alliance"
date_published: 2025-03-14       # v1.1; v1 released 2024; built Feb 2023 – Apr 2024
date_added: 2026-10-22
url: "https://pistoiaalliance.github.io/FAIRMaturityMatrix/FMMdimensions#fair-strategy"
type: standard
access: read-in-full              # via the public source repository (see provenance note)
value_chain: [cross-cutting, discovery, clinical]
intention_matrix: [automate-optimize, automate-satisfice]
stack_layer: [data-semantics, governance-trust, commercial-model]
players: [consortium, buyer, services, frontier-labs]
themes: [T1, T2, T3, T4, T5, T6, T7, T8]
signal: high
---

# S007 · FAIR Maturity Matrix (Pistoia Alliance)

**Why I saved it:** The FAIR concept (Findable, Accessible, Interoperable, Reusable), the dimensions view with a focus on **FAIR strategy**, and the resources and lexicon page. *(expand in your words)*

> **Provenance note.** The official site (pistoiaalliance.github.io) and the Confluence lexicon page were blocked in this environment. The full text was read from the public source repository that feeds the Pistoia documentation hub ([chris-day/FAIR-Maturity-Matrix](https://github.com/chris-day/FAIR-Maturity-Matrix), last updated 2026-04-29, referenced in Pistoia's [FAIR-COE](https://github.com/Pistoia-Alliance-Inc/FAIR-COE) build config). Its header matches the official release: **v1.1, 2025-03-14, CC BY 4.0**. The *Autonomous AI Agent* persona sits in that repository's personas folder; **[verify it appears on the official site]**.

Also covers: [Resources and lexicon (Confluence)](https://pistoiaalliance.atlassian.net/wiki/spaces/PUB/pages/3366879360/FAIR+Maturity+Matrix+resources+and+lexicon)

## TL;DR
- An **organizational** maturity model for FAIR data in life sciences: **7 dimensions × 6 levels (L0–L5)**. It's built for leaders who allocate budget, people, and time, not just for data teams.
- The **FAIR strategy** dimension explicitly includes *deciding what not to do*: "only some data may need to be FAIR, **'FAIR Enough'**." That is satisficing applied to data.
- The business value ladder names AI directly: at L3–L4, FAIR enables **"quality AI training data sets for LLM"**; at L5, **"AI trusted actionability significantly increase[s]."**
- The persona library treats an **Autonomous AI Agent as a data-consumer persona** whose success depends on "the FAIR characteristics of the underlying data."

## What the source says

**Purpose and audience**
- Fills a gap: many dataset-level FAIR metrics exist, but there was "no simple, agreed, maturity assessment model of FAIR data principle implementation at the organisational level for life-science organisations."
- Audience: "Leadership developing strategies and responsible for allocating resources (finance, people, time)." The ecosystem explicitly includes **implementation partners: CROs, technology and information providers, and consulting firms**.
- Intended use: an actionable assessment tool, "descriptive rather than prescriptive," so different assessors reach similar conclusions about the same organization.

**Seven dimensions (rows), non-hierarchical**

| Dimension | Key notions |
|---|---|
| FAIR data | Data, metadata, data products |
| FAIR leadership | Types of leadership necessary |
| **FAIR strategy** | Now, the next FAIR stage, and how to get there |
| FAIR roles / personas | Human roles needed |
| FAIR processes | Processes to implement explicitly |
| FAIR knowledge | What needs to be known |
| FAIR tools and infrastructures | From persistent identifiers to controlled vocabularies to semantic models |

An organization can sit at different levels on different dimensions and at different granularity (enterprise vs. department).

**Six levels (columns), with a marketplace metaphor**

| Level | Nickname | Metaphor | Key features |
|---|---|---|---|
| L0 | Life is unFAIR | Junkyard | Lack of awareness |
| L1 | Started the FAIR journey | Flea market | Awareness, first pilots |
| L2 | Getting FAIR | Street market | Pilots in place |
| L3 | Pretty FAIR | Specialized local markets | Transition to good and best practice |
| L4 | Really FAIR | Hypermarket | Operational; internal focus; emerging cross-organization |
| L5 | FAIRest of them all | Digital online store | Aspirational; cross-organization standards and interoperability |

**The FAIR strategy dimension**
> "Strategies are frameworks for making decisions related to FAIR implementation, from business case to capability-building to running operations... This dimension is also concerned with deciding what not to do (e.g., only some data may need to be FAIR, 'FAIR Enough'), identifying metrics, organizational sectors (beyond R&D) involved and the cultural change required."

How strategy matures:
- **L0:** no strategy; FAIR applied "haphazardly... in response to external pressures."
- **L1:** an embryonic vision. Organizations start seeing "the value of strategic collaborative efforts with pre-competitive organizations, e.g. Pistoia Alliance." A choice emerges between "closed" (build internally) and "open-source" resources (vocabularies, ontologies).
- **L2:** first approved strategy; **champions appear**; FAIR "emerges as an element of a broader Data strategy." Technical choices and partnerships are recognized as strategic.
- **L3:** C-suite-backed plan with budget. Value begins to be tracked. Legal requirements (e.g., research security, the US Sunshine Act) are interpreted through FAIR. Federated domain data with an operating model to connect it.
- **L4:** enterprise FAIR mandate; **FAIR metrics integrated into data governance and risk management**; dedicated budget and people; years of continuity.
- **L5:** clear links to business outcomes (cost savings, efficiency, IP opportunities) backed by empirical cost-benefit analysis; strategy externally visible to pharma, CROs, regulators, and academia.

**Business value ladder (verbatim highlights)**
- L1: "Speed and cost are the main benefits... Data is recognised as a Strategic Asset."
- L2: "machine automation increase[s]. Use-cases for machine-findable and interpretable data start becoming possible."
- L3: organizations "begin to reduce efforts required by retrospective 'FAIRification'"; enables "quality AI training data sets for LLM"; "Facilitated regulatory compliance and auditing."
- L5: "AI trusted actionability significantly increase[s]... Real-world evidence data-mining and improved patient outcomes... reduced time-to-market."
- "FAIR Maturity is not a goal by itself, rather it's an approach to meet strategic business goals." A FAIR Business Value Framework is noted as forthcoming.

**FAIR principles mapped to typical maturity level** (from the principles table)
- Findable F1–F2 and Accessible A1 typically arrive at **L1**; licenses (R1.1) at **L2**; provenance (R1.2) at **L3**.
- **Interoperable I1–I3 and community standards (R1.3) typically arrive at L4**, the latest of all.

**The Autonomous AI Agent persona** *(see provenance note)*
- Defined as "an orchestration framework that coordinates specialized analytics and knowledge services to support decision-making," running scheduled or event-driven sequential and parallel agents across preclinical and clinical domains.
- Its success "depends on how the AI is instructed, the suitability of the AI model used and the FAIR characteristics of the underlying data."
- Related human personas: Data Steward (quality for agent consumption), Data Owner (access policies for agents), Data Standards and Governance Expert (ontologies, identifiers), Research Scientist (validates agent recommendations).
- Illustrative upside and downside figures (scenario claims, not cited studies **[verify basis]**): ">90%" autonomous completion and ">95%" integration fidelity with FAIR data vs. "identifier fragmentation causing 40% data loss at integration boundaries," "manual access gates," "provenance voids," and "license ambiguity forcing conservative data exclusion" without it.
- Bottom line: "FAIR principles are operational substrate enabling autonomous multi-agent coordination."

**Resources and lexicon page:** a curated list of maturity tools and cases, including **EDM Council DCAM** ([S009](S009-edm-association-resources.md)), the **FAIR-Decide cost-benefit framework for pharma R&D** (2023), FAIR Toolkit cases from Roche, AstraZeneca, Bayer, and The Hyve, and automated FAIR checkers (F-UJI, FAIR Checker, FAIRshake). The lexicon defines *ontology* as "a formal, identifier-based representation of concepts and relationships used to make meaning explicit for machines" and *controlled terminology* as "often a stepping stone toward ontologies."

## Quotable
> "...deciding what not to do (e.g., only some data may need to be FAIR, 'FAIR Enough')"

> "FAIR principles are operational substrate enabling autonomous multi-agent coordination."

> "FAIR Maturity is not a goal by itself, rather it's an approach to meet strategic business goals."

## Our read

**"FAIR Enough" is satisficing for data.** The Intention Matrix ([S004](S004-ai-intention-matrix.md)) asks how good the *output* needs to be. The FAIR strategy dimension asks how FAIR the *input* needs to be. The two belong together: a use case in the *augment + satisfice* quadrant rarely justifies L4 interoperability investment, while *automate + optimize* almost always needs it. That pairing could become a scoping tool: **match data investment to intention quadrant.**

**The sequencing problem is a GTM insight.** Agents need interoperability most (shared ontologies, cross-references), yet the matrix places interoperability at **L4, the last thing most organizations achieve**. So the binding constraint on agentic AI in pharma is a capability most buyers haven't reached. That gap is the services opportunity and the frontier-lab adoption risk.

**AI makes FAIR fundable.** FAIR has long struggled with the business case (hence an entire strategy dimension and a forthcoming value framework). The AI agent persona reframes FAIR from data hygiene to *agent readiness*, a budget line executives are already approving.

**So what for services:**
- The matrix is a buyer-built, CC BY-licensed assessment instrument that names consulting firms as part of its ecosystem. It's a credible front door: a FAIR + UXLS ([S005](S005-uxls-maturity-model.md)) readiness assessment, scored on both, sized to the client's AI ambitions.
- The "L2: champions appear" marker is a qualification signal (MEDPICC Champion). The "L4: FAIR metrics in governance and risk" marker tells you who the economic buyer is (CDO, risk).

**So what for frontier labs:**
- An industry body has written a persona spec for what an autonomous agent needs from enterprise data: persistent identifiers, machine-readable access policies, provenance, licenses. That's a requirements document for agent-ready enterprise data, and a partner opportunity labs can point customers toward.
- Labs that make agents *respect* machine-readable licenses and access policies will clear pharma legal and data-governance review faster.

**Job to be done (pharma CDO):** When the board asks why our agentic AI pilots stall at scale, I want an objective view of which data capabilities are missing and what to fix first, so I can fund the foundations that unlock AI instead of more pilots.

| Current state | Future state | Gap (the offer) |
|---|---|---|
| FAIR treated as data hygiene; hard to fund | FAIR funded as agent readiness, tied to AI roadmap | FAIR × Intention Matrix scoping; business case linked to AI use cases |
| Most orgs at L1–L3; interoperability immature | Interoperability (I1–I3) in place for priority AI domains | Ontology adoption (IDMP-O, SNOMED CT), identifier policy, mapping |
| Agents blocked by manual access gates, unclear licenses | Machine-readable policies, provenance, licenses | Agent-ready data governance design |

## Open questions
- Is the Autonomous AI Agent persona in the published v1.1 site or a newer working draft? Is a v1.2 or v2 pending?
- When does the **FAIR Business Value Framework** ship? (A Pistoia repository for it exists but isn't public.)
- Is there benchmark data on where pharma companies cluster by level?

## Related
- [S005 · UXLS Maturity Model](S005-uxls-maturity-model.md): pair for the AI-readiness 2×2
- [S009 · EDM Association (DCAM)](S009-edm-association-resources.md): enterprise data-management maturity counterpart
- [S010 · FAIR data by design (Roche)](S010-fair-data-by-design-roche.md): an L3+ implementation case
- [S002 · IDMP-O](S002-pistoia-idmp-o-github.md) and [S008 · SNOMED CT](S008-snomed-ct-bioportal.md): the "FAIR vocabularies" interoperability requires
- Pistoia blog: [Is Your Organization a Data Junkyard or a Data Marketplace?](https://pistoiaalliance.org/blog/from-junkyard-to-data-marketplace/)
- [Bio-IT World on the FAIR Maturity assessment tool (June 2025)](https://www.bio-itworld.com/news/2025/06/17/pistoia-alliance-s-fair-maturity-assessment-tool)
