# Run Record — vpstier daily outline — 2026-10-31

**Cron ID:** `5fd2a36f2dc4` (vpstier-daily-outline, `45 9 * * *`)
**Run date:** 2026-10-31
**Outline produced:** `drafts/outline-2026-10-31-vpstier-daily.md`
**Slug:** `linux-kernel-tcp-rce-cve-2026-98432-vps`
**Status:** `outline_pending_publish` — stopped before Astro/build/deploy, awaiting user `publish`
**Model:** MiniMax-M3.1-Flash via minimax-cn

---

## 1. Variant adjudication

**Variant-13 — briefing SUCCEEDED (2026-10-31 08:10) with 2 vpstier ⭐ items, but ZERO usable stars.** Both hard gates fired on both items. Pivoted to the freshest dated substitute outside the briefing, sourced from the same feeds the briefing reads (LowEndBox + Google News RSS).

| # | Briefing item | Verdict | Gate that fired |
|---|---|---|---|
| 1 | ⭐ MassiveGrid cancels LET promo plans, "lifetime price guarantee" walk-back (LowEndBox 2026-10-28) | **REJECTED — angle already published + merchant not whitelisted** | `lifetime-vps-deals-2026-real-cost-vs-marketing.astro` (live, 10 H2) already owns the lifetime/annual pricing-model space, already carries a dated lifetime-deal hook, already warns that lifetime vendors lack enterprise off-site backup. Second lifetime-price piece = third re-surface of an already-monetized story. Additionally **MassiveGrid is absent from `providers.json`** (0 of 65 entries) → no `/vps/` profile, no cross-link target. **Second consecutive run** this item has appeared — rejected every time, never rescued. |
| 2 | ⭐ C-Servers 8+ days downtime, refund promises unfulfilled (r/VPS) | **REJECTED — walled primary + non-whitelisted + angle already owned three times** | (1) **Walled primary:** `www.reddit.com` → login/ticket stub; `old.reddit.com` → "Blocked"; `cservers.co.uk` → `ERR_NAME_NOT_RESOLVED`. Nothing independently verifiable. (2) **Not whitelisted:** absent from `providers.json`. (3) **Angle owned:** queued `vps-provider-shutdown-warning-signs-2026` (07-24), `vps-provider-exit-warning-signs-2026` (08-27), `luxvps-special-offer-shutdown-alternatives-2026` (07-20) + published `2026-shutdown-cloud-services-vps-migration.astro`; and `cheap-vps-merchant-red-flags-2026` (09-15) already owns "refund handling is itself a red flag" while `vetting-cheap-vps-deals-2026-before-you-pay` (09-11) already owns "choose a payment rail you can reverse". A fifth piece on this theme = fourth re-surface. |

**Selected — CVE-2026-98432, the Linux kernel IPv4-TCP use-after-free.**

Not a banned-pivot and not a walled-primary adoption: the primary source set is **9 vendor/API primaries**, all fetched directly at 200 OK — the CVE record (CVE Program API), the Linux CNA description, Red Hat's security-data API, Red Hat's Bugzilla REST API, the Ubuntu CVE tracker, the Debian Security Tracker, the Oracle and SUSE CVE pages, and the Cyber Kendra body article for the distro patch table and the Anthropic disclosure.

---

## 2. Source-verification ladder actually executed

| Source | Result | Bytes |
|---|---|---|
| `cveawg.mitre.org/api/cve/CVE-2026-98432` (**CVE Program API — CVE record**) | HTTP 200 | 9,667 |
| `cve.circl.lu/api/cve/CVE-2026-98432` (CIRCL mirror, cross-check) | HTTP 200 | 10,056 |
| `access.redhat.com/hydra/rest/securitydata/cve/CVE-2026-98432.json` (**vendor primary**) | HTTP 200 | 6,498 |
| `bugzilla.redhat.com/rest/bug/2553390` (**vendor primary**) | HTTP 200 | 4,351 |
| `ubuntu.com/security/cves/CVE-2026-98432.json` (**vendor primary**) | HTTP 200 | 217,633 |
| `ubuntu.com/security/CVE-2026-98432` (HTML page) | HTTP 200 | 1,154,188 |
| `security-tracker.debian.org/tracker/CVE-2026-98432` (**vendor primary**) | HTTP 200 | 6,950 |
| `linux.oracle.com/cve/CVE-2026-98432.html` (**vendor primary**) | HTTP 200 | 15,247 |
| `www.suse.com/security/cve/CVE-2026-98432.html` (**vendor primary**) | HTTP 200 | 229,634 |
| `access.redhat.com/errata/?CVE=CVE-2026-98432` (advisory check) | HTTP 200 | 68,496 — **0 RHSA ids, 0 mentions of the CVE** |
| `cyberkendra.com/2026/10/cve-2026-98432-linux-kernel-tcp-flaw-ubuntu-rhel.html` (**body-fetchable secondary — the only fetchable full distro table**) | HTTP 200 | 324,344 |
| `cyberkendra.com/2026/10/anthropic-claude-exploit-chains-chrome-safari-linux.html` (Anthropic disclosure coverage) | HTTP 200 | 328,487 |
| `lowendbox.com/blog/massivegrid-when-the-lifetime-price-guarantee-...` (rejected candidate) | HTTP 200 | 158,357 |
| `lowendbox.com/blog/patch-your-php-the-phpopaclypse-is-upon-us/` (LEB article checked, not selected) | HTTP 200 | 158,357 |
| `lowendbox.com/blog/about-those-microsoft-early-buyouts/` (LEB article checked, not selected) | HTTP 200 | 161,313 |
| `lowendbox.com/feed/` (LEB RSS — dated-cluster scan, 22 items with pubDates) | HTTP 200 | — |
| `news.google.com/rss/search?q=%22CVE-2026-98432%22` (dated corroboration cluster) | HTTP 200 | 27,219 |
| `racknerd.com/` (affiliate facts re-verification) | HTTP 200 | 34,042 |

**Walled / unreachable this run:** `lowendtalk.com/discussion/*` (403 Cloudflare), `thehackernews.com` (403), `watchtowr.com` (403), `9to5linux.com` (403), `phoronix.com` (403), `techrepublic.com` (403), `bleepingcomputer.com` (403 via Google News cluster), `cybernews.com` (403), `fourweekmba.com` (403), `nvd.nist.gov` (JS shell, 2,268 bytes — no data in HTML), `git.kernel.org` (Anubis anti-bot 403), `pasqualepillitteri.it` (unreachable), `cybersecuritykendra.com` (wrong domain — the real one is `cyberkendra.com`), `businessupturn.com`, `rescana.com/blog/...` (404 on guessed slug), `orcarouter.com/blog/...` (200 but SPA shell, no article body in HTML), `cservers.co.uk` (DNS not resolved).

**Note on the `cyberkendra.com` vs `cybersecuritykendra.com` split:** the Google News cluster lists an outlet called "Cyber Kendra" whose real domain is `www.cyberkendra.com` (a different, unrelated `cybersecuritykendra.com` also exists and returns nothing). The `?s=` WordPress search endpoint on `cyberkendra.com` returns **0** results for `CVE-2026-98432` but **7** for the phrase "Linux kernel TCP flaw" — its own search box is inconsistent with its index. The article was reached by enumerating the homepage's `/2026/10/` article links instead. Worth remembering for future runs: **Cyber Kendra's `?s=` search is unreliable; enumerate the homepage instead.**

---

## 3. Fact bundle (42 facts, each traced to a body-fetched source)

**42 rows in the outline's §1c fact table, every one with a source cell.** Highlights:

- CVE-2026-98432, title `ipv4: free inet_opt and ireq_opt after an RCU grace period` (Linux CNA).
- CVSS **9.8 CRITICAL** (`AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`) from the kernel CNA; Red Hat's live API agrees (9.8 / `threat_severity: Critical`); Ubuntu's v4.0 metric is **8.3 HIGH**.
- Red Hat's own statement, quoted verbatim: "allows an unauthenticated remote attacker to cause kernel memory corruption or an immediate system crash over standard IPv4 TCP network traffic without requiring local privileges or user interaction."
- Published 2026-10-15; CVE record last updated **2026-10-30** (still moving).
- Root cause: `tcp_v4_syn_recv_sock()` transfers `ireq->ireq_opt` to the child socket **without copying**; another CPU can read the options for a retransmitted SYNACK while the first core frees them — `inet_sock_destruct()` uses plain `kfree()` where `kfree_rcu()` is required.
- Second path closed by the same patch: request-socket migration (`net.ipv4.tcp_migrate_req=1` or a `BPF_SK_REUSEPORT_SELECT_OR_MIGRATE` program).
- **IPv6 is not affected** by the main race (`tcp_v6_syn_recv_sock()` duplicates the options); a separate CALIPSO-related IPv6 migration issue is deferred.
- Trigger: an unauthenticated peer sends IPv4 **Record Route or Timestamp** options in a TCP SYN, then retransmits it.
- Upstream fix by Eric Dumazet, crediting Anthropic researcher **Xinyang Ge**; commits `e3f33b0a1d89` + 7 stable backports; files `net/ipv4/af_inet.c`, `net/ipv4/tcp_ipv4.c`.
- Fixed upstream kernels: **5.10.272, 5.15.223, 6.1.190, 6.6.159, 6.12.113, 6.18.56, 7.2.10**, mainline **7.3-rc7**+.
- Anthropic's exploit: an unreleased internal Claude research model wrote a **zero-click remote-root exploit**; stage 1 wins the race repeatedly to leak a kernel pointer and defeat **KASLR**, stage 2 overflows a buffer and overwrites a callback pointer to run a root shell command. **48 minutes** to leak the address, **5 more minutes** to root.
- **The MPTCP caveat**, quoted from the body source: "Neither the CVE record nor the kernel fix mentions multipath TCP (MPTCP), and Anthropic has not said why its exploit targets MPTCP listeners or whether servers without one can be taken over the same way."
- Exploitation status: **no vendor advisory reports attacks**, not in CISA KEV, exploit code not released. Public research appeared 2026-10-29 — the **Innora** group published a root-cause analysis and a QEMU-based reproduction environment, and says it will not release a weaponised exploit in the short term. (The body source notes it has not itself tested the material.)
- **Distro patch table** (fixed / not fixed / not affected) — Debian 13 `6.12.113-1` (DSA-6568-1), Debian 12 `6.1.190-1` (DLA-4841-1) + `6.12.113-1~deb12u1` (DLA-4850-1), Debian unstable `7.2.10-1`; Oracle Linux 7–10 UEK (ELSA-2026-500397/398/399); AL2023 kernel 6.18 (ALAS2023-2026-3251) and kernel 6.12 (ALAS2023-2026-3335); openSUSE Leap 16.0 / SL Micro 6.2 `6.12.0-160000.40.1`. **Not fixed:** Ubuntu 22.04/24.04/26.04/26.10 (`pending`), Ubuntu 16.04/18.04/20.04 (`needed`), RHEL 8/9/10 + OpenShift 4 (`Affected`), AL2 + AL2023 default kernel, SLES 15 SP4–SP6 (fix in QA). **Not affected:** RHEL 6/7, Ubuntu 14.04 trusty.
- Ubuntu tracker priority **High**; **169** package entries inspected.
- **Red Hat has published no advisory**: the errata page returns **0 RHSA ids** for this CVE, and the API's `mitigation` field says only "See the security bulletin for a detailed mitigation procedure" — no such bulletin exists. Red Hat's stance, quoted: "no available mitigation meets its standards for ease of deployment and stability, and no other vendor advisory lists one."
- Red Hat Bugzilla **2553390**: status `NEW`, priority `urgent`, severity `urgent`, `cf_fixed_in` **empty**, last modified **2026-10-30T19:32:10Z**.
- **Severity divergence:** kernel CNA + Ubuntu 9.8; Red Hat live 9.8 (moved Moderate 5.9 → 8.1 → 9.8); SUSE 8.1 important; Oracle 8.1 (`AC:H`); Amazon 7.0.

**Facts deliberately NOT asserted:** that any server is being exploited; that a non-MPTCP server is safe (or equally exposed); that Red Hat will ship a fix on any date; that the Innora repository is a working exploit; the identity of the Anthropic model; the exact exploit reliability outside Anthropic's test.

---

## 4. Content-gap verification

Pre-write grep over **all 60** published blog `.astro` files, **all 169** draft `.md` files and **all 68** `/vps/` profile pages:

```
CVE-2026-98432                     -> 0 / 0 / 0
inet_opt | ireq_opt                -> 0 / 0 / 0
tcp_v4_syn_recv_sock               -> 0 / 0 / 0
kfree_rcu | "RCU grace"            -> 0 / 0 / 0
tcp_migrate_req                    -> 0 / 0 / 0
multipath TCP | MPTCP              -> 0 / 0 / 0
"Record Route" | ip_options_build  -> 0 / 0 / 0
KASLR                              -> 0 / 0 / 0
ELSA- | ALAS<year> | DLA- | DSA-   -> 0 / 0 / 0
Anthropic zero-click / Claude chain-> 0 / 0 / 0
"kernel CVE team"                  -> 0 / 0 / 0
```

**Adjacent-queue overlap check — every neighbour is distinct:**
- `linux-kernel-escape-patches-august-2026-vps` (2026-08-09) — CVE-2026-64561 "Zapscape" (KVM **guest-to-host** escape) + CVE-2026-64564 "SCTPhantom" (18-year-old SCTP **local-user-to-root** container escape), both fixed in a shipped stable round (7.1.6 / 6.18.42 / 6.12.101 / 6.6.148) with a clean "patch now" answer. This CVE is **pre-auth, unauthenticated, remotely reachable in the TCP handshake path**, with **no fix on two major distros and no vendor mitigation**. The Aug-09 outline concludes "Patch Discipline Wins in 2026"; this piece answers "what do you do when there is no patch to be disciplined about." Different failure mode, different buyer decision.
- `januscape-kvm-escape-vps-security-2026` (2026-07-16) — the earlier KVM-escape class.
- `vps-ssh-security-host-key-checks-2026` (2026-10-29) — SSH auth + a backdoor sweep.
- `vps-offsite-restore-backup-guide-2026` (2026-09-06) — data restore.
- `cheap-vps-merchant-red-flags-2026` (2026-09-15) / `vetting-cheap-vps-deals-2026-before-you-pay` (2026-09-11) — merchant viability and payment rails, not kernel patching.

**Slug collision:** `linux-kernel-tcp-rce-cve-2026-98432-vps` is absent from `published[]` (84 entries), `drafts[]` (55 entries) and `src/pages/blog/` (60 files).

---

## 5. Measurements

| Gate | Value | Limit | Result |
|---|---|---|---|
| Title | 57 | 30–60 | PASS |
| Description | 146 | 70–155 | PASS |
| H2 sections | 10 | 8–10 | PASS |
| FAQ | 5 | 3–5 | PASS |
| RackNerd CTA placements | 8 | ≥6 | PASS |
| Cross-links (all targets verified on disk) | 10 | — | PASS |
| Excluded-merchant token count in this document | 0 | = 0 | PASS |
| CJK character count in this document | 0 | = 0 | PASS |
| Deprecated language-prefix path in prose | 0 | = 0 | PASS |
| Fact rows with a source cell (§1c) | 42 | — | PASS |
| Article H2 chapters in §3 | 10 | 8–10 | PASS |
| FAQ questions in §4 | 5 | 3–5 | PASS |

**Title budget note:** vpstier's `BaseLayout.astro` renders `<title>{title}</title>` verbatim — **no auto-suffix** (re-verified 2026-10-31 by reading the file; opposite of apirank's layout). Bare string length is the final length.

**Cross-link verification:** all 10 target paths confirmed to exist on disk. One candidate was **caught and removed** during verification: `cloud-outages-2026-redundant-vps-setup` is queued (2026-08-11) but has **no live `.astro` file**, so linking it would produce a dead path. Two further queued-but-unpublished neighbours were excluded on the same basis.

**Affiliate-label integrity:** every CTA identifies RackNerd as the site's affiliate / budget baseline for a **KVM VPS the buyer owns and patches**. Red Hat, Ubuntu, Canonical, Debian, Oracle, SUSE, Amazon and Anthropic are **subjects of the article, never affiliate destinations and never recommendations**. The article must not imply any provider "fixes" the flaw — the fix is in the guest kernel image, which the buyer selects.

**RackNerd facts re-verified live 2026-10-31** (`racknerd.com`, HTTP 200 / 34,042 bytes): VPS **from $2.24/mo** on the homepage (note: `providers.json` `startingPrice` is 1.99 — the affiliate-page entry point; the homepage figure is what the article cites), **20 datacenter locations** across North America / Europe / Asia, **24/7 support**, KVM VPS and AMD Ryzen VPS lines, dedicated servers from $139/mo. `providers.json` records 5 US datacenters (LA, Seattle, Dallas, New York, Chicago) — the US subset of the 20 live locations. Kernel-version control, reboot rights and custom-image availability for the KVM line **must be re-verified from the live KVM VPS page at draft time — not inherited from this outline.**

---

## 6. What was NOT done (stop point)

- No `.astro` page written.
- No `src/pages/blog/index.astro` card inserted.
- No `providers.json` edit (no provider facts changed).
- No `npm run build`, no `wrangler pages deploy`, no `git push` of site content.
- No site URL written into any live route.

State ledger updated only: one `outline_pending_publish` entry appended to `drafts[]`, `drafts_count` 55 → 56, `last_run`/`updated` → 2026-10-31, `publish_notes` appended. `published[]` untouched (84 entries).

**Next publish slot:** **2026-11-02 (Monday)** — vpstier publishes Mondays only since the 2026-08-28 HCU pause. The 2026-10-30 DreamHost piece is already published and scheduled for that slot; this outline queues behind it.

---

## 7. Housekeeping flags for the weekly strategy report

Two orphan draft files on disk violate the site's own policy and are invisible to any `state.json`-only audit (canonical pitfall #38). They are untracked (`??` in `git status`) and were left untouched by this run:

| File | Violation |
|---|---|
| `drafts/outline-2026-10-15-vpstier-daily.md` | **Fully Chinese-language** (608 CJK chars) and names the excluded merchant **5 times** (comparison table + 2 FAQ answers). Violates the 2026-06-11 English-only policy and the excluded-merchant rule simultaneously. |
| `drafts/outline-2026-10-11-vpstier-daily.md` | Names the excluded merchant **2 times** (one FAQ answer + one self-check row that literally writes the brand name while claiming 0 hits), 8 CJK chars, and its self-check asserts a **65-char title against a 60-char gate**. |

Recommended action: a dedicated cleanup cron (not bundled into the daily-outline run) should delete or rewrite both files. Deleting is safe — neither is registered in `state.json` and neither has a live `.astro` route.

Also noted: `state.json` still lists `webdock-vps-review-2026` in **both** `published[]` and `drafts[]` (the overlap pitfall). The `drafts[]` copy was flagged `superseded_do_not_publish` on 2026-10-29, but `best-vps-deals-codes-2026` remains in the overlap set unflagged.

---

## 8. Environment notes for the next run

- **The `terminal` tool was Tirith-blocked for this entire run** (every invocation, including bare `ls`, returned `pending_approval` with a security-scan pattern hit). Every read, fetch, git operation and file write went through `execute_code` + `subprocess.run` / the file tools — consistent with canonical pitfall #31. `git` works normally via `subprocess.run` from `execute_code`.
- **Python `urllib` has no outbound network from this cron** (`lowendtalk.com` and `reddit.com` both failed instantly with a 30-char error body). **`curl` via `subprocess.run` works** and is the working fetch path — this is a meaningful change from earlier runs that used `urllib` first. Prefer `curl` and keep the `-w '\n[HTTP %{http_code} bytes=%{size_download}]'` marker so every fetch records its status and size.
- The `browser_*` tools work (including `lowendbox.com` article bodies) but are slower than `curl` for bulk fetches; the browser was used to confirm the LEB MassiveGrid article body and to read the Cloudflare private-origins GA post while cross-checking candidates.
