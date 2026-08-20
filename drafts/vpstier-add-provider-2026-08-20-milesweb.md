# vpstier Add-Provider-and-Review Run — 2026-08-20 (MilesWeb)

## Result: SUCCESS

**Provider added:** MilesWeb — established managed-hosting provider (est. 2009, UK+India HQ) with managed and unmanaged Linux KVM VPS across 32 global datacenters. Managed tiers from $69.99/mo.

## ⭐ Selection logic

The prompt's "good options" candidate list was **fully exhausted on disk** (13 of 13 already had `.astro` pages: A2 Hosting, Bluehost, FastComet, ScalaHosting, ChemiCloud, DreamHost, GreenGeeks, SiteGround, HostPapa, InMotion Hosting, TurnKey Internet, ServerPeacock; only ZAP VPS remained uncovered but it is an obscure budget host with thin verifiable public data — and `zap-hosting.astro` already covers the *different* German ZAP-Hosting company, creating a near-duplicate-slug risk). Repeated the "scan disk → pick a real gap with solid public info" pattern from the 2026-08-18/19 TMDHosting + Cloudblast runs.

Today's briefing (`3ea88f8bb2d0`, 2026-08-20) vpstier ⭐ picks were **both Hetzner** (banned merchant):
1. ⭐ Hetzner inference experiment → **REJECTED** (banned merchant)
2. Hetzner 187-250% price hike re-test → **REJECTED** (banned merchant)
3. (non-starred) data-center waste heat → **already covered** today by the daily-outline cron (`data-center-heat-siting-vps-selection-2026`)

Per the banned-pivot + add-provider rotation: no usable vpstier ⭐ today → fall back to adding a new vendor. **MilesWeb** was picked as a major uncovered provider with strong public data (live pricing + FAQ extracted from milesweb.com).

## Vendor verification

**Primary sources verified live (HTTP 200, 2026-08-20):**
- `https://www.milesweb.com/vps-hosting/` — 155,239 bytes, full managed-plan table + FAQ JSON-LD

**Managed VPS pricing (extracted from the milesweb.com VPS page plan cards):**

| Plan | vCPU | RAM | NVMe | Bandwidth | 1st-term | Renewal | Intro off |
|---|---|---|---|---|---|---|---|
| KVM 4GB | 2 | 4 GB | 80 GB | 3 TB | $69.99/mo | $89.99/mo | 22% |
| KVM 8GB (Best deal) | 4 | 8 GB | 160 GB | 4 TB | $89.99/mo | $109.99/mo | 18% |
| KVM 16GB | 6 | 16 GB | 320 GB | 5 TB | $129.99/mo | $149.99/mo | 13% |

**FAQ-verified features:** 32 global datacenters; provisioning <2 min; 30-day money-back (first term); free end-to-end migration (files/DB/email/DNS) across WordPress/Magento/custom PHP; cPanel/CyberPanel/Webuzo/Plesk/DirectAdmin panels; NVMe + 1 Gbps + network DDoS protection; managed + unmanaged tiers; transparent up-front renewal rates.

## Files created

- `src/pages/vps/milesweb.astro` (provider page, 9,582 bytes, 12 JSON-LD types)
- `src/pages/blog/milesweb-vps-review-2026.astro` (long-form review, 16,900+ bytes, 1,538 body words, 10 JSON-LD types, 11 H2, 5 FAQ)
- `drafts/vpstier-add-provider-2026-08-20-milesweb.md` (this file)

## Files modified

- `src/data/providers.json` (59 → 60 entries; new MilesWeb with 3 managed-plan tiers + 32-DC array + features)
- `src/pages/vps/index.astro` (60 → 61 cards, +1,265 bytes, MilesWeb card after Cloudblast)
- `src/pages/blog/index.astro` (+1 entry at top of `const posts`)
- `drafts/state.json` (published 74 → 75, last_publish → 2026-08-20, last slug = milesweb-vps-review-2026)

## Metric validation (script-measured)

```
VPS page   : title 49/60 ✓, desc 153/155 ✓, 258 body words (provider page; racknerd baseline 118)
              external links: affiliate 403 (expected), FAQ JSON-LD 5 Q/A
Blog page  : title 58/60 ✓, desc 149/155 ✓, 1538 body words ✓ (within 1500-2200)
              H2 x11 ✓, FAQ x5 ✓, 10 JSON-LD types, 5 internal links (all resolve on disk)
```

**External link verification (pre-deploy):**
- `https://www.milesweb.com/vps-hosting/` → 200 ✓ (155,239 bytes)
- `https://my.racknerd.com/aff.php?aff=16299` → 403 EXPECTED (standing RackNerd affiliate exemption)

**Internal link audit:** all `/blog/...` and `/vps/...` hrefs in both new pages resolve to existing `.astro` files on disk (verified via glob).

## Build & deploy

`npm run build` → **122 pages built in 3.65s** ✓ (was 120; +2 for new vps + blog). `[alias-sitemap]` wrote `dist/sitemap.xml` with 122 URLs, both milesweb URLs present.

**Pre-deploy drift check:** live sitemap 62 vps + 50 blog (excl milesweb) vs local disk 61 vps + 49 blog → LIVE-ONLY = `['vps']` only (the `/vps/` index slug artifact, NOT a lost page — served by `vps/index.astro`) + 0 blog. **No live page would be deleted. Deploy safe.**

`wrangler pages deploy dist --project-name=vpstier-com --commit-dirty=true` → **125 files uploaded (6 already uploaded)** in 2.25s ✓, deployment ID `466054f0`. Preview: https://466054f0.vpstier-com.pages.dev

## Live verification (cache-bust fetch, +30s after deploy)

| URL | HTTP | Bytes | Title match | Canonical OK | FAQ Q |
|---|---|---|---|---|---|
| `/vps/milesweb/` | 200 | 16,648 | YES | YES | 10 |
| `/blog/milesweb-vps-review-2026/` | 200 | 24,818 | YES | YES | 10 |

`/vps/` index: MilesWeb card rendered ✓. `/blog/` index: milesweb-vps-review-2026 slug rendered ✓. Live sitemap-0.xml: both milesweb URLs present ✓.

## Banned-provider self-audit: PASS

- 0 Hetzner mentions in all 5 files created/modified this run (verified via regex)
- 0 Hetzner mentions in live rendered HTML for `/vps/milesweb/`, `/blog/milesweb-vps-review-2026/`, `/vps/`, `/blog/` (verified via cache-bust fetch)
- All CTAs → `https://my.racknerd.com/aff.php?aff=16299` per standing policy

## Git workflow

```
<after state commit> commit + push to origin main
```
First commit `d733631` (article + providers.json + index edits) made BEFORE build/deploy (commit-before-build rule) — brand-new untracked `.astro` files are safe from any `git reset`. Used `git add <specific files>` (not `git add -A`); 12 untracked drafts from concurrent daily-outline crons left uncommitted, preserving their owner attribution.

## Why this run is worth saving as a reference

1. **Second add-provider run with "no usable briefing ⭐" today** — both vpstier ⭐ picks were the banned merchant (Hetzner), and the non-starred item was already covered by the same-day daily-outline cron. The add-provider cron correctly fell through to the vendor-rotation path rather than manufacturing a thin article.
2. **MilesWeb = the "established managed host with JS-rendered pricing" variant** — the Visible-Webflow/JSON-LD-FAQ probe pattern from 2026-08-19 (Crusoe/Cloudblast) applied, but MilesWeb's pricing sits in **plan-card HTML blocks** (`plan-col` divs with `mw-ban-price` spans + `plan-h4` names) rather than JSON-LD. Extraction recipe: split on `plan-col`, regex `plan-h4` for name + `mw-ban-price` for value, then tag-strip the whole block for specs. The FAQ JSON-LD (`acceptedAnswer` regex) still delivered the feature prose. Both patterns in one vendor.
3. **Batch 403-to-urllib is common among large US hosts** (HostGator/AccuWeb/Nexcess/GoDaddy/iPage all 403'd) — MilesWeb (200, full SSR HTML) was the verifiable pick. Reinforces the rule: probe first, pick what returns real data.
4. Near-duplicate-slug guard: `zap-hosting.astro` (German ZAP-Hosting) already exists, so **ZAP VPS** (a *different* US budget host) would create two confusingly similar slugs — deliberately avoided despite being the only "uncovered" prompt candidate.

References pulled: SKILL.md ilang-content (vpstier add-provider runbook + banned-pivot + Cloudblast reference), `references/vpstier-add-provider-2026-08-19-cloudblast.md`.
