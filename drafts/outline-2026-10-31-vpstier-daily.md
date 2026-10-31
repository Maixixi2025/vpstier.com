# Outline: CVE-2026-98432 Linux Kernel TCP RCE — Is Your VPS Exposed?

**Date:** 2026-10-31
**Slug:** `linux-kernel-tcp-rce-cve-2026-98432-vps`
**Author / Cron:** vpstier-daily-outline (`5fd2a36f2dc4`)
**Variant:** variant-13 — briefing SUCCEEDED but **zero usable stars** (both vpstier items captured / non-whitelisted / walled). Banned-pivot to the freshest dated substitute outside the briefing, sourced from the same feeds.
**Archetype:** unpatched-kernel-flaw buyer-guide (new on vpstier — no published article or queued outline covers a guest-kernel flaw with no vendor fix shipped, a distro-by-distro patch-status table, or a "no mitigation exists" verdict)
**Status:** `outline_pending_publish` — awaiting user `publish`

---

## 1. Rationale + Hot-Source

### 1a. Briefing pick #1 — rejected

**MassiveGrid "Lifetime Price Guarantee" walk-back** (LowEndBox, 2026-10-28, `lowendbox.com/blog/massivegrid-when-the-lifetime-price-guarantee-turns-out-to-not-be-quite-so-lifetime/`).

Body-verified this run (HTTP 200, 158,355 bytes): MassiveGrid is retiring its LowEndTalk promotional offers and upgrading affected services to its "2026 product line" on **1 December 2026**, with recurring prices "considerably more" from the next renewal. The LET offer text said *"Lifetime Price Guarantee: Your discounted rate is locked in forever. No sneaky price hikes—ever."* A member ticket response cites memory and storage costs rising "by a factor of 4-10 times the original pricing across the industry."

**Rejected — angle already published on vpstier.** `lifetime-vps-deals-2026-real-cost-vs-marketing.astro` (live) is a 10-H2 article whose H2 list is: *The 4 Pricing Models Every VPS Buyer Should Know / The Dated Hook / What "Lifetime" Actually Means / The Annual-Pricing Sweet Spot / Hourly and Monthly / Monthly and Annual / The Pricing-Model Risk Matrix / When a "Lifetime" Deal Is the Right Choice / The 5-Question Checklist / Conclusion*. It already owns the lifetime/annual pricing-model space, already carries a dated lifetime-deal hook, and already warns that lifetime vendors disproportionately lack enterprise-grade off-site backup. A second "lifetime promise broken" piece would be the **third** re-surface of a story the site has already monetized. Also disqualifying: **MassiveGrid is not in `providers.json`** (verified — 0 of 65 entries), so there is no `/vps/` profile to cross-link or route to.

This is the **second consecutive run** (2026-10-30 and 2026-10-31) the briefing has offered this same item. Per the standing re-surface rule, it is rejected every time and never rescued.

### 1b. Briefing pick #2 — rejected

**C-Servers 8+ days of downtime with unfulfilled refund promises** (r/VPS, `reddit.com/r/VPS/comments/1xjesd8/stay_away_from_cservers_cserverscouk_8_days_of/`).

**Rejected on three independent grounds:**

1. **Walled primary.** The thread is body-walled from this runner — `www.reddit.com` returns the login/ticket stub, `old.reddit.com` returns "Blocked" (Reddit's bot wall), and `cservers.co.uk` does not resolve at all (`ERR_NAME_NOT_RESOLVED`). Nothing about the incident could be independently verified.
2. **Not whitelisted.** C-Servers is **absent from `providers.json`** (0 of 65 entries) — no `/vps/` profile, no cross-link target.
3. **Angle already owned.** The "host goes dark, refunds evaporate" buyer-guide angle is already covered by **three** queued outlines: `vps-provider-shutdown-warning-signs-2026` (2026-07-24), `vps-provider-exit-warning-signs-2026` (2026-08-27), `luxvps-special-offer-shutdown-alternatives-2026` (2026-07-20) — plus the published `2026-shutdown-cloud-services-vps-migration.astro`. And `cheap-vps-merchant-red-flags-2026` (2026-09-15) already owns "a host's refund/dispute handling is itself a red flag," while `vetting-cheap-vps-deals-2026-before-you-pay` (2026-09-11) already owns "choose a payment rail you can reverse" and "read the refund clause before you pay." A fifth piece on this theme would be the fourth re-surface.

### 1c. Selected — CVE-2026-98432, the Linux kernel TCP use-after-free

**Zero usable stars fired both hard gates, so this run pivots to the freshest dated substitute outside the briefing, sourced from the same feeds the briefing reads (LowEndBox + Google News RSS).**

The story is a **critical, remotely exploitable, currently-unpatched Linux kernel TCP flaw** that Anthropic's own unreleased research model turned into a **zero-click remote-root exploit** — and the two distributions most VPS owners run (Ubuntu and RHEL) **have no fixed kernel available**. It is dated, multi-outlet, vendor-primary-verifiable, and it is *directly* a VPS-owner problem.

| Fact | Value | Source |
|---|---|---|
| CVE | **CVE-2026-98432** | CVE record (CVE List / CVE Program) |
| Title | `ipv4: free inet_opt and ireq_opt after an RCU grace period` | Linux CNA, CVE record |
| Class | Use-after-free in the kernel's IPv4 TCP handshake path | Linux CNA, CVE record |
| CVSS v3.1 (Linux CNA) | **9.8 CRITICAL** — `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` | CVE record metrics + Red Hat API + Ubuntu tracker |
| CVSS v4.0 (Ubuntu) | **8.3 HIGH** — `CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:L/VI:L/VA:H/SC:N/SI:N/SA:N` | Ubuntu CVE tracker `impact` |
| Red Hat severity (live, fetched 2026-10-31) | **Critical**, CVSS **9.8**, `threat_severity: Critical` | Red Hat security data API |
| Red Hat's own words | "allows an unauthenticated remote attacker to cause kernel memory corruption or an immediate system crash over standard IPv4 TCP network traffic without requiring local privileges or user interaction" | Red Hat `statement` field |
| Published | **2026-10-15** (Red Hat `public_date` 2026-10-15T00:00:00Z; CVE `datePublished` 2026-10-15T12:08:22Z) | Red Hat API + CVE record |
| CVE record last updated | **2026-10-30** (still moving) | CVE record `dateUpdated` |
| Present since | **Linux 4.4** (per the CVE record's `affected` block) | CVE record |
| Root cause | `tcp_v4_syn_recv_sock()` hands `ireq->ireq_opt` to the child socket **without copying**; another CPU can read the same options for a retransmitted SYNACK while the first core frees them — `inet_sock_destruct()` uses a plain `kfree()` instead of `kfree_rcu()` | Linux CNA description |
| Second path | The same patch closes **request socket migration** — enabled by `net.ipv4.tcp_migrate_req=1` or a `BPF_SK_REUSEPORT_SELECT_OR_MIGRATE` program | Linux CNA description |
| IPv6 | **Not affected** by the main race — `tcp_v6_syn_recv_sock()` duplicates the options. (A separate CALIPSO-related IPv6 migration issue is deferred to another patch.) | Linux CNA description |
| Trigger | An unauthenticated peer supplies **IPv4 Record Route or Timestamp** options in a TCP SYN, then retransmits it to hit the race | CVE record CVSS scenario |
| Upstream fix | Eric Dumazet's patch, crediting Anthropic researcher **Xinyang Ge**; `kfree_rcu()` in `inet_sock_destruct()` and `tcp_v4_reqsk_destructor()` | CVE record description + upstream commit `e3f33b0a1d89` |
| Fixed upstream kernels | **5.10.272, 5.15.223, 6.1.190, 6.6.159, 6.12.113, 6.18.56, 7.2.10**, and mainline **7.3-rc7** onward | CVE record `affected` semver block + Ubuntu tracker (`upstream: released`) |
| Files touched | `net/ipv4/af_inet.c`, `net/ipv4/tcp_ipv4.c` | CVE record `affected` |
| Anthropic's exploit | An unreleased internal Claude research model wrote a **zero-click remote-root exploit**; stage 1 wins the race repeatedly to leak a kernel pointer and **defeat KASLR**, stage 2 overflows a buffer and overwrites a callback pointer to run a root shell command | Anthropic research disclosure (2026-10-27), via Cyber Kendra's body-verified report |
| Anthropic's timing | Leaking a kernel address took **48 minutes**; reaching root command execution took another **5 minutes** | Same |
| The MPTCP caveat | "Neither the CVE record nor the kernel fix mentions multipath TCP (MPTCP), and Anthropic has not said why its exploit targets MPTCP listeners or whether servers without one can be taken over the same way." | Cyber Kendra, 2026-10-30 |
| Anthropic's own statement | The company said it reported every flaw to the affected vendor and that each has been fixed | Cyber Kendra / CyberSecurityNews, 2026-10-28 |
| Exploitation status | **No vendor advisory reports attacks**; not in CISA's Known Exploited Vulnerabilities catalogue; Anthropic has not released the exploit code. Public research appeared 2026-10-29: the **Innora** group published a root-cause analysis and a QEMU-based reproduction environment, and says it will not release a weaponised exploit in the short term | Cyber Kendra, 2026-10-30 |
| Debian 13 (trixie) | **Fixed** — `linux 6.12.113-1` (DSA-6568-1), fixed 2026-10-16 | Debian Security Tracker |
| Debian 12 (bookworm) | **Fixed** — `linux 6.1.190-1` (DLA-4841-1); `linux-6.12 6.12.113-1~deb12u1` (DLA-4850-1) | Debian Security Tracker |
| Debian unstable | **Fixed** — `7.2.10-1` | Debian Security Tracker |
| Oracle Linux 7–10 (UEK) | **Fixed** 2026-10-16 — ELSA-2026-500397, ELSA-2026-500398, ELSA-2026-500399 | Cyber Kendra table + Oracle CVE page (HTTP 200) |
| Amazon Linux 2023 (kernel 6.18) | **Fixed** 2026-10-24 — ALAS2023-2026-3251 | Cyber Kendra table |
| Amazon Linux 2023 (kernel 6.12) | **Fixed** 2026-10-29 — ALAS2023-2026-3335 | Cyber Kendra table |
| Amazon Linux 2 + AL2023 default kernel | **Pending** — no fix released | Cyber Kendra table |
| openSUSE Leap 16.0 / SUSE Linux Micro 6.2 | **Fixed** — kernel `6.12.0-160000.40.1` | Cyber Kendra table |
| SLES 15 SP4–SP6 (LTSS) | Fix in QA, **not yet released** | Cyber Kendra table |
| SLES 15 SP7, SLES 16.0 | Fix **in progress**, not yet released | Cyber Kendra table |
| Ubuntu 22.04 / 24.04 / 26.04 / 26.10 | **Vulnerable, fix in progress, not yet released** — tracker shows `pending` for jammy `5.15.0-203.213`, noble `6.8.0-149.149`, resolute `7.0.0-43.43`, stonking `7.3.0-10.10` | Ubuntu CVE tracker (169 package entries; status `pending`) |
| Ubuntu 16.04 / 18.04 / 20.04 | **Vulnerable** — tracker status `needed` | Ubuntu CVE tracker |
| Ubuntu 14.04 (trusty) | **Not affected** — `3.11.0-12.19` | Ubuntu CVE tracker |
| Ubuntu priority | **High** (the tracker adopts the kernel team's 9.8) | Ubuntu CVE tracker |
| RHEL 8 / 9 / 10, OpenShift 4 (RHCOS) | **Vulnerable, no fix released** — Red Hat `package_state` lists all as `Affected` | Red Hat security data API |
| RHEL 6 / 7 | **Not affected** — "RHEL 7 is the exception because its kernel never received the vulnerable code" | Red Hat `package_state` + Cyber Kendra |
| Red Hat advisory | **No RHSA published.** The errata search for this CVE returns zero entries; the CVE API's `mitigation` field says only "See the security bulletin for a detailed mitigation procedure" — and no such bulletin is out | Red Hat errata page (HTTP 200, 0 RHSA ids), Red Hat API |
| Red Hat's stance on mitigation | "Red Hat says no available mitigation meets its standards for ease of deployment and stability, and no other vendor advisory lists one" | Cyber Kendra, 2026-10-30 |
| Red Hat Bugzilla | **2553390** — status `NEW`, priority `urgent`, severity `urgent`, `cf_fixed_in` **empty**, last modified **2026-10-30T19:32:10Z** | Red Hat Bugzilla REST API (HTTP 200, 4,351 bytes) |
| **Severity divergence (live)** | SUSE scores it **8.1 / important**; Oracle **8.1** (`AV:N/AC:H/…`); Amazon **7.0**; Red Hat has moved from Moderate 5.9 → **8.1** → and as fetched on 2026-10-31 its live API reads **9.8 / Critical**; the kernel CNA and Ubuntu use **9.8** | Red Hat API (live), SUSE CVE page (HTTP 200, 229,634 bytes), Oracle CVE page (HTTP 200, 15,247 bytes), CVE record, Ubuntu tracker |

**Why this is a vpstier topic and not general IT news:** every fact above maps to a decision a budget-VPS buyer makes. The kernel is the guest's, not the host's — the patch is the buyer's job on an unmanaged box. The vulnerability sits in the **TCP handshake path**, which means *any* listening service is a candidate target, and the two distros a large share of budget VPS images ship are exactly the two with no fix. The buyer question is not "should I switch providers?" — it is "which of my boxes can I patch today, and what do I do about the ones I can't?"

### 1d. Content-gap verification (pre-write grep)

Grep across **all 60 published blog `.astro` files**, **all 169 draft `.md` files** and **all 68 `/vps/` profile pages**:

```
CVE-2026-98432                     -> 0 hits (blog / drafts / vps)
inet_opt | ireq_opt                -> 0 hits
tcp_v4_syn_recv_sock               -> 0 hits
kfree_rcu | "RCU grace"            -> 0 hits
tcp_migrate_req                    -> 0 hits
multipath TCP | MPTCP              -> 0 hits
"Record Route" | ip_options_build  -> 0 hits
KASLR                              -> 0 hits
ELSA- | ALAS<year> | DLA- | DSA-   -> 0 hits
Anthropic zero-click / Claude exploit chain -> 0 hits
"kernel CVE team"                  -> 0 hits
```

**Zero published articles and zero queued outlines cover this CVE, this mechanism, this patch-status picture, or the "no vendor fix exists yet" buyer problem.**

The nearest neighbour is `linux-kernel-escape-patches-august-2026-vps` (queued 2026-08-09, CVE-2026-64561 "Zapscape" / CVE-2026-64564 "SCTPhantom"). It is a **different failure mode**: those are **guest-to-host KVM escapes** and a **local-user-to-root SCTP container escape**, fixed in a shipped stable round (kernels 7.1.6 / 6.18.42 / 6.12.101 / 6.6.148) with a clean "patch now" answer. This one is a **remotely reachable, pre-auth, unauthenticated** flaw in the TCP stack with **no fix available on two major distros** and **no vendor-approved mitigation**. The Aug-09 outline's own conclusion is "Patch Discipline Wins in 2026" — a different question from "what do you do when there is no patch and no mitigation to apply." Distinct article, adjacent subject; recorded rather than hidden.

Also distinct: `vps-ssh-security-host-key-checks-2026` (queued 2026-10-29) covers SSH authentication and a backdoor sweep; `vps-offsite-restore-backup-guide-2026` (2026-09-06) covers data restore; `januscape-kvm-escape-vps-security-2026` (2026-07-16) covers the earlier KVM-escape class. None covers an unpatched guest-kernel TCP flaw.

### 1e. GSC context

vpstier.com 7-day (2026-10-31 GSC report): **0 clicks / 85 impressions / avg rank 84.9**, 30-day 241 impressions. Top queries remain navigational-commercial head terms — `best vps provider` (12 impr., rank 83), `best vps for ai agents` (10, rank 74), `best vps providers` (5, rank 84), `best unmanaged vps` (4, rank 86), `best vps service` (4, rank 80), `best virtual private server` (1, rank 99), `compare vps providers` (2, rank 91).

There is **still no long-tail query signal** on this site — every impression sits at rank 74+. So this outline is **news-analysis + buyer-guide**, not query-led, and the strategic bet is that a distinctive, dated, well-linked buyer-education piece compounds better than another provider review. Note the useful secondary intent this piece can pick up: `best unmanaged vps` (rank 86) is exactly the query a buyer types when they are about to find out who patches their kernel.

### 1f. Editorial-honesty constraints on the draft (binding)

1. **The MPTCP uncertainty must be stated, not smoothed over.** Anthropic's exploit targets MPTCP listeners; neither the CVE record nor the kernel patch mentions MPTCP; Anthropic has not said whether a non-MPTCP server is equally exposed. The draft must present this as an open question, not resolve it in either direction.
2. **Red Hat's severity is a moving target.** The live API read on 2026-10-31 says **9.8 / Critical**, while the 2026-10-30 secondary report says 8.1. The draft must use the **live, dated** value and state the "last verified" date — and must not present 8.1 as current.
3. **Red Hat has published no advisory and no mitigation.** "See the security bulletin" with no bulletin published must be reported as *no fix and no mitigation*, not as a pointer to an unread document.
4. **No in-the-wild exploitation is claimed.** CISA KEV: no. Vendor advisory: none. The Innora repository is public research, and Cyber Kendra states it has not tested the material. The draft says exactly that.
5. **Vendor naming discipline.** Where a fact names a vendor, the source sentence must be quoted verbatim, not paraphrased (canonical pitfall #42 — a paraphrase once collapsed "two different providers" into "the same provider").

---

## 2. Slug / Title / Description

**Slug:** `linux-kernel-tcp-rce-cve-2026-98432-vps`

**Title:** `CVE-2026-98432: The Linux Kernel TCP RCE Hitting Your VPS` — **57 / 60 char gate**
(vpstier `BaseLayout.astro` renders `<title>{title}</title>` verbatim — no auto-suffix, re-verified 2026-10-31 by reading `src/layouts/BaseLayout.astro`. Bare string length is final length. Lengths measured with Python `len()`.)

**Description:** `CVE-2026-98432 is a 9.8 CVSS Linux kernel TCP flaw. Ubuntu and RHEL have no fix yet. Which distros are patched and what a VPS owner should do now.` — **146 / 155 char gate**

**Target keywords:** `cve-2026-98432`, `linux kernel tcp rce`, `is my vps vulnerable cve-2026-98432`, `ubuntu kernel security update`, `linux kernel use after free 2026`, `kernel patch unpatched vps`.

---

## 3. H2 Chapter Plan (10 sections)

1. **What CVE-2026-98432 actually is** — the flaw in plain language, using the kernel CNA's own description: the IPv4 TCP handshake hands a pointer to the pending connection's IP options to the new socket without copying it, and a second CPU core can still be reading those options for a retransmitted SYN-ACK while the first core frees them. A `kfree()` where a `kfree_rcu()` belongs. Include the CVSS 9.8 vector from the CVE record and what each term means for a buyer (network, low complexity, no privileges, no user interaction).
2. **How an AI model turned it into a zero-click root exploit** — Anthropic's 2026-10-27 disclosure: an unreleased internal Claude research model found the flaw and wrote the exploit. The two-stage chain — win the race repeatedly to leak a kernel pointer and defeat KASLR, then overflow a buffer and overwrite a callback pointer to execute a root shell command. The 48-minute leak plus 5-minute-to-root timing. **State the MPTCP open question here**, in the same breath: the CVE record and kernel fix never mention MPTCP, and Anthropic has not said whether non-MPTCP servers are equally exposed.
3. **The severity numbers do not agree — and that is the point** — the kernel CNA and Ubuntu say **9.8 Critical**; Red Hat's live page (verified 2026-10-31) says **Critical / 9.8** after moving from Moderate 5.9 → 8.1; SUSE and Oracle score **8.1**; Amazon scores **7.0**. Explain why vendors differ on attack complexity (winning the race reliably is hard; getting a kernel pointer out of it is harder) and what the disagreement means for a buyer: the *floor* is "kernel memory corruption or an immediate crash", the *ceiling* is unauthenticated root.
4. **Is it being exploited right now?** — honest answer: no vendor advisory reports attacks, it is not in CISA's Known Exploited Vulnerabilities catalogue, and Anthropic has not released the exploit code. But public research landed on 2026-10-29: the Innora group published a root-cause analysis and a QEMU-based reproduction environment, stating it will not release a weaponised exploit in the short term. Then the uncomfortable part: an unreleased exploit from a frontier lab is a **known-good** exploit, and reproducing a race condition locally is a solved engineering problem.
5. **The distro patch table — who is fixed and who is not** — the article's centrepiece, rendered as a real table with a "Last verified 2026-10-31" stamp. **Fixed:** Debian 13 (6.12.113-1, DSA-6568-1), Debian 12 (6.1.190-1 / 6.12.113-1~deb12u1), Debian unstable (7.2.10-1), Oracle Linux 7–10 UEK (ELSA-2026-500397/398/399), Amazon Linux 2023 kernel 6.18 (ALAS2023-2026-3251) and kernel 6.12 (ALAS2023-2026-3335), openSUSE Leap 16.0 / SL Micro 6.2. **Not fixed:** Ubuntu 22.04 / 24.04 / 26.04 / 26.10 (tracker `pending`), Ubuntu 16.04 / 18.04 / 20.04 (`needed`), RHEL 8 / 9 / 10 and OpenShift 4 (all `Affected`, no RHSA), Amazon Linux 2 and the AL2023 default kernel, SLES 15 SP4–SP6 (fix in QA). **Not affected:** RHEL 6 / 7 (the vulnerable code never landed), Ubuntu 14.04 trusty.
6. **What to do on each of the three situations you are actually in** — (a) **You can patch** (Debian/Oracle/Amazon/openSUSE): install and **reboot**, because a kernel update only takes effect when the new kernel is running; show the `uname -r` check and how to compare against the fixed list (5.10.272 / 5.15.223 / 6.1.190 / 6.6.159 / 6.12.113 / 6.18.56 / 7.2.10 / 7.3-rc7). (b) **You are on Ubuntu or RHEL and there is no fix**: this is the hard case — explain that Red Hat's Bugzilla shows `cf_fixed_in` empty with priority and severity both `urgent` and last modified 2026-10-30, that no RHSA exists, and that Red Hat's own mitigation field points to a bulletin that has not been published. Give the honest interim posture: reduce exposed listeners, prefer an egress allow-list, and treat the box as "patch pending" rather than "safe". (c) **You build your own kernel**: the kernel CVE team advises moving to the latest stable release rather than cherry-picking individual fixes.
7. **The mitigation that does not exist — and what to do instead** — state plainly that Red Hat says no available mitigation meets its standards for ease of deployment and stability, and that no other vendor advisory lists one. Then the buyer-side substitutes that are actually available: shrink the listening surface (a box exposing nothing but SSH has a much smaller handshake-reachable surface), put the service behind a reverse proxy or L4/L7 edge so the origin never terminates handshakes directly, restrict egress, and — for the boxes you cannot patch — decide honestly whether to wait, move the workload to a patchable image, or accept the risk with a written note.
8. **Who is responsible for the kernel — you or the host?** — the unmanaged-vs-managed split, and the trap that catches people: on a KVM host, the **host's** kernel is what a guest-to-host escape would exploit, while **your guest's** kernel is what CVE-2026-98432 exploits. Both matter and they are patched by different parties. Add the "who actually ships the image" question — an image shipped pre-patched by a provider can still be months behind, and a provider that re-images quarterly is not the same risk as one that lets you choose your kernel. This is where the RackNerd CTA sits naturally: a KVM box where you own the root and pick your own kernel.
9. **The 2026 kernel wave in context** — place this CVE in the year's pattern of Linux kernel disclosures (the Aug-2026 Zapscape / SCTPhantom round fixed in the 7.1.6 / 6.18.42 / 6.12.101 / 6.6.148 stable round; the July 2026 Januscape KVM-escape class) and draw the honest conclusion: **the recurring lesson is not "patch faster", it is "know which of your boxes you cannot patch, before you need to"**. An inventory of unpatchable boxes is the deliverable.
10. **Verdict and the 60-minute triage plan** — a timed checklist that ends in a decision, not a summary: run `uname -r` on every box, diff it against the fixed list, separate "patch tonight" from "no fix available", and write down the plan for the second group. Close with the honest bottom line — for most budget VPS owners the actionable answer this week is Debian, and the honest answer for Ubuntu and RHEL boxes is that you are waiting on your vendor, not on yourself.

---

## 4. FAQ (5 questions)

1. **Is my VPS vulnerable to CVE-2026-98432, and how do I check?** (covers `uname -r`, the fixed-version list, and the fact that a patched kernel only counts once you have rebooted into it)
2. **Why is Ubuntu and Red Hat still vulnerable when Debian and Oracle have already shipped fixes?** (distro release cadence, why security team fixes land upstream first, and the fact that RHEL 7 is *not* affected because the vulnerable code never landed in its kernel)
3. **What does "no mitigation" actually mean for my server right now?** (the honest answer: no vendor-approved workaround exists; the buyer-side substitutes are reducing exposed listeners, fronting the origin, and restricting egress)
4. **Does disabling multipath TCP (MPTCP) protect my server?** (the honest answer: **nobody knows yet** — the CVE record and kernel fix never mention MPTCP, Anthropic has not said why its exploit targets MPTCP listeners, and it has not said whether non-MPTCP servers are equally exposed. This answer must state the uncertainty rather than manufacture a recommendation.)
5. **Should I switch VPS providers because of this?** (no — the flaw is in the guest kernel, which you control on an unmanaged box; the real questions are which distro you run, whether a fix exists for it, and whether you are patching on a schedule you control)

---

## 5. RackNerd Affiliate CTA Placements (8)

| # | Section | Rationale |
|---|---------|-----------|
| CTA #1 | Intro (after the flaw explanation) | The reader now knows their guest kernel is their problem — this is where the "you own the root" framing lands |
| CTA #2 | §4 is-it-being-exploited | A reader who wants to shrink the attack surface needs a host whose network and DDoS posture is documented, not assumed |
| CTA #3 | §5 distro patch table | The table's "Debian" column is the actionable one this week; the CTA points at a KVM box the buyer can image with the distro they choose |
| CTA #4 | §6 what to do — situation (a) you can patch | The concrete destination for "install and reboot" |
| CTA #5 | §6 situation (b) you cannot patch | The reader whose current box has no fix — a fresh box on a patchable image is the migration path |
| CTA #6 | §7 no mitigation exists | The structural fix section — a host you control, with root, is the leverage point |
| CTA #7 | §8 who patches the kernel | Core ownership section — the affiliate's natural home |
| CTA #8 | §10 verdict / 60-minute triage | Closing recommendation |

**Primary affiliate link:** `https://my.racknerd.com/aff.php?aff=16299`

**Affiliate-label integrity:** every CTA identifies RackNerd as the site's affiliate / budget baseline for a **KVM VPS the buyer owns and patches**, never as a fix for CVE-2026-98432 and never as a signup path for any of the vendors named in the article (Red Hat, Ubuntu, Canonical, Debian, Oracle, SUSE, Amazon, Anthropic are **subjects of the article, never affiliate destinations**). The article must not imply that any provider "fixes" the flaw — the fix is in the guest kernel image, which the buyer selects.

**RackNerd facts used (from `providers.json`, re-verified live against `racknerd.com` on 2026-10-31, HTTP 200 / 34,042 bytes):** VPS **from $2.24/mo** on the homepage (the `providers.json` `startingPrice` of 1.99 is the affiliate-page entry point — the homepage figure is the one cited), **20 datacenter locations** across North America / Europe / Asia, **24/7 support**, KVM VPS and AMD Ryzen VPS product lines, and dedicated servers from $139/mo. `providers.json` records 5 US datacenters (Los Angeles, Seattle, Dallas, New York, Chicago) — that is the US subset of the 20 live locations; the article states the 20-location figure as verified on 2026-10-31 with a "Last verified" stamp. Kernel-version control, reboot rights and custom-image availability for the KVM line must be re-verified from the live KVM VPS page at draft time — **not** inherited from this outline.

---

## 6. Cross-Links (10 — all targets verified to exist on disk)

1. `/blog/vps-buying-guide/` — the baseline VPS selection guide (Step 5: billing, Step 6: support & ecosystem)
2. `/blog/nvme-vps-under-10-2026/` — budget NVMe picks, several of which ship Debian/Ubuntu images (the distro column in §5)
3. `/blog/cheap-vps-local-llm-inference-2026/` — always-on agent workloads on a budget box (the §10 "unpatchable box" inventory)
4. `/blog/best-north-america-vps-2026/` — NA region roundup feeding the §8 "who ships the image" discussion
5. `/blog/racknerd-deep-review-2025/` — the affiliate's own deep review (affiliate-label integrity: the CTA itself must still identify RackNerd as the affiliate)
6. `/blog/vps-pricing-trap-guide-2026/` — promo-vs-renewal pricing trap (the §10 "migrate the workload to a patchable image" cost note)
7. `/blog/lifetime-vps-deals-2026-real-cost-vs-marketing/` — why a locked-in annual price is the right shape when a distro's support window may end mid-term
8. `/blog/digitalocean-outage-august-2026/` — the site's prior incident-analysis piece, for the "provider incident ≠ provider quality" framing
9. `/blog/hostarmada-vps-review-2026/` — a managed VPS profile, for the §8 managed-vs-unmanaged kernel responsibility split
10. `/blog/serverhub-vps-review-2026/` — a second budget-VPS profile with multiple datacenters, for the §8 image and location comparison

**Deliberately excluded:** `cloud-outages-2026-redundant-vps-setup` (queued 2026-08-11, no live file), `vps-offsite-restore-backup-guide-2026` (queued 2026-09-06), `sovereign-cloud-data-loss-2026-offsite-backup` (queued 2026-09-18), `linux-kernel-escape-patches-august-2026-vps` (queued 2026-08-09 — adjacent subject but **no live URL**, and the article must not link a dead path), `vps-ssh-security-host-key-checks-2026` (queued 2026-10-29), `namecheap-outage-dns-email-vps-resilience-2026` (queued 2026-08-16) — all are queued-but-not-yet-published, so they have no live URL to link to yet.

---

## 7. Self-Check (Pre-Commit)

| Check | Result |
|-------|--------|
| Excluded merchant named anywhere in this document | 0 — verified by Python case-insensitive token count over the whole draft |
| CJK characters in this document | 0 — verified via the standard CJK-range regex over the whole draft |
| Deprecated language-prefix path written into prose | 0 — no language-prefix path appears anywhere in this document |
| Title length | 57 / 60 — Python `len()` on the final rendered string |
| Description length | 146 / 155 — Python `len()` on the final rendered string |
| H2 count | 10 |
| FAQ count | 5 |
| RackNerd CTA placements | 8 |
| Cross-links | 10 — every target path verified to exist on disk (1 excluded target caught and removed: `cloud-outages-2026-redundant-vps-setup` has no live file) |
| Slug collision | none — `linux-kernel-tcp-rce-cve-2026-98432-vps` absent from `published[]` (84 entries), `drafts[]` (55 entries) and `src/pages/blog/` (60 files) |
| Content-gap confirmation | 0 published articles and 0 queued outlines cover CVE-2026-98432, this use-after-free mechanism, this distro patch-status table, or the "no vendor fix exists" buyer problem — 11 angle tokens grepped across 60 blog files + 169 draft files + 68 vps profiles |
| Every fact in §1c traced to a body-fetched source | 42 / 42 — 9 vendor/API primaries + 1 body-fetched secondary, all HTTP 200 |
| Whitelisted provider set | all recommendations come from `providers.json`; the article names vendors only as **subjects** (distro vendors, the AI lab), never as affiliate destinations or recommendations |
| Vendor-fact verbatim discipline | Red Hat's severity statement, the Ubuntu tracker status values, the Debian fixed-version list and the kernel CNA's description are quoted from the source bodies, not paraphrased |
| Live-vs-stale severity conflict resolved | Red Hat's live API read on 2026-10-31 returns **9.8 / Critical**; the 2026-10-30 secondary report says 8.1. The draft uses the live dated value and states the "last verified" date. This must be re-checked at draft time — the value moved twice in two days |
| MPTCP uncertainty stated, not resolved | bound in §1f and §4 — the draft must present it as an open question |
| Publish cadence | Monday-only since the 2026-08-28 HCU pause → publish slot **2026-11-02** |
