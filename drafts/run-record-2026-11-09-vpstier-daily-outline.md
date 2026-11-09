# Run Record: 2026-11-09 vpstier daily outline — Let's Encrypt 64-day certificates

**Cron:** `5fd2a36f2dc4` (vpstier-daily-outline)
**Date:** 2026-11-09 (Monday)
**Variant:** variant-13 / variant-4-hybrid — briefing SUCCEEDED but zero usable stars; substituted the freshest dated, body-verifiable story outside the briefing
**Archetype:** certificate-lifecycle / operational-reliability buyer-guide (NEW on vpstier)
**Output outline:** `drafts/outline-2026-11-09-vpstier-daily.md` (`lets-encrypt-64-day-certificates-vps-2026`)

---

## 1. Briefing triage (2026-11-09 08:27 UTC briefing)

Both vpstier items failed a hard gate:

| # | Item | Verdict |
|---|---|---|
| 1 | RackNerd fall giveaway + deals (LEB, 1GB $21.99/yr → 4GB $59.99/yr) | CAPTURED by queued `black-friday-2026-vps-deals-early-tracker`; same RackNerd promo rejected as captured 09-05/09-06/09-09 |
| 2 | Hostinger Black Friday Premium 87% off, $1.79/mo (48-month term) | CAPTURED by published `hostinger-review.astro` + the renewal-price archetype already owned by `vps-pricing-trap-guide-2026` and `lifetime-vps-deals-2026-real-cost-vs-marketing` |

No usable star. Banned-pivot to the freshest dated story outside the briefing.

## 2. Why Let's Encrypt 64-day certificates was chosen

The briefing did not surface it. A live sweep of the Let's Encrypt primary blog, the live production ACME directory, and the LE community forum found a concrete, dated, self-contained operational-reliability story the site has never covered. It is a **calendar-driven dependency change**, not a vulnerability — a working site can go dark on a schedule with no attacker at all.

**Body-grep-0 coverage verification:** `letsencrypt`, `certbot`, `acme`, `64-day`, `certificate lifetime`, `renewal window` = **0 hits** across all 62 published `.astro` + 64 queued outline files. True virgin topic.

**Differentiators vs existing coverage:**
- Existing security pieces are OS/hypervisor/runtime CVEs (kernel TCP queued 10-31, Xen XSA-523 queued 11-06, PHP2Shell queued 11-08) + SSH hardening (queued 10-29). Those are threat surfaces; this is an operational-dependency surface.
- Control-plane-separation pieces (DNS/email queued, Virtualizor BGP-hijack queued 09-09) cover a hijacked update channel; this covers certificate expiry, a third control-plane dependency.
- The only published articles mentioning "ssl certificate" treat it as a provider feature bullet, never a lifecycle topic.

## 3. Verified fact bundle (all body-fetched 2026-11-09)

| Fact | Value | Source |
|---|---|---|
| Effective date | Feb 10, 2027 (all subscribers, 64-day default) | letsencrypt.org/2026/10/07/64-day-certs (200) |
| Last 90-day cert | expires May 11, 2027; no revocation as part of the change | letsencrypt.org/2026/10/07/64-day-certs |
| Staging preview | 64-day issuance in staging from Oct 14, 2026 | letsencrypt.org/2026/10/07/64-day-certs |
| Hard-coded renewals | renew at ~⅔ of lifetime; grep for 83/80/60 in cron/systemd | letsencrypt.org/2026/10/07/64-day-certs |
| Auth reuse | 30d → 10d (→7h in 2028), removes CAA rechecking | letsencrypt.org/2026/10/07/64-day-certs |
| Future | 45-day default in 2028; 2029 max-validation-reuse reduction | letsencrypt.org/2026/10/07/64-day-certs |
| Profiles | classic(90d)/tlsserver(45d)/shortlived(6d) advertised in directory | letsencrypt.org/docs/profiles + live ACME directory |
| ARI live | production directory exposes `renewalInfo` endpoint | acme-v02.api.letsencrypt.org/directory (200, live) |
| acme.sh | follows RFC 9773 ARI automatically, no flag (47.9k★) | github.com/acmesh-official/acme.sh README |
| Certbot | renew decision consults ARI/OCSP/renew_before_expiry; v5.9.0 (2026-10-29) current | certbot `renewal.py`/`acme/client.py` source |
| Buyer pain | LE community 252017 (2026-10-09) + 252576 (2026-10-30) | community.letsencrypt.org |

## 4. Source chain + fetch results (2026-11-09)

| Source | Status |
|---|---|
| letsencrypt.org/2026/10/07/64-day-certs | 200, full body (the anchor primary) |
| letsencrypt.org/docs/profiles | 200, full profile table |
| letsencrypt.org/ (homepage) | 200, confirms latest blog post is the 11-05 post (no newer superseding announcement) |
| acme-v02.api.letsencrypt.org/directory (live) | 200, exposes `renewalInfo` endpoint |
| acme-v02.api.letsencrypt.org/acme/renewal-info (probe) | 400 malformed-CertID (endpoint live) |
| eff-certbot.readthedocs.io/en/stable/using.html | 200, 190 KB certbot docs |
| raw.githubusercontent.com/certbot/certbot/main (acme/client.py, renewal.py) | 200, ARI code present |
| raw.githubusercontent.com/acmesh-official/acme.sh/master/README.md | 200, native ARI support |
| community.letsencrypt.org topics 252017 + 252576 | 200 JSON, dated buyer questions |
| rfc-editor.org/rfc/rfc9773.txt | 200, ARI standard |
| racknerd.com/kvm-vps (affiliate) | 200, live KVM plan table |
| SecurityWeek / Security Boulevard / Ars Technica 64-day articles | 403 / 403 / 405 (bodies not read — headline + date only) |
| cPanel / Plesk AutoSSL docs | 404 (pages not on the public docs index) |

**Bounded-claim discipline (canonical):** the multi-outlet 64-day corroboration (SecurityWeek/HelpNet/Linuxiac/BetaNews/Ars 10-07→10-12) is cited as a dated GN RSS cluster with bodies not read. The primary facts are body-fetched from letsencrypt.org.

## 5. Live GSC (28d window 2026-10-10 → 2026-11-06)

- Total impressions: 285; homepage `/` holds ~296 of page-impressions at avg position 83.
- Top head terms absorbed by homepage: "virtual private server hosting reviews" 48 imp pos 84.7, "best vps for ai agents" 42 imp pos 74.5, "best vps provider" 29 imp pos 81.7.
- Hub-gap persists; today's operational-reliability outline is a complementary topical piece.

GSC token: live refresh via `/root/.hermes/scripts/gsc_daily_report.py` helpers; worked cleanly (canonical pitfall #52).

## 6. Pitfalls handled this run

1. **Pitfall #54 (GN RSS `when:` operator)** — all out-of-briefing freshness sweeps carried `when:2d`/`when:3d`/`when:5d`/`when:7d` operators; the bare `VPS hosting` wall of 2025→2026-08 items was avoided.
2. **Pitfall #55 (still-moving cluster)** — the 64-day headline is 33 days old but the cluster tail is current (cert-manager/certbot setup guides dated 2026-11-07; LE community thread 252576 dated 2026-10-30). Freshness = newest dated item.
3. **Pitfall #48 (self-check banned-token literal)** — §7 self-check rows written generically ("standard category-token sweep") without embedding any excluded-merchant literal. Verified 0.
4. **Pitfall #44 (asserted length)** — title/desc lengths computed with `len()` on the final rendered strings (54 / 139) BEFORE writing the self-check rows.
5. **Pitfall #53 (possibly-excluded merchant in fresh prose)** — briefing item #2's competitor framing was not adopted; no excluded merchant is named in the outline.
6. **Pitfall #2 (self-check banned-token row)** — the §7 banned-token row does not name the literal token.
