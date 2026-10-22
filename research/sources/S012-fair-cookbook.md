---
id: S012
title: "The FAIR Cookbook, incl. recipe FCB081 'Changing culture with the Dataset Maturity Model'"
publisher: "ELIXIR / FAIRplus (IMI public-private project); hosted at faircookbook.elixir-europe.org"
authors: "76 listed authors; affiliations include Janssen, AstraZeneca, Boehringer Ingelheim, Novartis, GSK, Bayer, The Hyve, Fraunhofer, EMBL-EBI, University of Oxford, Maastricht University, ELIXIR"
date_published: 2026-07-12       # latest repository commit
date_added: 2026-10-22
url: "https://faircookbook.elixir-europe.org/content/recipes/maturity.html"
type: standard
access: read-in-full              # via the public GitHub repository
value_chain: [discovery, clinical, cross-cutting]
intention_matrix: [automate-optimize]
stack_layer: [data-semantics, governance-trust]
players: [consortium, buyer, services]
themes: [T1, T3, T5, T6]
signal: medium
---

# S012 · The FAIR Cookbook (and the Dataset Maturity Model)

**Why I saved it:** FAIR cookbook. *(expand in your words)*

Repository: [FAIRplus/the-fair-cookbook](https://github.com/FAIRplus/the-fair-cookbook) (CC BY 4.0)

## TL;DR
- **Hands-on recipes** for making life-sciences data FAIR, organized by Findability, Accessibility, Interoperability, Reusability, assessment, infrastructure, and applied examples. Built by a public-private team that includes six large pharma companies.
- The **maturity recipe (FCB081)** introduces the **FAIRplus Dataset Maturity Model (DSM)**, a *dataset-level* model that complements the *organization-level* FAIR Maturity Matrix ([S007](S007-fair-maturity-matrix.md)).
- Its stated purpose is to help teams "**decide how far to go on a FAIR journey**" and "**manage expectations (and costs)**." That's satisficing, applied to datasets.

## What the source says
- FAIR Cookbook: "Practical Guidance on how to make data FAIR and move through data maturity levels." CC BY 4.0. Last commit 2026-07-12.
- **FCB081 abstract:** introduces the FAIRplus Dataset Maturity Model and shows how to use it "in the context of a FAIRification process to decide how far to go on a FAIR journey." Every recipe is anchored to the model, so recipes "can be assembled to build a coherent path." The DSM "provides a handy tool for data managers to advise on changing the culture of data management but also manage expectations (and costs) when devising a FAIRification program."
- **Lineage:** builds on the Capability Maturity Model Integration (CMMI) and Technology Readiness Levels from engineering, the DAMA-DMBOK for data management, and the Research Data Alliance FAIR maturity indicators.
- **Recipe cards** carry DSM indicators, so readers know what maturity level a recipe gets them to.
- **Measured intervention:** FAIRplus assessed 20 projects before and after FAIRification (mostly retrospective, a few prospective) using a manual DSM template. Assessors were trained and inter-rater agreement was checked, which led to refined definitions. An example shows before/after effects on an IMI eTOX dataset.
- **Contributors:** 76 listed authors. Pharma affiliations include Janssen, AstraZeneca, Boehringer Ingelheim, Novartis, GSK, and Bayer.

## Our read

**Three maturity models, three altitudes.** The library now holds a coherent stack:
- **Organization:** FAIR Maturity Matrix ([S007](S007-fair-maturity-matrix.md)) and DCAM ([S009](S009-edm-association-resources.md))
- **Dataset:** FAIRplus DSM (this source)
- **Adoption / UX:** UXLS ([S005](S005-uxls-maturity-model.md))

A services assessment can score all three without inventing a proprietary framework.

**"How far to go" is the recurring idea.** "FAIR Enough" ([S007](S007-fair-maturity-matrix.md)), "decide how far to go... manage expectations (and costs)" (DSM), and satisficing ([S004](S004-ai-intention-matrix.md)) are the same discipline at three levels. That makes **T3** one of the most durable themes in the library.

**Inter-rater agreement is a credibility detail worth borrowing.** FAIRplus trained assessors and tested consistency. A services maturity assessment that does the same is defensible in front of pharma quality and data-governance teams.

**So what for services:** The Cookbook is free, pharma-co-authored IP. Package it: a dataset maturity baseline using the DSM, a recipe-based roadmap to the target level (only as far as the use case needs), and before/after measurement. It's credible because the buyer helped write it.

**So what for frontier labs:** Recipes are machine-readable, structured guidance, a natural knowledge source for agents that help data stewards FAIRify data. "AI-assisted FAIRification" grounded in the Cookbook is a plausible co-build with a partner.

**Job to be done (R&D data manager):** When I'm asked to "make our data FAIR" with a limited budget, I want a recognized way to set a target maturity per dataset and a recipe-by-recipe path to reach it, so I can deliver what the use case needs without overspending.

| Current state | Future state | Gap (the offer) |
|---|---|---|
| "Make it FAIR" with no target level | Target DSM level per dataset, tied to use case | Dataset maturity baseline and target setting |
| Ad hoc FAIRification | Recipe-based, assessed, repeatable path | Recipe-driven roadmap; before/after measurement |
| Assessments vary by assessor | Trained, calibrated assessments | Assessor training; inter-rater calibration |

## Open questions
- What are the DSM's level definitions in detail? (See the [FAIRplus Data-Maturity site](https://fairplus.github.io/Data-Maturity/).)
- Is the Cookbook still actively maintained post-FAIRplus? The last commit (July 2026) suggests yes; ELIXIR now hosts it.

## Related
- [S007 · FAIR Maturity Matrix](S007-fair-maturity-matrix.md): organization-level counterpart; cites the FAIR Cookbook and FAIRplus DSM in its lexicon
- [S004 · AI Intention Matrix](S004-ai-intention-matrix.md): satisficing
- [S010 · FAIR data by design](S010-fair-data-by-design-roche.md): prospective vs. retrospective FAIRification
