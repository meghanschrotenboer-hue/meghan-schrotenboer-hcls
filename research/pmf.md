# Product-Market Fit Canvas: AI in HCLS

*Two vantage points on one market: **services firms** and **frontier labs**, and the seam between them. v0.1 · 2026-10-22*

Every hypothesis below links to evidence in [sources/](sources/) and names what would kill it. Confidence moves only when evidence moves.

---

## A · Services (the evolv lens)

**Target customer:** Pharma and biotech data, regulatory, and R&D digital leaders; health system CDAO, CMIO/CNIO; payer digital product owners.

**Core job to be done:**
*When my organization is under pressure to "do AI" in regulated workflows, I want a partner who speaks both AI and my compliance reality, so I can get value into production without creating audit, safety, or adoption risk.*

| Current state | Future state | Gaps → offers |
|---|---|---|
| AI pilots launched by enthusiasm, scoped "fully autonomous, max accuracy" | Backlog sequenced by intention quadrant; cost and validation matched to stakes | **Intention-mapping workshop** (S004) |
| Data duplicated across systems; standards met tactically per deadline | Governed, ontology-aligned data reused across regulatory, supply, AI | **IDMP-O knowledge graph + reuse roadmap** (S002, S003) |
| Agents specified as features; escalation logic implicit | Journey maps with agent states and escalation thresholds signed off by clinical/quality | **Agent journey mapping + threshold design** (S006) |
| Readiness assumed, not measured | UX and data maturity assessed against buyer-built models | **AI-readiness assessment (UXLS × FAIR)** (S005) |

### Hypotheses

| # | Hypothesis | Evidence for | Evidence needed | Kill signal | Confidence |
|---|---|---|---|---|---|
| **H1** | HCLS buyers buy AI-readiness work faster when it's framed through **buyer-built standards** (IDMP-O, UXLS, FAIR) than through generic "AI strategy." | S002, S003, S005 | Buyer interviews; RFP language; win/loss notes | Buyers don't recognize or value the standards | Low–Med |
| **H2** | The highest-value services work sits in the **optimize** quadrants (validation, rules, escalation design), not in satisfice-quadrant deployment. | S004, S006, S002 | Deal sizes by use-case type; rate cards | Optimize-quadrant work gets absorbed by product vendors | Low–Med |
| **H3** | Post–EMA PMS deadline (June 2026), pharma data and regulatory leaders are open to a **compliance-to-value** reuse pitch over the next 2–4 quarters. | S003 | EMA PMS roadmap; conversations with IDMP-O adopters | IDMP budgets closed at the deadline | Low |

---

## B · Frontier labs

**Target customer (for the lab):** Enterprise HCLS buyers (pharma R&D and regulatory, health systems, payers) plus the partners who deliver into them.

**Core job to be done (lab's buyer):**
*When I deploy a frontier model into a regulated workflow, I want it grounded in my domain's standards and honest about its confidence, so I can let it act where it's safe and hand off where it isn't.*

| Current state | Future state | Gaps |
|---|---|---|
| General-purpose assistants piloted horizontally | Workflow-embedded agents with standards-aligned grounding | Domain grounding (ontologies as context), reference integrations |
| Confidence and handoff left to each customer to build | Calibrated confidence and human-handoff primitives as platform features | Escalation primitives; audit trails |
| One premium model for every job | Routing by intention quadrant (cheap for satisfice, premium for optimize) | Packaging and pricing by quadrant |

### Hypotheses

| # | Hypothesis | Evidence for | Evidence needed | Kill signal | Confidence |
|---|---|---|---|---|---|
| **H4** | Labs win HCLS enterprise when they ship **standards-aligned grounding + confidence/escalation primitives** and rely on partners for validation and workflow. | S002, S004, S006 (indirect) | Lab HCLS launches; partner program terms; customer case studies | Labs win large HCLS deals direct with no partner layer | Low |
| **H5** | **Satisfice-quadrant** HCLS workloads commoditize fast; lab differentiation concentrates in **optimize-quadrant** work where reasoning quality and trust matter. | S004 | Pricing trends; usage mix data | Satisfice workloads remain the main revenue driver at premium prices | Low |

---

## C · The seam: where services and labs meet

**Hypothesis H6:** In HCLS, **whoever owns the workflow, validation, and escalation layer owns the customer relationship.** Labs need that layer to land regulated deployments; services firms need lab access and co-sell to differentiate. The partnership is structural, not optional.

| | Labs bring | Services bring |
|---|---|---|
| **Capability** | Models, agent platforms, rapid capability gains | Workflow and role design, validation, change management, data foundations |
| **Credibility** | Technical frontier | Buyer-side trust, regulatory fluency, relationships |
| **Economics** | Consumption revenue | Implementation and run services |

*Evidence for H6: thin (inferred from T2, T3). Needed: lab partner program details, SI alliance announcements, joint case studies.*

---

## Positioning notes (domain-expert lens)

Use these where the research supports a right-to-win claim:
- **Speak buyer dialect:** translate the Intention Matrix into "intended use," "risk-based validation," and "clinician in the loop." (S004)
- **Lead with standards the buyer built** rather than proprietary frameworks: IDMP-O, UXLS, FAIR. (S002, S003, S005)
- **Make escalation visible:** an agent journey map is a governance artifact quality teams can sign. (S006)
- **Sell the edges, not the model:** governed meaning below, designed role above. (themes.md, "the big idea")
