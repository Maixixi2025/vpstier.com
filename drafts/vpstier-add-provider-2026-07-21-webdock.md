# vpstier Add-Provider-and-Review Run — 2026-07-21 (Webdock)

## Result: SUCCESS

**Provider added:** Webdock (Webdock ApS, VAT DK40630015; own DK-DC1 datacenter)
**Files created:**
- `src/pages/vps/webdock.astro` (provider card, 8,428B → built 15.9KB)
- `src/pages/blog/webdock-vps-review-2026.astro` (long-form review, 20,283B → built 28.4KB)
- `drafts/webdock-verified-data-2026-07-21.md` (verified-data reference, 4.4KB)
- `drafts/vpstier-add-provider-2026-07-21-webdock.md` (this file)

**Files modified:**
- `src/pages/vps/index.astro` (+1,414 chars, Webdock card inserted after Zappiehost)
- `src/data/providers.json` (+2,026 chars, Webdock entry surgically inserted; total 49 → 50 providers)
- `drafts/state.json` (appended new published entry; published 53 → 54)

**Build:** `NODE_OPTIONS=--max-old-space-size=400 npx astro build --silent` → 124 files built in ~3.5s ✅
**Deploy:** `npx wrangler pages deploy dist --project-name=vpstier-com --branch=main --commit-dirty=true` → 117 files uploaded (6 already uploaded), 2.63s, deployment ID `0abfafb2` ✅

**Live URLs (verified HTTP 200 + correct content):**
- https://vpstier.com/vps/webdock/ (15,943B, title "Webdock VPS Review 2026: Own Denmark DC from €2.15/mo")
- https://vpstier.com/blog/webdock-vps-review-2026/ (28,446B, title "Webdock VPS Review 2026: Own Denmark DC + GDPR from €2.15/mo")
- https://vpstier.com/vps/ (68,117B, Webdock card present in grid after Zappiehost)
- Preview: https://0abfafb2.vpstier-com.pages.dev/

## Verified Data (live fetch 2026-07-21, webdock.io)

### VPS Cloud Hosting
| Tier | CPU | RAM | NVMe | Transfer | Price |
|------|-----|-----|------|----------|-------|
| Essential | Xeon Platinum | 2 GB | 15 GB | 1 TB | €2.15/mo |
| Advanced (most popular) | Epyc Milan | 2 GB | 15 GB | 1 TB | €7.10/mo |
| Pro | Epyc Milan | 10 GB | 40 GB | 7 TB | €19.60/mo |

### WordPress VPS Hosting
| Tier | CPU threads | Memory | NVMe | Price |
|------|-------------|--------|------|-------|
| Starter WP | 2 | 4 GB | 15 GB | €7/mo |
| WP Business | 4 | 6 GB | 30 GB | €13/mo |
| WP Pro | 6 | 16 GB | 50 GB | €24.20/mo |

### Identity
- **Founded:** 2012 (12+ years operating)
- **Founder:** Arni Johannesson
- **HQ:** Tværvejen 9A, 5580 Nørre Aaby, Funen, Denmark
- **VAT ID:** DK40630015
- **Operator:** Webdock ApS (Danish ApS)
- **Own datacenter launched:** 2024 (DK-DC1, Nørre Aaby)

### Stack
- Intel Xeon Platinum (Essential) + AMD Epyc Milan / better (Advanced + Pro)
- NVMe SSD on every tier (15 GB minimum)
- 1 Gbit/s network port on every tier
- Free DDoS, free SSL, free backup snapshots, free control panel, transactional emails, email forwarding on every tier
- Custom VPS profile builder for non-standard sizing

## 8-Check Pre-Flight (PASS)

1. ✅ Hetzner regex count: 0/0 (card/blog) — 0 mentions across full src/ (verified 2026-07-21)
2. ✅ Title length: 53 chars (card) / 60 chars (blog)
3. ✅ Description length: 148 chars (card) / 148 chars (blog)
4. ✅ ZH chars: 0/0
5. ✅ /zh/ paths: 0/0
6. ✅ RackNerd placements: 2 (card) + 6 (blog)
7. ✅ H2 count: 8 (within 8-10)
8. ✅ FAQ count: 5 in source → 10 in built page (5 page-specific + 5 BaseLayout global)

## Tier Selection Rationale

- **Tier 0 (GSC):** failed today (HTTP 403 from 5570fe2cffa6 — established pattern 2026-07-19 + 2026-07-20)
- **Tier 1 (briefing):** all VPS ⭐ items already covered
  - KVM escape vulnerability → outline at `outline-2026-07-16-januscape-kvm-escape-vps-security-2026.md` (`outline_pending_publish`)
  - Luxvps 7-31 closes specials → outline at `outline-2026-07-20-luxvps-special-offer-shutdown-alternatives-2026.md` (`outline_pending_publish`)
  - HostNamaste → already published 2026-07-13
- **Tier 2 (provider gap scan):** 49 providers in providers.json, none Webdock; Tier 4 orphans (virmach, hostdare) were already filtered out (skip per multi-orphan pre-filter rule). **Webdock is a clean Tier 2 fresh add** — EU-only + own 2024 datacenter + GDPR-native + Xeon/Epyc + free DDoS tier.
- **Tier 4 (orphan cards):** no safe repick (virmach already-complete 20KB review, hostdare locked by outline)

## Why Webdock

- **Own DK-DC1 datacenter built 2024** — uncommon for a 12-year-old bootstrapped company; gives full infrastructure control (physical security, power, cooling, hardware refresh).
- **EU-only jurisdiction** — 100% GDPR alignment, Danish company (Webdock ApS, VAT DK40630015). EU-only buyers avoid US CLOUD Act exposure.
- **Free DDoS + SSL + backups on every tier** — uncommon at budget tier; competitors charge €5-15/mo each as add-ons.
- **Xeon Platinum + Epyc Milan CPUs** — datacenter-grade silicon, not consumer hardware.
- **Custom VPS profile builder** — flexible sizing for non-standard workloads.
- **Founded 2012, 12+ years operating** — well past early-stage risk.
- **Public referral / affiliate program** — Webdock does have one (https://webdock.io/become-an-affiliate), but the site uses RackNerd fallback per established pattern (consistent with the rest of vpstier).

## Pitfalls Avoided

- ServerPeacock (task prompt suggestion) — DNS doesn't resolve, domain not in use
- All other task prompt suggestions (A2 Hosting, Bluehost, FastComet, ScalaHosting, ChemiCloud, DreamHost, GreenGeeks, SiteGround, HostPapa, InMotion Hosting, TurnKey Internet, ZAP-Hosting) — all already in providers.json
- ServaRica.com — actually WordPress hosting, not VPS, only one $ price point
- VPSnet.com — homepage references "AI console" / "MCP" but /vps /pricing return 404
- Hosthatch.com — Cloudflare 522 origin unreachable at probe time
- AlphaVPS.com — returns 403 Forbidden
- LITESERVER, SparkVPS — domain-for-sale or DNS failures

## Commit

Commit pending — to be created after this report.