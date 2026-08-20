# VPSTier Daily Outline Preview — 2026-08-20 (Thursday)

## 1. Topic rationale and demand source

- **Priority route:** today's 08:24 daily briefing cron (`3ea88f8bb2d0`) **SUCCEEDED** (10 items, sources
  verified). This is the **briefing-succeeds-but-vpstier-stars-are-banned** trigger (3rd occurrence; 8-16 and
  8-19 precedents). Both vpstier ⭐ picks reference the **excluded merchant** and are therefore ineligible
  under the permanent merchant policy:
  1. ⭐ "the [excluded] merchant's LLM-inference experiment recap" — references the excluded merchant →
     rejected.
  2. "[Excluded merchant] price increase re-test (187–250%)" — references the excluded merchant → rejected.
  No banned merchant appears anywhere in this outline (see §7 self-check).
- **Tier-0 GSC (cron `5570fe2cffa6`, 2026-08-20 07:00 — latest file):** vpstier's only query is
  `zappiehost` (rank 56, 1 impression) — a **whitelisted brand-name navigation signal** with an
  already-published page on disk → **NOT re-picked** (the 8-16 brand-query dismissal rule). No new
  actionable content-gap signal from GSC today.
- **The fresh, dated, multi-outlet news hook (verified this session via HN Algolia + HN item body + Google
  News RSS cluster):** on **Mon, Aug 18, 2026**, a **peer-reviewed field study** — *"Field measurements of
  neighborhood-scale air temperature impacts of data centers"* (ASME *Journal of Sustainable Buildings*,
  Vol. 7, Issue 2; a.k.a. "Data-Center Waste Heat as an Emerging Urban [heat source]") — was surfaced on
  Hacker News and hit **310 points / 486 comments** (submitter cwwc). The study measured actual air
  temperatures around a Phoenix, Arizona data-center campus and found real, wind-aligned downwind warming in
  the adjacent residential neighborhood.
- **Body-verified facts (extracted from the HN item's top-comment thread, quoting the study directly):**
  - **Location:** Phoenix, AZ. The studied campus is **NTT PH1** (~**169 MW** load), sited **directly across
    the street from a residential neighborhood** — called out in-thread as "a failure of urban planning" /
    poor industrial zoning (industrial zones, no residential buffer).
  - **Measured deltas:** mean air temp on the **upwind** side ≈ **42.7 °C**, rising to ≈ **43.5 °C** in the
    downwind residential area near the campus's eastern boundary → an **average ΔT of ≈ 0.8 °C**, with the
    warming signal detectable **as far as ~500 m downwind**.
  - **Max warming:** one commenter quoted "**downwind air temperature warming as high as 2.2 °C**" and
    "**average downwind air temperatures 0.7–0.9 °C warmer** than corresponding upwind areas"; headline
    coverage rounds this to "**up to 4 °F** in Phoenix neighborhoods."
  - **Why so hot:** a peer in-thread quoted the paper — "air-cooled **condenser arrays discharge air 8–14 °C
    above ambient**, often **exceeding 50 °C during Phoenix summers**."
  - **Attribution method:** the paper says warming is attributable to the DC because "the temperature signal
    [aligns] with the prevailing wind direction across multiple sites, dates, and meteorological conditions."
  - **Honest counterpoint (keep in final article for credibility):** several HN commenters (notably jeffbee)
    rightly challenged causal rigor — the adjacent parking lots / asphalt heat-island and lack of a proper
    control make exact attribution harder than the headline suggests. The article should present the
    *measured* numbers as peer-reviewed measurements and the *causal* jump with appropriate hedging.
- **Multi-outlet verification (Google News RSS, 7-day window — headline-attributed, some bodies bot-403 but
  clustered):** the story is a real ASU study with wide trade+local spread:
  - **Adafruit** (Tue, 2026-08-18) — "Data centers raise nearby temperatures by up to 4 degrees in Phoenix"
    (also surfaced 2026-05-18 on Tech Xplore / 2026-01-27 CNBC re-share of the earlier ASU finding)
  - **ASU News** (Mon, 2026-05-18) — the originating ASU announcement
  - **AZ Family** (Tue, 2026-05-19) — "Data centers raise temperatures up to 4 degrees in nearby
    neighborhoods: study"
  - **azcentral / The Arizona Republic** (Thu, 2026-06-04) — "ASU study finds data centers warming nearby
    neighborhoods"
  - **Facilities Dive** (2026-05-27), **Data Center Knowledge** (2026-08-11, "Turning down the heat from data
    centers"), **grist.org** ("Data Centers: The Heat Behind the Cloud", Pulitzer Center) — broader
    industry/environment corroboration
  - Note: the *fresh hook* is the 8-18 HN re-surfacing (310 pts) of this peer-reviewed paper; the underlying
    ASU study is May–June 2026. For the article the dated, attributed anchor is the ASME paper + 8-18 HN
    surge, with ASU/azcentral/AZ Family as corroboration.
- **Content-gap evidence (verified this run):** grep over `src/pages/blog/` + `src/pages/vps/` for `waste
  heat` / `heat island` / `heat-island` / `urban heat` / `siting` / `power density` / `data center heat` =
  **0 matches** across every term (the only `cooling` hits are inside unrelated vendor reviews). The site has
  **no article on data-center siting / neighborhood heat / environmental footprint** as a VPS-buyer
  consideration.
- **Differentiation from the pending data-center-politicalization queue (critical):** the queued outlines
  `data-center-politicalization-2026-vps-buyers` (8-04), `us-data-center-politics-2026-vps-impact` (8-05),
  and `ny-data-center-moratorium-2026-vps-buyers` (07-15) all cover the **REGULATORY / political** layer —
  state moratoriums, tax breaks, supply-chain bans, zoning politics. I verified the 8-04 + 8-05 outline
  bodies contain **0** mentions of heat/temperature/waste/cooling/siting. Today's angle is the **physical /
  environmental / site-selection** layer — *where a data center physically sits relative to homes, and what
  that means for a VPS buyer choosing a provider*. This is a **new strategy layer, not a duplicate**. It can
  even be framed as a natural companion to the politicalization theme (the political backlash is partly
  *fueled* by these physical neighborhood impacts).
- **Format:** single-deliverable **news-analysis + VPS buyer-guide** — multi-provider/multi-DC shaped
  (touches 5+ whitelisted providers' DC footprints as "is my provider's DC sitting in a neighborhood?"),
  so per the decision matrix a comparison/buyer-guide is the right shape. Orthogonal to the pending queue
  (a new siting/environmental layer; does not compound it).

## 2. Slug / Title / Description (measured with Python len())

- **Slug:** `data-center-heat-siting-vps-selection-2026`
- **Title:** `Data Center Heat and Siting: What VPS Buyers Should Check` — **57 chars** (target 30–60 ✅)
- **Description:** `A Phoenix study measured data-center waste heat raising nearby temps up to 4°F. For VPS
  buyers, here's why DC siting and location now matter.` — **141 chars** (target 70–155 ✅)
- **Search intent:** News-analysis + how-to-choose (informational → buyer-guide)
- **Language:** English only (LANG policy; no CJK, no /zh/)

## 3. Proposed H2 structure (10 H2)

1. **What Just Happened: A Peer-Reviewed Study Measured Data-Center Heat in Homes (Aug 2026)**
   - Lead with the dated, attributed hook: ASME *J. Sustainable Buildings* field study re-surfaced on HN
     2026-08-18 (310 pts / 486 comments); Phoenix, AZ, NTT PH1 ~169 MW campus across the street from a
     residential neighborhood; measured upwind 42.7 °C → downwind 43.5 °C, up to 2.2 °C (≈4 °F) localized
     warming, signal to ~500 m downwind. One-line thesis: the *physical* footprint of a data center now has
     hard numbers — and it is a real VPS-buyer consideration.
2. **The Study, in Plain English: What 0.8–2.2 °C Downwind Warming Actually Means**
   - Translate the numbers: average ΔT ≈ 0.8 °C, localized max ≈ 2.2 °C within ~500 m; condenser discharge
     8–14 °C above ambient (often >50 °C in Phoenix summers); attribution = wind-aligned signal. Honest
     caveat: parking-lot heat-island and control-design critiques from HN commenters mean the measured deltas
     are solid but the *causal* story should be framed carefully.
3. **Why "Where the Data Center Sits" Is Now a VPS-Buyer Question**
   - The bridge: hyperscale/gpu buildouts (higher per-rack power → more rejected heat, cf. A100 ~400 W →
     B300 ~1,400 W per chip) are colliding with residential zoning; community pushback, moratoriums, and
     siting rules follow (cross-ref the site's data-center-politicalization theme as REGULATORY companion).
     For a VPS buyer, the provider's data-center locations are now part of the due-diligence list.
4. **What a Budget VPS Buyer Can Actually Do With This (Realistic Guidance)**
   - Keep it honest: you rent compute, you don't control the DC's neighborhood. What you CAN do: (a) know
     where your provider's DCs physically sit (US DC list per provider), (b) prefer providers with
     dispersed/buffer-zoned enterprise-grade DCs over one-off single buildings in residential zones, (c)
     understand that siting pressure can *delay or stop* new buildouts near homes → capacity/price
     implications for that region. Frame siting as one more "where is my VM really running" question.
5. **Provider-by-Location: Whitelisted DC Footprints (re-verify at draft time)**
   - The editorial-anchor table. Rows for the 5 whitelisted providers used consistently in site
     news-analysis (RackNerd / Vultr / DigitalOcean / HostArmada / Hostinger). Columns: US DC cities,
     single-building-vs-multi-location, known residential-adjacent exposure, and a "siting-risk" note.
     **⚠️ Do NOT inherit DC lists from any prior outline — re-verify each provider's live `/datacenters/`
     page or JSON-LD at full-draft time** (RackNerd's own site 403s to urllib; pull the RackNerd US DC list
     from the live affiliate/landing page or a prior site article's verified footprint and re-confirm).
6. **Why Dispersed US Data Centers Beat a Single Overheated Building**
   - For budget buyers, DC *dispersion* matters: (a) thermal resilience — a hot Phoenix summer is a real
     risk to a single cooling-dependent site (ties to the site's outage-redundancy theme), (b) siting
     stability — multi-location providers absorb community pushback regionally, (c) latency choice. RackNerd
     US footprint is the affordable dispersed anchor (LA / Seattle / Dallas / NY / Chicago / San Jose —
     verify at draft); Vultr/DO offer global dispersion.
7. **Phoenix-Summer Reality Check: Heat + Cooling + the "4°F in My Backyard" Effect**
   - Direct address: Phoenix is a worst-case illustration (169 MW across the street from homes) but the
     *pattern* generalizes wherever new gpu/hyperscale DCs are sited near residential zones. Practical
     checklist: (a) does the provider state DC locations? (transparency), (b) are its buildings in
     industrial parks with buffer or in mixed/commercial zones?, (c) any local moratorium/siting news about
     that city? (grep + cross-ref politicalization companions).
8. **The Buyer's Siting Checklist: 5 Questions Before You Commit**
   - Turn H2 #7 into a tight 5-question checklist (where's my DC / is it single-tenant vs colocated / what
     city-zoning buffer / local siting news / redundancy in a second region). This is the SEO-hook section
     for "data center siting" and "vps data center location" queries.
9. **Why This Ties Into 2026's Broader Data-Center Story (Politicalization + Cost Waves)**
   - Connect three site themes into one narrative: physical neighborhood heat (today) + regulatory
     backlash/moratoriums (queued politicalization outlines) + the 2026 RAM/GPU cost wave (`vps-price-hikes-
     2026-ramageddon`) → what a buyer should watch for the rest of 2026. This is the "structural layer" H2.
10. **FAQ + Bottom Line**
    - FAQ (5), then a closing CTA anchored to the buyer's concrete takeaway: choose a provider whose
      dispersed US data-center footprint reduces both physical and regulatory siting risk — and lock a fixed
      annual price so a regional shock doesn't hit your renewal. → CTA (RackNerd annual-lock, dispersed US
      DCs).

## 4. FAQ plan (5 questions)

1. **Does data-center waste heat really raise temperatures in nearby neighborhoods?**
2. **Is this a reason to avoid a VPS provider with data centers in hot cities like Phoenix?**
3. **As a VPS customer, can I even control where my VM's data center sits?**
4. **What should I check about a provider's data-center locations before buying?**
5. **How does DC siting risk connect to the 2026 data-center moratoriums / politicalization news?**

## 5. RackNerd affiliate placement plan (≥6 placements; exact CTA = `https://my.racknerd.com/aff.php?aff=16299`)

1. **H2 #1 (news hook) close:** "Hard numbers on DC heat are one more reason to know exactly where your VPS
   runs — compare RackNerd's dispersed US locations." → CTA
2. **H2 #5 (provider table):** RackNerd row anchor — "affordable budget host with a multi-city US DC
   footprint instead of a single residential-adjacent building." → CTA
3. **H2 #6 (dispersed DCs):** "Dispersed US data centers at a budget price are RackNerd's exact niche —
   fixed annual price, multiple US cities." → CTA
4. **H2 #8 (siting checklist):** after "does the provider state DC locations?", "RackNerd publishes a clear
   US DC list — verify any host does the same." → CTA
5. **H2 #9 (2026 trends):** "When siting pressure delays new buildouts near homes, a provider that is
   already multi-location keeps serving you — lock RackNerd's annual rate." → CTA
6. **H2 #10 (bottom line):** final CTA — "Pick a provider with dispersed US data centers and a fixed annual
   price, so neither heat waves nor regional siting fights hit your renewal. Start at RackNerd." → CTA
7. **Inline CTA mentions** woven through §4/§6/§7 as above (6 explicit placements + inline).

## 6. Internal links (all verified on disk this run)

- `/blog/vps-buying-guide/` — general VPS buying intro (H2 #3/#4)
- `/blog/aws-us-east-1-outage-2026/` — prior single-DC incident coverage (H2 #6)
- `/blog/2026-shutdown-cloud-services-vps-migration/` — provider due-diligence theme (H2 #8)
- `/blog/vps-price-hikes-2026-ramageddon/` — 2026 DC cost-wave context (H2 #9) — VERIFIED on disk
- `/blog/racknerd-deep-review-2025/` — the RackNerd anchor page (H2 #5/#6)
- `/blog/vultr-deep-review/` — multi-region alternative reference (H2 #6)
- `/blog/hostinger-review/` — managed alternative row (H2 #5)
- `/blog/hostarmada-vps-review-2026/` — managed alternative row (H2 #5)
- `/blog/nvme-vps-under-10-2026/` — budget-VPS context (H2 #4)
- ⚠️ Pending-only companions (do NOT link until published): `cloud-outages-2026-redundant-vps-setup` (8-11),
  `namecheap-outage-dns-email-vps-resilience-2026` (8-16), `cloud-outage-insurance-vps-risk-2026` (8-17),
  and the politicalization outlines (8-04/8-05/07-15) — none have `.astro` files yet, so none are linked.

## 7. Self-check

- **Banned merchant in whole draft (case-insensitive `grep -c`):** 0 ✅ (excluded-merchant mechanism
  explained brand-free in §1)
- **Title length:** 57 chars (target 30–60 ✅)
- **Description length:** 141 chars (target 70–155 ✅)
- **H2 count:** 10; **FAQ count:** 5; **RackNerd CTA placements:** 6 explicit (§5) + inline mentions ✅ (≥6)
- **CJK:** 0 ✅; **`/zh/` refs:** 2 — both legitimate self-documentation audit lines (the 8-09/8-10/8-14/8-16
  precedent); all other paths exist on disk
- **All internal links** point to `.astro` files verified on disk ✅; pending companions explicitly marked
  "do not link until published"
- **All 5 providers** (RackNerd, Vultr, DigitalOcean, HostArmada, Hostinger) are whitelisted in
  `providers.json` ✅
- **Content gap:** confirmed — grep for `waste heat` / `heat island` / `urban heat` / `siting` / `power
  density` / `data center heat` over `src/` = 0 ✅
- **No duplicate of pending outlines:** differentiated at the **physical/environmental siting layer** from
  the regulatory-politicalization outlines (8-04/8-05/07-15) and from all outage-redundancy outlines
  (technical/financial vs the siting/heat angle) ✅
- **Facts to reverify at full-draft time:** (a) exact study numbers from the ASME abstract / ASU News (the
  numbers above came from the HN thread quoting the paper — re-confirm against the abstract or a fetched
  coverage body); (b) every whitelisted provider's live DC footprint; (c) RackNerd annual-lock price point.
