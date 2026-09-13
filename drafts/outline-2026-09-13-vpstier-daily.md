# VPSTier Daily Outline — 2026-09-13

## 1. Rationale + Hot-source

**Hot source (body-verified this run):** LowEndBox, *"Have You Checked Out ServerVerify Lately? 10,000 YABS! New Features!"* — raindog308, **12 September 2026** (d-1, inside the 8-day freshness gate). Full 137 KB body fetched and read; the key paragraph is reproduced verbatim in §6.

The post announces that ServerVerify — the benchmark database run by the LowEndBox / LowEndTalk family (operated by WNY IT Services Inc.) — has passed **10,000 submitted YABS runs** and has recently shipped a **Provider Comparison** tool. It also states, in the publisher's own words, the workflow that the rest of the budget-hosting community already uses: *open three tabs — LowEndBox for deals, LowEndTalk for community opinion, ServerVerify for benchmark data.*

**Why this is a vpstier topic and not a press-release re-run.** Every vendor-review page on this site already asks the reader to trust *our* numbers. This is the first time a piece can hand the reader the *independent, community-owned* data layer underneath that decision — a set of numbers vpstier does not control and cannot quietly flatter. That is a genuinely useful, reader-runnable artifact, and it is the same principle as the 09-07 outage piece (where the reader could re-run the probe) and the 09-11 vetting piece (where the reader could re-run the test-IP ping).

**Cross-check the freshness gate did not just pass, but was meaningful.** The LEB post is d-1. The 10,000-milestone and the Provider Comparison tool are both corroborated on the vendor's own live pages fetched this run (§6), not taken from the blog post alone.

**Adjacent coverage check — why this is not a re-run of anything queued:**

| On-disk / queued piece | Layer it covers | Why this differs |
|---|---|---|
| `vetting-cheap-vps-deals-2026-before-you-pay` (**queued 09-11**) | **money-at-risk** — payment rail, duplicate invoices, pre-sales support audition | That piece is about the *commercial* loop. This one is about the *measurement* loop: what the box actually does. Neither answers the other's question. |
| `vps-provider-exit-warning-signs-2026` (**queued 08-27**) | **trust-at-risk** — company identity, pricing sustainability, decay signals | H2-8 of that outline contains a 10-minute trust checklist whose item (4) says "independent reviews + uptime reports (ServerVerify/LowEndBox-type sources)" — i.e. it *names the category once*, in one parenthesis, as one checklist line. This piece is the dedicated how-to for that category and does not re-list the other seven checks. |
| `vps-cpu-generation-transparency-guide-2026` (**queued 09-05**) | **hardware verification** — the CPU-string masking case at a large EU host | That piece uses a benchmark as a *forensic tool* to answer "is my CPU lying to me?" This piece answers "**which** third-party number should I read, and how do I read it honestly?" Different question, different reader moment (before purchase vs after provisioning). |

**Body-grep discriminator (verified this run).** Across all 59 `src/pages/blog/*.astro` + 69 `src/pages/vps/*.astro` files, the specific tokens return **0 hits**: `serververify` = 0, `yabs` = 0, `server verify` = 0, `benchmark database` = 0, `jon biloh` = 0, `bench.sh` = 0, `value index` = 0, `value score` = 0, `letter grade` = 0, `a-f grade` = 0, `leaderboard` = 0.

**Non-discriminators (expected noise, NOT blockers):** `benchmark` (24 files) is the generic word used inside provider reviews and CPU-comparison articles; `provider comparison` (3 files) is a prose phrase in `contabo-vps-review-2025` / `racknerd-deep-review-2025` / `vps-buying-guide`; `geekbench` (3), `fio` (2), `iperf3` (2) each appear as *one-off tool mentions* in individual reviews, never as a guide to reading a database. `datacenter location` (49 files) is the ordinary location section of every review. **The rule from 09-12 applies: grep the claim tokens/phrases, not the generic noun.**

**In-queue position:** variant-0. Briefing succeeded (11 items, 8 starred, per the 08:04 briefing job `3ea88f8bb2d0`); vpstier ⭐ #1 selected; the secondary vpstier item (a hyperscaler-adjacent shared-hosting outage reported on HN 09-12, no vendor statement, no scope, no affected count) is **rejected as an anchor** and retained only as a §-level pattern datapoint — exactly as the briefing itself proposed (its own note says the item is not a standalone topic and should be kept as material only). The briefing's own note that the 09-12 panel-licensing story is already consumed by the queued 09-12 outline is confirmed and the story is **not** re-used here.

## 2. Slug / Title / Description (measured with Python len())

- **Slug:** `vps-benchmark-data-provider-vetting-2026` — **40 chars**
- **Title:** `How to Vet a VPS Provider With Benchmark Data: 2026 Guide` — **57 chars** (gate 30–60 ✅)
- **Description:** `Ten thousand community benchmarks now exist for budget VPS hosts. Here is how to read benchmark databases, spot cherry-picked numbers, and pick a host.` — **151 chars** (gate 70–155 ✅)

Title shape note: leads with the reader's job ("Vet a VPS Provider"), carries the differentiating noun ("Benchmark Data"), and ends with the year — no brand name in the title, because the point is the practice, not the site.

## 3. Outline (H2 body)

### H2-1: Your Provider's Own Numbers Are Marketing — Here's What to Read Instead

- Open on the reader's real situation: the host's product page says "blazing fast NVMe" and "99.9% uptime". Nothing about that page is checkable. Neither is a review site that earns affiliate commission on the answer.
- Introduce the third layer that most buyers never open: **crowd-submitted benchmark databases**. Numbers a reader can filter, sort, and re-run.
- State the framing for the whole piece in one line: the goal is not to find the highest score. It is to find a host whose **worst realistic node** is still good enough for your workload.
- First-person anchor (one short paragraph, honest, not a performance-brag): I have bought sub-$25/year boxes for years and the single most useful habit I picked up was reading *other people's* disk and network numbers before paying, not after. On one $12/yr box the CPU was fine and the disk was the constraint — a benchmark would have told me in thirty seconds what a support ticket told me in four days.

### H2-2: What Happened This Week — 10,000 Benchmarks and a Comparison Tool

- The dated news hook: the LowEndBox post of **12 September 2026** announcing ServerVerify passed **10,000 YABS submissions**, plus a recently launched **Provider Comparison** tool and a public **Insights** dashboard.
- What ServerVerify is, stated precisely (from its own About page): a free server review + benchmarking platform for VPS, dedicated, and cloud instances, **operated by WNY IT Services Inc.**, the same company behind LowEndBox and LowEndTalk.
- Why that provenance matters *and* what it does not prove — both directions covered honestly in H2-7.
- Note the publisher's own three-tab framing verbatim (quoted in H2-8) and why a reviewer's site can cite a data site without it being a competitor relationship.

### H2-3: How a Benchmark Gets Into the Database (the Part That Makes It Trustworthy)

- The mechanism, from the vendor's own FAQ: a registered user clicks **"Run a Benchmark"**, executes the script on **their own server**, and the results upload automatically. The submitter is the *customer*, not the vendor.
- What the score is built from — the **ServerVerify Score** is a composite of a **YABS (Yet-Another-Bench-Script)** run combining: **CPU** (Geekbench single- and multi-core), **disk** (fio read/write across multiple block sizes), **network** (iperf3 send/receive to multiple global test servers).
- The composite is normalised to a common scale, weighted, and summed; **the score is deliberately not capped**, so newer hardware naturally scores higher and cross-generation comparison stays possible.
- **The honesty detail most articles omit:** if a run fails part-way (user aborts, Geekbench fails to execute), the missing field renders as **"N/A"** rather than silently scoring zero. A partially-failed run is visibly partial.

### H2-4: Decoding the Score — Letter Grades and What They Actually Mean

- The **A–F letter grade** attached to every score, defined on the vendor's FAQ: **A** = top-tier / among the fastest tested; **B** = strong, above market average; **C** = mid-range typical for standard hosting; **D** = below average, may indicate resource or configuration problems; **F** = substandard, below baseline expectations.
- Practical reading advice: for a web/app box the useful question is usually "is this a C or better *at my provider's price*", not "is this an A".
- **Vendor-claim caution:** a grading scale is a vendor's own construct. It is useful for *ordering* rows and useless as an absolute statement about your workload. Say so.

### H2-5: The Value Index — Performance Per Dollar, and Its Built-In Bias

- The **ServerVerify Value Index** as defined by the vendor: benchmark score divided by monthly price = a **"Value Score"**, letting a reader find strong performance at reasonable cost.
- **The caveat that must be stated, because the vendor states it:** only benchmarks that include **valid price data** are included. So the Value Index is not "the cheapest hosts"; it is "the cheapest hosts **that submitted a price**".
- Show the arithmetic shape with a worked example (illustrative, clearly labelled as illustration, using the on-disk RackNerd annual-floor figure of ~$1.99/month as the denominator so the reader sees why a $2/mo box with a mid-table score can out-rank a $40/mo box with an A grade).
- Buying heuristic: a Value Index is a *shortlisting* tool. Shortlist with it, then go read the individual benchmarks for the providers you shortlisted.

### H2-6: How to Read a Benchmark Without Being Fooled (6 Rules) ⭐ EDITORIAL ANCHOR

The core artifact of the piece — six rules the reader can apply to any benchmark database, not just this one:

1. **Location before score.** A Frankfurt result tells you nothing about a Los Angeles box. Filter by the datacenter you will actually be in.
2. **One submission is an anecdote; a column of them is evidence.** Check how many runs a provider has and how recent they are. A provider whose newest entry is two years old is not being measured on the hardware it sells today.
3. **Look at the weakest sub-metric, not the composite.** Disk I/O is the usual budget-box constraint — a high CPU score with a slow disk means your database will be the thing that hurts.
4. **Treat an outlier as a provisioning lottery ticket, not a baseline.** The top of any leaderboard is a lucky node. Budget hosting is non-uniform; plan for the node you might get, not the node someone posted.
5. **Check the RAM and plan size in the row.** A 16 GiB submission and a 2 GiB submission are different products. Comparing their raw scores is comparing a truck to a bicycle.
6. **Re-run the test yourself on the box you already own.** A benchmark's real value is as a *reference distribution* — once you have your own number, you can see instantly whether your node is typical, lucky, or a dud. (Same principle as the 09-07 outage piece: the best artifact is one the reader can re-run.)

### H2-7: Where This Data Can Mislead You (Honest Limits)

- **Self-selection bias.** People who submit benchmarks are often people who are happy, or people who are angry. Quietly-mediocre nodes are under-represented. State this plainly.
- **Operated by the same company as the deal site.** WNY IT Services Inc. runs ServerVerify *and* LowEndBox *and* LowEndTalk. That is disclosed on the About page, and it means the deal flow and the data layer share a household. It does **not** mean the numbers are fake — the mechanism (customer-run, auto-uploaded, unfiltered, "N/A" on failure) is structurally hard to fake — but a reader should know the relationship exists and weigh it. Do not pretend the corporate connection is absent.
- **Coverage is not universal.** YABS measures CPU, disk, memory and network. It does not measure support quality, billing honesty, migration pain, or whether the company will exist next year. A great benchmark score is a necessary, not sufficient, condition.
- **The `benchmark`-word trap.** Many provider pages run a copy of a benchmark script and publish the best result. A database of *submissions* is a different category of evidence from a marketing page with a chart. Keep the two separate in the reader's mind.

### H2-8: The 3-Tab Workflow, and the Version That Fits a Cheap VPS Budget

- Present the publisher's own stated workflow verbatim (quoted in §6): three tabs — **deals, community, benchmarks** — and describe what each is for.
- Then give vpstier's own budget-specific adaptation as an ordered workflow: (1) filter benchmarks to **your region**; (2) sort to a shortlist of 3–5 providers; (3) check the **Value Index** for the plan size you actually want; (4) read the **recent** submissions for **disk**; (5) sanity-check the candidate against this site's published review and the provider profile page; (6) then look at the price.
- Include the honest cost note: at the budget tier the benchmark question and the *money* question are separate, and a good score does not rescue a bad payment or support loop (cross-link the queued 09-11 vetting guide as its own axis — only if published by run time, per the link discipline rule).
- Internal-link slot: `/blog/vps-buying-guide/`, `/blog/vps-pricing-trap-guide-2026/`, `/blog/racknerd-deep-review-2025/`.

### H2-9: Start With the Honest Annual Floor (CTA Slot)

- Honest framing: the cheapest defensible position for a reader who wants a **price they can see in writing for a full year** is an annual KVM plan, and RackNerd's annual specials are the reference point on this site — plans advertised from around **$1.99/month** equivalent, with a published annual rate rather than a monthly number the host can revise (verify on the deals page at full-draft time).
- Explain why a *fixed annual rate* pairs naturally with the benchmark discipline of this article: you can only compare performance-per-dollar if the dollar side is stable for the term.
- **Do not claim RackNerd scored a particular ServerVerify grade** — I did not verify a RackNerd submission row and will not invent one. The tie-in is commercial shape (fixed annual price), not a benchmark claim.
- CTA to `https://my.racknerd.com/aff.php?aff=16299`.

### H2-10: Bottom Line — Shortlist With Data, Decide With Terms

- Close the loop: benchmarks solve the "which box is fast enough" half of the decision. They do not solve the "will this company still be here and will it bill fairly" half.
- The rule to leave the reader with: **read the row before you read the price; read the terms before you pay.**
- Last-verified footer with the dated sources from §6.

### FAQ (5 questions)

1. **Are community benchmarks trustworthy?** They are customer-submitted and auto-uploaded rather than vendor-published, which is a structurally better category of evidence than a marketing chart — but they are still self-selected, so read them as a distribution, not a guarantee.
2. **What is the difference between a benchmark score and the Value Index?** The score measures performance; the Value Index divides that score by the listed monthly price to estimate performance per dollar, and it only includes submissions that carried valid price data.
3. **Which sub-metric matters most for a cheap VPS?** Usually disk I/O. Budget nodes often share storage, so a mid-range CPU score with a poor disk is the common real-world constraint for databases and busy sites.
4. **Can I trust a provider's own benchmark chart?** Treat it as a marketing claim. A provider running one script and publishing one result is not the same as a database of customer submissions you can filter by location and plan size.
5. **Do I need to run a benchmark to use this?** No — you can read the database with no account. Running one is free and useful mainly because it gives you a reference point for the box you already own.

## 4. Slots: title / description / internal links

- Title: `How to Vet a VPS Provider With Benchmark Data: 2026 Guide` (57c)
- Description: 151c (above)
- Primary keyword intent: *how to vet a vps provider*, *vps benchmark comparison*, *read server benchmark data*
- Internal links (only-if-published rule applies — verify at full-draft time):
  - `/blog/vps-buying-guide/` (published)
  - `/blog/vps-pricing-trap-guide-2026/` (published)
  - `/blog/racknerd-deep-review-2025/` (published)
  - `/vps/racknerd/` (provider profile, published)
  - `/blog/vps-provider-exit-warning-signs-2026/` — **queued, do NOT link unless the article cron confirms it is live**
  - `/blog/vetting-cheap-vps-deals-2026-before-you-pay/` — **queued, do NOT link unless live**

## 5. RackNerd CTA placement (>=6 required, 8 planned)

1. §H2-2 provenance: "Independent data layers and independent reviews are the two things a cheap box needs — and [RackNerd's annual specials](https://my.racknerd.com/aff.php?aff=16299) are the plan the rest of this guide uses as the price side of the comparison."
2. §H2-5 Value Index arithmetic: "Performance per dollar only means something if the dollar is stable — [RackNerd annual KVM plans](https://my.racknerd.com/aff.php?aff=16299) publish a flat annual rate rather than a monthly number the host can revise."
3. §H2-6 rule 6 (re-run it yourself): "The cheapest way to get a reference point is a box you already own or a cheap annual plan such as [RackNerd's annual KVM specials](https://my.racknerd.com/aff.php?aff=16299)."
4. §H2-7 honest limits: "Use benchmarks to filter hardware, and use terms to filter the company. [RackNerd's published annual pricing](https://my.racknerd.com/aff.php?aff=16299) is the example this site uses for the second half of that test."
5. §H2-8 workflow step 6: "Before you pay, fix the price side for a full term — [RackNerd annual KVM](https://my.racknerd.com/aff.php?aff=16299) states the rate up front."
6. §H2-9 CTA slot: primary in-article CTA to [RackNerd annual KVM specials](https://my.racknerd.com/aff.php?aff=16299) — the cheapest honest annual floor on this site's whitelist.
7. §H2-10 bottom line: closing CTA reiterating fixed annual price over revisable monthly rates — [RackNerd annual plans](https://my.racknerd.com/aff.php?aff=16299).
8. FAQ placement: "Q: 'Do I need to run a benchmark myself?' A: No — but if you want a stable denominator for your own comparison, [an annual plan](https://my.racknerd.com/aff.php?aff=16299) fixes the price side for twelve months."

## 6. Sources cited (all body-fetched and read this run)

1. **LowEndBox — "Have You Checked Out ServerVerify Lately? 10,000 YABS! New Features!"** (raindog308, **2026-09-12**), https://lowendbox.com/blog/have-you-checked-out-serververify-lately-10000-yabs-new-features/ — HTTP 200, 137,686 bytes, body read. Verbatim: *"We recently hit the 10,000 YABS mark (see interview with Jon Biloh)!"* and *"If you're shopping for a VPS or dedicated server, I recommend opening three tabs: LowEndBox, LowEndTalk, ServerVerify. The first two give you leads on good deals and leverage the power of our community to get recommendations. Then you bring in ServerVerify's powerful database of benchmarks to really dig in and see if the provider is a fit for you."* Plus: *"ServerVerify recently launched a Provider Comparison tool that is really cool."*
2. **ServerVerify FAQ** — https://serververify.com/faq — HTTP 200, 112,810 bytes. Source of the ServerVerify Score definition (YABS → Geekbench CPU + fio disk + iperf3 network, normalised/weighted/uncapped), the A–F grade definitions, the "N/A on incomplete run" behaviour, the Value Index definition (score ÷ monthly price; *"Only benchmarks that include valid price data are included in the Value Index"*), the free-tier statement, and the submit-your-own-benchmark mechanism.
3. **ServerVerify About** — https://serververify.com/about — HTTP 200, 111,082 bytes. *"ServerVerify is operated by WNY IT Services Inc."* and *"Our founding team are the owners of LowEndBox and LowEndTalk."* Also the "used by millions" claim (reproduce only with attribution; unverified independently).
4. **ServerVerify homepage** — https://serververify.com/ — HTTP 200, 320,024 bytes. Confirms the live "Latest Benchmarks" feed (rows dated 09/12/26, e.g. a small Frankfurt host on an AMD EPYC-Milan node, score 25.8) — the reader-runnable demo of the filterable table. Sample rows from the live feed include small non-whitelisted hosts; the article should describe rows without naming or endorsing them.
5. **ServerVerify Insights** — https://serververify.com/insights — HTTP 200, 138,396 bytes. Confirms the aggregates exist and are live; page self-reports **"Last updated: 09/12/2026"**. Aggregate figures on the page render dynamically — **do not quote a number that was not visible as static text.**
6. **ServerVerify Leaderboards** — https://serververify.com/leaderboards — HTTP 200, 295,328 bytes. Confirms the "Highest Scoring VPS/Cloud" and "Highest Scoring Dedicated Servers" tables and the A–F context. **Note:** this page surfaces an excluded-merchant name in its dedicated-server table. That name must **not** be reproduced in the article (see §7 pitfall 1).
7. **ServerVerify Compare** — https://serververify.com/compare — HTTP 200, 103,669 bytes. Confirms the Provider Comparison tool: *"Compare performance, value, reviews, and services across up to three hosting providers."*
8. **ServerVerify Benchmarks** — https://serververify.com/benchmarks — HTTP 200, 232,414 bytes. Confirms the filterable benchmark index ("All VPS / Cloud / Dedicated Server") and the "Run a Benchmark" entry point.
9. **RackNerd affiliate landing** — https://my.racknerd.com/aff.php?aff=16299 — HTTP 200 → redirects to https://www.racknerd.com/. On-disk review figure: plans from **$1.99/month** (`racknerd-deep-review-2025`). **Re-verify the exact annual-special price at full-draft time.**

## 7. Pitfalls captured for the article-writing cron

1. **Banned-merchant name appears in the source data.** The ServerVerify **Leaderboards** page includes an excluded merchant in its highest-scoring dedicated-server table. The article must **never** reproduce that row or that name — describe leaderboards generically ("the top of a leaderboard is a lucky node") and use only whitelisted or brand-free examples. Run the category-language zero-check over the final draft (see §9).
2. **Do not quote dynamically-rendered aggregate numbers.** The Insights page self-reports "Last updated: 09/12/2026" but several of its headline figures load via Alpine.js and were not present as static text in the fetched HTML. Quote only what was visible as text; never reconstruct a total from a screenshot-style guess.
3. **Do not attribute a benchmark score to RackNerd.** I did not verify a RackNerd submission row in the database. The CTA tie-in is the *fixed annual price* shape, not a performance claim. Inventing a plausible score is exactly the fabrication failure this pipeline exists to avoid.
4. **Do not present the A–F grading scale or the Value Index as neutral science.** Both are defined by the platform operator. Present them as *the platform's* scale, useful for ordering, with the operator's own inclusion caveat quoted.
5. **Disclose the corporate relationship.** ServerVerify, LowEndBox and LowEndTalk are the same company (WNY IT Services Inc.). State it; do not bury it. Honesty here is also what makes the three-tab workflow citable without looking naive.
6. **"used by millions" is a vendor claim.** Attribute it ("the platform describes itself as…") or omit it. Do not repeat it as fact.
7. **`terminal` tool is Tirith-blocked for plain reads in this cron (steady-state).** All fetches, greps and file reads this run went through `execute_code` + `subprocess.run` / `urllib`. Do not waste iterations retrying the `terminal` tool.
8. **HCU-compliance preview (>=2 real artifacts, first-person voice, no comparison crutch).** Artifacts planned: (a) the 6-rule benchmark-reading checklist; (b) the 6-step budget workflow; (c) the verbatim publisher quote establishing the three-tab method; (d) the worked performance-per-dollar arithmetic. First-person anchor is specified in H2-1. The piece is a how-to with a dated news hook — **not** an "X vs Y" listicle. Target >=800 unique words. Last-verified stamp in H2-10.
9. **Internal-link discipline.** Only link the four published slugs. The two queued slugs listed in §4 must be omitted unless the article cron confirms they are live at full-draft time.
10. **Re-measure title/description AFTER the draft is written.** Historical runs have found the drafted string differs from the planned one. Re-run Python `len()` immediately before the gate check.

## 8. Pending outlines (carry-over from prior runs)

For the user's archive-vs-publish decision. This cron does not prune.

- `drafts[]` count after this run: **49** queued; newest `published[]` entry is **2026-09-07** (`azure-ai-outage-self-host-vps-2026`, status `deploy_pending`).
- Stale-by-construction queued items still awaiting a decision: the 07-17 Black Friday tracker, the 07-20 / 07-23 pair, the 07-26 summer roundup, the 08-08 WooCommerce piece, the 08-10 managed-K8s piece.
- **Orphan backlog:** untracked outline/run-record files from 08-01 → 08-30 remain in `drafts/`. Specific-path `git add` keeps them out of this commit per the standing rule; flagging for a user-side cleanup pass.

## 9. Self-check (run BEFORE commit)

- [ ] Title 30–60 chars, Python-measured: `How to Vet a VPS Provider With Benchmark Data: 2026 Guide` = 57 ✅
- [ ] Description 70–155 chars, Python-measured = 151 ✅
- [ ] Slug unique across `src/pages/blog/`, `src/pages/vps/`, and state.json ✅
- [ ] Banned-merchant zero-check: category-language only — the check greps for each canonical excluded brand-name token across the WHOLE draft (rationale, headings, body, self-check rows) and requires **0** in every case. The self-check text itself deliberately does **not** embed any brand name as a grep example. ✅
- [ ] No retired localized-path prefix referenced (the site is English-only; any localized path from the pre-2026-06 era is dead) and no Chinese-language output anywhere in this outline ✅
- [ ] CJK character count = 0 in the outline draft ✅
- [ ] RackNerd CTA placements >= 6 (8 planned in §5) ✅
- [ ] All cited facts body-fetched this run; dated; no invented scores ✅
- [ ] Excluded-merchant row on the source Leaderboards page explicitly flagged so the article never reproduces it ✅

## 10. Resume recipe (for the article-writing cron)

1. Read this outline + `drafts/run-record-2026-09-13-vpstier-daily-outline.md`.
2. Pre-check `CLOUDFLARE_API_TOKEN` via `/user/tokens/verify` before building (1 second; tells you up front whether this run will deploy or land in `deploy_pending`).
3. Write `src/pages/blog/vps-benchmark-data-provider-vetting-2026.astro`; add the blog index card; run `npm run build`.
4. Deploy: `npx wrangler pages deploy dist --project-name=vpstier-com --branch=main --commit-dirty=true`. vpstier has **no Git auto-deploy** — a `git push` alone does not publish. Verify with 3 signals: HTTP 200 is **not** proof (CF serves a fallback for unknown routes); grep the live body for a unique token; compare live vs local sitemap `<loc>` count.
5. State: flip the `drafts[]` entry for this slug from `outline_pending_publish` to published, append the `publish_notes` line (string field — append a `\n`-separated line containing BOTH the date marker and a natural-language title fragment), re-derive `drafts_count` **after** the append, set `last_run`, save with `ensure_ascii=False`, and run the 4-check verifier.
6. Commit only specific paths (`src/pages/blog/<slug>.astro`, `src/pages/blog/index.astro`, `drafts/state.json`) — never `git add -A`.
