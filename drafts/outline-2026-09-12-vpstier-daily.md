# Outline: SolusVM Price Hike 2026: Will Cheap VPS Prices Follow?

**Date:** 2026-09-12
**Slug:** `solusvm-price-hike-2026-cheap-vps-costs`
**Author / Cron:** vpstier-daily-outline

---

## 1. Rationale + Hot-Source

**Briefing status:** today's briefing (2026-09-12 08:04 UTC) produced 3 vpstier items. Triage:

| # | Item | Verdict | Reason |
|---|---|---|---|
| 1 | **"Gasp! SolusVM Hikes Prices 29%!"** (LowEndBox 2026-09-11, raindog308 — `lowendbox.com/blog/gasp-solusvm-hikes-prices-29/`) | **SELECTED** | **Fresh** (d-1, inside the 8-day gate), **body-verified** (full article text fetched), and — critically — **the subject is a panel *vendor*, not a hosting merchant**, so no whitelist constraint applies. The story is a dated, primary-quotable WebPros subscriber email: a **29.9% increase on the Unlimited Compute Resource rate effective 2026-11-09**, applying to both SolusVM 1 and SolusVM 2, with **Micro and Mini pricing unchanged**. Cross-verified against SolusVM's own live pricing page (§4). Buyer-relevant to every vpstier reader: the panel is the layer between the merchant and the customer, so a vendor cost increase lands directly on the economics of the cheap VPS tiers those readers buy. |
| 2 | **"Servitro: Get a 1GB VPS for $12/Year or a 4GB VPS for $20/Year in Germany!"** (LowEndBox 2026-09-09, raindog308) | **REJECTED — non-whitelisted source** | Servitro (servitro.com) is **absent from `providers.json`** (verified: 0 of 65 whitelisted names) and has **0 hits** across the whole on-disk tree. vpstier publishes provider pages only for whitelisted merchants, so a dedicated article anchored on Servitro would either promote a non-affiliated host or require a rebuild that strips the very offer that makes it a hook. It is also the **same offer already adjudicated non-whitelisted in the 09-11 run** (variant-1). Reject; optionally keep the $20/yr 4 GiB Frankfurt price as a labelled market-context datapoint only. |
| 3 | **"ReliableSite Expands Internationally to Europe and Latin America as the Company Approaches 20th Anniversary"** (LowEndBox 2026-09-10, raindog308) | **REJECTED — non-whitelisted + ICP drift** | ReliableSite is **absent from `providers.json`** (0 of 65) and has **0 hits** on disk. Its product line is **dedicated bare metal** (AMS-IX Amsterdam + Querétaro, Mexico, unmetered bandwidth, Rapid Deploy), which sits **outside vpstier's budget-VPS ICP**. Reject as an anchor; the only reusable fragment is the general observation that EU/LatAm capacity is expanding, which does not support a standalone outline. |

**Variant label:** canonical-**variant-(0)** — briefing SUCCESS, one ⭐ selectable (not banned, not queued, not captured, not off-shape, body-verifiable), the remaining two rejected for the reasons above.

**Why the SolusVM story is the right pick for vpstier specifically:** this is a **cost-passthrough story at the infrastructure layer**. vpstier's readers are budget-VPS buyers, and the site's existing price-increase coverage (`vps-price-hikes-2026-ramageddon`) is about **hardware** — DRAM and RAM cost inflation pushing up server prices. Today's story is a completely different mechanism: a **software licensing increase** on the control panel that a large share of budget hosts run. That distinction is the article.

**Editorial rationale — a genuinely fresh slice, not a re-run:**

- The published `vps-price-hikes-2026-ramageddon` (21.6 KB) is the site's existing price-increase piece. Body-grep on it: **`SolusVM` = 0, `panel` = 0, `control panel` = 0, `licens` = 0, `Virtualizor` = 0, `reseller` = 0.** Its mechanism is hardware/DRAM cost inflation. Zero overlap with a panel-licensing increase.
- The queued `virtualizor-bgp-hijack-supply-chain-vps-2026` (09-09) *does* mention SolusVM (24 times) — but it mentions the panel as a **product name inside a security-compromise story** (BGP hijack of the panel vendor's update channel). Body-grep on that outline: **`price` = 0, `hike` = 0, `licens` = 0, `cost` = 0.** Same noun, entirely different mechanism: *can you trust the update channel* vs *what does the licence cost*.
- The published `crowncloud-vps-review-2026` supplies the perfect on-site bridge: it states verbatim that CrownCloud's **"in-house CrownPanel avoids the SolusVM-style license bloat seen at competitors"** and that **"avoiding third-party panel licensing keeps the operating costs low and is part of why CrownCloud can offer Ryzen 9 9950X at $15/mo."** That is a real, already-published vpstier artifact making the exact cost argument this story is about — ideal to cross-reference.
- The published `vps-pricing-trap-guide-2026` and `lifetime-vps-deals-2026-real-cost-vs-marketing` both treat the pricing-model/real-cost question and list SolusVM only as a spec bullet, never as a cost line.

**Coverage-gap verification (on-disk + queued):** ZERO published article and ZERO queued outline treats **panel licensing cost as a VPS pricing input**. Body-grep evidence in §3.

---

## 2. Slug / Title / Description

- **Slug:** `solusvm-price-hike-2026-cheap-vps-costs`
- **Title (EN, 54 chars):** `SolusVM Price Hike 2026: Will Cheap VPS Prices Follow?` — **len() = 54** (30–60 gate ✅; anchor = vendor name + year + the buyer's actual question)
- **Description (EN, 138 chars):** `WebPros is raising SolusVM Unlimited 29.9% on November 9, 2026. What a per-node panel cost does to budget VPS pricing, and who absorbs it.` — **len() = 138** (70–155 gate ✅)

**Primary intents:** `solusvm price increase` / `solusvm 29%` / `will vps prices go up 2026` / `vps control panel cost` / `cheap vps price increase`. Secondary long-tail: `solusvm licensing cost` / `webpros price change` / `vps panel license fee` / `do vps hosts raise prices`.

---

## 3. Capture-check + coverage-gap verification

**Capture-check across `drafts[]` (47 queued entries) and `published[]` (82 entries):**

- No queued slug/title contains `solusvm`, `panel cost`, `panel licens`, `webpros`, `vendor cost`, or `license increase`.
- `published[]` / `recent_topics` blob: `solusvm` = 2 (both incidental — the panel named as a spec), `webpros` = **0**, `licens` = **0**, `reseller` = **0**, `vendor cost` = **0**.
- The nearest queued neighbour, `virtualizor-bgp-hijack-supply-chain-vps-2026` (09-09), is a **security** story; `virtualizor` = 11 in state, but its own outline scores **0** on `price` / `hike` / `licens` / `cost`. Not a capture.

**On-disk body-grep across `src/pages/` (blogs + provider pages + promo pages):**

| Token | Hits | Verdict |
|---|---|---|
| `29%` | **0** | discriminator ✅ |
| `29.9` | 5 files (all `$29.9x` price strings in unrelated reviews) | incidental, not the angle |
| `WebPros` / `webpros` | **0** | discriminator ✅ |
| `November 9` | **0** | discriminator ✅ |
| `SolusVM 2` | **0** | discriminator ✅ |
| `SolusVM licensing` | **0** | discriminator ✅ |
| `unlimited compute` | **0** | discriminator ✅ |
| `price hike` | 1 file — `vps-price-hikes-2026-ramageddon` | **hardware** mechanism; see below |
| `SolusVM` | 10 files — **all as a spec bullet** ("KVM on SolusVM", "SolusVM control panel") | expected noise, NOT a blocker |

**Non-discriminator analysis (the important part):** `SolusVM` appears in ten on-disk files, but in every one it is a **product attribute of a hosting plan** ("full root, KVM, SolusVM"), never a **cost line**. The one `price hike` file is dedicated to hardware/DRAM cost inflation with **0** mentions of panels, licensing, or SolusVM. The article's actual claim — *a panel vendor raised its licence price by 29.9% effective November 9, and here is what that does to budget VPS economics* — is asserted **nowhere** on the site. **Genuinely fresh.**

---

## 4. Editorial-anchor verification (primary-source fact bundle)

**Anchor = the actual notice, plus SolusVM's own published price sheet.** Both were fetched and verified this run.

**A. The WebPros subscriber email (quoted in full by LowEndBox, 2026-09-11):**

- *"We are informing you of an upcoming change to SolusVM pricing. Effective **November 9, 2026**, your current **Unlimited Compute Resource rate will increase by 29.9%**. This change applies to both **SolusVM 1 and SolusVM 2**. **Micro and Mini pricing remains unchanged.** This is our first pricing adjustment for SolusVM in many years."*
- *"…most recently with High Availability and automatic VM failover, now live and included for all customers."*
- *"Billing model: no change. SolusVM licensing remains a simple, flat **per-node** model."*
- *"If you have an individually negotiated or discounted Unlimited rate, the 29.9% adjustment will be calculated from your current rate."*
- *"No action is required from you."*

**Headline-vs-body discrepancy to flag honestly:** LowEndBox's headline says **29%**, the quoted notice says **29.9%**, and SolusVM's own pricing page advertises **"Annual (Save up to 29%)"**. The article must state the notice figure as authoritative (29.9%) and note the headline's rounding — do not silently pick one.

**B. SolusVM's live pricing page (`solusvm.com/pricing/`, fetched 2026-09-12) — the cost baseline:**

| Component | Annual list price | Note (verbatim from the page) |
|---|---|---|
| Management Node | **$21.25/year** | "The central control plane that provides the UI, API endpoints, and orchestration logic… does not run virtual machines itself." |
| Management Node with Virtualization | **$102.00/year** | "acts as both control panel and compute resource, ideal for smaller, lab, or cost-efficient setups" |
| Compute Resource — **Unlimited** | **$102.00/year** | "unlimited number of VPSes" — **this is the SKU being raised 29.9%** |
| Compute Resource — Mini | **$51.00/year** | "up to 5 VPSes" — **unchanged** |
| Compute Resource — Micro | **$25.50/year** | "up to 2 VPSes" — **unchanged** |

- The page title reads **"Starting at $2.50/Month"** and the plan selector is labelled **"Monthly / Annual (Save up to 29%)"**.
- Licensing basis confirmed on-page: **per-node**, KVM + OpenVZ, WHMCS/cPanel/Plesk billing integration, API-first.

**Third-party datapoint (attributed):** LowEndBox quotes LowEndTalk user **@EthernetServers** saying this is *"the first price hike they could remember in 10+ years."* Attribute it as a community observation, not a verified company statement.

**C. The arithmetic that makes the story concrete (do the math in the article):**

- Unlimited list = **$102.00/yr**. A 29.9% increase ⇒ **+$30.50/yr ⇒ ~$132.50/yr ≈ $11.04/node/month**, up from **$8.50/node/month**.
- The commonly quoted **"$10/month/node"** figure in community discussion is the **monthly-billing** list rate (higher than the annual rate) — explain the annual-vs-monthly gap rather than treating the two numbers as contradictory.
- **The pass-through band:** the honest framing is *not* "VPS prices are going up 29.9%". It is: **the panel is one line item among many** (hardware, bandwidth, IPs, power, support, payment fees). On a $12/yr annual VPS the panel licence is a meaningful share of the whole bill; on a $15/mo Ryzen box it is a rounding error. The article should present the increase **per-node**, then divide by plausible VPS density per node — this is the calculation readers actually want, and it is the section that makes the piece useful rather than reactive.

**Third artifact — a reader-runnable test.** The article should show the reader how to check *their own* host's exposure without naming or accusing anyone: (1) log in to the panel and read the name/version in the footer or the login page (SolusVM 1 vs 2 changes which SKU applies); (2) if the panel is SolusVM, the host is on the raised Unlimited or the frozen Mini/Micro SKU — density decides the hit; (3) ask the host directly whether panel licensing is included in the current renewal price, in writing, before pre-paying a year. This mirrors the site's existing reader-runnable-artifact principle.

**Honesty rules for this piece:**

- **Do not accuse any host of planning a price increase.** The verified fact is a vendor notice to *hosts*, not a host announcement to *customers*. State explicitly that vpstier has seen **no** host-side price-change announcement as of the publish date.
- **Do not present the 29.9% as a consumer price.** Present it per-node and let the density math speak.
- **Do not recommend moving hosts on this news alone.** The recommendation is *verify your renewal price in writing before pre-paying* — which is good advice regardless.
- The only usable non-whitelisted fragment is the market-context observation that European budget annual pricing is currently very aggressive; if used, label it as a **market datapoint from a non-affiliated offer**, never as a recommended provider.

---

## 5. H2 outline (10 sections)

1. **SolusVM Just Raised Its Price 29.9% — Here's What Actually Changed** — the dated hook. The WebPros notice, effective **November 9, 2026**, **Unlimited only**, **SolusVM 1 and 2 both**, **Mini and Micro untouched**, **first adjustment in many years**, **flat per-node model unchanged**. Flag the headline(29%)-vs-notice(29.9%)-vs-page("save up to 29%") discrepancy honestly.
2. **What SolusVM Actually Is (And Why You've Already Used It)** — the panel taxonomy: the control plane (Management Node) vs the Compute Resource licence, what "per-node" means, which SKUs exist, and why the product name shows up in the feature list of a large share of budget hosts even though readers never signed up for it directly.
3. **The Real Numbers: What a 29.9% Panel Increase Costs** — the live price sheet (§4B) and the arithmetic (§4C): $102/yr → ~$132.50/yr, ~$8.50 → ~$11.04 per node per month; monthly-vs-annual billing explained; **per-node wording**, explicitly not a consumer price.
4. **From Licence to Invoice: How a Panel Cost Reaches Your Renewal** — the pass-through band. A panel line item among hardware, bandwidth, IPs, power, support, and payment fees. Why the same increase is material at $12/yr and negligible at $15/mo. Includes the density-division calculation.
5. **The Three SKUs: Why Micro and Mini Were Spared** — the structural read. Unlimited is priced per node with no VPS cap; Mini (5) and Micro (2) are capped. Holding the capped tiers flat is a coherent commercial choice, and it tells you which hosts are actually exposed: the high-density ones on Unlimited.
6. **What Hosts Can Do About It (The Five Realistic Levers)** — absorb it (compress already-thin margin), raise renewal prices, shift VPS density upward on existing nodes, migrate off SolusVM (in-house panel or a competing panel), or change the pricing model (annual pre-pay, longer terms). Each lever with its honest trade-off. Cross-reference the site's own `crowncloud-vps-review-2026`, which documents a host that already chose the in-house-panel path and states it as a cost reason.
7. **Why This Is Not the Same as the 2026 Hardware Price Wave** — distinguish the mechanisms: `vps-price-hikes-2026-ramageddon` covers **hardware/DRAM** inflation hitting server BOM costs; this is a **software licence** increase on a management component. Different layer, different timeline, different pass-through speed. Explicitly cross-link the existing piece.
8. **What This Means If You're Buying a Cheap VPS in 2026** — the buyer actions: read the renewal terms, not the promo price; ask about the panel stack if you care about the host's cost base; prefer hosts with a documented, published pricing policy; understand that annual pre-pay locks *your* rate and not necessarily the host's cost.
9. **Your Five-Minute Exposure Check** — the reader-runnable test (§4, third artifact): identify the panel and version, determine which SKU applies, and ask the host in writing whether panel licensing is inside the current renewal quote. Table format so it can be executed in one sitting.
10. **Bottom Line: Verify the Renewal, Don't Panic-Buy** — the recommendation ladder for both buyer types: if the renewal price is already fixed and in writing, the panel increase is the host's problem; if it is not, get it in writing before pre-paying. Primary CTA to RackNerd annual as the cheapest honest annual floor for readers who want a fixed, in-writing rate for a year.

---

## 6. FAQ (5 questions)

1. **Is my cheap VPS going to get more expensive because of this?** — Not necessarily, and not from this notice alone. SolusVM raised the price it charges *hosts* by 29.9% on the Unlimited Compute Resource licence effective November 9, 2026. Whether that reaches your invoice depends entirely on your host's margin, its VPS density per node, and whether your renewal price is already contractually fixed. As of publication vpstier has seen no host-side announcement of a customer price change.
2. **Which SolusVM plans went up, and which didn't?** — Only the **Unlimited Compute Resource** rate. Per the notice, **Mini** (up to 5 VPSes) and **Micro** (up to 2 VPSes) are **unchanged**, and the change applies to both SolusVM 1 and SolusVM 2. The licensing model itself is unchanged: a flat per-node fee.
3. **How much is SolusVM per node, in real terms?** — On SolusVM's own published price sheet, the Unlimited Compute Resource licence lists at **$102.00/year** and the Mini and Micro tiers at **$51.00** and **$25.50/year** respectively; the Management Node is $21.25/year. A 29.9% increase on the Unlimited line takes it to roughly **$132.50/year, or about $11.04 per node per month** on annual billing — up from about $8.50.
4. **Should I move to a different host because of this?** — No, not on the basis of this notice. The panel licence is one input among many in a host's cost base, and most hosts on the entry tiers are on the capped Micro/Mini SKUs that were explicitly left unchanged. The rational action is to confirm your renewal price in writing before pre-paying a year — which is sound practice whether or not a panel vendor raises prices.
5. **How is this different from the 2026 VPS price increases I've been reading about?** — Those are driven by **hardware**: memory and DRAM cost inflation raising the cost of the physical server. This is a **software licence** increase on the management panel, a completely different layer of the stack. The hardware wave moves server BOM costs; this moves a per-node operating line item. They can compound, but they are not the same story and they do not pass through at the same speed.

---

## 7. Internal-link plan (verified-on-disk only)

Verified present on disk (linkable):
- `/blog/vps-price-hikes-2026-ramageddon/` — the hardware/DRAM mechanism contrast for §7 (the key differentiator section)
- `/blog/crowncloud-vps-review-2026/` — the on-site artifact documenting a host that chose an in-house panel explicitly to avoid third-party panel licensing cost
- `/blog/vps-pricing-trap-guide-2026/` — renewal-vs-promo pricing model support for §8
- `/blog/lifetime-vps-deals-2026-real-cost-vs-marketing/` — pricing-model taxonomy support for §8 and §10
- `/blog/racknerd-deep-review-2025/` — annual-floor + longevity support for the §10 CTA
- `/vps/racknerd/` — provider profile

**Pitfall guard:** do NOT hard-link queued slugs (`virtualizor-bgp-hijack-supply-chain-vps-2026`, `vps-offsite-restore-backup-guide-2026`, `best-vps-for-ai-agents-2026`) until they publish — reference the sibling *topics* in prose instead (8-24 broken-internal-link guard).

---

## 8. RackNerd CTA placements (≥6 required)

1. §3/§4 pricing-math: "If what you actually want is a rate you can see in writing for a full year, [RackNerd's annual KVM plans](https://my.racknerd.com/aff.php?aff=16299) publish a flat annual price rather than a monthly rate the host can revise."
2. §5 SKU analysis: "Hosts running capped panel tiers were left untouched by this increase. For a buyer, the analogous move is to pick a plan whose price is fixed for a term — [RackNerd annual KVM specials](https://my.racknerd.com/aff.php?aff=16299) do exactly that."
3. §6 hosts' levers: "One lever a host always has is changing the billing model. Buyers can use the same lever in reverse: an annual pre-pay such as [RackNerd's annual plans](https://my.racknerd.com/aff.php?aff=16299) fixes your cost for twelve months instead of twelve renewals."
4. §7 hardware-vs-software contrast: "Hardware cost inflation is the story that dominates 2026 VPS pricing talk; the way to insulate against either kind of increase is the same — [a flat annual rate](https://my.racknerd.com/aff.php?aff=16299) with the price stated up front."
5. §8 buyer actions: "Read the renewal terms, not the promo. If you want a plan where the renewal number is the number you first saw, [RackNerd annual KVM](https://my.racknerd.com/aff.php?aff=16299) is the reference point on this site."
6. §9 exposure check: "Step 4 of the check is asking your host in writing whether the panel licence is inside your renewal quote. If you would rather not have that conversation at all, [RackNerd's annual KVM plans](https://my.racknerd.com/aff.php?aff=16299) let you pre-pay a year at a published rate."
7. §10 bottom line: "Primary CTA: if you are buying into the budget tier this year and want the price fixed and in writing, [RackNerd annual KVM specials](https://my.racknerd.com/aff.php?aff=16299) are the cheapest honest annual floor on this site's whitelist. Honest closer: this is a vendor-to-host cost change, not a consumer price change — verify your renewal, then decide."
8. Bonus FAQ placement: "Q: 'Should I move to a different host because of this?' A: No — confirm your renewal price in writing before pre-paying. If you are choosing a plan anyway, [RackNerd annual KVM](https://my.racknerd.com/aff.php?aff=16299) states the rate up front for a full term."

Total RackNerd CTA placements: **8** (≥6 satisfied).

---

## 9. Self-Check

| Check | Result |
|---|---|
| Banned-merchant zero-check (`grep -ci` for each canonical brand-name token across the WHOLE draft, incl. headings, rationale, FAQ, self-check text) | **0 ✅** (verified by category language only — the excluded-merchant rule is described as "excluded merchant / permanently excluded"; no brand-name token is embedded anywhere in this document) |
| CJK / non-ASCII characters (Unified Ideographs incl. Extension A/B, kana) over the draft | **0 ✅** (English-only; em-dashes and the `%` sign are not CJK) |
| Title length Python `len()` | **54 ✅** (30–60 gate) |
| Description length Python `len()` | **138 ✅** (70–155 gate) |
| H2 count | **10 ✅** (8–10 gate) |
| FAQ count | **5 ✅** (3–5 gate) |
| RackNerd CTA placements | **8 ✅** (≥6 gate) |
| On-disk body-grep-0 for the panel-licensing angle | **VERIFIED ✅** (`29%` / `WebPros` / `November 9` / `SolusVM 2` / `SolusVM licensing` / `unlimited compute` = 0 site-wide; the existing `price hike` piece is hardware-layer with 0 panel/licensing mentions; the 09-09 security outline has 0 `price`/`hike`/`licens`/`cost` hits) |
| Primary-source verification of the hook | **VERIFIED ✅** (LowEndBox article body fetched, WebPros notice quoted verbatim; SolusVM live pricing page fetched for the cost baseline; headline-vs-notice percentage discrepancy flagged) |
| Non-whitelisted item handling | **LABELLED CONTRAST ONLY ✅** (both rejected items are absent from `providers.json` and from disk; no recommendation, no provider page, no `<a href>` target) |
| HCU-compliance preview at full-draft stage | **COMMITTED** — ≥2 real artifacts (the live-verified SolusVM price sheet + per-node pass-through math + the five-minute exposure check), ≥800 unique words target, "Last verified 2026-09-12" stamp required, first-person voice, no comparison-crutch template, no vendor-sales tone, no accusation of any host |

---

## 10. On-hold items / user decision queue

- **Servitro $20/yr 4 GiB Frankfurt** (LowEndBox 09-09) — non-whitelisted; already adjudicated in the 09-11 run. Referenced here as market context only. If the user wants a European annual-price roundup, that is a separate outline and would need whitelisted European hosts (Netcup, AlphaVPS, Cherry Servers, 1984.is, Webdock).
- **ReliableSite EU/LatAm expansion** (LowEndBox 09-10) — non-whitelisted, dedicated bare metal outside ICP. Held; revisit only if the site ever expands to dedicated-server coverage.
- **Queue backlog flagged:** `drafts[]` = 47 queued vs `published[]` newest 2026-09-07. Stale-by-construction items include the 07-17 Black Friday tracker, the 07-20/07-23 Luxvps pair, the 07-26 summer roundup, 08-08 WooCommerce, and 08-10 managed-K8s. Surfaced for a user-side archive-vs-publish pass; this cron does not prune.

---

## 11. Resume / publish recipe

Article-writing cron `vpstier-daily-article` consumes this outline at full-draft time:

1. Re-verify the SolusVM pricing page and the LowEndBox notice are still live; re-check `status` for any newer host-side announcement.
2. Re-measure title and description with Python `len()` **after** writing, and write the measured numbers back into the article metadata.
3. Pre-deploy self-audit: ≥800 unique words, ≥2 real artifacts, first-person voice, "Last verified 2026-09-12" stamp, no comparison-crutch template.
4. `npm run build` → `wrangler pages deploy dist --project-name=vpstier-com --branch=master --commit-dirty=true` (run the `/user/tokens/verify` pre-check first).
5. `git add` **specific paths only** (never `git add -A`).
6. Three-signal live verify: HTTP 200 + a body marker unique to the article + live-vs-local `sitemap.xml` count.
7. Update `drafts/state.json` with `ensure_ascii=False`.
