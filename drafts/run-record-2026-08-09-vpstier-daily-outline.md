# VPSTier Daily-Outline Run Record — 2026-08-09 (Sunday)

## Run context
- **Cron:** `5fd2a36f2dc4` (vpstier daily-outline)
- **Briefing (`3ea88f8bb2d0`):** FAILED — HTTP 400 `reasoning_content` (3rd consecutive run: 8-06, 8-08, 8-09). Persistent failure; direct Google News RSS used as the topic source.
- **GSC (`5570fe2cffa6`):** vpstier.com shows only `ovh vps ssd` (rank 28, 1 imp) — **already captured** by the pending 8-07 `ovhcloud-vps-review-2026` outline. Not a new pick.

## Chosen topic
- **Slug:** `linux-kernel-escape-patches-august-2026-vps`
- **Title:** `Linux Kernel Escapes 2026: Patch Your VPS Now (CVE-64561)` — 57 chars ✅
- **Description:** 141 chars ✅
- **Format:** single-deliverable news-analysis + buyer hardening guide (9 H2 / 5 FAQ / 6 RackNerd CTAs / 6 whitelisted providers)
- **Story:** Aug 6–7, 2026 Linux kernel escape round — **Zapscape CVE-2026-64561** (KVM guest→host escape via shadow-MMU UAF, Hyunwoo Kim, disclosed 08-06) + **SCTPhantom CVE-2026-64564** (18-yr SCTP UAF → root + container escape, Tencent Zhuque Lab, disclosed 08-06), both fixed in stable kernels **7.1.6 / 6.18.42 / 6.12.101 / 6.6.148** (released 08-03).
- **Verification:** 6+ named outlets with dates (THN 08-06, Phoronix 08-07, CyberSecurityNews 08-07, 9to5Linux 08-07, CCB Belgium CERT 08-07, cyberkendra 08-06) + **body-verified facts** from the fetchable The Hacker News articles (CVE numbers, kernel versions, CVSS 7.0/8.5, CWE-825, root-cause, patch guidance).
- **Content gap:** `grep -riliE "zapscape|cve-2026-64561|sctphantom|sctp|kvm.{0,20}escape" src/` → 0 matches. Clean gap.

## Output files created
- `drafts/outline-2026-08-09-vpstier-daily.md` (the user-facing preview outline)
- `drafts/state.json` (appended `outline_pending_publish` entry; drafts_count 21→22; recent_topics + last_run + publish_notes updated; read-back assert PASSED)
- this run-record

## Self-check (all passed)
| Metric | Value |
|---|---|
| Excluded-merchant (banned-list) mentions in outline draft | 0 ✅ |
| CJK chars | 0 ✅ |
| `/zh/` routes (only negative assertions) | 0 new ✅ |
| Title | 57 / 30–60 ✅ |
| Description | 141 / 70–155 ✅ |
| H2 count | 9 / 8–10 ✅ |
| FAQ | 5 / 3–5 ✅ |
| RackNerd affiliate CTA | 6 ≥ 6 (all exact `aff=16299`) ✅ |
| Internal links | 10/10 resolve on disk ✅ |

## Pending outlines in `drafts[]` (user publish-gate = constraint)
greengeeks, hostdare, vps-kyc, ny-data-center-moratorium (07-15, superseded), januscape (07-16), black-friday-early, agent-zero, cloudflare-markdown, luxvps×2, cloudflare-internal-dns, vps-shutdown, 5-best-cheap-summer, namecheap, serverhost+cheapest-2gb, data-center-politicalization (8-04), ovhcloud (8-07), best-budget-vps-for-woocommerce (8-08), **+ linux-kernel-escape-patches-august-2026-vps (8-09, today)**.

### Partial-overlap flag (Januscape)
The queued 07-16 `januscape-kvm-escape-vps-security-2026` outline (July CVE-2026-53359) shares the general theme (KVM guest→host escape) with today's new outline. Per the supersede-recipe, today's angle is **partial overlap → written separately**, Januscape surfaced on-hold (NOT auto-archived). Recommendation: user may publish Januscape first, or fold its July context into today's new article and archive it. Cron does not auto-archive.

### Other on-hold / flagged
- Untracked 8-05 `us-data-center-politics-2026-vps-impact` outline: on disk, never entered in state.json. Flagged.
- DC-politicalization queue (07-15, 8-04, 8-05): user decides archive/publish.
- **Uncommitted-backlog risk (still open):** `git status` shows multiple untracked prior outline/run-record files (08-01, 08-03, 08-04, 08-05, 08-07). This run commits only its own 3 files (today's outline + run-record + state.json). The accumulated backlog is flagged for a user-scheduled cleanup commit — NOT swept blindly.

## Git
Two-commit order: (1) outline + run-record (+ any supporting), (2) state.json referencing the run. Push once.
