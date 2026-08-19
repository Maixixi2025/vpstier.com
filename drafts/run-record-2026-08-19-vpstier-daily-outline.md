# VPSTier Daily-Outline Run Record — 2026-08-19 (Tuesday)

## Outcome

- **New outline:** `drafts/outline-2026-08-19-vpstier-daily.md` → slug `gpu-ram-price-wave-2026-ai-vps-buyers`
- **Deliverable:** news-analysis + AI-VPS buyer-guide (10 H2 / 5 FAQ / 7 RackNerd CTA placements), English only (LANG policy). The **second-wave companion** to the existing 8-12 `vps-price-hikes-2026-ramageddon` article, adding the GPU side (RTX 50 +36-39%, Intel Arc Pro B70 +48%, monitor H2-2026 hike), the storage side (HDD/SSD +125% in Europe), the AI-workload cast, and the 2027-2030 horizon.
- **state.json:** 1 new `outline_pending_publish` entry appended (drafts 72 → 73); `last_run` = 2026-08-19; `publish_notes` schema-drift-safe appended. `last_publish` untouched (publish-side field).

## Topic decision

- **Briefing (`3ea88f8bb2d0`) SUCCEEDED today** (file `2026-08-19_08-04-19.md`, 10,163b): vpstier ⭐ picks = (1) the permanently excluded merchant's 187-250% price-increase re-test, (2) Cloudblast €4.03/mo 4GB unlimited-bandwidth (LEB, 2026-08-12), (3) Cursor self-hosted GitHub-rival (TechCrunch URL 404'd; no same-day named-outlet RSS hit).
- **Pick #1 → REJECTED under the permanent merchant policy** (the merchant requires a passport + manual review for affiliate enrollment and is fully delisted site-wide; `grep -c` for the excluded brand across `src/` = 0). Per the standing rule, even seeing the signal in the briefing is not actionable. The outline pivots to the **structural industry version** of the story (the briefing itself flagged the 187-250% range, which is exactly the Aug 17 Tom's Hardware second wave scope). Same pivot pattern the 8-12 `vps-price-hikes-2026-ramageddon` outline used (it pivoted from banned providers to OVHcloud's 87% headline).
- **Pick #2 (Cloudblast)** is a LEB-style new-provider entry — non-news and lower priority than the structural story. Available as a backup if the user prefers a Cloudblast review.
- **Pick #3 (Cursor self-hosted)** failed the freshness + multi-outlet bar (TechCrunch URL 404'd; Google News RSS shows no same-day named-outlet coverage; last Cursor mentions are 03-25 + 04-29, all Cursor-blog posts). Rejected.
- **Substituted pick — Aug 17 Tom's Hardware second wave.** Tom's Hardware published three same-day stories showing the 2026 component-cost wave has now **escalated from DRAM-only to a full RAM + GPU + storage crisis**, with an AI-workload cast:
  1. **"Memory prices climb 500% in 12 months, up to 10x the lowest ever tracked prices — 128GB of DDR5 now $3,399"** (Tom's Hardware, 2026-08-17 13:52 UTC, by Zak Killian) — **body fetched this session** (35 paragraphs; full source-of-truth for the article).
  2. **"GeForce RTX 50-series GPU prices spike as much as 39% as Blackwell price hikes hit the US"** (Tom's Hardware, 2026-08-17; headline-attributed).
  3. **"Intel's Arc Pro B70 workstation GPU is now up to 48% more expensive than it was just a month ago"** (Tom's Hardware 2026-08-17 11:40 UTC + VideoCardz 2026-08-16 corroboration; headline-attributed).
  4. **"PC Partner warns of rising GPU prices and budget card shortages"** (Tom's Hardware 2026-08-17 11:00 UTC; headline-attributed).
  5. **"Entry-Level GPUs and Monitors Face Price Hikes in H2 2026"** (TechPowerUp 2026-08-17 21:44 UTC; headline-attributed).
  6. **"Memory Prices Break a Record With Nearly 500% Surge in the Last 12 Months"** (TechPowerUp 2026-08-18 16:16 UTC; second-day corroboration).
- **Body-verified facts (Tom's Hardware 2026-08-17 body):**
  - 128GB DDR5 = **10x more expensive** than the lowest ever tracked price.
  - **$3,399** sticker for a 128GB DDR5 kit.
  - 64GB (2x32GB) DDR5-5600: **$200 → $1,100** in 12 months = **5x**.
  - DDR4 kits **+120-180%** YoY (the older-platform scramble).
  - **Europe** (ComputerBase): **average RAM +345%** since Sept 2025; **HDD/SSD +125%** in same period.
  - **2027 DRAM supply already locked in** by hyperscalers with advance deposits; "mainstream DRAM chips worth over half as much per kilogram as solid gold."
  - **SK Hynix CEO Kwak Noh-jung:** "2027 will be the worst year for memory supply"; demand expected to outstrip supply **into 2030**.
  - **ADATA Chairman Simon Chen:** DRAM crisis could last **another 10 years**; dismissed "AI bubble" thesis.
- **Content-gap evidence (verified this run):**
  - `vps-price-hikes-2026-ramageddon` (8-12, the structural wave article): GPU=0, Blackwell=0, GDDR=0, VRAM=0, RTX 50=0, AI workload=0, LLM inference=0 — DRAM-only; explicitly does not cover the GPU side.
  - `cheap-vps-local-llm-inference-2026` (8-02): GPU=5, inference=27 — but it's a **buyer-guide**, not a price-pressure story (it predates the wave).
  - **Conclusion: zero existing vpstier article covers the GPU side of the 2026 component-cost wave OR the AI-workload angle of the wave.** Genuine second-wave content gap.
- **Differentiation — second-wave companion vs duplicate:**
  - vs `vps-price-hikes-2026-ramageddon` (8-12): that article is **DRAM-only**. This article adds (a) GPU, (b) storage, (c) AI-workload cast, (d) 2027-2030 horizon, (e) buyer playbook. Different deliverable; cross-link, don't rewrite.
  - vs `cheap-vps-local-llm-inference-2026` (8-02): that article is a buyer-guide. This article is the **price-pressure analysis** that tells AI-inference buyers what the cost wave means for their next 12 months. Different intent.
- **GSC (2026-08-19 07:00, latest file):** vpstier has only **one** query in the last 7 days: `zappiehost` (rank 56) — brand-nav signal; `zappiehost-vps-review-2026.astro` already published → not re-picked.
- **Tier-0:** excluded-merchant vpstier ⭐ rejected; Cloudblast lower-priority; Cursor fresh failed the multi-outlet bar. No GSC re-pick. **Substituted with a fresh, dated, multi-outlet second-wave story with a confirmed content gap.** No excluded merchant appears anywhere in the outline.

## Validation (script-measured)

- Title `GPU and RAM Prices 2026: VPS Cost Wave Hits AI Workloads` = **56 chars** (30–60 ✅)
- Description = **124 chars** (70–155 ✅)
- H2 sections: **10**; FAQ: **5**; RackNerd CTA placements: **7 explicit + inline** (≥6 ✅)
- Excluded-merchant name in whole draft (case-insensitive `grep -c`): **0** ✅ (replaced with brand-free policy explanation in §1)
- CJK: **0** ✅; `/zh/` refs: **2** (audit-only mentions of the LANG policy) ✅
- Internal `/blog/` links: all on disk OR explicitly flagged "when published" (the 3 queued outage outlines: 8-11 cloud-outages, 8-16 namecheap, 8-17 cloud-outage-insurance) ✅
- Whitelisted VPS providers (RackNerd, Vultr, DigitalOcean, Linode, Kainode, LightNode, HostNamaste, HostArmada): all in `providers.json` ✅
- Body-verified source-of-truth: Tom's Hardware 2026-08-17 RAM-500% article (35 paragraphs; fetched this session via urllib). 6 additional outlets headline-attributed.

## Git discipline (two-commit, per ilang-content; branch `main` confirmed)

- Commit 1: `drafts/outline-2026-08-19-vpstier-daily.md` + `drafts/run-record-2026-08-19-vpstier-daily-outline.md`
- Commit 2: `drafts/state.json` (outline entry + last_run + publish_notes + published_count self-heal)
- Did **NOT** `git add -A` the accumulated untracked outline/run-record backlog (flagged below). Committed the specific files this run created only.

## On-hold / open items

1. **Uncommitted backlog in `drafts/`** (pre-existing, NOT from this run): outline-8-01/8-03/8-04/8-05/8-07/8-12/8-13/8-16/8-17 + run-record-8-03/8-04/8-05/8-07/8-11/8-12/8-14/8-16/8-17 .md files are untracked. A working-tree reset would destroy them (converter-epub 8-07 class of incident). Recommend a separate cleanup commit (user decision).
2. **Large pending-outline queue (6+ drafts now, including today's):** `namecheap-vps-review-2026`, `cloud-outages-2026-redundant-vps-setup`, `namecheap-outage-dns-email-vps-resilience-2026`, `best-vps-for-ai-agents-2026`, `cloud-outage-insurance-vps-risk-2026`, plus today's `gpu-ram-price-wave-2026-ai-vps-buyers`. User is the publish-gate; today's run appends one entry. **Recommend publishing `namecheap-vps-review-2026` (8-01) or `best-vps-for-ai-agents-2026` (8-14) first** — both are mature outlines with multi-week idle time and would unblock the queue. If the user wants to publish **today's outline** (component-cost second wave) it must be flagged that it cross-links the 8-12 RAMageddon article (already live) and the 8-02 AI VPS guide (already live); the cross-links resolve cleanly without waiting for the outage-queue outlines.
3. **Provider GPU offerings and prices (H2 #6/#8) must be reverified from live provider pages at full-draft time** — Kainode GPU plans, LightNode GPU plans, RackNerd annual-lock price point. Do not inherit stale tables.
4. **`excluded merchant` exclusion policy applied consistently** — the 2026-08-19 vpstier ⭐ #1 was rejected under the permanent merchant policy; the outline pivots to the structural industry version of the story (same pattern as the 8-12 RAMageddon outline's OVHcloud pivot). No excluded merchant in any content text.

## Notes for the publish conversation

- The **outline is ready for review** at `drafts/outline-2026-08-19-vpstier-daily.md`. The deliverable is a **second-wave companion** to the existing 8-12 RAMageddon article, not a rewrite.
- **Alternates if the user prefers a different angle:**
  - **Cloudblast €4.03/mo review** (briefing ⭐ #2, LEB 2026-08-12) — straightforward new-provider review.
  - **Cursor self-hosted Git** (briefing ⭐ #3) — would need a fresh news hook (the TechCrunch URL 404'd; needs a re-pick on a verified outlet).
- **Pending-queue publication order recommendation** (user's call): publish `namecheap-vps-review-2026` (8-01) and `best-vps-for-ai-agents-2026` (8-14) next to clear the longest-idle outlines; then `cloud-outages-2026-redundant-vps-setup` → `namecheap-outage-dns-email-vps-resilience-2026` → `cloud-outage-insurance-vps-risk-2026` (the outage theme trio; cross-link each other) → `gpu-ram-price-wave-2026-ai-vps-buyers` (today's outline; cross-links the live RAMageddon + AI-VPS-guide articles).
