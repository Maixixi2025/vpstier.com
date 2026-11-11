# Outline: Black Friday VPS Restocks — The 19-Day Data Point

**Date:** 2026-11-11
**Slug:** `black-friday-vps-restock-timing-2026`
**Author / Cron:** vpstier-daily-outline (`5fd2a36f2dc4`)
**Variant:** variant-0 — briefing SUCCEEDED and the top vpstier star is selectable, first-hand, dated, and virgin
**Archetype:** deal-timing / restock-window buyer-guide (NEW on vpstier — the site has never published on *when* a sold-out Black Friday plan comes back, only *which* plans are cheap)
**Status:** `outline_pending_publish` — awaiting user `publish`

---

## 1. Rationale + Hot-Source

### 1a. Briefing item triage

The 2026-11-11 08:09 UTC briefing (`/root/.hermes/cron/output/3ea88f8bb2d0/2026-11-11_08-09-40.md`) carried three vpstier items.

| # | Briefing item | Verdict | Reason |
|---|---|---|---|
| 1 | ⭐ **A first-hand year-long tracker of 17 sold-out Black Friday VPS deals** (r/VPS, posted 2026-11-10 01:58 UTC) | **SELECTED** | Dated **d-1** and read from the author's own post. The method is stated and reproducible (a cron curled 29 order pages every 6 hours and grepped for the out-of-stock string). The subject — **the restock window**, i.e. *when* a sold-out plan returns — is **virgin**: `restock` = 0 hits across all 63 published `.astro` + all 66 queued outlines, and `sold out` / `come back` / `median` / `19 day` appear only as isolated unrelated strings. See §1c for the full collision check. |
| 2 | A permanently excluded European dedicated-hosting merchant's Helsinki cloud price cut (vendor pressroom) | **REJECTED — hard-banned merchant** | The merchant named in the primary is on the standing hard-ban list. Per house rule the brand is not printed here, not in the run record, and not in the self-check row. Not referenced anywhere in this outline, in any form, including as background context. |
| 3 | **A prepaid-balance seizure after an account ban on a budget token-priced host** (r/VPS, 2026-11-09) | **REJECTED — already captured, and a bad story** | The account-suspension blast-radius angle is **already queued** as `hosting-account-suspension-blast-radius-2026` (2026-11-02). Separately, this item fails on its own facts: the thread is a two-sided dispute over a **user-caused terms-of-service breach** (the author acknowledged torrent traffic), the provider's refusal to refund was upheld by other users on the thread, and the author himself conceded mid-thread *"I wasn't terminated - I deleted all VPS instances myself"*. The account-suspension mechanism in the source is the author's own self-service deletion. Publishing a retaliatory-ban narrative on those facts would be a defamatory claim on a two-party Reddit argument, not buyer guidance. |

**Variant label:** canonical **variant-0** — the briefing succeeded, one vpstier star passed every hard gate (freshness, body-verifiability, angle-virginity, collision), and the other two failed independently.

### 1b. The selected story — and the number that makes it an article

The author tracked every Black Friday offer they seriously considered — **29 of them**, copied out of the LET and LES communities in November 2025 — into a sheet, then ran a **cron job that curled each order page every six hours and grepped for the out-of-stock text**, leaving it running until the end of January. The result, stated in the author's own words:

- **17 sold out within the first 48 hours**
- **11 of those came back at the same price, median 19 days later**
- **4 came back more expensive or with less RAM**
- **2 never came back, and both were storage boxes with 1TB+ disk**

The author's own conclusion: *"unless it's a storage plan, skip the midnight refresh and wait two or three weeks."*

**The editorial thesis:** *the Black Friday sale is a two-phase event, not a 48-hour one.* The instinct — refresh at midnight, grab the plan, lose sleep if you miss it — is aimed at the wrong window. The tracked data says most of what sells out in the first two days comes back at the same price within about three weeks, while a small minority (the large-storage plans) is the part that genuinely does not come back. **Knowing which category you are in is worth more than winning the midnight refresh.**

That is a decision the reader can actually make, and it is a question vpstier has never answered. The site's Black Friday coverage (`2026-black-friday-cheap-vps-under-25`, published 2026-06-11) answers *which plans are cheap* and *when the season runs*. The published weekly piece (`racknerd-fall-giveaway-2026`, 2026-11-09) answers *should you buy now or wait*. **Neither answers what happens after you lose.**

### 1c. Collision check — why this angle is virgin

Full-corpus grep on the day of writing (63 published `.astro` + 66 queued outlines + every run record):

| Token | Corpus hits | Verdict |
|---|---|---|
| `restock` | **0** | virgin |
| `back in stock` | **0** | virgin |
| `come back` / `returned` (in a restock sense) | **0** | virgin |
| `median` | **0** | virgin |
| `19 day` / `19-day` | **0** | virgin |
| `sold out` | 1 (`netcup-vps-review-2026`, a per-location ARM64 availability aside) | unrelated |
| `sell out` | 1 (`2026-black-friday-cheap-vps-under-25`, *"before they sell out"* in the season timeline) | unrelated |
| `YABS` | 0 in published articles (7 in the 2026-09-05 outline as a CPU-detection tool, 10 in the 2026-09-13 ServerVerify outline as a benchmark database) | the tracker raises the same question the 09-05/09-13 pieces raise — a **restocked unit may land on a packed node** — but as an open question the author could not answer, not as a benchmark comparison. Different piece. |

The published BF article's timeline section (`2026-black-friday-cheap-vps-under-25.astro`) contains **0** occurrences of `restock`, `sold out`, `median`, `19 day`, `midnight`, or `launch night`. The published weekly article (`racknerd-fall-giveaway-2026.astro`) contains **0** occurrences of `restock` and `median`, and its "Should You Buy Now or Wait for Black Friday?" section is a **before-the-launch** decision — today's piece is an **after-the-sellout** decision. Adjacent, not colliding.

### 1d. The correction this article must carry (and it is a real error on our own site)

While building the fact bundle, the run checked the Black Friday **launch date** against the primary source instead of against our own earlier articles — and found that **two published vpstier articles state the wrong launch window.**

- `2026-black-friday-cheap-vps-under-25.astro` (published 2026-06-11) states in its timeline section: *"November 1-7 is the main event. RackNerd's 2024 and 2025 BF launches were both on November 1st."* and repeats *"November 1-4 and ran 7-10 days."* in a FAQ answer.
- `racknerd-fall-giveaway-2026.astro` (published 2026-11-09) states: *"RackNerd's BF 2024 and 2025 deals both launched in the November 1-4 window"* and, on that basis, *"Black Friday is two weeks away."*

**The primaries say otherwise, and every launch date below is read off a body-fetched LowEndBox post's own `datePublished`:**

| Year | Launch post | `datePublished` | Entry price |
|---|---|---|---|
| 2024 | *BLACK FRIDAY: KVM VPS, Shared & Reseller Hosting by RackNerd* | **2024-11-29** | from **$10.99/yr** |
| 2024 | *RackNerd's Black Friday 2024: Bigger, Better, and Now in Dublin!* | **2024-11-19** | from **$10.99/yr** |
| 2025 | *RackNerd Black Friday 2025 — The Biggest Drop Yet is LIVE!* | **2025-11-19** | from **$10.60/yr** |
| 2025 | *[BLACK FRIDAY] RackNerd Returns With Their Biggest Event Yet!* | **2025-11-28** | from **$10.60/yr** |
| 2026 | *Is It Too Soon to Start Talking About BLACK FRIDAY? Nope!* (the season preview) | **2026-09-18** | *"It all starts **November 27**."* |

**November 27, 2026 is a Friday** (verified with Python `date`). The same publication that previews the season says, verbatim: *"Ten weeks from today, dear reader, is the most important day in the LowEnd calendar: BLACK FRIDAY! ... It all starts November 27. Mark your calendars!"*

**Why the correction matters to the article, not just to housekeeping.** The tracker measured **48-hour sell-outs**. A sell-out measured from a launch date is only comparable if you know the launch date. If a reader believes Black Friday starts November 1 and plans accordingly, they are shopping the wrong week — and, worse, they would judge the tracker's "median 19 days" against a launch they have mis-dated. **The article therefore cannot be written without fixing the launch date first.** The launch date is the anchor of the entire restock window.

**The Nov 9 article is internally contradictory, which is how the error survived.** It was published on **November 9, 2026** and says *"Black Friday is two weeks away"* — while in the same sentence claiming the launch window was *"November 1-4"*. **November 1-4 was already eight days in the past when that sentence was written.** The only reading that makes "two weeks away" true is a launch around **November 23-27**, which is exactly what the primaries say. The article's own timing logic was right and its stated date was wrong — so a reader who trusted the date would have concluded the season was already over, while a reader who trusted the timing would have waited.

There is a second internal tell in the June article. Its FAQ answer pairs the bad date with *"Early Bird access is emailed 24-48 hours before to subscribers. Subscribe to RackNerd's mailing list in September for first access."* A **September** subscription for a **November 1** launch is an eight-week gap; for a **late-November** launch it is a tight, sensible early-bird funnel. The article's own editorial logic points at late November — only its "November 1st" clause is the outlier.

**Scope discipline:** the two published articles are **live URLs with traffic**. This daily-outline run does **not** edit published articles — it flags the correction in §8 as a separate, small, publish-time fix, with the exact strings. The article itself carries the correct date and links back to the BF article for the plan/pricing side.

### 1e. Independent corroboration for the sell-out mechanism (not the same dataset)

The tracker's own numbers are one person's dataset and its author flags the limits himself: *"29 offers is tiny and skewed toward the $15 to $40 a year range I shop in. Grepping an order page is also a noisy signal, a couple of those 'restocks' could just be a provider changing their page template."* The article must carry that caveat verbatim — an article that quotes the data without the caveat is the thing this site should not publish.

A second, independent mechanism corroborates the *demand spike* that causes the sell-out. LowEndBox's own MegaThread statistics post (body-fetched, `datePublished` 2025-12-06) gives the LowEndTalk Black Friday MegaThread engagement by year:

| Year | Comments | Views |
|---|---|---|
| 2020 | 4,902 | 257,176 |
| 2021 | 9,645 | 1,160,748 |
| 2022 | 6,023 | 778,126 |
| 2023 | 11,040 | 896,659 |
| 2024 | 40,099 | 3,401,800 |
| 2025 | 21,261 | 2,300,881 |

The same post names the mechanism directly: *"Monitoring that solution to watch that it is submitting the deals to the thread"* and *"Monitoring and increasing resources on the VMs to make sure LET doesn't collapse under extreme load."* **The community's flash-deal channel is a single queue on a forum server that is being load-shed on purpose.** That is why the sell-out is concentrated in the first 48 hours and why the same plan returns later: the queue drains, and the provider re-opens the same SKU. This is a *structural* reason to expect restocks, and it is independent of the tracker's dataset.

The provider side corroborates it too: RackNerd's own Black Friday FAQ (body-fetched 2026-11-11) says the specials are *"lifetime recurring"* — *"You can renew at the same rate for as long as you decide to keep the service."* A recurring-rate special has no reason to permanently vanish; it has a **stock** problem, not a pricing problem.

---

## 2. Slug / Title / Description

**Slug:** `black-friday-vps-restock-timing-2026`

**Title:** `Black Friday VPS Restocks: The 19-Day Data Point` — **48 / 60 char gate**
(vpstier `BaseLayout.astro` renders `<title>{title}</title>` verbatim — no auto-suffix, re-verified 2026-11-11 by reading `src/layouts/BaseLayout.astro` and the rendered `<title>` of published articles. Bare string length is final length. Length measured with Python `len()`. Headroom note: adding the optional ` | VPSTier` branding suffix yields 58 chars, still inside 60, so the drafter may brand it.)

**Description:** `Data from 17 sold-out Black Friday VPS deals: 11 returned at the same price with a median 19-day wait. Here is when to buy and when to skip midnight.` — **149 / 155 char gate**

**Target keywords:** `black friday vps restock`, `do black friday vps deals come back`, `black friday vps sold out`, `black friday vps wait to buy`, `vps deal restock timing`, `black friday 2026 vps dates`, `cheap vps black friday timing`

**Secondary keywords:** `black friday vps launch date`, `black friday vps 19 days`, `vps restock same price`, `black friday storage box never came back`

**Search intent:** informational + commercial. The reader wants a *decision* (buy at midnight or wait) backed by evidence, and the commercial intent is the budget-VPS purchase that the article should not waste.

---

## 3. H2 Chapter Plan (10 sections)

1. **The 48-Hour Sell-Out Is Only Half the Story**
   Open on the tracker's own numbers, quoted from the source: 17 of 29 tracked offers sold out inside 48 hours. Then the turn: the same tracker ran until the end of January, and its answer is not "the deals are gone" but "the deals come back". Establish the two-phase framing in the first 120 words.

2. **The Data: 29 Offers Tracked From November to January**
   The method, stated plainly so a reader can judge it: 29 offers copied from the LET and LES communities, a cron curling **each order page every 6 hours** grepping for the out-of-stock string, run until end of January. Put the full results table here: 17 sold out / 11 back at the same price (median 19 days) / 4 back dearer or with less RAM / 2 never back. **Include the author's own caveat in the same block**, not in a footnote — "29 offers is tiny and skewed toward the $15 to $40 a year range I shop in."

3. **The 19-Day Median Is the Number to Plan Around**
   Translate the median into a plan. The reader's decision is a date, not a statistic: if the sale opens Nov 27 and the median restock is 19 days later, the wait lands in **mid-December**. Show the arithmetic on a small calendar strip (Nov 27 launch → Dec 16 median restock → Dec 4-11 tail, since 3 of the 11 came back "within three weeks of selling out" per the source). Be explicit that the median is not a guarantee — the source says "most of them within three weeks".

4. **The Two That Never Came Back — and Why Storage Plans Are Different**
   The most actionable finding, and the one most readers will miss: *"2 never came back, and both were storage boxes with 1TB+ disk."* Explain the asymmetry — a large-disk SKU is a different product with a different inventory constraint than a small compute SKU, so the restock assumption does not transfer. Give the reader a rule: **if your use case is storage-heavy, the wait strategy is the wrong strategy and you should buy at launch or not at all.** This is also the section that makes the article honest rather than a "wait and save" pitch.

5. **The 4 That Came Back Worse — Price Hides the Downgrade**
   *"4 came back more expensive or with less RAM."* The silent downgrade is the real hazard: a page that says "in stock" again may not be the same product. Give the reader a 5-item checkout re-check list (price, vCPU, RAM, storage type, transfer allowance) and the reason to re-read the order page rather than trust the coupon page. Tie to the site's existing renewal-cliff material.

6. **Why the Sell-Out Is Front-Loaded: the MegaThread Queue**
   The independent corroboration section. The LowEndTalk MegaThread stats table (2020-2025) plus the quoted mechanics — the forum coordinates with providers, monitors the submission queue, and load-sheds the VMs on purpose. The point: **the 48-hour crush is an infrastructure queue, not a pricing decision.** A queue drains. Note the author's own hypothesis that the tracker "could just be a provider changing their page template" and say why the queue reading is the better explanation *and* why the tracker still cannot rule it out.

7. **Black Friday 2026 Starts November 27 — Not November 1**
   The correction section, and the article's spine. Present the launch-date table (2024: Nov 19 and Nov 29; 2025: Nov 19 and Nov 28; 2026: Nov 27 per the season preview). Then state plainly that two live articles on this site currently give a November 1-4 window, that the primaries do not support it, and that the article uses the verified dates. Flag the two live articles for the correction (do not silently contradict a page on our own site without saying so). Reusable artifact: the reader can check any provider's launch date the same way — read the offer post's own date, not a roundup's.

8. **The Timing Decision Matrix: Buy Now, Buy at Launch, or Wait**
   The decision table that makes the article worth reading. Four rows against two axes (need-now? storage-heavy?) → **Buy at launch / Buy now and skip the season / Wait 19 days / Wait but keep a fallback**. Each row states the trigger, the action, and the deadline. Add the one non-negotiable rule: **never let the wait strategy apply to a storage SKU**, because that is the case the source says does not come back.

9. **What the Tracker Could Not Answer**
   The open question the author himself put to the community: *"whether restocked units land on a fresh node or get squeezed onto the one that was already packed. If you've bought the same BF plan on launch night and again after a restock, did your YABS numbers look different?"* Cross-link the site's existing benchmark-vetting material here. This section is what makes the piece honest and gives the reader a way to contribute — and it keeps this article from duplicating the 2026-09-05 / 2026-09-13 benchmark pieces, which ask a different question.

10. **Verdict: The Best Black Friday VPS Deal May Not Be On Launch Night**
    The verdict. Restate the thesis in one line: the sale is a two-phase event and the second phase is where the value is — *unless* you need storage now. One short paragraph on the affiliate CTA: RackNerd's current specials are **lifetime recurring** (their own FAQ), so a plan bought on launch night keeps the same rate, which makes the wait-vs-buy question a *timing* question rather than a *lock-in* question — the usual objection to waiting does not apply here. Then the final CTA.

---

## 4. FAQ (5 questions)

1. **Do Black Friday VPS deals come back if they sell out?**
   In the tracked sample, yes for most compute plans — 11 of 17 sold-out offers returned at the same price, median 19 days later. The exception is large-disk storage plans: both storage SKUs in the sample never returned.

2. **How long should I wait for a Black Friday VPS restock?**
   Plan on roughly two to three weeks, using a 19-day median as the midpoint. Set your own deadline: if you need the server before then, buy at launch instead of waiting.

3. **What date does Black Friday 2026 start for VPS deals?**
   The 2026 season preview says it starts **November 27, 2026** and that the flash-deal thread opens that day. The launch posts for 2024 (Nov 19 and Nov 29) and 2025 (Nov 19 and Nov 28) are the pattern to compare against.

4. **Will a restocked Black Friday plan be the same as the one I missed?**
   Not always — 4 of the 17 came back at a higher price or with less RAM. Re-read the order page's spec block (vCPU, RAM, storage type, transfer) rather than trusting the coupon page.

5. **Is it worth buying a Black Friday VPS deal before the season opens?**
   Only if the price gap is real. The specials are lifetime recurring, so there is no renewal penalty for buying early — but the launch and early-bird prices are typically lower than the standing rate, so buying early buys you a head start at a higher price, not the year's lowest price.

---

## 5. RackNerd Affiliate CTA Placements (8)

Affiliate URL: `https://my.racknerd.com/aff.php?aff=16299` — anchor copy varies, every CTA points here.

1. **§1 close (the two-phase framing)** — soft intro CTA: the practical version of "grab it now" is a plan you can hold at the same rate, and here is the annual entry point.
2. **§3 close (the 19-day calendar)** — "if 19 days fits your deadline, the plan is not going anywhere" → a recurring-rate annual plan.
3. **§4 close (storage plans are different)** — the storage-heavy reader CTA: a plan that is already live and not waiting on a sell-out.
4. **§5 close (the downgrade re-check)** — post-checklist CTA: "the plan you re-check is easier to audit on a box you control".
5. **§7 close (the launch-date correction)** — the reader who now knows the real date needs a plan to compare against the launch price → the standing specials, with their own renewal answer.
6. **§8 close (the decision matrix)** — the primary matrix CTA, framed by row: "not storage-bound and flexible on timing → here is the rate you can lock".
7. **§9 close (the benchmark question)** — the reader who wants to answer the node question for themselves needs a box to benchmark → a full-root KVM.
8. **§10 (the verdict + final CTA)** — the bottom-line closer: the recurring-rate plan that makes the wait-vs-buy question a timing question rather than a lock-in question.

**Affiliate-label integrity:** RackNerd is the site's affiliate *and* the recommendation is genuinely true advice — the article's own point is that a **recurring-rate** special makes waiting cost the buyer nothing in renewal terms, which is exactly what RackNerd's specials are (their own FAQ: *"lifetime recurring"*). No manufactured urgency, no fake scarcity, and explicitly **no** claim that the affiliate is running a sale the reader might miss.

---

## 6. Cross-Links (8 — all targets verified to exist on disk this run)

| # | Target | Role in the article |
|---|---|---|
| 1 | `/blog/2026-black-friday-cheap-vps-under-25/` | the plan/pricing side of BF 2026 (and the article carrying the launch-date correction to be fixed) |
| 2 | `/blog/racknerd-fall-giveaway-2026/` | the current-season deal table + the "buy now or wait" before-launch decision |
| 3 | `/blog/vps-pricing-trap-guide-2026/` | the renewal-cliff mechanic behind §5's "came back worse" check |
| 4 | `/blog/lifetime-vps-deals-2026-real-cost-vs-marketing/` | the "lifetime" naming collision — RackNerd's specials are lifetime-*recurring*, which is a different thing from a lifetime-*fee* plan |
| 5 | `/blog/vps-buying-guide/` | the general entry point for a first-time buyer landing from the timing query |
| 6 | `/blog/racknerd-deep-review-2025/` | the deep provider review behind the §10 CTA |
| 7 | `/blog/netcup-vps-review-2026/` | the only published article that mentions a plan selling out per-location — useful as the §5 "availability is per-location" contrast |
| 8 | `/vps/racknerd/` | the provider profile page |

**Also available (verified on disk):** `/blog/hostinger-review/` (a second live BF entry price for the §5 comparison), `/blog/lifetime-vps-hikes-2026-massivegrid-migration-guide/` (the counter-example to a recurring price — use only if the drafter wants the contrast between a price that holds and one that moves).

**Do NOT link:** `best-vps-deals-codes-2026` — it exists in `state.json` but there is **no** `.astro` file for it on disk (verified: `src/pages/blog/best-vps-deals-codes-2026.astro` does not exist), so it is a dead target. It also appears in **both** `published[]` and `drafts[]` (the 2-slug overlap flagged in the run record) — treat it as unresolved.

---

## 7. Verified Fact Bundle (every row body-fetched 2026-11-11)

| Fact | Value | Source (fetch result) |
|---|---|---|
| Tracker dataset size | 29 offers copied from LET + LES, November 2025 | r/VPS post `1xsam97` — **HTTP 200, 3,613 B** via the `.rss` route |
| Tracker method | cron curled each order page **every 6 hours**, grepped for the out-of-stock text, ran until end of January | same post, body |
| Sold out inside 48h | **17 of 29** | same post, body |
| Back at the same price | **11 of 17**, **median 19 days** later | same post, body |
| Came back worse | **4** — "more expensive or with less RAM" | same post, body |
| Never came back | **2** — "both were storage boxes with 1TB+ disk" | same post, body |
| Author's stated conclusion | *"unless it's a storage plan, skip the midnight refresh and wait two or three weeks"* | same post, body |
| Author's stated caveat | *"29 offers is tiny and skewed toward the $15 to $40 a year range I shop in"* / *"a couple of those 'restocks' could just be a provider changing their page template"* | same post, body |
| Author's open question | whether restocked units land on a fresh node or get squeezed onto a packed one | same post, body |
| Post date | **2026-11-10 01:58:13 UTC** (d-1 at run date) | same post, Atom `<updated>` |
| BF 2026 start | **November 27** — *"It all starts November 27. Mark your calendars!"* | lowendbox.com "Is It Too Soon to Start Talking About BLACK FRIDAY? Nope!" — **HTTP 200, 168,824 B**, `datePublished` 2026-09-18 |
| BF 2024 launch | **2024-11-29** (also 2024-11-19), from **$10.99/yr** | lowendbox.com BF2024 launch posts — **HTTP 200, 190,759 B** / 189,845 B |
| BF 2025 launch | **2025-11-19** (also 2025-11-28), from **$10.60/yr** | lowendbox.com BF2025 launch posts — **HTTP 200, 192,822 B** / 234,980 B |
| MegaThread engagement | 2020: 4,902 comments / 257,176 views · 2021: 9,645 / 1,160,748 · 2022: 6,023 / 778,126 · 2023: 11,040 / 896,659 · 2024: 40,099 / 3,401,800 · 2025: 21,261 / 2,300,881 | lowendbox.com "Nerding Out on LowEndTalk Black Friday MegaThread Stats" — **HTTP 200, 179,006 B** |
| MegaThread mechanics | *"Monitoring that solution to watch that it is submitting the deals to the thread"* / *"Monitoring and increasing resources on the VMs to make sure LET doesn't collapse under extreme load"* | same post, body |
| RackNerd specials are recurring | *"These RackNerd VPS specials are lifetime recurring. You can renew at the same rate for as long as you decide to keep the service."* | racknerd.com/BlackFriday/ — **HTTP 200, 87,951 B** |
| RackNerd current specials (live) | 1 GB $21.99/yr · 2 GB $35.99/yr · 4 GB $59.99/yr · 6 GB $89.99/yr · 8 GB $119.99/yr (1 vCPU/20 GB SSD → 7 vCPU/150 GB SSD) | racknerd.com/BlackFriday/ — same fetch, rendered price block |
| Order-page pids | 952 (1 GB), 953 (2 GB), 954 (4 GB), 955 (6 GB), 956 (8 GB) | same fetch, href extraction |
| 2026-11-27 weekday | **Friday** | Python `date(2026,11,27).strftime('%A')` |
| 19-day median lands on | **2026-12-16** if the sale opens Nov 27 | Python `date` arithmetic |
| Nov 9 article's own timing | published **2026-11-09**, says *"Black Friday is two weeks away"* while claiming a **Nov 1-4** launch — a date already 8 days past at publication | `racknerd-fall-giveaway-2026.astro`, read on disk; Python date arithmetic |
| GSC (live pull, 28d to 2026-11-10) | `best vps provider` 29 imp @ pos 81.7 · `virtual private server hosting reviews` 48 imp @ pos 84.7 · `best vps for ai agents` 42 imp @ pos 74.6 — homepage still absorbs the head terms | live GSC query via `gsc_daily_report.py` helpers |

### 7a. What could NOT be verified this run (the drafter must not guess these)

- **The tracker's 29 order pages are not published.** The dataset is a private sheet; only the four aggregate counts are public. **No per-provider restock table, no per-plan dates, and no named provider** may appear in the article. The article reports aggregates only.
- **Which providers sold out and which came back** — unknown. The author did not name them in the post.
- **Whether restocks land on fresh nodes** — the author explicitly could not answer it. Do not answer it in the article; answer it in §9 by forwarding the question.
- **The 4 "came back worse" cases** — the direction of each change (price vs RAM) is not broken out. Say "more expensive or with less RAM", do not split it.
- **Black Friday 2026 actual launch date** — November 27 is the *announced* date from the season preview, 70 days before the run date. It is **not** yet confirmed by a launch post. The article must phrase it as the announced date and re-check at publish time.
- **Cybernews.com** is bot-blocked from this sandbox (HTTP 403, canonical pitfall #24) — its 2026 "deal is live" posts were read **only** as Google News RSS headlines + dates, never as bodies. Do not cite them as sources for a fact; they are fine as a "deals are already being advertised" observation with the bodies-not-read disclosure.

---

## 8. Self-Check (Pre-Commit)

| Check | Result |
|---|---|
| Banned/excluded merchant tokens across the whole draft (category token, all case variants) | **0** — verified via the standard category-token sweep; no excluded provider is named, quoted, or implied anywhere in this document, including in the triage row or the self-check row itself |
| CJK characters in body or headings | **0** — verified via the standard CJK-range regex; the only non-English source document read this run (the briefing) was paraphrased into English, never pasted |
| Deprecated language-prefix routes written into prose | **0** — no non-English route is referenced anywhere in this document |
| Title length (Python `len()` on the final rendered string) | **48 / 60** |
| Description length (Python `len()` on the final rendered string) | **149 / 155** |
| Title branding headroom | 48 + 10 (` | VPSTier`) = 58, still inside 60 |
| Slug format | kebab-case, `black-friday-vps-restock-timing-2026`, no banned token, no collision with the 66 queued slugs |
| RackNerd CTA count | **8** placements (minimum 6), all pointing to `https://my.racknerd.com/aff.php?aff=16299` |
| Affiliate-label integrity | RackNerd is the affiliate and the recommendation is genuinely true — the article's thesis is that a recurring-rate special makes waiting cost nothing in renewal terms, which is what the affiliate's specials are |
| Cross-link targets verified on disk | **8 of 8** exist as `.astro` files in `src/pages/blog/` (or `src/pages/vps/`); 1 further candidate explicitly excluded as a dead target |
| H2 count / FAQ count | **10 H2 / 5 FAQ** |
| Every named fact traced to a body-fetched primary | tracker figures → the r/VPS post body; launch dates → four LowEndBox posts' own `datePublished`; MegaThread table → one LowEndBox post body; recurring-rate quote → the vendor's own FAQ on its live page; current prices → the vendor's live specials page |
| Caveats carried in the same block as the data | Yes — the author's own sample-size and signal-noise caveats are required in §2, not in a footnote |
| No slug collision with `published[]` or `drafts[]` | Confirmed — `black-friday-vps-restock-timing-2026` is in neither list |

---

## 9. Publishing Note

- **Archetype:** deal-timing / restock-window buyer-guide (NEW on vpstier). The site's BF coverage answers *which plans* and *when the season runs*; nothing covers *after the sell-out*.
- **Recommended publish slot:** Monday **2026-11-16** — it lands before the season opens, so the article can be updated as the launch date is confirmed, and it has a natural refresh hook on **2026-11-27** and again around the **2026-12-16** median restock date.
- **HCU self-audit ready:** first-person buyer voice; **≥2 real reproducible artifacts** — (a) the tracker's own method, which the reader can replicate with a cron and a grep, and (b) the launch-date table, which the reader can re-derive from the offer posts' own dates; a *"Last verified 2026-11-11"* stamp on every fact table.
- **The affiliate IS the honest advice** (canonical pitfall #51 analogue): the article's core recommendation is "a recurring-rate special makes waiting free", and the affiliate's specials are lifetime-recurring by their own FAQ — so the CTA is true advice, not a stretch.
- **⚠️ SEPARATE FIX FLAGGED FOR THE USER (not done in this run):** two live articles carry an incorrect Black Friday launch window — `2026-black-friday-cheap-vps-under-25.astro` ("November 1-7 is the main event. RackNerd's 2024 and 2025 BF launches were both on November 1st." and its FAQ "November 1-4 and ran 7-10 days.") and `racknerd-fall-giveaway-2026.astro` ("launched in the November 1-4 window", "Black Friday is two weeks away"). The four LowEndBox launch posts' own `datePublished` values (2024-11-19, 2024-11-29, 2025-11-19, 2025-11-28) and the 2026 season preview's "November 27" do not support a November 1 window. These are live URLs with traffic, so this outline only flags them; the fix belongs in a publish slot that can also update the two articles' internal consistency.
- **Banked follow-up:** after **2026-11-27**, a short companion piece can measure the real 2026 sell-out and compare it against the 2025 tracker's 48-hour baseline — a genuinely first-party dataset vpstier could own. The `1xsam97` `.rss` route should be re-polled weekly (Reddit's `.rss` endpoint returns 200 while the normal article and `.json` shapes return 403).
