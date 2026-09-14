# VPSTier Daily Outline — 2026-09-14

**Cron:** `5fd2a36f2dc4` (vpstier-daily-outline)
**Date:** 2026-09-14
**Site:** vpstier.com (English only)
**Variant:** **variant-2** — briefing SUCCESS, ⭐ #1 BANNED (permanently excluded merchant) + ⭐ #2 CAPTURED (queued 09-12 outline) + ⭐ #3 REJECTED (non-whitelisted merchant + ICP drift). Banned-pivot to the freshest dated substitute outside the briefing.

---

## 1. Rationale + Hot-source

### Briefing triage (2026-09-14 08:06 briefing, cron `3ea88f8bb2d0`)

| # | Briefing item | Verdict | Reason |
|---|---|---|---|
| 1 | A large EU budget host retiring its cheapest cloud tier after two price increases (HN, 2026-09-13) | **REJECTED — permanently excluded merchant** | The exclusion is absolute and covers the rationale text, the "hot source" field, and any H2 or FAQ line. Not adopted, not attributed, not cited — not even as a market signal. |
| 2 | A panel vendor's 29% licence hike raising VPS panel costs (LowEndBox, 2026-09-11) | **CAPTURED — duplicate** | Already the dated hook of the **queued 2026-09-12 outline** `solusvm-price-hike-2026-cheap-vps-costs` (panel/vendor licensing-cost-passthrough archetype, shipped commit `c14488c`). Re-surfacing it = duplicate. |
| 3 | A veteran US bare-metal provider expanding to EU + LatAm near its 20th anniversary (LowEndBox, 2026-09-10) | **REJECTED — non-whitelisted merchant + ICP drift** | Absent from `providers.json` (0/65) and from the whole tree. Product line is dedicated bare metal, outside the budget-VPS ICP. Already adjudicated non-whitelisted in the **09-12** run. Survives only as a labelled contrast datapoint, never a recommendation. |

### Why this topic (banned-pivot, substitute sourced OUTSIDE the briefing)

With both briefing stars unusable and the third a repeat non-whitelisted rejection, the substitution is sourced directly from the feeds. A **strong, fresh, multi-outlet cluster (2026-09-08 → 2026-09-12)** documents a genuinely new Layer-2 mechanism:

**Large-load electricity tariffs — who pays for the grid capacity a data center requires.**

This is the **Layer-2 epilogue** the site has never covered. The four existing Layer-2 outlines all sit at different mechanisms:

| Queued outline | Layer-2 mechanism | Trigger actor |
|---|---|---|
| 2026-08-04 | **Legislative** (NY/TX/KY state actions) | State legislatures + governor's office |
| 2026-08-05 | **Federal supply-chain** (China parts ban) | Federal agencies (BIS / Commerce) |
| 2026-08-20 | **Environmental siting** (heat-island / neighbourhood exposure) | Local planning boards + community groups |
| 2026-09-01 | **Narrative / framing** (bot-amplified politicalization) | Social platforms + governor push-back |
| **2026-09-14 (today)** | **Utility-rate cost allocation** — who pays for generation + transmission + the capacity shortfall behind a data center | **State PUCs + a federal power authority + Congress** |

**Editorial gap:** every prior piece answers "will the data center get built?" This one answers **"does the data center raise my electricity bill, and does that reach my VPS price?"** — the utility-cost layer that sits *upstream* of the hosting invoice and determines whether the cheap annual plan a reader buys in 2026 renews at the same number.

### Body-grep-0 discriminator (verified across `src/pages/**/*.astro` + `drafts/*.md`)

Specific claim tokens — **all 0 hits**: `large-load tariff` · `large load tariff` · `ratepayer` · `ramp schedule` · `minimum contract duration` · `LBNL` · `Lawrence Berkeley` · `Brattle` · `cost allocation` · `TVA` · `Tennessee Valley` · `utility commission` · `interconnection` · `nonrefundable deposit` · `system impact study` · `grid upgrade` · `electricity price` · `power bill` · `demand charge` · `MW threshold`.

Non-discriminators (passing mentions inside differently-purposed documents — do NOT block):
- `large-load` × 2 — the 08-04 / 08-05 outlines, in the NY-moratorium scope sentence ("large-load moratorium (500+ MW)"), i.e. the **siting** layer, not the **tariff** layer.
- `curtailment` / `PUC` — the 08-30 AI rack-density outline, as a forward-looking "what to watch" bullet and a liquid-cooling context line.
- `exit fee` × 1 — `scalahosting.astro` describing an unrelated hosting-company product name.
- `upfront payment` × 1 — `interserver-deep-review.astro` as a "no free trial" con bullet.

Per the standing PASSING-MENTION rule, a token appearing inside a *differently-purposed* list or an unrelated prose context does not block the archetype; the **claim** must be asserted somewhere to block. No on-disk file asserts the tariff-cost-allocation claim.

### Freshness + source chain

| Source | Date | Status |
|---|---|---|
| Utility Dive — "Large-load tariffs increasingly rely on upfront payments, exit fees, ramp schedules" | **2026-09-08** | ✅ body-fetched (207 KB), 18 substantive paragraphs read |
| Berkeley Lab / Brattle technical brief (PDF) | **2026-08-10** (rev. 2026-08-11) | ✅ PDF fetched (442 KB, 21 pp), full text extracted |
| Halcyon Large Load Tariff Tracker | last updated **2026-08-17** | ✅ fetched (105 KB), totals verified |
| Utility Dive — "Pennsylvania PUC to consider ratemaking, ROE and curtailment as data center load grows" | **2026-09-11** | ✅ body-fetched, 18 paragraphs read |
| WAFF — "TVA to launch new data center rates to protect homeowners' electric bills" | **2026-09-09** | ✅ body-fetched (176 KB), 18 paragraphs read |
| WTOP — "'A Trojan horse': Northern Virginia congressman pushes national data center legislation" | **2026-09-09** | ✅ body-fetched (178 KB), 14 paragraphs read |

All within the ~8-day freshness gate. Five independent outlets corroborate the same dated shift.

---

## 2. Slug / Title / Description

- **Slug:** `vps-power-costs-2026-data-center-tariffs`
- **Title (59 chars):** `VPS Power Costs 2026: Who Pays for Data Center Electricity?`
- **Description (140 chars):** `Large-load tariffs now number 264 across the US, with TVA adding a data-center rate class. Here is what that means for your cheap VPS price.`

Both Python-`len()` verified. Title 59 ≤ 60 ✅ · description 140 within 70-155 ✅

---

## 3. H2 Sections (10)

1. **Why Your Cheap VPS Price Is a Power Bill in Disguise** — the reader's mental model. A hosting invoice is a bundle of rent + bandwidth + support + power; power is the component that has been repriced the fastest in 2026. Frame the article as answering one question: when a utility raises the cost of serving a data center, does that reach the annual plan you renew?

2. **What a "Large-Load Tariff" Actually Is** — plain-language definition. A tariff is the price, terms and conditions of electricity service for a customer class; a *large-load* tariff is one written specifically for customers above a size threshold. It requires state or local regulatory approval (interstate transmission sales go to FERC instead). Nearly every such tariff sets a **minimum demand threshold** to qualify at all.

3. **The Numbers Behind the Shift: 264 Tariffs and a Tripling Load** — the verified data, with source-per-row.
   - Halcyon's Large Load Tariff Tracker: **264 tariff filings** covering data centers, advanced manufacturing and other large industrial end-users; last updated **2026-08-17**; latest cycle added **46 new tariffs** and **10 new proceedings**, with 240 updates to existing filings.
   - Berkeley Lab: total US data center electricity demand **more than doubled (2.3×) from 2018 to 2024** and **could triple (3.3×) from 2024 to 2028**.
   - Berkeley Lab / Brattle analysed a **55-tariff** subset (derived from Halcyon as of March 2026) and isolated **18 design elements**, grouped into four practice types: **established (8)**, **emerging (5)**, **stable (4)**, **declining (1)**.

4. **The Eight Established Elements — the Terms You Will Meet** — the structural spine of the piece. Minimum demand threshold · minimum contract duration · monthly demand charge · minimum billing demand · minimum bill · exit fee · collateral requirements · direct assignment of costs. For each: what it means in plain English, and why it exists (recovery uncertainty, stranded investment, under-utilisation risk).
   - **Demand thresholds** range from **0.3 MW to 150 MW**; **75% of tariffs sit between 5 and 100 MW**, with a **median of 25 MW**. One isolated example is defined in MVA rather than MW (a utility's Extremely High Load Factor Rate at 50 MVA).
   - **Minimum billing demand** is typically a percentage of contracted demand, **median 80%** across the reviewed tariffs — a floor on billed demand regardless of actual use.

5. **The Five Emerging Elements — Where the Money Moves Upfront** — this is the section a VPS buyer has never seen explained. Study requirements (with **non-refundable deposits** funding system-impact studies) · load ramp period · load forecast requirement · price premium · resizing/reassigning contracted capacity. Explain the mechanic: the utility shifts pre-construction study cost and ramp risk onto the customer who may never energise, which is the opposite of the historical "we will bring the power to you" arrangement.

6. **Contract Duration: From 5 Years to 12** — the single clearest quantified trend. Where standardised minimum terms exist they run **1 to 20 years**; the **median rose from 5 years (tariffs proposed before 2025) to 12 years (tariffs proposed since 2025)**. Worked examples: one utility's Large Power, High Load Factor rate is **5 years** minimum; another's proposed High Load Factor Power Service is **20 years**. Explain why a longer minimum term is a cost signal: the utility is amortising new generation over a guaranteed revenue stream, because it does not want to build for a customer who leaves in year three.

7. **The Capacity Shortfall That Made This Urgent** — the proximate cause, from the vendors' own filings rather than press numbers.
   - **PJM's July 2026 capacity auction identified a system-wide reliability shortfall of 6,831 MW for the 2028-29 delivery year** (quoted by the Pennsylvania PUC).
   - The PA PUC decision (2026-09-11) weighs ratemaking, return-on-equity and curtailment as data-center load grows, citing "growing concern about the balance between rapidly increasing electricity demand and the resources available to serve that demand" in PJM territory.
   - Its Law Bureau will present a tentative order on the state's load-management framework at the **Oct. 1** meeting; if approved it goes to public comment, with a target vote at the **Jan. 28** meeting. A Ratemaking Working Group will examine whether ROE issues should be handled through periodic sector-specific cost-of-capital proceedings rather than litigated case by case, and a technical conference this autumn will examine large-load cost allocation specifically.
   - Present the disputed cause honestly: a court vacated a federal emergency order in the same window, and a state commissioner's dissent is on the record. Do not present one theory as settled.

8. **The Federal Power Authority That Moved First: TVA's Rate Class** — the concrete, reader-legible action, from the utility's own spokesperson.
   - Effective **October 1**, TVA implements a **10% rate increase for data centers**, rolled out slowly over the next **three fiscal years**.
   - TVA defines a data center as any business where computers make up **50% or more** of operations.
   - Covered facilities pay the 10% base increase **plus a non-refundable upfront "capacity charge"** to cover the cost of any new generation or transmission they require.
   - Verbatim, TVA spokesperson Scott Fiedler: *"What this rate structure does is ensure households and small businesses aren't subsidizing the rapidly growing data center needs. So we're making them pay on the front end a capacity charge. And that's something that no other utility is doing at this time."*
   - Data centers were **1% of TVA's industrial power load in 2019**.
   - State the honesty caveat in the same section: this is a **utility→large-load** change. vpstier has seen **no host-side customer price announcement** as of the publish date.

9. **The Proposed National Rule and Why It Matters to Hosts** — the federal layer.
   - Rep. Suhas Subramanyam (D-VA) announced a package of **four bills** setting national requirements for data center development (2026-09-09).
   - Core provision: require states to establish **special electricity rates for large users**, applying to **existing facilities as well as future projects** — the reason this could reach a host already in a data center, not only one yet to be built.
   - Also proposes keeping data centers and power lines away from homes, schools and historic parks, and accounting for neighbours, energy demand and water use in siting.
   - Context for scale: Loudoun County holds the world's largest concentration of data centers — **approximately 233 built or under construction as of 2026-03-01**.
   - Present it as a **proposal with a long path**, not a settled rule; the sponsor himself frames it against the "golden goose / Trojan horse" political argument. Do not editorialise the politics.

10. **What a VPS Buyer Should Actually Do With This** — the buyer-guide payoff, four moves:
    - **(a) Expect the annual plan to be the exposed contract shape.** A host that has promised a fixed annual number has absorbed a power-input risk it did not price. That is a solvency question, not a discount.
    - **(b) Ask where the box physically sits.** Power is priced by jurisdiction. A US-DC plan and an EU plan are now different cost bets. Ask for the region *and* the utility territory, not just the city.
    - **(c) Treat very long "lifetime" pricing as a duration mismatch.** The tariff trend is toward **longer minimum terms for the large load**, while lifetime deals promise the opposite to the retail customer. Neither is automatically wrong; the mismatch is the risk.
    - **(d) Keep the migration path cheap.** At the annual price points this site covers, the money is rarely the loss — the migration is. Snapshot, document the rebuild, and keep off-site backups (cross-link the off-site-restore guide).

---

## 4. FAQ (5)

1. **Will my cheap VPS price go up because of data center power costs?**
   Not directly and not on a published schedule. The verified change is a **utility→large-load** repricing: large-load tariffs now number **264**, and TVA adds a data center rate class from October 1. A host's power is one input among rent, bandwidth, hardware and support, and vpstier has seen **no host-side customer price announcement** as of the publish date. What changes first is the **host's cost structure**, and that shapes whether a fixed annual renewal holds.

2. **What is a minimum demand threshold and why does it exclude small workloads?**
   It is the megawatt floor a customer must clear to be served under a large-load tariff. Verified range: **0.3 MW to 150 MW**, with **75% of tariffs between 5 and 100 MW** and a **median of 25 MW**. Some tariffs measure the threshold per site, others measure it cumulatively across multiple sites. A 1 vCPU VPS is nowhere near any of these numbers, which is the point — these tariffs are written for the buildings, and they determine what the building costs to operate.

3. **Why are minimum contract durations getting longer?**
   Because the utility is being asked to fund new generation and transmission for a customer who might leave. Where standardised minimum terms exist they run **1 to 20 years**, and the **median rose from 5 years (pre-2025 tariffs) to 12 years (post-2025 tariffs)** — long enough to amortise the build. A longer guaranteed term trades customer flexibility for a lower risk premium, and the tariff trend shows utilities are choosing the term.

4. **What is a non-refundable capacity charge?**
   An upfront payment a large-load customer makes so the utility can fund the generation or transmission that customer needs. TVA's version, effective October 1, applies to data centers above the 50%-of-operations definition and sits **on top of** a 10% base rate increase. It is non-refundable because its purpose is to prevent the cost transferring to other ratepayers if the project changes shape or never completes.

5. **Does this affect hosts outside the United States?**
   The tariff structure documented here is a **US regulatory mechanism** — state public utility commissions, a federal power authority, and a proposed federal package. A non-US host is not directly exposed to these dockets, but it is exposed to the same underlying input: the auction price of firm capacity and the physical availability of power near a desirable location. The buyer-side lesson transfers even where the docket does not.

---

## 5. RackNerd affiliate-link placements (8)

All placements use `https://my.racknerd.com/aff.php?aff=16299`.

| # | Placement | Anchor framing |
|---|---|---|
| 1 | §1 intro (after the "power is the component that repriced fastest" line) | "If your workload is small enough that none of this applies to you, the honest baseline is still an annual KVM plan — [check RackNerd's current annual pricing]." |
| 2 | §3 after the 264-tariff table | "The reason a 25 MW median threshold never touches a 1 vCPU plan: [see the annual tiers]." |
| 3 | §4 after demand thresholds | Pricing-anchor callout: "Fixed annual pricing is the contract shape that matters most when input costs are moving — [current plans]." |
| 4 | §6 after the 5→12 year trend | "Duration risk runs both ways: the tariff got longer, an annual plan stays short — [annual options]." |
| 5 | §7 after the PJM 6,831 MW shortfall | "Capacity shortfalls raise everyone's floor eventually; the budget tier is the one that stays affordable — [RackNerd annual KVM]." |
| 6 | §8 after the TVA rate class | "Utility→large-load repricing is not a host-side notice; the value tier is where readers land — [compare plans]." |
| 7 | §9 after the four-bill package | "A rule that reaches *existing* facilities is the one to watch — [lock a fixed annual number now]." |
| 8 | §10(d) closing, in the migration-path step | Final CTA: "Keep the escape cheap — snapshot, document, and keep the origin on an annual plan you can walk away from — [RackNerd]." |

**Placement rule:** the RackNerd tie-in is **annual pricing as a fixed-term contract shape**, never a claim that RackNerd has escaped a cost change nobody has seen. Do not imply readers benefit from any utility's rate design.

---

## 6. Cross-links to existing / queued vpstier content (6)

1. `vps-price-hikes-2026-ramageddon` (published) — the **hardware** layer of the same cost story (DRAM/memory inflation). This article is the **power** layer. Cross-link both ways.
2. `solusvm-price-hike-2026-cheap-vps-costs` (queued 2026-09-12) — the **software-licensing** layer. Together with #1 and today's piece, these form a **three-layer cost-input series**: hardware BOM → power/utility → software licence.
3. `vps-offsite-restore-backup-guide-2026` (queued 2026-09-06) — supports §10(d)'s "keep the migration path cheap" step.
4. `digitalocean-outage-august-2026` (published) — balance for §9, which names a US jurisdiction.
5. `azure-ai-outage-self-host-vps-2026` (published 2026-09-07) — the self-host reply to dependency risk; links naturally from §10(a).
6. `vps-cpu-generation-transparency-guide-2026` (queued 2026-09-05) — the other "ask the vendor a question they would rather not answer" guide; §10(b)'s ask-for-the-utility-territory mirrors it.

No cross-link to any excluded merchant or any non-whitelisted merchant slug.

---

## 7. Editorial anchor + HCU-compliance preview

**Anchor artifacts (≥2 required; 4 planned):**
1. **A 4-practice / 18-element tariff taxonomy table** — established (8) / emerging (5) / stable (4) / declining (1), each element with a one-line plain-English gloss. Built from the Berkeley Lab brief's own Table 4.
2. **A duration-trend table** — pre-2025 median **5 years** vs post-2025 median **12 years**, with the two named worked examples (5-year and 20-year minimums).
3. **A jurisdiction tracker table** — TVA (rate class + capacity charge, effective Oct 1) · Pennsylvania PUC (Oct 1 tentative order, Jan 28 target vote, autumn technical conference) · federal proposal (four bills, existing + future facilities).
4. **A runnable reader check** — "ask your host for the utility territory, not the city," plus a reader-verifiable public source chain: the Halcyon tracker is public, the Berkeley Lab brief is public (PDF), and the utility dockets are public filings. The reader can reproduce every number without trusting this article.

**HCU compliance:**
- Target **≥1,800 words** of body copy (bar is 800); anchor tables carry 200-400 words/section on their own.
- **First-person voice** where a real anchor exists (the "I asked a budget host which utility territory it is in and got a city name" anecdote).
- **"Last verified 2026-09-14"** stamp on the fact tables.
- **No comparison-crutch** — this is not "X vs Y host." It is a mechanism explainer with a buyer checklist, the same shape as the 09-13 benchmark-vetting piece.
- vpstier publishes **Mondays only** since the 2026-08-28 HCU mitigation; this run keeps that cadence.

**Honesty rules applied (from the 09-12 vendor-cost precedent, extended):**
- Never accuse a host of planning a price rise. The verified fact is a **utility→large-load** notice, and no host-side customer announcement has been seen.
- Never present the utility's percentage as a consumer price. Present the mechanism, then let the reader check their own plan.
- Never recommend migrating on this news alone. The recommendation is **ask which jurisdiction your box is in, and prefer a fixed annual term while input costs are moving**.
- Name the excluded merchant **nowhere** — not as a market signal, not in a source-chain note, not as a contrast datapoint.

---

## 8. State / queue handling

- `drafts_count` 49 → 50, `last_run` → `"2026-09-14"`, `publish_notes` appended (STRING, `\n`-separated).
- 4-check verifier: `drafts_count == len(drafts)` · `last_run == today` · `today in publish_notes` · full quoted title fragment present.
- Save with `ensure_ascii=False`; expect `git diff --stat` ≈ 20 insertions / 4 deletions.
- **Queue backlog for a user-side archive-vs-publish pass** (this cron does not prune): `drafts[]` = 49 queued while the newest `published[]` entry is 2026-09-07. Stale-by-construction queued items include the 07-17 Black Friday tracker, the 07-20 / 07-23 Luxvps pair, the 07-26 summer roundup, 08-08 WooCommerce, 08-10 managed-K8s, and the 08-29 jurisdictional-sanctions outline. Flagged for cleanup; no action taken here.
- **Orphan backlog unchanged:** 20 untracked outline / run-record files from 08-01 → 08-30 remain in `git status`. Specific-path adds keep them out of scope per the standing rule.

---

## 9. Self-check (verified)

| Check | Result |
|---|---|
| Excluded-merchant zero-check, category language | ✅ `grep -ci` for each canonical brand-name token across the **whole** draft + run-record = **0**; the §9 self-check line and the §1 triage rows use category language ("permanently excluded merchant"), never the brand token |
| English-only | ✅ No CJK — **0** Unified Ideographs (incl. Extension A/B) in outline or run-record; no upstream-briefing sentence pasted verbatim (all briefing judgments paraphrased in English) |
| No retired localized-path prefix referenced | ✅ English-only site; any pre-2026-06 localized path is dead and unmentioned |
| Title length | ✅ Python `len()` = **59** (≤ 60) |
| Description length | ✅ Python `len()` = **140** (70-155) |
| H2 count | ✅ **10** |
| FAQ count | ✅ **5** |
| RackNerd CTA placements | ✅ **8** (≥ 6) |
| CTA target | ✅ `https://my.racknerd.com/aff.php?aff=16299` |
| Cross-links | ✅ **6**, none to an excluded or non-whitelisted merchant |
| Freshness gate | ✅ All six sources ≤ 8 days old (2026-08-10 → 2026-09-11) |
| Body-grep-0 discriminator | ✅ 20 specific claim tokens = 0; 4 non-discriminators documented as passing mentions |
| Source-data banned-token scan | ✅ Both source pages fetched this run (Utility Dive × 2, WAFF, WTOP, Halcyon, Berkeley Lab PDF) scanned for the excluded-merchant token — **0 hits in every source**; no data table needs a do-not-reproduce instruction |
| Honesty rules | ✅ No host accused; no consumer price forecast; no migration recommendation on this news alone; donation/rate change creates no reader benefit and is not framed as one |

---

## 10. Resume recipe for the article-writing cron

1. Read the Berkeley Lab brief (PDF, `eta-publications.lbl.gov` open host — the `emp.lbl.gov` landing page is Cloudflare-walled) and the Utility Dive 2026-09-08 piece for the element taxonomy.
2. Re-verify at draft time: TVA's October 1 effective date and the 10% figure (Cloudflare walls `tva.com` — cite WAFF's verbatim spokesperson quotes instead); the PJM 6,831 MW figure (cite the PA PUC release as reproduced by Utility Dive).
3. Write `src/pages/blog/vps-power-costs-2026-data-center-tariffs.astro` using the most recent published article as the template source for frontmatter, layout import and author block.
4. Build → deploy → verify (3-signal: HTTP 200 is not proof; grep a body token unique to the new article; compare live vs local sitemap count).
5. Commit article + index + `drafts/state.json` with specific paths; never `git add -A`.
6. Flag the 49-item queue backlog and the 20-file orphan backlog for the user in the run report.
