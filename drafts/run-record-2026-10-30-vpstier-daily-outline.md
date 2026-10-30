# Run Record — vpstier daily outline — 2026-10-30

**Cron ID:** `5fd2a36f2dc4` (vpstier-daily-outline, `45 9 * * *`)
**Run date:** 2026-10-30
**Outline produced:** `drafts/outline-2026-10-30-vpstier-daily.md`
**Slug:** `dreamhost-breach-2026-password-reuse-vps`
**Status:** `outline_pending_publish` — stopped before Astro/build/deploy, awaiting user `publish`
**Model:** MiniMax-M3.1-Flash via minimax-cn

---

## 1. Variant adjudication

**Variant-0 (briefing succeeded; both vpstier ⭐ picks adjudicated; one selected, one rejected on content-grounded grounds).**

The 2026-10-30 08:16 briefing produced two ⭐ vpstier items plus one non-star. The non-star (ServerHost $16.99/yr + $500 giveaway) is a vendor self-promotion post and was not considered further.

| # | Briefing item | Verdict | Gate that fired |
|---|---|---|---|
| 1 | ⭐ MassiveGrid cancels LET promo plans, "lifetime price guarantee" walk-back (LowEndBox 2026-10-28) | **REJECTED — angle already published on vpstier + merchant not whitelisted** | `lifetime-vps-deals-2026-real-cost-vs-marketing.astro` is a live 10-H2 article that already owns the lifetime/annual pricing-model space, already carries a dated lifetime-deal hook, and already warns that lifetime vendors lack enterprise-grade off-site backup. Second lifetime-price piece = third re-surface of an already-monetized story (same staleness rule that rejected the Contabo back-to-school promo on 2026-09-18). Additionally **MassiveGrid is absent from `providers.json`** (0 of 65 entries) — no `/vps/` profile, no cross-link target, non-whitelisted merchant. |
| 2 | ⭐ DreamHost File Manager failure → account-wide email/FTP password reset (LowEndBox 2026-10-26) | **SELECTED** | Body-verified across the news source **and** DreamHost's own official 2026-10-29 disclosure. New archetype on vpstier: credential-exposure buyer-guide. Content gap confirmed at 0. |

**Selected — the DreamHost File Manager exploitation and credential rotation.**

This is not a banned-pivot and not a walled-primary adoption: the primary source is the **vendor's own disclosure**, fetched directly.

---

## 2. Source-verification ladder actually executed

| Source | Result | Bytes |
|---|---|---|
| `dreamhost.com/news/announcements/october-security-incident/` (**vendor primary, 2026-10-29**) | HTTP 200 | 285,360 |
| `lowendbox.com/blog/dreamhost-urges-affected-customers-to-reset-all-email-and-ftp-passwords/` | HTTP 200 | 165,229 |
| `lowendbox.com/blog/massivegrid-when-the-lifetime-price-guarantee-turns-out-to-not-be-quite-so-lifetime/` (rejected candidate) | HTTP 200 | 157,397 |
| `lowendbox.com/blog/proton-unleashes-massive-footgun-and-horrifies-its-user-community/` (considered, rejected — off-ICP: end-user privacy suite, not VPS) | HTTP 200 | — |
| `dreamhost.com/news/` (index — located the incident post) | HTTP 200 | 295,770 |
| `status.dreamhost.com/` | HTTP 200 | 93,669 |
| `status.dreamhost.com/api/v2/incidents.json` + `/summary.json` + `/components.json` | **not served** (statuspage API not exposed on this host) | — |
| `status.dreamhost.com/history` + `/incidents` | HTTP 404 | — |
| `racknerd.com/` (affiliate price + datacenter re-verification) | HTTP 200 | 34,035 |
| `racknerd.com/BlackFriday/` + `/NewYear/` (entry-plan spec table) | HTTP 200 | 87,794 |
| `racknerd.com/Locations/` | HTTP 404 | — |
| `racknerd.com/KVM-VPS/` + `/VPS/` | HTTP 404 | — |

**Corroboration:** the DreamHost timeline (status-page entries with PDT timestamps) comes from the LowEndBox piece quoting the status page directly; the scope, impact and remediation come from DreamHost's own disclosure. Both are body-fetched. The two are consistent — no conflict found between the news summary and the vendor statement.

**Note on `status.dreamhost.com`:** the status page is a JS-driven statuspage instance with no public JSON API on this host. The current state was read from the rendered HTML (all components Operational as of the 2026-10-30 fetch), but the **historical incident entries were not re-fetchable** — those come from the LowEndBox quote of the status page. This is stated rather than papered over.

---

## 3. Fact bundle (19 facts, each traced to a body-fetched source)

| # | Fact | Source |
|---|---|---|
| 1 | Discovered the afternoon of **Friday, 2026-10-23** | DreamHost official disclosure |
| 2 | Entry point: an **unauthorized third party** exploited a vulnerability in the **third-party software** behind the browser-based File Manager at `files.dreamhost.com` | DreamHost official disclosure |
| 3 | Harvested: **FTP/SFTP usernames and passwords** of users who logged into File Manager before detection | DreamHost official disclosure |
| 4 | Also reached certain webmail systems; obtained logins of a **limited number** of webmail users | DreamHost official disclosure |
| 5 | Exposure window: **~August 2026 → 2026-10-23** (anyone who logged into File Manager in that window) | DreamHost official disclosure |
| 6 | Scope: "a fraction of email and FTP/SFTP accounts hosted at DreamHost, **well under approximately 10%**" | DreamHost official disclosure |
| 7 | "In a small number of cases, we believe the unauthorized third party **may have used those credentials to view mailbox contents**" — those customers contacted individually | DreamHost official disclosure |
| 8 | "**no evidence** that the unauthorized third party accessed control panel logins or customer billing details"; no full card numbers stored (third-party processor) | DreamHost official disclosure |
| 9 | Response: File Manager servers taken offline; passwords of impacted accounts reset; **active sessions terminated the same day** | DreamHost official disclosure |
| 10 | Status timeline: 10-23 14:20 PDT investigating → 10-23 17:20 File Manager offline, webmail users signed out, precautionary resets begin → 10-23 22:13 resets extended to some email and FTP/SFTP users → 10-24 10:37 resets complete → 10-25 21:32 PDT still unavailable | LowEndBox 2026-10-26 quoting the status page |
| 11 | Recovery model: only the **primary account owner or a privileged user** can set new passwords from the control panel; users without panel access must contact the account owner | DreamHost official disclosure + LowEndBox |
| 12 | A changed password may take **up to 15 minutes** to take effect | DreamHost official disclosure |
| 13 | DreamHost **never emails asking for your password**; email/FTP/SFTP users do **not** receive automated reset/verify/confirm messages — such mail is phishing | DreamHost official disclosure + LowEndBox |
| 14 | Post-incident hygiene: check each mailbox for **unfamiliar forwarding rules and filters** | DreamHost official disclosure + LowEndBox |
| 15 | Remediation: affected server preserved for forensics; File Manager **rebuilt and relaunched** with added precautions and enhanced monitoring; internal credentials rotated; **outside security and forensics experts retained**; other customer-facing tools under review for similar vulnerabilities | DreamHost official disclosure |
| 16 | Regulatory: applicable regulators notified, required initial disclosures made, formal notices to follow | DreamHost official disclosure |
| 17 | Not related to recent **PHP updates**; PHP servers patched within hours of patch availability, and the WAF blocked **tens of thousands of intrusion attempts** before release | DreamHost official disclosure |
| 18 | Sitewide notice emails went out Friday evening and over the weekend; **those emails do not ask for your password** | DreamHost official disclosure |
| 19 | LowEndTalk member report on the rejected MassiveGrid story: **"More than 3 times what I paid before"**; provider cites memory/storage costs rising **4–10×** industry-wide; LET offer text said *"Your discounted rate is locked in forever. No sneaky price hikes—ever."* | LowEndBox 2026-10-28 (rejected candidate, recorded for the rejection rationale) |

**Facts deliberately NOT asserted:** the number of affected accounts is not disclosed ("the company has not disclosed how many accounts were affected" — LowEndBox); "may have used those credentials to view mailbox contents" is stated as the vendor's belief, not a confirmed count; the specific third-party File Manager software product is not named by DreamHost; the identity of the unauthorized third party is unknown.

**Language-integrity note:** the official disclosure contains **0 occurrences** of the word "breach" (verified by regex over the fetched body). The vendor's terms are "security incident" and "unauthorized third party". The outline's *title* uses the reader-facing word "Breach"; the article body must attribute the vendor's language precisely and must not put the word "breach" in DreamHost's mouth.

---

## 4. Content-gap verification

Pre-write grep over **all 59** published blog `.astro` files and **all 149** draft `.md` files:

```
password reuse / reuse password   -> 2 hits (both 2026-10-29 SSH-hardening outline)
reuse -> VPS/server linkage        -> 0 hits
credential rotation                -> 1 hit (2026-09-02 Oracle free-tier outline)
webmail                            -> 0 hits
ftp credential harvesting          -> 0 hits
filter / forwarding rule           -> 3 hits (unrelated add-provider notes)
account owner must reset           -> 0 hits
```

**Adjacent-queue overlap check — every neighbour is distinct:**
- `vps-offsite-restore-backup-guide-2026` (2026-09-06) — data restore, not credential rotation.
- `namecheap-outage-dns-email-vps-resilience-2026` (2026-08-16) — control-plane concentration during an outage; no breach, no credential exposure.
- `cloud-outages-2026-redundant-vps-setup` (2026-08-11) — redundancy topology, not incident credentials.
- `sovereign-cloud-data-loss-2026-offsite-backup` (2026-09-18) — data durability, not credential reuse.
- `cheap-vps-merchant-red-flags-2026` (2026-09-15) — merchant viability signals, not a credential incident.
- `vps-ssh-security-host-key-checks-2026` (2026-10-29, yesterday) — SSH key verification and Ebury on the box; the reused-password angle there is the **operator's own SSH password**, not a provider-issued FTP/webmail credential reaching a VPS. Different surface, different article.

**Slug collision:** `dreamhost-breach-2026-password-reuse-vps` is absent from `published[]` (83 entries), `drafts[]` (55 entries) and `src/pages/blog/` (59 files).

**Rejected-candidate collision check:** the published `lifetime-vps-deals-2026-real-cost-vs-marketing.astro` H2 list was extracted and confirms the "lifetime" pricing-model space is already owned (10 H2s incl. *The Pricing-Model Risk Matrix*, *The 5-Question Checklist Before You Click "Buy"*, *When a "Lifetime" Deal Is the Right Choice*).

---

## 5. Measurements

| Gate | Value | Limit | Result |
|---|---|---|---|
| Title | 51 | 30–60 | PASS |
| Description | 154 | 70–155 | PASS |
| H2 sections | 10 | 8–10 | PASS |
| FAQ | 5 | 3–5 | PASS |
| RackNerd CTA placements | 8 | ≥6 | PASS |
| Cross-links (all targets verified on disk) | 10 | — | PASS |
| Excluded-merchant token count in this document | 0 | = 0 | PASS |
| CJK character count in this document | 0 | = 0 | PASS |
| Deprecated language-prefix path in prose | 0 | = 0 | PASS |

**Title budget note:** vpstier's `BaseLayout.astro` renders `<title>{title}</title>` verbatim — **no auto-suffix** (re-verified 2026-10-30 by reading the file, opposite of apirank's layout). Bare string length is final length.

**Affiliate-label integrity:** every CTA identifies RackNerd as the site's affiliate / budget baseline for a self-controlled VPS. DreamHost is the case study, never a recommendation and never an affiliate destination. `/blog/dreamhost-review/` and `/vps/dreamhost/` appear as editorial cross-links only.

**RackNerd facts re-verified live 2026-10-30:** homepage shows "VPS from $2.24/mo", 20 datacenter locations across North America / Europe / Asia, Inc. 5000 (2026 #3693 National), 24/7 support; Black Friday page shows the 1 GB KVM special at **$21.99/yr** (1 vCPU, 20 GB SSD, 1 GB RAM, 3 TB transfer, 1 Gbps port, full root, 1 IPv4, KVM/ctrl panel), 2 GB $35.99/yr, 4 GB $59.99/yr. `providers.json` records 5 US datacenters (LA, Seattle, Dallas, New York, Chicago) — that is the US subset of the 20 live locations; the article states the 20-location figure as verified on 2026-10-30.

---

## 6. What was NOT done (stop point)

- No `.astro` page written.
- No `src/pages/blog/index.astro` card inserted.
- No `providers.json` edit (DreamHost entry unchanged — no factual correction was needed; its data is still accurate).
- No `npm run build`, no `wrangler pages deploy`, no `git push`.
- No site URL written into any live route.

State ledger updated only: one `outline_pending_publish` entry appended to `drafts[]`, `drafts_count` 55 → 56, `last_run`/`updated` → 2026-10-30, `publish_notes` appended. `published[]` untouched (83 entries).

**Next publish slot:** **2026-11-02 (Monday)** — vpstier publishes Mondays only since the 2026-08-28 HCU pause (last publish 2026-09-12).
