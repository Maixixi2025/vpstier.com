# vpstier Add-Provider-and-Review Run — 2026-07-31 (Cloudzy)

## Result: SUCCESS

**Provider added:** Cloudzy (independent self-funded cloud provider, formerly RouterHosting, founded 2008, headquartered in Dubai UAE)

**Files created:**
- `src/pages/vps/cloudzy.astro` (provider card, ~11KB → built 18,614B)
- `src/pages/blog/cloudzy-vps-review-2026.astro` (long-form review, ~29KB → built 35,961B)
- `drafts/cloudzy-verified-data-2026-07-31.md` (verified-data source file)
- `drafts/vpstier-add-provider-2026-07-31-cloudzy.md` (this file)

**Files modified:**
- `src/pages/vps/index.astro` (+1,337 chars, Cloudzy card inserted at end of grid)
- `src/data/providers.json` (+5,349 chars, Cloudzy entry appended after hosthatch; total 56 → 57 providers)
- `drafts/state.json` (appended new published entry; published 60 → 61)

**Build:** `NODE_OPTIONS=--max-old-space-size=512 npm run build` → 92 pages built in 3.05s ✅
**Deploy:** `npx wrangler pages deploy dist --project-name=vpstier-com --commit-dirty=true` → 94 files uploaded (6 already), 2.25s, deployment ID `50003e86` ✅

**Live URLs (verified HTTP 200 + correct content, 2026-07-31):**
- https://vpstier.com/vps/cloudzy/ (18,614B, title "Cloudzy VPS Review 2026: EPYC + DDR5 + 40 Gbps from $2.48/mo")
- https://vpstier.com/blog/cloudzy-vps-review-2026/ (35,961B, title "Cloudzy VPS Review 2026: EPYC + DDR5 + 40 Gbps from $2.48/mo")
- https://vpstier.com/vps/ (76,257B, 45 VPS cards — was 44, Cloudzy card present)
- Preview: https://50003e86.vpstier-com.pages.dev/

## Verified Data (sourced from live cloudzy.com fetch 2026-07-31)

### Identity
- **Provider:** Cloudzy
- **Formerly known as:** RouterHosting (rebranded to Cloudzy, same operator)
- **Legal name:** Cloudzy AI Information Technology L.L.C. (UAE Free Zone L.L.C.)
- **Founded:** 2008 (18 years operating continuously, never acquired, never VC-funded)
- **HQ:** Al Goze Industrial First, Bin Dasmal Building 1, Office 80, Dubai, UAE
- **Customer count:** 122,000+ developers and businesses
- **Trustpilot rating:** 4.6/5 (verified via cloudzy.com Trustpilot link)

### Datacenters (13 active + Tokyo coming soon)
| Region | Cities |
|---|---|
| North America | Los Angeles, New York, Miami, Dallas, Las Vegas, Toronto |
| Europe | Amsterdam, Frankfurt, London, Milan |
| Asia-Pacific | Singapore, Sydney (Tokyo coming soon) |

### Plan Matrix — Cloud VPS Regular CPU (verified 2026-07-31)
| Tier | RAM (DDR5) | vCPU | Transfer | Storage (NVMe) | Promo (50% off) | Standard |
|---|---|---|---|---|---|---|
| Sandbox | 512 MB | 1 | 1 TB @ 40 Gbps | 20 GB | $2.48/mo | $4.95/mo |
| Entry | 1 GB | 1 | 1 TB @ 40 Gbps | 25 GB | $3.48/mo | $6.95/mo |
| Standard | 2 GB | 1 | 3 TB @ 40 Gbps | 60 GB | $7.48/mo | $14.95/mo |
| Popular | 4 GB | 2 | 5 TB @ 40 Gbps | 120 GB | $14.48/mo | $28.95/mo |
| Performance | 8 GB | 4 | 7 TB @ 40 Gbps | 240 GB | $26.48/mo | $52.95/mo |
| Mid-Pro | 12 GB | 4 | 8 TB @ 40 Gbps | 300 GB | $34.98/mo | $69.95/mo |
| Pro | 16 GB | 8 | 10 TB @ 40 Gbps | 350 GB | $49.98/mo | $99.95/mo |
| High | 24 GB | 8 | 12 TB @ 40 Gbps | 450 GB | $69.98/mo | $139.95/mo |
| Heavy | 32 GB | 12 | 12 TB @ 40 Gbps | 750 GB | $109.98/mo | $219.95/mo |
| Workhorse | 64 GB | 16 | 16 TB @ 40 Gbps | 1500 GB | $199.98/mo | $399.95/mo |

**High-Frequency AMD Ryzen 4.2 GHz+ line:** identical spec/price matrix to Regular CPU line, but with 4.2 GHz+ Ryzen cores for game servers / trading bots / single-thread workloads. Starts at 1 GB / $3.48/mo promotional.

### Differentiators (verified from live cloudzy.com)
- **Independent self-funded since 2008** — never acquired, never VC-funded
- **AMD EPYC + DDR5 + pure NVMe** — uniform modern infrastructure on every tier
- **40 Gbps shared uplink** per node — present even on the $2.48/mo entry
- **13 datacenter locations** — NA, EU, APAC (Tokyo coming soon as 14th)
- **Monero (XMR) accepted directly** — rare for 18-year-old cloud provider
- **14-day unconditional money-back** — no questions asked, not pro-rated
- **99.95% uptime SLA** with free DDoS on all tiers
- **1000+ one-click apps** in marketplace
- **Live in 60 seconds** — fully automated provisioning
- **Dubai/UAE Free Zone company** — non-US, non-EU jurisdiction
- **122,000+ customers** — organic, multi-decade customer base
- **4.6/5 Trustpilot** — verified live

## 8-Check Pre-Flight (PASS)

| Check | VPS Card | Blog Review | Threshold | Result |
|---|---|---|---|---|
| Hetzner mentions | 0 | 0 | 0 | ✅ |
| Title length (decoded) | 60 | 60 | 30-60 | ✅ (at limit) |
| Description length | 144 | 152 | 70-155 | ✅ |
| H2 count (blog) | 3 | 10 | 8-10 | ✅ |
| FAQ Q&A | 5 | 5 | ≥5 | ✅ |
| RackNerd placements | 2 | 6 | ≥4 | ✅ |
| ZH characters | 0 | 0 | 0 (EN-only site) | ✅ |
| JSON-LD blocks | 3 | 3 | 3 (Breadcrumb + Review/Article + FAQPage) | ✅ |

## Tier Selection Rationale

- **Tier 0 (GSC):** today's vpstier.com GSC report shows 0 clicks / 183 imp / pos 49.0 (sparse). Per the 4-rule rejection framework, sparse sites trigger 0-changes verdict for technical SEO. Today's task is content production (not SEO tweak), so GSC sparse status doesn't block.
- **Tier 1 (briefing):** today's vpstier ⭐ was "Hetzner 正在做 LLM Inference 服务" (sliplane.io / HN 155p) — but **Hetzner the VPS provider is BANNED** (user's permanent preference 2026-05-25, reaffirmed 2026-06-03). Hetzner content is non-actionable for vpstier provider adds. No other Tier 1 ⭐⭐⭐ available today.
- **Tier 2 (provider gap scan):** 56 providers in providers.json before today, all 13 task-prompt-suggested candidates (A2 Hosting, Bluehost, FastComet, etc.) already covered. Live-probed 15+ fresh candidates (Verpex, SugarHosts, PacificRack, Qhoster, MonoVM, Hostens, RouterHosting/Cloudzy, VPS2day, HostZealot, HostGator, 10gbps.io, etc.) — picked **Cloudzy** for: (1) 18-year self-funded track record (unique among 2026 cloud providers), (2) uniformly modern infrastructure (DDR5 + EPYC + NVMe + 40 Gbps on every tier, no legacy hardware), (3) 13 datacenter locations + Tokyo coming soon, (4) accepts Monero (XMR) directly, (5) 122,000+ customers with 4.6/5 Trustpilot, (6) UAE Free Zone jurisdiction for non-US/non-EU buyers.
- **Tier 4 (orphan cards):** 14 orphan cards still exist in vps/index.astro (1984, atlantic-net, cherryservers, hawk-host, hivelocity, hostarmada, hostnamaste, linode, liquidweb, mochahost, netcup, rosehosting, scaleway, virmach). NOT fixed in this run (task is "add provider + write review", not orphan cleanup).

## Why Cloudzy (vs the other candidate options)

- **Cloudzy (formerly RouterHosting)** — live-probed routerhosting.com → 301-redirected to cloudzy.com. Verified rebranding via About page. Same operator, same founding date 2008, same Dubai address. Currently a major independent cloud provider with 122,000+ customers.
- **Cloudzy vs the 13 task-suggested candidates** — all 13 task candidates existed in providers.json OR had no verifiable data without network access. Cloudzy was a known gap with verifiable public data.
- **Cloudzy vs the 14 orphan-card candidates** — orphan cards (virmach, linode, liquidweb, etc.) have NO verified data, no blog reviews (except virmach which has only a 2026-07-25 blog review but missing the VPS card). Cloudzy has both VPS card data + blog review data + unique 18-year self-funded differentiator. Higher-fidelity candidate with cleaner public data.
- **Cloudzy vs Tier 1 Hetzner hot topic** — Hetzner LLM Inference is today's top vpstier ⭐ in the daily briefing. But Hetzner VPS provider is permanently BANNED (user directive 2026-05-25: "不写 Hetzner，以后也不写。换其他 VPS 商家。"). Tier 1 hot topic is non-actionable for provider adds. Cloudzy is the Tier 2 substitute that brings differentiated value without violating the Hetzner ban.

## Banned-Provider Audit

- Cloudzy VPS source: 0 Hetzner mentions (verified 2026-07-31)
- Cloudzy blog source: 0 Hetzner mentions (verified 2026-07-31)
- Cloudzy built dist (VPS card): 0 Hetzner mentions (verified 2026-07-31)
- Cloudzy built dist (blog review): 0 Hetzner mentions (verified 2026-07-31)
- vps/index.astro after edit: 0 Hetzner mentions (verified 2026-07-31)
- providers.json after edit: 0 Hetzner mentions (verified 2026-07-31)
- 5 pre-existing Hetzner mentions in `src/pages/blog/contabo-vps-review-2025.astro` are out-of-scope (published historical content, not new content from this run)

## Pitfalls Avoided

- Hetzner LLM Inference hot topic was NOT acted on (provider BANNED)
- Title at 60-char limit (acceptable, matches established pattern from serverpeacock/alphavps recent cards)
- Description kept under 155 chars by removing "pure NVMe" detail from VPS card (moved to "What Makes Cloudzy Different" section in body)
- All pricing/specs/datacenters sourced from live cloudzy.com fetch 2026-07-31, not pre-existing dist artifacts (per system policy: NEVER fabricate data)
- Promotional vs standard pricing distinguished clearly in both VPS card and blog review
- Monero (XMR) acceptance called out as differentiator in both card pros and blog body
- RouterHosting → Cloudzy rebrand mentioned in both card and blog for SEO (users may still search RouterHosting)

## Commit

Run report created. Source files + dist deployed live at https://vpstier.com/vps/cloudzy/ + https://vpstier.com/blog/cloudzy-vps-review-2026/.
