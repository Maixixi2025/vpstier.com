# Run Record: 2026-11-08 vpstier daily outline — PHP2Shell / CVE-2026-109618

**Cron:** `5fd2a36f2dc4` (vpstier-daily-outline)
**Date:** 2026-11-08 (Sunday)
**Variant:** variant-13 / variant-4-hybrid — briefing SUCCEEDED but zero usable stars; substituted the freshest dated, body-verifiable story outside the briefing
**Archetype:** language-runtime end-of-life + actively-exploited-RCE buyer-guide (NEW on vpstier)
**Output outline:** `drafts/outline-2026-11-08-vpstier-daily.md` (`php2shell-cve-2026-109618-php-rce-vps`)

---

## 1. Briefing triage (2026-11-08 08:14 UTC briefing)

All three vpstier items failed a hard gate:

| # | Item | Verdict |
|---|---|---|
| 1 | DreamHost breach follow-up | CAPTURED by published `dreamhost-breach-2026-password-reuse-vps.astro` (live 11-02) |
| 2 | Black Friday hosting deals | CAPTURED by queued `black-friday-2026-vps-deals-early-tracker` + banned-merchant figure + walled cybernews.com (403) |
| 3 | Kainode Singapore 4GB $5.99 | CAPTURED by published review (variant-8) + published APAC roundup |

No usable star. Banned-pivot to the freshest dated story outside the briefing.

## 2. Why PHP2Shell (CVE-2026-109618) was chosen

The briefing did not surface it. A live Google News RSS sweep found a sustained, still-moving multi-outlet story the site has never covered, at the application-runtime layer (distinct from every OS / hypervisor / control-panel / SSH piece already queued or published). The story is 17 days old at run date and still producing fresh coverage daily.

**Differentiators vs existing coverage:**
- Existing security pieces are OS/hypervisor CVEs (kernel TCP queued 10-31, Xen XSA-523 queued 11-06, kernel escape queued 08-09). This is the language-runtime layer — the buyer patches PHP, not the kernel, and there is an EOL cliff no OS piece has.
- Control-panel supply-chain (queued 09-09) is a hijacked update channel. This is the runtime's own patch lifecycle + EOL.
- SSH hardening (queued 10-29) is the login surface. This is the application surface.

## 3. Verified fact bundle (all body-fetched 2026-11-08)

| Fact | Value | Source |
|---|---|---|
| CVE IDs | CVE-2026-109618 + CVE-2026-109619 | cveawg.mitre.org CVE JSON |
| Root cause | OOM `longjmp()` → uninitialized request memory read/branch; + global state → freed request memory across requests | cveawg.mitre.org |
| CVSS 4.0 (both) | `AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H` | github.com/php/php-src advisories |
| Affected | 8.2.*<8.2.35, 8.3.*<8.3.36, 8.4.*<8.4.27, 8.5.*<8.5.12 | cveawg.mitre.org |
| Fixed / final patch | 8.2.35 released 22 Oct 2026 is final on 8.2 | php.net ChangeLog-8.php |
| 8.2 EOL | security support until 31 Dec 2026 (in 1 month) | php.net/supported-versions.php |
| 8.4 status | active support ends 31 Dec 2026; security-only to 31 Dec 2028 | php.net/supported-versions.php |
| Exploitation | China-nexus chained PHP2Shell + VMware ESX 0-day + Fragnesia → rooted 25 servers, breached US gov-affiliated network | GN RSS: THN/SecurityWeek/TechRadar/Cybernews 10-28→10-30 (bodies not read) |
| Gov impact | Japan gov/bank/ministry sites offline to patch | The Japan Times 10-22 (GN RSS, body not read) |
| Post-mortem | bug known ~2 years, kept quiet by small maintainer team | Tom's Hardware 11-04 (GN RSS, body not read) |

## 4. Source chain + fetch results (2026-11-08)

| Source | Status |
|---|---|
| cveawg.mitre.org CVE JSON (both CVEs) | 200, full JSON body |
| php.net/supported-versions.php | 200, EOL table body-fetched |
| php.net ChangeLog-8.php | 200, "Version 8.2.35 22 Oct 2026 … Fixed GHSA-w8hw-w9fx-j79w, GHSA-6wmf-4rv5-p3rp" |
| github.com/php/php-src advisories (both GHSAs) | 200, CVSS vector + CWEs body-fetched |
| php.net releases index | 200, 693 KB |
| racknerd.com/kvm-vps | 200, live KVM plan table |
| Google News RSS (PHP2Shell exploitation / Kaspersky / PHP clusters) | 200, outlet+date corroboration |
| Tom's Hardware PHP post-mortem permalink | 404 (body NOT read — used headline+date only) |
| cyfirma / notebookcheck PHP2Shell articles | 404 (bodies NOT read) |
| CISA KEV catalog | 403 (not used) |
| cybernews.com | not retried (canonical pitfall #24, bot-blocked) |

**Bounded-claim discipline (canonical):** the exploitation + government-impact + post-mortem rows are cited as dated multi-outlet Google News RSS clusters with bodies not read. The article says exactly that and makes no claim about body content.

## 5. Live GSC (28d window 2026-10-11 → 2026-11-07)

- Total impressions: 349; homepage `/` holds **292 (84%) at avg position 83**.
- Individual articles rank well but get almost no impressions (e.g. lightnode pos 1.0, hosthatch pos 5.0).
- Head terms absorbed by homepage: "best vps provider" 29 imp pos 82, "best vps providers" 21 imp pos 83, "virtual private server hosting reviews" 48 imp pos 85.
- This is the hub-gap pattern the 2026-11-03 `best-vps-providers-2026` outline targets; today's security outline is a separate, complementary topical piece.

GSC token: live refresh via `/root/.hermes/scripts/gsc_daily_report.py` helpers; worked cleanly (canonical pitfall #45 workaround not needed this run).

## 6. Pitfalls handled this run

1. **Pitfall #46 (CJK in briefing item title)** — briefing item #3 carried no CJK, but the item-#1 outlet's own framing was paraphrased; the whole draft was grep-verified CJK = 0.
2. **Pitfall #48 (self-check banned-token literal)** — the §7 self-check rows were written generically ("standard category-token sweep") without embedding any excluded-merchant literal. Verified: `hetzner|contabo` count = 0 in the final outline.
3. **Excluded-merchant discipline in the triage table** — briefing item #2's lead figure names a permanently excluded budget merchant; the outline references it only as "a permanently excluded budget merchant" and never re-prints the brand.
4. **Pitfall #44 (asserted length)** — title/desc lengths were computed with `len()` on the final rendered strings (45 / 142) BEFORE writing the self-check rows, not estimated.
5. **Pitfall #42 (vendor-naming verbatim)** — the patch/EOL/CVSS facts are quoted from body-fetched cveawg + php.net; every vendor-naming fact traces to a fetched source.
6. **Bounded claims for unwalled primaries** — Tom's Hardware / cyfirma / Notebookcheck permalinks 404'd; their headlines + dates were used only as RSS-cluster corroboration, never as read-body facts.
7. **Cross-link targets verified on disk** — 8 of 8 exist; queued-but-unpublished slugs (`vps-ssh-security-host-key-checks-2026`, `linux-kernel-tcp-rce-cve-2026-98432-vps`) were deliberately excluded (no live URL).

## 7. Queue / pipeline notes

- `drafts_count` moves 63 → 64; `published[]` untouched (84).
- 62 queued outlines, 84 published articles. Last published article: 2026-11-02 (MassiveGrid). The Monday publish cron (`c49b9d5fb6aa`) runs Mondays; the queue is deep.
- RackNerd live KVM entry (racknerd.com/kvm-vps, fetched 2026-11-08): 512 MB / 1 vCore / 30 GB / 500 GB @ 1 Gbps = **$26.99/yr** (the recurring low-price entry); monthly plans $17.99 → $55.99. This is the honest affiliate anchor (full root + KVM = you own the runtime, which is exactly this article's advice).

## 8. Recommended next step

User reviews the outline; on `publish` the article cron writes the full `.astro` article. Recommended publish slot 2026-11-16 (Monday) — the 11-09 Monday slot is crowded, and this dated security piece holds value through the Dec 31 8.2 EOL cliff.
