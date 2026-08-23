# VPSTier Daily Outline Run Record — 2026-08-23 (Sunday)

## Run summary

- **Cron:** vpstier-daily-outline (5fd2a36f2dc4)
- **Outline file:** `drafts/outline-2026-08-23-vpstier-daily.md`
- **Slug:** `vps-vs-vds-2026-which-to-choose`
- **Title:** `VPS vs VDS in 2026: Which Virtual Server Tier Do You Need?` (58 chars, 30–60 ✅)
- **Description:** 145 chars (70–155 ✅)
- **Format:** multi-provider comparison / buyer-guide (10 H2 / 5 FAQ / 7 RackNerd CTAs / 10 `/blog/` + 6 `/vps/` verified internal links)
- **Providers featured:** RackNerd (budget anchor), Servarica, RamNode, Hivelocity (dated hook), RoseHosting, MochaHost, Kamatera, CloudCone
- **Banned self-check:** PASSED — 0 excluded-merchant mentions anywhere in the draft (incl. rationale + self-check)
- **CJK / /zh/ check:** 0 new CJK; 2 `/zh/` are the legitimate self-documentation audit lines (LANG policy + "route tree deleted"), matching the 8-09/8-10/8-16 precedent
- **state.json update:** 1 new `outline_pending_publish` entry appended, `publish_notes` string-append, `drafts_count` incremented
- **Commits:** outline + run-record first (article-preview commit), then state.json; pushed `main`

## Decision log

1. **Briefing (3ea88f8bb2d0, 08-23) SUCCEEDED, both vpstier ⭐ = the excluded merchant** (a 187–250%
   price-increase post-mortem + an LLM-inference experiment). → Tier-1 banned-pivot (recurring default;
   8-16/8-19/8-20 precedent). No re-justification needed; the rationale explains WHICH substitute.
2. **GSC (5570fe2cffa6, 08-23) query `turnkey vps` (rank 58) verified and DISMISSED as a review:** probed
   `www.turnkeyinternet.net` with redirect-following — final URL = `hivelocity.net`, HTTP 200. TurnKey
   Internet is a **dead/absorbed brand**. Authoring `turnkey-vps-review` would describe a company that no
   longer exists standalone. Instead, this is a **site-hygiene finding**: the legacy `turnkey-internet` entry
   in `providers.json` + its `/vps/turnkey-internet` profile should be retired in a cleanup pass (flagged in
   §8; NOT acted on this run). The query's intent ("turnkey = ready-to-go VPS") is partially served by the
   VPS-tier explainer today.
3. **Fresh dated hook = Hivelocity VPS/VDS refresh (PR Newswire, 08-20-2026):** heart of the pick. Hivelocity
   is a **whitelisted** provider (rating 4.3, EPYC/Xeon, NVMe VPS + dedicated-core VDS, 40+ DCs / 6
   continents) with **zero on-disk coverage** (no blog review, no body mentions). Body-verified from the live
   `/vps/` page (200, ~200 KB): own framing "VDS gives fully dedicated hardware resources... VPS typically
   shares physical hardware." Unlike a non-whitelisted low-end merchant hook, this one is recommendable.
4. **Content-gap verification (this run):**
   - No dedicated "VPS vs VDS" / "VDS hosting" / "VPS or VDS" article exists — no slug targets vds, no `<h2>`
     in ANY article reads "VPS vs VDS".
   - `VDS` appears only as an aside in 7 single-provider reviews (kainode 34×, hostnamaste 21×, servarica
     17×, ramnode 12×, cherryservers 8× ...) — never as a *selection* page.
   - `reseller` tier likewise only in passing.
   → genuine evergreen buying-intent gap, orthogonal to the pending queue (all reviews + data-center/outage
   news-analysis layers).
5. **OVH 87% RAMageddon price hike REJECTED as the pick:** the existing published `vps-price-hikes-2026-
   ramageddon` article already covers it heavily (H2 #3 "The Freshest Proof: OVHcloud's 87% Price-Wave
   Warning (Aug 2026)"; 7 OVH / 5 "87%" / 16 RAMageddon mentions). Body-overlap rule → near-duplicate, reject.
6. **Data-center politicalization cluster (Economist 08-19, Tom's Hardware Amazon CO2 08-21, Axios politics
   08-21) NOT re-picked** — already queued (8-04/8-05/07-15 outlines).
7. **Format decision:** multi-provider comparison (Hivelocity hook + VDS tier touches 8+ whitelisted
   providers). Also breaks the single-provider-review run — 5 of the last 6 published were reviews
   (hostnamaste 8-16, tmdhosting 8-18, cloudblast 8-19, milesweb 8-20, ultahost 8-21).

## Verification notes

- **Hivelocity hook body-verified** from live `/vps/`: title "VPS | VDS Hosting | Linux & Windows Servers |
  24/7 Support"; 76 VDS mentions; NVMe (3), vCPU (6), DDR (2); DC names (Tampa/LA/NY/Chicago/Miami/Dallas/
  Atlanta/Phoenix/Ashburn) present in the page. `providers.json` confirms: cpu EPYC/Xeon (shared VPS +
  dedicated VDS cores), NVMe SSD 40GB–80GB+ VPS, 40+ DCs, 99.99% SLA, API + Terraform.
- **VDS-tier whitelisted providers** pulled from `providers.json` (cpu field): RamNode (dedicated cores VDS
  from ~$50/mo), Servarica (NVMe VDS from $8+/mo + V3 KVM slices on EPYC Milan), RoseHosting (dedicated Xeon
  cores, PCIe 4.0 NVMe), MochaHost (dedicated EPYC cores, NVMe), Kamatera (dedicated-thread options A/B/D/T),
  CloudCone (shared/dedicated KVM tiers), HostHatch (disclosed dedicated allocations), Hivelocity (dedicated
  VDS cores). Every row must be re-verified from the live page at draft time.
- **RackNerd cpu field = server-class (EPYC/Xeon) only, NO VDS/dedicated-core tier** — so RackNerd is
  anchored honestly as the shared-budget/2nd-box pick, NOT falsely as a VDS provider (the honest-when-your-
  advertiser-lacks-the-feature pattern).
- **Internal links all verified on disk** (see outline §6). `mochahost`/`cloudcone`/`rosehosting` have no
  blog-review pages, so they are linked via their `/vps/` profiles (all exist).

## Hygiene / on-hold items for the user

- **`turnkey-internet` is a dead/absorbed brand** (domain redirects to Hivelocity). Recommend retiring the
  `providers.json` entry + `/vps/turnkey-internet` profile in a cleanup pass. Also mirrors the apirank
  dead-end-probe pattern (OctoAI→NVIDIA, Paperspace→DigitalOcean absorbed).
- **Pending publish queue is large (20+ `outline_pending_publish`).** Recommend a future cleanup to archive
  superseded/aging outlines (07-15 ny-data-center-moratorium is scope-superseded by 8-04/8-05 politicalization).
- **Uncommitted backlog:** several prior outline/run-record drafts (8-01…8-13) + `src/pages/vps/iozoom.astro`
  remain untracked from prior runs. This run staged ONLY its own files (`git add <specific>`), per the
  concurrent-cron rule — it did NOT sweep the backlog. Recommend a separate cleanup commit.
- **Do NOT deploy from this outline** — this is the daily-outline cron (source-side only). It does not build,
  deploy, or live-verify. The article is authored only after the user replies `publish`.
