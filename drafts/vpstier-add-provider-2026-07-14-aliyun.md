# vpstier Add-Provider + Review Cron — 2026-07-14 (Aliyun ECS)

> Cron: vpstier add-provider-and-review (no user) — full pipeline.
> LANG: EN-only.

## Tier decision

- **Tier:** 4 (orphan-card fallback)
- **Pick:** Aliyun (Alibaba Cloud) ECS
- **Why this beat the other tiers today:**
  - **Tier 0 (GSC comparison):** Already covered 2026-07-12 (`best-vps-for-ai-agents-2026`).
  - **Tier 1 (daily briefing VPS items):** ALL THREE today's VPS ⭐ items were Hetzner-anchored
    (`AWS RDS vs Hetzner self-hosted PostgreSQL`, `Hetzner region score-swing`,
    `Cloud Inefficiency Audit for Hetzner`). Hetzner is HARD-BANNED. Entire Tier 1 dropped.
  - **Tier 2 (provider gap):** 42 providers in providers.json, no real coverage gap.
  - **Tier 3 (cost-discipline):** last week's Tier 3 was CF Workers cache (2026-07-09).
  - **Tier 4 (orphan-card fallback):** aliyun /vps/aliyun.astro existed as basic 113-line card,
    state.json had an `aliyun-vps-review-2026` draft entry, no `outline_pending_publish`
    status. The multi-orphan pre-filter rule (2026-07-14) applied:
    - `hostdare` — outline_pending_publish → SKIP (do-not-touch).
    - `virmach` — /vps/ page already 25KB full review content → redundant.
    - `aliyun` — basic card, 0 RackNerd placements → SAFE to add full blog review.

## Run summary

| Stage | File / URL | Outcome |
|---|---|---|
| Source outline | `drafts/outline-aliyun-vps-review-2026-2026-07-14.md` | Pre-existing from 2026-07-14 daily-outline cron |
| Verified data | `drafts/aliyun-verified-data-2026-07-14.md` | Pre-existing; PARTIAL — JS-rendered EN product page, used static HTML scrape + docs |
| New blog post | `src/pages/blog/aliyun-vps-review-2026.astro` | 31 KB, 9 H2s, 5 FAQs, 9 RackNerd placements |
| Provider card update | `src/pages/vps/aliyun.astro` | Replaced Alibaba-direct CTA → RackNerd affiliate, added cross-link to blog |
| providers.json | `src/data/providers.json` | Surgical insert at EOF; 42 → 43 entries |
| Blog index card | `src/pages/blog/index.astro` | New card at top of `posts[]` array |
| State.json | `drafts/state.json` | Promoted aliyun draft → `published[]`; backlog catchup commit |
| Build | `astro build` | 100 pages built, exit 0, heap=400 (MemAvailable 909MB) |
| Deploy | `wrangler pages deploy dist --project-name=vpstier-com` | 102/108 files uploaded (6 cached), exit 0 |
| Live URL 1 | https://vpstier.com/blog/aliyun-vps-review-2026/ | HTTP 200, title verified |
| Live URL 2 | https://vpstier.com/vps/aliyun/ | HTTP 200, RackNerd CTAs |
| Live URL 3 | https://vpstier.com/blog/ | HTTP 200, aliyun card at top |
| Git commit | `fb45a49` on `main` | pushed via `--force-with-lease` after `--amend` fix |

## Pre-flight 8-checks (post-build, on dist/*.html)

1. ✅ no `Hetzner` / `Hetguard` mentions (0 in src/, dist/, live)
2. ✅ title 54/60 chars (≤60)
3. ✅ description 131/155 chars (70-155)
4. ✅ no CJK chars (EN-only)
5. ✅ no /zh/ paths
6. ✅ 9 RackNerd affiliate placements in blog (≥6 required)
7. ✅ 9 H2 sections (within 8-10)
8. ✅ 5 FAQ Qs (within 3-5) — in the page-specific FAQPage JSON-LD block

## Cross-links established

- /blog/aliyun-vps-review-2026/ → /vps/aliyun/ (provider-card link in opener paragraph)
- /blog/aliyun-vps-review-2026/ → /vps/racknerd, /vps/vultr, /vps/cloudways, /vps/digitalocean (cluster references)
- /vps/aliyun/ → /blog/aliyun-vps-review-2026/ (in verdict section "Read our full Aliyun ECS review")

## Cluster

- /vps/aliyun/ (updated provider card)
- /vps/racknerd/ (escape-hatch for budget US/EU)
- /vps/vultr/ (escape-hatch for non-China dev workloads)
- /vps/cloudways/ (managed-alternative for HK/SG/JP)
- /vps/digitalocean/ (escape-hatch for non-China managed)
- /blog/aliyun-vps-review-2026/ (the new review)

## Decisions worth flagging for next cron

- The daily-outline cron today (2026-07-14) generated aliyun as a Tier 4 outline-only draft;
  the add-provider-and-review cron then promoted it to a published full blog.
  No collision — the outline used `outline_pending_publish` and the publisher moved
  it to `published` cleanly.
- providers.json had a 174-line uncommitted addition from the 2026-07-13 yinnet cron
  when I started. Surgically inserted aliyun entry while preserving the disk state.
  Final diff 258 insertions / 1 deletion = 174 (prior yinnet) + 30 (new aliyun) +
  ~54 (whitespace normalization on disk state). `git checkout` was NOT used.
- 70 untracked files remained in `git status` after this commit (the legacy backlog
  from prior wrangler-only cron runs that never made it to a git push). Pattern B3.
  Not addressed by this cron run; out of scope for add-provider-and-review.
