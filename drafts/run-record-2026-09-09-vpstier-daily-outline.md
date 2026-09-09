# Run Record: vpstier daily-outline 2026-09-09

**Cron:** vpstier-daily-outline (`5fd2a36f2dc4`)
**Date:** 2026-09-09 (Wed)
**Run mode:** no_agent (scripted outline cron)
**Variant label:** variant-(3) — briefing succeeds, **both vpstier ⭐ CAPTURED** (⭐ #1 by a published review/roundup [variant-8 component], #2 by a queued outline)

---

## §1 Variant classification — Briefing SUCCESS, both ⭐ CAPTURED

The 2026-09-09 briefing (08:03 UTC) produced 2 vpstier items, neither a fresh selectable outline:

| # | Briefing item | Status | Reason |
|---|---|---|---|
| 1 | **"Singapore Kainode 30% off"** (LowEndBox 2026-09-03, raindog308) | **CAPTURED — published review + APAC roundup on disk (variant-8, 3rd confirmation)** | Kainode has a **full published review** `kainode-vps-review-2026` (07-16: "Singapore VPS from $16.99/mo Tested across Singapore/Germany/USA") + the exact "cheap Asia VPS" roundup it suggests is `best-asia-pacific-vps-2026` (published 06-05). Same LowEndBox promo already classified CAPTURED on **09-05** (variant-8 1st conf) and **09-06** (variant-8 2nd conf). Today = **3rd confirmation** of the identical promo. A dated 30%-off promo of a merchant whose full review is on disk + an overlapping region roundup already on disk = deal-tracking, NOT a fresh outline. |
| 2 | **"ServerCrate backups — start for free"** (LowEndBox 2026-09-05, raindog308) | **CAPTURED — queued outline** | The ServerCrate 09-05 story was already consumed as the dated hook for the **09-06 queued outline** `vps-offsite-restore-backup-guide-2026` ("Are Provider Snapshots a Backup? VPS Off-Site Guide 2026"). Today's briefing re-surfaces a story the outline cron selected on 09-06. Result already queued; re-picking duplicates. |

**Variant label: canonical-variant-(3)** (briefing succeeds + all ⭐ CAPTURED — component variant-8 for Kainode [dated promo of a published-review merchant + overlap roundup], queued-outline capture for ServerCrate). Per canonical rule: pick the **freshest dated substitute OUTSIDE the briefing**, flag both captured items for the user's archive-vs-publish decision. NOT a Tier-1 banned-pivot (no ⭐ referenced the excluded merchant). NOT the OFF-SHAPE re-surface pattern (the CloudLinux op-ed that re-surfaced 09-06/09-07/09-08 is NOT in today's briefing — replaced by the ServerCrate item).

---

## §2 Selected pick: `virtualizor-bgp-hijack-supply-chain-vps-2026`

- **Title:** `Virtualizor BGP Hijack 2026: Can You Trust VPS Host Updates?` — **60 chars** (gate 30–60 ✅, at max deliberately: incident name + year + buyer-trust intent)
- **Description:** "A BGP hijack served a malicious Virtualizor update in Aug 2026. VPS buyers: which hosts run Virtualizor, how hosts sign updates, and how to verify yours." — **153 chars** (gate 70–155 ✅)
- **Editorial anchor:** the Virtualizor/Softaculous **BGP-hijack supply-chain control-panel compromise** (disclosed 2026-08-31, press 08-31→09-04) → a buyer-protection guide on **update-channel integrity** — "can you trust your VPS host's security updates?" — with a whitelisted control-panel exposure table (VirMach + HostNamaste = Virtualizor in-scope class; RackNerd SolusVM, HostHatch Peregrine, cPanel/proprietary hosts = NOT Virtualizor installs), the verified official remediation checklist + scanner URL, and a RackNerd honest CTA anchored on SolusVM + annual affordability.
- **H2 count:** 10 (gate 8–10 ✅)
- **FAQ count:** 5 (gate 3–5 ✅)
- **RackNerd CTA placements:** 7 (gate ≥6 ✅)

---

## §3 Capture-check + coverage-gap verification

**Capture-check across `drafts[]` (44 entries):** no queued slug/title contains `virtualizor`, `softaculous`, `bgp hijack`, `supply chain`, `control panel`, `malicious update`. The closest queued security pieces are orthogonal (distinct mechanism under a broad "security" umbrella):
- `linux-kernel-escape-patches-august-2026-vps` (08-09) — kernel CVE, OS-code vector;
- `januscape-kvm-escape-vps-security-2026` (07-16) — hypervisor/VM-escape vector;
- `vps-provider-exit-warning-signs-2026` (08-27) — provider-solvency trust axis;
- `oracle-cloud-free-tier-account-hack-2026` (09-02) — account takeover.
None covers the **update-channel BGP supply-chain** mechanism — the control panel a host applies its patches through is compromised. Genuine 0-gap.

**On-disk body-grep across 134 blog + 76 /vps/ files:**
- `virtualizor` — only as a *feature token* in provider profiles/reviews (VirMach `/vps/virmach.astro` + blog; HostNamaste `/vps/hostnamaste.astro` + blog; CrownCloud) i.e. "runs Virtualizor," NOT a security/incident discussion.
- `Softaculous` / `BGP hijack` / `malicious update` / `supply-chain`(security sense) / `supply chain` / `widdow.jar` / `ne-rat` / `java-jre-update` / `162.55.80` / `AS62390` — **0 hits site-wide**.
- Generic non-discriminators that DO hit (expected, NOT blockers): `bgp` in network pros/cons of a few provider reviews; `control panel` as a cPanel feature token. The discriminator is the SPECIFIC supply-chain-security tokens (all 0).

---

## §4 Editorial-anchor verification (control-panel exposure table)

Verified on-disk from `/vps/` profiles + providers.json `features`:

| Provider | Control panel (on-disk source) | Virtualizor in scope? | Buyer note |
|---|---|---|---|
| **VirMach** | Virtualizor (providers.json: "custom ISO mounting via Virtualizor") | **YES — in-scope class** | Ask: ran the official `virtualizor_security_scan.sh`? which build (3.2.9.9+)? |
| **HostNamaste** | Virtualizor + SolusVM (providers.json) | **YES — in-scope class** | Same ask. |
| **RackNerd** | SolusVM (not Virtualizor; per prior vpstier-run knowledge — re-verify against host pages at full-draft) | No (not a Virtualizor install) | Honest CTA anchor: SolusVM stack, no Virtualizor-update supply-chain exposure from THIS incident; annual KVM from $21.99/yr. |
| **HostHatch** | Peregrine (custom ISO + root) | No | Different panel stack. |
| **cPanel/proprietary hosts** (knownhost, AccuWeb, IOZoom, ServerHub, etc.) | cPanel / proprietary / ISO stacks | No | Panel diversity = risk diversification. |
| **Managed clouds** (DO/Vultr/Linode-style) | Proprietary cloud dashboards | No | Managed provisioning, no customer-visible control panel. |

**RackNerd honesty instance (8-21/8-23/9-08 pattern):** do NOT claim RackNerd is "immune to all supply-chain risk" — no host is. Honest framing: RackNerd runs SolusVM, so it was NOT a Virtualizor-install exposed to THIS specific hijack; supply-chain hygiene is host-wide posture, not a single-panel toggle. Anchor CTA on **annual affordability + 7-yr community longevity + 6x Inc.5000 honoree** + the genuinely-divergent panel stack as a buyer consideration.

**The single most buyer-relevant, host-agnostic lesson:** Softaculous admitted update clients **did not yet cryptographically verify packages**, so a modified package would not have been rejected (The Register). The checklist question is "does the host's panel crypto-sign updates / pin repos?" NOT "was my host named in a list?" (the vendor CANNOT produce a definitive list — every operator is in scope by default).

---

## §5 Editorial-anchor verification (incident facts)

Body-verified via research subagent (2026-09-09), sources fetched through r.jina.ai reader proxy (all news domains CF-wall plain curl):
- **Hijack window:** Aug 28 ~21:00 → Aug 30 ~06:10 UTC across **two diversion waves** (~33.3h total, ~11h lull when the origin re-announced); route withdrawn ~05:50–06:10, no diversion after 06:10.
- **Disclosure:** Aug 31 (hosting provider DreamIT raised alarm on LowEndTalk; Virtualizor confirmed same day). First press Aug 31 (cyberkendra); BleepingComputer/The Register Sep 1; The Hacker News Sep 2.
- **Mechanism:** more-specific route for `162.55.80.0/24` (inside a European host's `162.55.0.0/16` announcement) hijacked via AS62390 over transit AS6204, keeping the legitimate origin AS on the path tail so it never appeared as origin → more-specific route won on every accepting network. Diverted Virtualizor's software-update servers + Softaculous client/billing endpoints. Attacker held a technically-valid Let's Encrypt cert (domain-ownership validation itself routed through the hijack) → no TLS warning.
- **Malicious package served only to** Virtualizor installs that polled for an update during a diverted interval AND completed — "a small number/handful of servers" (vendor), not general user base. Update clients didn't crypto-verify packages → modified package accepted.
- **Scope:** AlbaHost confirmed 5 of 34 Virtualizor hypervisors infected. Vendor cannot produce a definitive list (attacker's responses never hit vendor logs). No confirmed client-account/payment-data theft; no confirmed VPS-tenant compromise as of Sep 2 advisories.

Full IOC table + quotes in §10 below.

---

## §6 H2 outline (10 sections)

1. Introduction: the update you trusted was a hijack — Aug 31 disclosure, multi-outlet, mechanism in one paragraph
2. What actually happened (the 33.3-hour timeline) — two waves, prefix, hijack mechanism, disclosure
3. Why the numbers look small but the lesson is big — small confirmed count vs undefinable potential; ~28% time-weighted diversion proxies (not infection counts)
4. The payload: how a fake update became root — injected @exec() in 3 files, root cron executes, SSH key, widdow.jar, java-jre-update.service; "version number proves nothing"
5. The control-panel exposure table (who's in the blast radius) — §4 table
6. Why 'just trust the updater' is broken — and the fix — unsinged updates, 3.2.9.9 + Security Analyzer, signing roadmap, cert revocation
7. The official remediation checklist (re-run by the reader/host) — 6-step vendor checklist + scanner URL + grep recipe
8. The VPS-buyer checklist (what to ask before/after you pay) — 5 questions incl. control panel / signing / scanner / disclosure / off-site backup
9. Are you the operator or the tenant? (two different checklists)
10. FAQ + bottom line — RackNerd primary CTA + honest closer

---

## §7 Self-check (on outline draft)

| Check | Result |
|---|---|
| Banned-merchant zero-check (`grep -ci` for each canonical excluded brand-name token across the WHOLE draft, run by category) | **0 ✅** (brand-name tokens scrubbed from draft + run-record; the factual origin-AS of the hijacked prefix was rewritten to neutral phrasing so no excluded-brand token appears even in §1 rationale or §10 source-chain, which references the ASN numerically only) |
| CJK chars (Python `re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf\u3040-\u30ff]', draft)`) | **0 ✅** |
| `/zh/` path references | **2** (both legitimate self-doc audit lines — the CJK regex self-doc row + the `/zh/ references` self-check row; canonical 8-09/8-11/8-29 pattern; route tree IS deleted) |
| Title length `len()` | **60 ✅** (gate 30–60) |
| Description length `len()` | **153 ✅** (gate 70–155) |
| H2 count | **10 ✅** (gate 8–10) |
| FAQ count | **5 ✅** (gate 3–5) |
| RackNerd CTA placements | **7 ✅** (gate ≥6) |
| On-disk body-grep-0 for supply-chain angle | **VERIFIED ✅** (8 SPECIFIC tokens = 0 hits; generic `bgp`/`control panel` hits are feature tokens, not coverage) |
| HCU-compliance preview (full-draft gate) | **COMMITTED** (≥800 unique words, ≥2 real artifacts, first-person voice, "Last verified 2026-09-09" stamp, no comparison-crutch, self-audit pre-deploy) |

Note: `grep -P "\u4e00..."` is PCRE; the CJK check is also run as a Python `re.findall` at full-draft time per the 9-08 note.

---

## §8 On-hold items / supersede flags

- **No supersede flag** for any existing pending outline. Today's pick is orthogonal to all 44 queued entries (a fresh control-panel-supply-chain archetype).
- **User inbox decision — both briefing ⭐ are CAPTURED:**
  (a) Kainode Singapore 30%-off promo → CAPTURED by published `kainode-vps-review-2026` + `best-asia-pacific-vps-2026`. **3rd confirmation** of the same promo (09-05, 09-06, 09-09). Recommend archive, not publish.
  (b) ServerCrate backups → CAPTURED by queued 09-06 `vps-offsite-restore-backup-guide-2026` (its hook IS the ServerCrate 09-05 story). Archive, don't duplicate.
- **Incident recency note:** disclosure was 08-31; by full-draft time the "breaking news" window has closed, but this is a **durable security buyer-guide** anchored on a dated body-verifiable incident + vendor advisories + release artifact (3.2.9.9 + Security Analyzer) + signing roadmap — same evergreen-security class as queued `oracle-cloud-free-tier-account-hack-2026` (09-02) and `linux-kernel-escape-patches-august-2026-vps`. Fits the reduced-cadence HCU-quality posture.
- 44 `outline_pending_publish` entries remain in `drafts[]` (last_run 2026-09-08). Today's append makes 45. The user is the publish-gate.
- **CLOUDFLARE_API_TOKEN: ACTIVE (verified 2026-09-08, expires 2027-09-02).** No deploy_pending needed for the article-cron downstream.

---

## §9 Pitfalls captured this run

1. **Briefing can re-surface the SAME captured promo 3× (Kainode 09-05/09-06/09-09)** — variant-8 rule (dated promo of a published-review merchant + overlap roundup) is stable. Cite the prior confirmations in §1, don't rescue.
2. **Briefing can re-surface an item the outline cron already consumed as a QUEUED entry's hook (ServerCrate→`vps-offsite-restore-backup-guide-2026`)** — a story that became a queued outline's dated anchor is CAPTURED by that queued outline; re-surfacing = duplicate. Capture-check must search BOTH published[] and the queued outlines' anchors.
3. **Origin-AS fact vs banned-merchant zero-rule** — the hijacked prefix's origin AS (a European host) is a factual network detail, but naming that host's brand would trip the site's absolute zero-token ban in outline text. Rewrote to neutral ("a European host's 162.55.0.0/16 announcement"); the ASN geography is preserved, the banned brand token is not.
4. **Verified-source hygiene:** SecurityWeek + SCMagazine were Cloudflare-walled / no article indexed → mark "could not verify," do NOT cite them for facts. BleepingComputer/The Register/The Hacker News/cyberkendra + both vendor advisories verified via reader proxy.
5. **Don't overstate scale:** confirmed infection count is SMALL (AlbaHost 5-of-34; vendor "handful"); the article's value is the update-integrity LESSON + buyer checklist, not a scare count. Use only verified IOC entries.
6. **"Version number proves nothing"** — fake was "3.2.9.8" but installs still reported 3.2.9.7; do not claim a version-based detection works.
7. **Crypto-verify admission** — Softaculous confirmed update clients did not yet cryptographically verify packages; that is the core host-agnostic buyer lesson and must be attributed to The Register quote, not invented.

---

## §10 Source-chain + verified fact bundle (for full-draft cron reuse)

**Sources fetched + attributed (2026-09-09, news domains via r.jina.ai reader proxy; plain curl is CF-walled):**
| Source | Article | Date |
|---|---|---|
| BleepingComputer (Bill Toulas) | "Hackers push malicious Virtualizor update in BGP hijacking attack" | 2026-09-01 |
| The Register | "33-hour BGP hijack of Softaculous traffic prompts security scramble" | 2026-09-01 |
| The Hacker News (Swati Khandelwal) | "BGP Hijack Delivers Malicious Virtualizor Update That Establishes Persistent Root Access" | 2026-09-02 |
| CyberKendra | "Virtualizor Compromised via BGP Hijack, Hosts Hit Hard" | 2026-08-31 |
| Virtualizor vendor advisory | "Security Incident - BGP Hijacking" (highest-detail primary) | ~08-31 |
| Softaculous vendor advisory | "Security Incident - BGP Hijacking Update" | ~08-31/09-01 |
| **SecurityWeek** | (headline surfaced) | **could not verify** (403 when fetched) |
| **SCMagazine** | no article indexed | **could not verify** |

**Timeline (verified):** onset first unauthorized announcement `2026-08-28T20:57:30Z`; Wave 1 ≈21:00 Aug 28 → ~08:50 Aug 29; lull ≈09:00–20:00 Aug 29 (origin re-announcement); Wave 2 ≈20:00 Aug 29 → ~06:00 Aug 30; route withdrawn 05:50–06:10; **no diversion after 06:10 Aug 30 (global routing restored)**. Net window **~33.3 hours** ("~33.3 hours" in Virtualizor advisory; "33-hour" in Register headline). Disclosure Aug 31 (DreamIT on LowEndTalk + Virtualizor confirm).

**Mechanism (verified):** hijacked prefix **`162.55.80.0/24`** (inside a European host's `162.55.0.0/16`), announced by **AS62390** (NexonHost) via transit **AS6204** (Zet.net), keeping legitimate origin AS24940 on the path tail → more-specific route won on every accepting network. Diverted **Virtualizor software-update servers** + a number of Softaculous systems (`api.*`, `files.*`, client/billing). Attacker held a technically-valid Let's Encrypt cert (CA domain validation routed through the hijack) → no TLS warning.

**Malicious package / payload (AlbaHost forensic, most complete):** fake "Virtualizor 3.2.9.8" update; injected `@exec()` calls into `_universal.php`, `globals.php`, and `zzvirtservice` (start script); executed by Virtualizor's own root cron `virt_check.php`; wrote attacker SSH key to `/root/.ssh/authorized_keys`; installed Java 17 if absent; downloaded **`widdow.jar`** from `cdn[.]nerat[.]cc`; ran as root; registered systemd unit **`java-jre-update.service`** for persistence; created **`proxyuser`** account; opened firewall rule; one node observed with an interactive SSH session >3 hrs from `193.32.127[.]248`. Tooling described as a commodity RAT rented via ne-rat.xyz (C2 `connect[.]ne-rat[.]xyz`, `31.77.220[.]138:2025`). **"Version number proves nothing"** — installs still reported 3.2.9.7; the fake was 3.2.9.8.

**Official IOC list (vendor scanner, via THN):** marker files `/etc/systemd/system/java-jre-update.service`, `/usr/lib/jvm/.cache/jre-runtime.dat` (~13.5MB), `/usr/lib/jvm/.cache/.installed`, `/tmp/.vz_svc_done`, `/tmp/widdow.jar`; payload SHA-256 `b81a4e1fab9fc4e404d57224fe71e2c143aa93942bd46998789bdc944a7870c7`; download URL `cdn[.]nerat[.]cc/installer/widdow.jar`; C2 `connect[.]ne-rat[.]xyz`; injected strings `jre-runtime.dat`, `cdn.nerat.cc`, `connect.ne-rat.xyz`; SSH key prefix `AAAAC3NzaC1lZDI1NTE5AAAAIP13pPAm…`; key fingerprint `SHA256:YQmy1hKF1h5cdJLxlZ5EScNoxe/UDWahjsWuQw2ERi8`; rogue account `proxyuser`; SSH source `193.32.127[.]248`; C2 `31.77.220[.]138:2025`. Altered files `globals.php`, `_universal.php`, `zzvirtservice` under `/usr/local/virtualizor/`.

**Scope:** Virtualizor = Softaculous' VPS management/control panel used by hosting providers to create/sell/manage VPSs (widely used by budget hosts). Malicious package authoritatively confirmed served to "a small number / handful" of installs (AlbaHost: 5 of 34 hypervisors). OTHER Softaculous products (Backuply, SitePad, Webuzo, ampps, Softaculous itself) — **no malicious package found** (vendor). No fixed affected version established; fix = **Virtualizor 3.2.9.9 / 3.2.9 Patch 9** (~Sep 1) with a new **Security Analyzer**; roadmap adds **cryptographic package signing**; fraudulent cert reported for revocation to Let's Encrypt. Vendor "cannot produce a definitive list" → treat every Virtualizor operator as in scope.

**Mitigation (vendor + security-researcher guidance, verbatim-numbered):**
1. Check for `/etc/systemd/system/java-jre-update.service`; if present **do NOT simply delete** — contact support first (evidence preservation; an infected start script re-runs the payload on restart).
2. Rotate + restrict Virtualizor API keys (master/admin panel); remove unrecognized API keys; restrict API to trusted IPs.
3. Audit unknown SSH keys, new accounts, unexpected cron/scheduled tasks, unexpected outbound connections; restrict SSH to trusted IPs.
4. Run the official scanner: `https://files.virtualizor.com/security/virtualizor_security_scan.sh` (retrieved-script SHA-256 `73e74402b3a61c7bab289fc11347bd54c7fcdc2fa2e410f4c3de9d6cd7377d48` as of Sep 2, 2026).
5. Contact support before remediating a positive host; altered core files require restore-from-known-good or reinstall; **with confirmed root compromise a clean rebuild is the only reliable remediation** ("deletion is not remediation").
6. Client area: reset Softaculous client-area password + anywhere reused; review statements if card entered in window; regenerate NOC/Client Center API keys; vendor invalidated client-area sessions from affected windows (Aug 28 ~20:57→Aug 29 ~08:50 UTC and Aug 29 ~20:57→Aug 30 ~06:10 UTC).

**Quick reader grep (CyberKendra):** `grep -RsnE 'cdn\.nerat\.cc|widdow\.jar|jre-runtime\.dat' /usr/local/virtualizor /etc/systemd/system /root/.ssh 2>/dev/null`; `systemctl status java-jre-update.service`; `getent passwd proxyuser`.

**Key verbatim quotes:**
- Softaculous (BleepingComputer): "We have confirmed that a malicious Virtualizor update package was delivered to a small number of installations that checked for updates while their traffic was being diverted… This affected a handful of servers rather than the general Virtualizor user base."
- Virtualizor advisory: "Because the malicious responses were served by the attacker's system and never reached our own logs, we cannot produce a definitive list of affected servers, so every Virtualizor operator should carry out the checks…"
- Softaculous (The Register): "Our product update clients did not yet cryptographically verify update packages, so a modified package would not have been rejected on that basis."
- AlbaHost (THN): "We can confirm that 5 of our 34 Virtualizor hypervisor nodes contained the same malicious modifications described in this thread."
- CyberKendra: "A BGP hijack against Virtualizor's update infrastructure pushed a malicious package onto VPS hypervisors running the panel, handing attackers root on every node that installed it."

---

## §11 Commit plan (two-commit pattern)

1. `feat:` outline + run-record (2 files)
2. `chore(state):` state.json (drafts append + count bump + last_run + publish_notes line + `ensure_ascii=False`)
3. `git push origin main`

---

*End of run record.*
