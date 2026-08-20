# VPSTier Daily-Outline Run Record — 2026-08-20

## Trigger: briefing-succeeds-but-vpstier-stars-are-banned (3rd occurrence)

The 08:24 briefing (`3ea88f8bb2d0`) **SUCCEEDED** (10 items, sources verified). Both vpstier ⭐ picks
referenced the **excluded merchant** and were rejected under the permanent merchant policy — the same
Tier-1 banned-pivot trigger as 8-16 and 8-19. The non-banned briefing item #3 (data-center waste-heat
study, HN 310p) was selected and independently verified.

## Decision

- **Selected topic:** data-center siting / neighborhood heat (physical/environmental layer of the
  site's data-center theme) — `data-center-heat-siting-vps-selection-2026`
- **Verified hook:** peer-reviewed ASME *J. Sustainable Buildings* field study, re-surfaced on HN
  2026-08-18 (310 pts / 486 comments). Phoenix, AZ, NTT PH1 ~169 MW campus across from a residential
  neighborhood. Measured upwind ~42.7 °C → downwind ~43.5 °C (~0.8 °C avg), up to 2.2 °C (~4 °F)
  localized warming within ~500 m downwind; condenser discharge 8–14 °C above ambient.
- **Multi-outlet cluster:** Adafruit 8-18, ASU News 5-18, AZ Family 5-19, azcentral 6-04, Facilities
  Dive 5-27, Data Center Knowledge 8-11, grist/Pulitzer. Bot-403 on ASU/Adafruit bodies; facts pulled
  from the HN thread quoting the paper + GNews headline cluster.
- **Content gap:** 0 hits for `waste heat` / `heat island` / `urban heat` / `siting` / `power density`
  / `data center heat` across `src/`.
- **Differentiation:** NEW environmental/siting layer — distinct from the REGULATORY politicalization
  outlines (8-04/8-05/07-15 — verified 0 heat/temperature/siting mentions) and from all outage-
  redundancy outlines (technical/financial). Not a duplicate.
- **GSC:** `zappiehost` only (brand-nav, published page on disk) → not re-picked.
- **Format:** single-deliverable news-analysis + buyer-guide; 10 H2 / 5 FAQ / 6 RackNerd CTAs / 9
  verified internal links. Title 57c / desc 141c (Python-measured).

## Self-check results

- Banned merchant in whole draft: **0** ✅
- CJK: **0** ✅; `/zh/` refs: 2 (legitimate audit lines)
- Title 57 (30–60) ✅; Description 141 (70–155) ✅
- H2 10 / FAQ 5 / RackNerd CTA 6 explicit ✅ (≥6)
- All internal links verified on disk; pending companions marked "do not link until published" ✅
- All 5 providers whitelisted in providers.json ✅

## Facts to reverify at full-draft time

1. Study numbers against ASME abstract / ASU News body (current figures from the HN thread)
2. Each whitelisted provider's live DC footprint (RackNerd site 403s to urllib — use live affiliate
   page or prior verified article footprint + re-confirm)
3. RackNerd annual-lock price point

## Pending-outline queue (for user awareness — do NOT auto-archive)

24 `outline_pending_publish` entries exist. Highlights: greengeeks (7-07), hostdare (7-08),
ny-data-center-moratorium (7-15), januscape-kvm-escape (7-16), black-friday-tracker (7-17),
agent-zero (7-18), cloudflare-markdown (7-19), 2× luxvps (7-20/7-23), provider-shutdown-warning-signs
(7-24), 5-best-summer-deals (7-26), namecheap (8-01), serverhost (8-03),
data-center-politicalization (8-04), ovhcloud (8-07), woocommerce (8-08), kernel-escape (8-09),
managed-k8s (8-10), outage-redundancy (8-11), ai-agents (8-14), dns-email-resilience (8-16),
outage-insurance (8-17). Today's outline is a separate entry (never bundle). The user is the
publish-gate and archive-gate.

## Notes

- state.json `drafts_count` field reads 26 but there are 24 `outline_pending_publish` + flush entries;
  the git log shows commit `57c84ec` claimed "gpu-ram-price-wave ... drafts 72->73" but the committed
  state.json does not contain a gpu-ram `drafts[]` entry — the 8-19 add-provider run's state.json entry
  for that outline appears to have been committed separately or rolled back. Flag for user awareness
  (not blocking this run; today's entry appends cleanly).
- state.json on disk is clean (matches git HEAD) before this run.
