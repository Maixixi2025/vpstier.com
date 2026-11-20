# Run Record — VPSTier Daily Outline — 2026-11-20

**Cron:** `5fd2a36f2dc4` (vpstier-daily-outline)
**Run time:** 2026-11-20 ~00:05–01:20 UTC (session clock 2026-11-20 00:00:34 UTC at start)
**Variant:** **variant-0** — briefing SUCCEEDED, 1 of 2 vpstier stars selectable
**Archetype:** web-server-layer RCE + escalation-chain buyer-guide (NEW)
**Output:** `drafts/outline-2026-11-20-vpstier-daily.md`
**Status:** `outline_pending_publish` — awaiting user `publish`

---

## 1. Briefing adjudication

The daily briefing (`3ea88f8bb2d0`, output file `2026-11-20_07-06-38.md`) **succeeded** and carried two vpstier stars.

| # | Item | Decision |
|---|---|---|
| 1 | NGINX two HTTP/2 unauthorized RCE — CVSS 9.2, fixed 11/18, NGINX on 225M+ sites | **SELECTED** — framing confirmed against the vendor primary; count corrected upward (five RCE paths across nine CVEs) and the kernel escalation chain added |
| 2 | ServerHost Black Friday warm-up — 2GB Ryzen/i9 VPS $22.99/yr, $100 giveaway | **REJECTED** — not whitelisted (absent from `providers.json`, 0 of 65) + captured by the queued Black Friday restock outline and the published Black Friday deal article |

Briefing item 2 was **body-fetched** before rejection (LowEndBox, HTTP 200, 159,751 B, `datePublished` 2026-11-19T12:00:04Z) so the rejection rests on confirmed grounds rather than assumed ones (pitfall #62). The comment thread in that body also contains a customer posting an unverified uptime block claiming an ISP/ASN that does not match the merchant's own network — a further reason not to build a review on that source.

**No provider is named anywhere in the outline.** The rejected merchant is referred to by category only.

---

## 2. Primaries — 6 bodies read, plus machine-readable vendor/distro trackers

| # | Source | HTTP / size | What it supplied |
|---|---|---|---|
| 1 | **NGINX security advisories** — `nginx.org/en/security_advisories.html` | 200, 28,421 B | The vendor-primary source of truth. 78 advisory entries; **35 with 2026 CVEs** (severity mix: 24 medium, 5 major, 3 minor, 3 low); 2 with 2025 CVEs. Nine entries in the 18-Nov batch; affected ranges and fixed versions per CVE. |
| 2 | **NGINX CHANGES** — `nginx.org/en/CHANGES` + `/CHANGES-1.30` | 200, 359,612 / 351,646 B | Both dated **18 Nov 2026**. The verbatim upstream wording per CVE, including the credit lines "Xint.io" and "Albert of Vexera AI". |
| 3 | **Xint Research write-up** — `xint.io/blog/nginx2root-remote-code-execution` | 200, 455,913 B | The five-CVE configuration table, the four-step exposure check with the combined-results matrix, the connection-statistics investigation method, the mitigation section, the disclosure timeline, and the SCTP kernel analysis. |
| 4 | **Wiz Research write-up** — `wiz.io/blog/nginx-http2-rce-vulnerabilities` | 200, 492,526 B | Independent discovery; the 225-million-websites figure; the "ordinary static files over TLS, no backend needed" detail; the explicit statement that Wiz is **not** releasing its PoCs; the ASLR caveat in the vendor's own framing. |
| 5 | **Security Affairs** — `securityaffairs.com/203440/hacking/nginx2rootai-...html` | 200, 129,940 B, dated 19 Nov 2026 | The Censys figure ("nearly 10M Internet services running vulnerable NGINX versions", attributed to Censys' CEO) and the Shodan 10-Nov scan figure (98.9% of versioned NGINX servers on a vulnerable release). |
| 6 | **CVE Program API** — `cveawg.mitre.org/api/cve/<id>` | 200 ×3 | Full CNA records for CVE-2026-123007 / 123633 / 121810: assignee `f5`, `datePublished` 2026-11-18T15:23Z, `dateUpdated` 2026-11-19, CVSS 3.1 **8.1 HIGH** + CVSS 4.0 **9.2 CRITICAL**, per-version affected ranges, and the upstream fix references. |

Machine-readable trackers read live (all HTTP 200):

- **Debian Security Tracker** — per-release fixed versions, **DLA-4918-1** / **DSA-6642-1**, upstream fix commits (`b89c4100…` release-1.30.7 for 123007; `0c87dd1d…` for 123633), and the note that `debian.org/security/2026/` is JS-gated (PoW challenge) while the tracker is not.
- **Ubuntu CVE tracker JSON** — per-release package status for both CVEs (`published` 2026-11-18T15:23:00): upstream released in `1.31.9,1.30.7`; jammy `1.18.0-6ubuntu14.23`; noble `1.24.0-2ubuntu7.20`; resolute `1.28.3-2ubuntu1.13`; stonking `1.30.4-7ubuntu1.2`; ESM pockets for xenial/focal/bionic; trusty **not-affected** ("code not present" — 1.4.6 has no HTTP/2 and no flow control).
- **Red Hat security data API** — `threat_severity: Critical`, CWE-787 (123007) / CWE-825 (123633), all RHEL nginx packages **Affected**, and the vendor's own mitigation text. Bugzilla REST: **2575895** and **2576209**, both `priority: urgent` / `severity: urgent`, both with **empty `cf_fixed_in`** — no RHSA build published as of the read.
- **GitHub release API** — `release-1.31.9` published `2026-11-18T15:54:06Z`; `release-1.30.7` published `2026-11-18T15:56:40Z`. Both bodies list the same CVE set.
- **CISA KEV** — the official CISA feed URLs returned **403** from this sandbox; the authoritative GitHub mirror `cisagov/kev-data` returned **200**, 1,786 entries. **None** of the five NGINX CVEs is listed.

Corroboration: **Google News RSS**, 52 items across ~28 outlets dated 2026-11-17 → 2026-11-19. **6 bodies read** (the six above); the remaining ~22 are **headline+date only** and are labelled as such in the outline.

Walled/failed this run (recorded so the next run does not retry blind): `thehackernews.com` **403**; `securityboulevard.com` **403**; `ox.security` **403**; `rapid7.com/blog/post/...` **404** (site search returns 200 but no matching slug); `securityaffairs.com/?s=` **200** but its article links are not in the markup — the **Atom feed** (`securityaffairs.com/feed/`) is the working route; `helpnetsecurity` / `infosecurity-magazine` / `cyberscoop` / `aikido` / `qualys` **404** on guessed slugs; `cisa.gov` KEV feed **403**; `lists.debian.org` **PoW-challenged**; `r.jina.ai` proxy **403**; `debian.org/security/2026/dsa-6642-1` **JS-gated**. `nginx2root.com` returned **200** but is a 422-char landing page linking back to the Xint write-up — no independent content.

---

## 3. Why this topic won

1. It is the **freshest dated, highest-impact** item available: the release shipped **18 Nov 2026**, and the cluster was still producing dated items on 19 Nov (the day of this run).
2. It is a **genuine VPS-buyer** story, not a generic web-security story: NGINX is the default front door on self-hosted boxes and the flagship bug has been present since **1.9.5 (2015)**.
3. It carries a **vendor-primary-verifiable** fact set — the advisory list, the changelog, the CVE API and the Debian/Ubuntu/Red Hat trackers all agree, and each can be re-read live at draft time.
4. It produced a **genuinely new angle** that no outlet led with: the SCTP **kernel** chain to host root, demonstrated from inside a Docker container. That is the part that converts "update your web server" into "understand whether a web-server compromise becomes a host compromise" — which is a VPS decision, not a webops decision.
5. **Content gap confirmed**: zero matches for `nginx2root`, `CVE-2026-123007`, `CVE-2026-123633`, `CVE-2026-121810`, `CVE-2026-123634`, `CVE-2026-125283`, `send_window`, `flow control`, `worker_connections`, `http2 off`, `1.31.9`, `1.30.7`, `heap buffer overflow`, `install sctp`, `DLA-4918`, `DSA-6642`, `Xint`, `Vexera`, `Wiz Research` across published blog, published provider profiles and every queued outline.

---

## 4. Collision discrimination (nearest neighbours — cleared, not assumed)

| Neighbour | Discriminator |
|---|---|
| `php2shell-cve-2026-109618-php-rce-vps` (queued 11-08) | Different **layer**: the PHP interpreter *below* the web server vs the web server itself. Different CVEs, different patch command, different artifact set. |
| `linux-kernel-tcp-rce-cve-2026-98432-vps` (queued 10-31) | Also a kernel RCE, but a **guest-kernel, pre-auth TCP-path** flaw whose editorial question is "what do I do when there is no patch?" This one ships a patch — the opposite question. |
| `linux-kernel-escape-patches-august-2026-vps` (queued 08-09) | Owns Zapscape / SCTPhantom — **guest→host KVM escapes** (CVE-2026-64561 / 64564). This piece's kernel element is a **separate, differently-disclosed SCTP use-after-free (v4.15, 2018)** used as a **post-exploitation escalation chain** (app → host), the opposite direction of travel. Shared word "SCTP" is vocabulary, not argument. |
| `dreamhost-breach-2026-password-reuse-vps` (published) | Credential rotation for a provider-side credential incident. Orthogonal. |
| `2026-black-friday-cheap-vps-under-25` (published) | Owns the Black Friday deal tables. Orthogonal. |

`published[]` ∩ `drafts[]` overlap remains the same two pre-existing slugs (`best-vps-deals-codes-2026`, `webdock-vps-review-2026`) — unchanged, still flagged.

---

## 5. GSC context (live pull, this run)

90-day window 2026-08-21 → 2026-11-19, pulled live through the canonical helper `/root/.hermes/scripts/gsc_daily_report.py` (`get_valid_token()` + `fetch_gsc(...)`, pitfall #52 — no hand-rolled OAuth):

- **1,332 impressions across 54 pages**; the **homepage absorbs 78.2%** at **position 85.0**.
- Top queries are all head terms: `best vps` 69 impr pos 85.0, `best vps provider` 74 impr pos 84.4, `best vps for ai agents` 71 impr pos 74.4, `best vps providers` 33 impr pos 86.2, `best unmanaged vps` 6 impr pos 85.8.
- Best-performing individual pages: `/about/` 12 impr pos 3.4, `/blog/` 25 impr pos 5.2, `/blog/aliyun-vps-review-2026/` 42 impr pos 5.0, `/blog/2026-black-friday-cheap-vps-under-25/` 5 impr pos 7.4.

**Read:** the homepage is still absorbing head terms while the article library sits at position 3-9 on a handful of pages. Therefore today's piece must target a **specific high-intent query** (`nginx http2 rce`, `nginx 1.31.9`, `nginx patch vps`) and must carry internal links into the existing articles — not another generic "best VPS" roundup.

---

## 6. Editorial constraints written into the outline (binding on the draft)

1. The count is **nine CVEs fixed, five RCE paths** — the briefing's "two" is corrected, not repeated.
2. Vendor severity labels ("major"/"medium") and CNA CVSS (3.1 8.1 / 4.0 9.2) are quoted as **two separate facts**, never merged.
3. The **ASLR caveat is load-bearing**: crash is trivial and unauthenticated; code execution needs an ASLR bypass.
4. **Not in CISA KEV**, and Wiz is not releasing PoCs → "no confirmed in-the-wild exploitation", stated plainly.
5. The kernel SCTP flaw has **no published CVE id** → described as unnumbered; none invented.
6. It is a **container escape to host root**, never described as a VM/hypervisor escape.
7. Distro versions ≠ upstream versions; check the **package** version, not `nginx -v`.
8. "Disable HTTP/2" blocks **two of five** — stated explicitly, since that is the most mis-sold mitigation in current coverage.
9. A **reload does not replace the running binary** — restart is part of the procedure.
10. Red Hat has **no published fix build** (empty `cf_fixed_in` on both urgent bugs).
11. Affiliate-label integrity: every CTA names RackNerd as RackNerd or as an alternative/hosting baseline. Live prices read this run: **from $2.24/mo**; specials **$15.98 / $27.98 / $47.98 / $74.98 / $94.98 per year** (1/2.5/4/6/8 GB KVM, 1 Gbps port, 1 IPv4, full root, 20 datacenter locations). **The stale $1.99/mo figure on this site's own RackNerd provider page is excluded** and flagged for a separate correction pass.
12. No deprecated-language route referenced; English-only.
13. No excluded merchant named in any mention class, including the rationale and the self-check rows.

---

## 7. Self-check result

Title **55/60**, description **149/155** — both computed with Python `len()` on the final rendered strings before the self-check row was written. H2 count **10 declared / 10 present** (re-parsed from the saved file). FAQ **5**. Affiliate placements **8** (minimum 6). Cross-links **9**, every route verified to exist on disk this run. Slug `nginx2root-2026-vps-rce-patch-guide` absent from both `published[]` and `drafts[]`. Excluded-merchant zero-check, deprecated-language-path zero-check and non-English-character zero-check: **0 / 0 / 0**.

`BaseLayout` re-verified this run: `src/layouts/BaseLayout.astro` line 18 is `<title>{title}</title>` — no auto-suffix, so the source title length is the final title length.

---

## 8. Flagged for the user (not fixed from a daily-outline slot)

1. **The site's own RackNerd provider page is stale** — `/vps/racknerd/` states `$1.99/mo` in its title, description and body copy, and "8 datacenters". The live vendor site shows **from $2.24/mo** and **20 datacenter locations** (verified 2026-11-20). Needs a correction pass in a publish slot; today's article uses the live figures and does not propagate the stale ones.
2. **Pre-existing zh-language carry-over** — three tracked files remain: two stale zh-language outline drafts under `drafts/` and one zh-language Astro page under `src/pages/`. Unchanged, still the standing cleanup item (not part of a daily-outline run).
3. **`published[]` ∩ `drafts[]` overlap = 2** (`best-vps-deals-codes-2026`, `webdock-vps-review-2026`) — unchanged.
4. **Three consecutive cron failures before this run** — 2026-11-17 and 2026-11-18 both failed with `RuntimeError: Request payload too large (413). Cannot compress further.`; 2026-11-19 failed with a provider-side `403 AccountOverdueError` (the request failed because your account has an overdue balance). Both are upstream/provider-side failures rather than content failures, and today's run completed normally — but the billing condition behind the 11-19 error is worth checking, since it will keep failing until the account balance is settled.
5. **The 2026-08-09 `linux-kernel-escape-patches-august-2026-vps` outline remains queued and unpublished**, and its SCTP content is the nearest neighbour to today's kernel-chain material. If both are published, today's §7 should link to it explicitly rather than re-explaining the August round.
