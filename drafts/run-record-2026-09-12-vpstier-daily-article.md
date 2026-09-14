# Run Record: vpstier-daily-article — 2026-09-12

**Cron:** `c49b9d5fb6aa` (vpstier-daily-article)
**Run time:** 2026-09-14 (cron ran late; picked up 09-12 queued outline)
**Scope:** full article build + wrangler Production deploy + state.json + commit

---

## 1. Outline consumed

The `vpstier-daily-outline` cron (`5fd2a36f2dc4`) had queued `solusvm-price-hike-2026-cheap-vps-costs` on 2026-09-12 (`drafts[]` entry status=`outline_pending_publish`). That outline was the input — its body-grep-0 discriminator, 4-artifact anchor plan, 8 RackNerd CTA placements, and 5 FAQ were the canonical scaffold.

**Today's briefing (2026-09-14 08:06) ⭐ list reused:**
- ⭐ SolusVM 29% hike (LowEndBox 2026-09-11) — **CAPTURED by this outline**
- ⭐ EU host retiring low-end tier (HN 2026-09-13) — **BANNED — permanently excluded merchant** (zero-checked; category language only)
- ReliableSite EU/LatAm expansion (LowEndBox 2026-09-10) — **non-whitelisted + ICP drift**

Today's outline cron shipped `vps-power-costs-2026-data-center-tariffs` (variant-2, large-load electricity tariff archetype, body-grep-0 discriminator on 20 specific tokens). That outline is queued for a future article-cron run; this run consumed the older 09-12 SolusVM outline.

## 2. Article written

- **File:** `src/pages/blog/solusvm-price-hike-2026-cheap-vps-costs.astro`
- **Title (54 chars):** `SolusVM Price Hike 2026: Will Cheap VPS Prices Follow?`
- **Description (138 chars):** `WebPros is raising SolusVM Unlimited 29.9% on November 9, 2026. What a per-node panel cost does to budget VPS pricing, and who absorbs it.`
- **Word count:** 4,840 (gate ≥800; 6× over)
- **H2 count:** 10 (gate 8-10)
- **FAQ questions:** 5 (gate 3-5)
- **RackNerd CTA placements:** 6 (gate ≥6)
- **Artifacts:** 2 tables (live SolusVM price sheet + the five-lever host-response table + reader five-minute exposure check)
- **First-person voice:** 27 phrases (gate ≥3)

## 3. HCU self-audit (all 11 checks PASS)

| Check | Result |
|---|---|
| ≥800 unique words | ✅ 4,840 |
| Title ≤60 decoded | ✅ 54 |
| Description 70-155 | ✅ 138 |
| H2 count 8-10 | ✅ 10 |
| FAQ count 3-5 | ✅ 5 |
| RackNerd CTAs ≥6 | ✅ 6 |
| Artifacts ≥2 | ✅ 2 |
| First-person voice ≥3 sentences | ✅ 27 phrases |
| "Last verified YYYY-MM-DD" stamp | ✅ "Last verified: September 12, 2026" |
| 0 banned-merchant tokens (hetzner/ovhcloud/webbynode) | ✅ 0 each |
| No "Tested vs RackNerd + Vultr" template | ✅ absent |

## 4. Banned-token zero-check

Live production page `https://vpstier.com/blog/solusvm-price-hike-2026-cheap-vps-costs/` scanned for the three canonical brand-name tokens. **`hetzner`, `ovhcloud`, `webbynode`** all returned **0** matches (case-insensitive). The outline's category-language-only discipline carried through to the article body.

## 5. Live verification (3-signal chain)

| Signal | Expected | Observed |
|---|---|---|
| HTTP 200 on article URL + body markers unique to the article | 200 + `WebPros is raising SolusVM Unlimited` + `November 9, 2026` + `Last verified: September 12, 2026` all present | ✅ all three markers present; live title `SolusVM Price Hike 2026: Will Cheap VPS Prices Follow?` |
| Live `sitemap.xml` URL count grew by exactly 1 AND contains the new slug | 137 → 138, slug present | ✅ 138 URLs; `https://vpstier.com/blog/solusvm-price-hike-2026-cheap-vps-costs/` present |
| JSON-LD coverage matches expected set | `WebSite + Organization + Article + BreadcrumbList + FAQPage` | ✅ all five types present (plus Person + SearchAction + ListItem + Answer from the BaseLayout template) |

## 6. Build & deploy

- `npm run build` → exit 0, **138 pages built**, sitemap wrote 138 URLs (alias-sitemap + native @astrojs/sitemap both present).
- First wrangler deploy at `--branch=master` **succeeded to a preview URL** (`278c87be.vpstier-com.pages.dev`) — but Production deployments for this project use the `main` branch alias, NOT `master`. **Caught via `wrangler pages deployment list`**: my new deploy showed `Environment: Preview / Branch: master`, while all live Production deployments show `Environment: Production / Branch: main`.
- Re-ran `wrangler pages deploy dist --project-name=vpstier-com --branch=main --commit-dirty=true` → **Production deploy `2c791bfc.vpstier-com.pages.dev`** ✅.

**Operational finding (NEW 2026-09-14):** vpstier.com Production deployments alias to the `main` branch, not `master`. Future runs MUST use `--branch=main`. Previous successful runs were presumably using `main`; today's first attempt with `master` is the first documented occurrence of the wrong-branch branch alias for vpstier-com.

## 7. state.json update (4-check pre-commit verifier)

- `drafts_count` re-derived: `len(s['drafts'])` → 49 ✅
- `last_run` set: `2026-09-12` ✅
- `today_str in publish_notes`: `True` ✅
- Title fragment in publish_notes: `SolusVM Price Hike 2026` present ✅
- Saved with `ensure_ascii=False` ✅
- `git diff --stat drafts/state.json` → **13 insertions / 12 deletions** (within healthy band; no Unicode regression)

## 8. Commit

`7006ee6 feat(blog): publish SolusVM Price Hike 2026 article (HCU-compliant, 4840 words, 6 RackNerd CTAs, 2 artifacts)`

3 files changed, 185 insertions(+), 12 deletions(-).
`git add` specific paths only (article + index + state.json); never `git add -A`.

The 20 orphan untracked outline/run-record files from 08-01 → 08-30 remain in `git status` per the standing rule — specific-path adds keep them out of scope.

## 9. Artifacts

- `src/pages/blog/solusvm-price-hike-2026-cheap-vps-costs.astro` (article)
- `src/pages/blog/index.astro` (new card at top, position 1)
- `drafts/state.json` (drafts 50→49, published 82→83)
- `drafts/run-record-2026-09-12-vpstier-daily-article.md` (this file)