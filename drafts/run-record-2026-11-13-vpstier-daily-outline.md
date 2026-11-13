# VPSTier Daily Outline — Run Record 2026-11-13

**Cron:** `5fd2a36f2dc4` (vpstier-daily-outline) · **Variant:** variant-13 (briefing SUCCEEDED, zero usable vpstier stars) · **Archetype:** administration-plane misconfiguration / credential-path takeover buyer-guide (NEW on vpstier)
**Outline:** `drafts/outline-2026-11-13-vpstier-daily.md` · Title 46/60 · Desc 153/155 · 10 H2 / 5 FAQ / 8 RackNerd CTA / 9 cross-links

---

## 1. Briefing triage — all 3 vpstier items rejected

| # | Item | Verdict | Reason |
|---|---|---|---|
| 1 | Platform-as-a-service October breach → ~$740,000 fraudulent AI-provider charges (TechRadar 2026-11-11); briefing suggests an "API key defence checklist for VPS/managed platforms" | REJECTED — captured by yesterday's queued outline | The same story is the dated hook of the queued `railway-breach-2026-740k-api-key-heist` (2026-11-12). The briefing's proposed angle is that outline's existing spine (§8 = the 60-minute secret-blast-radius audit). A **re-surface of a story queued yesterday**, not a fresh pick. |
| 2 | 15% cloud-server price cut in one European capital region, effective 11-10, new orders + resizes only | REJECTED — permanently excluded brand + off-shape | The subject is a **permanently excluded merchant** → name must not appear anywhere (pitfall #53). Independently off-shape: regional price cut, no failure mechanism; the site's pricing-model coverage already exists in two published articles. |
| 3 | Budget host's October offer back at $1.83/mo for 2GB KVM, with BF restock data (17 sold out in 48h, 11 back at same price, median 19 days) — LEB 2026-11-11 | REJECTED — captured + non-whitelisted | The restock figures are **verbatim the fact bundle of the queued `black-friday-vps-restock-timing-2026`** (2026-11-11). Merchant also absent from `providers.json` (65 checked) and has no dated incident. |

The briefing's site-wide "focus topics" list (generative-AI search model swap, Search Console reporting defect, Cloudflare open-source browser engine) carries three further entries, all off-site for vpstier.

**→ variant-13.** Substitute sourced from the same feeds the briefing reads via a `when:` date-window sweep (pitfall #54) and body-fetched from the research house's own report.

## 2. The substitute and why it was chosen

**Primary:** `securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/` — HTTP 200, **206,108 B**, `datePublished` **2026-11-06T10:00:12+00:00**, author Rauf Johari, 27,120 chars of body text extracted and parsed.

**Why it is the right vpstier story (not just a security story):**

- The primary's own closing judgement: *"GERT cases that we presented in this article did not require an attacker to break the VM boundary."* And from the introduction: *"A monitoring system that could reach the virtualization layer also exposed a reusable root credential. Once the attacker controlled that route, ordinary administrative access was enough to affect several hosts. No VM escape was required."*
- **The site has no article on this mechanism class.** Body-grep across `src/pages/blog/` + `src/pages/vps/`: `execInstalledOnly` 0 · `lockdown mode` 0 · `vncwebsocket` 0 · `prtg` 0 · `esxi` 0 · `monitoring identity` 0 · `vault retrieval` 0 · `copy fail` 0 · `cve-2026-31431` 0 · `ghsa-7fw3` 0 · `vcenter` 0 · `secure boot` 0 · `uptime kuma` 0 · `netdata` 0. `proxmox` 3 (unrelated provider review + index) · `hypervisor` 6 (provider-review boilerplate).
- **It inverts the site's whole security coverage**, which is code-shaped (kernel escape, hypervisor memory flaw, language-runtime RCE, SSH hardening). This is the counter-shape: the failure is in the **identity and network design**, and the buyer fixes it themselves tonight.
- **The buyer-side translation is exact.** On a $21.99/year box, "a monitoring server becomes privileged infrastructure when it holds credentials that can administer the systems it observes" is not an enterprise topology — it is one uptime script and one password.

**Three findings only the primary carries (no outlet reproduced them):**

1. The monitoring platform "had broad access to the ESXi hosts" and **the same root password was reused across several nodes**; the primary's verdict: *"This design joined monitoring, credential storage, and direct administration into one attack path."*
2. **The control that blocked the attacker was one he could switch off.** First execution refused with *"Execution of non-installed file prevented"* (the `execInstalledOnly` policy working), then the attacker — already root — disabled it with `esxcli system settings advanced set -o /User/execInstalledOnly -i 0` and ran the payload. Primary's judgement: *"A setting that can be silently disabled by the same credential used for daily administration provides limited resistance after account compromise."*
3. **Case #2 needed no monitoring at all** — administrative credentials and access details **stored in notes in plain text** on a compromised admin workstation → Proxmox login as root → VNC web socket → ransomware inside the cluster → *"the encryption of the entire virtual environment"*. The access-log artifact: five `root@pam` VNC-web-socket requests inside a 16-minute window on 01/08/2026.

## 3. Fetchability map (this niche, 2026-11-13)

- `securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/` ✅ 206,108 B — **the single most valuable source**
- `securelist.com/feed/` ✅ 531,915 B — **the recovery path**: the direct slug 404'd and the `?s=` search returned the wrong posts, but the Atom feed carried the real URL + date. Canonical feed-first recipe.
- `securelist.com/how-a-cloud-pentest-works/121921/` ✅ — adjacent post, same author series (2026-11-12), not used
- `racknerd.com` ✅ 34,042 B (entry price, 20 datacenter locations) · `racknerd.com/specials` ✅ 87,952 B (full specials ladder, specs, root-access FAQ)
- `thehackernews.com/2026/11/*` ✅ 167-175 KB — but the **Nov index page returns 1 unique link** (`?m=1`); the slugs must come from the **homepage** `href` scrape, not the month index. Confirmed working: `new-n-central-exploits-work-against.html`, `sckit-malware-targets-screenconnect.html`, `4837-hijacked-github-accounts-ran-ci.html`
- `lowendbox.com/feed/` ✅ 387,633 B (20 posts, dates intact) — `lowendbox.com/blog/` 404s and `/category/vps/` 404s; **the feed is the working entry point** (re-confirms pitfall #33: LEB blog bodies are NOT walled)
- `tbreak.io` ❌ DNS does not resolve · `itnews.com.au/<slug>` ❌ 404 on the guessed slug · `bleepingcomputer.com` ❌ (no body fetched) · `google.com` / `html.duckduckgo.com` ❌ both blocked → **Google News RSS remains the corroboration substitute** (pitfall #54)
- GN RSS `when:Xd` date operator confirmed working on 8 distinct queries this run.

## 4. Pitfalls exercised / re-tripped this run

1. **Pitfall #35 / #59 checked, did not fire.** `jobs.json` showed the briefing at `last_status: ok` with **no** `last_error`, and the output file held a clean report — so this is a genuine briefing SUCCESS, and the variant adjudication is 13 (zero usable stars), not 4 (briefing failure). The check was made *before* adjudicating, not after.
2. **Pitfall #54 applied — `when:Xd` sweeps, not bare queries.** A bare `hosting price increase` query returned a wall of Thanksgiving-dinner and Maryland-health-plan articles. Eight date-windowed queries (`when:2d`/`3d`/`4d`/`7d`/`10d`) surfaced the candidate set. Bare sweeps are not just noisy — they are unusable for a freshness gate.
3. **Pitfall #61 applied — labelled corroboration boundary.** The interpretation cluster is **2 outlets, headline + date only (2026-11-11), bodies not read**. The outline states this in §1b and again in §9 and the self-check. No sentence implies a broad review.
4. **NEW — a research house's Atom feed is the recovery path when its URL slugs are unstable.** The Securelist slug guessed from the briefing title 404'd, and `?s=<query>` returned unrelated posts (the site's search is weak). `securelist.com/feed/` returned the real URL, its `pubDate`, and 12 recent posts. **Rule: for a vendor/research site with a dated post index, fetch the feed FIRST and derive the slug from it, rather than guessing the slug from a headline** — guessing worked in prior runs for other outlets and silently breaks here.
5. **NEW — an outlet's month-index page can be a stub; the homepage carries the real links.** `thehackernews.com/2026/11/` returned 146 KB but only **one** unique article URL (`?m=1`). The homepage `href` scrape yielded 16 distinct `/2026/11/*.html` slugs, and those fetched clean at 167-175 KB. **Rule: when a month index yields < 5 unique article links, scrape the homepage instead.**
6. **Pitfall #22 / #44 applied — gate over a candidate list, then re-verify against the saved file.** 7 title candidates and 6 description candidates were gated in one pass before anything was written (3 descriptions failed at 160-168 chars). The declared 46/60 and 153/155 were then re-computed by **re-parsing the saved file**, not by trusting the earlier computation.
7. **Pitfall #53 applied — the triage row names the excluded merchant by category only.** Item #2's row reads "a permanently excluded merchant" and never prints the brand. Item #1's row names no merchant at all.
8. **Pitfall #51 applied — the affiliate's live price, not the site's stale one.** `racknerd.com` says **VPS from $2.24/mo**; the site's own `/vps/racknerd/` page still says **$1.99/mo** in **5 places**. Only the live figure appears in the outline; the stale one is flagged for a separate commit (§8.1).
9. **Pitfall #47 applied — schema mirrored from the most recent entry.** The 2026-11-12 entry's 21-key set was copied exactly. The repo still has **1 legacy `drafts[]` entry with no `slug` key** → all iteration used `d.get('slug')`, never `d['slug']`.
10. **Pitfall #32 (health check)** — state.json diff to be assessed below against the health signature: deletions == 4, `drafts_count == len(drafts)`, and zero `\uXXXX` escapes.
11. **Pitfall #57 applied — the site's own claims are not facts.** The 2026-11-12 run flagged that two live articles assert an unsupported Black Friday launch window. Briefing item #3 today re-offered the *same* restock data the queued 2026-11-11 outline already owns — a second instance of the same discipline: the queued outline's fact bundle is a **capture**, not a fresh pick.
12. **NEW — freshness is not the same as recency of the incident.** The report is dated 2026-11-06 with a 2026-11-11 interpretation cluster, but **the incidents themselves are older** (Case #1 timeline Oct 2025; Case #2 log stamps 01/08/2026). The outline therefore frames the piece as a **pattern piece, not breaking news**, and says so in §1b and §9. Reporting it as a live incident would have been the same class of error as the briefing's own stale framing.
13. **NEW — a rejected brief item can still be worth a freshness check.** Item #2's regional price cut was off-shape, but its *mechanism* ("new orders and resizes only, existing prices unchanged") was tested against the site's published pricing articles before rejection — confirming the rejection on a second independent ground rather than one.

## 5. GSC context (live, 90d: 2026-08-15 → 2026-11-10)

**1,206 impressions / 1 click / 61 pages.** Homepage absorbs **928 (76.9%) at avg position 85.0** — the hub-gap is unchanged from the 2026-11-12 run (76.0% @ 84.8), so it is structural, not noise.

Head terms, all at **pos 74-97**: "vps provider" 80/94.7 · "virtual private server hosting reviews" 74/86.0 · "best vps for ai agents" 71/74.4 · "virtual server hosting reviews" 68/86.0 · "best vps provider" 60/84.3 · "best vps" 58/83.6 · "vps hosting review" 40/92.2 · "vps hosts" 30/92.5 · "reliable vps" 26/84.3.

Pages that **do** rank: provider reviews at **pos 3.6-7.4** (aliyun 4.9, netcup 5.7, lightnode 4.1, hosthatch 4.1, scaleway 7.4) and the pricing-trap guide at 5.7. → A daily slot must not force another listicle; a **specific-mechanism** piece with a concrete buyer checklist is the right unit.

## 6. Affiliate-label integrity

The affiliate's live product line is **rooted KVM VPS, full root, own IPv4, own control panel, no shared credential store** — verified on `racknerd.com/specials` (87,952 B): *"Every RackNerd VPS special includes full root access, 1 IPv4 address, SSD storage, and a 1 Gbps network port. You manage the server from ctrl or over SSH."* The article's advice — one credential per machine, one machine per workload, an unprivileged account for every monitoring/backup agent — is **literally true** of the product being recommended, and the recommendation is the article's genuine conclusion rather than a reverse-engineered justification. Same integrity class as the 2026-11-06 KVM-vs-Xen case and the 2026-11-12 secret-store case.

Live prices quoted: **$2.24/mo** entry; specials ladder **$21.99/yr (1 GB)** → **$35.99/yr (2 GB)** → **$59.99/yr (4 GB)** → **$89.99/yr (6 GB)** → **$119.99/yr (8 GB)**; **20 datacenter locations**; OS choice CentOS/Rocky/AlmaLinux/Fedora/Debian/Ubuntu + custom ISO on request.

## 7. Cross-link hygiene

9 targets: **6 live URLs verified on disk this run** (`vps-buying-guide`, `dreamhost-breach-2026-password-reuse-vps`, `vps-pricing-trap-guide-2026`, `racknerd-deep-review-2025`, `cheap-vps-local-llm-inference-2026`, `ai-agent-vps-api-guide`) + **3 queued outlines flagged publish-time-only** (`vps-ssh-security-host-key-checks-2026`, `xen-xsa-523-cross-vm-memory-flaw-vps-2026`, `vps-offsite-restore-backup-guide-2026`). Never emit an href for an article that does not exist yet.

## 8. Flagged (not fixed from a daily-outline slot)

1. `src/pages/vps/racknerd.astro` — stale **$1.99/mo** in **5 places** (`<title>`, meta description, intro, pros list, CTA); live is **$2.24/mo**.
2. `published[]` ∩ `drafts[]` overlap = **2 slugs** (`best-vps-deals-codes-2026`, `webdock-vps-review-2026`).
3. Two live articles still assert an **unsupported Black Friday launch window** (re-flagged; the Nov 9 piece says "two weeks away" while naming a window 8 days past).
4. Provider-page pipeline still dead: 69 `/vps/` pages, only 18 with impressions; homepage absorbs 76.9% at pos 85.0.
5. **A fresher cluster deliberately not taken** (recorded so the next run does not re-discover it): a worm-style campaign against remote-support software that hijacks technician sessions and pivots into customer environments through the support tooling — 2026-11-12, **9 outlets**, still moving. Subject is RMM/support software rather than a VPS; needs its own mechanism check before it earns a slot.
