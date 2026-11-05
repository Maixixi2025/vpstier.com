# Outline: ZAP-Hosting ZapX Pass 2026 — The Real Cost of Lifetime VPS

**Date:** 2026-11-05
**Slug:** `zap-hosting-zapx-pass-lifetime-vps-2026`
**Author / Cron:** vpstier-daily-outline (`5fd2a36f2dc4`)
**Variant:** variant-0 — briefing SUCCEEDED (2026-11-05 08:04); the first ⭐ item is whitelisted, body-verifiable, dated d-1, and passes every hard gate. Selected directly.
**Archetype:** per-account platform-fee / lifetime-promise-redefined buyer-guide (NEW on vpstier — no published article or queued outline covers a *recurring platform-access fee attached to an already-paid-for server*, the *locked-but-not-deleted* state, or *per-account vs per-server fee scoping*)
**Status:** `outline_pending_publish` — awaiting user `publish`

---

## 1. Rationale + Hot-Source

### 1a. Briefing item triage

| # | Item | Verdict | Reason |
|---|---|---|---|
| 1 | **ZAP-Hosting "lifetime" hosting now needs a monthly ZapX Pass** (LowEndBox, `lowendbox.com/blog/zap-hosting-another-lifetime-offer-that-turns-out-not-to-be-lifetime/`) | **SELECTED** | ZAP-Hosting is **whitelisted** (`providers.json` id `zap-hosting`, 1 of 65) with a live `/vps/zap-hosting/` profile and a live `/blog/zap-hosting-vps-review-2026/` review — so there is a real cross-link target and a route to send the reader. Body-fetched HTTP 200, 153,963 bytes, `datePublished` **2026-11-04T12:00:42+00:00** (d-1). The angle is **not captured** (see §1d). |
| 2 | ~~Account-suspension incident thread + a second merchant's post-payment downtime~~ | **REJECTED — permanently excluded merchant** | The headline of the primary link names a permanently excluded merchant. Excluded even as background context, per the standing hard ban. Not referenced anywhere in this outline. |
| 3 | **Black Friday trio: HostNamaste LA $17.99/yr, RackNerd $21.99/yr, EnderHost Toronto $3.84/mo** (LowEndBox) | **REJECTED — datapoint reuse + non-whitelisted** | HostNamaste's Diwali offer was already consumed as a matrix datapoint in the 2026-11-03 head-term-hub outline; EnderHost is absent from `providers.json` (0 of 65). RackNerd's $21.99/yr is the site's own affiliate promo — used here as a **price anchor only**, never as the topic. |

### 1b. Why the ZapX Pass story is worth a full article

This is not "another price hike." It is a **change in what the word "lifetime" is contractually worth**, and it is the first time a whitelisted vpstier merchant has changed the *terms* of an already-paid product rather than the price of a new one.

**The three facts, all from the vendor's own announcement (not the news summary):**

1. **The fee is per account, not per server.** ZAP-Hosting's founder wrote it plainly in the comment thread: *"It applies to your entire account, not per server."* A single Plus Pass at €4.99/30 days covers **2** Lifetime servers; Pro at €9.99 covers **8**; Max at €14.99 covers **unlimited**. The effective per-server cost therefore falls with scale: **€2.50/server at Plus-2, €1.25/server at Pro-8**.
2. **"Locked" is not "deleted" — and this changed during the announcement.** A customer asked directly: *"I previously understood that if you no longer have the ZapX Pass, the server would be locked and deleted after 30 days. Now I read here in the blog post that the server simply remains locked."* The vendor's reply is the sentence that should anchor the article: *"We have decided that lifetime servers will only be locked without a pass. Your data remains stored and the server remains yours."* The only casualty is the **IP address or port**, which may change on reactivation.
3. **The legacy panel is the actual cliff — and it is not in the Pass.** The vendor states plainly: *"The old Customer Panel has reached the end of its life cycle. We're no longer developing it."* One customer put the sharpest version of it: *"if the old panel is eventually left behind, then 'you don't have to migrate' doesn't really feel like a choice. It just feels like a delayed subscription."* The vendor's answer is honest but narrow: *"it is not being developed any further… What it does still get are security updates and bug fixes. So it stays safe and usable."* **That is a maintenance-only promise, not a feature promise — and it is the real deadline.**

### 1c. The vendor's own cost comparison, checked against the vendor's own price list

ZAP-Hosting's announcement includes a "renting vs Lifetime with a Pass" table. Every figure in it reconciles against the vendor's live shop, which is what makes it usable rather than marketing:

| Vendor's own claim | Our independent recomputation | Verdict |
|---|---|---|
| 16 GB VPS rents at "around €216" per year | €17.99 × 12 = **€215.88** | ✅ matches |
| "Lifetime and the Plus Pass, you pay just under €60" per year | €4.99 × 12 = **€59.88** | ✅ matches |
| Plus Pass (1 server) = €4.99 / 30 days | €4.99 ÷ 30 × 365 = **€60.66** | ✅ ~consistent |
| Plus Pass (2 servers) = €2.50 / server | €4.99 ÷ 2 = **€2.495** | ✅ matches |
| Pro Pass (8 servers) = €1.25 / server | €9.99 ÷ 8 = **€1.249** | ✅ matches |

**The honest conclusion:** Lifetime + Plus Pass is **€156.00/year cheaper** than renting the comparable 16 GB VPS — the vendor is right about the arithmetic, and that is a genuinely good deal. The article's job is **not** to call this a scam; it is to tell the buyer **which** lifetime promise they are actually holding and **when** it converts into a subscription.

### 1d. Capture-check (body-grep-0 across 293 source files + 74 queued outlines)

| Token | Files |
|---|---|
| `ZapX` / `Zap-X` | **0** |
| `activity check` (the legacy-panel inactivity rule) | **0** |
| `locked, not deleted` / `reactivat*` | **0** |
| `platform fee` / `platform subscription` | **0** |
| `per 30 days` | **0** |
| `ZAP Coins` | **0** |
| `AI Assistant` | **0** in published articles |
| `Dedicated Lifetime slot` | **0** |
| `9.90` (the Dedicated slot price) | **0** |
| `4.99` (the Plus Pass price) | 33 files — all unrelated provider prices; the **phrase** `ZapX Pass Plus` = **0** |

**Published-angle collision gate — checked against the three closest live neighbours** (`lifetime-vps-deals-2026-real-cost-vs-marketing`, `lifetime-vps-hikes-2026-massivegrid-migration-guide`, `vps-pricing-trap-guide-2026`, `vps-price-hikes-2026-ramageddon`). All four score **0** on every distinguishing token (`platform fee`, `per account`, `activity check`, `reactivat*`, `per 30 days`, `ZapX`, `AI Assistant`, `Dedicated Lifetime slot`, `ZAP Coins`, `IP address may change`).

The distinction, stated precisely:
- `lifetime-vps-deals-2026` (Aug 31) = **which pricing model to pick** (lifetime / annual / monthly / hourly).
- `lifetime-vps-hikes-2026-massivegrid` (Nov 2) = **a provider cancelling a lifetime guarantee** → forced migration → 3× price. The server is **retired and replaced**; the buyer **loses the product** and must migrate.
- **This article** = the product **survives and is still paid for**, but a **recurring access fee** is attached to it, the access fee is **scoped per account**, and the failure mode is **silent suspension (locked) plus a one-way migration into a platform that stops being developed**.

Related-article ≠ block. The three are three different answers to three different questions.

**Adjacent queued outline** `hosting-account-suspension-blast-radius-2026` (2026-11-02) covers **provider-initiated legal suspension**. This article covers **voluntary, priced, self-service suspension**. Different trigger, different remedy, different actor. Not a collision.

### 1e. Why this is a buyer's guide and not a hit piece

The vendor's position is defensible and the article must say so:
- The server **is not deleted**. The vendor committed in public to locked-not-deleted and corrected a customer who had been told otherwise.
- The Pass is **account-wide**, so the per-server cost genuinely drops with scale.
- Lifetime + Pass is **3.6× cheaper than renting** the same spec — the vendor's own table says so and the arithmetic holds.
- The old panel still gets **security updates and bug fixes**.

The buyer's problem is not that the vendor did something wrong. It is that **"pay once" quietly became "pay once, plus a platform subscription, and the old panel you were relying on stops receiving features."** That is a purchase-decision problem, which is exactly what vpstier exists to answer.

---

## 2. Slug / Title / Description

| Field | Value | Length |
|---|---|---|
| **Slug** | `zap-hosting-zapx-pass-lifetime-vps-2026` | 39 chars |
| **Title** | ZAP-Hosting ZapX Pass 2026: The Real Cost of Lifetime VPS | **57/60 chars** |
| **Description** | The ZapX Pass puts a recurring per-account fee on ZAP-Hosting Lifetime servers. Real numbers, the locked-not-deleted rule, and when a flat VPS costs less. | **154/155 chars** |

**Length gate computed with Python `len()` on the exact strings above — no estimation.** Title is rendered verbatim (vpstier's `BaseLayout.astro` has **no** brand-suffix logic — verified this run), so 57 chars is the final `<title>` length.

**Title alternatives considered:** `ZAP-Hosting ZapX Pass: What Lifetime VPS Costs Now` (50), `ZAP-Hosting Lifetime VPS Now Has a Monthly Platform Fee` (55). The selected title leads with the brand + product name for brand-query capture and keeps "Lifetime VPS" as the head term.

---

## 3. H2 Chapter Plan (10 sections)

1. **What Actually Changed on 4 November 2026** — the timeline, sourced to the vendor's own announcement (published 2026-10-21) and the news coverage (2026-11-04). Three beats: (a) ZapX was announced in June 2026 as a new control platform with an AI assistant; (b) on 2026-10-21 the founder published *"Lifetime Behind a Paywall? Our Honest Answer"* explaining the Pass; (c) the migration is **voluntary and staged** — customers are invited one by one by email and panel banner, and **early movers get the Pass free for a limited time**. State the vendor's own framing of why: *"the old Customer Panel is no longer being developed… Everything new is built in ZapX only."*

2. **The Fee Structure, Exactly as Published** — reproduce the vendor's own three-tier table (Plus €4.99 / Pro €9.99 / Max €14.99 per 30 days; 2 / 8 / unlimited Lifetime servers; 1 / 3 / 5 backup slots per service; automatic backups and Discord control from Pro; direct team chat on Max), plus the **Dedicated Server exception**: Lifetime Dedicated Servers are in **no** tier and need a separate **Dedicated Lifetime slot at €9.90 per 30 days** on top of the Pass — because a dedicated machine burns power 24/7. Add the AI Assistant, Claude/ChatGPT via MCP, the mobile app, 300+ one-click apps, snapshots, automatic restarts, health checks and team sharing as what the Pass actually buys.

3. **The Per-Account Math: Why Your Fee Depends on How Many Servers You Own** — the analytical centrepiece, and the fact most readers will have missed. Because the Pass covers the **whole account**, the per-server price is **€4.99** (Plus, 1 server) → **€2.50** (Plus, 2 servers) → **€1.25** (Pro, 8 servers). Reproduce the vendor's own rent-vs-Pass table (8 GB / 16 GB / 32 GB) and extend it with the numbers the vendor does not show: a customer with **18 Lifetime servers** (a real case in the comment thread) sits on **Max at €14.99** = €179.88/yr ≈ **$202.67** for all 18 = **$11.26/server/yr**. A customer with **1 server** on Plus pays **€59.88/yr ≈ $67.47** for it = **$67.47/server/yr** — **6× more per server than the 18-server customer**. Include the FX note: ECB reference rate 1 EUR = **1.1267 USD** (2026-11-04, `api.frankfurter.app`), so EUR prices are converted once, at source, and marked as such.

4. **Locked, Not Deleted — and the 30-Day Myth That Was Corrected Publicly** — quote the customer question verbatim (*"I previously understood that if you no longer have the ZapX Pass, the server would be locked and deleted after 30 days. Now I read here in the blog post that the server simply remains locked"*) and the vendor's answer verbatim (*"We have decided that lifetime servers will only be locked without a pass. Your data remains stored and the server remains yours… The only limitation is that the IP address or port may change in the meantime."*). Then the **operational consequence that the announcement does not spell out**: a locked server is **stopped** — a live service is down — and the IP/port change breaks **DNS records, backup jobs, tunnels and any allow-list that pins the IP** (a named customer raised exactly this: *"several of my services (backup jobs, DNS, tunnels) depend on a fixed IP"*). Reactivation is free and immediate *once a Pass with a free slot exists*; the cost of the gap is **your downtime plus your re-pointing work**.

5. **The Legacy Panel Is the Real Deadline** — the part the Pass cannot buy. The vendor's own words: *"it is not being developed any further. No new features, no new tools, no AI"* but *"it does still get security updates and bug fixes."* Put the two statements side by side and let the reader draw the conclusion: **security maintenance ≠ feature development ≠ platform currency**, and the panel that still runs your server is the one that will not gain the AI assistant, the mobile app, the Discord bot, snapshots, automatic restarts or health checks. Note the migration is **one-way** (*"Can I go back to the old panel? No, the move is final."*) and that the vendor's own support team flags the trap for SSH-only users: *"in the legacy panel, Lifetime servers still have the activity check… SSH activity doesn't count for that. So open your server's page in the Customer Panel every now and then. You'll get a warning email before anything happens."* That is a **panel-login requirement to keep a paid-for server alive** — a concrete, checkable, and largely unknown burden.

6. **What It Actually Costs You in Year One** — the honest total-cost table, built from the vendor's own numbers, with the reader's own lifetime server in it:

   | You have | One-time price already paid | Pass tier you need | Pass/yr | Per server/yr | vs. renting same spec |
   |---|---|---|---|---|---|
   | 1 Lifetime VPS (8 GB) | $97.44 | Plus | €59.88 ≈ **$67.47** | **$67.47** | 8 GB rents €9.99/30d ≈ $135/yr → Pass is **~50% cheaper** |
   | 1 Lifetime VPS (16 GB) | $183.68 | Plus | €59.88 ≈ **$67.47** | **$67.47** | 16 GB rents €17.99/30d ≈ $243/yr → Pass is **~72% cheaper** |
   | 2 Lifetime VPS (16 GB each) | $367.36 | Plus (2 slots) | €59.88 ≈ **$67.47** | **$33.73** | — |
   | 8 Lifetime VPS | $734.72 | Pro | €119.88 ≈ **$135.07** | **$16.88** | — |
   | 18 Lifetime VPS | ~$3,300 | Max | €179.88 ≈ **$202.67** | **$11.26** | — |
   | 1 Lifetime Dedicated | $964.21 | Plus **+ Dedicated slot** | (4.99 + 9.90) × 12 ≈ **$201.32** | **$201.32** | — |

   Lifetime one-time prices are the vendor's live shop figures (`/en/shop/product/lifetime-vps/`): 4 GB $71.68, 8 GB $97.44, 16 GB $183.68, 32 GB $267.68, 48 GB $368.48, 64 GB $446.88, 96 GB $614.88, 128 GB $704.48 — **one-time**, and "Lifetime servers cannot be paid for with ZAP Coins." **The conclusion, stated plainly: on pure arithmetic the Pass is still a good deal. The risk is not price — it is the two non-price terms (the one-way migration and the un-maintained legacy panel).**

7. **When a Flat Annual VPS Is Simply the Better Buy** ⭐ PRIMARY AFFILIATE — the honest crossover section, and the commercial spine of the piece. RackNerd's **live** Fall 2026 specials (racknerd.com/BlackFriday, verified this run): 1 GB $21.99/yr, 2 GB $35.99/yr, 4 GB $59.99/yr, 6 GB $89.99/yr, 8 GB $119.99/yr — 20 datacenter locations, full root SSH, 1 Gbps port, 1 IPv4, KVM/ctrl panel, 3–5 TB monthly transfer. Cross the RackNerd ladder against the Pass:
   - **1 RackNerd 1 GB ($21.99/yr) beats a single-server Plus Pass ($67.47/yr)** — by $45.48/yr.
   - **2 RackNerd 1 GB ($43.98/yr) beats Plus-with-2-servers ($67.47/yr)** — by $23.49/yr.
   - **1 RackNerd 4 GB ($59.99/yr) beats Plus ($67.47/yr)** — by $7.48/yr.
   - **1 RackNerd 8 GB ($119.99/yr) is dearer than Plus ($67.47/yr)** — here the lifetime asset wins.
   - **4 RackNerd 1 GB ($87.96/yr) is dearer than Plus ($67.47/yr)** but cheaper than Max ($202.67/yr).
   The teaching point: **the Pass's per-account scaling only pays if you actually own multiple lifetime servers.** One server → the flat annual plan wins outright. Two servers → still wins. Four or more, or a 16 GB+ spec → the lifetime asset plus a Pass is the cheaper path. **Affiliate CTA #1, #2, #3.**

8. **The 5 Checks to Run on Your Own Lifetime Server This Week** — the practical core, and the reason the article exists. (1) **Count your servers and your tier** — the Pass is per account, so a single server on Plus is the expensive case; check whether you even need a Pass (the legacy panel still works). (2) **Log into the Customer Panel now** — the activity check locks a legacy-panel Lifetime server after **3 months** of panel inactivity and deletes it **4 weeks later**, and *"SSH activity doesn't count"*; the vendor sends a warning email first, so this is preventable. (3) **Write down what depends on your IP** — DNS records, backup jobs, tunnels, IP allow-lists — because the IP or port may change on reactivation. (4) **Decide whether you are migrating, and accept it is one-way** — there is no path back to the legacy panel; and note the **early-mover bonus** (free Pass for a limited time) that makes *testing* ZapX cheap if you have already been invited. (5) **Check your ZAP Coins and Premium Storage** — ZAP Coins stay in the legacy panel, Premium Storage keeps running there unchanged, and ZapX has no Premium Storage (the Pass's backup slots cover backups instead). Also note the vendor committed to a **yearly Pass option**: a customer asked for it, and ZAP-Hosting replied *"we're going to add this. You'll soon be able to pay the ZapX Pass for up to 12 months in advance."* **Affiliate CTA #4.**

9. **The Verdict, and Who Should Do What** — three clean recommendations. **Keep the legacy panel** if you are SSH-only, run Coolify or similar, and never want a monthly line item — the server keeps running with no Pass, no monthly fee, and security fixes; just open the panel every few months to satisfy the activity check. **Migrate to ZapX** if you want the AI assistant, snapshots, automatic backups, 300+ one-click apps, health checks and a supported platform, and can absorb a per-account fee. **Don't buy a Lifetime server today** until you know the Pass rules apply to it — the vendor confirmed in the thread that new Lifetime servers **will** be sold in ZapX *"paid once as usual, along with the pass"*, so a new lifetime purchase now carries the fee from day one. **Affiliate CTA #5** (RackNerd as the flat-annual alternative for a first-time buyer).

10. **Frequently Asked Questions** — see §4 below. Final CTA. **Affiliate CTA #6.**

---

## 4. FAQ (5 questions)

**Q1: Does ZAP-Hosting delete my Lifetime server if I cancel the Pass?**
No. The vendor's own answer in the announcement's comment thread: *"We have decided that lifetime servers will only be locked without a pass. Your data remains stored and the server remains yours. If you later get a pass with a free lifetime slot, you can simply activate it again."* A server without a Pass is **stopped (locked)**, not deleted. The one thing that may change on reactivation is your **IP address or port**.

**Q2: Is the ZapX Pass per server or per account?**
Per account. The vendor states it directly: *"It applies to your entire account, not per server."* One Plus Pass at €4.99 per 30 days covers **2** Lifetime servers; Pro at €9.99 covers **8**; Max at €14.99 covers **unlimited**. That is why a single-server customer pays €59.88/year while an 8-server customer on Pro pays €119.88/year — roughly **6× less per server**.

**Q3: What happens if I do nothing and keep using the old panel?**
Your Lifetime server keeps running in the legacy panel, with no Pass and no monthly fee — the vendor confirms this in the announcement's FAQ ("No. But we explicitly recommend it, because the old panel is no longer being developed"). What you lose is development: *"it is not being developed any further. No new features, no new tools, no AI."* You keep receiving **security updates and bug fixes**. You also keep the **activity check**, which locks a Lifetime server after **3 months** without a panel login and deletes it **4 weeks later** — and SSH use does not satisfy it.

**Q4: Is Lifetime-plus-Pass still cheaper than just renting a VPS?**
On the vendor's own published figures, yes — comfortably. A 16 GB VPS rents at €17.99 per 30 days ≈ **€216/year**, while Lifetime (paid once, €183.68 for 16 GB) plus a Plus Pass costs **€59.88/year**. That is a saving of about **€156/year**. The reason to hesitate is not the price; it is that the **migration to ZapX is final**, and the legacy panel receives only security and bug fixes from here on.

**Q5: How much does the ZapX Pass cost per year in dollars?**
Using the ECB reference rate of 1 EUR = **1.1267 USD** (2026-11-04): Plus **€59.88/yr ≈ $67.47**, Pro **€119.88/yr ≈ $135.07**, Max **€179.88/yr ≈ $202.67**. A Lifetime **Dedicated** Server needs an extra Dedicated Lifetime slot at **€9.90 per 30 days ≈ $133.85/yr** on top of any tier. For comparison, RackNerd's live 1 GB KVM special is **$21.99/yr** and 4 GB is **$59.99/yr** — both below a single-server Plus Pass.

---

## 5. RackNerd Affiliate CTA Placements (8 — minimum 6 required)

| # | Location | Anchor Text |
|---|---|---|
| 1 | §7 — crossover section, after the RackNerd ladder | "See RackNerd's $21.99/yr 1 GB KVM →" |
| 2 | §7 — after the 1 GB vs Plus comparison | "Compare RackNerd's full annual plan ladder →" |
| 3 | §7 — after the 4 GB crossover point | "RackNerd 4 GB KVM from $59.99/yr →" |
| 4 | §8 — check #1, "when a flat plan wins" | "Flat annual VPS instead →" |
| 5 | §9 — Verdict, first-time-buyer path | "Start on RackNerd from $2.24/mo →" |
| 6 | §9 — Verdict, multi-server path | "RackNerd annual specials →" |
| 7 | FAQ Q5 — dollar comparison | "RackNerd from $21.99/yr →" |
| 8 | §10 — closing CTA | "Compare budget VPS on RackNerd →" |

**Affiliate URL:** `https://my.racknerd.com/aff.php?aff=16299` — all 8 placements, each with `rel="sponsored nofollow"` and `target="_blank"`.

**Affiliate-label integrity (critical on this topic):** ZAP-Hosting is the merchant **under review**, and it is **not** the affiliate. Every RackNerd CTA in this article must be framed as **the flat-annual alternative** for a reader deciding *not* to buy a lifetime server — never as a sign-up link for ZAP-Hosting, and never adjacent to ZAP-Hosting's own pricing in a way that implies the two are the same product. RackNerd is a **different company with a different pricing model**; the article's whole point is that these two pricing models are not interchangeable.

---

## 6. Cross-Links (10 targets, all verified on disk)

| Target | Status | Rationale |
|---|---|---|
| `/vps/zap-hosting/` | ✅ Live (14,498 B, HTTP 200) | The provider profile the reader lands on — the review's own home base |
| `/blog/zap-hosting-vps-review-2026/` | ✅ Live (25,759 B, HTTP 200) | **Parent article.** Its own pricing table shows the *old* Cloud Server line — the reader needs this to see what "Lifetime VPS" and the Cloud line actually are. Note: it contains **zero** mentions of lifetime, ZapX or a Pass, so the two pieces are complementary, not overlapping |
| `/blog/lifetime-vps-deals-2026-real-cost-vs-marketing/` | ✅ Live | The 4-pricing-model guide — the natural "choose your pricing model" parent |
| `/blog/lifetime-vps-hikes-2026-massivegrid-migration-guide/` | ✅ Live | The contrast case: a lifetime guarantee **cancelled** and the product retired — versus today's product **surviving** with a fee attached |
| `/blog/vps-pricing-trap-guide-2026/` | ✅ Live | Renewal-cliff mechanics, 12-month true-cost method |
| `/blog/vps-price-hikes-2026-ramageddon/` | ✅ Live | The 2026 cost-inflation backdrop the vendor itself cites |
| `/blog/2026-black-friday-cheap-vps-under-25/` | ✅ Live | The flat-annual comparison set |
| `/blog/2026-shutdown-cloud-services-vps-migration/` | ✅ Live | Off-site backup discipline — the counterweight to a locked server |
| `/vps/racknerd/` | ✅ Live | Affiliate target profile |
| `/vps/vultr/` | ✅ Live | Hourly alternative for burst workloads mentioned in the Verdict |

**Not linked (queued, not live):** `hosting-account-suspension-blast-radius-2026`, `best-vps-providers-2026`, `best-vps-for-hermes-agent-2026`, `cheap-vps-merchant-red-flags-2026`. These are drafts; linking to them would create 404s.

---

## 7. Self-Check (Pre-Commit)

| Check | Result |
|---|---|
| Permanently excluded merchant token count in outline body | **0** (case-insensitive count over the whole draft; the triage table in §1a describes the rejected item in category language without naming it) |
| CJK characters in outline prose | **0** (standard Unified Ideographs range check; the check is written in category language with no regex literal, per the standing self-referential-literal pitfall) |
| Deprecated language-prefix path in prose | **0** (no non-English route paths; vpstier is English-only since 2026-06-11) |
| Title length (Python `len()`) | **57 chars** (gate 30–60: PASS) |
| Description length (Python `len()`) | **154 chars** (gate 70–155: PASS) |
| Title rendered verbatim, no auto-suffix | **VERIFIED** — `src/layouts/BaseLayout.astro` contains no brand-suffix logic this run |
| Slug uniqueness vs state.json | **PASS** (not in `drafts[]` (60) or `published[]` (84); no file with this slug) |
| Idempotency | **PASS** — `drafts/outline-2026-11-05-vpstier-daily.md` did not exist before this run |
| Whitelisting | **PASS** — `zap-hosting` is entry 34 of 65 in `providers.json`; live `/vps/zap-hosting/` page exists |
| Price anchors verified this run | **PASS** — Pass tiers from the vendor's own two tables (raw-HTML `<table>` extraction, 4-row and 7-row); Lifetime one-time tiers from the live shop dropdown; RackNerd from racknerd.com + /BlackFriday/; FX from `api.frankfurter.app` (ECB, 2026-11-04) |
| Vendor arithmetic independently recomputed | **PASS** — vendor's "around €216" → our €215.88; vendor's "just under €60" → our €59.88; per-server €2.50 → €4.99 ÷ 2; €1.25 → €9.99 ÷ 8 |
| RackNerd affiliate CTA count | **8** (minimum 6 required) |
| Cross-link targets exist on disk | **PASS** — 10/10 verified via `os.path.exists()`; 4 queued-but-unpublished targets deliberately excluded |
| Published-angle collision gate | **PASS** — 4 closest live articles score 0 on all 10 distinguishing tokens |
| Content gap | **PASS** — `ZapX` / `activity check` / `per 30 days` / `ZAP Coins` / `reactivat*` = **0 files** across 293 source files + 74 queued outlines |
| Primary-source strength | **PASS** — the article is built on the vendor's **own** announcement (2026-10-21, 805,417 B) and the vendor's **own** 265-comment thread, not on the news summary alone. The LowEndBox piece (2026-11-04, 153,963 B) is the dated news corroboration |
| First-person voice / HCU preview | **PASS** — recomputed vendor arithmetic, an 18-server case from the comment thread, the IP-change consequence, the panel-login requirement, and a crossover table the reader can run on their own server count |

---

## 8. Source Log (all body-fetched this run)

| Source | HTTP | Bytes | Used for |
|---|---|---|---|
| `legacy.zap-hosting.com/en/blog/2026/10/lifetime-behind-a-paywall/` (vendor, 2026-10-21, founder Marvin Kluck) | 200 | 805,417 | Pass rationale, the two vendor tables, per-account scoping, locked-not-deleted, activity-check removal, early-mover bonus, migration-is-final, FAQ |
| Same page, 265-comment thread | 200 | (same) | The corrected locked-vs-deleted answer, the 18-server case, the IP-pinning concern, the SSH-does-not-count warning, the yearly-Pass commitment, the one-sentence security/legal objection and the vendor's reply |
| `lowendbox.com/blog/zap-hosting-another-lifetime-offer-that-turns-out-not-to-be-lifetime/` | 200 | 153,963 | Dated news corroboration (2026-11-04T12:00:42+00:00), the editorial framing of the "paywall" question |
| `zap-hosting.com/en/shop/product/lifetime-vps/` | 200 | 759,895 | Lifetime one-time tiers 4 GB $71.68 → 128 GB $704.48; "Lifetime servers cannot be paid for with ZAP Coins" |
| `zap-hosting.com/en/shop/product/vps/` | 200 | 790,351 | Rental VPS tiers (RAM $6.61/8.85/16.69/25.65/… per 30 days) for the rent-vs-Pass cross-check |
| `zap-hosting.com/en/` | 200 | 428,165 | "Lifetime VPS from $71.68", "Lifetime Dedicated Server from $964.21", current product ladder |
| `zap-hosting.com/en/zapx/` (vendor, 2026-06-17) | 200 | 336,457 | ZapX origin, founder letter, AI-assistant feature list |
| `zap-hosting.com/impressum/` | 200 | 339,379 | Legal entity: ZAP-Hosting GmbH, Hafenweg 8, 48155 Münster, HRB 15672, VAT DE 320366231 |
| `www.racknerd.com/` | 200 | 34,042 | "VPS from $2.24/mo", 20 datacenter locations, 24/7 support |
| `www.racknerd.com/BlackFriday/` | 200 | 87,950 | Annual ladder: 1 GB $21.99, 2 GB $35.99, 4 GB $59.99, 6 GB $89.99, 8 GB $119.99 + specs (vCPU, SSD, transfer, IPv4, 1 Gbps) |
| `api.frankfurter.app/latest?from=EUR&to=USD` | 200 | 70 | ECB reference rate 1.1267 (2026-11-04) for the single EUR→USD conversion |
| GSC API (direct, token verified) | 200 | — | 90d query + page dimensions for vpstier (head terms at pos 74–96 on the homepage; no lifetime/deal query demand — this is an editorial-demand piece, not a query-demand piece) |
| `vpstier.com/sitemap-0.xml` + live probes | 200 | 9,277 | Confirmed the two Zap URLs are live and the slug is new |

**Walled / unavailable this run (declared, not guessed):** Reddit (403, steady-state); LowEndTalk search (403 Cloudflare interstitial); `lowendtalk.com` article bodies; `zap-hosting.com/en/shop/product/zapx-pass/` (the Pass is not sold as a standalone shop product — it appears only inside the account panel, so the vendor's announcement is the authoritative price source); `api.exchangerate.host` (401, no key — `frankfurter.app` used instead).

**Two factual drifts found in our own live data** (flagged for a separate cleanup, **not** fixed in this outline run):
1. `providers.json` and the published review both state ZAP-Hosting was **"founded in 1998 in Saarbrücken"** and *"25+ years"*. The vendor's own site says otherwise: the founder writes *"I started ZAP-Hosting back in 2010"* (2026-06-17), the footer reads *"Copyright 2010 - 2026"*, the imprint shows **Münster** (HRB 15672), and the domain was registered **2008-12-25** (RDAP). The defensible claim is **founded 2010 in Münster**; "25+ years" should become "16 years". This is a factual-accuracy fix in a published review and a JSON entry — out of scope for an outline-only run.
2. The published review's headline entry price **€2.99/mo** is the *game server* price (ZAP's own homepage: "Gameserver from $2.99"); the **VPS** line starts at **$8.62** ("VPS from $8.62" on the live homepage), and the review's own comparison table lists **RackNerd at $1.99/mo** against a current **$2.24/mo**. Both numbers are stale on a live page.
