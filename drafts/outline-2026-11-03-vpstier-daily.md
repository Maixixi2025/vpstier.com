# Outline: The Best VPS Providers 2026 — The Shortlist Before You Compare

**Date:** 2026-11-03
**Slug:** `best-vps-providers-2026`
**Author / Cron:** vpstier-daily-outline (`5fd2a36f2dc4`)
**Variant:** variant-0 + weekly-report-driven — briefing SUCCEEDED (2026-11-03 08:10) with fresh dated picks; selected the single largest site-level SEO gap (head-term hub) that the daily briefing cannot produce but the 2026-11-02 weekly strategy report (cron `537976c317e8`) explicitly recommended as vpstier pick #4 (highest ROI). Anchored on a fresh dated pricing finding from the briefing's own picks.
**Archetype:** head-term comparison hub / provider shortlist (NEW on vpstier — the site has 61 individual reviews ranking at position 2-6 but **zero** page consolidates them; the homepage currently absorbs every head-term query at position 80-95)
**Status:** `outline_pending_publish` — awaiting user `publish`

---

## 1. Rationale + Hot-Source

### 1a. Why this outline (the SEO problem it fixes, pulled from live GSC — verified 2026-11-03)

Live GSC (queried directly this run, token verified):

| Window | Impressions | Landing pages | Avg position |
|---|---|---|---|
| **30-day** | 342 | 34 | — |
| **→ on the homepage `/`** | **266** (**78%**) | 1 | 82.4 |
| **→ on every article + `/vps/` profile combined** | 76 | 33 | 3-9 |
| **90-day** | 1132 | 62 | — |
| **→ on the homepage `/`** | **835** (**74%**) | 1 | 84.4 |

The 30-day query×page report shows **every single head-term query** landing on the homepage:

| Query | Impr (30d) | Position | Landing page |
|---|---|---|---|
| best vps for ai agents | 42 | 73.4 | `/` (homepage) |
| virtual private server hosting reviews | 42 | 84.9 | `/` |
| virtual server hosting reviews | 36 | 83.8 | `/` |
| best vps provider | 27 | 80.7 | `/` |
| vps hosting review | 26 | 92.5 | `/` |
| best vps providers | 18 | 80.6 | `/` |
| best vps service | 7 | 78.4 | `/` |
| reliable vps | 7 | 91.4 | `/` |
| vps hosting reviews | 7 | 80.3 | `/` |
| best unmanaged vps | 6 | 85.8 | `/` |
| vps comparison | 6 | 87.3 | `/` |
| compare vps providers | 3 | 85.3 | `/` |

The diagnosis is exact: the site's 61 individual provider reviews rank at position 2-6 (strong long-tail) but attract almost no impressions, because buyers issuing a *category* query ("who are the best VPS providers?") never find a single page answering it. The site has **no head-term hub** — and a homepage is the weakest page to rank one (thin, off-intent). The 2026-11-02 weekly strategy report flagged exactly this as vpstier pick #4 (paraphrased — the original is in the weekly cron output): build a "Best VPS Providers 2026" comparison hub, because the head terms (vps provider 61 impr., virtual server hosting reviews 43 impr.) all sit at position 80-95 on the homepage and there is no hub page in the site. Today builds that hub.

### 1b. The dated hook (fresh, from today's briefing — picked #3 ⭐, body-verified)

The 2026-11-03 briefing (cron `3ea88f8bb2d0`) carried two fresh LowEndBox posts published **2026-11-02 07:00** (body-fetched this run, both HTTP 200):

1. **HostNamaste Diwali 2026 Early-Bird Special — Los Angeles KVM VPS from $17.99/Year** (`lowendbox.com/blog/hostnamaste-diwali-2026-early-bird-special-…`, 168,724 bytes) — KVM 1GB **$17.99/yr** (≈$1.50/mo), KVM 2GB **$29.99/yr** (≈$2.50/mo), KVM 4GB **$59.99/yr** (≈$5.00/mo); AMD EPYC 7402P, enterprise NVMe, ECC registered RAM; **offer ends 8 November 2026**; the owner (Mitesh, HostNamaste.com) left a comment on the post at 07:12 confirming the offer.
2. **EnderHost Toronto 4GB VPS — $3.84/month** (163,573 bytes) — coupon `LETSPECIAL96` = **36% off recurring**, bringing Ryzen 9 9950X + DDR5 + NVMe to **$0.96/GB/month recurring**; the provider is quoted on *why* the price is low: *"We have access to highly competitive colocation pricing in Toronto, we're able to source our hardware at favorable prices, and the infrastructure is fully owned by EnderHost."*

**The pricing-model finding (new on vpstier).** These two posts, side by side, expose a structural point no existing article makes: **EnderHost's coupon recurs** — the $0.96/GB is *"per month recurring"*, so the price you pay is the price you keep paying — while **HostNamaste's annual plan carries no stated renewal price at all.** The Diwali page (fetched 2026-11-03, 66,882 bytes) lists annual prices but never states what you pay at renewal, and the main KVM VPS page (72,310 bytes, fetched 2026-11-03) contains **no occurrence of the string "renew" anywhere**. Meanwhile the same HostNamaste KVM-1024 plan lists monthly $6.99 but annual $90.87 — i.e. paying for a year upfront costs **12.02× the monthly price, with zero annual discount** (verified on the live KVM page this run). Both are honest; they are *different pricing models*, and the difference — recurring-coupon vs unstated-renewal — is exactly what a buyer must learn to read. A site with 65 providers and `vps-pricing-trap-guide-2026` (which covers the *renewal cliff* on intro plans) has nothing on *reading which pricing model an offer uses before you buy*. (body-grep-0 on 14 pricing-model angle tokens across 293 files.)

**Affiliate-label integrity:** EnderHost and HostNamaste are **not** the affiliate; they are dated datapoints in §3 only. Neither receives an affiliate CTA. The primary affiliate is RackNerd (`https://my.racknerd.com/aff.php?aff=16299`) and every CTA is labelled.

### 1c. Capture-check (why this is not a duplicate)

- **Briefing pick #3 (HostNamaste $17.99/yr ⭐):** REJECTED as the standalone topic — HostNamaste already has a published review (`hostnamaste-vps-review-2026.astro`, 8,491 bytes) that does **not** mention the Diwali offer (body-grep for `17.99`/`diwali` = 0 in that file), so variant-8 (dated promo of a published-review merchant) would normally fire. **But** the offer is usable as a supporting datapoint inside a different article — variant-0 for the *hub*, with the Diwali deal as one price anchor in the matrix. This is the first time the hub archetype has been drafted, so the Diwali deal's *matrix* angle is virgin.
- **Briefing pick #4 (EnderHost Toronto ⭐):** REJECTED as the standalone topic — EnderHost is **absent from `providers.json`** (0 of 65), so a review would be non-whitelisted; retained only as a supporting datapoint in §3 (the recurring-coupon pricing model).
- **Weekly report pick #4 (Best VPS Providers hub):** NOT captured. Exact-slug grep (`best-vps-providers-2026` / `best-vps-providers` / `best-vps-2026` / `vps-provider-comparison-2026`) = 0 across all 293 files. The live sitemap contains no such URL. The `/compare/` page is a 4-provider affiliate-commission table, not a provider shortlist.
- **Adjacent-queue neighbour check:** `best-vps-for-ai-agents-2026` (2026-08-14) is a niche (AI-agent) use-case piece; `best-north-america-vps-2026` / `best-asia-pacific-vps-2026` are region-specific. None is a category-wide "best providers" hub. No collision.

### 1d. Fact table (every row traced to a body-fetched primary or live GSC this run)

| # | Fact | Value | Source |
|---|---|---|---|
| 1 | 30-day impressions | 342 across 34 pages | GSC API (verified 2026-11-03) |
| 2 | 30-day homepage share | 266 / 342 = **78%** | GSC API, query×page |
| 3 | 90-day homepage share | 835 / 1132 = **74%** | GSC API, page dimension |
| 4 | Head-term position band | 73.4 – 92.5 | GSC API (best vps for ai agents 73.4 … vps hosting review 92.5) |
| 5 | Article position band | 1.8 – 6.0 | GSC API (netcup /vps/ pos 9.2, aliyun review pos 4.7, kainode pos 1.8) |
| 6 | Provider inventory | 65 in providers.json, 68 live `/vps/` pages | providers.json + `ls /src/pages/vps` |
| 7 | Diwali KVM 1GB price | $17.99/yr ≈ $1.50/mo | HostNamaste special-offers.php (HTTP 200, 66,882 B, 2026-11-03) |
| 8 | Diwali offer end date | **8 November 2026** | same page (countdown + text) |
| 9 | Diwali hardware | AMD EPYC 7402P, 256GB ECC registered RAM, enterprise Intel NVMe | same page + LEB post |
| 10 | EnderHost recurring price | $0.96/GB/month recurring, coupon `LETSPECIAL96` | LEB post (163,573 B) |
| 11 | EnderHost price-stated reason | "highly competitive colocation pricing in Toronto… infrastructure is fully owned by EnderHost" | LEB post, provider quote |
| 12 | HostNamaste renewal price | **NOT stated** — zero "renew" strings on the KVM VPS page | hostnamaste.com/kvm-vps.php (72,310 B, 2026-11-03) |
| 13 | HostNamaste annual-vs-monthly | KVM-1024: monthly $6.99 → annual $90.87 = **12.02× monthly, no annual discount** | same KVM page (both figures listed) |
| 14 | RackNerd entry price | VPS from **$2.24/mo** | racknerd.com homepage (HTTP 200, 34,042 B, 2026-11-03) |
| 15 | RackNerd network | 20 datacenter locations, 24/7 support | racknerd.com homepage |
| 16 | RackNerd site profile | $1.99/mo entry, root access, KVM, $50-100/sale, 90-day cookie | `/vps/racknerd/` + providers.json |
| 17 | Hostinger KVM 1 | $6.49/mo intro, KVM 2 $8.79, KVM 4 $12.99, KVM 8 $25.99 | hostinger.com/vps-hosting (HTTP 200, 1.47 MB, 2026-11-03) |
| 18 | LightNode | KVM VPS from $7.71/mo, 40+ locations, hourly billing | lightnode.com (HTTP 200, 122,615 B) |
| 19 | Cloudzy | VPS from $2.48/mo (promo), AMD EPYC + DDR5 + 40 Gbps | cloudzy.com (HTTP 200, 501,199 B) |
| 20 | DigitalOcean | per-second billing from $0.01/min 60s, Basic Droplets from $4/mo | digitalocean.com/pricing/droplets (HTTP 200, 492,600 B) |
| 21 | Content gap | exact-slug grep for the hub = 0 across 293 files; no `best vps providers` hub in sitemap | own grep + live sitemap |

**Facts deliberately NOT asserted:** that HostNamaste's Diwali plan will renew at a higher price (the renewal price is unstated, not necessarily higher — the article says "unstated", not "a hike"); that EnderHost is the cheaper provider overall (per-GB and per-plan measure differently); that the hub page will outrank the homepage (the article frames it as "gives head terms a real landing page", a structural fix, not a ranking promise); any claim about the 3 orphaned `/vps/` pages (hostdare / hostnoc / vpsdime) which have no providers.json entry — noted as a separate cleanup, not used here.

### 1e. What could NOT be verified this run (stated so the drafter does not guess)

- **HostNamaste Diwali renewal price** — unstated on the page; flagged as a "check with the host" item, never invented. (Same honesty rule as the 2026-11-02 account-suspension outline.)
- **Vultr and Contabo live pricing** — both returned HTTP 403 from the sandbox (vultr.com/pricing, contabo.com/en/vps); use the figures already on their vpstier review pages (`vultr-deep-review.astro`, `contabo-vps-review-2025.astro`) and mark "re-verify at draft time."
- **EnderHost current plan stock** — enderhost.com did not resolve from the sandbox; the LEB post (2026-11-02) is the dated source; mark "re-verify at draft time."

---

## 2. Slug / Title / Description

**Slug:** `best-vps-providers-2026`

**Title:** `Best VPS Providers 2026: The Shortlist Before You Compare` — **57 / 60 char gate**

**Description:** `We reviewed 65 VPS providers. The 8 worth your money in 2026, the pricing trap that decides the real price, and one offer that ends Nov 8.` — **148 / 155 char gate** (specificity + "65 providers" trust signal + dated hook). (Python `len()` verified.)

**Target keywords (from live GSC):** `best vps providers 2026`, `best vps providers`, `best vps provider`, `best vps for ai agents`, `virtual private server hosting reviews`, `vps hosting review`, `best vps service`, `reliable vps`, `vps comparison`, `compare vps providers`, `best unmanaged vps`.

---

## 3. H2 Chapter Plan (10 sections)

1. **Why "Best VPS Provider" Is the Wrong First Question** — the opener that earns the click and sets the article apart. Reframe: there is no single "best" — there is a shortlist of ~8, and the right pick depends on which of three things you optimise for (price, location, workload). First-person hook: *"I've now reviewed 65 VPS providers for this site. Here is the honest shortlist — and the one pricing trap that changes what 'cheap' actually means."* State the scope (65 providers reviewed, 8 on the shortlist) and the promise (a decision path, not a listicle).

2. **The Shortlist at a Glance — 8 Providers, One Table** — the money section and the primary artifact. A single comparison table with columns: Provider | Starting price | Best for | Datacenters | CPU/storage | Rating. The 8 shortlist picks (all whitelisted, all live `/vps/` + `/blog/` pages): **RackNerd** (budget / $1.99-2.24/mo / 20 DCs), **Vultr** (global production / $2.50/mo / 16+ DCs), **DigitalOcean** (developer ecosystem / $4/mo), **Hostinger** (beginner + managed / $6.49/mo), **LightNode** (40+ locations, hourly / $7.71/mo), **Cloudzy** (EPYC+DDR5 value / $2.48/mo promo), **HostHatch** (storage-optimised), **Interserver** (price-lock, $6/mo, unlimited bandwidth). This is the table the head-term query wants and the homepage lacks.

3. **A Fresh 2026 Pricing Signal: Two New Offers, Two Pricing Models** — the dated, body-verified hook. Walk the two 2026-11-02 LowEndBox offers (HostNamaste Diwali $17.99/yr ending 8 Nov; EnderHost $0.96/GB recurring). Draw the structural contrast: EnderHost's coupon **recurs** (the price stays), HostNamaste's annual plan **states no renewal price** and its regular KVM-1024 costs 12.02× monthly with no annual discount. The buyer lesson: **the sticker price and the recurring price are different numbers, and the offer text tells you which one you're getting.** State plainly that both providers are honest — the point is learning to read which model an offer uses.

4. **How We Tested — Reading 65 Providers So You Don't Have To** — the trust / E-E-A-T section and the article's spine. Explain the selection: 65 providers reviewed across the site (every one has a `/vps/` profile and most a `/blog/` review), shortlisted to 8 on price transparency, location coverage, workload fit, and track record. Include a "what we did NOT shortlist, and why" sub-note (e.g. cheap-intro-renewal-cliff providers fall to the pricing-trap guide; single-niche providers go to region guides). First-person: what the author actually did.

5. **The Pricing-Model Trap — The One Check That Decides the Real Price** — the analytical core, and the most-linked section. The recurring-price vs intro-price distinction, extended from `vps-pricing-trap-guide-2026` to a *model-selection* frame. Three models: (a) **recurring / price-lock** (RackNerd budget tiers, Interserver, EnderHost coupon) — the price is the price; (b) **intro-then-cliff** (Hostinger KVM $6.49→$11.99 at renewal) — cheap first, expensive later; (c) **unstated renewal** (HostNamaste Diwali annual) — you won't know year-2 cost until you ask. Give the one question to ask any host before paying: *"Is the price on this page the price I pay every term, and what does it become at renewal?"* Link `vps-pricing-trap-guide-2026` as the deep-dive.

6. **Pick by Workload — 5 Scenarios, 3 Answers Each** — the decision matrix (the hub's real job). Rows: *First VPS / learning* → RackNerd or Hostinger; *Production web app / API* → Vultr or DigitalOcean; *AI agent / local LLM* → Vultr (global + NVMe) or RackNerd high-RAM; *Global / multi-region latency* → LightNode (40+ DCs) or Vultr; *Storage-heavy / backup box* → HostHatch or Contabo (storage-optimised). Each row: one-line why. This is the section the head-term searcher actually wants.

7. **Pick by Budget — Under $3, Under $6, Under $12** — the price-band view the buying guide lacks. Under $3/mo: RackNerd ($1.99-2.24), Cloudzy promo ($2.48), HostNamaste Diwali ($1.50/mo equiv, ends 8 Nov). Under $6: Vultr ($2.50+), DigitalOcean ($4), Interserver ($6). Under $12: Hostinger KVM 2-4, LightNode. Flag the dated Diwali offer as the cheapest current annual entry and note its renewal is unstated.

8. **Pick by Location — Where Your Users Are** — the latency tie-breaker. US: RackNerd (20 DCs), Vultr, DigitalOcean. EU: Vultr/DO/Cloudzy Frankfurt + Amsterdam, HostHatch, Netcup. Asia-Pacific: LightNode (40+ incl. APAC), Vultr, HostNamaste (India). Cross-link `best-asia-pacific-vps-2026` + `best-north-america-vps-2026` for the region deep-dives.

9. **What "Best" Actually Means — Transparency Over Hype** — the verdict criteria, honestly stated. Best = (a) states the recurring price, (b) has a real track record (not a 6-month reseller), (c) covers your region, (d) fits the workload. Why a transparent $5 plan beats a hidden-cliff $2 plan. Anti-listicle framing: *"Anyone can rank 10 providers. The useful question is which one won't surprise you at month 13."*

10. **The Verdict + The One Question to Ask Before You Pay** — the close. Summarise: 8 providers, one table, one pricing-model check. End on the buyer-action question (*"Is this the price every term, and what does it become at renewal?"*) and the affiliate CTA: the transparent budget baseline is RackNerd (from $2.24/mo, stated price). Closing line: the shortlist changes, but the pricing-model question is the part you control.

---

## 4. FAQ (5 questions)

1. **Who is the best VPS provider in 2026?** — There isn't one "best" — there's a shortlist of about 8 that depend on what you optimise for. For the cheapest transparent price, RackNerd (from $1.99-2.24/mo, stated recurring price, 20 datacenters). For global production apps, Vultr or DigitalOcean. For 40+ locations and hourly billing, LightNode. The right pick is the shortlist member whose region, workload fit, and — above all — *pricing model* matches your need. This article's table is the whole shortlist side by side.

2. **How many VPS providers are there, and how do I choose?** — This site alone has reviewed 65, and the honest shortlist is 8. Choose in three steps: (1) pick your workload (first box, production app, AI agent, storage, multi-region); (2) filter the shortlist by price band and location; (3) run the one pricing check — ask whether the listed price is the recurring price and what it becomes at renewal. A provider that answers clearly is a safer pick at the same price than one that doesn't.

3. **What's the cheapest reliable VPS in 2026?** — For a transparent, stated recurring price, RackNerd (from $1.99/mo) and Cloudzy (from $2.48/mo promo) are the cheapest with a clear price. The current cheapest *annual* entry is HostNamaste's Diwali offer ($17.99/yr ≈ $1.50/mo, ending 8 November 2026) — but note that plan states no renewal price, so the real long-term cost is unknown. Cheap and reliable aren't the same as cheap and stated; prefer a host that tells you the recurring price.

4. **Is the cheapest VPS price the real price?** — Usually not. Three pricing models hide the real cost: (a) a **recurring/price-lock** plan — the price is the price (RackNerd budget tiers, Interserver); (b) an **intro-then-cliff** plan — cheap first term, large renewal jump (e.g. Hostinger KVM 1 $6.49/mo intro renewing to $11.99/mo, a 1.85× cliff); (c) an **unstated-renewal** plan — the page never says what year two costs. The real price is the recurring price. Always ask, before paying: *"Is this the price every term, and what does it become at renewal?"*

5. **How is this different from the other "best VPS" lists?** — Most are 10-provider listicles with no testing and affiliate links to all ten. This one is built from 65 providers this site has actually reviewed, shortlisted to 8, and — critically — it leads with the pricing-model trap (the one check that changes the real price) rather than a ranked list. It also consolidates the site's individual reviews into one decision path, so a category query ("best VPS providers") finally has a real landing page instead of bouncing off the homepage.

---

## 5. RackNerd Affiliate CTA Placements (8 — minimum 6 required)

All placements use `https://my.racknerd.com/aff.php?aff=16299`, identify RackNerd as the affiliate provider, and carry `rel="sponsored noopener"`. **Affiliate-label integrity:** every CTA names RackNerd; the two briefing-case-study providers (HostNamaste, EnderHost) and the other 6 shortlist providers receive **no** affiliate CTA — they are comparison subjects, and the shortlist stays non-transactional.

| # | Section | Placement direction |
|---|---|---|
| 1 | §1 opener | "the transparent budget baseline we recommend" → the affiliate, named |
| 2 | §2 shortlist table | After the table: "the cheapest *stated* recurring price on the shortlist" → RackNerd |
| 3 | §5 pricing-model trap | "the model-a (recurring) example we'd steer a budget buyer to" → RackNerd |
| 4 | §6 workload matrix — First VPS | The "first box" row recommendation → RackNerd |
| 5 | §7 under-$3 band | The transparent-cheapest pick in the band → RackNerd |
| 6 | §8 US location | The US budget pick → RackNerd |
| 7 | §9 transparency verdict | "states the recurring price" example → RackNerd |
| 8 | §10 verdict close | Final CTA — "the box where the price on the page is the price you pay" → RackNerd |

**RackNerd facts used** (re-verified live 2026-11-03, homepage HTTP 200 / 34,042 bytes): VPS **from $2.24/mo**; **20 datacenter locations** across North America / Europe / Asia; **24/7 support**. Site profile (`/vps/racknerd/` + providers.json): **$1.99/mo** entry, root access, KVM, **$50-100/sale** commission, 90-day cookie. Homepage figure ($2.24/mo) quoted, with a **"Last verified 2026-11-03"** stamp on the fact table. KVM plan specs + current stock must be re-verified from the live KVM page at draft time (the dedicated `/kvm-vps/` path returned HTTP 500 on this run — flag it, don't guess).

---

## 6. Cross-Links (10 — all targets verified to exist on disk this run)

1. `/blog/vps-buying-guide/` — the beginner buying guide, for §6 workload paths
2. `/blog/vps-pricing-trap-guide-2026/` — the renewal-cliff deep-dive, for §5 (its "Core Provider Comparison" is 8 rows vs this hub's decision matrix — complementary, not duplicate)
3. `/blog/2026-black-friday-cheap-vps-under-25/` — the dated cheap-VPS piece, for §7 budget bands
4. `/blog/best-north-america-vps-2026/` — region deep-dive, for §8
5. `/blog/best-asia-pacific-vps-2026/` — region deep-dive, for §8
6. `/blog/racknerd-deep-review-2025/` — the affiliate's own review (CTA integrity: still labelled)
7. `/blog/hostnamaste-vps-review-2026/` — the Diwali provider's existing review, linked from §3
8. `/blog/lightnode-vps-review-2026/` — the 40+ location pick's review, linked from §6
9. `/blog/vultr-deep-review/` — the global production pick's review, linked from §6
10. `/vps/racknerd/` — the affiliate provider profile, for the §10 final CTA

**Deliberately excluded (queued but no live `.astro` — linking would produce a dead path):** `best-vps-for-ai-agents-2026`, `vps-vs-vds-2026-which-to-choose`, and all other `outline_pending_publish` slugs.

---

## 7. Self-Check (Pre-Commit)

| Check | Result |
|-------|--------|
| Excluded merchant named anywhere in this document | 0 — verified by Python case-insensitive token count over the whole draft |
| CJK characters in this document | 0 — verified via the standard CJK-range regex over the whole draft |
| Deprecated language-prefix path written into prose | 0 — no language-prefix path appears anywhere (generic phrasing used) |
| Title length | 57 / 60 — Python `len()` on the final rendered string |
| Description length | 148 / 155 — Python `len()` on the final rendered string |
| H2 count | 10 |
| FAQ count | 5 |
| RackNerd CTA placements | 8 (≥6 required) |
| Cross-links | 10 — every target path verified to exist on disk this run (10 queued-but-unpublished targets deliberately excluded) |
| Slug collision | none — `best-vps-providers-2026` absent from `published[]` (84), `drafts[]` (58), `src/pages/blog/` (61 files), live sitemap, and all 4 exact-slug variants grepped across 293 files |
| Content-gap confirmation | 0 across 293 files for the exact hub slug + 14 pricing-model angle tokens; the recurring-price / annual-carries-no-discount finding is virgin territory |
| Briefing-item adjudication | 2 vpstier items received; both rejected as standalone topics (#3 HostNamaste = variant-8 captured promo reused as a matrix datapoint; #4 EnderHost = non-whitelisted reused as a pricing-model datapoint). 1 weekly-report hub recommendation selected |
| Freshness of the dated hook | 2026-11-02 LowEndBox posts (both body-fetched HTTP 200); HostNamaste offer ends 2026-11-08 |
| Real artifacts present (HCU #3) | 2 — (1) the live GSC query×page + page-dimension evidence (78% of impressions on `/` at pos 82); (2) the fresh HostNamaste Diwali vs EnderHost recurring price table + the KVM-1024 12.02× monthly/annual finding from the live vendor page |
| Every fact in §1d traced to a body-fetched primary or GSC | 21 / 21 — GSC API, LEB ×2, HostNamaste ×2, racknerd.com, lightnode.com, cloudzy.com, hostinger.com, digitalocean.com |
| Unverifiable items declared, not guessed | 4 — HostNamaste renewal price (unstated), Vultr + Contabo live pricing (403), EnderHost stock (DNS), RackNerd dedicated KVM page (HTTP 500) |
| Vendor-fact verbatim discipline | The EnderHost "colocation / fully owned" quote is from the LEB body, not paraphrased; HostNamaste renewal framed as "unstated", never "a hike" |
| Anti-defamation / fairness discipline | EnderHost + HostNamaste are comparison subjects, never recommendations, never affiliate destinations; no motive claimed |
| Affiliate-label integrity | All 8 CTA placements identify RackNerd; none attached to the case-study or comparison providers |
| Whitelisted provider set | All 8 shortlist providers whitelisted (`providers.json`, 65 entries) with live `/vps/` pages; case-study providers not recommended |
| Duplicate-of-neighbour check | `/vps-buying-guide` (process guide, 8-row static table, 1 CTA) + `vps-pricing-trap-guide-2026` (renewal-cliff deep-dive) + region guides are complementary, not duplicate — this hub's job is the category-level shortlist + decision matrix |
| Publish cadence | Monday-only since 2026-08-28 HCU pause. **Next slot 2026-11-09** (the 2026-11-02 slot was taken by `dreamhost-breach-2026-password-reuse-vps`) |
| Pre-existing queue defect (not today's work) | `published[]` ∩ `drafts[]` overlap on `best-vps-deals-codes-2026` + `webdock-vps-review-2026`; 1 stale deprecated-language-prefix source file (`vps-pricing-trap-guide-2026.astro` under the old language tree) still built into the deprecated dist path; 3 orphaned `/vps/` pages (hostdare/hostnoc/vpsdime) with no providers.json entry — all flagged for a separate cleanup, not today's deliverable |

---
*End of outline — awaiting user `publish` to trigger the article-writing cron.*
