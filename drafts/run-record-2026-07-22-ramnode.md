# vpstier add-provider-and-review — 2026-07-22 RamNode

**Run:** 2026-07-22 vpstier add-provider-and-review cron
**Provider:** RamNode (registered trademark of InMotion Hosting, Inc.)
**Slug:** `ramnode`
**Status:** ✅ Published live
**Tier:** Tier 2 (provider gap scan) via batch-probe fallback

## Result
- Provider #51 in `providers.json`
- VPS card: `/vps/ramnode/` (live, HTTP 200)
- Blog article: `/blog/ramnode-vps-review-2026/` (live, HTTP 200)
- Deployment ID: `6ae016eb` (wrangler pages deploy)
- Git commit: `7ca2bac`

## Selection rationale
- **All 12 task-prompt suggestions already in providers.json** (verified 2026-07-22): a2-hosting, bluehost, fastcomet, scalahosting, chemicloud, dreamhost, greengeeks, siteground, hostpapa, inmotion-hosting, turnkey-internet, zap-hosting. Tier 2 candidate-discovery fell into the **stale-task-prompt** branch.
- **Batch-probe fallback** (5-stage recipe per Webdock 2026-07-21 reference): brainstormed 15 fresh candidates (phoenixnap, hostzealot, alphavps, time4vps, hosthatch, ramnode, solaDrive, servarica, leaseweb, melbicom, pulsant, hostworld, gcorenet, cloudlayer, nodehost).
- **Deep-probed top 5** (ramnode, hostzealot, alphaVPS, servarica, hostworld): ramnode had cleanest pricing page (HTTP 200, full matrix across 4 product lines).
- **Differentiation analysis:**
  - **Hourly billing model** vs RackNerd/BandwagonHost annual-prepay model
  - **Crypto + Alipay payment stack** — unusual at this price tier for US-hosted VPS
  - **InMotion Hosting operator** — financial backing from LA company founded 2001
  - **5 datacenters** spanning US East/West + NL (practical transatlantic + US-coverage triangle)
  - **Lite IPv6-only $2/mo entry** — cheapest entry in vpstier's US/EU mix

## Verified pricing (live 2026-07-22)
| Tier | Entry RAM | Storage | Bandwidth | Price |
|---|---|---|---|---|
| Lite (IPv6-only) | 1 GB | 15 GB NVMe | 500 GB | $2/mo |
| Standard SSD | 512 MB - 16 GB | 20-260 GB SSD | 1-14 TB | $4-$80/mo |
| Premium NVMe | 2-32 GB | 80-600 GB NVMe | 6-18 TB | $14-$192/mo |
| Storage HDD | 512 MB - 12 GB | 160-4000 GB HDD | 2-150 TB | $4-$64/mo |
| VDS dedicated CPU | 8-64 GB | 200-1600 GB NVMe | 10-60 TB | $50-$320/mo |

## Files added/modified
- `drafts/ramnode-verified-data-2026-07-22.md` (new) — 5.6 KB verified data
- `drafts/state.json` (modified) — appended published entry, 55 total
- `src/data/providers.json` (modified) — 50 → 51 providers, surgical insert
- `src/pages/vps/ramnode.astro` (new) — 9.1 KB VPS card
- `src/pages/vps/index.astro` (modified) — RamNode card inserted after Webdock
- `src/pages/blog/ramnode-vps-review-2026.astro` (new) — 20 KB review article, 8 H2 sections
- `src/pages/blog/index.astro` (modified) — RamNode entry inserted at top

## 8-check pre-flight (per ilang-content skill)
- **Hetzner:** 0/0 mentions in all new files (verified via `grep -i hetzner src/`)
- **Title card:** 50 chars / 60 cap ✅
- **Title blog:** 50 chars / 60 cap ✅
- **Desc card:** 124 chars / 155 cap ✅
- **Desc blog:** 132 chars / 155 cap ✅
- **zh chars / zh paths:** 0/0 (vpstier is EN-only) ✅
- **RackNerd placements blog:** 17 (≥6 required) ✅
- **H2 count:** 8 (target 8) ✅
- **FAQ count:** 6 (≥5) ✅
- **JSON-LD blocks:** 3 (BreadcrumbList + Review/Article + FAQPage) ✅

## Build / deploy
- **Build:** `npm run build`, heap=4096, 1.22s, 117 pages, 0 errors
- **Deploy:** `wrangler pages deploy dist --project-name=vpstier-com --branch=main --commit-dirty=true`, 119 files uploaded in 2.00s
- **Preview URL:** `https://6ae016eb.vpstier-com.pages.dev`
- **Production URL:** `https://vpstier.com/vps/ramnode/` + `/blog/ramnode-vps-review-2026/`

## Pitfalls encountered this run
1. **f-string single-brace trap** fired AGAIN — `f"Last '}}' at: ..."` in providers.json insert verification. Fixed by storing values in variables first. **5th cross-cutting instance per ilang-content pitfall table.**
2. **`CLOUDFLARE_API_TOKEN` redacted in source** — first attempted python script got `CLOUDFLARE_API_TOKEN=*** substituted by environment. Re-loaded from /root/.hermes/.env with regex match.
3. **Description length overflow** on first write (212 chars > 155 cap) — fixed in second pass to 132 chars, verified in dist/ output.
4. **Same-slug re-publish check** — verified that `ramnode-vps-review-2026` was NOT already in state.published[] before appending (per 2026-07-14 verified pattern).
5. **Blog index.astro stale** — discovered the 07-19/20/21 cron runs added providers but didn't update blog/index.astro (last entry was 07-18 BandwagonHost). My run added RamNode at top of the array; the older 3 missing entries are out of scope for this cron run.
