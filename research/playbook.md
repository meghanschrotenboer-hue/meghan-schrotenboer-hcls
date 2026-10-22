# Playbook: Working Faster and Presenting Findings

## Working faster

1. **Paste the link plus one line of "why."** Your reason for saving something is the most valuable metadata in the library, because it's the part nobody else can write. Everything else (summary, tags, theme links) can be drafted for you.
2. **Batch it.** Drop five or ten links into [inbox.md](inbox.md) or a single chat message, then say "process the inbox." It's one pass, one commit, and themes get updated once instead of piecemeal.
3. **Use the `/add-source` skill** in this repo (`.claude/skills/add-source/`). It runs the same steps every time: note from template → lens tags → index row → theme and heatmap update → commit.
4. **Upload PDFs directly** when a site is gated, paywalled, or blocked. A PDF in chat beats a summary from search snippets every time.
5. **Keep "what the source says" separate from "our read."** Every note has both sections. When you present to a client or a frontier lab, you can cite facts with confidence and own the interpretation as yours.
6. **Run a weekly 15-minute "refresh themes."** Ask Claude to re-read all notes, update the heatmap and confidence levels, and flag any theme resting on a single source as fragile.
7. **Log your own conversations.** Anonymized discovery-call notes logged as `type: interview` are first-party evidence, the strongest PMF signal you can collect.
8. **Pressure-test before you publish.** When a hypothesis in [pmf.md](pmf.md) reaches medium confidence, run it through the **WEDGE research skill** (falsification-first) to see whether it survives scrutiny.
9. **Watch your coverage, not just your count.** The [INDEX coverage snapshot](INDEX.md#coverage-snapshot) shows where the evidence is thin (today: frontier labs, clinical, payer, models). Use it to steer what you read next.

## Unblocking sources

This cloud environment's network policy currently blocks most research sites (so far: **pistoiaalliance.org** and its subdomains, **uxdesign.cc**, **medium.com**, **edmcouncil.org**, **bioportal.bioontology.org**), so those sources were captured from search excerpts rather than read in full. Public GitHub repositories *do* work, which is how IDMP-O and the FAIR Maturity Matrix were read in full. Two fixes:
- **Quickest:** upload the PDF or paste the article text in chat.
- **Durable:** add the domains under the environment's **Network access** settings (cloud environment menu in the session title bar → Edit → Allowed domains). Steps: <https://code.claude.com/docs/en/cloud-environments#network-access>. Worth allowing: `pistoiaalliance.org`, `pistoiaalliance.github.io`, `fairtoolkit.pistoiaalliance.org`, `pistoiaalliance.atlassian.net`, `edmcouncil.org`, `bioportal.bioontology.org`, `uxdesign.cc`, `medium.com`, `substack.com`, `uxmatters.com`.

## Ways to present the findings

| Format | What it shows | Best for |
|---|---|---|
| **1. HCLS Intention Matrix wall** | Every use case found in the research plotted on the augment/automate × satisfice/optimize grid, colored by value-chain stage, with "services-heavy" vs. "product-led" zones shaded | The signature visual; workshops; frontier-lab partner conversations |
| **2. Evidence heatmap** | Themes × sources, showing where conviction is earned and where it's thin | Leadership readouts; keeping yourself honest |
| **3. AI readiness four-box** | Data maturity (FAIR) × UX maturity (UXLS), accounts plotted | Account tiering; qualification; an entry offer |
| **4. Theme cards** | One page per theme: thesis, three proof points, so-what for services and for labs, "what would change our mind" | Executive decks; LinkedIn thought leadership series |
| **5. Gap → offer ladder** | Current state → future state → gap, with each gap converted to a named offer | Offer design; practice strategy |
| **6. "Why now" timeline** | Regulatory deadlines, standards releases, and lab launches on one timeline | Opening slide for buyer conversations (BANT timing) |
| **7. Two cuts, one evidence base** | The same research packaged twice: a services cut (offers, ICP, MEDPICC) and a frontier-lab cut (where labs need partners) | Internal strategy and external partnership pitches |
| **8. The standards stack** | One layered diagram: FAIR principles → maturity models (FAIR MM, DCAM, UXLS) → semantic standards (IDMP-O, SNOMED CT) → implementations (Roche RDP) → AI (agents, Intention Matrix). Shows where each offer and each partner sits | Explaining "why data before AI" in one picture |
| **9. Junkyard → online store** | Borrow the FAIR Maturity Matrix's marketplace metaphor (junkyard, flea market, street market, local market, hypermarket, online store) and overlay what AI each level can support | Executive storytelling; memorable and buyer-built |
| **10. Living dashboard** | A private web page that reads the notes' tags and redraws the heatmap and matrix as you add sources | Ongoing use; sharing a link instead of a deck |

*For anything presented under the evolv name, apply the evolv brand standards when producing the final version.*
