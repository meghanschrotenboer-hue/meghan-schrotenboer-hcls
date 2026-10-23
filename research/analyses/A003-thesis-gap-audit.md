# A003 · What's missing from the reference material that would strengthen the thesis?

*Gap audit, 2026-10-23. Library at 24 sources, 9 themes, 3 analyses. v1.*

## The thesis, stated plainly

> **AI in healthcare and life sciences succeeds on organizational maturity and shared meaning, not model choice. Industry bodies like Pistoia define the meaning. Snowflake is increasingly where HCLS data, and the frontier models that use it, run. evolv, a team of buyer-side HCLS operators who deliver on Snowflake, connects the two: landing industry standards in governed data products, grounding AI on them, and measuring the value.**

The thesis has eight load-bearing claims ("pillars"). The library supports some strongly and others barely at all.

## Evidence audit by pillar

| # | Pillar | Strength today | Best evidence | What's missing |
|---|---|---|---|---|
| P1 | **The problem:** maturity and meaning, not models, block AI value | 🟢 **Strong** | S011 (peer-reviewed), S018 (69% can't measure), S017, S015 | Full S011 paper; LLM-era project data; provider and payer equivalents |
| P2 | **Standards exist and buyers fund them** | 🟢 Strong (pharma) · 🔴 Absent (provider/payer) | S002, S003, S007, S015 | **Provider/payer standards:** FHIR, USCDI, OMOP, payer API mandates. S024 now adds CMS-0057-F. Also evidence of who has *adopted* PGO-T |
| P3 | **Snowflake is where HCLS data and AI converge** | 🟡 Medium, mostly vendor-sourced | S020, S021, S022, S023 | Snowflake's own HCLS strategy and industry-team priorities; HCLS customer counts; GxP and validation posture; **counter-evidence: Databricks, Palantir, Microsoft** |
| P4 | **The standards-to-platform bridge is unbuilt and valuable** | 🔴 **Weak**: argued from absence | A002, S021 (benchmark unverified) | **Buyer demand evidence**; Snowflake field confirmation; a working prototype; cost-benefit data |
| P5 | **evolv has a right to win** vs. Accenture, Cognizant, ZS | 🔴 **Weakest: no evolv evidence in the library** | Only positioning drafts in competitors.md | evolv HCLS case studies and outcomes; Snowflake partner tier and specializations; win/loss; bench depth in semantics; your Snowflake Intelligence demo engine |
| P6 | **Why now** | 🟡 Medium | EMA PMS passed (S003); Benchling DDS Oct 2026 (S020); Snowflake–Anthropic Dec 2025 (S023); CMS APIs Jan 2027 (S024) | A forward timeline: EMA PMS next phase, FDA AI guidance status, EU AI Act health obligations, CMS dates by payer type |
| P7 | **The economics work** for buyer, Snowflake, and evolv | 🔴 **Absent** | — | Deal sizes and willingness to pay; how AI workloads drive Snowflake consumption (why reps care); partner incentives; FAIR-Decide cost-benefit |
| P8 | **Frontier labs fit the picture** | 🟡 Thin (new) | S023 (Claude in Cortex, joint agent GTM) | Lab HCLS offerings and partner programs; HCLS examples of Claude or other models in Cortex |

**Pattern:** the library proves the *problem* (P1–P2) well. It's thin exactly where a GTM decision gets made: *demand for the solution* (P4), *why evolv* (P5), and *money* (P7).

## What each audience will ask that the library can't answer yet

| Audience | Their question | What's needed |
|---|---|---|
| **Snowflake HCLS industry team** | "Which of my accounts? Will it drive consumption? Why evolv over Accenture?" | An **account overlap map** (Pistoia members × Snowflake HCLS customers × Benchling/IQVIA users × evolv relationships); a consumption story; evolv references |
| **Pharma / provider / payer buyer** | "Who else has done this? What did it cost and return? Will it pass validation?" | A peer case (even a pilot); ROI framing; GxP and HIPAA posture on Snowflake |
| **evolv leadership** | "Is it big enough, can we win, what does it cost us?" | Sizing of target accounts; early pipeline signals; capability gaps (ontology skills); the investment ask (membership, prototype, poll) |

## Blind spots: counter-evidence the thesis needs to face

1. **Databricks is strong in life sciences.** ZS won Databricks' Life Sciences Partner of the Year in **2025 and 2026**. A skeptic will ask "why Snowflake?" Either show Snowflake's share in your target accounts or frame the standards layer as platform-neutral with Snowflake as your delivery strength. ([ZS 2026](https://www.zs.com/about/newsroom/zs-databricks-life-sciences-award-2026))
2. **Palantir sells "the Ontology" as its core product** (data, logic, and actions in one model), with life-sciences case studies. It's the most direct alternative to "semantics plus action on your data platform." ([Palantir 10-Q](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000041/pltr-20260630.htm))
3. **Knowledge-graph vendors** (Neo4j, Stardog, metaphacts, and others) are the traditional home for ontologies. Why put them in a data warehouse?
4. **S011's tension:** data sources didn't predict success. The thesis must lead with maturity and value, with semantics as an enabler, or the evidence turns against it.
5. **Fading urgency** after deadlines (BCBS 239's own warning, [S016](../sources/S016-bcbs-239-risk-data-aggregation.md)).

## Verification debt: firm up before using externally

| Claim | Where | Status |
|---|---|---|
| Snowflake ontology-grounded agent benchmark (50.0% → 78.2%) | S021 | Third-party report; verify on Snowflake's blog |
| Clinical poll sub-figures (42% ROI, 48% data cleaning, 22% patients) | S017 | Trade press; get poll PDF |
| Ten cases in your GPT brief | S019 | Unverified against cited sources |
| Accenture = Snowflake 2026 HCLS Services Partner of the Year | S022 | Search excerpt; confirm on Snowflake's awards page |
| IQVIA–Snowflake relationship today | S022 | Evidence is 2022–23 |
| Autonomous AI Agent persona on the official FAIR MM site | S007 | Read from source repo |
| Workbook = paper's Supplementary S2 | S011 | Inferred from file name |

## Priority list: the 10 adds that most strengthen the thesis

Ranked by impact on the weakest pillars, then by effort.

| Rank | Add | Pillar | Effort | Where it comes from |
|:-:|---|:-:|:-:|---|
| 1 | **evolv proof pack:** HCLS case studies and outcomes, Snowflake partner tier and specializations, your Snowflake Intelligence/Cortex demo engine, references | P5 | Low | Internal (you, evolv marketing, partner portal) |
| 2 | **5–8 buyer conversations** (pharma data/R&D, provider, payer) testing demand for the bridge, logged as anonymized `type: interview` | P4 | Med | Your network; existing accounts |
| 3 | **Snowflake field input:** 2–3 conversations with the HCLS industry and partner teams: their FY priorities, solution plays, target accounts, what they need from SIs | P3, P7 | Low–Med | Your Snowflake contacts |
| 4 | **Account overlap map:** Pistoia members ∩ Snowflake HCLS customers ∩ Benchling/IQVIA users ∩ evolv relationships | P3, P7 | Med | Public lists + CRM |
| 5 | **Working prototype:** PGO-T's 17 Phase 1 concepts as a Snowflake semantic view and KG tables, grounding a Cortex agent | P4, P5 | Med | Built in-house; open-licensed content |
| 6 | **Provider/payer rebalance:** CMS-0057-F detail (S024 started), FHIR/USCDI, OMOP/OHDSI, payer and provider Snowflake cases | P2, P6 | Med | CMS, ONC, OHDSI, Snowflake HCLS stories |
| 7 | **Competitive counterweights:** Databricks LS (ZS), Palantir, Microsoft Fabric in pharma; why buyers chose Snowflake | P3 | Med | Public announcements, analyst notes, buyer conversations |
| 8 | **Economics:** FAIR-Decide cost-benefit, typical deal sizes, Snowflake partner incentives, how AI workloads drive consumption | P7 | Med | Literature, Snowflake partner program, internal deal data |
| 9 | **Regulatory AI guidance:** FDA (AI in drug/biologic regulatory decisions), EMA AI reflection paper, EU AI Act health timelines | P1, P6 | Low–Med | Regulator sites |
| 10 | **Close verification debt** (table above), starting with the Snowflake benchmark and the S011 paper | All | Low | Uploads, primary pages |

**If you only do three:** #1 (proof pack), #2 (buyer conversations), and #3 (Snowflake field input). They turn the thesis from well-researched to market-validated, and none needs new web research.

## Note on balance
The library currently mirrors one buyer seat (pharma R&D and regulatory). Your right to win spans **pharma, provider, and payer**. Rebalancing (#6) doesn't just add evidence; it puts your strongest credential at the center of the story.
