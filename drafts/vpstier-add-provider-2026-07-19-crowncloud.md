# vpstier Add-Provider-and-Review Run — 2026-07-19 (CrownCloud)

## Result: SUCCESS

**Provider added:** CrownCloud (KVM VPS, LA + Frankfurt, in-house CrownPanel)
**Files created:**
- `src/pages/vps/crowncloud.astro` (provider card page, 7,978B)
- `src/pages/blog/crowncloud-vps-review-2026.astro` (long-form review, ~26,300B after edits)
- `drafts/crowncloud-verified-data-2026-07-19.md` (verified-data reference)
- `drafts/vpstier-add-provider-2026-07-19-crowncloud.md` (this file)

**Files modified:**
- `src/pages/vps/index.astro` (+18 lines, CrownCloud card inserted after LightNode)
- `src/data/providers.json` (+29 lines, CrownCloud entry inserted at end via surgical recipe)
- `drafts/state.json` (appended new published entry; current_index 48 → 49; published 51 → 52)

**Build:** `NODE_OPTIONS=--max-old-space-size=300 npx astro build --silent` → 111 pages built in 1.27s ✅
**Deploy:** `npx wrangler pages deploy dist --project-name=vpstier-com --branch=main --commit-dirty=true` → 5 files uploaded, deployment ID `be4528ba` ✅

**Live URLs (verified HTTP 200 + correct content):**
- https://vpstier.com/vps/crowncloud/ (15,617B, title "CrownCloud VPS Review 2026: KVM from $5/mo + Ryzen 9 9950X")
- https://vpstier.com/blog/crowncloud-vps-review-2026/ (34,795B, title "CrownCloud VPS Review 2026: KVM from $5/mo + Ryzen 9950X")
- https://vpstier.com/vps/ (65,580B, CrownCloud card present in grid)
- Preview: https://be4528ba.vpstier-com.pages.dev/vps/crowncloud/ + /blog/crowncloud-vps-review-2026/

## Verified Data (live fetch 2026-07-19, crowncloud.net/kvm-vps)

| Tier | CPU | Storage | Starting Price |
|------|-----|---------|----------------|
| Classic KVM | Standard KVM | HDD-based | $5/mo |
| SSD KVM | Premium SSD | SSD | $5/mo |
| NVMe KVM (improved) | Premium NVMe | Gen4 NVMe | $7/mo |
| Intel Core Ultra 9 NVMe KVM | Intel Core Ultra 9 285 (Arrow Lake) | High-perf NVMe | $7/mo |
| Storage KVM | KVM high-storage | High-storage | $10/mo |
| AMD Ryzen SSD KVM | AMD Ryzen 9 7950X (Zen 4) | Premium SSD | $10/mo |
| AMD Ryzen 9 9950X SSD KVM | AMD Ryzen 9 9950X (Zen 5) | Premium SSD | $15/mo |

**Datacenters:** Los Angeles, CA + Frankfurt, Germany
**Control panel:** In-house CrownPanel (1-click apps, custom ISO, free snapshot slot, 2FA, SSH keys, API)
**Affiliate:** No public program → uses RackNerd fallback affiliate `https://my.racknerd.com/aff.php?aff=16299`

## 8-Check Pre-Flight (PASS)

1. ✅ Hetzner regex count: 0 (no banned merchant mentions)
2. ✅ Title length: 56 chars (cap 60)
3. ✅ Description length: 137 chars (cap 155)
4. ✅ ZH chars: 0 (EN-only)
5. ✅ /zh/ paths: 0 (no ZH references)
6. ✅ RackNerd placements: 10 (min 6)
7. ✅ H2 count: 8 (cap 8-10)
8. ✅ FAQ count (JSON-LD): 5 (cap 3-5)

**6-place title sync:** BaseLayout title = Article headline = H1 body = "CrownCloud VPS Review 2026: KVM from $5/mo + Ryzen 9950X" (all match)

**Live JSON-LD:** 5 blocks parsed cleanly: WebSite, FAQPage (page-specific, 5 Q), BreadcrumbList, Article, FAQPage (BaseLayout global, 5 Q)

**Table audit:**
- Pricing table: 8 rows × 5 cells (header + 7 KVM tiers) ✅
- Side-by-side table: 5 rows × 6 cells (header + CrownCloud entry, Ryzen 9 9950X, RackNerd, Vultr) ✅

**Banned-provider audit (full src/ walk):** 0 mentions across all 80 .astro files ✅

## Tier Selection Rationale

- **Tier 0 (GSC):** failed today (HTTP 403); most recent successful report 2026-07-17 showed vpstier 7d: 0 click / 431 imp / avg rank 63.1. All top queries were branded reviews (a2 hosting, ionos, 1984.is, agent zero). Zero comparison-intent keywords meeting ≥3 imp + rank<60 bar. **Tier 0 has no candidate.**
- **Tier 1 (briefing):** all VPS ⭐ items already covered
  - NY data center moratorium (⭐⭐⭐) → outline at `outline-2026-07-15-ny-data-center-moratorium-2026-vps-buyers.md` (`outline_pending_publish`)
  - Kainode Singapore (⭐⭐) → published 2026-07-16
  - AWS outage (⭐⭐⭐) → published as `aws-us-east-1-outage-2026` (2026-06-06)
  - Garnix shutdown (⭐⭐) → published as `2026-shutdown-cloud-services-vps-migration` (2026-06-06)
- **Tier 2 (provider gap scan):** 47 providers in providers.json (last 5 picks all provider reviews: bandwagon 07-18, lightnode 07-17, kainode 07-16, aliyun 07-14, inmotion 07-07). Editorial variety warrants another provider — picked CrownCloud (long-running LET staple, modern CPU tier ladder)
- **Tier 4 (orphan cards):** hostdare locked by pending outline (do-not-touch); virmach already-complete review card (20KB / 7+ H2s). **No safe Tier 4 repick.**

## Why CrownCloud

- **Modern CPU tier ladder** — AMD Ryzen 9 9950X (Zen 5) at $15/mo, Intel Core Ultra 9 285 (Arrow Lake) at $7/mo. Most budget VPS providers still default to older Intel Xeon E5 / E3 hardware.
- **In-house CrownPanel** — not SolusVM or Virtualizor. Avoids third-party licensing overhead.
- **LA + Frankfurt DCs** — covers US + EU routing.
- **Monthly billing** — no annual lock-in required.
- **7 KVM tiers from $5 to $15/mo** — clearest CPU ladder in the budget tier.

## Pitfalls Avoided

- ServerPeacock (task prompt suggestion) — DNS doesn't resolve, domain not in use
- A2 Hosting, Bluehost, ScalaHosting, DreamHost, GreenGeeks, SiteGround, HostPapa, InMotion Hosting, TurnKey Internet, ZAP-Hosting — all already in providers.json (covered in prior runs)

## Verification Commands Run

```python
import urllib.request, re, json
# Live fetch + JSON-LD parse + table audit + banned regex audit
# All passed.
```