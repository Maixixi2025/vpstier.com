# VPSTier Add-Provider-and-Review Run — 2026-08-19 (Cloudblast)

## Result: SUCCESS

**Provider added:** Cloudblast — new vendor (Aug 2026 LEB coverage), 10 Gbps + DDoS-included KVM-Proxmox VPS from €3.6/mo across Amsterdam, Salt Lake City, and Hong Kong.

## Why Cloudblast (vs the prompt's stale candidate list)

The task prompt's "good options" list (A2 Hosting / Bluehost / FastComet / etc.) was fully exhausted (all 13 already covered on disk → 60 vps pages matching 60 cards). Repeated the 2026-08-18 TMDHosting "scan disk → pick gap" pattern: looked at the briefing for new vendors and picked the day's ⭐ vpstier pick #2.

**Hot-topic briefing (`3ea88f8bb2d0`, 2026-08-19) vpstier ⭐ picks:**
1. ⭐ Hetzner 187-250% price-increase re-test → **REJECTED** per permanent merchant policy
2. ⭐ **Cloudblast 4GB €4.03/mo unlimited bandwidth** (LowEndBox, raindog308, 2026-08-12) → **PICKED**
3. Cursor self-hosted GitHub-rival → TechCrunch URL 404'd, no named-outlet RSS hit → rejected

The briefing's pick #1 (Hetzner retrospective) was rejected because the merchant is permanently delisted site-wide. The daily-outline cron (`5fd2a36f2dc4`, run earlier today) pivoted the same briefing signal to "structural industry version" (Aug 17 Tom's Hardware component-cost second wave → slug `gpu-ram-price-wave-2026-ai-vps-buyers`, already in state.json as `outline_pending_publish`). For the add-provider cron, we have different available actions — we can pick a *new vendor* (Cloudblast) that does NOT trigger the merchant ban.

## Vendor verification

**Primary sources verified live (HTTP 200, 2026-08-19):**
- `https://cloudblast.io/pricing` — 721,656 chars, full plan table + add-ons
- `https://cloudblast.io/` — 1,016,813 chars, datacenter locations + DDoS-as-standard copy
- `https://lowendbox.com/blog/cloudblast-4gb-vps-for-only-e4-03-month-in-usa-nl-and-hong-kong-with-unlimited-bandwidth/` — 142,288 chars, raindog308 2026-08-12 feature, node specs (AMD EPYC 7551P / 7C13 / 7663)

**Pricing tiers (verified from cloudblast.io/pricing):**

| Plan | €/mo | €/hr | vCPU | RAM | NVMe | BW |
|---|---|---|---|---|---|---|
| VMA11 | €3.6 | €0.0049 | 1 EPYC | 3GB | 20GB | Unlimited US/NL; 1TB HK |
| VMA21 | €4.8 | €0.0067 | 2 EPYC | 4GB | 30GB | Unlimited US/NL; 1TB HK |
| VMA31 | €7.2 | €0.010 | 3 EPYC | 6GB | 40GB | Unlimited US/NL; 1TB HK |
| VMA41 | €9.6 | €0.014 | 4 EPYC | 8GB | 40GB | Unlimited US/NL; 1TB HK |
| VMA51 | €19.2 | €0.027 | 8 EPYC | 16GB | 60GB | Unlimited US/NL; 1TB HK |
| VMA61 | €28.8 | €0.040 | 8 EPYC | 24GB | 60GB | Unlimited US/NL; 1TB HK |
| VMA71 | €38.4 | €0.054 | 10 EPYC | 32GB | 140GB | Unlimited US/NL; 1TB HK |
| VMA81 | €78.8 | €0.109 | 16 EPYC | 64GB | 200GB | Unlimited US/NL; 1TB HK |

Add-ons: backups €0.09/GB/mo, IPv4 €2.5/mo, block storage €0.15/GB/mo. Payment: credit cards via Stripe (Visa/MC/Amex), AliPay, crypto including Monero (XMR).

## Differentiation vs the rest of vpstier

- vs **RackNerd** ($1.99/mo entry, unmanaged KVM) — Cloudblast €3.6/mo entry undercuts at the 3 GB tier; bundles DDoS + 10 Gbps port that RackNerd does not
- vs **Vultr** ($5/mo entry, NVMe, hourly) — Cloudblast VMA11 (€3.6/mo / 3 GB) undercuts Vultr's 4 GB tier ($24/mo); Vultr has 32+ DCs vs Cloudblast's 3
- vs **HostHatch** ($4/mo entry, EPYC, 14 regions) — Cloudblast cheaper at 4 GB (€4.8 vs $4); HostHatch has 14 DCs vs 3
- vs **Linode (Akamai)** ($5/mo Nanode) — Linode has 11+ DCs + GPU tiers; Cloudblast is bare-bones DDoS+10Gbps play

## Files created

- `src/pages/vps/cloudblast.astro` (provider page, 13,578 bytes)
- `src/pages/blog/cloudblast-vps-review-2026.astro` (long-form review, 24,913 bytes, 2,172 body words)
- `drafts/cloudblast-verified-data-2026-08-19.md` (evidence file)

## Files modified

- `src/data/providers.json` (58 → 59 entries; new Cloudblast with 8 VMA plans + 3-DC array + features)
- `src/pages/vps/index.astro` (60 → 61 cards, +1,265 bytes)
- `src/pages/blog/index.astro` (+1 entry at top of `const posts` array, +349 bytes)
- `drafts/state.json` (published 73 → 74, last_publish + last_run → 2026-08-19, last slug = cloudblast-vps-review-2026)

## Metric validation (script-measured against `dist/`)

```
VPS page   : title 58/60 ✓, desc 148/155 ✓, 700 body words
              13 internal links (all resolve), 5 external links (3 vendor + 2 font + about.me)
              H2 x4 ✓, FAQ x5 ✓, 12 schema types
Blog page  : title 59/60 ✓, desc 155/155 ✓, 2172 body words ✓ (within 1500-2200)
              H2 x9 ✓, FAQ x5 ✓, 10 schema types, 31 internal links (all resolve)
```

**External link verification (pre-deploy):**
- `https://cloudblast.io/` → 200 ✓ (1,016,575 bytes)
- `https://cloudblast.io/pricing` → 200 ✓ (725,438 bytes)
- `https://lowendbox.com/blog/cloudblast-4gb-vps-for-only-e4-03-month-in-usa-nl-and-hong-kong-with-unlimited-bandwidth/` → 200 ✓ (142,288 bytes)
- `https://my.racknerd.com/aff.php?aff=16299` → 403 EXPECTED (standing RackNerd affiliate CTA)

## Build

`npm run build` → **120 pages built in 3.71s** ✓ (was 118; +2 for new vps + blog). `[alias-sitemap]` post-build wrote `dist/sitemap.xml` with 120 URLs.

## Pre-deploy drift check

| Set | Count |
|---|---|
| Live vps+blog slugs (sitemap-0.xml, 2026-08-19) | 108 |
| Local dist vps+blog slugs | 110 |
| `live_only` (would be DELETED by deploy) | **0** |

Disk (61 vps / 50 blog) vs dist (61 vps / 49 blog) = only `blog/index` differs (the index listing page, expected). **No live page would be deleted. Deploy safe.**

## Deploy

`wrangler pages deploy dist --project-name=vpstier-com --commit-dirty=true` → **123 files uploaded (6 already uploaded)** in 1.88s ✓, deployment ID `6d239220`. Preview: https://6d239220.vpstier-com.pages.dev

## Live verification (cache-bust fetch, +50s after deploy)

| URL | HTTP | Bytes | Title match | Canonical OK | JSON-LD types |
|---|---|---|---|---|---|
| `/vps/cloudblast/` | 200 | 20,125 | YES | YES | 12 (BreadcrumbList, Review, FAQPage+5Q/A, Product, Rating, + base layouts) |
| `/blog/cloudblast-vps-review-2026/` | 200 | 31,985 | YES | YES | 10 (BreadcrumbList, Article, FAQPage+5Q/A, + base layouts) |

`/vps/` index: Cloudblast card rendered ✓. `/blog/` index: cloudblast-vps-review-2026 slug rendered in `const posts` array ✓. Live sitemap-0.xml: 120 URLs ✓ (up from 118; both new Cloudblast URLs present).

## Banned-provider self-audit: PASS

- 0 Hetzner mentions in any created/modified file (verified via `grep -i 'hetzner'` on all 5 touched files)
- 0 Hetzner mentions in live rendered HTML (verified via `grep -i '[Hh]etzner'` on both live URLs + both index pages)
- All CTAs → `https://my.racknerd.com/aff.php?aff=16299` per standing policy

**Note on legacy Hetzner mention:** `src/pages/blog/contabo-vps-review-2025.astro` contains 4 mentions of Hetzner in comparison tables (last touched 2026-05-30, pre-ban). This is a pre-existing file from before the Hetzner ban was established; the ban policy is "do not write articles, do not add to providers.json, do not 'fix' dead links by creating pages" — i.e. it governs new work, not retroactive rewrites of committed legacy content. The 4 mentions are not in any file we wrote or modified this run.

## Git workflow (skill-compliant two-commit + separate run-record pattern)

```
41c0a46 chore(state): record Cloudblast VPS publish 2026-08-19 (git_commit fd494b7)
fd494b7 feat(vps): add Cloudblast provider page + VPS review 2026-08-19
97bcef6 chore(drafts): add run record for 2026-08-18 TMDHosting add-provider-and-review ← prior HEAD
```

**Push** to `origin main` succeeded (`97bcef6..41c0a46`). Branch confirmed via `git branch --show-current` → `main` (vpstier convention).

Used `git add <specific files>` (not `git add -A`) — 13 untracked drafts from concurrent crons (`outline-2026-08-01-namecheap-vps-review-2026.md` etc.) left uncommitted, preserving their owner cron attribution.

## Why this run is worth saving as a reference

This is the **second pure-new-provider rotation run with 0 dead cards** (after 2026-08-18 TMDHosting). The pattern is now repeatable:

1. **Briefing succeeded but pick #1 is a banned-merchant signal** → pivot to pick #2 (Cloudblast) for add-provider cron; pick #1 → daily-outline cron handles the structural-industry version
2. **Verify from the vendor's OWN pricing page** (cloudblast.io/pricing — 721 KB, full plan table) not the homepage alone (1 MB shell)
3. **Cross-check with LowEndBox body** for node specs, promotional SKUs, and editorial framing
4. **Keep Hetzner mentions out** even from neutral comparisons (originally wrote "RackNerd/Hetzner/Vultr" — patched to "most budget VPS tiers ship 1 Gbps" before commit)
5. **One commit for the article + provider files, one commit for state.json** (skill: commit articles first so a `git reset` can't destroy untracked work; state.json references the article commit hash)

References pulled from this run's evidence file: `drafts/cloudblast-verified-data-2026-08-19.md`.