# Run Record — vpstier-daily-outline — 2026-09-18

**Cron:** `5fd2a36f2dc4` (vpstier-daily-outline, `45 9 * * *`)
**Run date:** 2026-09-18
**Artifacts written:**
- `drafts/outline-2026-09-18-vpstier-daily.md` (28,319 bytes)
- `drafts/run-record-2026-09-18-vpstier-daily-outline.md` (this file)
- `drafts/state.json` (one `drafts[]` append + `publish_notes` append + field updates)

---

## 1. Inputs consumed

| Input | Path | Status |
|---|---|---|
| Daily industry briefing | `/root/.hermes/cron/output/3ea88f8bb2d0/2026-09-18_08-02-51.md` | ✅ SUCCEEDED (10 items, 2 vpstier VPs, all links HEAD/G verifies 200) |
| GSC morning signal | `/root/.hermes/cron/output/5570fe2cffa6/2026-09-18_07-00-44.md` | ✅ read (vpstier 30d 0 clicks / 365 impressions; 7d 0 / 62, avg rank 85.2) |
| Whitelist | `src/data/providers.json` | ✅ 65 providers, 0 excluded-merchant hits |
| State | `drafts/state.json` | ✅ 83 published / 52 drafts before append; `last_run` was 2026-09-17 |
| Live VPS feed | `lowendbox.com/feed/` | ✅ HTTP 200, 20 items retrieved |
| Primary article body | `lowendbox.com/blog/when-data-sovereignty-rules-bite-you-hard-...` | ✅ HTTP 200, 141,786 bytes |
| Trade-press detail body | `w.media/aws-cant-recover-resources-and-data-stored-in-uae-region-...` | ✅ HTTP 200, 233,074 bytes |
| Corroborating headlines | Google News RSS (2 queries) | ✅ 48 + 26 items |

---

## 2. Variant classification

**Variant: (4)-equivalent handling with a variant-12 precedent — "briefing SUCCEEDED but every briefing item is a stale re-surface; freshest usable story sits outside the briefing in the same feed".**

Chosen because:
- The briefing returned HTTP 200 with 10 items — so the literal variant-4 trigger ("briefing FAILURE") does **not** fire.
- But all three vpstier-relevant briefing items failed a hard gate: item #1 is a **3rd-consecutive re-surface of an already-captured story** (the variant-12 staleness/capture rule), item #2 is a **vendor self-promotion listicle re-surfaced from yesterday** (no dated hook), item #3 is **directly captured by the queued Namecheap outline**.
- That combination is a new shape in the variant table: **"briefing SUCCESS, zero usable stars, and the substitute is verifiably fresher than anything the briefing offered."** Closest existing handle is variant-12's spirit (reject the stale re-surface outright, do not rescue via variant-7) extended to *all* items rather than one.

**Recommended variant-table addition for the canonical reference:** a variant-13 row, *"Briefing SUCCESS, ALL vpstier items are stale re-surfaces/captured (zero usable stars) → banned-pivot to the freshest dated substitute outside the briefing; log the re-surface count per item."* Today's item #1 hit **3 consecutive runs** (09-16, 09-17, 09-18) — worth a standing note in the reference.

---

## 3. Capture-check results (search BOTH `published[]` and queued-outline dated-hook origins)

| Briefing item | Capture mechanism found | Verdict |
|---|---|---|
| ⭐ Contabo Back-to-School promo (Cybernews) | (a) queued outline `cheap-vps-back-to-school-promo-eval-2026` (09-16) consumed it as its dated hook; (b) variant-7 walled-primary (Cybernews 403); (c) same-story-different-URL on 09-17 | **CAPTURED — 3rd re-surface. Rejected.** |
| ⭐ Hostinger "14 best VPS" listicle | (a) `hostinger-review` published; (b) `best-asia-pacific-vps-2026` published covers Hostinger's position; (c) re-surfaced from 09-17 where it was also rejected | **REJECTED — vendor self-promotion, no dated hook** |
| Namecheap facility outage (~1M sites) | queued outline `namecheap-outage-dns-email-vps-resilience-2026` (08-16) covers the same provider/outage pattern | **CAPTURED — rejected** |

**Capture-check scope note:** today's check searched `published[]` slugs, queued `drafts[]` slugs, **and** the queued outlines' dated-hook origins (per the 2026-09-09 scope verification). The Contabo entry only resolved via the third scope — a plain slug search would have missed it.

---

## 4. Substitute selection + freshness verification

**Selected:** LowEndBox editorial *"When Data Sovereignty Rules Bite You Hard: Some AWS Data in UAE, Bahrain is Gone for Good"* (raindog308, **2026-09-17 11:00 UTC**, 1 day old).

**Freshness gate:** ✅ 1 day. Well inside the 8-day gate.

**Why fresher than the briefing's own items:** the briefing's vpstier items are dated 09-16 (Contabo) and undated (Hostinger listicle). The substitute is dated **09-17** and is the top item in the same `lowendbox.com/feed/` the briefing reads.

**Stale-rehash rule applied (pitfall from 2026-09-16):** the selected story carries an explicit in-body date chain (Feb 2026 war start → Mar 1 2026 AZ damage → Mar 2 2026 facility confirmation → Apr 30 2026 AWS relocate advisory → Sep 15 2026 AWS recovery-exhausted statement). The **event year is current** and the *news* (the September 15 admission) is 3 days old. This passes; it is **not** a 15-month-old thread like the 2026-09-16 CloudCone rejection.

**Non-merchant / non-whitelisted check:** the dated hook is an **event about a hyperscaler**, not a merchant recommendation. The article's **entire recommendation set is whitelisted providers** (24 multi-DC whitelisted providers cited in §6, RackNerd as the CTA anchor). No provider-page requirement is triggered — same structural basis as variant-10 (non-merchant subject) and variant-9 sub-mode (labelled context).

---

## 5. Source verification detail

### Content-serving vs blocked (2026-09-18 sandbox reality)

| Source | HTTP | Bytes | Usable |
|---|---|---|---|
| lowendbox.com/blog/* (article) | 200 | 141,786 | ✅ full body |
| w.media/* (trade press) | 200 | 233,074 | ✅ full body |
| Google News RSS (2 queries) | 200 | — | ✅ 48 + 26 items |
| theregister.com | 200 | 2,101 | ❌ "Are we human?" interstitial |
| datacenterdynamics.com | 403 | 5,913 | ❌ Cloudflare "Just a moment..." |
| arstechnica.com | 200 | 2,103 | ❌ JS CAPTCHA |
| helpnetsecurity.com (2 URL shapes) | 404 / 200 | 62,822 | ❌ 404 shell |
| tomshardware.com (guessed slug) | 200 | 1,251,151 | ❌ "Page not found" shell |
| cybersecuritynews.com | 403 | 75,193 | ❌ |
| gadgetreview.com | 403 | 5,903 | ❌ |
| blocksandfiles.com (guessed slug) | 200 | 2,101 | ❌ interstitial |
| channelregister.co.uk | 522 | 16 | ❌ |
| itpro.com (guessed slug) | 404 | 657,966 | ❌ |

**Two independent body-fetchable sources were obtained** (LowEndBox editorial + W.Media trade press), which is sufficient: the LowEndBox piece supplies the mechanism/thesis and the W.Media piece supplies the AZ-level technical detail and the verbatim AWS statements. **No fabricated content was used; every quote in the outline traces to one of these two fetched bodies.**

**Wayback NOT attempted** (pitfall #23 — steady-state unreachable, 7+ consecutive runs).
**Cybernews NOT retried** (pitfall #24 — permanently bot-blocked).
**LET `lowendtalk.com` NOT attempted** (pitfall #25 — Cloudflare walled).

---

## 6. Self-check (brand / language / structural)

All brand, language and structural checks ran via `execute_code` + `subprocess.run` (the `terminal` tool is Tirith-blocked for this cron per pitfall #20).

| Check | Method | Result |
|---|---|---|
| Excluded-merchant brand token in `outline-2026-09-18-vpstier-daily.md` | Python `str.count` (case-insensitive) over the full file | **0** ✅ |
| Excluded-merchant brand token in this run-record | same | **0** ✅ |
| Excluded-merchant brand token across the whole draft tree + `src/` | recursive case-insensitive scan | **0 in today's artifacts** ✅ |
| Excluded-merchant token in `providers.json` | list scan | **0** ✅ |
| Excluded-merchant token inside fetched source bodies (pitfall #16) | scan of both fetched bodies | **0** ✅ |
| CJK characters in either document | standard CJK-range regex (pattern deliberately not written literally — pitfall #28) | **0** ✅ |
| CJK in the verbatim upstream quotes (pitfall #17) | all upstream quotes are English-only; none pasted as CJK | **0** ✅ |
| Deprecated language-prefix path in prose (pitfall #18) | substring scan | **0** ✅ (phrased generically) |
| Title length | Python `len()` | **58** (gate 30-60) ✅ |
| Description length | Python `len()` | **147** (gate 70-155) ✅ |
| §0 header gate label matches rendered length (pitfall #22) | string compare against `len()` | ✅ 58 asserted / 58 rendered |
| Slug collision | grep across `state.json` + `src/pages/blog/` listing | **0 collisions** ✅ |
| Cross-link targets exist on disk | compared every path against `ls src/pages/blog/` | ✅ 7 published paths all present; 2 queued paths match `drafts[]` slugs |

**Self-check-line pitfalls avoided this run:**
- The §6 row describing the excluded-merchant check is written as **category language** ("excluded-merchant brand token"), never as a literal brand string — avoids pitfall #2 (writing the brand in the self-check row trips its own zero rule).
- The §6 row describing the CJK check does **not** paste the regex literal with CJK glyphs — avoids pitfall #28 (regex-literal CJK self-reference false positive).
- The deprecated-language-path check is phrased generically in §6 rather than writing the literal path — avoids pitfall #18.

---

## 7. state.json write plan (two-commit pattern)

```python
# Draft entry (drafts[] append) — vpstier publish_notes is a STRING (pitfall #3)
draft = {
  "date": "2026-09-18",
  "slug": "sovereign-cloud-data-loss-2026-offsite-backup",
  "title": "Sovereign Cloud Data Loss 2026: When Multi-AZ Isn't Enough",
  "title_en": "Sovereign Cloud Data Loss 2026: When Multi-AZ Isn't Enough",
  "description_en": "Two AWS regions hit by war damage can never be restored. What VPS buyers must copy off-site, and the 3-2-1 rule that survives any provider failure.",
  "status": "outline_pending_publish",
  "variant": "variant-4-equivalent (briefing SUCCEEDED but ALL vpstier items are stale re-surfaces / captured — zero usable stars; banned-pivot to the freshest dated substitute outside the briefing)",
  "archetype": "geopolitical failure-domain / data-sovereignty buyer-guide (3-2-1 off-site-copy guide; failure domain LARGER than the provider and LARGER than the region)",
  "outline_file": "drafts/outline-2026-09-18-vpstier-daily.md",
  "run_record_file": "drafts/run-record-2026-09-18-vpstier-daily-outline.md",
  "en_astro": "src/pages/blog/sovereign-cloud-data-loss-2026-offsite-backup.astro",
  "zh_astro": None,
  "h2_count": 10, "faq_count": 5, "cta_placements": 8, "cross_links": 9,
  "primary_affiliate": "RackNerd",
  "providers_featured": ["RackNerd"],
  "hot_topic_source": "LowEndBox 2026-09-17 (raindog308) - AWS me-south-1 Bahrain + mec1-az2 UAE recovery exhausted; multi-AZ defeated by a correlated geopolitical failure domain; corroborated by Reuters/WSJ/CNBC 09-15, TheRegister/DCD/Ars 09-16, HelpNetSecurity/TechSpot 09-17 (Google News RSS resolved 2026-09-18); body-fetchable detail source W.Media 2026-09-17"
}
```

- `publish_notes`: vpstier is a **STRING** — append `\n`-joined (date marker + natural-language title fragment; the kebab slug intentionally NOT in the appended line per pitfall #4).
- `drafts_count` updated **AFTER** the append, in the same Python operation (pitfall #6).
- `last_run` set with a **separate explicit assignment** (pitfall #7).
- `json.dump(..., ensure_ascii=False)` to preserve Unicode.
- **Two-commit pattern:** commit 1 = the two markdown files; commit 2 = `drafts/state.json`. Never `git add -A` (pitfall #11).

---

## 8. Expected state.json health-check delta

Per the state.json health-check table: **vpstier single-entry append ≈ 50-80 insertions / 4 deletions** (larger than converter-epub's ~49 because the publish_notes line carries the variant description + datapoints). A delta **>100 insertions** would signal a state-reset or an `ensure_ascii=True` Unicode-escape regression — watch for that after the write.

---

## 9. Novel learnings this run (candidates for the canonical reference)

1. **New variant shape worth adding as variant-13:** *"Briefing SUCCESS, zero usable stars because ALL vpstier items are stale re-surfaces or captured → banned-pivot to the freshest dated story outside the briefing, and log the per-item re-surface count."* The existing table jumps from variant-12 (a 2-star hybrid rejection) straight to no row — today shows the case where **every** item fails, not just two.
2. **Re-surface counter discipline:** the Contabo back-to-school item has now been re-surfaced **3 consecutive runs** (09-16, 09-17, 09-18). The canonical reference already documents the *first* re-surface; the **3-run streak** is the new fact and it argues for a standing "captured" marker rather than re-adjudicating each day.
3. **`lowendbox.com` article bodies are fetchable even though `lowendtalk.com` is Cloudflare-walled** — the LEB *blog* article URL returned 141,786 bytes at 200 OK today, while the LET forum remains 403. The canonical pitfalls list walls `lowendtalk.com/discussion/*`; it should **explicitly carve out `lowendbox.com/blog/*` as the fetchable alternative**, since the two are easy to conflate and LEB is the site's top VPS-news feed.
4. **W.Media (`w.media`) is a new body-fetchable data-center trade-press fallback** when The Register / DCD / Ars / Tom's Hardware / Help Net Security are all walled or CAPTCHA'd. It returned the **deepest technical detail** of the whole story cluster (explicit `mec1-az1/az2/az3` AZ identifiers, verbatim AWS statements, the full month-by-month timeline). Worth adding to the walled-primary-alternatives priority list alongside HostAdvice (added 2026-09-16).
5. **Geopolitical failure domain is a genuinely new archetype layer** — it sits *above* the existing Operational-resilience sub-members (workload / control-plane / financial / single-DC) because it is the first case where the failure domain exceeds **both** the provider **and** the region, which **inverts multi-AZ advice** rather than restating it. It also functions as the **layer-1 (data-at-risk) deep-dive** of the buyer-side 5-layer series.

---

## 10. Handoff to the article-writing cron

- **Publish slot:** 2026-09-21 (Monday — vpstier publishes Mondays only since the 2026-08-28 HCU pause).
- **Awaiting:** user review of the outline → reply `publish` → write the full Astro page at `src/pages/blog/sovereign-cloud-data-loss-2026-offsite-backup.astro`, then `npm run build` → git push → `wrangler pages deploy dist --project-name=vpstier-com`.
- **Pre-deploy HCU audit** (≥800 unique words, ≥2 real artifacts, first-person voice, "Last verified 2026-09-21" stamp, no comparison-crutch template) is specified in §5 of the outline.
- **Brand discipline:** no excluded merchant anywhere; RackNerd featured as the CTA anchor with `https://my.racknerd.com/aff.php?aff=16299` across 8 placements.
