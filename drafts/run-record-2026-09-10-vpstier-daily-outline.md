# Run Record: vpstier daily-outline 2026-09-10

**Cron:** vpstier-daily-outline (`5fd2a36f2dc4`)
**Date:** 2026-09-10 (Thu)
**Run mode:** no_agent (scripted outline cron)
**Variant label:** variant-(0) — briefing SUCCESS, one ⭐ selectable (whitelisted + fresh + not queued + not off-shape); remaining items rejected for cause

---

## §1 Variant classification — Briefing SUCCESS, one ⭐ selectable

The 2026-09-10 briefing (08:05 UTC) produced 3 vpstier items:

| # | Briefing item | Status | Reason |
|---|---|---|---|
| 1 | **"DigitalOcean becomes a Founding Corporate Patron of Omarchy, donating $3M"** (omarchy.org news, dated 2026-09-09, by DHH) | **SELECTED** | **Whitelisted** (DigitalOcean in `providers.json`), **fresh** (d-1, inside the 8-day gate), **body-verifiable** (full article + the patrons page fetched directly). Buyer-relevant: a mainstream VPS vendor is funding and productising the always-on agentic-compute use case — the exact workload vpstier's ICP queries. |
| 2 | "Linode $12 vs $5 benchmark — gap not obvious" (webbynode.com/articles/linode-5-12-48-los-angeles-six-fresh-deployments, Sept 3) | **REJECTED — non-whitelisted source + un-fetchable body + covered vendor** | webbynode.com is **not in `providers.json`** (0 hits). Its article URL returned a client-side SPA shell (21 KB, empty `<div id="root">`) with **no fetchable body** — the benchmark numbers cannot be verified. Separately, Linode already has a full published review on disk (`linode-vps-review-2026`, 2026-08-08) covering the $5 → $192 plan ladder and the transparent-renewal-pricing differentiator. Rejecting on source integrity AND coverage. |
| 3 | "Google Compute shut down my server for distributing malware" (HN item 49594022, Sept 7) | **REJECTED — thin engagement + no verified artifact** | HN **score 2 / 0 comments** — a single uncorroborated anecdote; the submitter's own text concedes the binary *was* false-flagged. No dated vendor statement, no policy document, no affected count. The provider-trust / account-termination mechanism is already covered from a stronger angle in the queued `oracle-cloud-free-tier-account-hack-2026` (09-02) and the queued provider-exit piece (08-27). Used only as a **pattern** in §9, never as evidence. |

**Variant label: canonical-variant-(0)** (briefing succeeds, ≥1 ⭐ selectable, remaining items off-shape/thin). Not a banned-pivot (no ⭐ referenced the excluded merchant), not a capture (neither rejected item duplicates a queued/published slug), not off-shape-only.

---

## §2 Selected pick: `agentic-vps-always-on-ai-agent-2026`

- **Title:** `Agentic VPS 2026: Do You Need a Server for Your AI Agent?` — **57 chars** (gate 30–60 ✅)
- **Description:** "DigitalOcean just bet $3M on the agentic OS. Do your AI agents need an always-on VPS? Workload test, cost math, and 6 tested hosts." — **131 chars** (gate 70–155 ✅)
- **Editorial anchor:** the DigitalOcean/Omarchy $3M founding-patron news (dated 2026-09-09) → a buyer-guide on the **always-on agentic-workload** question: *when does an AI agent graduate from a laptop session to a persistent server, and what is the cheapest sensible way to run one?* Anchor artifacts = a 6-row decision matrix + a live-verified cost table + a minimum-viable-setup recipe.
- **H2 count:** 10 (gate 8–10 ✅)
- **FAQ count:** 5 (gate 3–5 ✅)
- **RackNerd CTA placements:** 8 (gate ≥6 ✅)

---

## §3 Capture-check + coverage-gap verification

**Capture-check across `drafts[]` (45 entries):** no queued slug/title contains `agentic`, `always-on`, `persistent agent`, `agent server`, `24/7 agent`. Closest queued items are orthogonal:
- `best-vps-for-ai-agents-2026` (06-10) — provider roundup ("which host"), not "do I need one and how do I size it";
- `cheap-vps-local-llm-inference-2026` (08-02) — local model *inference*, not agent persistence;
- `oracle-cloud-free-tier-account-hack-2026` (09-02) — account takeover, unrelated mechanism.

**On-disk body-grep across 59 blog + 40 /vps/ files:**
- `Omarchy` / `Founding Corporate Patron` / `Omacom` / `DHH` / `37signals` / `Paddy Srinivasan` / `one-click Droplet` / `Hermes and OpenClaw` / `contributors.rubyonrails` / `1 million a year` — **0 hits site-wide**.
- `agentic VPS` / `agentic OS` / `long-running agent` / `one-click agent` / `persistent agent` — **0 hits**.
- Published `ai-agent-vps-api-guide.astro` inspected directly: `Omarchy` 0, `agentic OS` 0, `one-click` 0, `always-on` 0, `24/7` 0, `persistent` 0, `OpenClaw` 0, `Droplet` 0. The existing piece is **API-cost + Ollama inference** — a different question from agent persistence.
- Generic non-discriminators that DO hit (expected, NOT blockers): `agentic`/`always-on` appear once in `azure-ai-outage-self-host-vps-2026.astro` in an unrelated self-host-resilience sentence; `VPS for AI agents` in blog index card copy. The **agentic-workload-persistence** token set is all 0 — genuine gap.

---

## §4 Editorial-anchor verification (decision matrix + cost table)

**Decision matrix** (built from workload characteristics, not vendor specs) — the fastest artifact a reader can self-apply:

| Your agent today | Runs on | Needs a VPS? | Why |
|---|---|---|---|
| Answers a prompt in a chat window | Vendor's cloud | **No** | No persistence requirement; the vendor owns the runtime. |
| Runs as a CLI/TUI session on your laptop | Local machine | **No** (yet) | Fine while you're present; breaks the moment you close the lid. |
| Polls an API / inbox on a schedule | Cron on your desktop | **Yes, soon** | Missed windows during sleep/shutdown = missed work. Graduation point. |
| Maintains long-lived state + a queue | Local process | **Yes** | Process death = lost state unless checkpointed off-device. |
| Serves webhooks / accepts inbound requests | Localhost | **Yes** | A closed laptop is unreachable; nothing can call it. |
| Multi-agent hand-off | Ad-hoc local | **Yes** | Coordination needs a shared, always-reachable address. |

**Cost table — live-verified 2026-09-10:**

| Option | Monthly | Always-on? | Ops burden | Honest note |
|---|---|---|---|---|
| Local CLI on your laptop | $0 | No | You are the scheduler | Fails on lid-close/reboot. |
| Managed agent platform (vendor-run) | varies | Yes | Lowest | Vendor owns runtime + pricing. |
| DigitalOcean Basic Droplet (512 MiB / 1 vCPU / 10 GiB SSD / 500 GiB transfer) | **$4.00** ($0.00595/hr) | Yes | You patch it | Per-second billing since 2026-01-01 (60s / $0.01 min). |
| DigitalOcean Basic Droplet (1 GiB / 1 vCPU / 25 GiB SSD / 1,000 GiB transfer) | **$6.00** ($0.00893/hr) | Yes | You patch it | Realistic floor for Node/Python agent + logs. |
| RackNerd annual KVM special | **from $21.99/yr** (~$1.83/mo) | Yes | You patch it | Cheapest always-on floor on the whitelist; annual pre-pay trade. |

**Verified DO pricing (digitalocean.com/pricing/droplets, parsed today) — Basic tier:** 512 MiB $4.00/mo ($0.00595/hr) · 1 GiB $6.00 ($0.00893) · 2 GiB/1 vCPU $12.00 ($0.01786) · 2 GiB/2 vCPU $18.00 ($0.02679) · 4 GiB/2 vCPU $24.00 ($0.03571) · 8 GiB/4 vCPU $48.00 ($0.07143) · 16 GiB/8 vCPU $96.00 ($0.14286). **Effective Jan 1 2026:** per-second billing (minimum 60 seconds or $0.01).

**Honesty instances (the 8-21/8-23/9-08 pattern):**
1. DO is the news hook, **not** the cheapest always-on tier — RackNerd annual is. Stated explicitly.
2. The $3M is a **foundation donation**, not a discount/credit/price change. Stated in §4 and FAQ 3.
3. A third artifact covers the security/ops caveat (non-root, scoped tokens, systemd restart, log rotation, restore-tested snapshot), cross-referencing the queued off-site-backup + supply-chain pieces by *concept*, not by dead link.

---

## §5 Self-check (on outline draft)

| Check | Result |
|---|---|
| Banned-merchant zero-check (`grep -ci` for each canonical brand-name token across the WHOLE draft incl. headings, rationale, FAQ, section 9 self-check text) | **0 ✅** — category language only ("excluded merchant / permanently excluded"); no brand-name token embedded anywhere |
| CJK / non-ASCII (Unified Ideographs incl. Ext. A/B, kana) over draft | **0 ✅** |
| `/zh/` references in draft | **0 ✅** (route tree deleted; no self-doc regex present that would introduce a false positive) |
| Title length Python `len()` | **57 ✅** (30–60) |
| Description length Python `len()` | **131 ✅** (70–155) |
| H2 count | **10 ✅** (8–10) |
| FAQ count | **5 ✅** (3–5) |
| RackNerd CTA placements | **8 ✅** (≥6) |
| On-disk body-grep-0 for the always-on-agent angle | **VERIFIED ✅** |

---

## §6 On-hold items / supersede flags

- **No supersede.** Today's pick is additive; nothing on disk is invalidated by the DO/Omarchy announcement.
- **No capture.** Neither rejected item maps to a queued slug.
- **Rejected item 2 (Linode benchmark) recommendation:** leave rejected. If the user wants a Linode plan-value piece later, draft it from Linode's own pricing page against the existing `linode-vps-review-2026`, not from the un-fetchable non-whitelisted SPA.
- **Rejected item 3 (Google Compute termination):** do not upgrade to a standalone article on HN score-2 / 0-comment evidence. If the pattern recurs with a vendor statement or an affected count, it becomes a legitimate provider-trust piece.
- 45 `outline_pending_publish` entries remain in `drafts[]`; today's append makes 46. User is the publish-gate.

---

## §7 Pitfalls captured this run

1. **Non-whitelisted SPA source** — webbynode.com is absent from `providers.json` AND returns a body-less SPA shell. Reject on source integrity even when the topic is legitimate.
2. **Thin-engagement HN anecdote as evidence** — score 2 / 0 comments is a pattern, not an incident. Cite as pattern with the caveat.
3. **Donation ≠ discount** — an announcement about a company giving money to a project creates no reader benefit; say so explicitly to prevent an accidental sales framing.
4. **Headline vendor ≠ recommended cheapest** — when the news hook is a premium vendor, the cheapest honest recommendation may be a different whitelisted host; state both.
5. **Queued-slug link guard** — queued outlines referenced as topics only, never as `<a href>` to unbuilt routes.
6. **Excluded-merchant self-check line** — described in category language; no brand token embedded in the self-check text itself.
7. **Anti-fabrication** — every number is either live-fetched today or explicitly labelled "re-verify at full-draft time" (the $21.99/yr annual promo figure).

---

## §8 Operational state

- **CLOUDFLARE_API_TOKEN: ACTIVE** (verified 2026-09-08, expires 2027-09-02) — no `deploy_pending` flag needed downstream.
- **Orphan backlog:** 20 untracked prior outline/run-record files (8-01 → 9-07) remain — out of scope for this cron; flagged for user cleanup. `git add` specific paths only.
- **Two-commit pattern:** `feat(drafts):` (outline + run-record) then `chore(state):` (state.json), then `git push origin main`.

---

## §9 Source-chain (verified 2026-09-10)

| Source | URL | Fetch result | Facts used |
|---|---|---|---|
| Omarchy news (announcement) | `https://omarchy.org/news/2026/09/digitalocean-joins-as-founding-corporate-patron/` | HTTP 200, full body | dated 2026-09-09 by DHH; $1M/yr x 3yr = $3M; total ~$18.5M; DO joins Meta Superintelligence Labs as Founding Corporate Patron; "one-click Droplets for Hermes and OpenClaw"; Paddy Srinivasan (DO CEO); "Compute by DigitalOcean" footer; Krzysztof Wilczyński (Head of Kernel) + outfoxxed (Head of Shell) hires |
| Omarchy patrons page | `https://omarchy.org/patrons` | HTTP 200, full body | Founding Corporate Patrons = $1,000,000/year for three years; listed: Meta Superintelligence Labs + DigitalOcean; Distinguished Corporate Patrons ($100k/yr): 1Password, 37signals, Anthropic, Fireworks, Four Technologies, OpenAI, OpenRouter |
| DigitalOcean Droplet pricing | `https://www.digitalocean.com/pricing/droplets` | HTTP 200, table parsed | Basic tiers 512 MiB→16 GiB ($4.00→$96.00/mo; $0.00595→$0.14286/hr); per-second billing effective 2026-01-01, min 60s or $0.01 |
| RackNerd affiliate landing | `https://my.racknerd.com/aff.php?aff=16299` | HTTP 200 | "VPS hosting... starting at just $2.24/month" (site-wide starting figure); 12 DCs listed (LA, San Jose, Seattle, Dallas, Atlanta, Chicago, NY, Ashburn, Amsterdam, France, Dublin, Toronto); dedicated servers from $139/mo |
| HN item | `https://hacker-news.firebaseio.com/v0/item/49594022.json` | HTTP 200 | score 2, descendants 0, by farzher, title "Google Compute shut down my server for distributing malware"; submitter concedes binary false-flagged (UPX compression) |
| webbynode.com Linode article | `https://webbynode.com/articles/linode-5-12-48-los-angeles-six-fresh-deployments` | HTTP 200 but **SPA shell — no body** | rejection basis only; no facts used |
| On-disk providers whitelist | `/root/vpstier-site/src/data/providers.json` | parsed | 65 whitelisted providers; DigitalOcean + Linode + Vultr + RackNerd present; webbynode.com absent |

**Unverified / to re-check at full-draft time:** the RackNerd **$21.99/yr** annual-promo figure is the standing figure used across prior vpstier articles; the affiliate landing page shows a site-wide "starting at $2.24/month" rather than the promo table. The full-draft cron must re-read the RackNerd deals page (`/BlackFriday/` per the 09-07 note, since `/kvm-vps/` returned HTTP 500 historically) before quoting the annual price.

---

## §10 State.json plan

- `drafts[]` append: slug `agentic-vps-always-on-ai-agent-2026`, date `2026-09-10`, status `outline_pending_publish`, title_en/description_en as §2, note: 10 H2 / 5 FAQ / 8 RackNerd CTA; variant-0 ⭐ #1 selected; always-on agentic-workload buyer guide.
- `drafts_count`: 45 → 46 (bump AFTER append, same Python op).
- `last_run`: `"2026-09-10"` (explicit assignment).
- `publish_notes` (string): append `\n`-separated line with date marker + natural-language title fragment.
- `json.dump(..., ensure_ascii=False)`.
- 4-check verifier: count == len(drafts); last_run == today; today-in-`publish_notes`; natural-title fragment in `publish_notes`.

---

## §11 Commit plan (two-commit pattern)

1. `feat(drafts):` outline + run-record (this file + `outline-2026-09-10-vpstier-daily.md`).
2. `chore(state):` state.json update.
3. `git push origin main`.

---

*End of run record.*
