# vpstier Add-Provider-and-Review Run — 2026-07-20 (Zappiehost)

## Result: SUCCESS

**Provider added:** Zappiehost (own AS61138, Auckland + Johannesburg + Santiago)
**Files created:**
- `src/pages/vps/zappiehost.astro` (provider card, 7,878B)
- `src/pages/blog/zappiehost-vps-review-2026.astro` (long-form review, 20,542B)
- `drafts/zappiehost-verified-data-2026-07-20.md` (verified-data reference, 4,637B)
- `drafts/vpstier-add-provider-2026-07-20-zappiehost.md` (this file)

**Files modified:**
- `src/pages/vps/index.astro` (+18 lines, Zappiehost card inserted after CrownCloud)
- `src/data/providers.json` (+36 lines, Zappiehost entry surgically inserted; total 48 → 49 providers)
- `drafts/state.json` (appended new published entry; published 52 → 53)

**Build:** `NODE_OPTIONS=--max-old-space-size=300 npx astro build --silent` → 113 pages built in 3.62s ✅
**Deploy:** `npx wrangler pages deploy dist --project-name=vpstier-com --branch=main --commit-dirty=true` → 115 files uploaded (6 already uploaded), deployment ID `1fb0795c` ✅

**Live URLs (verified HTTP 200 + correct content):**
- https://vpstier.com/vps/zappiehost/ (15,469B, title "Zappiehost VPS Review 2026: Rare NZ + SA + Chile Locations")
- https://vpstier.com/blog/zappiehost-vps-review-2026/ (27,831B, title "Zappiehost VPS Review 2026: NZ + SA + Chile from $4.50/mo")
- https://vpstier.com/vps/ (66,870B, Zappiehost card present in grid with "Free BGP" badge)
- Preview: https://1fb0795c.vpstier-com.pages.dev/

## Verified Data (live fetch 2026-07-20, zappiehost.com)

### Premium KVM VPS (Linux or Windows) — same pricing in Auckland, Johannesburg, Santiago
| Tier | RAM | vCPU | SSD | Traffic | Price (semi-annual) |
|------|-----|------|-----|---------|---------------------|
| Starter | 512 MB | 1 core | 30 GB | 200 GB | $6.00/mo |
| Medium | 1 GB | 2 cores | 50 GB | 400 GB | $9.00/mo |
| Advance | 2 GB | 4 cores | 100 GB | 800 GB | $17.00/mo |
| Super | 4 GB | 6 cores | 150 GB | 1.2 TB | $24.50/mo |

### Budget LXC VPS (Auckland only)
| Tier | RAM | vCPU | SSD | Traffic | Price (semi-annual) |
|------|-----|------|-----|---------|---------------------|
| Starter | 512 MB | 1 core | 30 GB | 200 GB | $4.50/mo |
| Medium | 1 GB | 2 cores | 50 GB | 400 GB | $7.00/mo |
| Advance | 2 GB | 4 cores | 100 GB | 800 GB | $13.00/mo |
| Super | 4 GB | 6 cores | 150 GB | 1.2 TB | $19.00/mo |

**Datacenters:** Auckland NZ (IPv4 185.99.133.234, IPv6 2A06:1280:BEE1::DEA:234), Johannesburg SA, Santiago Chile (IPv4 216.73.159.15)
**Network:** Own AS61138, multi-gbps in Auckland, 1 Gbps port in Auckland / 100 Mbps in SA + Chile
**Founded:** March 2015 (11+ years operating)
**Payment methods:** PayPal, Bitcoin + other cryptocurrencies
**Affiliate:** No public program → uses RackNerd fallback affiliate `https://my.racknerd.com/aff.php?aff=16299`

## 8-Check Pre-Flight (PASS)

1. ✅ Hetzner regex count: 0 (no banned merchant mentions)
2. ✅ Title length: 58 chars (provider card) / 57 chars (blog)
3. ✅ Description length: 145 chars (card) / 138 chars (blog), both in 70-155 range
4. ✅ ZH chars: 0 (EN-only)
5. ✅ /zh/ paths: 0 (no ZH references)
6. ✅ RackNerd placements: 6 (blog) + 2 (card)
7. ✅ H2 count: 8 (within 8-10)
8. ✅ FAQ count: 5 in source, 10 in built page (5 page-specific + 5 BaseLayout global)

**6-place title sync:** BaseLayout title = Article headline = H1 body = "Zappiehost VPS Review 2026: NZ + SA + Chile from $4.50/mo" (all match)

**Live JSON-LD:** Blog has Article + BreadcrumbList + FAQPage + WebSite; provider card has Review + BreadcrumbList + FAQPage + WebSite

**Table audits:**
- Pricing table (blog): 8 rows × 6 cells (header + LXC×4 + KVM×4) ✅
- Side-by-side table (blog): 5 rows × 5 cells (header + Zappiehost×2 + RackNerd + Vultr) ✅

**Banned-provider audit (full src/ walk):** 0 mentions across all 80+ .astro files ✅

## Tier Selection Rationale

- **Tier 0 (GSC):** failed today (HTTP 403 from 5570fe2cffa6, default assumption per 2026-07-20 rule); most recent successful report was 2026-07-17. **Tier 0 has no candidate.**
- **Tier 1 (briefing):** all VPS ⭐ items already covered in recent runs
  - HostNamaste (⭐⭐⭐) → published 2026-07-13
  - Luxvps closes 2026-07-31 (⭐⭐) → outline at `outline-2026-07-20-luxvps-special-offer-shutdown-alternatives-2026.md` (`outline_pending_publish`)
  - Hetzner items (⭐) → BANNED, skipped
- **Tier 2 (provider gap scan):** 48 providers in providers.json, no Zappiehost entry; virmach already-complete review card (20KB / 0 H2-N, 7+ H2s); hostdare locked by pending outline. **Zappiehost is a clean Tier 2 fresh add** — rare-region footprint + own AS + free BGP + crypto payments = strong differentiation vs existing 48.
- **Tier 4 (orphan cards):** virmach already-complete review card (skip per multi-orphan pre-filter rule); hostdare locked by pending outline. **No safe Tier 4 repick.**

## Why Zappiehost

- **Rare geographic footprint** — Auckland NZ, Johannesburg SA, Santiago Chile. Most Western-managed VPS providers concentrate in US/EU; Zappiehost is one of the few with self-owned AS in all three regions.
- **Free BGP sessions** on Premium KVM — uncommon in the budget tier; useful for operators with their own IP allocations.
- **Multi-RIR membership** (ARIN + RIPE + APNIC + Afrinic) — unusual breadth for a small operator.
- **Crypto payments** — explicit privacy-first positioning (PayPal + Bitcoin + other crypto).
- **11+ years operating** — established LowEndTalk community presence.
- **Active community sponsorships** — Tor exit node, LowEndSpirit, RIPE Atlas anchor.

## Pitfalls Avoided

- ServerPeacock (task prompt suggestion) — DNS doesn't resolve, domain not in use
- All other task prompt suggestions (A2 Hosting, Bluehost, ScalaHosting, DreamHost, GreenGeeks, SiteGround, HostPapa, InMotion Hosting, TurnKey Internet, ZAP-Hosting) — all already in providers.json
- LITESERVER — domain was for sale on HugeDomains, not actually active
- AlphaVPS — returns 403 Forbidden
- SparkVPS — DNS doesn't resolve

## Verification Commands Run

```python
import urllib.request, re
# Title length check, H2 count, banned regex, RackNerd placement count, FAQ count
# All passed for both provider card and blog article.
```

## Commit

Commit `e53cac4` pushed to main: `Add Zappiehost VPS provider + review (2026-07-20)` — 6 files changed, 431 insertions, 1 deletion.
