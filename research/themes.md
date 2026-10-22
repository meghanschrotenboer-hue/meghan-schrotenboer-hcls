# Themes Board

*Living synthesis. v0.1 · 2026-10-22 · 6 sources*

## The big idea forming

> **In healthcare and life sciences, AI product-market fit is decided at the edges of the model, not inside it.** Below the model: governed, shared meaning (ontologies, standards, FAIR data). Above it: a designed role in a real workflow. Between them: machine-checkable rules and escalation thresholds that decide how much autonomy is safe to grant. Whoever owns those edges owns the customer.

*Confidence: low–medium. Six sources, weighted toward pharma regulatory and UX. Zero frontier-lab sources yet. See [evidence gaps](#evidence-gaps).*

---

## Evidence heatmap

● supports · ◐ supports, pending full read · blank = not addressed

| Theme | S001 | S002 | S003 | S004 | S005 | S006 | # | Confidence |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **T1** Governed semantics are the on-ramp | | ● | ● | | | | 2 | Medium |
| **T2** Design the role before the model | ◐ | | | ● | ● | ● | 4 | Medium |
| **T3** Right-size the intelligence | | ● | | ● | | ● | 3 | Medium |
| **T4** Deadlines fund it; reuse justifies it | | ● | ● | | | | 2 | Low–Med |
| **T5** Consortia are the standards *and* relationship layer | ◐ | ● | ● | | ● | | 4 | Medium |
| **T6** AI readiness is a maturity problem first | | | | | ● | | 1 | Low |

---

## T1 · Governed semantics are the on-ramp to regulated AI

**Thesis:** Regulated AI fails or scales on whether the underlying data means the same thing everywhere it flows. Shared ontologies (IDMP-O) and FAIR data are becoming the precondition, not the nice-to-have.

**Evidence**
- IDMP-O exists because "diverse, non-standard IDMP implementations" undermine the standard; it aims for interoperability "by design." ([S002](sources/S002-pistoia-idmp-o-github.md))
- More than 10 pharma companies have adopted it; J&J, BI, Merck & Co., and Amgen govern it; the next steps are knowledge graphs and implementation guides. ([S003](sources/S003-pistoia-idmp-o-info-sheet.md))

**So what, services:** Data foundation work gets reframed as *AI enablement*, not plumbing. That changes the buyer (CDO + business owner, not just IT) and the budget.
**So what, frontier labs:** Standards-aligned grounding is a credibility signal in regulated buyers.
**What would change my mind:** Evidence that LLMs perform reliably on regulated product data *without* ontology grounding (e.g., benchmarks or production case studies).

---

## T2 · Design the role before the model

**Thesis:** Buyer-side leaders are converging on "workflow first, AI second." The hard part isn't explaining what AI decides; it's designing the role it plays and the moments it hands back to a human.

**Evidence**
- UXLS: "Start with the Workflow, Not the AI." AI on a broken workflow accelerates frustration. ([S001](sources/S001-pistoia-ux-for-ai-and-ai-for-ux.md), context)
- The Intention Matrix frames feature scope as a deliberate choice of human involvement and output quality. ([S004](sources/S004-ai-intention-matrix.md))
- Agent journey maps put JTBD, agent states, and escalation logic on one artifact. ([S006](sources/S006-journey-mapping-ai-agents.md))
- UX maturity (impact, process, metrics) sets how well an org can absorb new tools. ([S005](sources/S005-uxls-maturity-model.md))

**So what, services:** Role design, journey mapping, and change management are the adoption layer. Adoption is where pilots die, so that's where buyers will pay.
**So what, frontier labs:** "Chat on top" will plateau in HCLS; workflow-embedded patterns win and mostly arrive through partners.
**What would change my mind:** Horizontal AI assistants reaching broad, sustained clinical or scientific adoption with no workflow redesign.

---

## T3 · Right-size the intelligence: satisfice vs. optimize, augment vs. automate

**Thesis:** Not every job needs the most autonomous, most precise AI. Matching each use case to its quadrant controls cost, risk, and validation scope. In regulated work, **machine-checkable rules** (ontology constraints, SHACL, competency questions) and **escalation thresholds** are what let work move safely from augment to automate.

**Evidence**
- Defaulting to full-automation, max-precision modes wastes tokens on outputs users don't need or trust. ([S004](sources/S004-ai-intention-matrix.md))
- IDMP-O ships SHACL shapes, competency questions, and retention checks, i.e., rule-based acceptance criteria. ([S002](sources/S002-pistoia-idmp-o-github.md))
- Agents escalate to humans when confidence is low; the quadrant becomes a runtime state. ([S006](sources/S006-journey-mapping-ai-agents.md))

**So what, services:** Three sellable outputs: an intention map of the client's AI backlog, documented acceptance thresholds ("good enough" written down), and escalation/validation design.
**So what, frontier labs:** Model routing by quadrant is a margin and trust lever. Calibrated confidence and clean human-handoff primitives make partners' governance work easier.
**What would change my mind:** Regulators or quality functions accepting AI outputs for regulated decisions without defined thresholds or rule-based checks.

---

## T4 · Regulatory deadlines create the budget; reuse creates the ROI

**Thesis:** Regulation (e.g., EMA PMS, June 2026) is the forcing function that funds data standardization. After the deadline, the winning pitch shifts from compliance to reuse: the same structured data powering supply chain, safety, and AI.

**Evidence**
- IDMP-O's use-case sequence tracks regulatory pressure: EMA PMS → cross-jurisdiction reporting → batch tracking → packaging. ([S002](sources/S002-pistoia-idmp-o-github.md))
- The June 2026 announcement explicitly ties the next phase to "tightening European medicines data requirements." ([S003](sources/S003-pistoia-idmp-o-info-sheet.md))

**So what, services:** BANT timing is now. Post-deadline is the window for a compliance-to-value conversation.
**So what, frontier labs:** Regulatory affairs is a near-term, budgeted HCLS entry point with defined data.
**What would change my mind:** Buyers telling us IDMP spend ended at the deadline with no reuse appetite. **[test in conversations]**

---

## T5 · Precompetitive consortia are both the standards layer and the relationship layer

**Thesis:** In life sciences, the rules of the road for AI-ready data and AI UX are being written in precompetitive consortia like Pistoia. Membership brings early access (IDMP-O releases reach funders a year before the public) and puts you in the room with buyer-side champions.

**Evidence**
- Staged access: funders immediately, members at +6 months, public at +1 year. ([S002](sources/S002-pistoia-idmp-o-github.md))
- Pharma governance roster and a not-for-profit "convene, govern, accelerate" model. ([S003](sources/S003-pistoia-idmp-o-info-sheet.md))
- UXLS produces buyer-built artifacts (maturity model, AI workstream) that shape how AI is evaluated. ([S001](sources/S001-pistoia-ux-for-ai-and-ai-for-ux.md), [S005](sources/S005-uxls-maturity-model.md))

**So what, services:** Consortium participation is a GTM channel: champions, early signal, and earned credibility. Worth evaluating membership.
**So what, frontier labs:** A neutral contributor seat (e.g., Pistoia's agentic AI standards work **[verify]**) builds trust that direct selling can't.
**What would change my mind:** Evidence that consortium standards are ignored in actual procurement decisions.

---

## T6 · AI readiness is a maturity problem before it's a technology problem *(emerging)*

**Thesis:** Whether an organization can absorb AI depends on measurable maturity in UX practice and data practice. Buyer-built maturity models make a credible, low-risk entry offer.

**Evidence**
- UXLS Maturity Model: five levels; top level = UX as company strategy and business value. ([S005](sources/S005-uxls-maturity-model.md))

**Next evidence to add:** Pistoia FAIR Maturity Matrix; any data on AI pilot-to-production rates in pharma or health systems.

---

## Evidence gaps

| Gap | Why it matters | Suggested adds (see [inbox](inbox.md)) |
|---|---|---|
| **No frontier-lab sources** | Half the PMF question is unaddressed | Lab HCLS product launches, partner programs, customer case studies |
| **No provider or payer sources** | Everything so far is pharma/R&D-centric | Health system AI adoption surveys, ambient documentation evidence, payer AI use (prior auth) |
| **No first-party buyer voice** | Articles ≠ demand | Your own call notes, anonymized, logged as `type: interview` |
| **No regulator sources** | Thresholds and "intended use" are defined there | FDA and EMA AI guidance; EMA PMS roadmap |
| **No pricing or deal data** | PMF needs willingness to pay | Rate cards, RFP language, public contract values |
