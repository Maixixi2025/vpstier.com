# Run Record: vpstier add-provider-and-review (Cherry Servers) — 2026-08-04

## Decision
- **Hot topic ⭐⭐⭐ Hetzner LLM Inference**: BANNED — pivoted to substitute angle.
- **Hot topic ⭐⭐ Data Center Politicalization**: Already used by daily-outline cron at 09:45 today.
- **Brief candidate list**: 13/13 stale (all already covered).
- **Drift A**: 10 candidates waiting (providers.json entry, no vps page).
- **Pick**: Cherry Servers — 25-year Lithuanian operator, 6 regions (4 EU + US + SG), ISO 27001 + SOC 2 + PCI DSS, dual cloud + bare-metal product line, $3.51/mo entry.

## Why Cherry Servers
- 25-year European operating history is a strong 2026 differentiator (most modern providers are 5-15 years old).
- ISO 27001 + SOC 2 + PCI DSS triple certification covers all 6 regions — appeals to regulated SMB buyers (finance, healthcare, public sector).
- Dual cloud + bare-metal product line is rare among SMB-tier European providers.
- US + APAC presence extends coverage outside EU without sacrificing EU contractural entity.
- Cherry card already existed in vps/index.astro from a prior (incomplete) run, but no vps/cherryservers.astro page existed and no blog review existed.

## Files Created
- `src/pages/vps/cherryservers.astro` (12264 bytes) — VPS profile page (racknerd template, Cloudzy-style structured-data)
- `src/pages/blog/cherryservers-vps-review-2026.astro` (26319 bytes) — Long-form blog review

## Files Modified
- `src/pages/vps/index.astro` — Cleaned up a duplicate Cherry card (a prior run had inserted a purple-500 card after Cloudzy, outside the grid section)
- `src/pages/blog/index.astro` — Inserted Cherry Servers blog post at top of array (newest-first)
- `src/data/providers.json` — Updated Cherry Servers entry with live-verified facts: 6 datacenter regions (NL/DE/LT/SE/US/SG), ISO 27001 + SOC 2 + PCI DSS, $3.51/mo entry, 30k+ deployments/year, 8-min average provisioning

## Build & Deploy
- `npm run build` → 100 pages built in 3.19s, exit 0
- `npx --no-install wrangler pages deploy dist --project-name=vpstier-com --commit-dirty=true` → deployment_id `1b74e698`, uploaded 5 new files (103 already uploaded), 1.97s
- Preview URL: https://1b74e698.vpstier-com.pages.dev
- Production URL: https://vpstier.com (verified after 10s CF propagation)

## Live Verification (post-deploy)
| URL | Status | Title |
|---|---|---|
| https://1b74e698.vpstier-com.pages.dev/vps/cherryservers/ | ✅ | Cherry Servers Review 2026: 25yr EU Cloud from $3.51/mo |
| https://1b74e698.vpstier-com.pages.dev/blog/cherryservers-vps-review-2026/ | ✅ | Cherry Servers Review 2026: 25yr EU Bare-Metal + ISO 27001 |
| https://1b74e698.vpstier-com.pages.dev/vps/ | ✅ | VPS Hosting Reviews - VPSTier.com (Cherry card visible) |
| https://1b74e698.vpstier-com.pages.dev/blog/ | ✅ | Blog (Cherry post at top) |
| https://vpstier.com/vps/cherryservers/ | ✅ | Cherry Servers Review 2026: 25yr EU Cloud from $3.51/mo |
| https://vpstier.com/blog/cherryservers-vps-review-2026/ | ✅ | Cherry Servers Review 2026: 25yr EU Bare-Metal + ISO 27001 |

## SEO Compliance
- VPS page title: 55 chars (≤60 ✅)
- VPS page description: 154 chars (≤155 ✅)
- Blog review title: 58 chars (≤60 ✅)
- Blog review description: 155 chars (≤155 ✅)
- BaseLayout does NOT auto-append "| VPSTier" (verified — source title length = final title length)
- 3 JSON-LD blocks per page: BreadcrumbList + Review/Article + FAQPage
- Affiliate link: https://my.racknerd.com/aff.php?aff=16299 (per task spec)

## Banned-Provider Audit (Hetzner)
| File | Hetzner mentions |
|---|---|
| `src/pages/vps/cherryservers.astro` | 0 ✅ |
| `src/pages/blog/cherryservers-vps-review-2026.astro` | 0 ✅ (1 mention scrubbed during draft) |
| `src/pages/vps/index.astro` | 0 ✅ |
| `src/pages/blog/index.astro` | 0 ✅ |
| `src/data/providers.json` | 0 ✅ |
| Built dist files (all 3) | 0 ✅ |
| Live URLs (all 6 verified) | 0 ✅ |

## state.json Updates
- Added 1 entry to `state.published[]` for `cherryservers-vps-review-2026` with type `add-provider-and-review`
- `published_count`: 63 → 64
- `last_publish`: 2026-08-04
- `publish_notes` appended (string field — handled per CANONICAL #16 schema drift recipe)

## Single-Provider Review Streak
- Streak before today: 20 consecutive single-provider reviews
- Today: 21 (Cherry Servers add-provider-and-review)
- Streak ≥ 10 threshold continues — comparison format still pending

## Follow-ups / Next Cron
- Drift A remaining: atlantic-net, hivelocity, hostnamaste, linode, liquidweb, mochahost, netcup, rosehosting, scaleway, virmach (10 candidates)
- Daily-outline cron tomorrow should pivot to a comparison format (≥ 10 streak)
- Cherry Servers data may benefit from a future re-verification once they add new regions or refresh pricing
