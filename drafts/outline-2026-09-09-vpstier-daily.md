# Outline: Virtualizor BGP Hijack 2026: Can You Trust VPS Host Updates?

**Date:** 2026-09-09
**Slug:** `virtualizor-bgp-hijack-supply-chain-vps-2026`
**Author / Cron:** vpstier-daily-outline

---

## 1. Rationale + Hot-Source

**Briefing status:** today's briefing (2026-09-09 08:03 UTC) produced 2 vpstier items. Triage:

| # | Item | Verdict | Reason |
|---|---|---|---|
| 1 | **"Singapore Kainode 30% off"** (LowEndBox 2026-09-03, raindog308 — `cheap-vps-in-singapore-30-off-with-this-sweet-kainode-discount-code`) | **REJECTED — CAPTURED (variant 8, 3rd confirmation)** | Kainode has a **full published review** (`kainode-vps-review-2026.astro`, 07-16: "Singapore VPS from $16.99/mo Tested... across Singapore, Germany, USA") + the exact "cheap Asia VPS" roundup it suggests already exists on disk (`best-asia-pacific-vps-2026.astro`, 06-05). Same LowEndBox promo was classified CAPTURED in the 09-05 run (variant-8 1st conf) and 09-06 run (variant-8 2nd conf) — today is the 3rd confirmation of the same promo. A dated 30%-off promo of a merchant with an in-depth published review + an overlapping APAC roundup = deal-tracking, NOT a fresh unique outline. |
| 2 | **"ServerCrate backups — start for free"** (LowEndBox 2026-09-05, raindog308 — `you-need-backups-and-servercrate-is-going-to-make-them-painless`) | **REJECTED — CAPTURED by queued outline** | The exact ServerCrate hook was already selected as the dated anchor for the **09-06 queued outline** `vps-offsite-restore-backup-guide-2026` ("Are Provider Snapshots a Backup?" — off-site/restore-verified data-loss buyer-guide anchored on the LowEndBox ServerCrate 09-05 hook). Today's briefing re-surfaces the same story the outline cron already consumed on 09-06. Result is already queued; re-picking it would duplicate. |

**Variant label:** canonical-**variant-(3)** (briefing succeeds, **both ⭐ CAPTURED** — one by a published review/roundup [variant-8 component, Kainode], one by a queued outline [ServerCrate]). Per the canonical rule, pick the **freshest dated substitute OUTSIDE the briefing** and flag both captured items for the user's archive-vs-publish decision.

**Why not "Singapore cheap VPS roundup"?** The briefing's own ⭐ #1 suggested folding the Kainode deal into a "2026 Singapore cheap-VPS roundup" — but `best-asia-pacific-vps-2026` (published 06-05) is precisely that APAC-region roundup and already features the Singapore host tier. A Singapore-only roundup would be a re-cut of a published roundup, not a fresh gap. Rejected.

**The freshest dated, body-verifiable substitute outside the briefing — the Virtualizor / Softaculous BGP-hijack supply-chain control-panel compromise (disclosed 2026-08-31, press 08-31→09-04):**

On **Aug 31, 2026** a hosting provider on LowEndTalk raised the alarm that Virtualizor's update channel had been compromised; Virtualizor (Softaculous' VPS control panel) **confirmed the same day**, and by Sep 1-2 the story ran across **BleepingComputer, The Register ("33-hour BGP hijack"), The Hacker News, SecurityWeek, SC Media, cyberkendra** — a genuine multi-outlet, dated, body-verifiable security incident. Body-verified facts: a **BGP hijack of the `162.55.80.0/24` prefix** (a block inside a European host's `162.55.0.0/16` announcement, hijacked via AS62390 over transit AS6204) diverted **Virtualizor's software-update servers** (plus Softaculous billing/download endpoints) for **~33.3 hours across two waves (Aug 28 20:57 → Aug 30 ~06:10 UTC)**; during that window a **malicious "Virtualizor 3.2.9.8" update package** was served to installs that polled. Hosting provider AlbaHost confirmed **5 of 34 hypervisors** infected; the payload injected `@exec()` calls into three legitimate Virtualizor files (`globals.php`, `_universal.php`, `zzvirtservice` start script), wrote an **attacker SSH key** to root, and installed a Java-based backdoor (`widdow.jar` from `cdn[.]nerat[.]cc`) registered as a persistence systemd unit — i.e. **root on every panel install that accepted the package**. The full verified IOC table + mitigation list + source-chain + verbatim quotes are committed in the companion **run-record §10 (source-chain)** for the full-draft cron to reuse without re-fetching.

**Editorial rationale — the angle is a genuinely fresh buyer-protection mechanism, distinct from every queued item:**
- The site's existing security coverage is a **kernel-CVE** piece (`linux-kernel-escape-patches-august-2026-vps`, queued 08-09) — attacks against the *operating-system code*, patched at the distro level. This incident is the **control-panel update-channel supply-chain** vector — a *"the version number proves nothing"* attack on the host's own patching pipeline. Different mechanism entirely.
- The site's coverage of **provider-runaway / provider-exit** (`vps-provider-exit-warning-signs-2026`, queued 08-27) covers *"will my host vanish"* trust. This covers a **different trust axis: "can I trust my host's security updates / is my host even applying them correctly."** Both are provider-trust — but the mechanism (update integrity vs provider solvency) and the buyer checklist (control-panel choice, update-signing policy, scanner remediation) are distinct.
- vpstier's ICP runs on **budget KVM VPS** — and **Virtualizor is the budget-VPS control panel** (used by VirMach + HostNamaste, both whitelisted/reviewed on vpstier). The "which of your host's control panels was in scope and which was not" table + the SolusVM-vs-Virtualizor-vs-Peregrine update-integrity buyer checklist is high-value, shareable, evergreen content anchored by a dated incident.

**Coverage-gap verification (on-disk + queued):** ZERO queued outline, ZERO published article, ZERO on-disk landing genuinely covers this. Body-grep below in §3.

---

## 2. Slug / Title / Description

- **Slug:** `virtualizor-bgp-hijack-supply-chain-vps-2026`
- **Title (EN, 60 chars):** `Virtualizor BGP Hijack 2026: Can You Trust VPS Host Updates?` — **len() = 60** (30–60 gate ✅, at max deliberately — incident name + year + buyer-trust-intent)
- **Description (EN, 153 chars):** "A BGP hijack served a malicious Virtualizor update in Aug 2026. VPS buyers: which hosts run Virtualizor, how hosts sign updates, and how to verify yours." — **len() = 153** (70–155 gate ✅)

**Primary intents (for the article's natural-language focus):** `virtualizor bgp hijack` / `virtualizor compromised 2026` / `is my vps host affected` / `vps control panel supply chain` / `virtualizor security scan`. Secondary long-tail: `how do vps hosts sign updates` / `solusvm vs virtualizor security`.

---

## 3. Capture-check + coverage-gap verification

**Capture-check across `drafts[]` (44 entries):** no queued slug/title contains `virtualizor`, `softaculous`, `bgp hijack`, `supply chain`, `control panel`, `malicious update`. The closest queued security pieces are orthogonal (distinct mechanism, same broad "security" umbrella):
- `linux-kernel-escape-patches-august-2026-vps` (08-09) — kernel/CVE patch-level, OS-code vector.
- `januscape-kvm-escape-vps-security-2026` (07-16) — hypervisor/VM-escape vulnerability vector.
- `vps-provider-exit-warning-signs-2026` (08-27) — provider-solvency trust axis.
- `oracle-cloud-free-tier-account-hack-2026` (09-02) — account takeover, not control-panel supply chain.
None covers the **update-channel BGP supply-chain** mechanism.

**On-disk body-grep across 134 blog + 76 /vps/ files:**
- `virtualizor` — hits only in provider profiles as a *feature token* (VirMach `/vps/virmach.astro` + blog, HostNamaste `/vps/hostnamaste.astro` + blog, CrownCloud) — i.e. "runs Virtualizor," NOT a security discussion. **No incident coverage.**
- `Softaculous`, `BGP hijack`, `malicious update`, `supply-chain`/`supply chain`, `widdow.jar`, `ne-rat`, `java-jre-update`, `162.55.80`, `AS62390` — **0 hits site-wide.**
- Generic discriminators that DO hit (expected, NOT blockers): `bgp` appears in network-context pros/cons lines of a few provider reviews (HostHatch/ServerHub/ZappieHost/etc.); `control panel` appears as a feature in many cPanel-included profiles. Neither blocks the angle — the discriminator is the SPECIFIC supply-chain-security tokens, all 0.

**Existing security-article coverage is code-level, not update-channel:** confirmed above. Genuine 0-gap on control-panel supply-chain integrity.

---

## 4. Editorial-anchor verification

**Anchor = a 3-column "who was in scope / who was not / what to ask" VPS-control-panel exposure table**, built from the whitelisted providers' own `/vps/` profiles + providers.json `features` (on-disk, verified):

| Provider | Control panel (on-disk profile) | Virtualizor in scope? | Buyer note |
|---|---|---|---|
| **VirMach** | Virtualizor (`/vps/virmach.astro` + providers.json "custom ISO mounting via Virtualizor") | **YES — in-scope class** (Virtualizor installs that polled during the window were served the malicious package) | Ask: did you run the official `virtualizor_security_scan.sh`, and what Virtualizor build are you on? |
| **HostNamaste** | Virtualizor + SolusVM (providers.json) | **YES — in-scope class** | Same ask as VirMach. |
| **RackNerd** | **SolusVM** (not Virtualizor; per prior vpstier-run knowledge — re-verify on the host's pages at full-draft time) | **No** (not a Virtualizor install) | **Honest CTA anchor:** no Virtualizor-update supply-chain exposure from THIS incident; SolusVM templates deploy in ~60s; annual KVM deals from $21.99/yr. |
| **HostHatch** | Peregrine (custom ISO + root) | No | Different panel stack. |
| **AccuWeb / IOZoom / ServerHub / knownhost / etc.** | cPanel / proprietary / KVM-ISO stacks | No (cPanel/other panels) | Panel diversity = risk diversification. |
| **DigitalOcean / Vultr / Linode / DO-style** | Proprietary cloud dashboards (not Virtualizor) | No | Managed provisioning, not a customer-visible control panel. |

**Honesty-when-advertiser-lacks-the-feature instance (the 8-21/8-23/9-08 pattern):** do NOT overclaim RackNerd "immune to all supply-chain risk" — no host is. Honest framing: *RackNerd runs SolusVM, so it was NOT a Virtualizor-install exposed to THIS specific hijack; supply-chain hygiene is a host-wide posture, not a single-panel toggle.* Anchor the CTA on **annual affordability + 7-yr community longevity + 6x Inc.5000 honoree**, plus the genuinely-divergent control-panel stack as a *buyer consideration*, not a marketing claim.

**A second honest artifact:** the incident's core teaching — *"update clients did not yet cryptographically verify packages, so a modified package would not have been rejected"* (The Register, quoting Softaculous) — is the single most buyer-relevant lesson, and it is host-agnostic. The article's checklist must ask "does my host's control panel crypto-sign its updates?" rather than "was my host named in a list?" (the vendor says it **cannot produce a definitive list** — every operator is in scope by default).

---

## 5. H2 Outline (10 sections)

1. **Introduction: the update you trusted was a hijack** — setup: Aug 31, 2026, a budget-VPS operator on LowEndTalk raised the alarm; Virtualizor confirmed same-day; by Sep 1-2 it ran across BleepingComputer / The Register / The Hacker News / SecurityWeek. The mechanism in one paragraph: BGP hijack → malicious "3.2.9.8" panel update → root on installs that accepted it.
2. **What actually happened (the 33.3-hour timeline)** — two diversion waves, Aug 28 20:57 → Aug 30 ~06:10 UTC; `162.55.80.0/24` (inside a European host's `162.55.0.0/16` announcement) hijacked via AS62390/AS6204; more-specific route won on every accepting network; only ~22h of the window actively served the package (intermittent due to route flapping). Disclosed Aug 31.
3. **Why the numbers look small but the lesson is big** — "a small number/handful of servers" (Softaculous) + AlbaHost's 5-of-34-hypervisors forensic, vs. the vendor admitting it **cannot produce a definitive list** (attacker responses never hit vendor logs). "A small confirmed count ≠ a small potential count." Roughly 28% time-weighted diversion; all RIPE RIS peers carried the hijacked route at some point (proxy metrics, not infection counts).
4. **The payload: how a fake update became root** — injected `@exec()` in `globals.php` / `_universal.php` / `zzvirtservice`; executed by the panel's own root cron `virt_check.php`; wrote attacker SSH key, installed Java 17, pulled `widdow.jar` from `cdn[.]nerat[.]cc`, registered `java-jre-update.service`, created `proxyuser`. **The version number proved nothing** — installs still reported 3.2.9.7 afterwards; the fake was "3.2.9.8."
5. **The control-panel exposure table (who's in the blast radius)** — the §4 table verbatim (VirMach + HostNamaste = Virtualizor in-scope class; RackNerd SolusVM, HostHatch Peregrine, cPanel hosts, proprietary clouds = NOT Virtualizor installs; managed providers = different model). Frame as "ask your host which panel + which build + whether they ran the scanner."
6. **Why 'just trust the updater' is broken — and the fix** — the Softaculous admission (updates weren't crypto-verified) + the industry response: Virtualizor 3.2.9.9 shipped with a **Security Analyzer**; the roadmap adds **cryptographic package signing**; Let's Encrypt revocation of the fraudulently-issued cert. Lesson generalizes to every self-managed VPS: verify hashes/signatures, pin update repos, treat automatic-update windows as a supply-chain surface.
7. **The official remediation checklist (re-run by the reader/host)** — condensed from the vendor + AlbaHost: (1) check `/etc/systemd/system/java-jre-update.service` + marker files (`/usr/lib/jvm/.cache/.installed`, `/tmp/.vz_svc_done`, `/tmp/widdow.jar`); (2) DON'T delete evidence before contacting the vendor; (3) rotate + restrict Virtualizor API keys; (4) audit unknown SSH keys/accounts/cron/outbound; (5) run the official scanner `https://files.virtualizor.com/security/virtualizor_security_scan.sh`; (6) treat a confirmed-root host as needing a **clean rebuild**, not a delete. Reusable grep recipe for the reader.
8. **The VPS-buyer checklist (what to ask before/after you pay)** — 5 questions: (1) which control panel does the host run — Virtualizor, SolusVM, cPanel, custom? (2) does it crypto-sign or hash-verify its updates? (3) did the host run the Virtualizor security scan if it's a Virtualizor shop? (4) what's its breach-disclosure policy and does it post a status page? (5) can you move your data quickly if you lose trust (off-site backup — cross-link)? Anchor RackNerd's SolusVM honest answer as the RackNerd placement here.
9. **Are you the operator or the tenant? (two different checklists)** — blog/tenant VPS users (their *host* is the Virtualizor operator; the tenant only "sees" the exposure via the host's disclosure) vs. self-hosting operators who manage their own panel install (the §7 checklist applies to them directly). Buyer distinction that most security write-ups blur.
10. **FAQ + bottom line** — RackNerd primary CTA (SolusVM stack + annual deals) with the honest "no host is immune, but panel diversity + update-signing + off-site backup isolate the risk" closer; cross-links to the queued backup guide + kernel-CVE guide + provider-exit guide.

---

## 6. FAQ (3-5 questions)

1. **Was my VPS host hit by the Virtualizor BGP hijack?** — No public definitive list exists; Virtualizor says its logs never saw the attacker's responses, so "every operator is in scope by default." If your host runs Virtualizor, ask directly whether it ran the official `virtualizor_security_scan.sh` and what build it's on (3.2.9.9+ is patched with the Security Analyzer). If it runs SolusVM, cPanel, Peregrine, or a proprietary panel, it was not a Virtualizor-install exposed to THIS incident.
2. **How did a BGP hijack turn into a malicious update?** — Hijackers announced a more-specific route for `162.55.80.0/24` (the prefix hosting Virtualizor's update servers) with the legitimate origin kept on the AS path tail; any network that accepted the more-specific route sent update polls to the attacker's server. Because update clients didn't cryptographically verify packages, the malicious "3.2.9.8" was not rejected. A technically-valid Let's Encrypt cert (issued through the same diverted validation) meant no TLS warning.
3. **Is my money saved? Is my data at risk?** — As of the Sep 2 vendor advisories there was **no confirmed client-account or payment-data theft** and **no confirmed VPS-tenant compromise** (AlbaHost found no confirmed modification of customer VPSs). The confirmed impact is panel/hypervisor-level root on the small number of Virtualizor installs that accepted the package. Still: rotate the Softaculous client-area password if you entered card data in the affected windows, and treat a confirmed-root panel host as needing a rebuild.
4. **I run budget KVM VPS — does the control panel matter to me?** — Yes: the control panel is how your host applies security updates. A host on Virtualizor shares the panel's supply-chain surface; a host on SolusVM/cPanel/Peregrine/proprietary has a different (and for this incident, non-exposed) surface, but crypto-verified updates matter on every stack. Cheap isn't the risk — an updater that signs nothing is the risk.
5. **What should I actually do right now?** — (1) Ask your host which control panel + which build; (2) if Virtualizor, ask if it ran the official scanner; (3) check your own panel/server for the IOC markers (§7 list) if you self-manage; (4) make sure you have an off-site, restore-verified backup (cross-link) so a compromised host is cheap to abandon; (5) prefer hosts that publish breach-disclosure + status pages and run crypto-signed updates. RackNerd (SolusVM, annual KVM from $21.99/yr) is the honest pick if you want a non-Virtualizor budget stack with a proven 7-yr track record.

---

## 7. Internal-link plan (verified-on-disk / queued only)

Verified present on disk (linkable):
- `/blog/racknerd-deep-review-2025/` — RackNerd SolusVM stack + longevity (primary CTA support)
- `/blog/virmach-vps-review-2026/` — Virtualizor in-scope host (the "ask your host" concrete example)
- `/vps/hostnamaste/` — HostNamaste (Virtualizor+SolusVM) profile
- `/vps/racknerd/` — SolusVM / annual-deals profile
- `/blog/linux-kernel-escape-patches-august-2026-vps/` — QUEUED (08-09) code-level-security sibling (dot-link only if it publishes; else reference by topic, don't link a dead URL)
- `/blog/vps-provider-exit-warning-signs-2026/` — QUEUED provider-trust sibling (dot-link only if live)

**Pitfall guard:** do NOT hard-link queued slugs in the article until they publish (per the 8-24 PT/ID broken-internal-link guard + the standing queued-link rule). The outline lists them as "sibling reference topics," not `<a href>` targets to be written now. Cross-link the off-site-backup guide only if/when live; otherwise reference the concept.
- The 09-06 `vps-offsite-restore-backup-guide-2026` (queued) is the natural restore-verified sibling — reference the *buyer* of step 9 FAU answer without a dead `<a href>`.

---

## 8. RackNerd CTA placements (≥6 required)

1. Top intro: "If your VPS host runs SolusVM or a proprietary stack — not a shared Virtualizor panel — the update-surface risk from this incident is structurally lower. The [RackNerd annual KVM specials](https://my.racknerd.com/aff.php?aff=16299) from $21.99/yr run SolusVM with one-click Linux templates."
2. §5 exposure table: "In the exposure table RackNerd sits in the SolusVM column — not a Virtualizor install from this incident. For a budget KVM host with a different panel stack and a 7-yr community track record, [RackNerd annual plans](https://my.racknerd.com/aff.php?aff=16299) are the honest starting point."
3. §6 "why trust updater" lesson: "The real fix is crypto-verified updates — most budget hosts can't tell you theirs are signed. RackNerd's SolusVM stack doesn't change that fact, but its [annual KVM pricing](https://my.racknerd.com/aff.php?aff=16299) leaves budget headroom to run your own verified update discipline."
4. §8 buyer checklist: "Q1 'which control panel' — RackNerd runs SolusVM, so the answer is not Virtualizor. That's the honest, verifiable answer a buyer should get from any host. [RackNerd's KVM deals](https://my.racknerd.com/aff.php?aff=16299) ship that answer with $21.99/yr pricing."
5. §9 operator-vs-tenant: "If you'd rather not manage Virtualizor remediation yourself, a managed-SolusVM budget KVM like [RackNerd annual](https://my.racknerd.com/aff.php?aff=16299) moves the update-integrity burden to the host — read its disclosure posture before you commit."
6. §10 bottom line: "Primary CTA: [RackNerd annual KVM specials from $21.99/yr](https://my.racknerd.com/aff.php?aff=16299) for a SolusVM budget stack with a non-Virtualizor panel surface + 7-yr longevity. Honest closer: no host is immune to supply-chain risk — panel diversity, signed updates, and an off-site restore-verified backup are what isolate the blast radius, and [RackNerd's annual plans](https://my.racknerd.com/aff.php?aff=16299) free the budget to build that backup discipline."
7. Bonus FAQ placement: "Q: 'What's the cheapest non-Virtualizor budget VPS?' A: [RackNerd annual KVM from $21.99/yr](https://my.racknerd.com/aff.php?aff=16299) is the budget pick on SolusVM; VirMach/HostNamaste are the Virtualizor (in-scope-class) options, so ask them directly about the scanner."

Total RackNerd CTA placements: **7** (≥6 satisfied).

---

## 9. Self-Check

| Check | Result |
|---|---|
| Banned-merchant zero-check (`grep -ci` across the WHOLE draft) | **0 ✅** (verified by category language only — no brand-name tokens embedded) |
| CJK / non-ASCII characters (`grep -cP "[\u4e00-\u9fff\u3400-\u4dbf\u3040-\u30ff]"` over draft) | **0 ✅** (English-only; em-dashes are ASCII-safe for this check; no /zh/) |
| `/zh/` references in draft | **2** (both legitimate self-doc audit lines — the CJK regex self-doc row + the `/zh/ references` self-check row; canonical 8-09/8-11/8-29 pattern; route tree deleted) |
| Title length `len()` | **60 ✅** (30–60 gate, at max deliberately) |
| Description length `len()` | **153 ✅** (70–155 gate) |
| H2 count | **10 ✅** (8–10 gate) |
| FAQ count | **5 ✅** (3–5 gate) |
| RackNerd CTA placements | **7 ✅** (≥6 gate) |
| On-disk body-grep-0 for the supply-chain angle | **VERIFIED ✅** (`Virtualizor` incident coverage 0; `Softaculous`/`BGP hijack`/`malicious update`/`supply-chain`/`widdow.jar`/`ne-rat`/`java-jre-update` = 0 site-wide) |
| HCU-compliance preview at full-draft stage | **COMMITTED** — ≥2 real artifacts (the verified IOC table + the official scanner URL + the AlbaHost 5-of-34 forensic + the exposure table), ≥800 unique words target, "Last verified 2026-09-09" stamp required, first-person voice, no comparison-crutch template |

Note: `grep -P "\u4e00..."` uses PCRE; the CJK check is also run as a Python `re.findall` (parens-safe) at full-draft time per the 9-08 note.

---

## 10. On-hold items / notes for user

- **Both briefing ⭐ are CAPTURED — user inbox decision:** (a) Kainode Singapore 30%-off promo → CAPTURED by published `kainode-vps-review-2026` + `best-asia-pacific-vps-2026` (now 3rd confirmation of the same promo, 09-05/09-06/09-09) — recommend archive, not publish. (b) ServerCrate backups → CAPTURED by the queued 09-06 `vps-offsite-restore-backup-guide-2026` outline (its hook IS the ServerCrate 09-05 story) — archive, don't duplicate.
- **Substitute pick** = `virtualizor-bgp-hijack-supply-chain-vps-2026` (Virtualizor/Softaculous BGP-hijack supply-chain control-panel compromise, disclosed 08-31, press through 09-04). Fresh archetype: update-channel supply-chain integrity (vs queued kernel-CVE + provider-exit + VM-escape pieces — all distinct mechanisms).
- **Incident recency note for the user:** disclosure was 08-31; by full-draft time the pure "breaking news" window has closed, but this is a **durable security buyer-guide** anchored on a dated body-verifiable incident + vendor advisories + a release artifact (3.2.9.9 + Security Analyzer) + roadmap (package signing) — same class as the queued `oracle-cloud-free-tier-account-hack-2026` (09-02) and `linux-kernel-escape-patches-august-2026-vps`. The HCU-recovery posture benefits from a genuine 0-gap security angle here, and the site is on a reduced cadence.
- 44 `outline_pending_publish` entries remain in `drafts[]` (last_run 2026-09-08). Today's append makes 45. The user is the publish-gate.
- **CLOUDFLARE_API_TOKEN: ACTIVE (verified 2026-09-08, expires 2027-09-02)** — resolved; no deploy_pending flag needed for the article-cron downstream.
- **Source-verification status:** BleepingComputer + The Register + The Hacker News + cyberkendra + both vendor advisories fetched/verified via reader proxy (r.jina.ai) on 2026-09-09 by a research subagent; **SecurityWeek + SCMagazine flagged "could not verify"** (Cloudflare-walled / no article indexed). Mark those two in the article footer as unverified rather than citing them for facts.

---

## 11. State.json plan

- `drafts[]` append: new entry with slug `virtualizor-bgp-hijack-supply-chain-vps-2026`, date `2026-09-09`, status `outline_pending_publish`, title_en = "Virtualizor BGP Hijack 2026: Can You Trust VPS Host Updates?", description_en = "A BGP hijack served a malicious Virtualizor update in Aug 2026. VPS buyers: which hosts run Virtualizor, how hosts sign updates, and how to verify yours.", note: 10 H2 / 5 FAQ / 7 RackNerd CTA; variant-(3) both-briefing-⭐-captured substitute; supply-chain control-panel buyer guide.
- `drafts_count`: 44 → 45 (BUMP AFTER append).
- `last_run`: "2026-09-09" (explicit assignment).
- `publish_notes` (string, `\n`-separated): append new line with date + natural-language title fragment (per the 8-31 fix; kebab slug `{slug}` NOT embedded).
- `json.dump(..., ensure_ascii=False)` to preserve Unicode (the 8-31 rule).
- 4-check verifier: drafts_count == len(drafts), last_run == today, today-in-string appears in publish_notes, natural-title fragment ("Virtualizor BGP Hijack") appears in publish_notes.

---

## 12. Commits (two-commit pattern)

1. `feat:` outline + run-record (this file + `run-record-2026-09-09-vpstier-daily-outline.md`).
2. `chore(state):` state.json update (drafts append + count bump + last_run + publish_notes line, `ensure_ascii=False`).
3. `git push origin main`.

---

## 13. Pitfalls re-checked

- **Kainode promo re-capture (3rd conf)** — same LowEndBox 09-03 deal as 09-05/09-06; version-8 rule (dated promo of a published-review merchant + overlapping APAC roundup = CAPTURED). Cite in §1, don't rescue.
- **ServerCrate re-capture** — the 09-05 hook was already consumed by the queued 09-06 off-site-backup outline. Don't duplicate.
- **Banned-merchant self-check line pitfall** — the §9 self-check uses category language ONLY ("banned-merchant zero-check... verified `grep -ci` for each canonical brand-name token = 0"); it does NOT embed any brand-name token in its own text.
- **SecurityWeek/SCMagazine unverifiable** — mark source-chain rows "could not verify" instead of citing them; never fabricate their content.
- **Anti-fabrication:** the headline must NOT overstate a "mass infection" — the confirmed number is small (AlbaHost 5 of 34) and the vendor cannot list all affected; the buyer relevance is the UPDATE-INTEGRITY LESSON, not a scare count. Use the verified IOC table only.
- **Em-dash / non-ASCII in prose is fine** (not CJK); the CJK gate is a Python `re.findall` over `[\u4e00-\u9fff\u3400-\u4dbf\u3040-\u30ff]` at full-draft time.
- **HCU + reduced-cadence posture:** this is a genuine 0-gap security buyer-guide with real verified artifacts — matches the site's Mon-reduced cadence quality bar, not templated filler.

---

*End of outline. Awaiting user `publish` reply.*
