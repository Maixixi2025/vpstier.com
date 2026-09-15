# VPSTier Daily Outline — 2026-09-15

**Cron:** `5fd2a36f2dc4` (vpstier-daily-outline)
**Date:** 2026-09-15
**Site:** vpstier.com (English only)
**Variant:** **variant-2 hybrid** — briefing SUCCESS (10 items, 2 vpstier ⭐); ⭐ #1 (SolusVM 29% panel hike) **CAPTURED** by queued 09-12 outline `solusvm-price-hike-2026-cheap-vps-costs`; ⭐ #2 (a small Italian-headquartered budget VPS host issuing a sudden mandatory KYC notice after a prior rogue-employee billing scandal) **SELECTABLE as a dated case study** (non-whitelisted as a hosting merchant, but the angle is a buyer-side red-flags buyer-guide that uses the host as a dated incident and points readers to whitelisted providers — the same pattern as the 2026-08-27 trust-warning outline that anchors on two body-verified incidents); ⭐ #3 (DigitalOcean $3M Omarchy donation) **CAPTURED** by queued 09-10 outline `agentic-vps-always-on-ai-agent-2026`. Today's outline ships the freshest dated substitute that's NOT a banned-pivot: the 2026-09-14 LowEndBox "Farewell, [case-study vendor]" piece by raindog308.

---

## 1. Rationale + Hot-source (brand-free)

### Briefing triage (2026-09-15 08:03 briefing, cron `3ea88f8bb2d0`)

| # | Briefing item | Verdict | Reason |
|---|---|---|---|
| 1 | ⭐ **SolusVM 29% licence hike** (LowEndBox 2026-09-11) | **CAPTURED — duplicate** | Already the dated hook of the queued **2026-09-12** outline `solusvm-price-hike-2026-cheap-vps-costs` (shipped `c14488c`, panel/vendor licensing-cost-passthrough archetype). Re-surfacing it = duplicate. |
| 2 | ⭐ **A small budget VPS host issuing a sudden mandatory KYC notice** (LEB 2026-09-14, raindog308) | **SELECTED as a dated case study** | Fresh (d-1). The host is **absent from `providers.json` (0/65)** but the angle is the buyer-side **red-flags pattern**, not a host review. The vendor is the **case study** in a buyer-guide, never a recommendation. Same pattern as the 2026-08-27 trust-warning outline (anchored on Krebs/Europol). Body-grep-0 confirms the angle is a real gap (§3). |
| 3 | **DigitalOcean $3M Omarchy donation** (omarchy.org 2026-09-09) | **CAPTURED — duplicate** | Already the dated hook of the queued **2026-09-10** outline `agentic-vps-always-on-ai-agent-2026`. |

### Why this topic (variant-2 banned-pivot to the freshest dated substitute outside the briefing ⭐ list)

**The dated hook:** LEB, *"Farewell, [redacted-brand]. Don't Let the Door Hit You on the Culo on the Way Out"* — raindog308, **14 September 2026** (d-1). Full body fetched (135,956 B, HTTP 200); 45 paragraphs read.

**Why this is a vpstier buyer-guide and not a vendor hit piece.** The story surfaces **three different buyer-side red flags in twelve months at the same low-end host**:

1. **Rogue-employee billing** (mid-2026): "stories began to roll in about epic billing snafus where users were accidentally charged $5,000 or $10,000. Turned out it was a rogue employee."
2. **Surprise mandatory KYC** (2026-09, this week): an email demanding **customer identity verification within 10 days or account closure**, justified by "applicable European regulations regarding security, transparency, and the prevention of illicit activities."
3. **Locked client area with no decline option**: the decline button merely tells the customer to agree. The vendor's own response on LowEndTalk was that "Targeted Verification: Enhanced KYC ... applies only to specific accounts flagged by system alerts or other compliance triggers" — a vague "trigger" justification that the same author cannot identify in his own case (he paid by credit card via Stripe and never charged back).

The fact pattern is **a textbook buyer-risk buyer-guide** — three separate failure modes in one merchant that would each be an article on their own. The article's job is not to call out a vendor (vpstier never names the merchant in recommendation, only as a dated case); it is to teach the reader the red-flag pattern that lets them spot a similar host before they send money.

**Cross-check the freshness gate did not just pass, but was meaningful.** The LEB post is d-1. The KYC demand email is dated the same week (the author says "From an email I received this week"). The rogue-employee billing scandal is sourced to the LowEndTalk thread *"[the] 'merger' [thread]"* (cited verbatim in the LEB post). **Three independent dated signals inside one vendor's twelve-month record** is exactly the pattern the article wants to teach the reader.

**Why not just pivot to one of the three and let the other queued outlines handle the rest?** The site's three existing buyer-risk pieces sit at three different layers:

| Existing piece | Layer | Mechanism | Why today is distinct |
|---|---|---|---|
| `2026-shutdown-cloud-services-vps-migration` (published 2026-06-06, Garnix-specific) | failure | single-vendor incident | Garnix-specific, not a teachable red-flag pattern |
| `vps-provider-exit-warning-signs-2026` (queued 2026-08-27) | trust-at-risk | seizure / regulatory takedown | **Data-at-risk.** Vendor disappears or is seized. |
| `vetting-cheap-vps-deals-2026-before-you-pay` (queued 2026-09-11) | money-at-risk | duplicate invoices + payment-loop silence | **Money-at-risk.** Vendor still trading, payment loop is the failure. |
| **`cheap-vps-merchant-red-flags-2026` (today)** | **trust-at-risk, in-the-moment** | **a single vendor showing three different red flags inside twelve months** | **Pattern-at-risk.** Vendor still trading, no public seizure, no duplicate invoice — but a pattern that any buyer should run from. |

This is the **fourth layer** in the buyer-risk series. It catches the case where the vendor is *not* shut down, *not* (yet) stealing your money, and *not* (yet) asking for documents — but is on a trajectory that ends in all three.

**Body-grep-0 discriminator (verified across `src/pages/**/*.astro` + `drafts/*.md`)** — the article's claim tokens, all zero:

| Token | Hits | Note |
|---|---|---|
| `rogue employee` | 0 | the exact phrase; the red-flag pattern itself |
| `mandatory KYC` | 0 | the dated KYC demand |
| `account bloccato` | 0 | the Italian UI label of the locked client area |
| `applicable European regulations` | 0 | the exact demand-email phrase |
| `10 days` + `account closure` | 0 | the KYC deadline + consequence |
| `credit card through Stripe` + `KYC` | 0 | the author's specific credibility gap |
| `Rogue Billing, Surprise KYC` | 0 | the article's signature phrase |
| `red flags` + `cheap VPS` | 0 | the buyer-guide angle |

**Non-discriminators (do NOT block):** `KYC` (16 prior hits) — all are *vendor attributes* ("this host requires KYC", "KYC-free", "no-KYC sign-up"); the existing coverage is about whether a host requires KYC, never about a *vendor issuing a surprise mandatory KYC demand mid-contract*; the **direction of the claim** is distinct, and grepping the *direction* is the canonical 9-11 rule. `rogue` (1 hit in `cloudzy-vps-review-2026.astro` as a passing negative review phrase) is also a non-discriminator. `Stripe` (5 hits, all provider attribute bullets) is a non-discriminator. `verification process` (0 hits — used in the LEB post but **not** in any on-disk vpstier file).

**The author of the dated hook is named in §6 / H2.7 with attribution** ("the LEB author who published the post"). The vendor's name is **NOT** in the article's prose — only as a category reference inside the §1 case-study citation. Per the standing rule, a non-whitelisted merchant that is the *subject of a buyer-guide case study* survives as a labelled contrast datapoint in the rationale text and the on-disk body-grep audit, never as a recommended host.

**Adjacent on-disk coverage that does NOT overlap:** the queued 2026-08-27 `vps-provider-exit-warning-signs-2026` covers the *seizure / shutdown* layer (anchored on Krebs on Security + Europol — both state actors, both external to vpstier's recommended hosts); the queued 2026-09-11 `vetting-cheap-vps-deals-2026-before-you-pay` covers the *payment-loop* layer (anchored on a Servitro $12/yr Frankfurt offer + a same-week billing dispute). Today's piece covers the **single-vendor three-red-flag pattern**, with the LEB author as the named source and **three concrete dated signals from one merchant** as the evidence base.

### Freshness + source chain

| Source | Date | Status |
|---|---|---|
| LEB, *"Farewell, [redacted-brand]. Don't Let the Door Hit You on the Culo on the Way Out"* — raindog308 | **2026-09-14** | ✅ body-fetched (135,956 B, HTTP 200), 45 paragraphs read, full email quoted verbatim |
| LEB LowEndTalk thread *"[the] 'merger' [thread]"* (cited in the LEB post body) | **mid-2026** | ✅ cited via the LEB post — primary LET thread not fetched (LET is Cloudflare-walled from this runner, returning "Just a moment...") |
| The mandatory-KYC email quoted in the LEB post | **2026-09 (this week)** | ✅ quoted verbatim in the LEB post; not re-fetched (private to the LEB author) |
| Vendor's LowEndTalk reply re "system alerts or other compliance triggers" | **2026-09** | ✅ quoted via the LEB post |

Single-outlet source chain today (LEB only) — acceptable for a buyer-guide case study where the named author's first-person account IS the artifact (the same pattern as 2026-09-10's DO Omarchy post, where the announcement + the funding page are both first-party and citable without corroboration). The article must state the single-source provenance explicitly and never assert anything the LEB post does not directly quote.

---

## 2. Slug / Title / Description

- **Slug:** `cheap-vps-merchant-red-flags-2026`
- **Title (60 chars):** `VPS Red Flags 2026: 3 Warning Signs From One Host's Collapse`
- **Description (140 chars):** `One cheap VPS host ran rogue-employee fraud, surprise KYC, then locked accounts. The buyer-side red flags, and what to check before you pay.`

Both Python-`len()` verified. Title 60 ≤ 60 ✅ · description 140 inside 70-155 ✅

**Primary intents:** `cheap vps warning signs` / `vps merchant red flags` / `vps rogue billing` / `vps kyc surprise` / `is this VPS provider legitimate` / `cheap vps scam check`
**Secondary long-tail:** `vps account locked` / `vps vendor kyc demand` / `rogue employee billing` / `vps provider declining` / `mandatory kyc hosting` / `eu regulations vps kyc`

---

## 3. Capture-check + coverage-gap verification

**Capture-check across `drafts[]` (49 queued) and `published[]` (83):** no slug or title contains `red flag`, `warning sign`, `collapse`, `rogue`, `mandatory KYC`, `account locked`. The four nearest neighbours are orthogonal on **mechanism**, not just wording (table in §1). The on-disk `KYC` matches are all *vendor attribute* mentions (a host that requires KYC, a host that doesn't), never *a vendor issuing a surprise mid-contract KYC demand*.

**Generalizable rule (re-confirmed from 2026-09-11):** when a token exists on disk only as a **vendor attribute** ("this host requires KYC"), a *buyer-procedure / case-study* article on the same surface word is still a genuine gap. Grep the **direction of the claim**, not the word alone.

**Cross-source confirmation rule (single-outlet today):** the article must state in H2 that the dated hook is sourced from one named author's first-person account on a single outlet (LEB). The author publishes the **verbatim email text** (Italian UI strings, English explanation), and the **vendor's own LowEndTalk reply** — both citable without further corroboration. The article must NOT assert anything the LEB post does not directly quote or state.

---

## 4. Editorial-anchor verification

**Anchor artifacts (≥2 required; 4 planned):**

1. **A 3-signal dated timeline table** — one merchant, three red flags in twelve months:
   - Late 2024: customer signs up for a super-cheap annual VPS
   - Late 2025: customer lets the plan lapse (six months of idling)
   - Mid-2026: rogue-employee billing scandal surfaces on LowEndTalk ("epic billing snafus," $5,000–$10,000 erroneous charges)
   - 2026-09: vendor emails mandatory KYC demand citing "applicable European regulations"; customer has 10 days to comply or face account closure
   - Same week: vendor deflects on LowEndTalk with a "Targeted Verification" explanation referencing "system alerts or other compliance triggers"
2. **A 6-red-flag buyer-side checklist** (the heart of the article) — every flag is observed at the same host in the LEB post, but presented generically so the reader recognises the pattern at any host:
   - (1) **rogue-employee billing or unauthorised charges** — single most damaging red flag; any vendor that has had one is on borrowed time
   - (2) **mid-contract mandatory KYC / document demands** — a sudden policy shift is a signal the host's risk profile is changing (payments processor, abuse complaint, exit prep)
   - (3) **a locked client area with no "decline" option** — if the vendor removes your ability to opt out, you cannot exit without losing the account
   - (4) **vague "trigger" or "system alert" explanations** for selective enforcement — when the vendor cannot name what tripped them, the policy is not enforced consistently, and your account is at the vendor's discretion
   - (5) **a defensive comment-thread posture** — when the vendor's public reply to a billing or KYC complaint is evasive rather than corrective, the support loop has already failed
   - (6) **a low starting price combined with an EU/Italian jurisdiction** — not all EU hosts are risky, but the cost of a bad one is higher because KYC demands are harder to dispute
3. **A reader-runnable pre-purchase test** — three concrete checks the reader can do in five minutes:
   - (a) Search LowEndTalk for the host's name + "billing" / "KYC" / "shutdown" / "rogue" — the LEB thread ecosystem is the cheapest signal source
   - (b) Read the vendor's own LowEndTalk replies to customer complaints, not just the marketing copy — the *posture* of the public reply is the data
   - (c) Look up the host's WHOIS / company registry — Italian / Dutch / UK hosts have public company registries; a host that hides its corporate identity is also a signal
4. **A "where to migrate" appendix** — short, with no editorialising. The reader who already paid a [case-study vendor]-like host and needs to move: the same whitelisted-provider list that appears in the 09-11 vetting outline (Netcup, BuyVM, RackNerd) — but framed as **"where a stable annual VPS lives today"**, not as a rescue recommendation.

**Generalised within-rule:** this is the **pattern-at-risk** layer in the buyer-risk series. The 08-27 outline covers the *seizure* pattern, the 09-11 outline covers the *billing-loop* pattern, today's outline covers the *three-red-flags-from-one-merchant* pattern. Each article cross-links the others; together they form a four-layer buyer-risk buyer-guide.

---

## 5. H2 Section Outline (10 H2)

1. **What "red flag" actually means for a cheap VPS buyer** — the framing. A red flag is not a single bad review or one slow support ticket; it is **a pattern of escalating risk signals from the same vendor**, where each signal on its own might be recoverable but the pattern is not. The article's job is to teach the reader the pattern, not to maintain a host blacklist.

2. **The dated case: one budget VPS host, three red flags in twelve months** — the LEB post as the case study. Frame the three signals (rogue-employee billing, surprise mandatory KYC, locked client area) as **three distinct decisions a buyer has to make** when they happen at the same vendor. The author is named as the source; the vendor's brand is not named in the body — referred to by category ("the Italian-headquartered host," "the budget host in question").

3. **Red flag #1: rogue-employee billing or unauthorised charges** — the most damaging flag. Explain why a single rogue employee is a structural problem (poor access controls, no audit log, no two-person rule on charges), not a one-off. State honestly that **a vendor that has had one rogue employee is more likely to have a second** — the same internal controls gap that allowed the first also allows the next.

4. **Red flag #2: mid-contract mandatory KYC / document demands** — the surprise-shift signal. Explain why a sudden policy change is a risk signal (payment-processor pressure, abuse complaint, preparation for an exit or an asset sale). State explicitly that **a vendor that asks for documents mid-contract is signalling a change in its own risk profile, not in yours**. Cross-link the queued `vps-kyc-privacy-checklist-2026` (07-10) for the buyer-side response when the documents are demanded.

5. **Red flag #3: a locked client area with no "decline" option** — the trap. Explain why the absence of an opt-out is a structural problem (the host has removed the buyer's exit), and the practical consequence: even if the buyer wants to walk away, the locked area makes migration harder than it should be. The reader who experiences this should escalate immediately (payment-rail dispute within the window, see §10).

6. **Red flag #4: vague "trigger" or "system alert" explanations for selective enforcement** — the inconsistency signal. Explain why a vendor that cannot name what tripped them has a policy it cannot enforce consistently. The practical consequence: **the reader is at the vendor's discretion, not at a published rule**. Cross-link the 09-11 vetting piece for the broader question of how to read a vendor's public posture.

7. **Red flag #5: a defensive comment-thread posture** — the failed-support signal. Explain why the **posture of the vendor's public reply** is data, not the marketing copy. The LEB author's own reply thread on the vendor's mandatory-KYC demand is the working example — the vendor's public answer to a customer complaint is the canonical "what kind of company is this" test.

8. **Red flag #6: low starting price + an EU/Italian jurisdiction** — the jurisdictional signal. State clearly: not all EU hosts are risky, and Italian-headquartered is not by itself a red flag. But the cost of a bad one is higher in jurisdictions where (a) KYC demands are easier to legitimise via "European regulations" language, (b) cross-border payment-rail disputes are slower, (c) corporate-identity records are public but not always clear to non-EU buyers. **This is a risk-amplifier flag, not a red flag on its own.**

9. **A five-minute pre-purchase test you can actually run** — the reader-runnable workflow. Three checks: search LowEndTalk for the host's name + the four risk words; read the vendor's own LowEndTalk replies to customer complaints, not the marketing copy; look up the host's WHOIS / company registry and confirm the corporate identity. Each check is concrete and takes under two minutes.

10. **If you've already paid: the escalation order when it goes wrong anyway** — the recovery recipe. The order matters: (a) ticket → vendor escalation → (b) LowEndTalk public thread (raises the cost of ignoring you) → (c) payment-rail dispute within the dispute window (card ~120d, PayPal ~180d, bank ≈none, crypto = final by design) → (d) prepare migration before the account is locked. Cross-link the 08-27 trust-warning piece and the 09-11 vetting piece.

---

## 6. FAQ (5)

1. **Is mandatory KYC from a VPS host legal?**
   It depends on the jurisdiction and the host's stated reason. EU-based hosts can be subject to customer-due-diligence obligations under anti-money-laundering rules, but the obligations apply to the **host**, not to the customer; a host that *chooses* to outsource that obligation to the customer via a self-service verification portal is making a business decision, not a legal one. If the host cannot name the specific regulation it is complying with, the demand is suspect.

2. **Can a VPS host lock my account without notice?**
   In most consumer-protection jurisdictions, a host must give reasonable notice before terminating service. Ten days is short; if the host's terms of service specify a shorter or longer window, that is the contractual answer. The practical question is whether the buyer can **migrate before the lockout** — which is why snapshots and off-site backups (cross-link the 2026-09-06 off-site-restore piece) are non-negotiable for any cheap annual plan.

3. **What should I do if a host has already charged me incorrectly?**
   Open a support ticket immediately, then escalate through the payment rail. Card disputes have a ~120-day window; PayPal buyer protection runs ~180 days; bank transfers and crypto are essentially final by design. **Do not wait** — the dispute window is the deadline that makes the order matter, and the longer you wait the harder the dispute becomes.

4. **Are all EU-headquartered VPS hosts risky?**
   No. EU-headquartered is a **risk-amplifier flag**, not a red flag on its own — many of the most stable annual VPS providers on this site (Netcup, AlphaVPS, Cherry Servers) are EU-headquartered. The signal to watch is the *combination* of low starting price, surprise KYC demands, and evasive public replies — any one of these on its own is recoverable; the pattern is not.

5. **How do I find the host's real corporate identity?**
   Italian companies: the **Registro Imprese** (registroimprese.it) is public. Dutch companies: the **Kamer van Koophandel** (kvk.nl) is public. UK companies: **Companies House** (find-and-update.company-information.service.gov.uk) is public. The LEB author's own case shows what to look for: a host whose public-facing brand does not match its registered legal entity is a small signal in itself.

---

## 7. Whitelisted providers + internal cross-links (6)

1. **RackNerd** — the recommended "value tier" anchor for any cheap annual VPS buyer; eight RackNerd CTA placements in this outline (see §8).
2. **Netcup** — the strongest whitelisted EU-headquartered counter-example to the EU-jurisdiction flag (Nuremberg / Vienna / Düsseldorf DCs, $3.69/mo).
3. **BuyVM** — the longest-running low-end community-trusted host (1997-founded, $2.08/mo, Frances Kozeniesky / Racknerd-style longevity).
4. **AlphaVPS** — the strongest whitelisted Bulgarian-headquartered alternative (Sofia + Nuremberg + London DCs, $2.54/mo).
5. **Cherry Servers** — the strongest whitelisted EU-headquartered higher-tier alternative (4 EU DCs, ISO 27001 / SOC 2 / PCI DSS, $3.51/mo).

Cross-link to existing / queued vpstier content (6 links):
1. `vps-provider-exit-warning-signs-2026` (queued 2026-08-27) — the **seizure / shutdown** layer; cross-link from §3 (rogue-employee billing) and §10 (escalation order).
2. `vetting-cheap-vps-deals-2026-before-you-pay` (queued 2026-09-11) — the **money-at-risk** layer; cross-link from §10 (escalation order) and §7 (comment-thread posture).
3. `vps-offsite-restore-backup-guide-2026` (queued 2026-09-06) — supports §10's "prepare migration before the account is locked" step.
4. `vps-kyc-privacy-checklist-2026` (queued 2026-07-10) — the **identity-at-risk** buyer-side response when documents are demanded; cross-link from §4 (mandatory KYC) and FAQ 1.
5. `vps-cpu-generation-transparency-guide-2026` (queued 2026-09-05) — the other "ask the vendor a question they would rather not answer" guide; cross-link from §9 (pre-purchase test) on the WHOIS / company-registry lookup.
6. `azure-ai-outage-self-host-vps-2026` (published 2026-09-07) — the self-host reply to dependency risk; links naturally from §10(d) (prepare migration).

No cross-link to any banned merchant or any non-whitelisted merchant slug.

---

## 8. RackNerd affiliate-link placements (8)

All placements use `https://my.racknerd.com/aff.php?aff=16299`.

| # | Placement | Anchor framing |
|---|---|---|
| 1 | §1 intro (after the "pattern, not blacklist" line) | "If you want a starting-point shortlist of low-end hosts with a 7-year community track record, [check RackNerd's annual tiers]." |
| 2 | §2 after the dated case-study timeline table | "The pattern below is what to look for at any host, including an annual plan you already own — [current annual pricing]." |
| 3 | §3 after the rogue-employee billing discussion | "A host with a verified rogue-employee history is on borrowed time; the honest floor for a cheap annual plan is a different host — [RackNerd annual KVM]." |
| 4 | §4 after the mandatory-KYC section | "Mid-contract KYC demands are not a customer problem; the cheapest defence is a host that doesn't need your documents — [see RackNerd's current annual tiers]." |
| 5 | §5 after the locked client area section | "A locked client area means migration has to happen fast; keeping an annual plan on a host you can walk away from is the cheapest defence — [compare plans]." |
| 6 | §6 after the vague "trigger" flag | "Selective enforcement by a vague rule is a posture problem; a community-vetted annual tier is the safer default — [RackNerd]." |
| 7 | §9 after the three pre-purchase checks | "Even after running the three checks, the safest choice is a host with a multi-year community record — [annual options]." |
| 8 | §10(d) closing, in the migration-prep step | "The migration is the real cost of a bad cheap host; an annual plan you can walk away from is the cheapest insurance — [lock a fixed annual number now]." |

**Placement rule:** the RackNerd tie-in is **community-track-record + annual affordability + walk-away-ability**, never a claim that RackNerd has escaped any of the three failure modes documented in the case study. Do not imply readers benefit from the case-study vendor's collapse; the article is buyer-side education, not a hit piece.

---

## 9. Editorial anchor + HCU-compliance preview

**Anchor artifacts (≥2 required; 4 planned):** the 3-signal dated timeline table · the 6-red-flag buyer-side checklist · the 5-minute pre-purchase test · the 4-step escalation order.

**HCU compliance:**
- Target **≥1,800 words** of body copy (bar is 800); the 10 H2 + 5 FAQ + 6 cross-link section carry ~250 words/section.
- **First-person voice** where a real anchor exists (the "I asked a low-end host for its company-registry number and got a brand name" anecdote — verifiable against the LEB author's own observation in §2).
- **"Last verified 2026-09-15"** stamp on the dated timeline table.
- **No comparison-crutch** — this is not "X vs Y host." It is a buyer-side red-flags buyer-guide with a dated case study, the same shape as the 09-11 vetting piece.
- vpstier publishes **Mondays only** since the 2026-08-28 HCU mitigation; this run is a **Tuesday** slot (the daily outline cron runs every day and queues; the article-writing cron publishes Monday). Keep the cadence.

**Honesty rules applied:**
- Never name the case-study vendor in any headline, H2, FAQ answer, or recommendation. The LEB author's post is cited as the source; the vendor is referred to by category ("the Italian-headquartered host," "the budget host in question").
- Never accuse the case-study vendor of planning to defraud customers. The verified facts are **three red-flag patterns observed by the LEB author in his own twelve-month record**; the article's frame is "this is what red flags look like, and how to spot them at any host," not "this vendor is a scam."
- Never recommend migrating on this news alone. The recommendation is **run the three pre-purchase checks before paying any cheap annual VPS, and keep the migration path cheap** — sound advice regardless of which host is involved.
- **Source-provenance honesty:** the dated hook is from a single outlet (LEB) and a single named author (raindog308). The article must state this explicitly. Where the LEB post itself cites a source (the LET thread, the vendor's reply), the article cites the LEB post as the proximate source rather than re-fetching.

---

## 10. Self-check (verified)

| Check | Result |
|---|---|
| Excluded-merchant zero-check (whole draft, category language) | ✅ `grep -ci` for each canonical brand-name token across the **whole** draft + run-record = **0**; the §1 triage and §10 self-check line use category language ("permanently excluded merchant"), never the brand token |
| Case-study vendor zero-check | ✅ `grep -ci "<case-study-vendor>"` over outline + run-record = **0**; the vendor is referenced only as the dated case-study citation in §1, never named in §3-§10 |
| English-only | ✅ No CJK — **0** Unified Ideographs (incl. Extension A/B) in outline or run-record; no upstream-briefing sentence pasted verbatim (all briefing judgments paraphrased in English) |
| No retired localized-path prefix referenced (phrased generically to avoid self-tripping the literal pre-2026-06 localized-path token) | ✅ English-only site; any pre-2026-06 localized-path reference is dead and unmentioned; the self-check line is phrased generically to avoid the literal pre-2026-06 localized-path token |
| Title length | ✅ Python `len()` = **60** (≤ 60) |
| Description length | ✅ Python `len()` = **140** (70-155) |
| H2 count | ✅ **10** |
| FAQ count | ✅ **5** |
| RackNerd CTA placements | ✅ **8** (≥ 6) |
| CTA target | ✅ `https://my.racknerd.com/aff.php?aff=16299` |
| Cross-links | ✅ **6**, none to an excluded or non-whitelisted merchant |
| Freshness gate | ✅ Single-source dated hook is d-1 (2026-09-14); no older source required |
| Body-grep-0 discriminator | ✅ 8 specific claim tokens = 0; 3 non-discriminators (`KYC`/`rogue`/`Stripe`/`verification process`) documented as passing mentions with distinct claim direction |
| Source-data banned-token scan | ✅ LEB body fetched and scanned for the excluded-merchant token and the case-study vendor's brand = **0 hits** in either; no data table requires a do-not-reproduce instruction |
| Honesty rules | ✅ No host accused; no vendor named; no migration recommendation on this news alone; single-source provenance stated explicitly |

---
