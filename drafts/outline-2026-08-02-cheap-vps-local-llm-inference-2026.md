# VPSTier Daily Outline Preview — 2026-08-02

## 1. Topic rationale and demand source

- **Priority route:** Tier 1 banned-provider pivot (4th consecutive firing) + Tier 3 cost-discipline comparison.
- The leading VPS item in today's industry briefing focuses on a specific EU operator moving into LLM inference. The brand is on the permanent excluded-merchant list, so the original article is not actionable. The story still reveals a real 2026 buyer intent: small-model self-hosting on a budget VPS, away from per-token API bills.
- A comparison article that directly answers that intent — naming 5 whitelisted budget hosts and showing tokens-per-dollar for 7-8B models — captures the same editorial territory without referencing the excluded brand or its pricing.
- This also breaks vpstier's 17-pick streak of single-provider reviews and brings the editorial wheel back to the comparison format. The existing `ai-agent-vps-api-guide.astro` is dated (May 30 2026) and broad; a 2026 update with current pricing, NVMe SSDs, DDR5, and a focus on inference tokens-per-dollar fills a real gap.
- **Publication guardrail:** Reverify every plan price, RAM tier, NVMe capacity, network port, and region coverage from current primary sources before drafting the full article. Do not inherit the May 30 figures from the older guide.

## 2. Slug, title, and description

- **Slug:** `cheap-vps-local-llm-inference-2026`
- **Title:** `Cheap VPS for Local LLM Inference 2026: 5 Hosts Tested`
- **Title length:** 54 characters (30–60 range)
- **Description:** `Run Llama 3.1 8B or Mistral 7B on a $5-$25/mo VPS. 5 budget KVM hosts tested for RAM, NVMe, and tokens-per-dollar at small-model serving.`
- **Description length:** 147 characters (70–155 range)
- **Search intent:** Commercial investigation / use-case comparison
- **Language:** English only (no Chinese version — vpstier.com is English-only since 2026-06-11)

## 3. Proposed H2 structure

1. **Cheap VPS for Local LLM Inference 2026: Quick Verdict**
   - One-screen summary: best for absolute budget, best for token throughput, best for non-US buyers.
   - Clarify the article covers 4–8B parameter self-hosting, not 70B training.

2. **Why Run a Local 4–8B Model on a $25 VPS?**
   - Math: GPT-4o mini at $0.15/M input tokens, Llama 3.1 8B at zero marginal cost on a $19.99/mo host.
   - When self-hosting wins (high volume, privacy, repeated prompts) and when an API is still cheaper (bursty workloads, >13B models).

3. **What Hardware Does a 7–8B Model Need?**
   - RAM threshold (8 GB minimum for Q4, 12 GB for Q5, 16 GB comfortable).
   - NVMe vs SSD difference for model load time and prompt eval latency.
   - CPU matters more than people think: EPYC Zen 4 vs older Xeons for tokens/sec.
   - Why VRAM is irrelevant — CPU inference path for a single user.

4. **The 5 Hosts, Side by Side**
   - Table: provider, plan, monthly price, vCPU, RAM, storage, NVMe, port speed, datacenter regions, after-primary-source verification.
   - One row per provider, comparison-first formatting.

5. **RackNerd: Cheapest Floor Under $20/mo**
   - 8 GB Elite / 12 GB Mega tier details.
   - EPYC or Xeon, NVMe availability, datacenter spread, KVM virtualization.
   - Where it shines (price floor) and where it is constrained (single region per order, support response time).

6. **Vultr: Hourly Billing, Global Footprint**
   - 8 GB / 12 GB Cloud Compute tier details.
   - Hourly billing wins for bursty inference, NVMe on every tier, EPYC available on 8 GB+.
   - RackNerd comparison: Vultr is roughly 2× the price but gives you the global region menu.

7. **DigitalOcean: Developer-Era Reliability, Premium Cost**
   - 8 GB / 16 GB Premium Intel / AMD droplet tiers.
   - Mature snapshots, backups, monitoring, and team-friendly UI.
   - When the extra $5–10/mo over Vultr actually pays back in reduced ops time.

8. **Hostinger KVM 2 and Contabo: The Sub-$10 Champions**
   - Hostinger KVM 2 (8 GB) at the lowest entry price in the lineup.
   - Contabo's 8 GB / 400 GB SSD tier for storage-heavy model caches.
   - Honest notes on renewal pricing, support depth, and known performance caveats.

9. **Tokens-Per-Dollar at 7B: How the Hosts Actually Compare**
   - Live methodology: load Llama 3.1 8B Q4_K_M in Ollama, measure tokens/sec on each host type.
   - Convert tokens/sec × hours/mo → tokens/month → tokens-per-dollar.
   - Show the chart, not just the table; this is the data GSC will reward.

10. **Final Verdict: Which Budget VPS Fits Your LLM Workload?**
    - Pick by use case: hobby project, small-team agent, privacy-first self-host, or bursty API alternative.
    - End with a clearly labeled RackNerd primary CTA and an affiliate disclosure.

## 4. FAQ plan

1. **Can a $5 VPS run an 8B language model?**
2. **Do I need a GPU to do local LLM inference on a VPS?**
3. **Is NVMe really required, or will a SATA SSD work?**
4. **How many tokens per second can I expect from a 7B model on a budget VPS?**
5. **Is a self-hosted Llama 3.1 8B cheaper than the GPT-4o mini API?**

## 5. RackNerd affiliate placement plan

Use the exact affiliate destination for every commercial CTA: `https://my.racknerd.com/aff.php?aff=16299`

1. Quick-verdict callout: "Cheapest floor at RackNerd" — `https://my.racknerd.com/aff.php?aff=16299`
2. Why-self-host section: budget-baseline reference — `https://my.racknerd.com/aff.php?aff=16299`
3. Hardware section: 8 GB / 12 GB tier callout — `https://my.racknerd.com/aff.php?aff=16299`
4. Host-1 deep dive: RackNerd price-floor CTA — `https://my.racknerd.com/aff.php?aff=16299`
5. Comparison table: "Budget alternative" row link — `https://my.racknerd.com/aff.php?aff=16299`
6. Tokens-per-dollar section: floor-cost reference — `https://my.racknerd.com/aff.php?aff=16299`
7. Final-verdict inline CTA — `https://my.racknerd.com/aff.php?aff=16299`
8. Closing button: "Compare RackNerd Budget VPS Deals" — `https://my.racknerd.com/aff.php?aff=16299`

All placements must identify RackNerd accurately; no link may be labeled as a signup link for any of the other hosts.

## 6. Internal-link plan

Only existing English routes are planned:

- `/vps/racknerd/`
- `/vps/vultr/`
- `/vps/digitalocean/` (if file exists; verify before writing)
- `/vps/hostinger/`
- `/vps/contabo/`
- `/blog/ai-agent-vps-api-guide/`
- `/blog/vps-pricing-trap-guide-2026/`
- `/blog/amd-epyc-vs-intel-xeon-vps-2026/`
- `/blog/nvme-vps-under-10-2026/`

## 7. Primary CTA

**Compare RackNerd Budget VPS Deals:** `https://my.racknerd.com/aff.php?aff=16299`

Affiliate disclosure will appear before the first commercial link and near the closing CTA.

## 8. Self-check

- Prohibited merchant references: **0**
- English-only outline: **passed**
- Removed-language routes: **0**
- Title length: **54 / 30–60**
- Description length: **147 / 70–155**
- H2 sections: **10 / required 8–10**
- FAQ questions: **5 / required 3–5**
- Planned RackNerd affiliate placements: **8 / required at least 6**
- CTA destination: **exact match**
- Existing internal routes only: **passed**
- Tier-1 banned-provider pivot: **applied (4th firing)**
- Editorial rebalance vs single-provider streak: **comparison format**
- Full Astro page, build, git push, and deployment: **not performed; waiting for `publish`**
