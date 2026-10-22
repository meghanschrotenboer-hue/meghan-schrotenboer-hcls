---
name: add-source
description: Add a link, PDF, or note to the HCLS × AI research library in research/. Use when the user shares a source for the research base, says "add this", "save this to the library", "process the inbox", or invokes /add-source.
---

# Add a source to the research library

The library lives in `research/`. Read `research/README.md` and `research/lenses.md` first if they aren't already in context.

For each new source (or each row in `research/inbox.md` → "To process"):

1. **Read it.** Fetch the URL or read the uploaded file. Public GitHub repositories can be cloned when the web page is blocked. For uploaded datasets, copy them to the scratchpad, analyze with `python3 -I`, report **aggregates only**, never commit the raw file, and never record individuals' names or attribute anonymized rows to companies. If the host is blocked or paywalled, use web search to confirm what you can, set `access: partial` or `pending`, and add a row to the inbox's "Blocked" table. Never fill gaps with guesses; mark unconfirmed items **[verify]**.
2. **Assign the next ID** (`S###`, one higher than the highest in `research/INDEX.md`). File name: `research/sources/S###-short-kebab-title.md`.
3. **Write the note from `research/sources/_TEMPLATE.md`.** Fill every front-matter field using the tag values in `lenses.md`. Keep "What the source says" (traceable, with links) strictly separate from "Our read" (interpretation, so-whats, JTBD, current/future/gap). Put the user's own words about why they saved it in "Why I saved it."
4. **Update `research/INDEX.md`:** add the row and refresh the coverage snapshot counts.
5. **Update `research/themes.md`:** add evidence bullets to the themes the source supports, update the heatmap row counts and confidence, and create a new theme (`T#`) only if two or more sources support it. Otherwise, note it as emerging.
6. **Update `research/pmf.md`** if the source moves evidence for or against a hypothesis. If the source is a company or product, add or update its row in `research/competitors.md`.
7. **Clear processed rows** from `research/inbox.md`.
8. **Commit** with a message like `research: add S007 <short title>` and push to the working branch.
9. **Report back in 3–5 lines:** what the source adds, which themes moved, any new tension or contradiction, and one suggested next read.

House style: human, consulting-grade, no jargon for its own sake. "evolv" is always lowercase.
