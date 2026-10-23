# HCLS × AI Research Library

A living evidence base for one question: **where is AI finding product-market fit in healthcare and life sciences, and what does that mean for services firms and frontier labs?**

*Started 2026-10-22 · 24 sources · 9 themes · 3 analyses*

## Start here

| File | What it's for |
|---|---|
| [themes.md](themes.md) | **The synthesis.** The big idea forming, the evidence heatmap, each theme with so-whats, and evidence gaps |
| [pmf.md](pmf.md) | **The PMF canvas.** JTBD, current/future/gap, and testable hypotheses for services, frontier labs, and the seam between them |
| [INDEX.md](INDEX.md) | **The source register.** Every source, tagged, plus a coverage snapshot |
| [lenses.md](lenses.md) | **The tagging system.** AI Intention Matrix, value chain, stack layer, player, buyer/JTBD |
| [analyses/](analyses/) | **Answers to specific questions**, built from the evidence (A001: could evolv contribute to Pistoia as a Snowflake SI? · A002: is Pistoia mutually exclusive from the Snowflake and SI world? · A003: what's missing to strengthen the thesis?) |
| [briefs/](briefs/) | **Your own research briefs**, kept verbatim (e.g., the GPT customer journey brief) |
| [prompts/](prompts/) | **Your discovery prompts**, saved so they can be rerun by segment |
| [competitors.md](competitors.md) | **The competitive landscape.** Who else sells into these problems; compete, partner, or both |
| [glossary.md](glossary.md) | **Plain-English definitions.** FAIR, ontology, SNOMED CT, IDMP, SHACL, DCAM, and more |
| [inbox.md](inbox.md) | **The drop zone.** New links, blocked sources, and suggested adds |
| [playbook.md](playbook.md) | **How to work faster** and **ways to present** the findings |
| [sources/](sources/) | One note per source, built from [_TEMPLATE.md](sources/_TEMPLATE.md) |
| [tools/coverage.py](tools/coverage.py) | Recounts tags and sources per theme: `python3 research/tools/coverage.py` |

## Adding a source

1. Paste the link (or upload the PDF) in chat with one line on why it matters, or add it to [inbox.md](inbox.md).
2. Say **"add this to the research library"**, **"process the inbox"**, or **`/add-source`**.
3. Claude creates the note, tags it, updates the index, and reports which themes it strengthened, weakened, or created.
4. Edit the **"Why I saved it"** line and the **"Our read"** section in your own voice.

## Conventions

- **IDs:** sources `S001…`, themes `T1…`, hypotheses `H1…`. Never renumber; retire instead.
- **Facts vs. interpretation:** "What the source says" is traceable; "Our read" is ours. Never mix them.
- **`[verify]`** marks anything not confirmed against the primary source.
- **Access status:** ✅ read in full · ◐ partial · ⏳ pending.
- **Privacy:** this folder is excluded from the website deployment (`.vercelignore`). It is still in the GitHub repository, so anything sensitive (client names, deal details) belongs only in a private repository.
