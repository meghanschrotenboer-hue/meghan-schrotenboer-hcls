---
id: S004
title: "Designing AI with purpose: the AI intention matrix"
publisher: "UX Collective (uxdesign.cc); also The Ambitious Designer (Substack)"
authors: "Richard Yang (@richard.ux), self-described ex-design at Anthropic, Scale AI, Meta, Shopify"
date_published: 2025-05-09        # Substack original; UX Collective version May 2025
date_added: 2026-10-22
url: "https://uxdesign.cc/designing-ai-with-purpose-the-ai-intention-matrix-04f1ab20bd91"
type: article
access: partial                   # uxdesign.cc blocked in this environment; framework confirmed via the author's Substack and secondary write-ups
value_chain: [cross-cutting]
intention_matrix: [augment-optimize, augment-satisfice, automate-optimize, automate-satisfice]
stack_layer: [workflow-ux, commercial-model]
players: [frontier-labs, services, isv]
themes: [T2, T3]
signal: high                      # as a categorization lens; adopted as Lens 1
---

# S004 · The AI Intention Matrix (Optimizing vs. Satisficing)

**Why I saved it:** Categorization patterns like **optimizing vs. satisficing**. *(expand in your words)*

> ⚠️ **Partial read.** uxdesign.cc was blocked in this environment on 2026-10-22. The two axes and the cost argument are confirmed across the author's Substack and secondary coverage. **Quadrant names come from a secondary write-up [verify against the original].**

## TL;DR
- A 2×2 for deciding **what an AI feature should be** before building it: **Augmentation ↔ Automation** (how involved the human stays) × **Satisficing ↔ Optimizing** (whether the output must be the best possible or just good enough).
- **Neither end is inherently better.** The right cell depends on context, stakes, and user preference.
- The argument is **economic** as much as experiential: features that default to high-precision, full-automation modes drain tokens and compute on outputs users don't need or trust.

## What the source says
- **Axis 1, Augmentation ↔ Automation:** human-in-the-loop assistance vs. AI acting on its own.
- **Axis 2, Satisficing ↔ Optimizing:** "good enough" output vs. "best possible" output.
- **Quadrants** (as named in secondary coverage **[verify]**):
  - **Augmentation + Optimizing → High-stakes co-pilots** (e.g., clinical diagnosis aids, legal research, financial advice: AI improves critical decisions, humans stay involved)
  - **Augmentation + Satisficing → Everyday AI assistants**
  - **Automation + Optimizing → Autonomous precision**
  - **Automation + Satisficing → Autonomous utility**
- **Purpose:** guide design decisions on the *scope and function* of AI features; use resources more efficiently by minimizing token and compute waste.
- **Background:** *satisficing* is Herbert Simon's decision-theory term for stopping the search once an option meets the standard. It is not settling for mediocrity.

## Quotable
> Neither end of the spectrum is inherently better; the choice depends on context, stakes, and user preferences. *(paraphrase; pull exact line when accessible)*

## Our read

**Why this lens is so useful for HCLS:** healthcare buyers already think this way; they just use different words. "Intended use," "risk-based validation," "clinician in the loop," and "fit for purpose" all map to the matrix. That makes it a **translation layer between AI product language and regulated-buyer language**, which is exactly where a services firm with buyer-side experience earns its keep.

**Three extensions for regulated industries:**
1. **"Good enough" must be written down.** In GxP and clinical contexts, satisficing means meeting a *documented acceptance threshold tied to intended use*. Defining that threshold is real work and a real deliverable.
2. **Rules unlock automation.** Moving from augment to automate in regulated work needs machine-checkable acceptance criteria. Ontology constraints like IDMP-O's SHACL shapes and competency questions ([S002](S002-pistoia-idmp-o-github.md)) are one example.
3. **The quadrant can be a runtime state, not a fixed label.** Confidence- and risk-based escalation ([S006](S006-journey-mapping-ai-agents.md)) lets one agent run *automate + satisfice* on routine cases and drop into *augment + optimize* on edge cases.

**So what for services:** The matrix is a ready-made **discovery and scoping tool**. Plot a client's AI backlog on it in a workshop and you get (a) a sequencing plan (start with augment + satisfice wins, build trust, then move right), (b) a cost conversation (stop paying optimize prices for satisfice jobs), and (c) a validation scope (the augment + optimize and automate + optimize cells drive the CSV and governance work).

**So what for frontier labs:** It's a pricing and packaging lens. Satisfice workloads favor smaller, cheaper models and high volume. Optimize workloads justify premium models, longer reasoning, and partner-delivered validation. Labs that help customers route work to the right cell protect margin and trust at the same time.

**Job to be done (AI product owner at a pharma or health system):** When I have 40 AI ideas and a fixed budget, I want a simple way to decide how autonomous and how precise each one needs to be, so I can fund the right ones and not over-engineer the rest.

| Current state | Future state | Gap (the offer) |
|---|---|---|
| AI backlog prioritized by enthusiasm; every use case scoped "fully autonomous, maximum accuracy" | Backlog plotted by intention; cost, validation, and UX matched to the quadrant | Intention-mapping workshop; acceptance-threshold definitions; model-routing design |

## Open questions
- Does the original article give HCLS or other regulated examples beyond the clinical co-pilot mention?
- Is there a third dimension worth adding for HCLS, such as **reversibility** (can the action be undone?) or **regulatory exposure**?

## Related
- [Lens 1 in lenses.md](../lenses.md#lens-1--ai-intention-matrix-augment--automate--satisfice--optimize): HCLS overlay
- Secondary: [The AI Intention Matrix (AIIM): When to use AI and when not!](https://medium.com/design-bootcamp/the-ai-intention-matrix-aiim-when-to-use-ai-and-when-not-74facc407099) *(similar name; may be a separate framework, verify)*
- Background: [When you're overthinking your UX: Satisficing vs Maximizing](https://uxplanet.org/when-youre-overthinking-your-ux-satisficing-vs-maximizing-1096e9d702b1)
