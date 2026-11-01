# Run Record — vpstier daily outline — 2026-11-01

**Cron ID:** `5fd2a36f2dc4` (vpstier-daily-outline, `45 9 * * *`)
**Run date:** 2026-11-01
**Outline produced:** `drafts/outline-2026-11-01-vpstier-daily.md`
**Slug:** `ai-managed-vps-2026-managed-vs-self-hosted`
**Status:** `outline_pending_publish` — stopped before Astro/build/deploy, awaiting user `publish`
**Model:** MiniMax-M3.1-Flash via minimax-cn

---

## 1. Variant adjudication

**Variant-0 — briefing SUCCEEDED (2026-11-01 08:07) with 3 vpstier items; 1 selected, 1 rejected as a standing re-surface, 1 rejected as off-shape + published-angle collision.**

| # | Briefing item | Verdict | Gate that fired |
|---|---|---|---|
| 1 | ⭐ MassiveGrid cancels its LET "lifetime price guarantee" (LowEndBox 2026-10-28) | **REJECTED — angle already published + merchant not whitelisted** | `lifetime-vps-deals-2026-real-cost-vs-marketing.astro` (live, 10 H2) already owns the lifetime/annual pricing-model space and already carries a dated lifetime-deal hook. The merchant is **absent from `providers.json`** (0 of 65) → no `/vps/` profile, no cross-link target. **Third consecutive run** this item has been offered (10-30, 10-31, 11-01) — rejected every time, never rescued. |
| 2 | Hostinger uses three years of store data to argue against the Black Friday myth (hostinger.com blog, 2026-10-30) | **REJECTED — off-shape (e-commerce data, not VPS) + published-angle collision** | The data is about **online stores selling physical goods** (2.02× → 1.77× daily order multiple; BF week = ~11% of quarter orders; median established store ~1% of quarter orders on BF; a third or more sold nothing on BF). It is not about VPS capacity, pricing or provider behaviour. The VPS seasonal-pricing lesson is already owned by the published `2026-black-friday-cheap-vps-under-25.astro` (10 H2, incl. *Black Friday VPS Timeline & What to Expect*, *Renewal Trap Depth Comparison*) and the queued `cheap-vps-back-to-school-promo-eval-2026` (2026-09-16). Also a vendor publishing its own store analytics to argue its own promo timing — self-promotional framing, not an independent finding. Retained as a §2 supporting datapoint only. |
| 3 | ⭐ Hostinger has put Hermes Agent / OpenClaw / Paperclip on the market as managed, hosted applications | **SELECTED** | Whitelisted provider (`hostinger`, in `providers.json`), body-verifiable across 5 vendor primaries, and the angle is genuinely new — see §3. |

---

## 2. The briefing's framing of item #3 was wrong — and correcting it produced the article

This is the substantive finding of the run and is worth stating plainly, because it is the kind of error that a less careful pass would have written straight into an article.

The briefing cited **Hostinger's Week 43 product-updates post** (`hostinger.com/blog/product-updates-week-43-2026/`) as evidence that "Hostinger has launched hosted Hermes Agent / OpenClaw / Paperclip VPS", and described the **navigation bar** as the proof.

**Fetching the Week-43 body shows it ships five unrelated features** — AI Builder SSR one-click migration, Anti-DDoS events in the dashboard, PDF attachments in Hostinger Reach prompts, Reach form analytics, a larger Ecommerce CSV importer, and LP Express bulk label export — **and never mentions the agent products in its body at all.** The strings "Hermes", "OpenClaw" and "Paperclip" appear only in the site-wide navigation, which every Hostinger page carries. The briefing citation was a nav-bar reading presented as a launch announcement.

**The real story is larger than the briefing described and is fully verifiable from Hostinger's own pages:**

1. **Four managed application products** — Managed Hermes Agent, Managed OpenClaw, Managed Paperclip and Managed n8n — all on **one shared plan** ("AI automation apps — One plan, any AI automation app. Switch anytime.").
2. **A separate AI-managed VPS category** at `/ai-managed-vps` — a genuine KVM product line with published specs (1–8 vCPU, 4–32 GB RAM, 50–400 GB NVMe, 4–32 TB bandwidth) whose differentiator is an embedded AI agent that *operates* the server, while the buyer keeps **root**.
3. The vendor itself treats these as a **fork**, not a synonym: the product pages carry a side-by-side "Managed Hermes Agent / Hermes Agent on VPS" table with genuinely different rows (root access; who owns SSL, updates and firewall).

The article's spine came from a fact the briefing did not have: the Hostinger changelog's **2026-06-09 "Free subscription migrations now available"** entry, which supports migrations between Managed Hermes, OpenClaw **and VPS hosting** for eligible customers. That single clause **removes the lock-in objection** that would otherwise be the strongest argument for self-hosting — and it inverts the site's existing vendor-lock-in red-flag material. A mainstream budget host is now voluntarily reducing switching cost in the new agent-hosting category.

---

## 3. Source-verification ladder actually executed

| Source | Result | Bytes |
|---|---|---|
| `hostinger.com/blog/product-updates-week-43-2026/` (briefing's cited source) | HTTP 200 | 274,447 — **body does not contain the claimed launch** |
| `hostinger.com/managed-hermes-agent` (**vendor primary**) | HTTP 200 | 564,218 |
| `hostinger.com/managed-openclaw` (**vendor primary**) | HTTP 200 | 541,814 |
| `hostinger.com/managed-paperclip` (**vendor primary**) | HTTP 200 | 523,958 |
| `hostinger.com/ai-managed-vps` (**vendor primary — the category page**) | HTTP 200 | 808,067 |
| `hostinger.com/ai-automation-apps` (**vendor primary — shared plan**) | HTTP 200 | 1,545,827 |
| `hostinger.com/self-hosted-n8n` (**vendor primary — the 4th app**) | HTTP 200 | 811,668 |
| `hostinger.com/ai-agents` | HTTP 200 | 634,547 — nav-link inventory |
| `hostinger.com/changelog` (**vendor primary — launch timeline**) | HTTP 200 | 1,522,565 (raw HTML) |
| `hostinger.com/sitemap.xml` (**vendor primary — page inventory**) | HTTP 200 | 288,714 — surfaced `/ai-managed-vps`, `/applications/*`, `/managed-*` |
| `hostinger.com/blog/black-friday-as-a-season/` (rejected candidate) | HTTP 200 | 312,695 |
| `lowendbox.com/blog/massivegrid-when-the-lifetime-price-guarantee-...` (rejected candidate) | HTTP 200 | 157,006 |
| `racknerd.com/` (affiliate facts re-verification) | HTTP 200 | 34,042 |
| `news.google.com/rss/search?q="Managed Hermes Agent" Hostinger` (dated corroboration) | HTTP 200 | 6 items |
| `news.google.com/rss/search?q=Hostinger managed agent hosting` (dated corroboration) | HTTP 200 | 37 items |
| `news.google.com/rss/search?q=VPS hosting news` (cluster scan) | HTTP 200 | 68 items |

**Changelog parsing note:** the changelog's rendered page flattens to a structure of `TITLE BODY CATEGORY DATE` (the **date follows** the entry, not precedes it). A date-first regex silently mis-attributes entries. Worked around by splitting the flattened text on the date regex and matching the trailing category token against the body — 43 date-pair entries parsed, covering 2026-05-05 → 2026-07-15. This is the same class of parse-ordering bug as canonical pitfall #30 (fixed line-index assumptions) and is worth remembering for any future vendor-changelog run.

**Also tried and failed:** `hostinger.com/hosting/hermes-agent` (404), `hostinger.com/hosting/openclaw` (404), `hostinger.com/hosting/managed-paperclip` (404), `hostinger.com/blog/hostinger-ai-automation-applications/` (404), `hostinger.com/blog/sitemap.xml` (1,212 bytes — effectively empty), `racknerd.com/ai-vps/` (500), `racknerd.com/vps/` (404).

---

## 4. Fact bundle (28 rows, every one traced to a body-fetched source)

Full table is in the outline's §1d. Headline figures, all live-fetched 2026-11-01:

- **Managed app plan: $21.99 → $4.99/mo, 24 months prepaid ($119.76), renews at $11.99/mo.** A **2.40× renewal cliff**, ≈ **+$84 over a term**. Identical on all four managed app pages — one price point, no per-app tiers.
- **AI-managed VPS KVM tiers:** KVM 1 $19.49 → $6.49/mo (renews $11.99, **1.85×**), KVM 2 $24.49 → $8.79 (renews $14.99, **1.71×**), KVM 4 $42.99 → $12.99 (renews $28.99, **2.23×**), KVM 8 $73.99 → $25.99 (renews $49.99, **1.92×**).
- **Launch timeline from the vendor changelog:** Managed Hermes released **2026-06-09**; free migrations between Managed Hermes / OpenClaw / VPS **2026-06-09**; API-key rotation for Managed OpenClaw and Hermes **2026-07-07**; OpenClaw + Hermes bundled under one plan **2026-07-15**.
- **Managed vs VPS split:** managed = preinstalled template, built-in AI credits, built-in Telegram pairing, visual UI, "Security SSL, update and firewall — managed by us", container isolation + custom security gateway, 200+ models, cron scheduler, subagents, persistent memory, 6 messaging channels, **no root**. VPS = full root, self-managed firewall/DDoS.
- **Agent counts:** "10,000+ Hermes Agents already launched" / "100,000+ agents already deployed" (OpenClaw).
- **RackNerd (affiliate) live facts:** "VPS from $2.24 /mo", 20 datacenter locations; site's own profile: $1.99/mo entry, root access + KVM virtualization, $50–100/sale.

**Facts deliberately NOT asserted:** that managed hosting suits any workload; that the AI-managed VPS replaces root; that the free migration applies to every customer (changelog says "eligible"); that Hostinger Agent can do anything a sysadmin can; that the 10,000+/100,000+ counts are paying subscribers (the pages do not say).

---

## 5. Content-gap verification

Pre-write grep over **all 61** published blog `.astro` files, **all 169** draft `.md` files and **all 69** `/vps/` profile pages:

```
AI-managed VPS              -> 0 / 0 / 0
ai-managed-vps              -> 0 / 0 / 0
Hostinger Agent             -> 0 / 0 / 0
managed Hermes              -> 0 / 0 / 0
Managed OpenClaw            -> 0 / 0 / 0
Managed Paperclip           -> 0 / 0 / 0
AI automation apps          -> 0 / 0 / 0
managed n8n                 -> 0 / 0 / 0
AI Web Terminal             -> 0 / 0 / 0
agentic AI hub              -> 0 / 0 / 0
application hosting         -> 0 / 0 / 0
migration between           -> 0 / 0 / 0
```

**Adjacent-queue neighbours are all distinct (related-article ≠ block):**
- `agentic-vps-always-on-ai-agent-2026` (2026-09-10, queued) — covers *whether* you need a server and how to size one; its H2s are "What 'Agentic' Actually Changes About Your Hosting", "Always-On Is the Feature, Not the Size", "The Six Hosts Worth Considering", "Running Your First Always-On Agent". It has **no managed-application-hosting angle at all** — the token probe for `managed Hermes` / `Managed OpenClaw` / `AI automation apps` returns 0 against it. This new piece asks the *opposite* question: a vendor is now selling the managed version — do you buy it, and at what renewal price?
- `best-vps-for-ai-agents-2026` (2026-08-14, queued) — a 7-provider comparison; its H2 #7 is "Best Managed/Hands-Off: Hostinger & HostArmada — turnkey agent panels / managed wrappers, one-click deploys". That is a **provider-comparison** angle. This new piece is a **category** angle: two products from one vendor, a decision boundary, and a renewal cliff. Distinct enough to proceed, and the queued piece is excluded from cross-links because it has no live `.astro` file.
- `2026-black-friday-cheap-vps-under-25.astro` (published) — the seasonal-pricing angle, which is why briefing item #2 was rejected as a collision.
- `lifetime-vps-deals-2026-real-cost-vs-marketing.astro` (published) — the lifetime/annual pricing-model angle, which is why briefing item #1 was rejected.
- `vps-pricing-trap-guide-2026.astro` (published) — already owns the renewal-cliff mechanic **for VPS hosts**. This article applies the same mechanic to a **new category** (managed application plans), where the cliff is 2.40× and where the vendor's own migration clause inverts the usual lock-in argument. Not a duplicate — an extension — and the article links the existing piece rather than restating it.

**Slug collision:** `ai-managed-vps-2026-managed-vs-self-hosted` is absent from `published[]` (84 entries), `drafts[]` (56 entries) and `src/pages/blog/` (61 files).

**Pre-existing queue defect (not today's work, flagged for the user):** `published[]` ∩ `drafts[]` = `['best-vps-deals-codes-2026', 'webdock-vps-review-2026']` — two slugs are queued for republication while already live. Left untouched (not today's deliverable).

---

## 6. Measurements

| Gate | Value | Limit | Result |
|---|---|---|---|
| Title | 50 | 30–60 | PASS |
| Description | 149 | 70–155 | PASS |
| H2 sections | 10 | 8–10 | PASS |
| FAQ | 5 | 3–5 | PASS |
| RackNerd CTA placements | 8 | ≥6 | PASS |
| Cross-links (all targets verified on disk) | 9 | — | PASS |
| Excluded-merchant token count in this document | 0 | = 0 | PASS |
| CJK character count in this document | 0 | = 0 | PASS |
| Deprecated language-prefix path in prose | 0 | = 0 | PASS |
| Fact rows with a source cell (§1d) | 28 | — | PASS |
| Briefing items adjudicated | 3 | — | PASS |
| Sources body-fetched at HTTP 200 | 16 | — | PASS |

**Title budget note:** vpstier's `BaseLayout.astro` renders `<title>{title}</title>` verbatim — **no auto-suffix** (re-verified 2026-11-01 by reading line 18 of `src/layouts/BaseLayout.astro`; the opposite of apirank's layout, which appends ` | APIRank`). Bare string length is the final length.

**Cross-link verification:** all 9 target paths confirmed present on disk. Four queued-but-unpublished neighbours were deliberately excluded to avoid dead paths: `agentic-vps-always-on-ai-agent-2026`, `best-vps-for-ai-agents-2026`, `cheap-vps-back-to-school-promo-eval-2026`, `vps-ssh-security-host-key-checks-2026`.

**Affiliate-label integrity:** all 8 RackNerd CTA placements identify RackNerd as the affiliate; none is attached to the provider under review (Hostinger).

**Language policy:** English-only. No deprecated language-prefix path appears in the outline or this record. (The two stale pre-2026-06-11 carry-over files in `drafts/` and in the deprecated language-prefix source tree were left in place — they are a separate cleanup item, not today's deliverable.)

**Publish cadence:** vpstier publishes Mondays only since the 2026-08-28 HCU pause → publish slot **2026-11-02**.

---

## 7. Operational note — sibling cron failures (not this run's blocker)

`jobs.json` shows several sibling crons in `last_status: error` with `Error code: 404 - The model 'qwen/qwen3.6-2...'` (jobs `537976c317e8`, `c49b9d5fb6aa`, `e5feb8292369`, `516d24492295`). This is the retired-fallback-model class of failure (canonical pitfall #36): a model retired upstream in the fallback chain takes down every cron in the profile that touches it. `/root/.hermes/config.yaml` now lists `kimi-for-coding` / `kimi-coding-api` as the fallback provider rather than the retired groq model, so the configuration appears already amended — but the failures recorded in `jobs.json` are the residue of the earlier window. **This run's cron (`5fd2a36f2dc4`) completed normally**; its own `last_status` error entry is a *reporting* artifact (the job's stored error text is the outline report body, not a model error — the same false-positive shape as canonical pitfall #35). No action taken on the sibling crons from this run, but flagging it for the weekly strategy report.

---

## 8. Commits (two-commit pattern)

- Commit 1: `git add drafts/outline-2026-11-01-vpstier-daily.md drafts/run-record-2026-11-01-vpstier-daily-outline.md` → `feat(drafts): ...`
- Commit 2: `git add drafts/state.json` → `chore(state): ...`

Never `git add -A` — the vpstier repo accumulates orphan files from prior runs and a blanket add would bundle them.
