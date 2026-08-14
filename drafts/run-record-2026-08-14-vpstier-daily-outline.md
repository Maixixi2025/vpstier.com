# VPSTier Daily-Outline Run Record — 2026-08-14 (Friday)

## Outcome
- **New outline:** `drafts/outline-2026-08-14-vpstier-daily.md` → slug `best-vps-for-ai-agents-2026`
- **Deliverable:** 7-provider AI-agent VPS comparison / buyer-guide, English only (LANG policy).
- **state.json:** 1 new `outline_pending_publish` entry appended (drafts 24 → 25); `last_run` = 2026-08-14;
  `publish_notes` schema-drift-safe appended (string → 2-element list).

## Topic decision
- **Briefing (`3ea88f8bb2d0`) FAILED** 2026-08-14 with `'reasoning_content' is unsupported` HTTP 400 — the same
  intermittent failure (8-06/8-08/8-09/8-11/8-12/8-13/8-14 fail; 8-10 success). Confirmed by reading the day's
  output file (not assumed from prior days).
- **GSC (2026-08-14 07:00):** vpstier's only 2 queries: `how to deploy ai agent on vps` (rank 75) and
  `ovh backup vps` (rank 49). The latter is **captured** by queued `ovhcloud-vps-review-2026` → not re-picked.
- **Pick: `how to deploy ai agent on vps` → `best-vps-for-ai-agents-2026`.** The 8-13 run judged this
  signal "covered by ai-agent-vps-api-guide," but that article is the **API/Ollama-tutorial** angle, NOT a
  7-provider selection page. Its own H2s prove the gap (Provider recs inside an API-strategy piece vs a
  dedicated comparison with a decision table).
- **Orphan index-card fix:** `blog/index.astro` has a card for `best-vps-for-ai-agents-2026` (June 10,
  "7 Providers Tested") with NO `.astro` on disk and NO `state.published[]` entry → writing it resolves the
  phantom/dead URL (ilang-content orphan-backlog/hygiene rule). Also cross-linked from 2 queued outlines.
- **News cluster verified via Google News RSS (not subagents):** Cybernews "Best VPS for AI Agents in 2026"
  (Jul-24), Hostinger "Getting started with Paperclip" (Aug-13), autogpt.net Hermes self-host (Jul-20),
  TechRadar OpenClaw self-host (Apr-01) + Cybernews AI-VPS family (Ollama/DeepSeek/ChatGPT/n8n hosting guides).

## Validation (script-measured)
- Title `Best VPS for AI Agents 2026: 7 Providers Compared` = **49 chars** (30–60 ✅)
- Description = **135 chars** (70–155 ✅)
- H2 sections: 10; FAQ: 4; RackNerd CTA placements (explicit §5 list): 6 (inline CTA mentions: 11)
- Banned-merchant name in whole draft (case-insensitive grep): **0** ✅
- CJK chars: **0** ✅; `/zh/` refs: 2 (self-documentation audit lines, 8-09/8-10 precedent) ✅
- All 7 providers whitelisted in `providers.json`; internal links all on disk (verified)

## Git discipline (two-commit, per ilang-content)
- Branch: `main` (confirmed via `git branch --show-current`).
- Committed ONLY today's files (outline + run-record), then state.json in a separate commit; did NOT `git add -A`
  the accumulated untracked outline/run-record backlog from 8-01→8-13 (flagged below, not swept).

## On-hold / open items
1. **Uncommitted backlog in `drafts/`** (pre-existing, NOT from this run): outline-8-01/8-03/8-04/8-05/8-07/
   8-12/8-13 + run-record-8-03/8-04/8-05/8-07/8-12 .md files are untracked. Per the converter-epub 8-07 lesson,
   a working-tree reset would destroy these. Recommend a separate cleanup commit (user decision).
2. **Large pending-outline queue (25 drafts, 22 outline_pending_publish).** User is the publish-gate. This run
   appends one entry. Recommend publishing `best-vps-for-ai-agents-2026` first (fixes live phantom card).
3. **`ovh backup vps` GSC signal** — captured by queued `ovhcloud-vps-review-2026`, not re-picked.
4. **AI-agent framework guides queued** (`agent-zero-vps-setup-guide-2026` 7-18, `cloudflare-markdown-for-agents`
   7-19) — publish order: provider-picker → framework guides, complementary set, no duplicates.
