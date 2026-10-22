---
id: S003
title: "IDMP Ontology Information Sheet"
publisher: "Pistoia Alliance"
authors: "Pistoia Alliance"
date_published: 2026-08-06
date_added: 2026-10-22
url: "https://pistoiaalliance.org/wp-content/uploads/2026/08/2026-08-06_IDMP-Ontology-Information-Sheet.pdf"
type: report
access: partial                   # PDF host blocked; content below from the web version and June 2026 press coverage
value_chain: [regulatory-cmc]
intention_matrix: [automate-optimize]
stack_layer: [data-semantics, governance-trust, commercial-model]
players: [consortium, buyer, isv, services]
themes: [T1, T4, T5]
signal: high
---

# S003 · IDMP Ontology Information Sheet (Aug 2026), with the June 2026 Stewardship Announcement

**Why I saved it:** *(add your line)*

> ⚠️ **Partial read.** The PDF host was blocked in this environment on 2026-10-22. The points below come from the information sheet's web listing and from the 10 June 2026 press release and trade coverage. Items marked **[verify]** should be checked against the PDF itself.

## TL;DR
- Pistoia positions IDMP-O as **the pharmaceutical industry's directly deployable implementation layer for the ISO IDMP standards**: vendor-neutral and expert-built. **[verify exact wording]**
- In June 2026, Pistoia moved IDMP-O into **long-term stewardship**: Accurids does maintenance under a **three-year engineering partnership** with guaranteed quarterly releases, and pharma members govern it.
- The commercial trigger is the **EMA Product Management System (PMS)** submission deadline (June 2026), framed as "tightening European medicines data requirements."

## What the source says
- **Positioning:** an expert-built, vendor-neutral framework. Pistoia describes itself as a not-for-profit that *convenes, governs, and accelerates* shared standards and tools rather than selling products. The sheet also serves as a plain-language introduction for regulators and industry teams. ([info sheet listing](https://pistoiaalliance.org/resource-library/idmp-ontology-information-sheet/)) **[verify]**
- **Stewardship (10 June 2026):** Accurids provides maintenance. Governance is overseen by members including **Johnson & Johnson, Boehringer Ingelheim, Merck & Co., Amgen, and Global Value Web**. ([press release](https://pistoiaalliance.org/news/pistoia-alliance-advances-idmp-ontology/))
- **Adoption:** "more than 10 pharmaceutical companies" have adopted the framework. (press release)
- **Funding/operations:** a three-year engineering partnership with Accurids, in place as of May 2026, guarantees quarterly releases and continuous improvement. ([project page](https://pistoiaalliance.org/project/idmp-o/))
- **Next steps from the steering committee:** simplified vocabularies, **knowledge graphs**, and **implementation guides** to lower technical barriers. (press release)
- **Coverage:** all five ISO IDMP standards. ([IDMP-O 1.0 launch](https://pistoiaalliance.org/news/press-release-pistoia-alliance-launches-idmp-1-0/))
- **Regulatory driver:** the EMA PMS deadline in June 2026 for manufacturers to submit standardized medicinal product data. (press release; [Discover Pharma](https://discover-pharma.com/pistoia-idmp-ontology-ema/); [FirstWord Pharma](https://firstwordpharma.com/story/7542418))

## Our read

**Timing is the story.** The EMA deadline has now passed (June 2026). Most companies likely met it tactically. The next budget conversation shifts from *"are we compliant?"* to *"why are we paying to maintain this data twice?"* That's the opening for a **compliance-to-value pivot**: reuse IDMP-structured product data for supply chain traceability, safety, and AI. **[hypothesis; test with buyer conversations]**

**Governance roster = target list.** J&J, BI, Merck & Co., and Amgen are governing the standard. Their IDMP-O owners are, by definition, the internal champions for semantic product data. That's a ready-made MEDPICC "Champion" hypothesis for each account.

**The "implementation guides + knowledge graphs" next step** is the steering committee admitting the gap between a published ontology and a running system. That gap is services territory.

**So what for services:** Lead with the post-deadline reuse story, not compliance. Offer: IDMP-O-aligned product knowledge graph on the client's data platform, AI-assisted source mapping with rule-based validation, and a stewardship operating model.

**So what for frontier labs:** Regulatory affairs buyers are being trained to value *vendor neutrality and governance*. A lab showing up with standards-aligned grounding (IDMP-O as context) and partner-delivered validation will read as credible. One showing up with a generic chatbot will not.

**Job to be done (CDO in pharma):** When we've just spent heavily to meet a regulatory data deadline, I want that structured product data to become a reusable enterprise asset, so I can show the board a return beyond avoided penalties.

| Current state | Future state | Gap (the offer) |
|---|---|---|
| PMS submission met by a tactical, regulatory-owned data effort | Product data governed once, reused across regulatory, supply, safety, AI | Enterprise ownership model; IDMP-O knowledge graph; reuse business case |
| Ontology published but hard to implement | Implementation guides and reference architectures | Accelerators, reference implementations on common data platforms |

## BANT / MEDPICC quick map (for an IDMP reuse conversation)
- **Metrics:** cost to maintain product data per submission; time to answer cross-jurisdiction product queries; batch trace time
- **Economic buyer:** CDO / Head of Regulatory Ops jointly (that ownership seam is itself a pain)
- **Decision criteria:** vendor-neutral, ISO-aligned, platform-agnostic, validated
- **Decision process:** steering-committee culture; consortium membership matters
- **Paper process:** Quality/CSV sign-off for anything touching regulated data
- **Identify pain:** duplicate data maintenance; jurisdiction-by-jurisdiction rework
- **Champion:** the company's IDMP-O / ontology lead
- **Competition:** RIM platform vendors' native modules; Big Four regulatory practices; in-house

## Open questions
- What exactly did EMA require by June 2026, and what's next on the PMS roadmap (the next forcing function)? **[verify with EMA sources]**
- Who are the >10 adopters beyond the governing members?

## Related
- [S002 · IDMP-O repository and release notes](S002-pistoia-idmp-o-github.md)
- Pistoia event: [Navigating the New IDMP Era: Data Quality, Ontologies, and AI-Powered Compliance](https://pistoiaalliance.org/eventdetails/navigating-the-new-idmp-era-data-quality-ontologies-and-ai-powered-compliance/)
- [Accurids](https://accurids.com/): IDMP-O maintenance partner
