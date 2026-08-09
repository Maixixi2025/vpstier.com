# VPSTier Daily Outline Preview — 2026-08-09 (Sunday)

## 1. Topic rationale and demand source

- **Priority route:** Tier 1 daily-briefing ⭐ substitute. Today's industry briefing (cron `3ea88f8bb2d0`, 2026-08-09 08:14 CST) **FAILED again** with HTTP 400 `reasoning_content` — the same provider error that killed the 8-06 and 8-08 briefings. No Tier-1 ⭐ story was produced. This is now a **recurring, persistent failure** (8-06, 8-08, 8-09 — 3 runs) and the **11th consecutive run where the Tier-1 #1 slot is a banned-provider/briefing non-starter** (banned-merchant-LLM runs 7-29→8-07 plus briefing-failure runs 8-06/8-08/8-09). Per the canonical recipe, treat this as the **default case** — fall back to direct Google News RSS for a fresh, verified, multi-outlet story, and reserve the rationale for WHICH substitute.
- **Fresh, verified hot news (direct Google News RSS fallback, since briefing failed):** A **new Linux kernel escape disclosure round (Aug 6–7, 2026)** — two long-dormant guest/host-escape vulnerabilities fixed in the **same stable-kernel release round (kernels 7.1.6 / 6.18.42 / 6.12.101 / 6.6.148, released Aug 3)**, disclosed publicly Aug 6–7:
  - **Zapscape — CVE-2026-64561** (KVM/x86 shadow-MMU use-after-free, disclosed Aug 6 by Hyunwoo Kim): a **guest-to-host KVM escape** — a privileged L1 guest VM can escape KVM isolation and run code on the host with kernel/root privileges when nested virtualization is exposed to untrusted guests. Public PoC targets AMD nested SVM/NPT on Linux 7.1.3; produces a root-owned `/Zapscape` file on the host. NVD lists Linux 5.9+ affected until the fixed stable releases; Red Hat preliminary CVSS 7.0 (CWE-825); no in-the-wild exploitation claimed.
  - **SCTPhantom — CVE-2026-64564** (18-year-old SCTP use-after-free, since Linux 2.6.25/2008, disclosed Aug 6 by Tencent Zhuque Lab): a **local-user → root + container-escape** flaw; Tencent reports root on Debian 13, Ubuntu 24.04, Rocky Linux 9, RHEL 9, OpenCloudOS and a container escape (6/8 attempts) with default seccomp and no CAP_NET_ADMIN/CAP_SYS_ADMIN; Tencent CVSS 8.5 (v4). Needs SCTP reachable; blocking the module removes the attack surface.
  - **Verified across 6+ independent named outlets with dates:**
    - The Hacker News, 2026-08-06 — "New Zapscape KVM Flaw Could Let Privileged L1 Guest Code Escape to Linux Hosts"
    - Phoronix, 2026-08-07 — "Zapscape Is The Latest Linux Vulnerability For KVM Guest-To-Host Escape, LPE"
    - CyberSecurityNews, 2026-08-07 — "CVE-2026-64561 Zapscape Lets KVM Guests Escape to Linux Host With Root Privileges"
    - 9to5Linux, 2026-08-07 — "New Debian 13 Kernel Security Update Fixes 'Zapscape' and 'SCTPhantom'"
    - CCB Belgium (national CERT), 2026-08-07 — "Warning: VM Escape Vulnerabilities in KVM, Patch Immediately!"
    - cyberkendra.com, 2026-08-06 — "Zapscape KVM Flaw Lets Guest VMs Seize Host Root"
    - (context) The Hacker News, 2026-08-07 — "18-Year-Old Linux SCTP Flaw Could Let Local Users Gain Root and Escape Containers"
  - **Body-verified facts:** concrete CVE numbers, kernel versions, CVSS, root-cause, patch status, and mitigation guidance were pulled from the fetchable The Hacker News article bodies (both the Zapscape and SCTPhantom pieces) during this run — not just headlines.
- **Why this is the right substitute:** (a) it is a genuine, dated, **multi-outlet security story only ~2 days old** — the strongest fresh signal available today; (b) it is **directly, personally relevant to every VPS owner**: KVM is the hypervisor running the overwhelming majority of budget VPS providers, and on unmanaged VPS the **guest-kernel patching is the buyer's job**; (c) the angle is **multi-provider-shaped** (which whitelisted provider patches its KVM hosts fast, and what the buyer must do on the guest side) → fits the news-analysis + buyer-guide format; (d) it is the **second major KVM-escape disclosure in a year** (after the July 2026 Januscape CVE-2026-53359 round), which is exactly the recurring-security-wave pattern that earns search + trust; and (e) it serves strong evergreen + timely intent ("linux kernel 7.1.6 update", "debian 13 kernel update zapscape", "cve-2026-64561", "how to patch my vps kernel", "kvm escape 2026", "is my vps provider patching kvm").
- **Content-gap evidence (verified):** `grep -riliE "zapscape|cve-2026-64561|sctphantom|sctp|kvm.{0,20}escape" /root/vpstier-site/src` returns **0 matches**. There is NO existing article on Zapscape, SCTPhantom, or any Linux kernel-escape patch story. The only related item is the **queued (unpublished) 2026-07-16 `januscape-kvm-escape-vps-security-2026` outline** — same general theme (KVM guest-to-host escape), different specific story (July Januscape CVE-2026-53359 vs this new Aug 6–7 CVE pair). Per the supersede-recipe, this is **partial overlap → write separately**, and surface the Januscape outline in on-hold items (do NOT auto-archive; recommend the user publish Januscape first or together, since today's new outline naturally references the Januscape lineage).
- **Publication guardrail:** every kernel/CVE fact (versions, CVSS, fixed-kernel list, distro tracker status) must be reverified from primary sources during the full-article draft (kernel.org stable releases, distro security trackers, the researcher write-ups). Each whitelisted provider's **KVM-host patching posture + guest kernel guidance** must be reverified from the provider's live VPS page + docs at draft time — do NOT inherit from any prior article's table. No banned merchant may be named in the article body. No `/zh/` routes (tree deleted 2026-06-11).

## 2. Slug, title, and description

- **Slug:** `linux-kernel-escape-patches-august-2026-vps`
- **Title:** `Linux Kernel Escapes 2026: Patch Your VPS Now (CVE-64561)`
- **Title length:** 57 characters (30–60 range) ✅
- **Description:** `Zapscape (CVE-2026-64561) lets a KVM guest escape to the host; SCTPhantom root + container escape. What VPS owners must patch and harden now.`
- **Description length:** 141 characters (70–155 range) ✅
- **Search intent:** News-analysis + informational/buyer-guidance (`cve-2026-64561`, `zapscape kvm`, `linux kernel 7.1.6`, `debian 13 kernel update`, `how to update kernel vps`, `kvm escape 2026`, `linux sctp flaw`, `is my vps safe`, `vps provider kernel patching`)
- **Language:** English only (vpstier.com is English-only since 2026-06-11)

## 3. Proposed H2 structure (9 sections, 8–10 required)

1. **Linux Kernel Escapes August 2026: What You Need to Know Right Now**
   - One-screen executive summary: two long-dormant Linux flaws (CVE-2026-64561 Zapscape KVM guest→host escape; CVE-2026-64564 SCTPhantom local→root + container escape) disclosed Aug 6–7, both fixed in the same stable-kernel round (7.1.6 / 6.18.42 / 6.12.101 / 6.6.148, Aug 3). What each means for a VPS owner, in one line each; the "patch fast / verify your provider / harden your guest" three-step action plan.
2. **Zapscape (CVE-2026-64561): The KVM Guest-to-Host Escape**
   - The news hook, verified: disclosed Aug 6 by security researcher Hyunwoo Kim; a stale-root check ordering flaw in KVM's x86 shadow-MMU → use-after-free that lets a privileged L1 guest escape to the host with kernel/root privileges when nested virtualization is exposed to untrusted guests. Public PoC (AMD nested SVM/NPT, Linux 7.1.3) writes a root-owned `/Zapscape` file on the host. NVD: Linux 5.9+ affected until fixed stable releases; Red Hat preliminary CVSS 7.0, CWE-825 (expired pointer dereference). No in-the-wild exploitation claimed.
3. **SCTPhantom (CVE-2026-64564): The 18-Year-Old Root + Container Escape**
   - The second flaw in the same round: a use-after-free in Linux SCTP networking, in every kernel since 2008 (Linux 2.6.25). Tencent Zhuque Lab discloses Aug 6: local user → root, and a demonstrated container escape (6/8 attempts) under default seccomp with no CAP_NET_ADMIN/CAP_SYS_ADMIN; root reproduced on Debian 13, Ubuntu 24.04, Rocky Linux 9, RHEL 9, OpenCloudOS. Tencent CVSS 8.5 (v4); NVD unassigned as of Aug 7. Needs SCTP reachable on the target — blocking the module removes the attack surface.
4. **The Fixed Kernels: 7.1.6 / 6.18.42 / 6.12.101 / 6.6.148 — Are You On One?**
   - The actionable core: the Aug 3 stable release round that ships both fixes; how to check `uname -r` on your VPS; the caveat that vendors backport fixes without rebasing, so a version string alone doesn't prove coverage — check your distro's security tracker (Debian bullseye/bookworm/trixie listed vulnerable as of Aug 6 for Zapscape; Ubuntu/Rocky/RHEL trackers for SCTPhantom). A short "what to run" command table.
5. **Who Patches Your KVM Host? Managed vs Unmanaged Responsibility**
   - The VPS-buyer reality: on a managed VPS, the provider patches the KVM host + often the guest; on an unmanaged VPS, **you** own the guest kernel. Walk through which whitelisted providers document fast host-patching / managed-update service (reverify each from the live provider page at draft time), and the honest line that no provider publishes its KVM-patch SLA blindly — ask / check status pages.
6. **What VPS Buyers Should Do This Week (Practical Hardening Checklist)**
   - A concrete, ordered checklist: (1) `uname -r` + distro tracker check; (2) `apt` / `dnf` full upgrade + reboot; (3) block/unload SCTP if unused (`modprobe -r sctp`, blacklist); (4) treat nested virtualization as untrusted by default; (5) enable unattended-upgrades or a patch schedule; (6) snapshot/backup before rebooting a production box. Tie RackNerd's root-access budget VPS to the "you need shell access to do this yourself" reality.
7. **Does This Change Which VPS You Should Pick?**
   - The buyer-guidance pivot: security hygiene (fast patching, transparent update policy) becomes a selection criterion alongside price/RAM/NVMe. Reference the whitelisted providers (see §5) and note that a **root-access budget VPS you can patch yourself** (RackNerd) is the honest default for the unmanaged route, while managed tiers (ScalaHosting / Hostinger / A2 / Bluehost) shift patching to the provider. No banned merchant may be named.
8. **The Bigger Picture: A Year of Linux Escape Waves**
   - Broaden the lens: this is the second major KVM-host escape wave in a year after the July 2026 Januscape (CVE-2026-53359) round, plus a growing run of AI-assisted kernel-vulnerability discovery (the SCTPhantom finder credits its Corvus AI pipeline). What that trend means for VPS buyers' patching discipline in 2026. Cross-link to the queued Januscape theme and the site's VPS-buying guide.
9. **Final Verdict: Patch Discipline Wins in 2026**
   - Close with the action imperative: this week's disclosure is a reminder that on an unmanaged VPS the kernel is your responsibility; pick a provider that patches fast and keep your guest updated. Primary CTA: RackNerd for an affordable root-access VPS where you control the kernel; secondary: managed tier for readers who'd rather outsource patching.

## 4. FAQ plan (5 questions, within 3–5)

1. **Is my VPS affected by the Linux kernel escapes (CVE-2026-64561 / 64564)?**
2. **How do I check which kernel my VPS is running and whether it's patched?**
3. **On an unmanaged VPS, who is responsible for patching the kernel — me or the host?**
4. **What's the fastest way to patch my VPS kernel this week?**
5. **Should I switch VPS providers over a Linux kernel vulnerability?**

## 5. RackNerd affiliate placement plan

Use the exact affiliate destination for every commercial CTA: `https://my.racknerd.com/aff.php?aff=16299`

1. Exec-summary callout (§1): "you need root access to patch — an affordable unmanaged VPS you control" — `https://my.racknerd.com/aff.php?aff=16299`
2. Fixed-kernels section (§4): root-access budget VPS for `uname -r` + distro-upgrade control — `https://my.racknerd.com/aff.php?aff=16299`
3. Managed-vs-unmanaged section (§5): the unmanaged/root-access route where you own the kernel — `https://my.racknerd.com/aff.php?aff=16299`
4. Hardening checklist (§6): "run the checklist on a VPS with full root" — `https://my.racknerd.com/aff.php?aff=16299`
5. Provider-selection section (§7): budget self-managed pick for patching control — `https://my.racknerd.com/aff.php?aff=16299`
6. Final verdict (§9): primary CTA button — `https://my.racknerd.com/aff.php?aff=16299`

6 placements (at the 6-required floor) ✅. All placements identify RackNerd accurately as the budget/root-access unmanaged option, honestly framed against managed tiers; no link is labeled as a sign-up for another provider. The RackNerd SSDs-vs-NVMe and unmanaged-responsibility trade-offs are stated honestly so the guide reads as trustworthy.

## 6. Internal-link plan

Only existing published routes (verified filenames in `/root/vpstier-site/src/pages/blog` and `/root/vpstier-site/src/pages/vps`):

1. `/vps/racknerd/` — budget root-access provider profile (CTAs in §5, §7)
2. `/vps/vultr/` — global/dev provider profile, guest-kernel control (§5, §7)
3. `/vps/digitalocean/` — developer provider profile (§5, §7)
4. `/vps/hostarmada/` — managed VPS provider profile (managed-patching route, §5)
5. `/vps/hostinger/` — cheap managed-feel provider profile (§5)
6. `/vps/ovhcloud/` — EU provider profile, NVMe/unlimited-traffic angle (§7)
7. `/blog/vps-buying-guide/` — general VPS buying guidance (intro, §7)
8. `/blog/vps-pricing-trap-guide-2026/` — renewal-cost discipline (§1, §7)
9. `/blog/cheap-vps-local-llm-inference-2026/` — self-managed root-access workloads that need the same hygiene (§6)
10. `/blog/2026-shutdown-cloud-services-vps-migration/` — why pick a provider you control (§7)

No new files outside existing routes. Zero references to `/zh/` (route tree deleted 2026-06-11).

## 7. Self-check pre-flight

| Check | Result |
|---|---|
| Prohibited merchant references (banned-list audit) | 0 in outline draft incl. article body ✅ (the excluded merchant is never named, incl. in "avoid"/rationale-desc sections) |
| CJK chars in outline | 0 ✅ |
| Removed-language routes (zh-language audit) | 0 new ✅ |
| Title length | 57 / 30–60 ✅ |
| Description length | 141 / 70–155 ✅ |
| H2 count | 9 / required 8–10 ✅ |
| FAQ questions per page | 5 (within 3–5) ✅ |
| RackNerd affiliate placements | 6 ≥ 6 required ✅ |
| CTA destination = exact match (`https://my.racknerd.com/aff.php?aff=16299`) | yes ✅ |
| Existing internal routes only | yes ✅ (all 10 verified on disk) |
| Tier-1 from briefing | briefing FAILED (400) 3rd consecutive run; default-case fallback via direct Google News RSS ✅ |
| Tier-2 add-provider | NOT applied (news-analysis guide, no new provider card) ✅ |
| Streak pressure | recent picks comparison-shaped (8-04, 8-08) + single-provider (8-07); security buyer-guide chosen on multi-provider angle shape, not streak ✅ |
| Conflicts with pending politicalization outlines | none — orthogonal security-story; does not compound backlog ✅ |
| Conflicts with queued Januscape outline | partial overlap (same KVM-escape theme, distinct new CVE) → separate entry, Januscape flagged on-hold, NOT auto-archived ✅ |
| Content-gap evidence | 0 zapscape/64561/sctp/kvm-escape matches in `src/` ✅ (verified grep) |
| Facts body-verified | yes — CVE numbers, kernel versions, CVSS, root-cause from fetchable THN bodies ✅ |

## 8. Run-record notes / on-hold items (not part of this run)

- **Today's industry briefing FAILED (cron `3ea88f8bb2d0`, HTTP 400 `reasoning_content`)** — 3rd consecutive failure (8-06, 8-08, 8-09). This is now a **persistent failure**; treat direct Google News RSS as the expected topic source until it recovers. The cron fell back per the canonical recipe and verified the Zapscape/SCTPhantom story from 6+ named outlets with dates + fetchable THN bodies.
- **GSC today (cron `5570fe2cffa6`)**: vpstier.com shows only `ovh vps ssd` (rank 28) — that signal is **already captured** by the pending 8-07 `ovhcloud-vps-review-2026` outline (capture-check: not a new pick). No NEW GSC demand signal today; today's pick is driven by the fresh security disclosure + clean content gap.
- **Untracked 8-05 outline** (`us-data-center-politics-2026-vps-impact`): on disk, never entered in state.json. Still flagged; user reconciles at publish.
- **Januscape partial-overlap flag:** the queued 2026-07-16 `januscape-kvm-escape-vps-security-2026` outline covers the same general theme (KVM guest-to-host escape) but the July 2026 CVE-2026-53359 story, now superseded in urgency by the Aug 6–7 Zapscape/SCTPhantom disclosures. Today's new outline references the Januscape lineage (§8). **Recommendation (not auto-applied):** the user may want to (a) publish the Januscape outline first so both KVM-escape pieces coexist, or (b) fold Januscape's July context into today's new article and archive the Januscape outline. Cron does not auto-archive.
- **DC-politicalization queue (3-4 overlapping):** `ny-data-center-moratorium` (07-15), `data-center-politicalization` (8-04), untracked `us-data-center-politics` (8-05). User decides archive/publish; cron does not auto-archive.
- **Uncommitted-backlog risk (rediscovered 8-08, still open):** `git status --short` shows multiple untracked prior outline/run-record files in `drafts/` (08-01, 08-03, 08-04, 08-05, 08-07 outlines + run-records). Per the "commit after every run" rule, this run commits its own 3 files (today's outline + run-record + state.json); the accumulated untracked backlist is flagged here for a user-scheduled cleanup commit (NOT swept blindly).
- **Full pending `outline_pending_publish` queue in `drafts[]`** remains backed up (greengeeks, hostdare, vps-kyc, ny-data-center, januscape, black-friday-early, agent-zero, cloudflare-markdown, luxvps×2, cloudflare-internal-dns, vps-shutdown, 5-best-cheap-summer, namecheap, serverhost, data-center-politicalization, ovhcloud, best-budget-vps-for-woocommerce). Today's outline is appended as a separate `outline_pending_publish` entry, NOT merged. The user's publish-gate is the constraint.

## 9. Awaiting user action

- Reply `publish` to trigger the full Astro page write, build, git push, and `wrangler pages deploy` of:
  - `src/pages/blog/linux-kernel-escape-patches-august-2026-vps.astro`
  - Card insertion into `src/pages/blog/index.astro`
  - `drafts/state.json` updated with the new `published[]` entry
- Optional: reply `archive 8-04 + 8-05 + 07-15` to reconcile the politicalization backlog; reply `publish` on any queued outline (incl. the Januscape KVM-escape outline) to publish those surfaces separately.
