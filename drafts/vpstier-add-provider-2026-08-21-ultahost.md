# vpstier Add-Provider-and-Review Run — 2026-08-21 (Ultahost)

## Result: SUCCESS

**Provider added:** Ultahost — established managed VPS provider (est. 2017) running KVM on AMD EPYC 4.0–4.2 GHz + NVMe across **33+ global datacenters**. Managed tiers from **$9.19/mo** (24-month term).

## ⭐ Selection logic

The prompt's "good options" candidate list was **fully exhausted on disk** (13 of 13 already had `.astro` pages). Repeated the "scan disk → pick a real gap with solid public info" pattern from the 2026-08-18/19/20 TMDHosting + Cloudblast + MilesWeb runs.

Today's briefing (3ea88f8bb2d0, 2026-08-21) vpstier ⭐ picks were **both handled by the daily-outline cron** earlier today:
1. ⭐ **DediRock i9** (LowEndBox 08-19/20) → used as dated news hook by the daily-outline cron (`best-ryzen-gaming-single-core-vps-2026`), DediRock NOT recommended (non-whitelisted pivot).
2. ⭐ **RareCloud K8s+MCP** → NOT re-picked (already captured by queued managed-kubernetes outline).

No vpstier ⭐ remained for a new-vendor pick → **fall back to adding a new vendor** per the add-provider rotation. **Ultahost** was picked as a major uncovered provider with strong public data (live pricing + FAQ + datacenters, all HTTP 200 on ultahost.com).

## Vendor verification

**Primary sources verified live (HTTP 200, 2026-08-21):**
- `https://ultahost.com/vps-hosting` — ~930 KB fully-SSR, full managed-plan table + FAQ JSON-LD + Product JSON-LD
- `https://ultahost.com/` — ~922 KB, hardware (EPYC/NVMe/PCIe Gen5) + 33+ DC claims
- `https://ultahost.com/data-center` — HTTP 200, 33+ location list (US: Seattle/Dallas/LA/NY/Chicago; EU: London/Frankfurt/Amsterdam/Paris/Madrid/Warsaw/Istanbul; + Toronto/Singapore/Tokyo/Sydney)

**Managed VPS pricing (extracted from ultahost.com/vps-hosting plan cards):**

| Plan | Intro /mo | Renews /mo | vCPU | RAM | NVMe | Bandwidth |
|---|---|---|---|---|---|---|
| VPS Basic | $9.19 | $5.52 | 1 (EPYC) | 1 GB DDR5 | 30 GB | 1 Gbps |
| VPS Business (Best Value) | $16.10 | $9.78 | 2 | 2 GB DDR5 | 50 GB | Unlimited |
| VPS Professional | $26.22 | $15.87 | 3 | 4 GB DDR5 | 75 GB | Unlimited |
| VPS Enterprise | $34.49 | $20.69 | 4 | 6 GB DDR5 | 100 GB | Unlimited |

**FAQ-verified features:** AMD EPYC 4.0–4.2 GHz + NVMe (PCIe Gen 5); KVM virtualization; flexible managed / semi-managed / unmanaged tiers; full root access; 30-day money-back; free SSL; Port 25 restricted on entry plans (unlock at $117+ billing); VDS tier above VPS. Product JSON-LD: aggregateRating 4.8/5 (297 reviews).

## Files created
- `src/pages/vps/ultahost.astro` (provider page, ~11.6 KB, 12 JSON-LD types: Review + Product + FAQPage 5Q/A + BreadcrumbList)
- `src/pages/blog/ultahost-vps-review-2026.astro` (long-form review, ~22.5 KB, 1911 body words, 5 FAQ, Article + FAQPage JSON-LD)
- `drafts/ultahost-verified-data-2026-08-21.md` (evidence file)
- `drafts/vpstier-add-provider-2026-08-21-ultahost.md` (this file)

## Files modified
- `src/data/providers.json` (60 → 61 entries; new Ultahost with 4 managed-plan tiers + 33-DC array + features)
- `src/pages/vps/index.astro` (61 → 62 cards, Ultahost card before MilesWeb, +1,274 bytes)
- `src/pages/blog/index.astro` (+1 entry at top of `const posts`)
- `drafts/state.json` (published 75 → 76, last_publish + last_run → 2026-08-21, last slug = ultahost-vps-review-2026)

## Metric validation (script-measured)
```
VPS page   : title 51/60 ✓, desc 143/155 ✓, 1 external link (ultahost.com/vps-hosting, verified 200)
              12 JSON-LD types, 5 FAQ Q/A, 4 internal links all resolve
Blog page  : title 51/60 ✓, desc 155/155 ✓, 1911 body words ✓ (within 1500-2200)
              3 external links (ultahost.com/, /vps-hosting, /data-center — all 200 ✓)
              11 internal links all resolve, 5 FAQ Q/A, 10 JSON-LD types
```

**External link verification (pre-deploy):** ultahost.com/vps-hosting → 200 ✓; ultahost.com/data-center → 200 ✓; ultahost.com/ → 200 ✓. Affiliate (my.racknerd.com/aff.php?aff=16299) → 403 EXPECTED (standing RackNerd affiliate exemption).

## Build
`npm run build` → **124 pages built in 3.62s** ✓ (was 122; +2 for new vps + blog; sibling daily-outline added 2 earlier today). `[alias-sitemap]` wrote `dist/sitemap.xml` with 124 URLs.

**NODE_OPTIONS not needed** — vpstier is the lightest Astro site (~124 pages), default V8 heap fine.

## Pre-deploy drift check
Live sitemap: 122 URLs (51 blog + 63 vps). dist: 51 blog + 63 vps. Live-only = `blog` + `vps` index URLs only (benign — the /blog/ and /vps/ index routes). **No live article would be deleted. Deploy safe.**

## Deploy
`wrangler pages deploy dist --project-name=vpstier-com --commit-dirty=true` → **7 files uploaded (126 already uploaded)** in 1.63s ✓, deployment ID `638f835d`. Preview: https://638f835d.vpstier-com.pages.dev

## Live verification (cache-bust fetch, +50s after deploy)
| URL | HTTP | Bytes | Title | Canonical | JSON-LD types | Hetzner |
|---|---|---|---|---|---|---|
| /vps/ultahost/ | 200 | 18,797 | ✓ | ✓ ultahost/ | Review, Product, FAQPage, BreadcrumbList | 0 |
| /blog/ultahost-vps-review-2026/ | 200 | 29,724 | ✓ | ✓ blog/... | Article, FAQPage, BreadcrumbList | 0 |
| /vps/ (index) | 200 | — | Ultahost card present ✓ | — | — | 0 |
| /blog/ (index) | 200 | — | ultahost post top card ✓ | — | — | 0 |

Live sitemap-0.xml: 124 URLs ✓ (up from 122; both new Ultahost URLs present).

## Banned-provider self-audit: PASS
- 0 Hetzner mentions in any file created/modified this run (grep -i on all 6 touched files)
- 0 Hetzner mentions in live rendered HTML for all 4 checked URLs (vps page, blog, both indexes)
- All CTAs → https://my.racknerd.com/aff.php?aff=16299 per standing policy

## Git workflow (skill-compliant two-commit)
```
9430065 feat(vps): add Ultahost provider page + VPS review 2026-08-21 (managed KVM, 33+ DCs, AMD EPYC)  ← article commit
<state commit to follow>
```
Used `git add <specific files>` (not `git add -A`) — sibling cron's untracked drafts (outline-*.md, run-record-*.md) left alone.

## Why this run is worth saving as a reference
1. **Prompt candidate list now exhausted for 4 consecutive runs** (8-18 TMDHosting, 8-19 Cloudblast, 8-20 MilesWeb, 8-21 Ultahost) — the "scan disk → pick gap" pattern is now the default for this cron; the prompt's "good options" list is entirely stale.
2. **Briefing ⭐ picks were both consumed by the daily-outline cron the same morning** — the add-provider cron correctly fell back to a new-vendor rotation. Confirms the dual-cron coordination: when the morning outline cron takes both ⭐ picks, add-provider does a vendor rather than re-picking.
3. **Managed VPS providers are a legitimate add-provider target** — Ultahost (managed, 33+ DCs) added cleanly, distinct from the budget-unmanaged rotation. The template/JSON-LD/provider-card patterns transfer unchanged.
