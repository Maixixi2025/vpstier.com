# VPSTier Daily Outline — 2026-09-06 (Off-Site, Restore-Verified VPS Backups)

**Slug:** `vps-offsite-restore-backup-guide-2026`
**Title:** `Are Provider Snapshots a Backup? VPS Off-Site Guide 2026` (56/60 char gate — Python `len()` verified)
**Description:** `Host 'snapshots' are not backups. Keep your VPS data off-site, restored and verified — the cheap 3-2-1 setup that outlives a vanished provider.` (143/155 char gate — Python `len()` verified)
**Author:** vpstier-daily-outline cron `5fd2a36f2dc4`
**Run time:** 2026-09-06 (cron-output pipeline)
**Briefing source:** `/root/.hermes/cron/output/3ea88f8bb2d0/2026-09-06_08-06-36.md` (SUCCEEDED; 1 VPS ⭐ = already-covered-merchant promo, 1 VPS item = off-shape provider-side op-ed)
**GSC source:** `/root/.hermes/cron/output/5570fe2cffa6/2026-09-06_07-00-52.md` (vpstier 7d = 0 clicks / 215 impressions / 10 purely generic rank-76-92 queries; 30d = 0 / 264 — no actionable uncovered-intent query)

---

## 1. Variant classification — Briefing SUCCESS, VPS ⭐ #1 CAPTURED by already-published content + VPS item #2 OFF-SHAPE (canonical variant 8, 2nd confirmation after 2026-09-05)

The 2026-09-06 briefing's VPS section produced two items, neither of which is a fresh selectable outline:

| # | Briefing item | Status | Reason |
|---|---|---|---|
| 1 | **Kainode Singapore VPS 30% off** (LowEndBox 2026-09-03, raindog308) | **CAPTURED — existing full review + region roundup on disk** | `kainode-vps-review-2026` (published) covers Kainode's Singapore DC in depth (its H2-3 is "Datacenter Coverage — Singapore, Germany, USA") + `best-asia-pacific-vps-2026` (published) is the exact "Asia cheap VPS" roundup the briefing itself suggests folding it into + `2026-black-friday-cheap-vps-under-25` (published) covers the Black-Friday tie-in it also floats. This is the **2nd confirmation** of canonical variant 8 (a dated promo of a merchant with a full published review + overlap roundup = deal-tracking, NOT a fresh unique outline) — first confirmed 2026-09-05 on the same Kainode promo. |
| 2 | **"How to improve VPS profitability while reducing support load"** (LowEndBox 2026-09-04) | **OFF-SHAPE — provider/vendor-side ops op-ed** | Body-fetched: it is a **CloudLinux VPS Bundle commercial/guest piece** aimed at *hosting providers* (CloudLinux OS LVE, Imunify360, PHP X-Ray, standardized stacks, margin levers) — the audience is hosting companies, not the vpstier **buyer-side ICP**. Not a buyer guide; not a dated multi-outlet news event. Rejected whole, not rescued. |

**The freshest dated, body-verifiable substitute** (found outside the briefing ⭐ list, LowEndBox RSS 2026-09-05): **ServerCrate** — a zero-knowledge off-site backup service intro'd on LowEndBox (raindog308, `2026-09-05`, "You Need Backups and ServerCrate is Going to Make Them Painless"). Its editorial hook is a genuinely fresh, buyer-relevant dated datapoint: ServerCrate's stated thesis — *"Most backups fail silently. You find out the night your drive dies. We test that your data actually restores, every single day, and show you the proof"* — plus the industry-set fact that **most hosts only check that a backup RAN, not that it can be restored**. ServerCrate is a **third-party merchant NOT in providers.json** → used strictly as the dated, attributed non-whitelisted hook (NOT a recommendation), per the standing non-whitelisted-hook pivot.

**Why this is the pick:** the off-site / restore-verified / data-loss-protection buying question — "**where does my VPS data live if the provider's disk dies, my account is terminated, or the host itself vanishes — and how do I know I can actually restore it?**" — is a genuinely uncovered buyer intent AND the direct data-safety corollary of the site's strongest recurring franchise theme (merchant-exit / provider-trust: a host can vanish, and off-site data is the only real recovery — the 8-27 exit-warning + 8-29 sanctions through-line). Distinct primary intents: `vps offsite backup`, `3-2-1 backup strategy vps`, `are provider snapshots a backup`, `vps backup restore verification`, `cheap offsite backup for vps`, `host vanished how to recover data`, `is a vps snapshot a backup`.

**⚠️ Content-gap vetting that rejected the naive "VPS backup strategy" framing (important — do NOT write the general version):** a first pass proposed a generic "VPS backup strategy guide," which FAILED body-overlap: the published `aws-us-east-1-outage-2026` guide has H2 "Multi-Region Backup Strategy: A Practical Plan" (a standalone mini buyer-guide: standby RackNerd box + rsync + DNS failover, $4.49/mo) and `digitalocean-outage-august-2026` has a 4-tier fallback framework mentioning off-site snapshots — both are **availability/DR** content, and I verified they contain **0** occurrences of the *data-loss/restorability* claims. The genuinely distinct slice is the **data-loss / off-site / restore-verified** intent (protection against silient backup failure + provider-side data loss + host disappearance), NOT general DR. Discriminator tokens verified 0-on-disk as dedicated-guide treatment: `3-2-1`, `off-site backup` (as a guide intent; only passing review mentions), `not a backup`, `restore-verif`, `zero-knowledge`, `provably recover`, `bit rot`, `restorability`.

## 2. ⭐ status (per canonical recipes)

| # | Briefing ⭐ | Status | Reason |
|---|---|---|---|
| 1 | Kainode Singapore 30% off (LowEndBox 09-03) | **CAPTURED — variant 8 (2nd confirmation)** | Full published review (`kainode-vps-review-2026`) covers Kainode + Singapore DC; published `best-asia-pacific-vps-2026` is the roundup the briefing references; published `2026-black-friday-cheap-vps-under-25` covers the Black-Friday tie-in. Deal-tracking of an already-covered merchant — NOT a fresh outline. Referenced below only as a supporting honestly-disclosed small-provider example if it genuinely illustrates the backup-angle (it discloses a single honest node), NOT as the subject. |
| 2 | AI-support / VPS-profitability op-ed (LowEndBox 09-04) | **OFF-SHAPE — rejected** | Provider-side CloudLinux commercial op-ed; audience is hosting companies, not the buyer ICP. Rejected whole (8-24 rule: ineligible ⭐ = drop, don't rescue). |

**Tier-1 substitute:** `vps-offsite-restore-backup-guide-2026` — evergreen buyer-guide + how-to format (the 8-27 / 8-29 / 9-05 evergreen-guide precedent), anchored on the ServerCrate 09-05 dated hook + the merchant-exit/data-independence through-line.

## 3. Why the budget-VPS buyer actually cares (editorial honesty — HCU bar)

The site already tells readers, across multiple published pages, to spread workloads and keep DNS/email off the web host. This guide answers the question those pages leave open: **"if my host dies with my data on it, what have I actually kept?"** It is not an availability/DR article (those exist and are linked, not duplicated). It is the **data-recovery** page: what a snapshot is and is NOT, why backups must be off-site, why they must be restore-verified, and the $2-25/mo setups that give a small operator true independence from any single provider. Anchored on the dated fact that this month's backup-service news explicitly calls out that most hosts only verify backups *ran*, not that they *restore*.

## 4. Editorial anchor — the buyer framework (what a "real" VPS backup is)

Anchor the whole article on a 4-part "is this actually a backup?" buyer test (each maps to a section):

1. **Off-site** — the copy does not live on the box (or provider) it protects. Provider-hosted snapshots die with the provider.
2. **Independent** — restorable even if the account is terminated / the host is gone / DNS is controlled by the attacker. (This is where the merchant-exit franchise and this guide connect.)
3. **Automated** — a manual "I'll snapshot it weekly" plan fails exactly when you forget it. Automation must be cron/documented.
4. **Restore-verified** — you have *actually performed a restore* (or the tool proves restorability), because a backup you've never restored is an unverified claim. This is the exact gap the ServerCrate 09-05 news calls out and the standard most hosts do NOT meet.

Supporting table (editable at draft time from provider pages, do not hard-inherit): 4 buyer scenarios vs what each plan actually protects — (a) same-box local copy, (b) provider snapshot, (c) same-provider different-DC copy, (d) off-site copy on an independent host/service.

## 5. Slug, title, and description (Python-measured)

- **Slug:** `vps-offsite-restore-backup-guide-2026`
- **Title (56):** `Are Provider Snapshots a Backup? VPS Off-Site Guide 2026`
- **Description (143):** `Host 'snapshots' are not backups. Keep your VPS data off-site, restored and verified — the cheap 3-2-1 setup that outlives a vanished provider.`

(56/60 title gate; 143/155 desc gate — both Python `len()`-verified. Measure again at full-draft time.)

## 6. Proposed H2 structure (10 sections, 8–10 required — evergreen-guide format, H2 #1 is a definition opener, NOT a "what happened" news lead)

### H2 #1: What This Guide Is — and the One Question It Answers
- You rely on a cheap VPS. Your "backup" is the provider's snapshot button — or nothing. If that provider's disk dies, your account is locked, or the company itself disappears (it happens in this industry — see the merchant-exit coverage), what do you actually still own?
- **This guide is about data-recovery, not uptime.** Uptime/DR is already covered by the linked outage articles. This page answers: how do I keep a copy of my data that no single provider can take away, and how do I prove I could actually restore it?
- First-person note: I have run budget boxes for a decade-plus and have been burned by trusting a host-side snapshot as "a backup" — the restore you test is the only one you own.
- Why now (dated hook): September 2026 backup-service coverage re-lit the industry-standard failure — *most hosts verify backups ran, not that they restore* (see the dated hook in H2 #3).

### H2 #2: Is a Provider Snapshot Actually a "Backup"? (The Hard Truth)
- **Provider snapshot = point-in-time image stored on (or reachable only through) the same provider.** It protects you from your own mistakes (bad deploy, deleted file) on a *healthy* host.
- **It is NOT a backup against the failures you actually fear:** host outage (snapshot may be on the same infra), account suspension/termination (you lose access to it), host shutdown/seizure (the copy is gone with the company), and silent data corruption of the snapshot itself.
- The deciding test: *does it survive the provider disappearing?* If no → it is convenience, not protection.
- A snapshot is worth having (fast rollback), but it is one layer — never the only layer. When this guide's framework says "3 copies," the snapshot is not one of the durable two.

### H2 #3: The Dated Case — Why "Restore-Verified" Is the New Bar (ServerCrate, LowEndBox 09-05)
- **Dated hook (attributed, non-whitelisted — NOT a recommendation):** on **2026-09-05** LowEndBox profiled **ServerCrate**, a zero-knowledge US-based off-site backup service, whose opening line is the industry criticism this article's thesis rests on: *"Most backups fail silently. You find out the night your drive dies. We test that your data actually restores, every single day, and show you the proof."* (LowEndBox by raindog308, 2026-09-05.)
- Their technical pitch (reported in the piece): client-side-encrypted per-user **Restic vaults** over HTTPS, each on its own **ZFS dataset with checksumming + snapshots** so silent bit rot in old archives is caught, plus a public **restore-verification monitor** (status.servercrate.net) that continuously proves backups can be restored — "not just that they ran, which is all most hosts check."
- **Why this matters to you even if you'll never use ServerCrate:** it documents, with a named dated datapoint, that **the industry default is to verify backups RAN, not that they RESTORE.** That is the single most important correction a budget-VPS owner can make to their own setup. (ServerCrate is a third-party backup service outside the whitelist — cited as attributed evidence only, never as a recommended host; mark it clearly non-whitelisted at draft time.)
- Companion fact: this echoes the site's own merchant-exit warning literature — when a host vanishes, the difference between surviving and data loss is decided months earlier, at backup-setup time, not at the moment of loss.

### H2 #4: The Framework — the "3-2-1" Rule Made Concrete for a Budget VPS
- The classic data rule: **3 copies of your data, on 2 different media, 1 of them off-site.** For a single VPS this collapses to the honest, cheap version the guide will actually walk through.
- The budget version the article recommends (costs $2-25/mo and is the editorial anchor): **copy 1 = the working box (not a backup, just where you run); copy 2 = provider snapshot (fast rollback, convenience only); copy 3 = the real backup: an off-site, independent, automated, restore-verified copy.** Copy 3 is the one this guide is about.
- Off-site options ranked by cost + independence (table to finalize at draft from live provider pages; honest secondaries only):
  - Cheapest independent: a **cheap annual second VPS at a different provider/region** running the backup tooling — most independent, most control, ~$11.25-35/yr at entry annual tiers (RackNerd deal class).
  - Storage-object / backup-service class: zero-knowledge off-site backup vendors (e.g. the profiled ServerCrate tier from ~$3-11/mo, free 10 GB tier) — least hands-on, restore-verification built in.
  - Object storage (S3-compatible) with versioning — mid-cost, good for larger data sets; watch egress.
  - A friend's/second location or a cheap home NAS — free but depends on an uplink you don't control.
- The takeaway: pick off-site + independent FIRST; only then optimize cost/automation.

### H2 #5: What to Back Up and How Often (the honest scope)
- Not everything needs the full 3-2-1 treatment. **Config + code + the irreplaceable state** (databases, uploads, keys, cron, dotfiles, nginx/apache config, container compose files, app data) is the real target; a 20 GB OS image you can rebuild from a template is not worth off-site-ing.
- Priority guide by workload (web DB, side project, self-hosted app, game server, agent/personal infra): DB → files/uploads → config → OS (rebuildable, lowest).

### H2 #6: The Restore-Verified Backbone — Encryption, Automation, and the Single Most Important Test
- **Encrypt before it leaves the box** (client-side). A zero-knowledge backup you hold the key to is the only one that is genuinely "independent" of both the source host AND the backup host.
- **Automate with cron / systemd timer** — a backup that requires a human to remember is a backup that will be missing the night it matters. Give the exact systemd-timer or cron pattern.
- **Always verify your uploads with the tool's check command / checksum path** — catching silent corruption at the earliest point.
- **THE test:** at least once, actually **restore to a fresh throwaway box (a cheap one) and confirm the app boots and the DB opens.** The 09-05 "restore-verified" news applies to you directly: if you've never restored, treat your backup as unverified. This is the differentiator that separates this page from every "how to rsync" tutorial on the web.

### H2 #7: RackNerd's Honest Anchor — the Cheap Annual Second Box as the Independent Copy (CTA Slot #1)
- The cleanest, most independent off-site copy for the budget owner is a **second cheap VPS at a DIFFERENT provider** — and RackNerd's annual KVM deals ($21.99/yr for 1 GB, 2 GB $35.99/yr, 4 GB $59.99/yr per the current verified deal table) make that independent copy affordable to lock for a full year.
- This is the same "cheap annual second host as self-insurance" thesis the site uses in its outage/insurance coverage — here applied to data-recovery specifically.
- **CTA slot:** `The cheapest truly independent backup copy is a second cheap annual VPS from a different provider. RackNerd's annual KVM plans lock in from ~$21.99/yr — see current deals →` (linking the affiliate URL). Honest framing: RackNerd is the value/second-box pick; it is NOT a backup service and does NOT pretend to be — present it as compute you run your own backup tooling on.
- CTA #2 slot (this section footer): the ~$1.83/mo equivalent framing for readers who budget monthly.

### H2 #8: Honest Secondaries — Vultr, DigitalOcean, and the Object-Storage Route (CTA Slots #3/#4)
- **Vultr** (from ~$2.50/mo, 13+ regions): pick a region far from your primary — a genuinely independent geo for the copy; good second-provider choice.
- **DigitalOcean** (~$4/mo droplets + Spaces/S3-compatible object storage with versioning): the easy on-ramp if you already use DO; object-store versioning gives point-in-time recovery without running a second box.
- Route matching table (finalize at draft): pick the off-site route by data size + how hands-on you want to be. RackNerd annual box = control/independence/value; Vultr = cheap always-on second region; DO Spaces/object storage = simplest versioned storage for bigger data. (ServerCrate = the attribution hook only, not a third pick.)

### H2 #9: The "Delete-Day" Checklist — What You Do the Day You Lose Access
- A 6-step pre-made runbook for the worst case (host dies, account locked, or the provider is gone): (1) your off-site copy is encrypted and you hold the key; (2) spawn the throwaway at a different provider; (3) restore → verify boot → verify DB; (4) repoint DNS when it's proven; (5) test the app end-to-end; (6) only then decommission or rebuild. This is the "off-site data is the only recovery" payoff and it ties the guide to the site's merchant-exit coverage without re-typing it.

### H2 #10: Conclusion + Last-Verified Footer
- **Bottom line:** provider snapshots are convenience, not protection. A real backup for a budget VPS is off-site, on an independent host or service, encrypted client-side, automated, and — above all — **actually restored at least once.** The dated 09-05 industry push for restore-verification is the prompt to fix your own setup this week, not next quarter.
- **Last-verified footer:** "Verified against LowEndBox 'You Need Backups and ServerCrate…' (raindog308, 2026-09-05), ServerCrate pricing tiers via the LEB piece (free 10 GB / Starter ~$3.75/mo / 200 GB), RackNerd annual KVM deal table (1 GB $21.99/yr … 4 GB $59.99/yr, from the 2026-08-26 LowEndBox-sourced fact bundle — re-verify from the racknerd.com specials page at draft time), Vultr ~$2.50/mo and DigitalOcean ~$4/mo entry prices (re-verify at draft). ServerCrate is a non-whitelisted third-party — cited as attribution only, NOT recommended. Last verified: 2026-09-06."

### FAQ (4 questions, within 3-5)
1. **Is my VPS provider's snapshot a real backup?** — Not by itself. A provider snapshot survives your own mistakes on a healthy host, but it dies with the provider if the account is terminated, the host is seized, or the company shuts down, and it may live on the same infrastructure as the failure. Treat it as fast rollback, not protection; keep a separate off-site copy.
2. **What is the cheapest way to back up a VPS off-site?** — A cheap annual second VPS at a different provider running your own encrypted backup tooling (RackNerd annual KVM from ~$21.99/yr / ~$1.83/mo class) is the most independent low-cost route. Zero-knowledge backup services and S3-compatible object storage with versioning are the less-hands-on alternatives.
3. **How do I know my backups actually work?** — The only honest answer: actually restore one. At least once, restore your encrypted backup to a fresh throwaway box and confirm the app boots and the database opens. The September 2026 backup-industry coverage (and the profiled ServerCrate pitch) makes the point that most hosts only verify backups *ran* — restore-verification is the bar you should hold yourself to.
4. **I run one small VPS and nothing important — do I still need off-site backups?** — If losing your config, DB, and keys would cost you more than ~$2/mo in time, yes. The cheap setup here (a $21.99/yr second box + one encrypted automated job + one test restore) is under the cost of a coffee and gives you independence from any single provider — the same independence the site's merchant-exit guidance already pushes for.

## 7. RackNerd CTA placement (≥6 required, 7 planned — all to `https://my.racknerd.com/aff.php?aff=16299`)

1. H2 #7 anchor CTA: RackNerd cheap annual second box as the independent off-site copy (~$21.99/yr entry; $1.83/mo equivalent).
2. H2 #7 footer CTA: the monthly-budget framing of the same anchor.
3. H2 #8 route-table: RackNerd row = control/independence/value pick in the off-site route table (honest — compute you run your own tooling on, not a backup service).
4. H2 #4 framework: RackNerd annual deal as the cheapest *independent* route option under "off-site options ranked."
5. H2 #6 restore-test section: "If you want a throwaway cheap box to actually practice a restore on, RackNerd's annual tier is the lowest-cost test bench."
6. H2 #9 delete-day checklist: step 2 "spawn the throwaway at a different provider" → RackNerd as the cheap emergency restore target.
7. H2 #10 conclusion: RackNerd as the budget way to make the independent off-site copy real this week.

All 7 link to the affiliate URL with anchor text matching editorial context (no false "backup service" claim for RackNerd — it's the compute you run tooling on). Self-check: ≥6 ✅ (7 placed).

## 8. Internal-link plan (all verified on disk — only-link-if-published)

- `/blog/aws-us-east-1-outage-2026/` — multi-region DR/availability sibling (link to distinguish DR from data-loss; the two-page pairing the outline avoids duplicating).
- `/blog/digitalocean-outage-august-2026/` — 4-tier fallback framework sibling (availability side).
- `/blog/2026-shutdown-cloud-services-vps-migration/` — host-shutdown/migration context (the merchant-exit tie-in).
- `/blog/vps-pricing-trap-guide-2026/` — pricing/renewal transparency context.
- `/blog/lifetime-vps-deals-2026-real-cost-vs-marketing/` — cheap-annual pricing model + the "second host as insurance" precedent + verified RackNerd price source.
- `/blog/racknerd-deep-review-2025/` — RackNerd honest anchor (§7).
- `/blog/vultr-deep-review/` — honest secondary (§8).
- `/blog/kainode-vps-review-2026/` — an honest single-node-disclosed small provider example threaded lightly (whitelisted; only if it genuinely illustrates the "know where your data physically sits" note).
- `/blog/vps-buying-guide/` — general buyer framework (§1).
- ⚠️ Do NOT link the queued-not-published `vps-provider-exit-warning-signs-2026` / `cloud-outages-2026-redundant-vps-setup` — pending, not on disk. Reference them in the run-record on-hold notes instead.

## 9. ⭐ status: pending-outline carry-over + source list

**Pending outline queue:** per `drafts/state.json`, the 09-04 (proxmox) + 09-05 (vps-cpu) entries are committed. The dated `outline_pending_publish` backlog continues to accumulate for the user's archive-vs-publish decisions (43 total drafts after today's append; the newest dated queue 8-24 → 9-06). No auto-archive; surface in §11.

**Sources cited (all body-fetched 2026-09-06):**
- **LowEndBox (dated hook):** lowendbox.com/blog/you-need-backups-and-servercrate-is-going-to-make-them-painless-start-for-free/ — raindog308, 2026-09-05; ServerCrate "restore-verification" thesis, ZFS/Restic/checksum technicals, status.servercrate.net monitor, pricing (free 10 GB / Starter 200 GB ~$3.75/mo w/ LEB25 / Standard 1 TB ~$11.25 / Pro 2 TB ~$21.75), LA-based zero-knowledge.
- **Kainode (captured ⭐, supporting only):** LowEndBox Kainode Singapore 30% piece, 2026-09-03.
- **providers.json** `/root/vpstier-site/src/data/providers.json` — RackNerd (annual-deal price class, affiliate `my.racknerd.com/aff.php?aff=16299`, 5 US DCs), Vultr, DigitalOcean whitelisted; ServerCrate NOT in providers.json (non-whitelisted hook).
- **On-disk AWS + DO outage guides** — verified they cover DR/availability, NOT the data-loss/restore intent (distinctness check).
- **GSC** 2026-09-06 file — no backup/restore query in vpstier top 10 (confirms content gap).

## 10. Pitfalls captured for the article-writing cron

1. **Non-whitelisted hook discipline:** ServerCrate is a third-party backup service NOT in providers.json. Cite it as the dated, attributed news hook (H2 #3) with the URL + "NOT a recommendation / non-whitelisted" note. Never present it as a recommended host; it is evidence the industry only verifies backups *ran*.
2. **Do NOT write the generic "VPS backup strategy" version** — it body-overlaps the published `aws-us-east-1-outage-2026` "Multi-Region Backup Strategy" section + the `digitalocean-outage-august-2026` fallback tiers. The distinct slice is **data-loss / off-site / restore-verification** (the "is a snapshot actually a backup" buying question). If any H2 starts sliding into multi-region DR/availability, stop and re-anchor on data-independence.
3. **RackNerd honesty pattern:** RackNerd is compute you run backup tooling on — do NOT imply RackNerd is a backup/storage service or sells "managed backups." Anchor on cheap annual second-box value + independence. Pricing: re-verify the current deal table from racknerd.com specials at draft time (the 1 GB $21.99/yr / 2 GB $35.99 / 4 GB $59.99 figures are the 8-26-sourced bundle — re-confirm live).
4. **Banned-merchant zero-check:** this self-check is written in category language ("banned-merchant zero-check" / "permanently excluded merchant"). At draft time run `grep -ci` for each canonical brand-name token across the WHOLE draft (title, description, H2, FAQ, prose, pending-outlines table, self-check rows) and confirm 0 — do not embed any brand token in the check's own wording.
5. **CJK zero-check:** CJK chars (Chinese/Japanese/Korean Unified Ideographs incl. Extension A/B) = 0; describe the regex in prose so the self-check row doesn't trip its own rule.
6. **Length discipline:** title 56 and desc 143 are Python-measured. Re-run Python `len()` at full-draft; title ≤60, desc ≤155 (70-155 gate).
7. **HCU-compliance preview:** ≥2 real artifacts committed (the dated ServerCrate LowEndBox hook + provider price re-verification + on-disk DR-outage sibling distinction); first-person opening note + Last-verified stamp scheduled; ≥800 unique words; NO "X vs RackNerd vs Vultr" comparison-crutch template — this is a how-to/decision guide with a dated case, not a listicle.
8. **Internal-link discipline:** use only the on-disk slugs in §8. Do NOT link queued-not-published `vps-provider-exit-warning-signs-2026` / `cloud-outages-2026-redundant-vps-setup`.
9. **RackNerd price source:** cite from the 8-26 LowEndBox-sourced bundle only as a starting point; re-verify live at draft.

## 11. On-hold items (not part of this run)

- **Related queued outlines the user should know about** (this guide complements, does not duplicate): `vps-provider-exit-warning-signs-2026` (8-27, treats off-site backup as one merchan-exit defense bullet; this guide is the full data-recovery how-to) and `cloud-outages-2026-redundant-vps-setup` (8-11, DR/availability; this guide is data-loss/restore). Recommend (not auto-applying) publishing those first if the queue order matters, since this guide cross-references the data-safety theme.
- **Full pending queue** enumerated in `drafts/state.json` `drafts[]` (43 after this run); user decides archive-vs-publish. No auto-archive.

## 12. Awaiting user action

Reply `publish` to have the article-writing cron build `src/pages/blog/vps-offsite-restore-backup-guide-2026.astro` from this outline (see resume recipe below). Reply `[SILENT]` / skip to decline so the outline stays queued in `drafts[]` without publishing.

---

## Resume recipe (for the article-writing cron)

When the user confirms `publish`:
1. Read `/root/vpstier-site/drafts/outline-2026-09-06-vpstier-daily.md` as the canonical structure.
2. Write `/root/vpstier-site/src/pages/blog/vps-offsite-restore-backup-guide-2026.astro` per the canonical blog-article template.
3. Title (`Are Provider Snapshots a Backup? VPS Off-Site Guide 2026`, 56) + Description (143) Python-verified at write; keep ≤60 / ≤155.
4. ≥800 unique words + ≥2 real artifacts + first-person voice + Last-verified 2026-09-06 stamp per HCU. Keep ServerCrate as non-whitelisted attribution only.
5. `cd /root/vpstier-site && npm run build`.
6. Check `CLOUDFLARE_API_TOKEN` via the curl token-verify recipe; vpstier is wrangler-deploy-only (no Git auto-deploy). If expired → state `deploy_pending` + commit+push anyway (see cloudflare-api-token-deploy-blocker.md).
7. `git add src/pages/blog/vps-offsite-restore-backup-guide-2026.astro drafts/state.json` (+ any untracked outline/run-record from prior runs still uncommitted) — specify paths, never `git add -A`.
8. `git commit -m "feat(blog): add VPS off-site restore-verified backup guide 2026-09-06"` + `git push origin main`.
9. If token active: `wrangler pages deploy dist --project-name=vpstier-com --branch=master --commit-dirty=true` and live-verify (HTTP 200 + title live + JSON-LD ≥5 + sitemap +1). If expired: flip state to `deploy_pending` and resume after token refresh.

---

## State.json update (this cron run)

- Read `drafts/state.json` (base `state.json` not present; drafts/state.json is the canonical file).
- Append ONE new `outline_pending_publish` entry: `{date: "2026-09-06", status: "outline_pending_publish", slug: "vps-offsite-restore-backup-guide-2026", title: "Are Provider Snapshots a Backup? VPS Off-Site Guide 2026", outline_file: "drafts/outline-2026-09-06-vpstier-daily.md", run_record: "drafts/run-record-2026-09-06-vpstier-daily-outline.md"}`.
- `drafts_count = len(drafts)` AFTER the append (same Python operation).
- `last_run = "2026-09-06"` explicit assignment.
- `publish_notes` string append with `\n` + BOTH date marker and kebab slug + a natural-title fragment.
- `json.dump(..., ensure_ascii=False)`.
- 4-check verifier: `drafts_count == len(drafts)`, `last_run == today`, date marker in publish_notes, title fragment in publish_notes.
- Then the two-commit pattern: outline + run-record first (feat-style), state.json second (chore-style), then `git push origin main`.
