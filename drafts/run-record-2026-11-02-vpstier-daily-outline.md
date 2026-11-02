# Run Record — vpstier daily outline — 2026-11-02

**Cron ID:** `5fd2a36f2dc4` (vpstier-daily-outline, `45 9 * * *`)
**Run date:** 2026-11-02
**Outline produced:** `drafts/outline-2026-11-02-vpstier-daily.md`
**Slug:** `hosting-account-suspension-blast-radius-2026`
**Status:** `outline_pending_publish` — stopped before Astro/build/deploy, awaiting user `publish`
**Model:** MiniMax-M3.1-Flash via minimax-cn

---

## 1. Variant adjudication

**Variant-9 — briefing SUCCEEDED (2026-11-02 08:06) but ALL three vpstier items failed a hard gate; substituted the freshest dated, body-verifiable story found outside the briefing via the same feeds the briefing reads.**

| # | Briefing item | Verdict | Gate that fired |
|---|---|---|---|
| 1 | ⭐ MassiveGrid cancels its LET "lifetime price guarantee" (LowEndBox 2026-10-28) | **REJECTED** | Published-angle collision + non-whitelisted merchant. `lifetime-vps-deals-2026-real-cost-vs-marketing.astro` (live, 10 H2) already owns the lifetime/annual pricing-model space; the merchant is **absent from `providers.json`** (0 of 65). **Fourth consecutive run** (10-30, 10-31, 11-01, 11-02) — rejected every time, never rescued. |
| 2 | RackNerd fall giveaway + VPS from $21.99/year (LowEndBox 2026-11-01) | **REJECTED** | Off-shape + self-referential. A promo roundup for the site's **own affiliate** is not a VPS industry story, and the seasonal-discount framing is already owned three times over (published `2026-black-friday-cheap-vps-under-25.astro`, published `lifetime-vps-deals-2026-real-cost-vs-marketing.astro`, queued `cheap-vps-back-to-school-promo-eval-2026`). Retained only as a **price anchor** ($21.99/year = what a cheap entry-level VPS actually costs per year at renewal). |
| 3 | ⭐ r/VPS: "Hostinger suspended my server and they are asking for business/affiliation documents" + C-Servers 8-day downtime / refund withdrawn | **REJECTED** | Stale re-surface + already captured + non-whitelisted. The briefing presented the Reddit item as a **2026-11-01** incident; the Brave index returns the **identical title** attributed to **r/Hostinger, dated October 9, 2015** — an 11-year-old thread. The C-Servers half resolves to a LowEndTalk thread dated **2026-08-21**, C-Servers is **absent from `providers.json`**, and the angle is **already captured** by the queued `cheap-vps-merchant-red-flags-2026` (2026-09-15), whose red flag #3 is *"a locked client area with no 'decline' option"*. |

---

## 2. The selected story — found outside the briefing

A five-outlet, dated, body-verified cluster the briefing did not carry: **on 2026-10-28 a hosting provider suspended an entire hosting account without notice and without citing any court order, and the domain never came back.**

The trigger was an abuse report categorised **"Fraud/Scam"**; a support specialist told the account holder's colleague that **"unsuspension is not negotiable in this case"** (6:48 a.m. support call). The affected site was a **12-year-old** archive of a working journalist's output. The underlying dispute concerned **one article** published in 2019.

**Why this beat every briefing item:** the site's coverage inventory has nothing on it. Queued material covers *merchant exit* (a host vanishing), *jurisdictional risk* (a host sanctioned), and *seasonal promo* (a host's pricing games). None covers the far more common case — **a live, healthy, whitelisted provider suspending a healthy account because someone else filed a report.** That is what happened, and it is a structural question every buyer can act on.

**The angle is the blast radius, not the incident:** the provider did not take down one URL, it took down a domain, its subdomains, and everything else on the account. A buyer running three sites from one account is exposed to a single complaint taking out all of them at once.

---

## 3. Source-verification ladder actually executed

| Source | Result | Bytes | What it gave |
|---|---|---|---|
| `maktoobmedia.com/post?id=116828&slug=twelve-years-of-journalism...` | HTTP 200 | 219,856 | **Primary narrative** — full chronology, the 52-URL Lumen record, the four questions put to the provider |
| `countercurrents.org/2026/10/the-arbitrary-takedown-of-paranjoy-guha-thakurtas-website-is-an-attack-on-press-freedom/` | HTTP 200 | 237,000 | **Analysis** — proportionality, ex parte vs final adjudication, Article 19 framing |
| `countercurrents.org/?s=Paranjoy` (search index) | HTTP 200 | 195,044 | **The only way the body was reachable** — the dated permalink 404s intermittently; this fetch returned the full 27,391-char article text |
| `timelinedaily.com/media/journalist-paranjoy-guha-thakurta-s-12-year-old-archive-vanishes...` | HTTP 200 | 50,663 | Timeline + the provider's non-response caveat |
| `theobserverpost.com/12-years-of-journalism-lost-as-paranjoy-guha-thakurtas-website-is-taken-down...` | HTTP 200 | 124,863 | Independent framing + press-freedom context |
| `madhyamamonline.com/india/host-pulls-down-veteran-journos-website-overnight-no-prior-notice-1567977` | HTTP 200 | 415,534 | Independent framing, "no prior notice" headline |
| `news.google.com/rss/search?q="Paranjoy Guha Thakurta"` | HTTP 200 | 108,600 | Dated corroboration — 5 outlets in the 2026-10-31 cluster + the second case |
| `news.google.com/rss/search?q="unsuspension is not negotiable"` | HTTP 200 | 4,410 | Confirms the quote is carried independently by 2 outlets |
| `news.google.com/rss/search?q="Eye Radio" Hostinger` | HTTP 200 | 8,703 | **Second case** — 4 items, 2 outlets, 2026-09-17 |
| `dreamhost.com/legal/acceptable-use-policy/` (**vendor primary**) | HTTP 200 | 230,063 | Verbatim "sole discretion … with or without prior notice" + "regardless of whether the IP addresses were listed as a direct result of your actions" — **artifact #2** |
| `racknerd.com/` (affiliate facts) | HTTP 200 | 34,042 | $2.24/mo entry, 20 datacenter locations, 24/7 support |
| `cloudflare-dns.com/dns-query` (DoH, `application/dns-json`) | HTTP 200 | 233–252 | **NXDOMAIN** for apex + 3 subdomains + NS + SOA; controls `example.com` / `vpstier.com` resolve NOERROR — **artifact #1** |

**Also tried and failed (recorded so the drafter does not guess):**

| URL | Result | Consequence |
|---|---|---|
| `hostinger.com/report-abuse` | **HTTP 403** (Cloudflare interstitial) | No policy claim made about the provider under review |
| `hostinger.com/legal/*` (8 path variants) | **HTTP 404** | Same |
| `support.hostinger.com/en/articles/*` | **HTTP 429** (rate-limited, 4 attempts) | Same |
| `hostinger.com/sitemap.xml` (288,714 B, 2,104 URLs) | HTTP 200 | Contains **no** terms/AUP/abuse-policy URL beyond `/report-abuse` |
| `lumendatabase.org` (+ `/notices/101001876`) | **HTTP 000** — does not resolve | The 52-URL figure is attributed to the outlets' reporting of the record, not to the record |
| `eyeradio.co.ke` (all paths, sitemap, WP REST API) | **HTTP 000** — does not resolve | Second-case bodies unreachable; **titles + dates + outlet names only** |
| `radiotamazuj.com` (all paths) | **HTTP 000** | Same |
| `reddit.com/r/VPS/comments/1xl6bn1` (+ `old.reddit`, `.json`) | **HTTP 403** | Item #3's freshness verified via the Brave index instead |
| `countercurrents.org` dated permalink | **HTTP 404** on 3 of 4 attempts | Recovered via the `?s=` search index — see the retry note below |
| `html.duckduckgo.com/html/?q=...` | **HTTP 202** challenge page | Unusable; Brave used instead |
| `search.brave.com` | **HTTP 429** after ~8 requests | Rate-limited; the last two queries were re-run with backoff and one succeeded |
| `racknerd.com/terms-of-service/`, `/affiliates/` | **HTTP 500** | Affiliate facts taken from the homepage + the site's own profile page |

**Retry note (a real lesson worth recording):** the Countercurrents article body was returned at HTTP 200 / 237,000 bytes on the *first* fetch, then the identical URL returned HTTP 404 / 1,443 bytes on three consecutive attempts. The full text had already been captured. **Always capture the body on the first successful fetch** — a later re-fetch is not a reliable confirmation, and a 404 on retry does not mean the URL was wrong. The `?s=Paranjoy` search index was the recovery path.

---

## 4. Fact bundle

24 rows, every one traced to a body-fetched source — the full table is in the outline's §1f. Headline figures, all live-fetched 2026-11-02:

- **Suspension:** 2026-10-28, entire account + all subdomains, **no notice to the owner, no court order cited**.
- **Support quote (6:48 a.m. call):** abuse report categorised **"Fraud/Scam"**; **"unsuspension is not negotiable in this case"**.
- **The scope mismatch:** the court order (ex parte ad interim injunction, 2026-10-24, Civil Suit No. 529/2026, Defendant No. 19) covered **one article**; the provider's action covered **the whole domain and every subdomain**. The **52-URL** search-engine takedown complaint (filed 2026-10-26) named major outlets and social platforms, and **most of those URLs are still online**, including the original 2019 article.
- **Owner's checks (2026-10-28, 07:48–07:56):** **none of 92 security vendors** flagged the domain (VirusTotal); Safe Browsing returned **"No unsafe content found"**.
- **Provider's response:** **none published** as of the reporting date; the outlets explicitly note the claims were drawn from the owner's statement and **have not been independently verified**.
- **Second case (same provider, 7 weeks earlier):** 2026-09-17, a Kenyan judge confirmed the website suspension was **unauthorised** and that the station was **not a party** to the underlying lawsuit; the station's lawyers gave the provider **24 hours** to restore the site.
- **Artifact #1 — live probe, 2026-11-02 ~02:00–02:20 UTC:** `getent hosts paranjoy.in` → **no A/AAAA record**; `curl` → **HTTP 000** with DNS lookup time **0.000s** (no resolution attempted) for the apex and all three subdomains; independent **Cloudflare DoH** → **Status 3 = NXDOMAIN** for the apex, `www.`, `media.`, `adanifiles.`, **and for both NS and SOA** (the zone has no delegation at all, not a misconfigured record). Controls `example.com` and `vpstier.com` resolved normally in the same probe. **Five days after the suspension, the domain is still dead.**
- **Artifact #2 — vendor primary:** a whitelisted provider's own AUP states it reserves the right "in its sole discretion, to disable, suspend, or terminate" a site "that cannot be immediately verified as being in compliance with applicable regulations, **with or without prior notice**", and may act where an assigned IP is on an abuse database "**regardless of whether the IP addresses were listed as a direct result of your actions**". Used to make the *process* point generalisable without asserting anything about the provider under review.
- **Affiliate facts (re-verified live 2026-11-02):** VPS **from $2.24/mo**; **20 datacenter locations**; 24/7 support; dedicated from $139/mo. On-site profile: $1.99/mo entry, root + KVM, $50–100/sale commission.

**Facts deliberately NOT asserted:** that the abuse report was false or malicious (owner + outlets say "alleged"); that the provider acted unlawfully (the article asserts sequence and scale, not motive); that the two cases share a mechanism (dated and adjacent, not causal); that the provider's policy forbids this (its policy pages were unfetchable); that the 92-vendor check proves legitimacy (it is the owner's check, with the outlets' caveat attached); that the adjacent shutdown titles have a known cause (bodies unreachable).

---

## 5. Content-gap verification

Pre-write grep over **all 61** published blog `.astro` files, **all 169** draft `.md` files and **all 69** `/vps/` profile pages (285 files total). 26 angle tokens:

```
account suspended          -> 0      abuse report            -> 0
suspended my               -> 0      abuse-report            -> 0
not negotiable             -> 0      unsuspension            -> 0
Fraud/Scam                 -> 0      fraud or scam           -> 0
legal notice               -> 0      ex parte                -> 0
Lumen Database             -> 0      Safe Browsing           -> 0
VirusTotal                 -> 0      domain suspended        -> 0
whole domain               -> 0      entire account          -> 0
entire hosting account     -> 0      all your sites          -> 0
hosting provider takedown  -> 0      collateral              -> 0
proportionality             -> 0      due process             -> 0
complaint mechanism        -> 0      third-party complaint   -> 0
false positive report      -> 0      unsolicited report      -> 0
account-level suspension   -> 0      suspended my account    -> 0
no notice                  -> 1      without notice          -> 1
abuse complaint            -> 1      blast radius            -> 9
one URL / single URL        -> 1      multiple domains        -> 0
same account               -> 0      multiple sites          -> 2
```

The four non-zero hits were checked and none covers account suspension: "no notice" → `lifetime-vps-deals-2026-real-cost-vs-marketing.astro` (promo-renewal caveat); "without notice" → `outline-2026-09-15-vpstier-daily.md`; "abuse complaint" → `outline-2026-09-15-vpstier-daily.md` (red flag #2's rationale); "blast radius" → 3 published articles, all in the **outage/credential** sense (`digitalocean-outage-august-2026.astro`, `aws-us-east-1-outage-2026.astro`, `dreamhost-breach-2026-password-reuse-vps.astro`), never the **account-multiplicity** sense.

**Adjacent-queue neighbours that are NOT collisions:**
- `vps-provider-exit-warning-signs-2026` (2026-08-27) — a host **vanishing**. Different failure: loud and visible, and it is a pre-purchase vet. Referenced by title in §3 only, not linked (no live file).
- `vps-provider-shutdown-warning-signs-2026` (2026-07-24) — 5 pre-purchase warning signs. Same distinction. Not linked.
- `cheap-vps-merchant-red-flags-2026` (2026-09-15) — pattern-at-risk across 3 flags at one vendor. The overlap is only the *method* (recognise a pattern); this piece's subject is a **single account-level suspension event** and the pre-purchase process question. Not linked (no live file).
- `dreamhost-breach-2026-password-reuse-vps` (published 2026-11-02) — the closest published neighbour. It is a **credential** story ("the leaked secret is only dangerous because of where it is also used"); this is an **account-membership** story (a complaint you did not file removes things you did not leak). Its H2-9 "Moving the Blast Radius Off a Shared Host" is credential-scoped, not account-scoped. Linked, not duplicated.

**Slug collision:** `hosting-account-suspension-blast-radius-2026` is absent from `published[]` (84 entries), `drafts[]` (57 entries) and `src/pages/blog/` (61 files).

---

## 6. Measurements

| Gate | Value | Limit | Result |
|---|---|---|---|
| Title | 54 | 30–60 | PASS |
| Description | 143 | 70–155 | PASS |
| H2 sections | 10 | 8–10 | PASS |
| FAQ | 5 | 3–5 | PASS |
| RackNerd CTA placements | 8 | ≥6 | PASS |
| Cross-links (all targets verified on disk) | 10 | — | PASS |
| Excluded-merchant token count in this document | 0 | = 0 | PASS |
| CJK character count in this document | 0 | = 0 | PASS |
| Deprecated-language-path in prose | 0 | = 0 | PASS |
| Fact rows with a source cell (§1f) | 24 | — | PASS |
| Briefing items adjudicated | 3 | — | PASS |
| Sources body-fetched at HTTP 200 | 12 | — | PASS |
| Real artifacts present (HCU req. #3) | 2 | ≥2 | PASS |
| Unverifiable items declared, not guessed | 5 | — | PASS |

**Title budget note:** vpstier's `BaseLayout.astro` renders `<title>{title}</title>` verbatim — **no auto-suffix** (re-verified 2026-11-02 at line 18 of `src/layouts/BaseLayout.astro`). Bare string length is the final length; measured with Python `len()` on the string as written into this outline.

**Cross-link verification:** all 10 targets confirmed present on disk this run. 7 queued-but-unpublished neighbours were deliberately excluded to avoid dead paths. (First verification pass used a malformed path pattern and reported 9 false MISSINGs — the paths are `src/pages/blog/<slug>.astro` for blog and `src/pages/vps/<id>.astro` for provider profiles; re-run correctly, all 10 exist.)

**Affiliate-label integrity:** all 8 RackNerd CTA placements identify RackNerd as the affiliate; none is attached to the provider under review. The provider under review appears only as the **subject of the reporting**.

**Language policy:** English-only. No deprecated language-prefix path appears in the outline or this record.

**Publish cadence:** vpstier publishes Mondays only since the 2026-08-28 HCU pause. **The 2026-11-02 Monday slot is already occupied** by `dreamhost-breach-2026-password-reuse-vps` → next available slot is **2026-11-09 (Monday)**.

---

## 7. Operational note — sibling cron failures (not this run's blocker)

`jobs.json` shows `c49b9d5fb6aa` (vpstier publish cron), `e5feb8292369`, `516d24492295` in `last_status: error` with `404 The model 'qwen/qwen3.6-27b' does not exist`. This is the retired-fallback-model class of failure (canonical pitfall #36), **not** a single-job fault: `/root/.hermes/config.yaml` now lists `kimi-for-coding` / `kimi-coding-api` and `qwen/qwen3.8-27b`, so the configuration is already amended and the recorded errors are residue of the earlier window.

**This matters for today's run specifically:** `c49b9d5fb6aa` has `next_run_at: 2026-11-02T10:45:00` — it is due to run today, and the last recorded attempt failed on the retired model. If the config amendment did not take effect for that job's provider chain, **the Monday publish slot will be missed again**. Flagging it here rather than attempting a fix from the outline cron, since that job owns its own retry.

**This run's cron (`5fd2a36f2dc4`) completed normally** (`last_status: ok`, `last_run_at: 2026-11-01T09:56:52`, `next_run_at: 2026-11-03T09:45`).

---

## 8. Commits (two-commit pattern)

- Commit 1: `git add drafts/outline-2026-11-02-vpstier-daily.md drafts/run-record-2026-11-02-vpstier-daily-outline.md` → `feat(drafts): ...`
- Commit 2: `git add drafts/state.json` → `chore(state): ...`

Never `git add -A` — the vpstier repo accumulates orphan files from prior runs and a blanket add would bundle them. Commit messages use `git commit -F <file>` (never `-m`) because the house message format carries `$` price figures and shell interpolation would corrupt them.
