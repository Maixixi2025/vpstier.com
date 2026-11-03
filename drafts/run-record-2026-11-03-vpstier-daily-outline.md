# Run Record — vpstier daily outline — 2026-11-03

**Cron ID:** `5fd2a36f2dc4` (vpstier-daily-outline, `45 9 * * *`)
**Run date:** 2026-11-03
**Outline produced:** `drafts/outline-2026-11-03-vpstier-daily.md`
**Slug:** `best-vps-providers-2026`
**Status:** `outline_pending_publish` — stopped before Astro/build/deploy, awaiting user `publish`
**Model:** MiniMax-M3.1-Flash via minimax-cn

---

## 1. Variant adjudication

**Variant-0 + weekly-report-driven.** Briefing SUCCEEDED (2026-11-03 08:10). Two vpstier items received; both rejected as *standalone* topics, then reused as *datapoints* inside a different article. The article itself is the single largest site-level SEO gap, explicitly recommended by the 2026-11-02 weekly strategy report (cron `537976c317e8`, vpstier pick #4) — a gap the daily briefing structurally cannot produce but the weekly report can.

| # | Briefing item | Verdict | Gate that fired |
|---|---|---|---|
| 1 | ⭐ HostNamaste Diwali 2026 Early-Bird — LA KVM VPS from $17.99/yr (LowEndBox 2026-11-02 07:00) | **REJECTED as standalone** | Variant-8: HostNamaste already has a published review (`hostnamaste-vps-review-2026.astro`, 8,491 bytes) that does not mention the Diwali offer (body-grep `17.99`/`diwali` = 0 in that file). A dated promo of a published-review merchant = captured. **Retained as a matrix datapoint** in the new hub — the first time the hub archetype exists, so the Diwali deal's matrix angle is virgin. |
| 2 | ⭐ EnderHost Toronto 4GB VPS $3.84/mo, coupon `LETSPECIAL96` (LowEndBox 2026-11-02 07:00) | **REJECTED as standalone** | Non-whitelisted: EnderHost is **absent from `providers.json`** (0 of 65) — no review possible. **Retained as a pricing-model datapoint** in the new hub (its coupon is *recurring*, which is the structural contrast). |
| 3 | (weekly report pick #4) New "Best VPS Providers 2026" comparison hub | **SELECTED** | Live GSC confirms the gap (see §2). Not captured: exact-slug grep for 4 hub variants = 0 across 293 files; live sitemap has no hub. |

---

## 2. The decisive evidence — live GSC (queried this run, token verified)

**The problem the hub fixes:** 235 of 342 30-day impressions (69%) and 835 of 1132 90-day impressions (74%) land on the **homepage `/`** at avg position 82-84. Every head-term query routes there:

| Query | Impr (30d) | Position | Landing |
|---|---|---|---|
| best vps for ai agents | 42 | 73.4 | `/` |
| virtual private server hosting reviews | 42 | 84.9 | `/` |
| best vps provider | 27 | 80.7 | `/` |
| vps hosting review | 26 | 92.5 | `/` |
| best vps providers | 18 | 80.6 | `/` |

The 61 individual reviews rank at position 1.8-6.0 but attract ~30 impressions/30d combined — because a *category* query has no category page. The weekly report flagged this exact gap (head terms at pos 80-95 on the homepage, no hub). The hub gives those head terms a real, on-intent landing page.

---

## 3. The selected story

**A head-term comparison hub — `Best VPS Providers 2026: The Shortlist Before You Compare`.** 65 providers reviewed → 8 shortlisted → one table + a decision matrix. The 8 are all whitelisted with live pages (RackNerd, Vultr, DigitalOcean, Hostinger, LightNode, Cloudzy, HostHatch, Interserver).

**The dated hook** (from today's briefing, body-fetched both HTTP 200 on 2026-11-02 LEB posts): two new offers expose **two pricing models** — EnderHost's coupon is *recurring* ($0.96/GB/mo, price stays), HostNamaste's annual plan states *no renewal price* and its regular KVM-1024 costs $90.87/yr = **12.02× the $6.99 monthly** (no annual discount; verified on the live KVM page, which has zero "renew" strings). This recurring-price vs intro-price distinction is a genuine gap (body-grep-0 on 14 angle tokens across 293 files); `vps-pricing-trap-guide-2026` covers the renewal *cliff* on intro plans but not the *model-selection* frame. The hook is time-sensitive (Diwali offer ends 2026-11-08).

**New archetype:** head-term comparison hub / provider shortlist. Adjacent pieces are complementary, not duplicate — `vps-buying-guide` (process guide, 1 CTA) and `vps-pricing-trap-guide-2026` (renewal-cliff deep-dive) vs this hub's category-level shortlist + workload/budget/location decision paths.

---

## 4. Research log (body-fetched this run)

| Source | HTTP | Bytes | Used for |
|---|---|---|---|
| lowendbox.com HostNamaste Diwali post | 200 | 168,724 | Dated hook, plan prices, owner comment |
| lowendbox.com EnderHost Toronto post | 200 | 163,573 | Recurring-coupon pricing model, "colocation / fully owned" quote |
| hostnamaste.com/special-offers.php | 200 | 66,882 | Diwali prices ($17.99-109.99/yr), end date 8 Nov |
| hostnamaste.com/kvm-vps.php | 200 | 72,310 | **No "renew" string anywhere**; KVM-1024 $6.99/mo vs $90.87/yr (12.02×) |
| racknerd.com | 200 | 34,042 | From $2.24/mo, 20 DCs, 24/7 support |
| lightnode.com | 200 | 122,615 | From $7.71/mo, 40+ locations, hourly |
| cloudzy.com | 200 | 501,199 | From $2.48/mo promo, EPYC+DDR5+40Gbps |
| hostinger.com/vps-hosting | 200 | 1,466,151 | KVM 1 $6.49, KVM 2 $8.79, KVM 4 $12.99, KVM 8 $25.99 |
| digitalocean.com/pricing/droplets | 200 | 492,600 | Per-second billing, Basic from $4/mo |
| GSC API (direct, token verified) | 200 | — | query×page + page dims, 30d + 90d |
| vpstier.com/sitemap-0.xml | 200 | — | Confirmed no hub URL exists |

**Unverifiable (declared, not guessed):** HostNamaste renewal price (unstated); Vultr + Contabo live pricing (HTTP 403 from sandbox); EnderHost current stock (enderhost.com DNS not resolved); RackNerd dedicated KVM page `/kvm-vps/` (HTTP 500).

---

## 5. Affiliate + integrity

- **8 RackNerd CTA placements** (≥6 required), every one labelled + `rel="sponsored noopener"`, all pointing to `https://my.racknerd.com/aff.php?aff=16299`.
- **Affiliate-label integrity:** EnderHost and HostNamaste (the case-study providers) and the 6 non-affiliate shortlist providers receive **no** affiliate CTA — they are comparison subjects only.
- **Fairness discipline:** HostNamaste's renewal framed as "unstated", never "a hike"; EnderHost's price-stated reason quoted verbatim from the LEB body. No motive claimed.

---

## 6. Self-check results (all run against the committed draft)

| Check | Result |
|---|---|
| Excluded-merchant token | 0 (Python case-insensitive count over whole draft) |
| CJK characters | 0 (standard CJK-range regex) |
| Deprecated language-prefix path | 0 (generic phrasing) |
| Title length | 57/60 (first pass was 61 — fixed by dropping the lead "The"; **re-verified after the fix**, canonical pitfall #22) |
| Description length | 138/155 |
| H2 count | 10 |
| FAQ count | 5 |
| RackNerd CTAs | 8 |
| Cross-links | 10, all targets verified on disk (10 queued-but-unpublished targets excluded) |
| Slug collision | none (published[] 84, drafts[] 58, src/pages/blog/ 61, live sitemap, 4 exact-slug variants) |
| Content gap | exact-slug = 0; 14 pricing-model angle tokens = 0 across 293 files |
| Real artifacts | 2 (GSC query×page evidence; fresh price-table + 12.02× finding) |

---

## 7. Pre-existing queue defects (flagged, not fixed — separate cleanup)

1. `published[]` ∩ `drafts[]` still overlaps on `best-vps-deals-codes-2026` and `webdock-vps-review-2026`.
2. One stale deprecated-language-prefix source file (`vps-pricing-trap-guide-2026.astro` under the old language tree) remains and is still built into the deprecated dist path (the deprecated language route was supposed to be fully removed on 2026-06-11).
3. Three orphaned `/vps/` pages (`hostdare`, `hostnoc`, `vpsdime`) have no `providers.json` entry.
4. The site has **no category-level hub** — this outline is the fix; until it publishes, the homepage keeps absorbing head terms at pos 80-95.

---

## 8. Commit plan

- **Commit 1 (drafts):** `git add drafts/outline-2026-11-03-vpstier-daily.md drafts/run-record-2026-11-03-vpstier-daily-outline.md` → `feat(drafts): ...`
- **Commit 2 (state):** `git add drafts/state.json` → `chore(state): ...`
- Never `git add -A` (sweeps the orphan backlog).
- Both commits use `git commit -F <file>` (canonical pitfall — shell `$` corrupts price strings in `-m`).
