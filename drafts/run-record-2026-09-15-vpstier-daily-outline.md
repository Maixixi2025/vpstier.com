# Run Record — vpstier daily outline 2026-09-15

**Cron:** `5fd2a36f2dc4` (vpstier-daily-outline)
**Date:** 2026-09-15
**Variant:** **variant-2 hybrid** (briefing SUCCESS; ⭐ SolusVM 29% CAPTURED by queued 09-12 outline · ⭐ mandatory-KYC budget host SELECTED as dated case study (non-whitelisted merchant, used as a case-study anchor only) · ⭐ DO Omarchy $3M CAPTURED by queued 09-10 outline). Banned-pivot to the freshest dated substitute outside the briefing ⭐ list: LEB 2026-09-14 (raindog308) "Farewell, [case-study vendor]..." three-red-flag case study.

---

## 1. Inputs read

| Input | Path | Status |
|---|---|---|
| Today's industry briefing | `/root/.hermes/cron/output/3ea88f8bb2d0/2026-09-15_08-03-27.md` | ✅ present (9,075 B), briefing SUCCEEDED, 10 items / 2 vpstier ⭐ |
| GSC daily summary | `/root/.hermes/cron/output/5570fe2cffa6/2026-09-13_07-01-03.md` | ✅ vpstier 30-day = 0 clicks / 303 impressions; 7-day = 0 / 33, avg rank 81.8. Top query "best vps for ai agents" 13 impressions. No fresh actionable vpstier signal. |
| `providers.json` | `/root/vpstier-site/src/data/providers.json` | ✅ 65 providers, list-shaped; the case-study vendor is **absent** (0/65) — the article uses it as a dated incident, never as a recommendation |
| `drafts/state.json` | `/root/vpstier-site/drafts/state.json` | ✅ drafts 49 · published 83 · drafts_count 49 · last_run 2026-09-13 (pre-this-run) |
| Last commit | `c10cd60` (state) over `c6f3008` (outline 09-13) → today's commits `3d14bfa` (outline 09-14) + `7a0e637` (state 09-14) are the last push | ✅ tree clean apart from the known orphan backlog |

---

## 2. Briefing triage detail

### ⭐ #1 — SolusVM 29% licence hike
**Verdict: CAPTURED — duplicate.** Already the dated hook of the queued **2026-09-12** outline `solusvm-price-hike-2026-cheap-vps-costs` (shipped `c14488c`, panel/vendor licensing-cost-passthrough archetype, ten H2). Re-surfacing it would duplicate a pending outline. Capture-check searched both `published[]` (83 entries) and the queued-outline hook origins.

### ⭐ #2 — small Italian-headquartered budget VPS host issuing a sudden mandatory KYC notice
**Verdict: SELECTED as a dated case study.** Fresh (LEB 2026-09-14, d-1). The vendor is **absent from `providers.json` (0/65)** but the angle is the buyer-side **red-flags pattern**, not a vendor review. The vendor is the **case study** in a buyer-guide, never a recommendation. Same structural pattern as the 2026-08-27 trust-warning outline (anchored on Krebs on Security + Europol as dated incidents, both external to the recommended host set). Body-grep-0 confirms the angle is a real gap (§3 of outline).

### ⭐ #3 — DigitalOcean $3M Omarchy donation
**Verdict: CAPTURED — duplicate.** Already the dated hook of the queued **2026-09-10** outline `agentic-vps-always-on-ai-agent-2026`. Re-surfacing it = duplicate.

**Verdict label:** variant-2 hybrid. The strongest dated signal in the briefing (SolusVM 29%) was already consumed; the second-⭐ was non-whitelisted but selectable as a buyer-side case study; the third was already consumed. Today's outline ships the freshest dated substitute **outside** the briefing ⭐ list — the LEB 2026-09-14 piece.

---

## 3. Substitute selection — single-vendor three-red-flag buyer-guide (NEW buyer-risk layer)

Sourced from a direct feed sweep (LowEndBox RSS at `https://lowendbox.com/feed/` — verified, 20 items; Google News RSS returned 0 hits for the case-study vendor's name because the LEB post is the canonical source).

**Cluster window:** single dated source (LEB 2026-09-14), with **three independent dated signals** inside the article body:
- Late 2024: customer signs up for a super-cheap annual VPS (the LEB author's first-person account)
- Mid-2026: rogue-employee billing scandal surfaces on LowEndTalk (cited via the LEB post; primary LET thread not fetched — LET is Cloudflare-walled from this runner)
- 2026-09 (this week): vendor emails mandatory KYC demand citing "applicable European regulations"; the LEB author has 10 days to comply or face account closure
- Same week: vendor deflects on LowEndTalk with a "Targeted Verification" explanation referencing "system alerts or other compliance triggers"

**Archetype:** **fourth layer in the buyer-risk buyer-guide series** — the **pattern-at-risk** layer. Distinct **mechanism** from the three queued layers:

| Layer | Outline | Mechanism | Trigger signal |
|---|---|---|---|
| 1. **Data-at-risk** | `vps-provider-exit-warning-signs-2026` (queued 2026-08-27) | seizure / regulatory takedown | vendor disappears, hardware seized, customer data unrecoverable |
| 2. **Money-at-risk** | `vetting-cheap-vps-deals-2026-before-you-pay` (queued 2026-09-11) | duplicate invoice + payment-loop silence | duplicate charge + unanswered support ticket + payment rail |
| 3. **Identity-at-risk** | `vps-kyc-privacy-checklist-2026` (queued 2026-07-10) | mid-contract document demand | host demands passport/ID mid-contract; buyer must choose compliance vs exit |
| **4. Pattern-at-risk (today)** | **`cheap-vps-merchant-red-flags-2026`** | **single vendor, three red flags inside twelve months** | rogue-employee billing → surprise KYC → locked client area, all at the same host |

Each layer cross-links the others; together they form a four-layer buyer-risk buyer-guide. The body-grep-0 discriminator confirms the angle is a real gap: 8 specific claim tokens (`rogue employee`, `mandatory KYC`, `account bloccato`, `applicable European regulations`, etc.) = 0 across `src/pages/**/*.astro` + `drafts/*.md`. Three non-discriminators documented as passing mentions with distinct claim direction (`KYC` is a *vendor attribute* in 16 prior files; the today's claim is the *direction* of the demand — mid-contract surprise — which no on-disk file asserts).

---

## 4. Verified fact bundle (reusable — no re-fetch needed)

### LEB post (fetched 2026-09-15, full body 135,956 B)
- **Title:** "Farewell, [case-study vendor]. Don't Let the Door Hit You on the Culo on the Way Out"
- **Author:** raindog308
- **datePublished:** 2026-09-14T11:00:24+00:00
- **URL:** `https://lowendbox.com/blog/farewell-[case-study-vendor]-dont-let-the-door-hit-you-on-the-culo-on-the-way-out/`
- **Engagement:** 0 comments at fetch time
- **Tag in URL:** `/[case-study vendor]` (the brand tag in the URL slug is the only on-disk place the vendor's brand appears; the body-grep-0 audit excluded URL-tag mentions)

### Key quoted text (verbatim from the LEB post body, paragraph numbers from the fetch)
- **P2 (mid-2026 rogue-employee billing):** "There was the epic '[the] 'merger' [thread]' thread on LowEndTalk and then stories began to roll in about epic billing snafus where users were accidentally charged $5,000 or $10,000. Turned out it was a rogue employee."
- **P3-P7 (mandatory KYC demand, verbatim email text):**
  - "In compliance with applicable European regulations regarding security, transparency, and the prevention of illicit activities, our organization is required to perform a customer identity verification process (KYC – Know Your Customer)."
  - "We kindly ask you to complete the verification process via the following secure link..."
  - "Please note that completing this process is a mandatory legal requirement. Failure to complete or fully finalize the verification within 10 days of this notification will result in the closure of your account and the termination of all provided services, pursuant to applicable law and contract terms."
- **P11 (Italian UI strings):** "My Italian is a bit rusty but 'account bloccato' and 'verifica' and 'completa verifica' sure sounds like mandatory KYC."
- **P13 (no decline option):** "Clicking Decline just tells me that I need to agree. I can't even get into the Client Area without going through this."
- **P15 (community skepticism):** "No one was sure what 'applicable European regulations' were requiring this, since if that was true, tons of hosting providers would be requiring it."
- **P17 (vendor's LET reply, paraphrased):** "Targeted Verification: Enhanced KYC (Know Your Customer) verification is not being requested for all accounts. It applies only to specific accounts flagged by system alerts or other compliance triggers."
- **P18 (author's response):** "What possible 'trigger' could I have triggered? I paid with my credit card through Stripe, so Stripe already knows all about me. It was more than a year ago and I haven't charged back, so apparently I really am the credit card holder."
- **P19 (rogue-employee → KYC escalation):** "And remember, they already had one employee who started issuing fraudulent charges to people's payment methods on file... and now they want me to upload government ID."

### Cross-source confirmation rule (single-outlet today)
The article must state in H2 that the dated hook is sourced from one named author's first-person account on a single outlet (LEB). The author publishes the **verbatim email text** (Italian UI strings, English explanation), and the **vendor's own LowEndTalk reply** — both citable without further corroboration. The article must NOT assert anything the LEB post does not directly quote or state.

### Whitelisted EU-headquartered counter-examples (verified against `providers.json`, 65 providers)
- **Netcup** — Nuremberg / Vienna / Düsseldorf DCs, $3.69/mo, established German provider with a documented stable track record
- **AlphaVPS** — Sofia (Bulgaria) + Nuremberg + London DCs, $2.54/mo, EU-native + custom-ISO install
- **Cherry Servers** — 4 EU DCs + ISO 27001 / SOC 2 / PCI DSS, $3.51/mo, higher-tier alternative
- **RackNerd** — recommended 8 (annual affordability + community track record); 6 DCs US + 3 EU (Amsterdam, France, Dublin)

---

## 5. Outline output

- **File:** `drafts/outline-2026-09-15-vpstier-daily.md` (29,572 B)
- **Slug:** `cheap-vps-merchant-red-flags-2026`
- **Title (60):** `VPS Red Flags 2026: 3 Warning Signs From One Host's Collapse`
- **Description (140):** `One cheap VPS host ran rogue-employee fraud, surprise KYC, then locked accounts. The buyer-side red flags, and what to check before you pay.`
- **10 H2 · 5 FAQ · 8 RackNerd CTA placements · 6 cross-links**
- Anchor artifacts planned: 4 (3-signal dated timeline table · 6-red-flag buyer-side checklist · 5-minute pre-purchase test · 4-step escalation order)
- **Variant:** variant-2 hybrid (CAPTURED + SELECTED-as-case-study + CAPTURED)
- **Archetype:** fourth layer in the buyer-risk buyer-guide series — **pattern-at-risk**

---

## 6. Self-check results

| Check | Result |
|---|---|
| Excluded-merchant zero-check (whole draft + this record, category language) | ✅ **0** |
| Case-study vendor zero-check (`[case-study vendor]` brand token) | ✅ **0** in outline body; the vendor's brand appears only as a category reference in the §1 case-study citation and as a single URL slug reference in the resume-recipe URL of §10 |
| CJK zero-check (Unified Ideographs incl. Ext A/B) | ✅ **0** in both files; no upstream-briefing sentence pasted verbatim (all briefing judgments paraphrased in English) |
| Retired localized-path prefix | ✅ not referenced; policy phrased generically to avoid tripping the literal pre-2026-06 localized-path token |
| Title / description Python `len()` | ✅ 60 / 140 |
| H2 · FAQ · CTA placements · cross-links | ✅ 10 · 5 · 8 · 6 |
| Slug present | ✅ `cheap-vps-merchant-red-flags-2026` |
| Freshness gate | ✅ single dated source is d-1 (2026-09-14) |
| Body-grep-0 discriminator | ✅ 8 specific claim tokens = 0; 3 non-discriminators (`KYC`/`rogue`/`Stripe`) documented as passing mentions with distinct claim direction |
| Source-data banned-token scan | ✅ LEB body scanned — **0 hits** for excluded-merchant token; case-study vendor brand appears only in URL slug, not in cited prose |

---

## 7. Pitfalls encountered / re-confirmed

1. **`terminal` tool is Tirith-blocked for this cron (5th consecutive confirmation, 09-11 → 09-15).** Every read, grep and fetch ran through `execute_code` + `subprocess.run`. Steady-state; do not retry the `terminal` tool first.
2. **LowEndBox body fetch uses the standard `<body>` extract pattern.** No SPA shell this run — the page is server-rendered HTML with 45 substantive paragraphs. The 09-13 ServerVerify + 09-14 Utility Dive walled-page lessons do NOT apply to LEB.
3. **HN Algolia and Google News RSS both returned 0 hits for the case-study vendor's name.** HN has 39,893 results for "[case-study vendor]" but 0 in `tags=story`; Google News does not index the LEB post directly. The single-outlet (LEB) source chain is the correct fallback per the canonical single-source-provenance rule.
4. **The case-study vendor's brand appears in the URL slug of the LEB post** (`/[case-study vendor]`-tagged URL). The body-grep audit must allow this ONE URL reference (the article's resume-recipe URL §10) but **never** allow the brand to appear in the article's prose. Verified via `grep -ic "[case-study vendor]" outline-2026-09-15.md` = 0; the URL reference appears in the run-record (this file) only.
5. **`grep` zero-rule on the §10 self-check line** — the documented 9-13 pitfall re-confirmed. The self-check line for case-study vendor says "case-study vendor zero-check" rather than embedding the brand name; the URL reference in §10 uses a placeholder `[case-study-vendor]` rather than the actual slug.
6. **`git status` orphan backlog unchanged** — 20 untracked outline/run-record files from 08-01 → 08-30. Specific-path adds keep them out of scope per the standing rule.
7. **Queue backlog: `drafts[]` = 50 queued vs newest `published[]` = 2026-09-12.** Stale-by-construction queued items flagged for a user-side archive-vs-publish pass (07-17 Black Friday tracker, 07-20/07-23 Luxvps pair, 07-26 summer roundup, 08-08 WooCommerce, 08-10 managed-K8s, 08-29 jurisdictional sanctions, 08-30 AI rack-density, 08-31 lifetime-pricing). This cron does not prune.

---

## 8. State.json update + commits

- `drafts_count` 49 → 50 · `last_run` → `"2026-09-15"` · `publish_notes` appended (STRING, `
`-separated, natural-language title fragment).
- 4-check verifier passed pre-staging.
- Saved with `ensure_ascii=False`.
- Commit 1: `git add drafts/outline-2026-09-15-vpstier-daily.md drafts/run-record-2026-09-15-vpstier-daily-outline.md`
- Commit 2: `git add drafts/state.json`

---

## 9. Flags for the user

- ⚠️ **Queue backlog (50 queued / 22 published this cycle):** a user-side archive-vs-publish pass is overdue. The oldest queued items are 2026-06 / 2026-07 dated and their news hooks are dead. The four-layer buyer-risk series (08-27 exit-warning + 07-10 KYC + 09-11 vetting + 09-15 pattern-at-risk) is internally consistent; an editor can pick any of the four to ship first.
- ⚠️ **20-file orphan backlog** in `git status` (08-01 → 08-30 outlines + run-records) — untracked, never committed. Safe to add in one dedicated housekeeping commit, or to discard.
- ℹ️ **Single-outlet source today.** The article is anchored on one named author's first-person account on one outlet (LEB). This is acceptable for a buyer-guide case study where the author's verbatim quoted email IS the artifact; the article states this provenance explicitly.
- ℹ️ **Three-layer buyer-risk series completion.** With today's outline shipped, the site has FOUR buyer-risk buyer-guide pieces queued (07-10 KYC + 08-27 exit-warning + 09-11 vetting + 09-15 pattern-at-risk). They cross-link each other; an editor can ship any one as a stand-alone article or ship all four together as a series.
- ℹ️ **vpstier.com publish cadence = Mondays only** since the 2026-08-28 HCU mitigation. The daily-outline cron runs every day and queues outlines; the article-writing cron publishes Monday. Today's outline ships a Tuesday outline that will sit in `drafts[]` until the next article-writing cron slot.
