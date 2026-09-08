# Outline: OpenBSD on a $4 VPS: Self-Host OS Guide 2026

**Date:** 2026-09-08
**Slug:** `openbsd-vps-self-host-2026`
**Author / Cron:** vpstier-daily-outline

---

## 1. Rationale + Hot-Source

**Briefing status:** today's briefing produced 2 vpstier stars (2026-09-08 08:04 UTC). Triage:

| # | Item | Verdict | Reason |
|---|---|---|---|
| 1 | **"Run OpenBSD on DigitalOcean for $4/month"** (HN 204p/95c, posted 2026-08-25 by speckx, nil.wallyjones.com) | **SELECTED** | Fresh + multi-outlet (HN high-points + author's site + 95-comment discussion thread). Body-verified: dated Aug 23 2026, $4.24/mo DO Basic droplet with 512MB RAM + 1vCPU + 500GB transfer + 10GB disk, custom-image upload of OpenBSD 7.9 miniroot79.img, full httpd(8) + acme-client(1) + Let's Encrypt walkthrough. |
| 2 | "How to Improve VPS Profitability While Reducing Support Load" (LowEndBox 2026-09-04) | **REJECTED — OFF-SHAPE (already classified twice)** | CloudLinux commercial op-ed aimed at hosting PROVIDERS (LVE / Imunify360 / PHP X-Ray / margin levers); the audience is the seller's P&L, not the vpstier buyer. Already marked OFF-SHAPE in 9-06 + 9-07 daily-outlines (see `drafts/outline-2026-09-06-vpstier-daily.md` and `drafts/outline-2026-09-07-vpstier-daily.md`). Today's briefing re-surfaces the same item; consistent rejection stands. |

**Variant label:** canonical-variant-0 (briefing succeeds, 1 ⭐ selected, 1 ⭐ off-shape — drop, don't rescue).

**Coverage-gap verification (body-grep across 134 on-disk blog + 76 on-disk /vps/ files, total 529 H2s):**
- `OpenBSD` — only 1 file (`tmdhosting-vps-review-2026.astro`), in a single sentence about custom-ISO support for uploading OpenBSD ISOs. **Zero dedicated OpenBSD self-host articles.**
- `OpenBSD httpd` / `OpenBSD install` / `OpenBSD droplet` / `OpenBSD VPS` / `$4/month OpenBSD` / `miniroot` / `acme-client(1)` — **0 hits site-wide**.
- The only existing OS-comparison page is `almalinux-vs-rocky-vs-ubuntu-vps-2026` — purely RHEL-derivative Linux distro comparison. **No BSD coverage. No OS-self-host-on-budget-VPS guide. No self-hosted-UNIX/VPS roundup.** Genuine 0-gap.

**Editorial rationale:** the BSD/Linux divide is the most under-served OS axis on vpstier. The AlmaLinux piece covers the choice *between three RHEL-derivative Linux distros*; this piece covers the choice *between staying on Linux and going to a BSD* (OpenBSD primary, with FreeBSD / NetBSD as alternatives). The HN item is a clean, dated, body-verifiable anchor (speckx, OpenBSD 7.9, httpd(8), acme-client(1), DO custom-image $4/mo Basic). Buyer takeaway: which VPS host lets me run the OS I actually want, and what does the trade-off look like?

**Why not "BSD vs Linux on a VPS" generic comparison?** Generic would be too abstract; the HN item is concrete + dated + cheap. Anchor on the cheap end of the BSD-self-host market, then expand.

---

## 2. Slug / Title / Description

- **Slug:** `openbsd-vps-self-host-2026`
- **Title (EN, 50 chars):** `OpenBSD on a $4 VPS: Self-Host OS Guide 2026` — measured **len() = 44** (30–60 gate ✅)
- **Description (EN, 134 chars):** "Run OpenBSD on a $4/mo VPS in 2026 — DO custom-image upload, HostHatch/Netcup/VirMach ISO support, BSD vs Linux picker's checklist." — measured **len() = 131** (70–155 gate ✅)

**Title character count (Python `len()`):** 44
**Description character count (Python `len()`):** 131

---

## 3. 8-10 H2 Sections

1. **Why Run OpenBSD on a $4 VPS in 2026?** — the BSD/Linux buyer tradeoff in one paragraph (security-by-default + httpd(8) base + lean RAM footprint + 7.9-stable release cadence). Sets up the speckx HN hook.
2. **What the HN story actually proves (and what it doesn't)** — speckx's specific setup: DO Basic $4.24/mo, 512MB RAM, OpenBSD 7.9 miniroot79.img, custom-image upload step, httpd(8) + acme-client(1) + Let's Encrypt. Note that DO does NOT have an official BSD image — the article is precisely about the workaround.
3. **Why DigitalOcean charges you extra for the custom-image upload** — DO's hidden $0.024/GB-month charge for storing the custom image until you delete it. Pitfall buyers miss; speckx flags it; reproduce the calculation.
4. **Which VPS hosts actually let you upload a custom ISO (the 2026 verified list)** — HostHatch (custom ISO support, AMD EPYC, 14 regions from $4/mo), Netcup (ISO install via control panel + 3 EU DCs Nuremberg/Vienna/Dusseldorf), VirMach (custom ISO mounting via Virtualizor, KVM plans, 14 US/EU DCs), AlphaVPS (30+ OS templates + KVM full root), Cherry Servers (snapshots + ISO install + ARM Ampere option), 1984.is (ISO 27001 + out-of-band VNC + privacy-friendly jurisdiction), AccuWeb (KVM/Xen + 16 DCs + easy OS reinstalls), ZAP-Hosting (game-server-grade + KVM full root + custom ZAP panel). Verified via on-disk `/vps/` profiles + provider docs.
5. **The RackNerd honesty note** — RackNerd does NOT advertise a one-click custom-ISO workflow for BSD on its standard plans; the SolusVM control panel allows ISO mount in some cases but isn't a documented BSD-onboarding path. Anchor RackNerd on **annual affordability + 7-yr community longevity + 6x Inc. 5000 honoree + value-for-shared-Linux-workloads** — NOT on BSD self-host capability. The honest-when-advertiser-lacks-the-feature pattern (8-21/8-23 precedent).
6. **BSD vs Linux on a budget VPS: the actual trade-off matrix** — RAM footprint (OpenBSD base install ~150MB vs Ubuntu Server ~700MB), package ecosystem (ports tree vs apt), kernel update cadence, security defaults, container story (Linux wins, BSD has jails but no Docker-equivalent mainstream), tooling maturity for common workloads (WordPress / Node / Python / Postgres). Honest: BSD wins on RAM/security defaults; Linux wins on tooling/community.
7. **Step-by-step: replicate speckx's setup (or do it cheaper elsewhere)** — DO path verbatim from HN, then a 4-step HostHatch / Netcup / VirMach alternative path (sign up → upload OpenBSD 7.9 miniroot79.img → select during VM create → install via VNC console). Time-cost: ~30 min from blank droplet to httpd(8) serving a static page.
8. **Which workloads actually benefit from OpenBSD on a cheap VPS** — static sites + reverse proxies + VPN endpoints + personal blogs (speckx's use case). Honest: NOT a fit for AI/LLM inference, NOT a fit for Docker-heavy stacks, NOT a fit for managed-database workloads.
9. **The 5-question BSD-on-VPS readiness checklist** — (1) Is your workload single-purpose / static-site / VPN-ish? (2) Are you comfortable with BSD man pages + ports tree? (3) Can you operate without Docker? (4) Do you need 24/7 GUI tooling (cPanel/Plesk)? (5) Is RAM < 1GB acceptable for your app? Yes-to-1-3 = OpenBSD is a fit. Yes-to-4-5 = stick with Linux.
10. **FAQ + bottom line** — RackNerd primary CTA anchored on annual affordability for the Linux-default workload; HostHatch/Netcup/VirMach secondary for the BSD-on-budget case; DO tertiary for the speckx-replication scenario.

---

## 4. FAQ (3-5 questions)

1. **Can I run OpenBSD on any VPS provider?** — Only on hosts that allow custom ISO upload (HostHatch, Netcup, VirMach, AlphaVPS, Cherry Servers, 1984.is, AccuWeb, ZAP-Hosting, or any DO/Linode/Vultr via the custom-image workaround speckx used). Most budget hosts ship Ubuntu/CentOS/Alma templates only; check before signing up.
2. **Why pay for OpenBSD when Ubuntu is free on every host?** — Three reasons: smaller attack surface (OpenBSD has had only 2 remote-root exploits in default install in 20+ years), leaner RAM footprint (~150MB base vs ~700MB Ubuntu Server), and a curated ports tree with consistent quality. The trade-off is a smaller software ecosystem and no Docker equivalent.
3. **What about FreeBSD instead of OpenBSD?** — FreeBSD is closer to Linux in tooling (jails, ZFS, bhyve), has more cloud-provider first-party support (some providers ship FreeBSD templates, almost none do OpenBSD), and runs Docker. OpenBSD wins on security defaults + minimalism. Both are legitimate; pick by workload shape.
4. **Is the $4/mo DO Basic plan really enough for OpenBSD?** — Yes for static sites, reverse proxies, VPN endpoints, and personal blogs (speckx's exact use case). NO for AI inference, managed databases, Docker-heavy stacks, or anything needing >1GB RAM. Verify the workload fits 512MB before committing.
5. **What's the cheapest VPS that supports OpenBSD custom ISO?** — HostHatch $4/mo AMD EPYC plans + VirMach KVM custom-ISO via Virtualizor + Netcup G7 ISO install via control panel all support it at the $4-5/mo floor. The DO Basic $4/mo works too, with the custom-image-upload workaround + the storage-charge caveat.

---

## 5. Internal-link plan (verified-on-disk only)

Verified present on disk (no pending companions):
- `/blog/almalinux-vs-rocky-vs-ubuntu-vps-2026/` — sister OS-tier-comparison article (Linux distros only)
- `/blog/vps-vs-vds-2026-which-to-choose/` — virtualization-tier selection (different axis)
- `/blog/best-ryzen-gaming-single-core-vps-2026/` — CPU-tier selection (different axis)
- `/blog/cloud-outages-2026-redundant-vps-setup/` — operational resilience (different axis)
- `/blog/lifetime-vps-deals-2026-real-cost-vs-marketing/` — pricing-model taxonomy
- `/vps/hostHatch/` — custom-ISO profile
- `/vps/netcup/` — ISO install profile
- `/vps/crowncloud/` — custom-ISO profile (additional option)
- `/vps/linode/` — no custom ISO but has recovery kernel + stacked distro templates
- `/vps/racknerd/` — annual-affordability honest anchor

DO NOT link to pending `vps-kyc-privacy-checklist-2026` or `agent-zero-vps-setup-guide-2026` — they're still queued.

---

## 6. RackNerd CTA placements (≥6 required)

1. Top intro: "If your workload is Linux-default (WordPress / Node / Python / Docker), start with the [RackNerd annual KVM specials](https://my.racknerd.com/aff.php?aff=16299) from $21.99/yr — best price/perf for shared-Linux workloads."
2. §5 honesty note: "If BSD self-host is the goal, RackNerd isn't the right fit — use [HostHatch custom-ISO plans](https://hosthatch.com/) or [Netcup G7 ISO install](https://www.netcup.eu/) instead. But for the typical Linux-default buyer, [RackNerd annual deals](https://my.racknerd.com/aff.php?aff=16299) deliver 60-70% savings over monthly billing."
3. §6 trade-off matrix: "For Linux-default workloads, [RackNerd's KVM specials](https://my.racknerd.com/aff.php?aff=16299) keep the door open if you decide BSD is too lean."
4. §7 step-by-step: "If you go the Linux route instead, [RackNerd annual plans](https://my.racknerd.com/aff.php?aff=16299) skip the custom-image dance entirely — Ubuntu/Debian/Alma templates deploy in 60 seconds."
5. §9 checklist: "If your answers push you back to Linux, [RackNerd KVM annual](https://my.racknerd.com/aff.php?aff=16299) is the budget pick."
6. §10 bottom line: "Primary CTA: [RackNerd annual KVM specials from $21.99/yr](https://my.racknerd.com/aff.php?aff=16299) for Linux-default buyers. For BSD-on-budget self-hosters, HostHatch or Netcup are the honest picks."
7. Bonus FAQ placement: "Q: What's the cheapest OpenBSD VPS? A: HostHatch $4/mo for custom-ISO, or DO Basic $4/mo via the speckx custom-image workaround. For Linux-default buyers, [RackNerd annual deals](https://my.racknerd.com/aff.php?aff=16299) are cheaper than both."

Total RackNerd CTA placements: **7** (≥6 satisfied).

---

## 7. Self-Check

| Check | Result |
|---|---|
| Banned-merchant zero-check (`grep -ci` across the WHOLE draft) | **0 ✅** (verified by category language only — no brand-name tokens embedded anywhere) |
| CJK / non-ASCII characters (`grep -cP "[\u4e00-\u9fff\u3400-\u4dbf\u3040-\u30ff]"` over draft) | **0 ✅** (English-only; no /zh/ path; site is English-only since 2026-06-11) |
| `/zh/` references in draft | **0 ✅** (route tree deleted; no plan to re-add) |
| Title length `len()` | **44 ✅** (30–60 gate) |
| Description length `len()` | **131 ✅** (70–155 gate) |
| H2 count | **10 ✅** (8–10 gate) |
| FAQ count | **5 ✅** (3–5 gate) |
| RackNerd CTA placements | **7 ✅** (≥6 gate) |
| On-disk body-grep-0 for OpenBSD self-host angle | **VERIFIED ✅** (5 distinct tokens = 0 hits site-wide) |
| HCU-compliance preview at full-draft stage | **COMMITTED** — ≥2 real artifacts (custom-image charge calculation + speckx-walkthrough step-list + verified provider ISO-support table), ≥800 unique words target, "Last verified 2026-09-08" stamp required, first-person voice, no templated comparison-crutch |

---

## 8. On-hold items / notes for user

- The 9-08 briefing's other star (LowEndBox "Improve VPS profitability / support load") is the **3rd independent daily re-surface** of the same CloudLinux op-ed — all three runs (9-06, 9-07, 9-08) classified it OFF-SHAPE for the vpstier buyer ICP. Consistent rejection. The LowEndBox editorial slot in 9-08 could be redirected at a fresher vendor-side story if the briefing picks it up again next week.
- 43 `outline_pending_publish` entries remain in `drafts[]` (last_run 2026-09-07). Today's append makes 44. The user is the publish-gate.
- CLOUDFLARE_API_TOKEN confirmed ACTIVE (verified 2026-09-08, expires 2027-09-02). The 7-day expiry-blocker (08-31 → 09-06) is resolved.

---

## 9. State.json plan

- `drafts[]` append: new entry with slug `openbsd-vps-self-host-2026`, date `2026-09-08`, status `outline_pending_publish`, title_en = "OpenBSD on a $4 VPS: Self-Host OS Guide 2026", description_en = "Run OpenBSD on a $4/mo VPS in 2026 — DO custom-image upload, HostHatch/Netcup/VirMach ISO support, BSD vs Linux picker's checklist.", 7 RackNerd CTA placements, 10 H2 / 5 FAQ.
- `drafts_count`: 43 → 44 (BUMP AFTER append).
- `last_run`: "2026-09-08" (explicit assignment).
- `publish_notes` (string, `\n`-separated): append new line with date + natural-language title fragment (per the 8-31 fix; kebab slug `{slug}` NOT embedded in the line).
- `json.dump(..., ensure_ascii=False)` to preserve Unicode (the 8-31 rule).
- 4-check verifier: drafts_count == len(drafts), last_run == today, today in publish_notes, natural-title-fragment in publish_notes.

---

## 10. Commits (two-commit pattern)

1. `feat:` outline + run-record (this file + a parallel `run-record-2026-09-08-vpstier-daily-outline.md`).
2. `chore(state):` state.json update (drafts append + count bump + publish_notes line).
3. Push `main`.

---

## 11. Pitfalls re-checked

- **Off-shape rejection stands** for the LowEndBox profitability item (now 3rd time classified; canonical 9-06 / 9-07 precedent).
- **OpenBSD-on-RackNerd honesty pattern:** do NOT promise BSD-onboarding on RackNerd (SolusVM ISO mount exists in some setups but isn't a documented BSD path); anchor RackNerd on Linux-default + annual affordability.
- **Custom-image charge calculation** must be reproducible — speckx flags the per-GB-month charge; the article should show the math ($0.024/GB/mo × image size × months). Verify the per-GB-month number from a current DO pricing page at full-draft time.
- **Body-grep on `acme-client(1)` and `httpd(8)`** with parens — these parens are shell-special characters in regex; the grep must use fixed-string or escape the parens. Documented as a verifier gotcha.
- **The `$4.24/mo` figure from speckx** is post-tax (speckx says "$4.24 after tax"); the article should distinguish the $4 list price from the post-tax $4.24 actual. Verify current DO tax handling for the relevant region.

---

*End of outline. Awaiting user `publish` reply.*
