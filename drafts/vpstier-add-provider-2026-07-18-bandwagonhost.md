# vpstier add-provider-and-review 2026-07-18 (BandwagonHost)

**Provider added:** BandwagonHost (IT7 Networks Inc., long-running low-end VPS brand)
**Pipeline:** Tier 2 (provider gap scan, manual curation) — autonomous one-block-per-step execution

## Topic selection

- **Source:** Manual curation from cron task brief and today's VPS briefing section. Today's briefing highlighted Hetzner price hikes (BANNED merchant — cannot use as Tier 1), NY moratorium (already covered by 2026-07-15 outline_pending_publish), and HostNamaste (already added 2026-07-16). No fresh Tier 1 candidate for new-provider work today.
- **Pick rationale:** BandwagonHost (bandwagonhost.com) chosen because (a) it's a real, documented provider with verified live pricing ($49.99/yr / $52.99/half-yr / $19.99/mo / $39.99/mo / $79.99/mo / $119.99/mo), (b) long-running LowEndTalk community staple (15+ year brand history), complementary to recent LightNode (40+ regions, monthly billing) — BandwagonHost is the multi-month-prepay / annual-floor tier in the budget segment, (c) operator IT7 Networks Inc. verified via TOS, (d) covers Hong Kong APAC presence, (e) different from Hetzner (banned) so no Tier 1 hard-ban applies.
- **Conflict check:** No existing blog slug targets BandwagonHost, bandwagonhost.com, or "IT7 Networks" — clean slot for a new add.

## Verified pricing (2026-07-18, 5-min window before publish)

Re-crawled 3 URLs (live HTTP probe, 5-min window):

| URL | Status | Bytes | Notes |
|-----|--------|-------|-------|
| `https://bandwagonhost.com/` | 200 | 15,473 | Full pricing + 6 plan blocks (verified live) |
| `https://bandwagonhost.com/tos` | 200 | 32,741 | Full refund policy + IT7 Networks Inc. jurisdiction |
| `https://bandwagonhost.com/knowledgebase` | 200 | 13,402 | KB index |

**Verified plans (KVM, Intel Xeon, RAID-10 SSD):**

| Plan | SSD | RAM | CPU | Transfer | Price | Cadence |
|------|-----|-----|-----|----------|-------|---------|
| 20G KVM VPS | 20 GB | 1 GB | 2 cores | 1 TB/mo | $49.99 | annual |
| 40G KVM VPS | 40 GB | 2 GB | 3 cores | 2 TB/mo | $52.99 | half-year |
| 80G KVM VPS | 80 GB | 4 GB | 4 cores | 3 TB/mo | $19.99 | monthly |
| 160G KVM VPS | 160 GB | 8 GB | 5 cores | 4 TB/mo | $39.99 | monthly |
| 320G KVM VPS | 320 GB | 16 GB | 6 cores | 5 TB/mo | $79.99 | monthly |
| 480G KVM VPS | 480 GB | (higher tier) | (higher tier) | (higher tier) | $119.99 | monthly |

**Verified company info:** Operator is IT7 Networks Inc. (verified from TOS section "us/we/our"). Datacenters include Los Angeles, New York, Hong Kong (multiple locations per public site). Plans may include separate SLA. Refund: 30-day full refund on new orders (not renewals), subject to 5 conditions (good standing, no chargebacks, no blacklisted IPs, transfer under 10% of quota, no excessive refund requests). Self-managed: buyers must have sufficient Linux knowledge — BWH only manages the host server, NOT the VPS.

**Pricing effective-month comparison:**
- BWH 20G annual: $49.99/yr ÷ 12 = $4.16/mo effective
- BWH 40G half-year: $52.99 / 6 = $8.83/mo effective
- BWH 80G monthly: $19.99/mo (no discount)
- RackNerd annual special: $10.98-$11.99/yr ≈ $0.92-$1.00/mo effective

## Pipeline executed (autonomous)

1. **Topic pick** — Tier 2 (provider gap scan)
2. **Verified data** — `drafts/bandwagonhost-verified-data-2026-07-18.md` (2.5 KB)
3. **VPS basic card** — `src/pages/vps/bandwagonhost.astro` (6.5 KB) — racknerd-style basic card pattern with 4 FAQs, 2 RackNerd placements
4. **Long-form blog review** — `src/pages/blog/bandwagonhost-vps-review-2026.astro` (26.5 KB) — 8 H2 sections, 5 FAQs, 9 RackNerd placements. Assembled via /tmp/bwh_parts/ to avoid write_file >2KB silent truncation pitfall.
5. **providers.json** — surgical insert at end (47 entries, was 46). Verified ends with `  }\n\n]`, replaced with `  }<new_entry>\n]`. JSON parses cleanly.
6. **vps/index.astro card** — added BEFORE LightNode card (newest-first ordering). Amber/orange "Multi-Month Prepay" badge.
7. **blog/index.astro post** — inserted BEFORE LightNode entry in `const posts = [...]` array (newest-first).
8. **state.json** — appended to `published[]` (51st entry). Atomic write via tempfile.
9. **Title + description pre-build trim** — caught 1 length violation:
   - Blog description was 167 chars → trimmed to 148 (`"Real pricing, 30-day refund policy"` → `"30-day refund policy + RAID-10 SSD"`)
   - Both BaseLayout prop + Article JSON-LD description updated in lockstep (H1 was 55 chars, already ≤60)
10. **8-check pre-flight** — all 8 PASS on both files (Hetzner regex: 0; title 51-55; desc 145-148; 0 ZH chars; 0 /zh/ paths; RackNerd 2 VPS / 9 blog; H2 markers 8 in blog; FAQ count 4 VPS / 5 blog)
11. **Build** — `npx astro build --silent` with `NODE_OPTIONS=--max-old-space-size=400` — 3.3s, exit 0, 109 dist pages (was 107 → +2 = new VPS page + new blog page). MemAvailable was 1043 MB (above 1GB tier — heap=400 worked first try).
12. **Deploy** — `wrangler pages deploy dist --project-name=vpstier-com --branch=main --commit-dirty=true` — 15.2s, 117 files uploaded (111 new + 6 already), deploy ID `5df8ec92`, preview URL `https://5df8ec92.vpstier-com.pages.dev`
13. **Live verify** — all 6 URLs return HTTP 200 with correct titles + body keywords:
    - `/vps/bandwagonhost/` → 200, 13,658 B preview / 14,162 B custom, title "BandwagonHost VPS Review 2026: Plans from $19.99/mo"
    - `/blog/bandwagonhost-vps-review-2026/` → 200, 33,368 B preview / 33,872 B custom, title matches, 8 H2 markers, 5 FAQPage questions, 9 RackNerd placements
    - `/vps/` → 200, 64,367 B, contains BandwagonHost marker (BEFORE LightNode)
    - `/blog/` → 200, 42,949 B, contains bandwagonhost slug (BEFORE LightNode in posts list)
14. **Git commit + push** — commit `d4c313a` on `main`, 8 files / +444/-4 lines, pushed to remote (`52d1f39..d4c313a  main -> main`)

## Self-audit

| Check | Result |
|---|---|
| Hetzner regex in new files (VPS + blog + index.astro + blog index + providers.json + state.json) | 0 matches |
| Hetzner regex in self-check section / outline / reference | 0 matches |
| Pre-flight 8-check on new files | All 8 PASS on both |
| Live URL verify | 6/6 URLs return HTTP 200 with correct title + body |
| Build | 109 dist pages (was 107), 3.3s with heap=400 at 1043MB MemAvailable |
| Deploy | Deploy ID `5df8ec92`, preview `https://5df8ec92.vpstier-com.pages.dev`, 15.2s, 117 files uploaded |
| Git commit | `d4c313a` on `main`, 8 files / +444/-4 lines, pushed to origin/main |
| Banned providers audit (Hetzner / hetguard) in new files | 0 mentions |
| Newest-first ordering preserved | VPS card inserted BEFORE LightNode; Blog entry inserted BEFORE LightNode entry |
