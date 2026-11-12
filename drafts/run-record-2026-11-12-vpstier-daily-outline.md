# Run Record — vpstier daily outline — 2026-11-12

**Cron:** `5fd2a36f2dc4` (vpstier-daily-outline)
**Date:** 2026-11-12
**Variant:** **variant-13** — briefing SUCCEEDED (2026-11-12 08:16 UTC, cron `3ea88f8bb2d0`), but **all three vpstier items failed a hard gate**; substituted the freshest dated, body-verifiable story found **outside** the briefing via the same feeds the briefing reads.
**Archetype:** secret-store breach / credential-blast-radius buyer-guide — NEW on vpstier.
**Slug:** `railway-breach-2026-740k-api-key-heist`
**Title:** 47/60 · **Desc:** 148/155 (both computed with Python `len()` on the final strings)
**Status:** `outline_pending_publish` — awaiting user `publish`.

---

## 1. Inputs read

| Input | Result |
|---|---|
| Daily briefing (`3ea88f8bb2d0`, 2026-11-12 08:16) | ✅ 14 items across 5 sites. 3 vpstier items, all rejected (§2). **Note:** `jobs.json` shows `last_status: error` with the report text wrapped inside a `RuntimeError:` — this is the canonical **pitfall #35** false-positive shape (the report itself succeeded; the delivery wrapper failed). The briefing content was read from the output file, not from the status field. |
| GSC daily report (`5570fe2cffa6`, 2026-11-12 07:00) | ✅ vpstier 30d: 306 imp / 0 clicks / avg pos 90.0 |
| Live GSC API (this run) | ✅ 90d pull via `gsc_daily_report.py` helpers (pitfall #52 — reused the module rather than hand-rolling OAuth): 60 page rows / 67 query rows |
| Weekly strategy report (`537976c317e8`, 2026-11-09 09:34) | ✅ vpstier: +1 article, 36 imp, 0 clicks, avg pos 85.1; 🟡 provider-page pipeline still dead; external-link target = LowEndTalk / HN Ask HN. **Paraphrased into English** — the original recommendation is in Chinese (pitfall #43). |
| `state.json` | ✅ 67 drafts / 84 published / 7 recent_topics; schema template taken from the 2026-11-11 entry (pitfall #47 — mirrored its exact key set) |
| `providers.json` | ✅ 65 entries — **Railway absent** (PaaS, not a hosting merchant ⇒ variant-10, no whitelist gate) |
| `src/pages/blog/` | ✅ 63 `.astro` files; H2 lists extracted for the collision check |
| `src/pages/vps/` | ✅ 69 pages; all 6 live cross-link targets verified on disk |
| Pre-existing repo state | ✅ 2 tracked files already modified + 25+ untracked orphan drafts — **left untouched** (defensive `git add`, no `-A`) |

---

## 2. Briefing triage — all three vpstier items rejected

| # | Item | Verdict | Reason |
|---|---|---|---|
| 1 | A permanently excluded European dedicated-hosting merchant's production server offline 3 days after a boot-disk swap, no ETA, no out-of-band access (r/VPS `1xslvbf`) | **REJECTED — hard-banned merchant + off-shape** | The merchant is a permanently excluded brand, so its name must not appear in the outline (pitfall #53 — "in `providers.json`" is NOT a safe harbour). Independently: the subject is a **dedicated server**, not a VPS. Body was fetched via the Reddit Atom route (HTTP 200, 3,407 B — pitfall #56) so the facts are known, but the topic is unusable either way. |
| 2 | A gaming host's 2GB KVM at $1.83/mo first year; price ladder $87.96 → $43.99 → $21.99 (LowEndBox 2026-11-11) | **REJECTED — captured by a published article** | The same merchant's renewal cliff (2GB Ryzen at $2/mo month 1 → $8/mo renewal, a 4× markup) is already the worked example inside the live `vps-pricing-trap-guide-2026` article, naming the brand in 4 places including a price-table row. Also not in `providers.json`. |
| 3 | A 14-location budget host at $2.39/mo for 4GB KVM/NVMe Gen4 (LowEndBox 2026-11-09) | **REJECTED — non-whitelisted + no dated hook** | Not in `providers.json`. No dated incident, no failure mechanism — a plain product listing. |

**→ zero usable stars ⇒ variant-13.** Substitute sourced via a `when:` date-window GN RSS sweep (pitfall #54) and body-fetched from the vendor's own disclosure.

---

## 3. Fact bundle — every row body-fetched this run

| Source | URL | Code / size |
|---|---|---|
| **Vendor incident report (PRIMARY)** | `blog.railway.com/p/incident-report-october-security-incident` | 200 / 108,389 B · `datePublished` 2026-11-10T14:00:00.000Z · "Last updated: November 10, 18:02 UTC" |
| Vendor preliminary report | `blog.railway.com/p/preliminary-report-october-security-incident` | 200 / 78,972 B · 2026-10-22 |
| Vendor first disclosure | `blog.railway.com/p/security-disclosure-wednesday-october-21st` | 200 / 36,509 B · 2026-10-21 |
| Vendor remediation runbooks ×5 | `blog.railway.com/p/security-disclosure-recommendation-*` | 200 each (40-51 KB) · 2026-10-22 |
| Independent #1 | The Hacker News — "Railway Says Stolen Customer AI Keys Led to $740,000…" | 200 / 174,644 B · 2026-11-11 |
| Independent #2 | Wiz — "\"Black October\" for AI Developer Platforms" | 200 / 454,513 B · 2026-10-30 |
| Industry context | `railway.com/pricing` | 200 / 297,474 B |
| Affiliate live pricing | `racknerd.com` + `racknerd.com/specials` | 200 / 34,042 B + 87,951 B |
| Corroborating cluster | 20+ outlets, titles + dates via GN RSS | BleepingComputer, TechRadar, Cloud Computing News, CyberSecurityNews, iTnews, MLQ.ai, Mezha.net, 2-Spyware, GBHackers, The 420.in, Business Upturn, news.lavx.hu, FourWeekMBA, Meteora Web, BigGo Finance |

**Key figures (all traced to the vendor primary):** $740,000 unauthorized spend · ≤1.85% / ~100,000 workspaces (upper bound by the vendor's own statement) · 353 build histories read · 1,852 linked-account tokens reset · 8 providers asked to revoke at 09:25 UTC Oct 21 · entry point 07:28 UTC Oct 20 (previously unknown build-infra vulnerability, partial filesystem-isolation escape) · detection 13:58 UTC Oct 20 · full eviction 09:24 UTC Oct 21 · decryption window 04:42→07:14 UTC Oct 21 (2h32m) · account swarm began Oct 18 · builds restored 22:49 UTC Oct 22 · new signups paused Oct 22 19:06 → reopened Nov 2 · 6-provider refund matrix (2 auto-refund, 2 case-by-case, 1 pending, 1 no-refund-policy) · **Oct 26 "unable to refund" → Nov 10 backstop reversal**.

---

## 4. Gate results

| Gate | Result |
|---|---|
| Freshness | ✅ vendor report 2026-11-10 (d-2); 20+ outlet cluster 11-10 → 11-12 (d-0/d-1/d-2); cluster still moving |
| Body-verified | ✅ vendor primary + 2 vendor follow-ups + 5 vendor runbooks + 2 independent primaries, all parsed |
| Banned merchant | ✅ 0 occurrences — described by category only, including inside the §1a triage row |
| Whitelist | N/A — non-merchant subject (variant-10); article recommends only whitelisted providers |
| Published-angle collision | ✅ cleared against 3 neighbours (§5) |
| Queued-outline collision | ✅ cleared against 3 neighbours (§5) |
| Slug uniqueness | ✅ 0 hits on disk / `published[]` / `drafts[]` / `recent_topics[]` |
| Title / description gate | ✅ 47/60 and 148/155, Python `len()` on the final strings |
| CJK | ✅ 0 in the outline file |
| CTA count | ✅ 8 RackNerd placements, all `aff=16299` |
| Cross-links | ✅ 8 targets — 6 live URLs verified on disk, 2 queued outlines flagged publish-time-only (no dead hrefs) |
| Body-grep-0 | ✅ `railway`, `740,000`, `distillation`, `token spend`, `secret store`, `llmjack`, `build system`, `isolation escape`, `mcp server`, `pentest` → **0 hits** across `src/pages/blog/` + `src/pages/vps/` |

---

## 5. Collision discrimination (cleared explicitly, not assumed)

| Neighbour | Axis | Discriminator |
|---|---|---|
| `dreamhost-breach-2026-password-reuse-vps` (published 11-02) | secret type | **human passwords** (email/FTP/SFTP) vs **machine AI-provider keys** |
| | mechanism | third-party software vuln in a file-manager server vs **isolation escape in a build path** + trusted-client scope failure |
| | cost dimension | none vs **$740,000** + refund-negotiation matrix |
| `januscape-kvm-escape-vps-security-2026` (queued 07-16) | escape layer | KVM **guest-to-host** escape vs **platform build-path** filesystem-isolation escape |
| | code owner | hypervisor vendor vs PaaS vendor |
| `hosting-account-suspension-blast-radius-2026` (queued 11-02) | blast-radius type | **account-level** (one complaint → whole account dark) vs **secret-level** (one key → unbounded metered balance) |
| | trigger actor | provider-initiated legal action vs external threat actor |
| `vps-pricing-trap-guide-2026` (published) + briefing item #2 | axis | **price** (intro vs renewal) vs **credential blast radius** — and briefing item #2 is the *same story this site already published* ⇒ capture, not merely overlap |

---

## 6. Pitfalls encountered this run

1. **Pitfall #35 (re-confirmed)** — `jobs.json` reported `last_status: error` for the briefing with the full report text wrapped in a `RuntimeError:`. The briefing had actually **succeeded**; only the delivery wrapper failed. Reading the status field alone would have produced a false "briefing failed" adjudication. The report content was read from the output file.
2. **Pitfall #43 (re-tripped and fixed)** — the first draft of the §1d fact table quoted the weekly strategy report's own risk label verbatim, which is **Chinese** — 7 CJK glyphs in the outline. Fixed by paraphrasing into English and attributing it. Caught by the CJK regex gate before commit.
3. **Pitfall #29 (re-tripped and fixed)** — the first draft's self-check row described the language-policy check by printing the **deprecated language-prefix path literal**, producing 1 hit in its own zero-check. Fixed by phrasing the row generically. Second canonical recurrence in this exact form.
4. **Pitfall #44 (avoided)** — the title/desc gate was run as a **candidate loop** before the outline was written (6 title candidates, 7 desc candidates), not asserted afterwards. The first desc candidates all failed (173/162/166/173 chars); the chosen one passes at 148. The declared numbers in the file were then re-verified by **re-parsing the written file** rather than trusting the earlier computation.
5. **Pitfall #56 (re-confirmed)** — the Reddit `.rss` route again returned the full post body (3,407 B) for briefing item #1, which `.html`/`.json` cannot. Used to **know** the facts and then **reject** the topic — a body fetch that prevents a wrong pick is still worth doing.
6. **Pitfall #50 (applied)** — the *preliminary* report (Oct 22) contains **zero** occurrences of `740` and no refund-policy section. The $740,000 figure exists **only** in the Nov 10 final report. Quoting the preliminary report for that number would have been an anachronism; the outline cites the final report and the Nov 11 independent article instead.
7. **Pitfall #42 (applied)** — every vendor-naming fact is quoted from the vendor's own sentence rather than paraphrased. E.g. the scope-mismatch sentence and the "distributed transfer stations for use for distillation" sentence are reproduced exactly, because a paraphrase of either collapses a material distinction.
8. **Pitfall #51 (applied)** — the affiliate's **live** entry price ($2.24/mo) was verified against `racknerd.com`, not taken from the site's own `/vps/racknerd/` page, which is **stale at $1.99/mo** in five places. The stale figure is excluded from the outline and **flagged for the user** instead of being silently used or silently edited.
9. **Pitfall #49 (applied)** — the briefing's own framing ("no ETA, no compensation", "3 days down") was checked against the fetched body, which is in **Spanish** — so the outline does not paraphrase a non-English source into an English claim it cannot support. The topic was rejected on independent grounds (banned merchant + off-shape subject), so no translation was needed.

---

## 7. Flagged for the user (NOT fixed from a daily-outline slot)

1. **`src/pages/vps/racknerd.astro` price is stale** — renders "$1.99/mo" in the `<title>`, meta description, intro paragraph, pros list and CTA area, while the live site says **$2.24/mo**. Needs a separate price-refresh commit. Not edited here.
2. **`published[]` ∩ `drafts[]` overlap = 2 slugs** (`best-vps-deals-codes-2026`, `webdock-vps-review-2026`) — duplicate-queue landmine for the publish cron.
3. **Two live articles assert an unsupported Black Friday launch window** (re-flagged; the Nov 9 piece is internally contradictory).
4. **The provider-page pipeline is still dead** — 69 `/vps/` pages, only 18 with any impressions; homepage absorbs 76.0% of impressions at position 84.8; two provider-review jobs have not run since June.
5. **Cross-link timing** — 2 of the 8 cross-links point at *queued outlines* (`hosting-account-suspension-blast-radius-2026`, `januscape-kvm-escape-vps-security-2026`). They are **not** live URLs. The writer must add those anchors only when those articles exist, or reference them by title in prose without an href.

---

## 8. GSC context (live, 90d, `sc-domain:vpstier.com`)

- 1,185 impressions / 1 click across 60 pages. The **homepage absorbs 901 (76.0%) at avg position 84.8**.
- Every head term sits at **position 74-95**: "best vps for ai agents" (71 imp, pos 74.4), "best vps provider" (58, pos 84.1), "best vps" (56, pos 83.4), "vps hosting review" (36, pos 92.6).
- The pages that *do* rank are provider reviews at **pos 3.6-7.4** (aliyun 43 imp / 4.9, lightnode 15 / 3.9, hosthatch 11 / 4.1, scaleway 11 / 6.9).
- **Why this shaped the outline:** the hub-gap is structural, so a daily slot must not force another listicle. A *specific-mechanism* incident piece with a concrete buyer checklist is the right unit here — it targets the "reliable vps" / "vps hosting review" intent class through a mechanism no other site covers, and it carries the affiliate placement honestly (a rooted KVM VPS genuinely answers the blast-radius question).
