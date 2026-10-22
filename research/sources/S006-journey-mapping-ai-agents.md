---
id: S006
title: "Journey Mapping for AI Agents: Designing Empathetic Interactions in the Age of Intelligence"
publisher: "Medium; republished on UXmatters (April 2026)"
authors: "Ranjan Nigam"
date_published: 2026-02-20
date_added: 2026-10-22
url: "https://medium.com/@ranjan.nigam/journey-mapping-for-ai-agents-097e7d3d59fc"
type: article
access: partial                   # medium.com blocked here; structure confirmed via search excerpts of both versions
value_chain: [cross-cutting, provider]
intention_matrix: [automate-satisfice, augment-optimize]
stack_layer: [workflow-ux, governance-trust]
players: [services, frontier-labs, isv]
themes: [T2, T3]
signal: medium
---

# S006 · Journey Mapping for AI Agents (AI Behavior Flows)

**Why I saved it:** AI behavior flows, journey mapping. *(expand in your words)*

> ⚠️ **Partial read.** medium.com was blocked in this environment on 2026-10-22. The points below come from search excerpts of the Medium original and the [UXmatters republication](https://www.uxmatters.com/mt/archives/2026/04/journey-mapping-for-ai-agents-designing-empathetic-interactions-in-the-age-of-intelligence.php). Verify details against the full text.

## TL;DR
- Extends the classic customer journey map to **map what the agent does, thinks, and decides** alongside what the human experiences.
- Describes a **five-step AI behavior flow** handled by specialized agents: **Perception → Reasoning → Prediction → Conversation → Coordination**.
- Puts **decision logic** on the map itself: **confidence, risk, and escalation rules**, including handing the case to a person when confidence is low.

## What the source says
- **The behavior flow (example):** a *perception* agent reads inputs (e.g., images or readings) → a *reasoning* agent checks them against baselines → a *prediction* agent looks for anomalies → a *conversation* agent explains the findings → a *coordination* agent raises alerts or **escalates to a human when confidence is low**.
- **Core components of an agent journey map** (UXmatters version): **user jobs to be done**, **agent inputs**, **agent states**, and **decision logic** (confidence, risk, escalation rules).
- Framing: designing *empathetic* interactions as agents take on more of the journey.

## Our read

**This is the operational partner to the Intention Matrix.** The matrix ([S004](S004-ai-intention-matrix.md)) says *where* a use case should sit. The agent journey map shows *how* it moves between cells at runtime: routine, high-confidence cases run automated, while low-confidence or high-risk cases escalate to a human in an augmented mode. The escalation rule is the quadrant boundary.

**It speaks HCLS natively.** The example flow (readings → baseline → anomaly → explain → alert or escalate) reads like remote monitoring or clinical surveillance. "Escalate when confidence is low" is what clinical safety and quality teams will ask for first. A journey map that makes escalation logic visible is a **validation and governance artifact**, not just a design artifact.

**JTBD is built into the method,** which makes this an easy fit for a JTBD-led discovery practice.

**So what for services:** Package "agent journey mapping" as a discovery deliverable. One workshop produces the user JTBD, the agent states, and the escalation thresholds, which feed the build, the validation plan (what gets tested at each threshold), and the change plan (what humans do differently). This turns abstract "agentic AI" pitches into a concrete artifact clinical and quality stakeholders can sign off on.

**So what for frontier labs:** Multi-agent patterns (perception, reasoning, prediction, conversation, coordination) map onto how labs pitch agent platforms. The HCLS differentiator is first-class **escalation and confidence handling**. Labs that expose calibrated confidence and clean human-handoff primitives make partners' governance work far easier.

**Job to be done (CNIO / clinical ops leader):** When an AI agent starts monitoring patients or triaging work, I want to see exactly when it acts alone and when it hands off to my team, so I can trust it, staff around it, and defend it to quality and risk.

| Current state | Future state | Gap (the offer) |
|---|---|---|
| Agent pilots specified as features; escalation logic buried in code or missing | Journey map shows agent states and escalation thresholds, signed off by clinical and quality teams | Agent journey mapping workshop; threshold calibration; human-handoff design; monitoring |

## Open questions
- Does the article address how thresholds get set and validated (clinical evidence, retrospective data)?
- Is the example explicitly healthcare, or general-purpose? **[verify]**

## Related
- [S004 · AI Intention Matrix](S004-ai-intention-matrix.md)
- [Agent Journey Map: Designing Software for AI Agents (Leonie Monigatti)](https://www.leoniemonigatti.com/blog/agent-experience.html): a different take that maps the *agent's* own experience as a user of software. Possible add.
