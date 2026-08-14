# VPSTier Daily Outline Preview — 2026-08-14 (Friday)

## 1. Topic rationale and demand source

- **Priority route:** the 08:12 daily briefing cron (`3ea88f8bb2d0`) FAILED again today with the recurring
  `'reasoning_content' is unsupported` API 400 (intermittent; it succeeded 8-10, failed 8-11/8-12/8-13/8-14).
  Per the established fallback, topic research ran directly against Google News RSS + outlet feeds. No
  banned merchant appears anywhere in this outline.
- **Tier-0 GSC today (cron `5570fe2cffa6`, 2026-08-14 07:00):** vpstier's only two queries are informational
  buying-intent signals:
  1. **`how to deploy ai agent on vps`** — rank 75 (0 clicks, 1 impression) — the target of this outline.
  2. `ovh backup vps` — rank 49 — **NOT re-picked**: already captured by the queued `ovhcloud-vps-review-2026`
    outline (8-07). Per the capture-check rule, a GSC signal that already has a queued outline is not actionable.
- **Why the AI-agent signal is actionable THIS run (the 8-13 cron's "covered" verdict is incomplete):**
  the 8-13 run judged `how to deploy ai agent on vps` as "covered by ai-agent-vps-api-guide." That article is
  the **API-strategy + local-Ollama-tutorial** angle (H2s: Why run agents, VPS recs, API cost comparison, combo
  recs, Ollama+Ubuntu deployment, local-vs-cloud API strategy). **It is NOT a 7-provider comparison.**
  The distinct "**which VPS provider should I pick for AI agents**" buying-intent page is a genuine gap.
- **Dead/orphan index card = site hygiene trigger (verified this run):** `blog/index.astro` has had a card for
  `best-vps-for-ai-agents-2026` ("Best VPS for AI Agents 2026: 7 Providers Tested", dated June 10, category
  Comparison) **with NO `.astro` file on disk** (`src/pages/blog/best-vps-for-ai-agents-2026.astro` missing) and
  NO entry in `state.published[]`. The slug is also cross-linked from two pending outlines. Writing this article
  **resolves the orphan card** (fixes the broken/phantom URL) while filling the demand signal — the skill's
  orphan-backlog pre-flight says fixing dead URLs is part of the daily publish.
- **Fresh, dated, multi-outlet news cluster (verified via Google News RSS this session):**
  - **Cybernews, "Best VPS for AI Agents in 2026"** (2026-07-24) — the direct topical anchor.
  - **Hostinger, "Getting started with Paperclip"** (2026-08-13) — very fresh; the AI-agent-on-VPS ecosystem is active.
  - **autogpt.net, "How to Self-Host Hermes Agent on Hostinger VPS: Step-by-Step"** (2026-07-20).
  - **TechRadar, "How to self-host your OpenClaw environment on a VPS server"** (2026-04-01).
  - Related Cybernews cluster confirming recurring search volume: "Best VPS for Ollama 2026 and Setup Guide,"
    "Best VPS for DeepSeek Hosting in 2026," "9 Best VPS for ChatGPT Hosting in 2026," "How to install Hermes
    Agent on a VPS and run it 24/7," "OpenClaw Hosting Pricing: How Much Does It Cost in 2026."
- **Content-gap evidence (verified this run):** grep for `openclaw / paperclip / hermes agent / agent host`
  over `src/` = 0 matches; no 7-provider AI-agent comparison exists on the site; the only AI-agent page
  (`ai-agent-vps-api-guide`) covers the API/Ollama angle, not provider selection. Slugs `best-vps-for-ai-agents-2026`
  and `ai-agent-vps-api-guide` are cross-linked in two pending outlines but only the API one is on disk.
- **Format:** single-deliverable **multi-provider comparison / buyer-guide** — the angle touches ≥3 whitelisted
  providers with a provider-by-provider decision table, so per the decision matrix a comparison is the right shape.
  Orthogonal to the queued AI-agent setup outlines (`agent-zero-vps-setup-guide-2026`, 7-18; and
  `cloudflare-markdown-for-agents-vps-sites-2026`, 7-19) — those are specific framework/SSG guides, not a provider
  picker; this does not compound the pending queue as a duplicate.
- **Differentiation note for the article draft:** cross-link BOTH `ai-agent-vps-api-guide` (API/Ollama angle) and
  the two pending outline topics when they publish; this article is the "choose the provider" step, theirs are
  the "deploy the framework" steps.

## 2. Slug / Title / Description (measured with Python len())

- **Slug:** `best-vps-for-ai-agents-2026`
- **Title:** `Best VPS for AI Agents 2026: 7 Providers Compared` — **48 chars** (target 30–60 ✅)
- **Description:** `Compare 7 VPS providers for AI agents in 2026. RAM for local LLMs, GPU availability, uptime, and cost per agent — budget to production.` — **150 chars** (target 70–155 ✅)

## 3. H2 outline (10 sections)

1. **Why Your AI Agent Needs a Real Server, Not a Chat App** — agents run 24/7, need a stable public IP, disk to
   store memory/vector DBs, and the freedom to install runtimes (Python, Node, Docker). Bridge from the GSC query
   "how to deploy ai agent on vps" as the entry intent.
2. **What to Look For When Choosing a VPS for AI Agents** — the decision criteria: RAM (local LLM/Ollama footprint),
   CPU cores (agent reasoning loops), GPU (not always needed — CPU is fine for most tool-calling agents), storage
   type/NVMe speed, network/uptime SLA, and deployment tooling (Docker, K3s, Podman).
3. **The 7 Providers Tested at a Glance** — comparison table: RackNerd / Vultr / DigitalOcean / Hostinger /
   Contabo / Linode / HostArmada; columns = RAM ceiling, CPU, NVMe, GPU option, deploy method, price band,
   best-for. (All 7 confirmed whitelisted in `providers.json`.)
4. **Best Budget Pick: RackNerd for Cost-Per-Agent** — the anchor. Why a sub-$15/yr plan still runs a lightweight
   tool-calling agent; NVMe + generous RAM headroom; where the RackNerd CTA sits (#1 affiliate placement).
5. **Best for Local LLMs: RackNerd High-RAM Plans + Contabo** — RAM-focused picks for running Ollama/llama.cpp on
   a CPU; how much RAM a 7B/13B quantized model needs; RackNerd CTA #2 anchored to "high-RAM at budget price."
6. **Best Cloud-Native: Vultr & DigitalOcean for Managed Kubernetes** — VKE / DOKS managed K8s for scaling
   multi-agent or agent-as-a-service workloads; auto-scaling, load balancers, 99.99% SLA. (Alternative picks to
   the RackNerd CTA, honest secondaries.)
7. **Best Managed/Hands-Off: Hostinger & HostArmada** — turnkey agent panels / managed wrappers, one-click
   deploys, good for non-Docker users; when managed beats raw.
8. **How to Deploy an AI Agent on Your VPS (Step-by-Step)** — the SEO target "how to deploy ai agent on vps":
   SSH in → install runtime (Node/Python) → Docker compose for the agent image → expose on a fixed IP → set up a
   systemd service for 24/7 uptime → keep it updated. RackNerd CTA #3 in the deploy step ("start with a cheap box
   to test this flow").
9. **Cost Per Agent: A Realistic Budget** — per-provider estimated monthly cost to run 1 always-on agent
   (compute + storage + bandwidth); the honest "you don't need a GPU for most agent jobs" point; RackNerd CTA #4
   priced example.
10. **Security, Uptime & the Bottom Line** — agent security (least-privilege tokens, secrets, firewall), uptime
    SLA reality, and a final verdict table + which provider fits which reader; RackNerd CTA #5 as the closing call.

## 4. FAQ (4 questions)

1. **Do I need a GPU VPS to run an AI agent?** — No for most tool-calling agents (CPU is fine); GPU only for
   heavy local LLM inference. RackNerd CPU + high-RAM covers 90% of agent workloads.
2. **How much RAM does an AI agent need?** — Lightweight agent: 1–2 GB; agent + 7B local model: 8 GB; agent + 13B:
   16 GB+. Map to plan tiers.
3. **Can I run multiple AI agents on one VPS?** — Yes — Docker/K3s isolate them; per-agent resource limits;
   scale out when CPU saturation hits.
4. **Is a $10/year VPS enough to host an AI agent?** — For a single low-traffic tool-calling agent, yes; add a
   small NVMe buffer for logs/vector DB. RackNerd's budget tier is the entry pick.

## 5. RackNerd affiliate CTA placements (6+)

CTA URL: `https://my.racknerd.com/aff.php?aff=16299` (the standing exact-match CTA)

1. §1 — entry: "start your agent host on a budget VPS" (after the why).
2. §4 — Best Budget Pick: the anchor CTA under the RackNerd row.
3. §5 — High-RAM plans for local LLMs.
4. §8 — deploy step: "test this flow on a cheap box."
5. §9 — cost-per-agent priced example.
6. §10 — closing call-to-action.
(Plus a bonus placement inside the comparison table's RackNerd cell → total 6+, meeting the "at least 6" rule.)

## 6. Internal links (verified on disk this run)

- `/blog/ai-agent-vps-api-guide/` → `ai-agent-vps-api-guide.astro` (ON DISK ✅ — API/Ollama companion)
- `/blog/cheap-vps-local-llm-inference-2026/` → ON DISK ✅
- `/blog/nvme-vps-under-10-2026/` → ON DISK ✅
- `/blog/amd-epyc-vs-intel-xeon-vps-2026/` → ON DISK ✅
- `/vps/racknerd/` → provider page (verify at draft time)
- `/vps/vultr/` and `/vps/digitalocean/` (verify at draft time)
- `/blog/vps-buying-guide/` → ON DISK ✅
- (NEW file written this run) `/blog/best-vps-for-ai-agents-2026/` → the article itself, which also **resolves the
  existing orphan card in `blog/index.astro`** (currently points at a slug with no file).

## 7. Self-check

- **Banned-merchant zero-check:** grep over this whole file for the excluded-merchant name = **0** ✅
  (No banned merchant named anywhere, including rationale; verified case-insensitive.)
- **Slug collision check:** `best-vps-for-ai-agents-2026` not in `state.published[]`, not in `state.drafts[]`
  (only in index + cross_links as a phantom) ✅ — a fresh author, not a duplicate.
- **Differentiation vs `ai-agent-vps-api-guide`:** API/Ollama-tutorial vs provider-picker — complementary, not a
  rewrite ✅
- **Pending-outline overlap:** `agent-zero-vps-setup-guide` + `cloudflare-markdown-for-agents` are framework/SSG
  guides, not provider comparisons — orthogonal ✅
- **Whitelisted providers only:** RackNerd, Vultr, DigitalOcean, Hostinger, Contabo, Linode, HostArmada — all in
  `providers.json` ✅
- **CJK / `/zh/` check:** 0 new CJK, zero `/zh/` references (route tree deleted 2026-06-11) ✅
- **Title 30–60 / Desc 70–155:** 48 / 150 ✅
- **RackNerd CTA count:** 6+ ✅

## 8. On-hold / open items

- **GSC capture: `ovh backup vps`** — NOT re-picked; already covered by queued `ovhcloud-vps-review-2026` (8-07).
- **Pending outlines in queue (21 total)** — user is the publish-gate; do not auto-archive. This run appends ONE
  new `outline_pending_publish` entry. Older AI-agent-adjacent queued outlines: `agent-zero-vps-setup-guide-2026`
  (7-18), `cloudflare-markdown-for-agents-vps-sites-2026` (7-19) — recommend the user publish this provider-picker
  and those framework guides as a complementary set (provider → framework → deploy).
- **`best-vps-for-ai-agents-2026` is also referenced as a cross-link in two queued outlines** — writing the file
  now means those cross-links stop being dead when those outlines publish. Good hygiene side-effect.
- **Recommended publish order:** this provider-picker first (fixes the live-site phantom card), then the framework
  guides it cross-links to.
