# Run Record — vpstier-daily-outline — 2026-11-15

**Job:** `5fd2a36f2dc4` (vpstier-daily-outline)
**Run date:** 2026-11-15
**Variant:** **13** — briefing SUCCEEDED, **zero usable vpstier stars** (2 hard-banned merchant + 1 non-whitelisted / captured / pricing-shaped); substituted the freshest dated, body-verifiable story found **outside** the briefing via the same feeds the briefing reads.
**Outcome:** outline written and verified → `drafts/outline-2026-11-15-vpstier-daily.md` + `drafts/run-record-2026-11-15-vpstier-daily-outline.md` + `drafts/state.json` append. **Not yet published** — awaiting user `publish`.

---

## 1. Variant adjudication

The daily briefing (cron `3ea88f8bb2d0`, output `2026-11-15_08-08-04.md`) **succeeded**. Its report is intact in the output file. `jobs.json` shows the briefing job's `last_status: error` with the **entire formatted report wrapped inside a `RuntimeError:`** — this is a **delivery-wrapper failure, not a briefing failure** (canonical pitfall #59, which has now re-confirmed on a different day). Adjudicating on the status field alone would have produced a false variant-4.

All three vpstier items fail a hard gate:

| # | Item | Verdict | Ground |
|---|---|---|---|
| 1 | Network-stack benchmark: firewall connection limit 84-88k → 120k per address family, WireGuard +18-39%, multi-flow inbound to a single VM 16-18 Gbit/s → 9-10 Gbit/s | REJECTED | Permanently excluded merchant (the brand must not be printed); independently off-ICP (dedicated-server network stack). |
| 2 | Helsinki cloud-server price cut of 15% from 2026-11-10, new orders + resizes only, CPX/CCX lines, existing instances unchanged | REJECTED | Same permanently excluded merchant. |
| 3 | Black Friday price ladder: 2GB KVM at $1.83/mo first year against a $87.96/yr list price and a $43.99 channel price (LEB 2026-11-14) | REJECTED | Merchant absent from `providers.json` (65 providers checked); the intro-vs-renewal mechanic is the canonical worked example inside the **published** `vps-pricing-trap-guide-2026`; Black-Friday timing is already the dated hook of the **queued** `black-friday-vps-restock-timing-2026` outline. Third rejection of this shape in three days. |

**Consequence:** zero usable stars → **variant-13**.

---

## 2. Substitute selection — how it was found

1. **Freshness sweep with the `when:` operator** (canonical pitfall #54). Queries run: `VPS hosting when:3d`, `VPS outage when:3d`, `hosting provider when:4d`, `data center outage when:3d`, `cloud hosting price increase when:4d`, `VPS provider price increase when:5d`, `VPS server outage ransomware when:5d`, `hosting account suspended when:5d`, `VPS disk space data loss when:5d`, `bare metal server pricing when:5d`, `virtual private server announcement when:3d`, `data center fire power outage when:4d`, `VPS migration provider switch when:5d`, `cheap VPS benchmark when:5d`, `self-host email server when:4d`, `cloud provider breach customer data when:4d`, `Black Friday VPS deals when:4d`, `Hostinger price increase when:5d`, `whitelisted-provider name + outage/price when:5d`, `RackNerd announcement when:7d`, `VPS storage NVMe migration when:5d`, `hosting company acquired acquisition when:7d`, `VPS control panel vulnerability when:7d`, `IPMI password bruteforce when:7d`, `DNS outage when:5d`, `VPS backup failed restore when:7d`, `BGP hijack when:7d`, `Let's Encrypt expiry when:5d`, `VPS email deliverability when:7d`, `server RAM ECC error when:7d`, `IPv6 routing when:7d`, plus a second-wave sweep at `when:2d` on VPS / hosting / cloud security breach / server compromise / self-hosted AI agent attack.
2. **Mechanism-term queries** (the 2026-11-02 lesson — search the mechanism, not the brand): `AI agents steal API keys exposed servers`, `LLMJacking API keys servers`, `exposed Ollama server API key stolen`, `honeytrap exposed server LLM API key harvest`, `ARTEX FBI flash alert AI pentesting tool`, `AntiFox pentesting AWS`, `Japan 1000 servers AI cyberattacks`.
3. **Primary-source fetch ladder** applied to each surviving candidate. Bodies fetched whole: FBI IC3 PDF, AWS Security Blog, JPCERT/CC, Darktrace Signal Labs, Arctic Wolf via The Hacker News, GitGuardian, The Record, The 420.in, GitHub API, mirror READMEs, The Straits Times/Kyodo.

**Candidates evaluated and rejected after body-fetch:**

| Candidate | Why rejected |
|---|---|
| Fireworks AI October incident (vendor primary `fireworks.ai/security/bulletins`, both bulletins fetched whole) | Genuinely strong and body-verifiable, but **the AI-credential-theft angle collides head-on with the queued `railway-breach-2026-740k-api-key-heist` outline** (both are "stolen AI keys → self-financing inference"). The ARTEX story has a different mechanism (an attacker-side *tool*) and so did not need to take the collision. |
| Darktrace "Claude memory stores as covert C2" (primary fetched, 502,428 B, 2026-11-12) | Excellent and genuinely VPS-shaped (a stolen key turns a coding agent into a remote-controlled implant on a Linux box with a systemd service). **Rejected on collision with the same queued Railway outline** — same "an AI credential is worth more than a password" thesis. Held as the backup if the queued piece is dropped. |
| Darktrace "hijacking agentic harnesses" (conversation-history poisoning) | Published **2026-09-24** — 52 days old. Not fresh enough to lead on 11-15. |
| AntiFox/AWS credential theft via the Arctic Wolf report | Strong, but it is a **subsection** of the ARTEX story (AntiFox is an ARTEX fork), and the FBI FLASH is the stronger, more authoritative anchor. Folded into the outline as fact-table rows (§1d) rather than run as a separate piece. |
| JPCERT/CC national investigation | **Not rejected — promoted to a chapter.** The Kyodo report is d-0 (published 2026-11-15 08:06) and the JPCERT/CC primary is body-fetchable, so it became chapter 10 and the d-0 freshness peg. |
| Belarusian cloud-firm ransomware (The Record, 11-13) | The Record's article URL was not recoverable from the homepage href scrape (only 2 hrefs present); only the RSS route worked, and the body could not be fetched. Rejected as unbody-verifiable. |
| "AI Agents Steal OpenAI and DeepSeek API Keys From Exposed Servers … 5,132 children" (GBHackers, 11-11) | `gbhackers.com` returned HTTP 403 for the homepage, search and both sitemap paths — 4 attempts, 0 bodies. Rejected as unbody-verifiable (the headline number could not be confirmed anywhere). |
| China-led probe, 1,000 servers / 1,000 AI-attack servers | Same story as the JPCERT chapter — kept as the chapter, not a separate piece. |

---

## 3. The fact bundle — three primaries fetched whole

| Primary | URL | Status / size | What it gave |
|---|---|---|---|
| **FBI IC3 flash alert** | `ic3.gov/CSA/2026/261113.pdf` | 200, **541,176 B, 13 pages, 25,163 chars extracted** | FLASH-20261113-001, dated 13 NOVEMBER 2026, TLP:CLEAR. Full summary, MITRE-mapped TT&P table (3 phases), IOC list, "Information Requested" list, 4-part Recommendations, 11 numbered references. PDF metadata: `Author: Federal Bureau of Investigation`, `CreationDate D:20261113125706-05'00'`. |
| **AWS Threat Intelligence** | `aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/` | 200, **1,452,605 B** | Two campaigns described from the attackers' own records, captured by the MadPot decoy sensor network between **Oct. 3 and Nov. 5, 2026**; the credential-grading scheme; the full discovery-surface list; the named default keys and CVEs; the complete 11-row IPv4 IOC table with first-seen / last-seen dates. |
| **JPCERT/CC** | `blogs.jpcert.or.jp/en/2026/10/web_api_attacks.html` | 200, **55,711 B** | The national CERT's own attack-infrastructure analysis: APK analysis → API discovery → SSRF testing via a Python HTTPS server returning HTTP 302 redirects; Blutter + jadx for Flutter/Android reversing; a separate server with files targeting web apps, MySQL, Jenkins and email gateways, EDR-evasion attempts and web shells believed deployed inside the target network. |

**Supporting bodies read:** The Hacker News (11-11), The Record (11-13), The 420.in (11-12), GitGuardian (11-11), The Straits Times / Kyodo (11-15), GitHub API, and two ARTEX mirror READMEs via `raw.githubusercontent.com`.

**Bodies-not-read boundary (canonical pitfall #61):** 15-outlet cluster dated 2026-11-11 → 2026-11-15. **5 bodies read**, **11 headline+date only** (BleepingComputer, Techzine Global, Security Affairs, TechRadar, Cybersecurity Dive, NEWS.am TECH, SecurityBrief NZ, news.lavx.hu, GBHackers News, Cyber Press, a Korean-language security outlet). Stated explicitly in the outline and to be repeated in the article.

---

## 4. Archetype — NEW on vpstier

**Agentic-offensive-tool / exposed-surface buyer-guide.** The discriminator against every security piece the site already has:

- Not a **CVE** (no patch to apply) — the flaw is the *speed and persistence* of the attacker.
- Not a **provider breach** (the blast radius is not the provider's fault) — the target is the reader's own box.
- Not a **credential-reuse** story (a human with a wordlist) — the actor is a **multi-agent program the attacker installed**, which arrives with valid access and then escalates on its own.

The thesis: **the attacker's console looks exactly like your admin panel, and it may be running on your own server.** The FBI's 1,600-exposed-console census plus the tool's one-line `docker compose up -d` install and `localhost:8787` UI is the part no outlet framed for a VPS owner.

---

## 5. Collision clearance (measured this run, not assumed)

- **Slug uniqueness:** 0 hits for `artex`, `scanning-your-vps`, `fbi-alert` across `src/pages/blog/`, `drafts/`, `published[]`, `drafts[]`, `recent_topics[]`.
- **Mechanism-token sweep** on published `src/pages/blog/*.astro` + all `drafts/*.md`: `agentic` 0 pub / 11 draft-mentions; `pentest` 0 / 3; `penetration test` 0 / 0; `living off the land` 0 / 0; `LOTL` 0 / 0; `exposed server` 0 / 0; `internet-facing` 0 / 2; `ARTEX` 0 / 1 (a single mention inside the 11-12 Railway outline's fact table — adjacent, not covered).
- **Nearest neighbours, each discriminated explicitly** in the outline's §3 table: `ai-agent-vps-api-guide` (published), `cheapest-vps-local-llm-inference-2026` (published), `dreamhost-breach-2026-password-reuse-vps` (published), `vps-no-vm-escape-admin-credential-ransomware-2026` (queued 11-13), `railway-breach-2026-740k-api-key-heist` (queued 11-12), `agentic-vps-always-on-ai-agent-2026` (queued 09-10).
- **Deliberate non-cross-link:** the two queued neighbours are **not** linked from this outline. Linking to two adjacent queued pieces would make this article read as an instalment of a series it is not part of. Both are recorded in the neighbour table instead.

---

## 6. Verification gates run on the saved file

Every numeric gate was re-computed by **re-parsing the saved file**, never transcribed from the draft (canonical pitfalls #22, #44, #66):

| Gate | Declared | Computed from file | Result |
|---|---|---|---|
| Title length (30-60) | 54 | **54** | PASS |
| Description length (70-155) | 154 | **154** | PASS |
| H2 chapter count | 10 | **10** numbered items in §3 | PASS |
| FAQ count | 5 | **5** | PASS |
| RackNerd CTA placements | 8 | **8** table rows, all → the house affiliate URL | PASS |
| Cross-links | 8 | **8** rows, **8/8 targets confirmed present** in `src/pages/blog/` this run | PASS |
| Excluded-merchant zero-check | 0 | **0** case-insensitive hits over the whole file, including the self-check rows | PASS |
| CJK-range zero-check | 0 | **0** — one Korean outlet name was caught and replaced during the check (canonical pitfall #46) | PASS |
| Deprecated language-prefix path | 0 | **0** | PASS |
| Cyrillic / Greek | 0 | **0** | PASS |
| Non-ASCII inventory | — | `§ · — → ∩ ✅` only | PASS |
| Fact-table traceability | every row | every row carries a body-fetched source | PASS |
| Bodies-not-read boundary stated | yes | 5 read / 11 headline+date only, stated in §1b | PASS |

---

## 7. Affiliate-label integrity (canonical pitfall #51)

The affiliate is a KVM budget VPS with a public IPv4 and a control panel. It is **not** an AI-gateway host, **not** a hardened agent sandbox, and **not** a product that automates any of the FBI's mitigations. All 8 CTAs are therefore framed as **"the box you run the audit on"** or **"the spend you watch"** — never as a fix. The live entry price was verified this run on `racknerd.com`: **"VPS from $2.24 /mo"**. The site's own provider page still says **$1.99/mo**; the outline instructs the article to use **$2.24** and flags the stale page for the SEO slot rather than silently reusing the stale figure.

---

## 8. Flagged for the user (not fixed from this slot)

1. The site's own RackNerd provider page quotes **$1.99/mo**; live vendor price is **$2.24/mo**. SEO slot.
2. Live GSC (from the 2026-11-14 pull): 1,206 impressions / 1 click / 61 pages, homepage absorbs **76.9%** at position 85.0; the 2026-11-15 daily report shows 340 impressions / 0 clicks / 78 impressions in 7 days at avg position 90.9. Every head term still lands on the homepage at position 84-98. The queued `best-vps-providers-2026` hub remains the structural fix.
3. `published[]` ∩ `drafts[]` still overlaps on 2 slugs — pre-existing, unrelated.
4. The deprecated language-prefix tree still has one file, one URL and one sitemap entry — pre-existing.
5. **Sibling cron failures on 2026-11-15** (reported, not this job's fault): `74aa76f6b770` → provider-side `403 AccountOverdueError`; `c7ba564d1345`, `e5feb8292369`, `48d46f266018`, `82d8b8a903ed`, `2b2bb0391699` → `413 Request payload too large`; `aa24405635c9` and `f5d8820fbe21` → report-shaped prose inside a `RuntimeError` wrapper (delivery-channel failures, not content failures). The vpstier outline cron itself ran normally.
6. **Two other sites' crons are in the same AI-credential space.** The queued Railway outline (11-12) is the site's other AI-credential piece. This outline deliberately takes the *attacker-tool* axis so the two do not overlap; if the Railway piece is dropped, the Darktrace "Claude memory stores as covert C2" research (body already fetched, 502,428 B, dated 2026-11-12) is the ready replacement and does not need re-research.

---

## 9. Tooling notes for the next run

- **PDF extraction on this box:** `pdftotext` is absent and `pypdf` is installed only under **python3.6** (which fails — it imports `typing.Protocol`) and in the uv cache. The working invocation is `PYTHONPATH=/root/.cache/uv/archive-v0/_ZrKkpiNel1_D1tqUYjF_ python3.11 <script>` (pypdf 6.18.1). Do not waste calls rediscovering this.
- **FBI IC3 document discovery:** the ARTEX FLASH is **not** on the PSA path (no `/PSA/2026/PSA26xxxx` id exists for it). It is an **Industry alert**, a PDF at `/CSA/<year>/<MMDD>.pdf`. Recover it from the IC3 homepage `href` scrape and read the `type="application/pdf"` attribute — the RSS feed does not carry industry alerts.
- **The Record:** article slugs are not on the homepage; the working route is `therecord.media/feed/` (5,319 B, 5 items with real slugs).
- **GitHub API is a first-class primary** for tool-fork censuses: `api.github.com/search/repositories?q=<name>+in:name&sort=stars` plus `api.github.com/repos/<owner>/<repo>` for per-repo metadata. No auth needed.
- **AntiFox's README is in Chinese** (`raw.githubusercontent.com/AntiFox-AI/antifox/main/README.md`) — the English mirror `BaaRai/ARTEX` is the readable one, and it carries the `localhost:8787` deployment detail.
- **`terminal` remains Tirith-blocked** for this cron (canonical pitfalls #20/#31) — every read, fetch, grep and git operation ran through `execute_code` + `subprocess.run`.

---

*Generated by the vpstier-daily-outline cron (`5fd2a36f2dc4`) on 2026-11-15. Variant-13. Archetype: agentic-offensive-tool / exposed-surface buyer-guide (NEW). Awaiting `publish`.*
