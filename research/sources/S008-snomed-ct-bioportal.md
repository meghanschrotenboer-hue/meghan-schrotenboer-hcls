---
id: S008
title: "SNOMED CT (via NCBO BioPortal)"
publisher: "SNOMED International; distributed in the US by NLM via UMLS; indexed on NCBO BioPortal"
authors: "SNOMED International"
date_published: 2025-11-03       # BioPortal version 2025_09_01 (UMLS 2025AB), uploaded 2026-03-22
date_added: 2026-10-22
url: "https://bioportal.bioontology.org/ontologies/SNOMEDCT"
type: standard
access: partial                   # BioPortal blocked here; details from search excerpts of BioPortal and NLM pages
value_chain: [provider, payer, clinical, commercial-medical]
intention_matrix: [automate-optimize, augment-optimize]
stack_layer: [data-semantics, governance-trust]
players: [consortium, buyer, isv, frontier-labs]
themes: [T1, T7]
signal: medium
---

# S008 · SNOMED CT on BioPortal

**Why I saved it:** *(add your line)*

> ⚠️ **Partial read.** bioportal.bioontology.org was blocked in this environment on 2026-10-22. Facts below come from search excerpts of the BioPortal entry and NLM pages. **[verify]** against the live page.

## TL;DR
- **SNOMED CT** is the leading clinical terminology. BioPortal hosts it as **SNOMEDCT** (current version 2025_09_01, sourced from UMLS 2025AB).
- Scale: over **1,000,000 descriptions** (including synonyms) and roughly **903,000 relationships** between concepts, per BioPortal.
- **Licensing is the GTM fine print.** Access runs through the UMLS license, issued to individuals. Use is free in SNOMED International member countries (including the US); fees can apply in non-member territories. BioPortal does not allow downloading the RDF file.

## What the source says
- **Version:** 2025_09_01, released 2025-11-03, uploaded to BioPortal 2026-03-22; earlier versions archived. Source: UMLS 2025AB.
- **Size:** >1,000,000 descriptions; ~903,000 links/semantic relationships. BioPortal doesn't show a class count.
- **License:** "This ontology is made available via the UMLS. Users of all UMLS ontologies must abide by the terms of the UMLS license." UMLS licenses are issued to individuals, not organizations.
- **Ownership and fees:** SNOMED CT is owned by SNOMED International (formerly IHTSDO). NLM is a member, so there's no charge for use in the US and other member countries. License fees and conditions apply in non-member territories (SNOMED CT Affiliate License, clauses 7 and 9).
- **Access:** browsable and queryable through BioPortal's interface and REST API. The RDF download is restricted. **[verify current policy]**
- **Releases:** NLM announces International Edition releases through 2026 (e.g., Jan, Feb, May, Sept 2026), each requiring a UMLS license and login. ([NLM Sept 2026](https://www.nlm.nih.gov/pubs/techbull/so26/brief/so26_snomed_int.html))

## Our read

**SNOMED CT is to clinical data what IDMP-O is to product data.** Together they cover the two semantic backbones an HCLS AI strategy has to touch: *what the patient has and what was done* (SNOMED CT) and *what the medicinal product is* (IDMP). In FAIR terms ([S007](S007-fair-maturity-matrix.md)), they are the "vocabularies that follow FAIR principles" that interoperability (I2) requires, which is also the capability most organizations reach last.

**Licensing is an agent-readiness issue, not just a legal footnote.** The FAIR Autonomous AI Agent persona lists "license ambiguity forcing conservative data exclusion" as a top failure mode. SNOMED CT is the textbook case: free in member countries, licensed differently elsewhere, and distributed through an individual-licensed channel. Any AI product that embeds or redistributes SNOMED CT content across borders needs a licensing position. That's a due-diligence question frontier labs and their partners will get from health system and payer legal teams.

**Provider and payer bridge.** This is the library's first source rooted in the provider and payer side. It's the semantic layer under clinical decision support, quality measurement, risk adjustment, and prior authorization: the clinical half of "governed semantics are the on-ramp" (T1).

**So what for services:** Terminology mapping and normalization (local codes → SNOMED CT, and across to other standard vocabularies) is perennial work. AI makes it faster, and validation keeps it billable. That puts it in the *automate + optimize* quadrant with human review by exception.

**So what for frontier labs:** Grounding clinical agents in SNOMED CT concepts improves precision and auditability, but labs need a clear story on license-compliant use, especially for international customers.

**Job to be done (health system CMIO / informatics lead):** When we deploy AI that reads and writes clinical data, I want it to speak standard clinical terminology, so I can trust its outputs, measure quality consistently, and exchange data without remapping.

| Current state | Future state | Gap (the offer) |
|---|---|---|
| Local codes and free text; manual terminology mapping | AI-assisted mapping to SNOMED CT with rule-based validation | Mapping accelerators; validation design |
| AI outputs in free text, hard to audit | AI outputs coded to standard concepts | Grounding and output-coding patterns for clinical AI |
| Licensing questions surface late in procurement | License-aware AI architecture from day one | Terminology licensing review in AI due diligence |

## Open questions
- What's the official current concept count for the International Edition? (A vendor terminology server lists ~529k concepts for the Feb 2026 edition, which likely includes inactive concepts; not an official figure.)
- Does SNOMED International have explicit guidance on using SNOMED CT in AI model training or retrieval? **[research]**

## Related
- [S002 · IDMP-O](S002-pistoia-idmp-o-github.md): the product-data counterpart
- [S007 · FAIR Maturity Matrix](S007-fair-maturity-matrix.md): I2 "vocabularies that follow FAIR principles"
- [NLM UMLS](https://www.nlm.nih.gov/databases/umls.html)
