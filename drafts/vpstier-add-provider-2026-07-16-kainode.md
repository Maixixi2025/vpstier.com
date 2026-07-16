# vpstier add-provider-and-review 2026-07-16 (Kainode VPS)

**First verified instance of:** Tier 1 briefing-pick add-provider-and-review (vs the Tier 4 orphan pattern of recent runs), plus state-drift reconciliation of providers.json in the same run.

## Topic selection

- **Source:** Daily briefing `2026-07-16` from cron `3ea88f8bb2d0` — VPS ⭐ #2: "Kainode 推出新加坡便宜 VPS — LowEndBox (7-15)"
- **Tier rationale:** Tier 1 (research-lead briefing item) — the briefing explicitly called out Singapore as a buyer pain point, Kainode as the new entrant, and pricing as "需要实测" (verify-on-test).
- **Why not the other Tier 1 candidates:** HostNamaste (already covered by incomplete 2026-07-15 run, with the .astro file + index card on disk) and KVM Guest-to-Host escape (covered by today's separate daily-outline cron as `januscape-kvm-escape-vps-security-2026`).
- **Conflict check:** No existing blog slug targets Kainode, kainode.com, or Singapore VPS in the budget tier.

## Verified pricing (2026-07-16, 5-min window before publish)

Re-crawled `https://kainode.com/` (59,028B HTML, JS-rendered pricing carousel loaded with full data — NOT the JS-shell fallback seen on `/vps` and `/pricing`):

| Plan | vCPU | RAM | NVMe | BW | Daily | Monthly |
|------|------|-----|------|----|-------|---------|
| VDS Pro | 2 dedicated | 4 GB | 80 GB | 3 TB | $0.25/day | $16.99/mo |
| VDS Business (Popular) | 3 dedicated | 6 GB | 100 GB | 5 TB | $0.40/day | $19.52/mo |
| VDS Enterprise | 4 dedicated | 8 GB | 150 GB | 10 TB | $0.63/day | $29.99/mo |

Datacenters: Singapore (relaunched 2026), Germany, USA. Anti-DDoS included by default. Daily/weekly/monthly/yearly billing cycles supported. Wyoming-registered (30 N Gould St Ste R, Sheridan, WY 82801).

## Pipeline executed (autonomous, one execute_code block per major step)

1. **Topic pick** — Tier 1 #2 from briefing, distinct from the other 2 candidates
2. **Verified data** — `drafts/kainode-verified-data-2026-07-16.md` (3.6KB)
3. **Source files written** — `src/pages/vps/kainode.astro` (11.5KB) + `src/pages/blog/kainode-vps-review-2026.astro` (23.2KB), split into 3+4 pieces each to avoid `write_file` >2KB silent truncation (per skill pitfall NEW 2026-07-15)
4. **providers.json** — surgical insert at end + reconstruction of 3 missing entries (scaleway, yinnet, aliyun) that were lost in disk state drift
5. **vps/index.astro card** — added before the grid's closing `</div>` (after hostnamaste card)
6. **blog/index.astro post** — inserted at top of `posts` array (right after `const posts = [`)
7. **state.json** — appended to `published[]` (49th entry, 45 published + 4 published-during-cron patterns). Removed 0 stale drafts (no prior kainode draft existed).
8. **8-check pre-flight** — all 8 checks PASS on the new files
9. **Build** — `NODE_OPTIONS="--max-old-space-size=400" npx astro build --silent` — 3.3s elapsed, exit 0, 105 dist pages
10. **Deploy** — `wrangler pages deploy dist --project-name=vpstier-com --branch=main --commit-dirty=true` — 15.3s, 107 files uploaded, deploy ID `f605e7e4`
11. **Live verify** — both production URLs return correct title + content (after ~30s CF Pages propagation for `/blog/kainode-vps-review-2026/`)
12. **Git commit + push** — `dd2b678` pushed to `main`, 7 files changed (+999/-261), GitHub remote `49973dd..dd2b678`

## Three new cross-cutting lessons

### 1. State-drift reconciliation: disk entries missing from git HEAD (NEW 2026-07-16)

**Symptom:** Git HEAD `providers.json` had 43 entries; disk had 41. Three entries (scaleway, yinnet, aliyun) committed in `fb45a49` (2026-07-14 aliyun cron) were missing from disk. Adding kainode without restoring those 3 would have lost them on next commit.

**Discovery recipe:**
```python
import json, subprocess
disk = json.load(open('/root/vpstier-site/src/data/providers.json'))
git_head = json.loads(subprocess.run(['git', 'show', 'HEAD:src/data/providers.json'], capture_output=True, text=True, cwd='/root/vpstier-site').stdout)
disk_ids = set(p['id'] for p in disk)
git_ids = set(p['id'] for p in git_head)
print(f"Missing from disk: {git_ids - disk_ids}")
print(f"Added to disk: {disk_ids - git_ids}")
```

**Fix:** Before any `providers.json` mutation, run the discovery recipe. If entries are missing from disk, **reconstruct disk to match git HEAD order + add new entries at end**. Verify with `assert all(disk_by_id[p['id']] == git_by_id[p['id']] for p in git)` — every git HEAD entry must be byte-identical on disk.

**Verification pitfall:** Even after the fix, the resulting diff may be 600-700 lines because the original git HEAD entries had **non-uniform indentation** (e.g. scaleway entry uses 2-space indent for top-level fields, while newer entries use 4-space). This is a legacy artifact from the `rfind('  }')` surgical insertion pattern. The diff is functional-equivalent — git will accept it but the diff stats look noisy.

**Detection in next cron run:** always run the discovery recipe FIRST in any vpstier cron that touches `providers.json`. Pattern B3 in ilang-content v3.0.11 covers the case where disk has more than git, but this is the inverse case (disk has LESS than git, both legitimate from prior crons that didn't commit).

### 2. Briefing ⭐ #2 vs #3 editorial choice (NEW 2026-07-16)

**Symptom:** Today's VPS briefing had 3 Tier 1 candidates:
1. ⭐ HostNamaste (already covered by incomplete 2026-07-15 run)
2. ⭐ Kainode Singapore VPS (new)
3. ⭐ KVM Guest-to-Host escape (security news, better fit for daily-outline cron as a buyer-guide comparison)

**Decision:** Pick #2 (Kainode) for add-provider-and-review because:
- HostNamaste's incomplete state can be addressed via a separate cleanup commit (not the add-provider cron)
- KVM escape is a Tier 3 cost-discipline / security-news article archetype, not a provider add
- Today's daily-outline cron (09:45) had already produced the KVM escape outline (`januscape-kvm-escape-vps-security-2026`), so picking #3 would duplicate that handoff

**Rule (generalized):** when multiple briefing items fit the add-provider cron, pick the one that:
- Is NOT already covered by prior cron outputs (check `drafts/*.md` for outline presence)
- Is NOT a comparison/security article archetype that fits better with daily-outline
- Is the freshest / most concrete / most actionable for buyers

### 3. JS-rendered pricing page detection extended to Kainode (REINFORCED 2026-07-16)

Kainode's `/vps` and `/pricing` pages return 8.8KB and 9.8KB of JS-shell HTML with no pricing table data. The full pricing only loads in the homepage's carousel (59KB). The `browser_navigate` + `browser_console` recipe from the aliyun/scaleway runbooks was NOT needed — `urllib.request` on the homepage was sufficient because the carousel data was server-rendered into the HTML, not lazy-loaded via JS.

**Pattern:** when a provider's `/vps` or `/pricing` page returns small JS-shell HTML, **always check the homepage first**. Many providers render pricing into the homepage's hero carousel server-side (good for SEO) but lazy-load the dedicated `/pricing` page (bad for scraping). The homepage is usually the higher-fidelity data source.

## Self-audit

| Check | Result |
|---|---|
| Hetzner regex in new files | 0 matches across VPS page, blog, both indexes, providers.json entry, verified-data, dist HTML |
| Hetzner regex in state.json | 1 match (pre-existing aliyun entry from 2026-07-14, in `tier_decision` rationale explaining why aliyun was picked over Hetzner — meta-reference, NOT content) |
| Pre-flight 8-check on new files | All 8 PASS (Hetzner 0, titles ≤60, descs 70-155, no ZH, no /zh/, RackNerd 6+, H2 9, FAQ 5) |
| Live URL verify | Both URLs return correct title + body on `vpstier.com` (after 30s CF Pages propagation) |
| Git commit | `dd2b678` on `main`, pushed to remote |

## Files modified (this run)

| File | Type | Size |
|------|------|------|
| `src/pages/vps/kainode.astro` | NEW | 11.5 KB |
| `src/pages/blog/kainode-vps-review-2026.astro` | NEW | 23.2 KB |
| `src/data/providers.json` | MODIFIED (surgical insert + state-drift restore) | +3.2 KB net |
| `src/pages/vps/index.astro` | MODIFIED (kainode card) | +1.2 KB |
| `src/pages/blog/index.astro` | MODIFIED (kainode post) | +0.4 KB |
| `drafts/state.json` | MODIFIED (published[] append) | +1.2 KB |
| `drafts/kainode-verified-data-2026-07-16.md` | NEW | 3.6 KB |

## Live URLs (verified 2026-07-16)

- VPS card: https://vpstier.com/vps/kainode/ — 17,850B, 34× kainode mentions
- Blog review: https://vpstier.com/blog/kainode-vps-review-2026/ — 30,093B, 69× kainode mentions, 5 JSON-LD blocks
- Preview (CF Pages): https://f605e7e4.vpstier-com.pages.dev
