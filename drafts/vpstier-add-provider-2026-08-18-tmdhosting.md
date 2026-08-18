# vpstier Add-Provider-and-Review Run — 2026-08-18 (TMDHosting)

## Result: SUCCESS

**Provider added:** TMDHosting (managed cPanel/WHM VPS, est. 2007, AMD EPYC + NVMe SSD, 8+ global data centers)

### Why TMDHosting (no dead cards needed; gap-filling new provider)
- All 59 cards in `src/pages/vps/index.astro` already had matching `.astro` files (no dead-card cleanup needed this run).
- The task's suggested list (A2 Hosting, Bluehost, FastComet, ScalaHosting, ChemiCloud, DreamHost, GreenGeeks, SiteGround, HostPapa, InMotion Hosting, TurnKey Internet, ServerPeacock, ZAP VPS, etc.) was already covered.
- Picked TMDHosting: NOT yet on disk, $69/mo entry for fully managed cPanel/WHM VPS — a distinct specialization vs Liquid Web/Atlantic.Net (non-managed cheap) and Cloudways (managed multi-cloud, no cPanel). Established operator (since 2007). Rich verified public data on tmdhosting.com.

### Files created
- `src/pages/vps/tmdhosting.astro` (provider review page, 11,023 bytes)
- `src/pages/blog/tmdhosting-vps-review-2026.astro` (long-form review, 20,421 bytes, 1,883 body words)
- `drafts/tmdhosting-verified-data-2026-08-18.md` (evidence file, 4,093 bytes)

### Files modified
- `src/data/providers.json` (57 → 58 entries, new tmdhosting entry)
- `src/pages/vps/index.astro` (added TMD card at top of grid, +1,403 bytes)
- `src/pages/blog/index.astro` (added tmdhosting as first object in const posts array, +335 bytes)
- `drafts/state.json` (published 71 → 72, last_publish + last_run updated to 2026-08-18)

### Build
`NODE_OPTIONS=--max-old-space-size=768 npm run build` → **118 pages built** in 3.57s ✅
(alias-sitemap post-build step also ran → dist/sitemap.xml with 118 URLs)

### Deploy
`npx wrangler pages deploy dist --project-name=vpstier-com --commit-dirty=true` →
**121 files uploaded (6 already on edge)** in 1.82s ✅, deployment ID `8b787ac7`
Preview: https://8b787ac7.vpstier-com.pages.dev

### Pre-deploy drift check (CRITICAL)
Live sitemap: blog+vps = 104 unique slugs. Local dist: blog+vps = 108 unique slugs.
live_only = ∅ → 0 live pages would be deleted by deploy. ✅
Disk (60 vps / 49 blog) vs dist (60 vps / 48 blog) = only `index` differs (the blog index page, expected).

### Live URLs (verified HTTP 200 + correct title/desc/canonical/JSON-LD, 2026-08-18)
- https://vpstier.com/vps/tmdhosting/ (17,999b, title 54c, desc 126c, 12 JSON-LD types incl. Review/BreadcrumbList/FAQPage)
- https://vpstier.com/blog/tmdhosting-vps-review-2026/ (27,563b, title 54c, desc 126c, 11 JSON-LD types incl. Article/BreadcrumbList/FAQPage)
- Sitemap-0.xml: 118 URLs (was 116; +2 for the new vps + blog); both new URLs present ✅
- /vps/ index: TMDHosting card renders in the grid ✅
- /blog/ index: tmdhosting-vps-review-2026 slug renders in const posts array ✅

### Verified Data (2026-08-18, all from tmdhosting.com — no second-hand citations)
- **Provider:** TMDHosting, founded 2007 ("TMDHosting © est. 2007" footer + "15+ years" copy)
- **Specialization:** managed cPanel/WHM Linux VPS, also shared/WP/WooCommerce/dedicated
- **Hardware (consistent across every tier):** AMD EPYC CPU, NVMe SSD, KVM virtualization, 100% dedicated RAM, CloudLinux, Apache HTTP/2+HTTP/3+QUIC, Litespeed (16GB+), PHP 5.6-8.5, MariaDB 11.4
- **Pricing (Paid Monthly, USD):** $69 / $109 / $169 (Most Popular) / $279 / $499 / enterprise $1099-$2199
- **Datacenters (8+):** Chicago, London, Amsterdam, Singapore, Sydney, Tokyo, Johannesburg, Mumbai
- **SLA:** 99.99% uptime with credit; 24/7/365 human monitoring on every tier
- **Security (bundled):** Auto SSL, WAF, Monarx malware scanner, daily backups, Anti Virus
- **Affiliate:** TMDHosting does not appear on vpstier's partner list → use standing RackNerd fallback CTA per policy

### Metrics validation (script-measured against dist/)
- vps page: 17,699b → title 54/60 ✓, desc 126/155 ✓
- blog page: 27,248b → title 54/60 ✓, desc 126/155 ✓, 1883 body words (within site range 1300-2300) ✓, H2 x9 ✓, FAQ x5 ✓
- All internal `/vps/<slug>/` hrefs verified to resolve (Atlantic.Net, Cherry Servers, Cloudways, HostArmada, HostHatch, Linode, Liquid Web, OVHcloud, RackNerd, Vultr — all on disk)
- External links: 3 total — 2 official TMDHosting pages (vps-hosting.html + data-centers.html, both verified 200 OK) + 1 RackNerd affiliate CTA (expected 403 — exempt)

### Banned-provider self-audit: PASS
- 0 Hetzner mentions in any created/modified file ✅
- 0 Hetzner mentions in live rendered HTML (verified via grep on dist) ✅
- All CTAs → RackNerd affiliate (`https://my.racknerd.com/aff.php?aff=16299`) per standing policy

### Git workflow (two-commit pattern from skill)
- **Article commit:** `bd35ce67aace130c61c1126540b99d36c9b0424f` — 6 files, +512 / -1
- **State commit:** `d20aed8a0089142de38ece05ade2f328e115a103` — 1 file, +42 / -6
- **Push:** `origin main` succeeded (e0e6a91..d20aed8)
- Used `git add <specific files>` rather than `git add -A` — 13 untracked drafts from other crons left uncommitted
