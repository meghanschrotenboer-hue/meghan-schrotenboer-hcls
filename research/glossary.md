# Glossary

Plain-English definitions for the terms that keep showing up. Where a source defines a term, the source is cited.

## FAIR (Findable, Accessible, Interoperable, Reusable)

A set of principles for making data usable by **both people and machines**. FAIR isn't a product or a standard you buy. It's a property data can have more or less of. ([GO FAIR](https://www.go-fair.org/fair-principles/); [S007](sources/S007-fair-maturity-matrix.md))

| Letter | Means | In practice | Typical maturity level* |
|---|---|---|---|
| **F**indable | Data and metadata have **globally unique, persistent identifiers** and rich metadata, and are registered in a searchable catalog | You (or an agent) can find the dataset without knowing who to ask | F1–F2 at L1; F3–F4 at L3 |
| **A**ccessible | Retrievable by identifier using a standard, open protocol, **with authentication and authorization where needed**; metadata stays available even if the data is retired | "Accessible" does **not** mean "open." It means the path to access is clear and machine-readable | A1 at L1; A1.2 at L2; A1.1 and A2 at L3 |
| **I**nteroperable | Uses formal, shared languages and **vocabularies that are themselves FAIR** (ontologies such as IDMP-O and SNOMED CT), with qualified links to other data | Data from different systems can be combined without custom translation | I1–I3 at **L4** (the latest to mature) |
| **R**eusable | Richly described, with a **clear usage license**, **detailed provenance**, and adherence to community standards | You can trust it, legally use it, and know where it came from | License at L2; provenance at L3; community standards at L4 |

\* From the FAIR Maturity Matrix principles table ([S007](sources/S007-fair-maturity-matrix.md)). The "typical level" is where an organization usually achieves the principle.

**"FAIR Enough"**: the FAIR Maturity Matrix's term for deciding that *not all data needs to be fully FAIR*. It's a strategic choice, and the data equivalent of *satisficing* in the [AI Intention Matrix](lenses.md#lens-1--ai-intention-matrix-augment--automate--satisfice--optimize).

**FAIRification**: making existing data FAIR after the fact. **FAIR by design** means making data FAIR at the point of creation, which the evidence favors as cheaper ([S010](sources/S010-fair-data-by-design-roche.md)).

## Other terms

| Term | Plain English | Source |
|---|---|---|
| **Ontology** | "A formal, identifier-based representation of concepts and relationships used to make meaning explicit for machines." The key to semantic interoperability | [S007 lexicon](sources/S007-fair-maturity-matrix.md) |
| **Controlled terminology** | A governed list of allowed terms or codes, "often a stepping stone toward ontologies" | [S007 lexicon](sources/S007-fair-maturity-matrix.md) |
| **IDMP** | ISO standards (11238, 11239, 11240, 11615, 11616) for identifying medicinal products and substances, driven by regulators | [S002](sources/S002-pistoia-idmp-o-github.md) |
| **IDMP-O** | Pistoia's open ontology implementing ISO IDMP for machines | [S002](sources/S002-pistoia-idmp-o-github.md), [S003](sources/S003-pistoia-idmp-o-info-sheet.md) |
| **SNOMED CT** | The leading clinical terminology for diagnoses, findings, and procedures; licensed through SNOMED International (via UMLS in the US) | [S008](sources/S008-snomed-ct-bioportal.md) |
| **EMA SPOR / PMS** | EMA's master-data services (Substances, Products, Organisations, Referentials); PMS is the Product Management System for medicinal product data | [S002](sources/S002-pistoia-idmp-o-github.md), [S003](sources/S003-pistoia-idmp-o-info-sheet.md) |
| **SHACL** | A W3C language for writing rules that data must satisfy, i.e., machine-checkable acceptance criteria for graph data | [S002](sources/S002-pistoia-idmp-o-github.md) |
| **Competency questions** | The questions an ontology must be able to answer; used as tests | [S002](sources/S002-pistoia-idmp-o-github.md) |
| **Provenance (W3C PROV)** | A record of where data came from and how it was transformed | [S007](sources/S007-fair-maturity-matrix.md) |
| **DCAM** | EDM Association's Data Management Capability Assessment Model, an enterprise data-management maturity framework | [S009](sources/S009-edm-association-resources.md) |
| **CDMC** | EDM Association's Cloud Data Management Capabilities framework, including 14 key automated controls | [S009](sources/S009-edm-association-resources.md) |
| **OMG** | Object Management Group, a standards body (Commons Ontology Library; ISO PAS submitter). Its assets were acquired by the EDM Association in Oct 2025 | [S009](sources/S009-edm-association-resources.md) |
| **Satisficing** | Herbert Simon's term: stop searching once an option meets the standard. The counterpart of optimizing | [S004](sources/S004-ai-intention-matrix.md) |
