# VPSTier Daily-Outline Run Record — 2026-08-16 (Sunday)

## Outcome
- **New outline:** `drafts/outline-2026-08-16-vpstier-daily.md` → slug `namecheap-outage-dns-email-vps-resilience-2026`
- **Deliverable:** news-analysis + resilience buyer-guide (10 H2 / 5 FAQ / 7 RackNerd CTA placements), English only (LANG policy).
- **state.json:** 1 new `outline_pending_publish` entry appended (drafts 25 → 26); `last_run` = 2026-08-16;
  `publish_notes` schema-drift-safe appended. `last_publish` untouched (publish-side field).

## Topic decision
- **Briefing (`3ea88f8bb2d0`) SUCCEEDED today** (re-checked the day's file, not assumed): 10 items, all healthy.
  BUT **both vpstier ⭐ picks reference the excluded merchant** (a 187–250% price-increase re-test + an
  inference-API teardown, both about that merchant) → ineligible under the permanent merchant policy. Per the
  Tier-1 banned-pivot, substituted a fresh, dated, multi-outlet VPS story with a confirmed content gap.
- **GSC (2026-08-16 07:00):** vpstier's only 2 queries:
  - `how to deploy ai agent on vps` (rank 75) → **captured** by queued `best-vps-for-ai-agents-2026` (8-14) → not re-picked.
  - `zappiehost` (rank 56) → brand nav query; `zappiehost-vps-review-2026.astro` already published → not re-picked.
- **Pick — the Namecheap outage (Aug 13–15, 2026):** a storm-triggered cooling failure at Namecheap's Phoenix
  (RadiusDC Tier 3) data center took down hosting, EasyWP, and private email for several hours. Verified across
  **11 named outlets with dates** (Engadget 8-13, TechRadar 8-14, cyberkendra 8-13, Emerald Book 8-13,
  finchannel 8-15, Domain Name Wire 8-14 [**body fetched via wp-json**], PCMag UK 8-14, Hindustan Times 8-14,
  AOL 8-14, techbarrista 8-15, + mprnews 8-10 Minneapolis as a second single-DC datapoint).
- **The article thesis (body-verified):** Domain Name Wire confirms **DNS resolution + URL forwarding kept
  working but DNS/email *management* was impaired** — the registrar's control plane sits in the same Phoenix DC
  as its web hosting, so one cooling incident takes down the workload AND the reroute tools. → The durable
  lesson: **separate control-plane services (DNS + email) from the VPS/workload tier** so one DC failure can't
  take your whole operation offline.
- **Content-gap evidence:** grep over `src/` for `DNS outage` / `cooling failure` / `private email` / `EasyWP` /
  `external DNS` / `DNS provider separate` / `secondary DNS` / `DNS redundancy` = **0 matches** for every term.
  No site article covers DNS/email control-plane separation or single-DC concentration risk.
- **Differentiation (not a duplicate):** vs queued `namecheap-vps-review-2026` (8-01) = a commercial provider
  *review* (buying decision); this is a news-analysis + resilience architecture. vs queued
  `cloud-outages-2026-redundant-vps-setup` (8-11) = workload-level multi-cloud redundancy; this is
  control-plane-level (DNS/email) separation. Distinct intents, distinct deliverables.

## Validation (script-measured)
- Title `Namecheap Outage 2026: Keep DNS, Email and Hosting Separate` = **59 chars** (30–60 ✅)
- Description = **155 chars** (70–155 ✅)
- H2 sections: 10; FAQ: 5; RackNerd CTA placements: 7 (≥6 ✅)
- Banned-merchant name in whole draft (case-insensitive): **0** ✅
- CJK: **0** ✅; `/zh/` refs: 2 (self-documentation audit lines, 8-09/8-10/8-14 precedent) ✅
- Internal `/blog/` links: all on disk except `cloud-outages-2026-redundant-vps-setup`, explicitly flagged
  "when it publishes" (8-11 outline) — NOT linked until live ✅
- Whitelisted VPS providers (RackNerd/Vultr/DigitalOcean/Hostinger/HostArmada): all in `providers.json` ✅
  Note: Cloudflare appears only as the *external-DNS* recommendation (a free service, not a VPS product page),
  which is outside the provider-whitelist scope; flag for user awareness.

## Git discipline (two-commit, per ilang-content; branch `main` confirmed)
- Commit 1: `drafts/outline-2026-08-16-vpstier-daily.md` + `drafts/run-record-2026-08-16-vpstier-daily-outline.md`
- Commit 2: `drafts/state.json` (outline entry + last_run + publish_notes)
- Did NOT `git add -A` the accumulated untracked outline/run-record backlog (flagged below). Committed the
  specific files this run created only.

## On-hold / open items
1. **Uncommitted backlog in `drafts/`** (pre-existing, NOT from this run): outline-8-01/8-03/8-04/8-05/8-07/
   8-12/8-13 + run-record-8-03/8-04/8-05/8-07/8-12 .md files are untracked. A working-tree reset would destroy
   them (converter-epub 8-07 class of incident). Recommend a separate cleanup commit (user decision).
2. **Large pending-outline queue (26 drafts).** User is the publish-gate; today's run appends one entry.
   Recommend publishing `best-vps-for-ai-agents-2026` (8-14) first — it fixes the live phantom index card.
3. **`ovh backup vps` + `how to deploy ai agent on vps` GSC signals** — both captured by queued outlines, not re-picked.
4. **Provider DC + DNS/email footprint tables (H2 #5) must be reverified from live provider pages at full-draft
   time** — do not inherit stale tables from any prior article.
5. **Cloudflare-as-DNS-recommendation scope note:** referenced conceptually (free DNS service), not as a
   whitelisted VPS merchant; confirm acceptable with user if in doubt.
