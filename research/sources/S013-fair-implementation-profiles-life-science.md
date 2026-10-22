---
id: S013
title: "FAIR Implementation Profiles (FIPs): Life Science domain export and Dublin Core as a semantic model"
publisher: "FAIR Implementation Space on Nanodash (Knowledge Pixels); FIP approach originated with GO FAIR"
authors: "Community-contributed nanopublications"
date_published: 2026-10-22       # PDF export date; live, community-maintained data
date_added: 2026-10-22
url: "https://nanodash.knowledgepixels.com/part?10&id=http://purl.org/np/RApwFvegOdPfNuKlF64wctAzaffAv3j_2kAU9y6kfBoy8%23DCMI&context=https://w3id.org/spaces/FAIR-Implementation-Space&label=DC+%7C+Dublin+Core&part=https://w3id.org/fair/fip/terms/Semantic-model&part-label=Semantic+Model"
type: dataset
access: partial                   # uploaded PDF read in full (Life Science domain); Nanodash page not fetchable here
value_chain: [discovery, cross-cutting]
intention_matrix: []
stack_layer: [data-semantics]
players: [consortium]
themes: [T1, T5, T7]
signal: low
---

# S013 · FAIR Implementation Profiles: What Communities Actually Use

**Why I saved it:** *(add your line; you shared the Life Science domain export and Dublin Core as a "Semantic Model")*

Uploaded file: *part_http___aims_fao_org_aos_agrovoc_c_4318.pdf* (24 pages, generated 2026-10-22), the "Life Science" domain page (AGROVOC concept c_4318) in the FAIR Implementation Space.

## TL;DR
- A **FAIR Implementation Profile (FIP)** is a community's declared list of the specific standards and tools it uses for each FAIR principle, published as machine-readable **nanopublications**.
- The Life Science domain export lists **~84 FIPs**. Contributors are overwhelmingly **European academic and research-infrastructure communities** (ecology, biodiversity, ocean and atmospheric science, toxicology). **Pharma companies are essentially absent.**
- The **most-used FAIR supporting resources are generic web standards**, not domain ontologies: HTTPS, DOI, CC BY 4.0, JSON-LD, PROV-O, DataCite, and **Dublin Core** (7 communities, 11 subdomains).

## What the source says
- **Domain:** Life Science (broader: Natural Science); 6 subdomains, 12 communities listed in domain info.
- **FIPs listed (~84):** e.g., LifeWatch, ICOS, SeaDataNet, DiSSCo, ACTRIS, eLTER, AnaEE, PARC Toxicology, PINK (toxicology/safety), TOXRIC, HBM4EU (human biomonitoring), Pathogens Portal Netherlands, IUPAC, RSpace ELN, OECD Harmonised Templates.
- **Most-used FAIR supporting resources (communities using):** HTTPS (37) · DOI (36) · CC BY 4.0 (32) · JSON-LD (16) · Open Data (15) · NetCDF (15) · PROV-O (15) · DataCite ontology and metadata schema (14 each) · XML Schema (13) · CC0 (13) · OAuth (11) · REST (11) … **Dublin Core (7)** · OWL (6) · RDF (6). Domain vocabularies such as MeSH, ChEMBL, Cell Ontology, and EDAM appear further down the full resource list, mostly for I2 (FAIR vocabularies).
- Each resource maps to the FAIR principles it supports (e.g., Dublin Core → F2, I3, R1.2; MeSH → I2).
- **Dublin Core** appears in your Nanodash link as a declared **Semantic Model** in the FIP ontology.
- **Background** (search, not the PDF): the FIP Ontology's current version is 20260227. A Semantic Interoperability Profile is "a list of FAIR Supporting Resources chosen by a community to support semantic interoperability." FIPs and SIPs are created with Data Stewardship Wizard instances and published as nanopublications via Nanodash. ([FIP ontology on Nanodash](https://nanodash.knowledgepixels.com/resource?0=&id=https%3A%2F%2Fw3id.org%2Ffair%2Ffip%2Fterms%2FFIP-Ontology); [FOIS 2024 paper on FAIR Supporting Resources](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/magagna-et-al-ontological-analysis-of-fair-implementation-profiles.pdf))

## Our read

**Convergence happens bottom-up, on generic standards first.** The top of the list is plumbing every web developer knows (HTTPS, DOIs, open licenses, JSON-LD, provenance). Domain ontologies show up, but further down. For AI, that's encouraging: agents already handle these generic standards well. The hard, valuable part is the **domain semantics layer** (IDMP-O, SNOMED CT, MeSH), which is where differentiated work sits.

**Pharma's FAIR practice is private.** Academic and public research infrastructures publish FIPs; commercial pharma doesn't. Pharma's equivalent "declaration" happens in consortia (Pistoia's FAIR Maturity Matrix, IDMP-O governance) and internal standards. That reinforces **T5**: if you want to see where pharma is converging, watch the consortia, not the open registries.

**Machine-readable declarations are agent-friendly.** FIPs are nanopublications, small RDF graphs with provenance. An agent can read a community's FIP and know which identifiers, vocabularies, and licenses to expect. It's an early pattern for **T7** (agents as data consumers): communities publishing *how to read their data* in a machine-actionable form.

**So what for services:** A FIP is a ready template for a client deliverable: "your organization's FAIR implementation profile." It documents, per FAIR principle, which standards each domain uses, and becomes the backbone of a data-standards roadmap. Most pharma clients don't have one.

**So what for frontier labs:** Supporting nanopublication and FIP formats in agent tooling is a niche but credible signal to the FAIR community. Low priority vs. domain ontologies.

**Job to be done (enterprise data architect):** When multiple R&D domains each pick their own identifiers and vocabularies, I want a declared, machine-readable profile of what each domain uses, so I can converge on shared standards and give agents a map to our data.

## Open questions
- Is any pharma company or Pistoia project publishing FIPs? Search the FAIR Implementation Space for pharma communities.
- Could a Pistoia-sponsored "pharma FIP" become a standard deliverable?

## Related
- [S007 · FAIR Maturity Matrix](S007-fair-maturity-matrix.md): lexicon lists the FIP Ontology and FIP Wizard
- [S002 · IDMP-O](S002-pistoia-idmp-o-github.md) and [S008 · SNOMED CT](S008-snomed-ct-bioportal.md): the domain semantics layer
