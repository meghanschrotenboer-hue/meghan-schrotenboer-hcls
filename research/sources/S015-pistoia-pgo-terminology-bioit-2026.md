---
id: S015
title: "Pharma General Ontology (PGO)-Terminology: Building a Semantic Backbone for FAIR and AI-Ready Knowledge Graphs"
publisher: "Pistoia Alliance (Bio-IT World 2026, Knowledge Graphs session, Boston)"
authors: "Pistoia Alliance PGO-Terminology project manager; steering group from AstraZeneca, Chiesi, GSK, Merck KGaA, Novo Nordisk, Roche, Pfizer, Vertex"
date_published: 2026-05
date_added: 2026-10-22
url: "https://github.com/Pistoia-Alliance-Inc/Pistoia-Alliance-PGO/"
type: conference
access: read-in-full              # uploaded deck, 15 slides
value_chain: [discovery, clinical, regulatory-cmc, manufacturing-supply, commercial-medical, cross-cutting]
intention_matrix: [automate-optimize]
stack_layer: [data-semantics, governance-trust]
players: [consortium, buyer, services, frontier-labs]
themes: [T1, T5, T7, T9]
signal: high
---

# S015 · Pistoia PGO-Terminology (Bio-IT World, May 2026)

**Why I saved it:** *(add your line)*

## TL;DR
- Pharma has a **"Tower of Babel"** problem: "compound," "molecule," "substance," and "drug" mean different things across domains and companies. **PGO-Terminology (PGO-T)** is a community-governed **"lingua franca"** of core pharma concepts.
- The pitch is explicitly about AI: **"AI requires a common data language."** PGO-T gives knowledge graphs resolvable URIs, entity disambiguation, cross-company graph federation, and **RAG / LLM grounding** that "reduces hallucination risk."
- **Funded by seven pharma companies** (AstraZeneca, Chiesi, GSK, Merck KGaA, Novo Nordisk, Pfizer, Roche); open access (CC BY 4.0 / MIT). Phase 1 delivered 17 core concepts; Phase 2 (2025–26) expands beyond R&D.

## What the source says
- **Pistoia by the numbers:** global not-for-profit (incorporated 2008); "200+ member companies, 30+ active projects, 1,000+ participants." Members shown include AbbVie, **Accenture**, AstraZeneca, Bayer, BI, BMS, CSL Behring, Elsevier, Chugai, Galápagos, GSK, Chiesi, Lilly, Merck, Novartis, Pfizer, Merck KGaA, Novo Nordisk, Roche, Thermo Fisher, Vertex, Takeda, Eurofins, Kyowa Kirin.
- **The challenge (three structural problems):** similar concepts, different words; deep but disconnected domain ontologies ("semantic silos"); no cross-pharma lingua franca. "Teams spend enormous time on semantic reconciliation before any real work begins." Charter quote: "With limited semantic interoperability we are creating semantic silos, slowing the path towards data centricity while increasing costs."
- **Pistoia's ontology stack:** PGO-T (terminology layer) sits above the domain ontologies **IDMP-O** (regulatory product identification), **CMC Process Ontology** (manufacturing), and **ClinOps** (clinical operations shared vocabulary). It aligns to BFO (upper level) and OMG and IOF libraries (mid level).
- **What PGO-T is:** a community-governed reference set; declares which terms are used and why; open access on GitHub. **What it isn't:** a replacement for MedDRA, SNOMED, ChEBI; a top-down mandate; domain-specific; or (yet) an ontology.
- **Scope, two axes:** knowledge domains (Research & Early Development → Manufacturing → Clinical → Regulatory → Commercial and Market Access → Corporate → Supply Chain) × semantic complexity (controlled vocabulary → thesaurus → ontology).
- **Governance:** a steering group of sponsoring pharma companies funds and directs the work; an expert group (ontologists, curators, domain experts) chooses existing definitions; a project manager handles delivery. Rules: don't reinvent definitions; be human-readable; have a resolvable URL/IRI; be machine-readable from Phase 2 (e.g., OWL). "No single company decides." Initial modeling uses **LinkML** ([CEUR paper](https://ceur-ws.org/Vol-4196/paper_3.pdf)).
- **Status:** Phase 1 (2024–25) delivered **17 core concepts** (e.g., Gene, Protein, Cell/Species, Assay, Biomarker, Biospecimen, Substance, Compound, Drug, Disease, Indication, Clinical_study). Phase 2 (2025–26) adds 20+ concepts (Adverse Event, Excipient, Instrument, Study Site…), machine-readable schemas, and mappings to external ontologies. **Sustainability model: "PGO as permanent industry reference data product."**
- **Long-term vision:** machine-readable terminology on EBI OLS and BioPortal; public declarations of who implements PGO-T; organizations tag data assets with PGO URIs and exchange data across **CROs, partners, and regulators**.
- **Practical example:** "A CRO delivers a data product tagged with PGO-T URIs. The receiving pharma company's knowledge graph ingests it directly: no manual mapping, no reconciliation meetings."
- **Getting involved (members):** **User** (feedback), **Expert** (ontologists and curators advise the steering group), **Sponsor** (fund and direct Phase 3+).

## Quotable
> "AI requires a common data language." (funders' video)

> "Knowledge graphs are only as good as their underlying semantics... Cross-company KGs require shared concept identifiers; without them, graph federation fails."

> "A CRO delivers a data product tagged with PGO-T URIs. The receiving pharma company's knowledge graph ingests it directly."

## Our read

**This is the consortium making T1 and T7 its explicit pitch.** Seven pharma funders say, in effect: AI fails without shared meaning, and agents and RAG need resolvable identifiers. It's the clearest buyer-side statement of "semantics before AI" in the library.

**"Data product" is the bridge to cloud data platforms.** PGO-T's own example is a CRO delivering a *tagged data product* to a sponsor. Data products, governed sharing between organizations, and catalog-level metadata are exactly what modern cloud data platforms do. The ontology is authored in semantic-web tooling (LinkML/OWL), but it **lands** in data products and pipelines. That landing layer is where a data-platform SI can contribute credibly. **[our inference]**

**Contribution roles are spelled out:** user, expert, sponsor, open to Pistoia members. An SI with ontology-literate data engineers fits the expert or user role; a sponsorship is a bigger, executive-level bet.

**So what for services:** Offer "PGO-T-ready data products": tag priority R&D and clinical data assets with PGO URIs, map internal vocabularies, and publish them through the client's catalog and sharing layer. It's small, concrete, standards-backed, and AI-relevant.

**So what for frontier labs:** PGO-T URIs are cheap, high-value grounding anchors for RAG and agents. Supporting them in connectors is low effort with outsized credibility.

**Job to be done (R&D data platform owner):** When every partner and CRO sends data in its own vocabulary, I want a shared reference set of core concepts my systems and partners can all tag against, so I can ingest partner data without reconciliation meetings and ground AI on unambiguous concepts.

| Current state | Future state | Gap (the offer) |
|---|---|---|
| Semantic reconciliation before every project | Data assets tagged with PGO-T URIs at creation | PGO-T mapping and tagging of priority data products |
| Partner and CRO data remapped by hand | Tagged data products ingested directly | Sponsor–CRO data product contracts and sharing patterns |
| RAG grounded on ambiguous terms | Grounding on resolvable concept URIs | URI-aware retrieval and agent connectors |

## Open questions
- Phase 2 concept list and timeline; is Phase 3 funded?
- Who has publicly declared PGO-T implementation?

## Related
- [S002 · IDMP-O](S002-pistoia-idmp-o-github.md): domain ontology under PGO-T
- [S007 · FAIR Maturity Matrix](S007-fair-maturity-matrix.md): I2, FAIR vocabularies
- [S010 · FAIR data by design](S010-fair-data-by-design-roche.md): Roche is also a PGO-T funder
- [A001 · Could evolv contribute as a Snowflake SI?](../analyses/A001-evolv-pistoia-snowflake-si.md)
- [Clinical Operations Ontology project](https://pistoiaalliance.org/project/clinical-operations-ontology/): built on CDISC USDM 2.0, TransCelerate DDF, SNOMED CT
