# Themes Board

*Living synthesis. v0.2 · 2026-10-22 · 10 sources*

## The big idea forming

> **In healthcare and life sciences, AI product-market fit is decided at the edges of the model, not inside it.** Below the model: governed, shared meaning (ontologies, standards, FAIR data). Above it: a designed role in a real workflow. Between them: machine-checkable rules and escalation thresholds that decide how much autonomy is safe to grant. **And the newest consumer of all that data is the agent itself.** Whoever owns those edges owns the customer.

*Confidence: medium on the "below the model" half (6 sources, consistent), low–medium on the rest. Caution: most evidence so far comes from standards bodies and consortia whose mission is to promote these standards. See [tensions](#tensions-to-watch) and [evidence gaps](#evidence-gaps).*

---

## Evidence heatmap

● supports · ◐ supports, pending full read · blank = not addressed

| Theme | S001 | S002 | S003 | S004 | S005 | S006 | S007 | S008 | S009 | S010 | # | Confidence |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **T1** Governed semantics are the on-ramp | | ● | ● | | | | ● | ● | ● | ● | 6 | Medium ↑ |
| **T2** Design the role before the model | ◐ | | | ● | ● | ● | ● | | | | 5 | Medium |
| **T3** Right-size the intelligence | | ● | | ● | | ● | ● | | | | 4 | Medium |
| **T4** Deadlines fund it; reuse justifies it | | ● | ● | | | | ● | | | ● | 4 | Low–Med ↑ |
| **T5** Consortia are the standards *and* relationship layer | ◐ | ● | ● | | ● | | ● | | ● | ● | 7 | Medium ↑ |
| **T6** AI readiness is a maturity problem first | | | | | ● | | ● | | ● | | 3 | Medium ↑ |
| **T7** Agents are the new data consumer *(new)* | | ● | | | | | ● | ● | | ● | 4 | Low–Med |

↑ = moved up in v0.2

---

## T1 · Governed semantics are the on-ramp to regulated AI

**Thesis:** Regulated AI fails or scales on whether the underlying data means the same thing everywhere it flows. Shared ontologies (IDMP-O for products, SNOMED CT for clinical data) and FAIR data are becoming the precondition, not the nice-to-have.

**Evidence**
- IDMP-O exists because "diverse, non-standard IDMP implementations" undermine the standard; it aims for interoperability "by design." ([S002](sources/S002-pistoia-idmp-o-github.md))
- More than 10 pharma companies have adopted it; J&J, BI, Merck & Co., and Amgen govern it; the next steps are knowledge graphs and implementation guides. ([S003](sources/S003-pistoia-idmp-o-info-sheet.md))
- The FAIR Maturity Matrix ties maturity to AI value: "quality AI training data sets for LLM" at L3–L4, "AI trusted actionability" at L5. ([S007](sources/S007-fair-maturity-matrix.md))
- SNOMED CT is the clinical counterpart: >1M descriptions and ~903k relationships, the semantic layer under provider and payer AI. ([S008](sources/S008-snomed-ct-bioportal.md))
- The EDM Association, now owner of OMG, frames its frameworks and ontologies around "AI-ready data." ([S009](sources/S009-edm-association-resources.md))
- Roche's "FAIR by design" portal shows a top-10 pharma building semantics in at the source. ([S010](sources/S010-fair-data-by-design-roche.md))

**So what, services:** Data foundation work gets reframed as *AI enablement*, not plumbing. That changes the buyer (CDO + business owner, not just IT) and the budget.
**So what, frontier labs:** Standards-aligned grounding (IDMP-O, SNOMED CT) is a credibility signal in regulated buyers.
**What would change my mind:** Evidence that LLMs perform reliably on regulated product or clinical data *without* ontology grounding (benchmarks or production case studies).

---

## T2 · Design the role before the model

**Thesis:** Buyer-side leaders are converging on "workflow first, AI second." The hard part isn't explaining what AI decides; it's designing the role it plays, including its relationships to human roles and the moments it hands back to a person.

**Evidence**
- UXLS: "Start with the Workflow, Not the AI." ([S001](sources/S001-pistoia-ux-for-ai-and-ai-for-ux.md), context)
- The Intention Matrix frames feature scope as a deliberate choice of human involvement and output quality. ([S004](sources/S004-ai-intention-matrix.md))
- Agent journey maps put JTBD, agent states, and escalation logic on one artifact. ([S006](sources/S006-journey-mapping-ai-agents.md))
- UX maturity sets how well an organization can absorb new tools. ([S005](sources/S005-uxls-maturity-model.md))
- The FAIR Maturity Matrix models an **Autonomous AI Agent as a persona** with defined relationships to Data Steward, Data Owner, and Research Scientist roles. That is role design, written by the buyer community. ([S007](sources/S007-fair-maturity-matrix.md))

**So what, services:** Role design, journey mapping, and change management are the adoption layer. Adoption is where pilots die, so that's where buyers will pay.
**So what, frontier labs:** "Chat on top" will plateau in HCLS; workflow-embedded patterns win and mostly arrive through partners.
**What would change my mind:** Horizontal AI assistants reaching broad, sustained clinical or scientific adoption with no workflow redesign.

---

## T3 · Right-size the intelligence: satisfice vs. optimize, augment vs. automate

**Thesis:** Not every job needs the most autonomous, most precise AI, and not every dataset needs to be fully FAIR. Matching each use case to its quadrant controls cost, risk, and validation scope. In regulated work, **machine-checkable rules** and **escalation thresholds** are what let work move safely from augment to automate.

**Evidence**
- Defaulting to full-automation, max-precision modes wastes tokens on outputs users don't need or trust. ([S004](sources/S004-ai-intention-matrix.md))
- IDMP-O ships SHACL shapes, competency questions, and retention checks: rule-based acceptance criteria. ([S002](sources/S002-pistoia-idmp-o-github.md))
- Agents escalate to humans when confidence is low; the quadrant becomes a runtime state. ([S006](sources/S006-journey-mapping-ai-agents.md))
- **"FAIR Enough":** the FAIR strategy dimension explicitly includes deciding what not to do, since "only some data may need to be FAIR." Satisficing, applied to data. ([S007](sources/S007-fair-maturity-matrix.md))

**So what, services:** Four sellable outputs: an intention map of the AI backlog, a matching *data* investment map ("FAIR Enough" per quadrant), documented acceptance thresholds, and escalation/validation design.
**So what, frontier labs:** Model routing by quadrant is a margin and trust lever.
**What would change my mind:** Regulators or quality functions accepting AI outputs for regulated decisions without defined thresholds or rule-based checks.

---

## T4 · Regulatory deadlines create the budget; reuse creates the ROI

**Thesis:** Regulation (e.g., EMA PMS, June 2026) is the forcing function that funds data standardization. After the deadline, the winning pitch shifts from compliance to reuse, and to building data right the first time.

**Evidence**
- IDMP-O's use-case sequence tracks regulatory pressure: EMA PMS → cross-jurisdiction reporting → batch tracking → packaging. ([S002](sources/S002-pistoia-idmp-o-github.md))
- The June 2026 announcement ties the next phase to "tightening European medicines data requirements." ([S003](sources/S003-pistoia-idmp-o-info-sheet.md))
- The FAIR business value ladder: speed and cost at L1 → reuse, "facilitated regulatory compliance and auditing," and reduced "retrospective FAIRification" at L3 → reduced time-to-market at L5. L0 strategy is FAIR applied "in response to external pressures." ([S007](sources/S007-fair-maturity-matrix.md))
- Roche's progression from retrospective FAIRification to "FAIR by design" is the reuse logic in practice. ([S010](sources/S010-fair-data-by-design-roche.md))

**So what, services:** BANT timing is now. Post-deadline is the window for a compliance-to-value conversation, and "by design" is the offer that stops the remediation tax.
**So what, frontier labs:** Regulatory affairs is a near-term, budgeted HCLS entry point with defined data.
**What would change my mind:** Buyers telling us IDMP spend ended at the deadline with no reuse appetite. **[test in conversations]**

---

## T5 · Precompetitive consortia are both the standards layer and the relationship layer

**Thesis:** In life sciences, the rules of the road for AI-ready data and AI UX are being written in precompetitive consortia. Membership brings early access and puts you in the room with buyer-side champions. The standards bodies themselves are consolidating.

**Evidence**
- IDMP-O staged access: funders immediately, members at +6 months, public at +1 year. ([S002](sources/S002-pistoia-idmp-o-github.md))
- Pharma governance roster and a not-for-profit "convene, govern, accelerate" model. ([S003](sources/S003-pistoia-idmp-o-info-sheet.md))
- UXLS produces buyer-built artifacts that shape how AI is evaluated. ([S001](sources/S001-pistoia-ux-for-ai-and-ai-for-ux.md), [S005](sources/S005-uxls-maturity-model.md))
- The FAIR Maturity Matrix was built by 20+ experts (AstraZeneca, BMS, CSL Behring, IQVIA, Novo Nordisk, and others). It treats *collaborating with precompetitive organizations* as a marker of L1 strategy maturity and names consulting firms as part of the ecosystem. ([S007](sources/S007-fair-maturity-matrix.md))
- The EDM Association acquired OMG (Oct 2025), uniting data-management frameworks and the ontology standards path IDMP-O depends on. ([S009](sources/S009-edm-association-resources.md))
- Roche publishes its FAIR cases through Pistoia's toolkit. ([S010](sources/S010-fair-data-by-design-roche.md))

**So what, services:** Consortium participation is a GTM channel: champions, early signal, earned credibility. Worth evaluating Pistoia membership (FAIR-for-Pharma and UXLS communities).
**So what, frontier labs:** A neutral contributor seat builds trust that direct selling can't.
**What would change my mind:** Evidence that consortium standards are ignored in actual procurement decisions.

---

## T6 · AI readiness is a maturity problem before it's a technology problem

**Thesis:** Whether an organization can absorb AI depends on measurable maturity across leadership, strategy, roles, processes, knowledge, tools, and UX practice, not just technology. Buyer-built maturity models make a credible, low-risk entry offer.

**Evidence**
- UXLS Maturity Model: five levels; top level = UX as company strategy and business value. ([S005](sources/S005-uxls-maturity-model.md))
- FAIR Maturity Matrix: seven organizational dimensions; only two (data, tools) are technical. ([S007](sources/S007-fair-maturity-matrix.md))
- DCAM: the enterprise data-management maturity standard CDOs already know. ([S009](sources/S009-edm-association-resources.md))

**So what, services:** A combined **UXLS × FAIR MM × DCAM** readiness assessment is credible because none of the frameworks are yours.
**What would change my mind:** Evidence that maturity scores don't predict AI pilot-to-production success.

---

## T7 · Agents are the new data consumer *(new in v0.2)*

**Thesis:** Enterprise data is now being designed for a consumer that can't ask a colleague. Agents need persistent identifiers, machine-readable access policies, clear licenses, provenance, and shared vocabularies. Data that's findable *by people* isn't enough; it has to be actionable *by machines*. The catch: interoperability is the last FAIR capability most organizations reach.

**Evidence**
- The FAIR Maturity Matrix defines an **Autonomous AI Agent persona** whose success depends on "the FAIR characteristics of the underlying data." Its failure modes are identifier fragmentation, manual access gates, provenance voids, and license ambiguity. "FAIR principles are operational substrate enabling autonomous multi-agent coordination." Interoperability typically arrives at **L4**. ([S007](sources/S007-fair-maturity-matrix.md))
- IDMP-O's SHACL shapes and competency questions let machines verify data without human review. ([S002](sources/S002-pistoia-idmp-o-github.md))
- SNOMED CT licensing (free in member countries, licensed elsewhere, individual UMLS licenses) is a real-world case of "license ambiguity" agents must handle. ([S008](sources/S008-snomed-ct-bioportal.md))
- Roche's single FAIR-compliant portal and API, with automated FAIR assessment, is the kind of integration surface agents need. ([S010](sources/S010-fair-data-by-design-roche.md))

**So what, services:** "Agent-ready data" is a fundable reframe of FAIR. Offer an agent-readiness review of priority data domains: identifiers, machine-readable access policies, licenses, provenance, and catalog/API surface.
**So what, frontier labs:** The buyer community has effectively published a requirements spec for agent-ready enterprise data. Labs that make agents respect machine-readable policies and licenses, and that connect at the catalog layer, will clear governance review faster.
**What would change my mind:** Agents performing reliably at scale on non-FAIR enterprise data through retrieval alone, without identifiers, provenance, or policy metadata.

---

## Tensions to watch

1. **Proponent bias.** Nearly all ten sources come from standards bodies, consortia, or practitioners advocating for these approaches. The direction is consistent, but independent evidence (ROI studies, failed-without-FAIR case studies, analyst data) is missing.
2. **Illustrative vs. measured.** The FAIR agent persona's figures (">90%" autonomous completion, "40% data loss") are scenario claims, not cited studies. Don't quote them as facts without a source.
3. **Sequencing.** Agents need interoperability most, yet it matures last (L4). Is that a services opportunity, or a reason agentic AI in pharma stalls for years? Probably both, depending on the account.

## Evidence gaps

| Gap | Why it matters | Suggested adds (see [inbox](inbox.md)) |
|---|---|---|
| **No frontier-lab sources** | Half the PMF question is unaddressed | Lab HCLS product launches, partner programs, customer case studies |
| **Thin provider and payer coverage** | One source (S008) so far | Health system AI adoption surveys, ambient documentation evidence, payer AI use |
| **No independent / outcome evidence** | Counters proponent bias | FAIR-Decide cost-benefit framework; EDM Pharma/Life Sciences benchmark report; analyst data |
| **No first-party buyer voice** | Articles ≠ demand | Your own call notes, anonymized, logged as `type: interview` |
| **No regulator sources** | Thresholds and "intended use" are defined there | FDA and EMA AI guidance; EMA PMS roadmap |
| **No pricing or deal data** | PMF needs willingness to pay | Rate cards, RFP language, public contract values |
