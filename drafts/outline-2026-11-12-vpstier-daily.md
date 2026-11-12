# Outline: Railway Breach 2026: The $740,000 API Key Heist

**Date:** 2026-11-12
**Slug:** `railway-breach-2026-740k-api-key-heist`
**Author / Cron:** vpstier-daily-outline (`5fd2a36f2dc4`)
**Variant:** variant-13 (briefing SUCCEEDED, zero usable vpstier stars; substituted the freshest dated, body-verifiable story found **outside** the briefing via the same feeds the briefing reads)
**Archetype:** secret-store breach / credential-blast-radius buyer-guide (NEW on vpstier — no published article or queued outline covers *secret-store* compromise, *API-key blast radius*, or *why an AI credential is worth more than a database password*)
**Status:** `outline_pending_publish` — awaiting user `publish`

---

## 1. Rationale + Hot-Source

### 1a. Briefing item triage (2026-11-12 08:16 UTC, cron `3ea88f8bb2d0`) — all 3 vpstier items fail a hard gate

The briefing itself succeeded (its report is intact inside the delivery wrapper — the `last_error` field wraps report text, not a real failure; canonical pitfall #35). All three vpstier items fail a gate:

| # | Briefing item | Verdict | Reason |
|---|---|---|---|
| 1 | A European dedicated-hosting merchant's production server offline for 3 days after a boot-disk swap, no ETA, no out-of-band access (r/VPS post `1xslvbf`, updated 2026-11-10T12:39:45Z) | **REJECTED — hard-banned merchant + off-shape subject** | The merchant is a permanently excluded brand, so its name must not appear in the outline (canonical pitfall #53). Independently, the subject is a **dedicated server**, not a VPS — off-ICP for this site. Body was fetched via the Reddit Atom route (HTTP 200, 3,407 B) so the facts are known, but the topic is unusable either way. |
| 2 | A gaming-focused host's 2GB KVM offer at $1.83/mo first year ($87.96 → $43.99 → $21.99 price ladder), LowEndBox 2026-11-11 | **REJECTED — captured by a published article** | The same merchant's renewal cliff (a 2GB Ryzen plan at $2/mo in month 1, $8/mo on renewal — a 4x markup) is already the worked example inside the live `vps-pricing-trap-guide-2026` article, which names the brand in four places including a price table row. This is a **re-surface of a story the site already published**, and the merchant is not in `providers.json`. As a headline it is also off-shape: it is a pricing-model story the site has covered. |
| 3 | A 14-location budget host at $2.39/mo for 4GB KVM/NVMe Gen4, LowEndBox 2026-11-09 | **REJECTED — non-whitelisted + no dated hook** | Not in `providers.json` (65 providers checked). No dated incident, no failure mechanism — it is a plain product listing. Off-shape for a buyer-guide. |

**Consequence: zero usable stars → variant-13.** The substitute was sourced from the same feeds the briefing reads, using a `when:` date-window sweep (canonical pitfall #54) and body-fetched from the vendor's own disclosure.

### 1b. Substitute selected — the Railway breach (vendor primary + a 20-outlet cluster)

**Why this one.** It is the strongest dated story available on 2026-11-12 that vpstier has never covered, and it is the **first time the site's readers are the actual target of the story**.

| Gate | Result |
|---|---|
| Freshness | ✅ Vendor's final incident report published **2026-11-10 14:00 UTC** (d-2); the $740,000 figure was covered by 20+ outlets across **2026-11-10 → 2026-11-12** (d-0/d-1/d-2). Cluster still moving (the vendor's report is the tail). |
| Body-verified | ✅ **Vendor primary fetched whole and parsed**: `blog.railway.com/p/incident-report-october-security-incident` (HTTP 200, 108,389 B, `datePublished` 2026-11-10T14:00:00.000Z, "Last updated: November 10, 18:02 UTC"). Also fetched: the preliminary report (2026-10-22, 78,972 B), the first disclosure (2026-10-21, 36,509 B), and five vendor remediation runbooks (2026-10-22). |
| Independent corroboration | ✅ The Hacker News 2026-11-11 (174,644 B), Wiz "Black October" (2026-10-30, 454,513 B), plus BleepingComputer / TechRadar / Cloud Computing News / CyberSecurityNews / iTnews / MLQ.ai / Mezha.net / 2-Spyware / GBHackers / The 420.in / Business Upturn / news.lavx.hu / iTnews / FourWeekMBA / Meteora Web — all titles+dates confirmed via Google News RSS. |
| Non-merchant subject | ✅ Railway is a platform-as-a-service, **not** in `providers.json` — selectable without a whitelist gate (canonical variant-10). |
| Banned merchant | ✅ 0 — the brand is not printed anywhere in this outline or the run record. |
| Slug uniqueness | ✅ 0 hits on disk / `published[]` / `drafts[]` / `recent_topics[]`. |
| Published-angle collision | ✅ cleared — see §3. |
| Queued-outline collision | ✅ cleared — see §3. |

### 1c. The angle: the secret store, not the server

This is **not** a "provider got hacked, rotate your password" story. Three things make it new on vpstier, and all three are facts only the vendor's own report carries:

1. **The breach started in the build system, not the customer-facing one.** The attacker's first move was a **previously unknown vulnerability in the build infrastructure** that let them **partially escape filesystem isolation** and read files on the host virtual machine. Railway's build infra ran multiple builds "in full isolation from each other, on the same virtual machine" — so a shared-host escape existed *inside a hosted platform that sells isolation as a feature*.
2. **The credential that leaked was a build credential with a much wider blast radius than its stated purpose.** The credential was "intended to authorize only work needed to complete builds, such as registry pushes, and nothing else" — but Railway's internal Temporal instance "accepted it as a trusted client", so the attacker could call APIs intended for a Temporal client elsewhere and read the stored histories of **other builds**. A scoped credential that a shared internal service trusted as privileged became a lateral-movement primitive.
3. **The target was not the customer. The target was the customer's AI credentials.** Railway parsed the attacker's own database queries: "the attacker had begun creating a swarm of accounts as early as October 18th", and the queries "were specifically for AI credentials", believed to be "passed on to distributed transfer stations for use for distillation". **$740,000** of unauthorized spend on stolen keys followed.

**The reader-side inversion (the article's real thesis):** the VPS buyer reads this as "a hosting company got breached". But the actual exposure is the **keys the buyer's application reads at runtime** — the OpenAI/Anthropic/OpenRouter key in a `.env` file on a $22/year box. A VPS compromise is recoverable in an afternoon; a leaked **AI provider key** has no rotation-until-you-notice window, bills against a prepaid balance, and (per OpenRouter's own policy as relayed by the vendor) may not be refundable at all. **The blast radius of a cheap VPS is not the VPS.** That is the sentence the article is built to deliver, and it is the reason a VPS *review site* — not a security blog — should run it.

### 1d. Fact table (every row traced to a body-fetched primary)

| # | Fact | Value | Source (fetched this run) |
|---|---|---|---|
| 1 | Incident report published | 2026-11-10 14:00 UTC, last updated 18:02 UTC | vendor incident report (108,389 B) |
| 2 | Attacker's first signups | **October 18th** — two days *before* the page that opens the timeline | vendor report, "Customer impact" |
| 3 | First entry point | 07:28 UTC Oct 20 — a **previously unknown vulnerability in the build infrastructure** that "partially escape[d] filesystem isolation" | vendor report, "First entry point" |
| 4 | Detection | 13:58 UTC Oct 20, via anomalous registry API calls | vendor report + preliminary report |
| 5 | Full eviction | 09:24 UTC Oct 21 | vendor report |
| 6 | Builds halted (twice) | 17:03 UTC Oct 20 and 07:22 UTC Oct 21 | vendor report |
| 7 | Sessions/tokens invalidated | 20:19 UTC Oct 21 | vendor report |
| 8 | Builds restored for all plans | 22:49 UTC Oct 22 | vendor report |
| 9 | Decryption window | 04:42 → 07:14 UTC on Oct 21 (**2h32m**) | vendor report, "Customer impact" |
| 10 | Workspaces affected | **at most 1.85%, about 100,000** — logs "identify a subset of environments, not individual variables, so that figure is an upper bound" | vendor report |
| 11 | Build histories read | **353 builds**, sealed variables included, between 13:50 and 15:30 UTC Oct 20 | vendor report |
| 12 | Linked-account tokens reset | **1,852 users** (BYOK agent keys + GitHub OAuth tokens); "no logins to Railway accounts using credentials taken in this incident" | vendor report |
| 13 | **Unauthorized spend on stolen keys** | **~$740,000** | vendor report |
| 14 | Providers asked to revoke (from 09:25 UTC Oct 21) | GitHub, GitLab, Anthropic, OpenAI, OpenRouter, SpaceXSI, Google, Stripe — Railway sent **hashes of every key it held** to isolate blast radius | vendor report |
| 15 | Attack tooling | attacker used **abliterated models** (no safeguards); a harness "similar to ARTEX, according to Wiz" | vendor report (cites Wiz) |
| 16 | Attacker account swarm | began Oct 18; earlier attempts "were thwarted via our automated systems" | vendor report, "Attack intent" |
| 17 | Encryption design | per-environment key, itself encrypted by a **root key held in an upstream cloud KMS that "cannot leave the key management service"** | vendor report, "Customer impact" |
| 18 | Running deployments | **not affected** — "existing deployments continued to run" | vendor preliminary report FAQ + incident report |
| 19 | New signups paused | 2026-10-22 19:06 UTC → reopened **2026-11-02**; support tooling restored Oct 26 | vendor report, "Prioritizing existing users" |
| 20 | Notification-delay reasoning | providers notified *before* users; "Broad strokes notification ... produced **1-2 orders of magnitude influx of traffic** which delayed recovery" | vendor report, "User Notification Timelines" |
| 21 | Refund policy per vendor | AWS Bedrock **and** Google Gemini: existing fraud policy covers it, refunds initiated. OpenAI **and** SpaceXSI: case-by-case support bridge. Anthropic: under discussion — **Railway covering costs itself**. OpenRouter: **enforcing its no-refund policy — Railway covering all costs itself** | vendor report, "Unauthorized token spend" |
| 22 | Earlier policy conflict | Railway told customers on Oct 26 it was "unable to refund customers for spend performed with compromised API keys"; by Nov 10 it says it will "backstop" uncovered costs — **a public reversal** | THN 2026-11-11 (quotes the Oct 26 wording) + vendor report |
| 23 | Post-incident hardening | each build now gets a **dedicated ephemeral VM** + a registry-push-only credential; CI rebuilt with **2FA approval and biometrics**; short-lived just-in-time credentials; **Project Glasswing** access obtained with US Treasury approval | vendor report, "Railway security updates" |
| 24 | Industry context | **at least nine AI developer platforms** disclosed incidents in October: Fireworks AI (Oct 6), Andromeda (Oct 9), Zeabur (Oct 14), Lightning AI (Oct 15), OpenCode (Oct 16-17), Railway (Oct 20), Warp (Oct 23), CommandCode (Oct 28), Northflank (Oct 30); plus Brev, Trigger.dev, Chainstack, kernel.sh, Blacksmith, Tensorlake, NEAR AI | Wiz, "Black October" for AI Developer Platforms, 2026-10-30 (454,513 B) |
| 25 | Campaign framing | "All public reports highlight targeted exploitation, explicitly hunting stored environment variables, with a focus on those granting AI access." | Wiz, same article |
| 26 | Cloud-provider template | Railway's own docs carry a "Compare to VPS" page and "Migrate to VPS" guide — the platform itself positions VPS as the alternative | railway.com/docs nav (fetched) |
| 27 | Railway's model today | usage-priced PaaS: Free $0, Hobby $5 min, Pro $20 min, Enterprise "Dedicated VMs"; plus "Sandboxes & VMs" for agents/builds | railway.com/pricing (297,474 B) |
| 28 | Affiliate's live entry price | **VPS from $2.24/mo**; specials ladder 1 GB $21.99/yr, 2 GB $35.99/yr, 4 GB $59.99/yr, 6 GB $89.99/yr, 8 GB $119.99/yr; dedicated from $139/mo; 20 datacenters | racknerd.com + racknerd.com/specials (34,042 B / 87,951 B) |
| 29 | Affiliate's product shape | **KVM VPS** with full root, own control panel — the opposite of a shared secret store; no managed secret vault in the product line | racknerd.com/specials |
| 30 | Affiliate CTA framing | RackNerd is the **"the key lives on a machine you control, and the machine is a full KVM VM you root"** alternative to a managed platform's encrypted-variable store. True advice, not a stretch — same integrity class as the 2026-11-06 KVM-vs-Xen case | derived from #28/#29 |
| 31 | Live GSC (90d, `sc-domain:vpstier.com`) | homepage absorbs **901 of 1,185 impressions (76.0%) at avg position 84.8**; every head term ("best vps provider", "best vps", "vps hosting review") sits at **pos 74-95**; the best-performing pages are provider reviews at pos 3.6-7.4 | live GSC API this run (`gsc_daily_report.py` helpers) |
| 32 | Weekly strategy report (2026-11-09) | vpstier: **+1 article, 36 impressions, 0 clicks, avg pos 85.1**; flag raised as 🟡 the provider-page pipeline is still dead (69 vps pages but only 18 with any impressions); external-link target recommended: LowEndTalk / HN Ask HN | cron `537976c317e8` weekly report |

### 1e. Editorial anchor + HCU preview

- **Anchor:** the vendor's own sentence — *"We believe the credentials were passed on to distributed transfer stations for use for distillation"* — paired with the operational fact that the exposed secret was an **AI provider key**, not a database password.
- **Artifacts (≥2 required, all body-fetched this run):** (a) the vendor's incident report with its timestamped entry/eviction/revocation timeline; (b) the **$740,000** figure and the per-provider refund matrix (six providers, six different outcomes); (c) the **353 builds** and **1,852 tokens** counts; (d) the **nine-platform October cluster** from an independent research house; (e) the live RackNerd specials ladder with today's prices.
- **First-person voice:** required. I will state plainly what I checked, what I could not verify, and why the $740,000 figure is an *estimate* rather than a confirmed loss.
- **"Last verified 2026-11-12"** stamp on every fact table.
- **No comparison-crutch template:** the piece must not read as "we tested X vs Y". It is a mechanism explainer + a buyer checklist.

---

## 2. Slug / Title / Description

| Field | Value | Gate |
|---|---|---|
| **Slug** | `railway-breach-2026-740k-api-key-heist` | unique — 0 hits on disk / `published[]` / `drafts[]` / `recent_topics[]` |
| **Title** | `Railway Breach 2026: The $740,000 API Key Heist` | **47 / 60** chars (Python `len()`, computed — not asserted) |
| **Description** | `Railway's October breach exposed $740,000 in stolen AI API keys across up to 100,000 workspaces. Here is how to shrink your own secret blast radius.` | **148 / 155** chars (Python `len()`, computed — not asserted) |

*Lengths verified by running `len()` on the final strings above before this row was written (canonical pitfall #22/#44 — compute, then write the number).*

---

## 3. H2 Chapter Plan (10 sections)

1. **The $740,000 headline, and the number underneath it** — open with the two figures that define the story: **~$740,000** of unauthorized spend on stolen keys, and **at most 1.85% of workspaces, about 100,000**. Immediately state the honesty caveat the vendor itself states: the logs "identify a subset of environments, not individual variables, so that figure is an **upper bound**". Then the arithmetic a VPS owner can actually use: **~$7.40 per affected workspace** of direct spend, on top of the credential's resale value, which is the number that matters. Close the section with the three smaller counts that no headline carried — **353 build histories**, **1,852 reset linked-account tokens**, and **8 providers** asked to revoke at 09:25 UTC on Oct 21 — and the one negative finding that should reassure without reassuring too much: running deployments never went down.

2. **Where the attacker actually came in — and it was not the login form** — the first entry point in detail. A **previously unknown vulnerability in Railway's build infrastructure** let the attacker "partially escape filesystem isolation" and read files on the **host virtual machine**. Explain why that is a different threat model from a normal hosting breach: the build system ran "multiple builds ... in full isolation from each other, on the same virtual machine" — i.e. **a shared-host escape inside a platform whose product is isolation**. Timeline anchors: first probing 06:50 UTC Oct 20 → exploit 07:28 UTC → detection 13:58 UTC via anomalous registry calls → full eviction 09:24 UTC Oct 21. Note the vendor's own framing: "This was not a single breach followed by a single fix ... a contest of agent speed."

3. **The scope mismatch that made a scoped credential lethal** — the analytical centrepiece. The leaked credential was "intended to authorize only work needed to complete builds ... and nothing else", but Railway's internal Temporal instance "accepted it as a trusted client", so the attacker could "call APIs intended for a Temporal client, elsewhere" and read the stored histories of **other builds** — including environment variables and secrets passed to those builds. This is the transferable lesson and the article's spine: **a credential scoped to one job becomes a lateral-movement primitive the moment any shared internal service trusts it as privileged.** Add the multi-tenant dimension: one compromised build host, many unrelated customers' secrets in the history store. Then the **2h32m** decryption window (04:42 → 07:14 UTC on Oct 21) as the reason the number is bounded but large.

4. **Why an AI API key is worth more than your database password** — the reader-facing reframe, and the reason a VPS buyer should care. The vendor's forensics: the attacker "had begun creating a swarm of accounts as early as **October 18th**" — two days before the exploit — and the queries were "specifically for AI credentials", believed to be "passed on to **distributed transfer stations for use for distillation**". Explain the buyer's economics: an AI provider key is a **metered prepaid balance** with no per-request authentication beyond the key itself, no IP binding, no challenge — it bills against a prepaid credit balance and (per OpenRouter's policy as relayed by the vendor) "a leaked key spends your prepaid credits directly". Contrast with a database password: rotatable, scoped, and — in Railway's own design — protected by a per-environment key whose root "cannot leave the key management service". Put the buyer question plainly: **what is the worst thing a stranger can do with each secret I left on that box?**

5. **The refund matrix — six AI providers, six different answers** — a genuinely useful, hard-to-elsewhere table, and a section no other outlet wrote. From the vendor's own report: **AWS Bedrock** — existing fraud policy covers it, account teams have initiated refunds. **Google Gemini** — same, refunds initiated. **OpenAI** — open a support request and pass the Case ID; reviewed case-by-case on a shared bridge. **SpaceXSI** — contact Railway, case-by-case bridge. **Anthropic** — under discussion; **Railway is covering breached key costs itself** in the interim. **OpenRouter** — enforcing its **no-refund** Terms of Service policy; **Railway is covering all costs itself**. Then the catch: Railway told customers on **October 26** it was "unable to refund customers for spend performed with compromised API keys" — by **November 10** it says it will backstop uncovered costs. That public reversal is the honest headline of the section: **in a credential-theft incident, the refund policy is a negotiation, and it can change weekly. Buy accordingly.**

6. **Nine platforms in one month — this is a campaign, not an incident** — the industry-scale section, and the reason a single-provider checklist is not enough. Independent research house Wiz published "Black October" for AI Developer Platforms on **2026-10-30** documenting **at least nine** AI developer platforms disclosing incidents in October: Fireworks AI (Oct 6), Andromeda (Oct 9), Zeabur (Oct 14), Lightning AI (Oct 15), OpenCode (Oct 16-17), Railway (Oct 20), Warp (Oct 23), CommandCode (Oct 28), Northflank (Oct 30) — plus Brev, Trigger.dev, Chainstack, kernel.sh, Blacksmith, Tensorlake and NEAR AI. Their shared pattern: "All public reports highlight targeted exploitation, explicitly hunting stored environment variables, with a focus on those granting AI access." Note that Zeabur **shut down** as a result and one platform's incident is traced to an SGLang remote-code-execution vulnerability exposing cloud API keys in logs. **Reader takeaway: assume the attacker class is targeting AI credentials across your entire stack, and that the platform you chose may be one of the next nine.**

7. **What the vendor changed afterwards — and the one fix that matters most to you** — hardening, read as buyer guidance rather than vendor PR. The headline change is the right one: **each build now gets a dedicated ephemeral VM** with a credential scoped to pushing a single OCI image, and "the shared systems exploited by the attacker are no longer in use". Also: CI rebuilt with **2FA approval and biometrics**, short-lived just-in-time credentials, a full service-account privilege audit, and **Project Glasswing** access obtained with US Treasury approval. But be honest about what this does and does not tell a reader: this is **one provider's** remediation of **one** attack vector. It is not evidence that your own setup is safe. That distinction is the whole point of the section — the reader must leave with **their own** checklist, not with reassurance about someone else's fix.

8. **Your 60-minute secret-blast-radius audit** — the practical centrepiece, and the part the reader will screenshot. Five blocks, each with a concrete command or a concrete place to look:
   - **8a — Inventory.** List every AI-provider key that exists on the box *right now*: `grep -rIl 'sk-\|api_key\|API_KEY' /srv /home /opt 2>/dev/null`, then `printenv | grep -i key`. The question is not "do I have a key" — it is "how many copies of it exist, in how many places, on how many machines".
   - **8b — Rank by blast radius, not by convenience.** For each secret, ask: *if this leaked, what does the stranger get, and who pays?* An AI provider key = a metered balance + model access. A DB password = a database. A deploy token = your whole pipeline. Put the AI keys at the top of the rotation list.
   - **8c — Find the copies.** The Railway breach read **353 build histories** — the secret that lived in a config file also lived in a CI log, a build artefact, a `.env.example`, a shell history, a screenshot in a chat app, and a wiki page. For each key: `grep -rn '<first-8-chars-of-key>' <your repo and CI logs>`.
   - **8d — Rotate in the right order.** Revoke first, then replace (a revoked key is dead immediately; a replaced key on a live service may still be the one in the log). Where a provider offers a "disable but keep history" option, use it so you can audit spend afterwards. Then redeploy — and note the ordering trap from the incident: **a credential you rotate while the build path is down leaves you unable to redeploy**, which is exactly how a credential rotation turns into an outage.
   - **8e — Make the audit repeatable.** A monthly cron that greps for live-looking key prefixes and diffs against your secret store, plus a documented rotation order for each provider. Include the alert rule: **watch spend, not just failure** — the OpenRouter runbook's own tell is "your credit balance dropped without a matching change in your traffic", and OpenAI's is "your spend rose without a matching change in your traffic". A key theft shows up as *spend*, long before it shows up as *error*.

9. **Choosing a host where the blast radius is smaller** — the buyer-guide section that earns the affiliate placement honestly. The contrast is architectural, not brand-versus-brand:
   - On a **managed platform's** encrypted variable store, a single shared-internal-service trust mistake can expose many customers' secrets at once — the vendor's own words: "each environment separately encrypts its environment variables using a per-environment encryption key that is itself encrypted by a root key in our key management service", and that root key "cannot leave the key management service". The design is sound; the 2026-10-20 failure was an **isolation escape in the build path**, i.e. a different layer, and it reached the variables anyway.
   - On a **rooted KVM VPS you control**, the secret's blast radius is bounded by what you put on the box. There is no shared variable store to escape, no build-service credential to lateral-move with, no central secret manager holding a root key on your behalf. **You are the isolation boundary** — which sounds like a burden until you realise it is also the thing that makes a compromise containable.
   - The honest counterweight (state it, or the section reads like a shill): **a rooted VPS means you are the one who has to keep the keys off the box correctly.** A managed store gives you encryption-at-rest and rotation tooling you would otherwise build yourself. The trade is real; say so.
   - Then the concrete recommendation: if you are running an AI workload with a paid provider key, **a dedicated KVM VPS with its own disk, its own key, and its own rotation cadence** is the lower-blast-radius choice — and if you need somewhere to put the workload, today live entry pricing is **$2.24/mo**, with an annual specials ladder from **$21.99/yr (1 GB)** up to **$119.99/yr (8 GB)**, across **20 datacenters**, full root on a modern control panel. *(RackNerd affiliate placement — see §5.)*

10. **What we could not verify, and what we would still check** — the trust section, and mandatory for a piece this size. State the limits honestly:
    - The **$740,000** figure is the vendor's **estimate** of unauthorized spend ("was estimated to reach ~$740,000"); it is not a confirmed loss and the incident report carries a **"Last updated: November 10, 18:02 UTC"** stamp, so it may still move.
    - The **1.85% / ~100,000** workspace figure is an **upper bound** by the vendor's own statement.
    - The attacker was **never identified publicly**; Railway filed a complaint with the FBI's IC3 and engaged a specialist forensics firm whose "investigation is ongoing". **No claim is made here about who did it.**
    - The **ARTEX** harness comparison is **attributed to Wiz**, not asserted by the vendor.
    - Independent outlets' bodies were **not all fetched** — the corroborating cluster is outlet + title + date, and the article says so explicitly rather than implying we read 20 articles.
    - **What we would still check** before acting: whether your provider's own incident history has changed since this run, and whether the "disable but keep history" option exists for your provider (it does not for all).

---

## 4. FAQ (5 questions)

1. **Should I rotate my API keys just because of the Railway breach?** — Only if you actually stored an AI provider key on Railway. If your keys live on a VPS you control and were never in a managed variable store, this incident is a reason to audit, not to panic-rotate. The vendor's own recommendation to pre-October-21 Railway users was to rotate; that advice does not transfer to people who were never on the platform. What transfers is the *method*: inventory, rank by blast radius, revoke-then-replace, redeploy last.
2. **If my AI provider key leaks, will I get the money back?** — Sometimes, and it depends entirely on the provider's fraud policy and on whether you notice. Of the six providers the vendor names: two (AWS Bedrock, Google Gemini) applied existing fraud policies and initiated refunds; two (OpenAI, SpaceXSI) reviewed case by case; one (Anthropic) was still under discussion with the vendor covering costs in the interim; and one (OpenRouter) enforced its **no-refund** policy, with the vendor covering the loss. Railway itself told customers on Oct 26 it "was unable to refund" and reversed that position by Nov 10. Treat the refund as a *negotiation you may lose*, and set a spend alert so you catch it in hours rather than weeks.
3. **Does this mean shared hosting and managed platforms are unsafe?** — No, and saying so would be dishonest. This was one provider, one attack vector (a build-path isolation escape), and one month. The vendor reports that "each of the attack vectors used during the incident has been remediated" and that per-environment keys with a KMS-held root are a sound design. What the incident does show is that **"the platform manages my secrets" is a trust decision with a blast radius, not a free safety upgrade** — the root key "cannot leave the key management service", but the credentials it protects were reachable through a path nobody was guarding at the time.
4. **How much does this cost me if it happens to me?** — Directly, the vendor's own numbers give a rough per-victim figure: **~$740,000 across at most ~100,000 workspaces ≈ $7.40 per affected workspace** of direct spend, plus whatever the stolen key was worth on the resale market it was routed to ("distributed transfer stations for use for distillation"), plus your time. Add the outage risk from rotation ordering and the direct answer is: **it is a low-dollar, high-annoyance incident for an individual, and an existential one for the platform** — which is why the platform disclosed in this much detail.
5. **What should I change first on my own VPS?** — Inventory every AI-provider key on the box, rank by what it grants, find the copies (the secret in your `.env` is also in your CI logs, your build artefacts, your shell history and your chat apps), revoke before you replace, then redeploy last. And turn on a spend alert on every AI provider account — the two most reliable tells of a stolen key are "your spend rose without a matching change in your traffic" and "your credit balance dropped without a matching change in your traffic". Both are *spend* signals, not error signals.

---

## 5. RackNerd Affiliate CTA Placements (8 — minimum 6 required)

All placements use `https://my.racknerd.com/aff.php?aff=16299`. Each is written to be **true advice in context**, not a bolt-on — the affiliate's own product line (rooted KVM VPS, full root, own control panel) is the concrete instance of the section-9 architecture.

| # | Placement | Section | Framing (honest, mechanism-level) |
|---|---|---|---|
| 1 | H2 #9 opening — "the lower-blast-radius choice" | 9 | "If you want the secret's blast radius bounded by one machine you control, that machine can be a full KVM VPS you root." → affiliate link. |
| 2 | H2 #9 — price line | 9 | Live entry pricing **$2.24/mo**; specials ladder **$21.99/yr (1 GB)** → **$119.99/yr (8 GB)**; 20 datacenters. → affiliate link. |
| 3 | H2 #9 — the isolation-boundary argument | 9 | "You are the isolation boundary" — rooted KVM, own disk, own key, own rotation cadence. → affiliate link. |
| 4 | H2 #8d — rotation-order / redeploy point | 8 | "Rotate first, then redeploy last" — and if you rotate on a box whose build path is broken, you lose the ability to redeploy; a separate machine you control avoids that coupling. → affiliate link. |
| 5 | H2 #8b — "one key per machine" rule | 8 | A dedicated KVM VPS per workload is how you make "which key lives where" answerable. → affiliate link. |
| 6 | H2 #9 — the honest counterweight | 9 | "A managed store gives you rotation tooling you would otherwise build yourself" → "or you build it yourself on a box you control." → affiliate link. |
| 7 | H2 #8a — inventory anchor | 8 | "If you want to check the inventory yourself instead of trusting a dashboard, you need shell access to the machine holding the keys." → affiliate link. |
| 8 | H2 #10 — "where we would still check" | 10 | Verifiable live pricing and a readable specials page, so the reader can check today's numbers rather than trust ours. → affiliate link. |

**Affiliate-label integrity note (verified this run):** RackNerd's live product line is **rooted KVM VPS with full root access and its own control panel** — `racknerd.com/specials` (87,951 B) shows no managed secret vault and no shared variable store. The article's advice ("bound your secret's blast radius to a machine you control") is therefore *literally true* of the product being recommended, and the recommendation is the article's genuine conclusion rather than a reverse-engineered justification. Prices quoted are **live today** ($2.24/mo entry; $21.99–$119.99/yr specials ladder) — not the stale figure that appears on the site's own `/vps/racknerd/` page (see §7 flag).

---

## 6. Cross-Links (8 — all targets verified to exist on disk this run)

| Target | Path | Why it links |
|---|---|---|
| `vps-pricing-trap-guide-2026` | `/blog/vps-pricing-trap-guide-2026/` | the site's existing renewal-cliff/pricing-trap piece — the reader who came from a deal post needs this one too |
| `dreamhost-breach-2026-password-reuse-vps` | `/blog/dreamhost-breach-2026-password-reuse-vps/` | the site's prior credential-exposure article — this piece is the *secret-store* sequel to the *password-reuse* one |
| `cheap-vps-local-llm-inference-2026` | `/blog/cheap-vps-local-llm-inference-2026/` | self-hosting an LLM is the natural alternative to paying a leaked provider key |
| `ai-agent-vps-api-guide` | `/blog/ai-agent-vps-api-guide/` | the site's AI-agent-on-VPS guide; the API-cost section connects directly to the $740,000 figure |
| `vps-buying-guide` | `/blog/vps-buying-guide/` | the general buyer path, for readers who want the full checklist rather than this incident |
| `racknerd-deep-review-2025` | `/blog/racknerd-deep-review-2025/` | the affiliate's full review — the article recommends the product, so the review must be one click away |
| `hosting-account-suspension-blast-radius-2026` | *(queued outline, 2026-11-02)* | sibling blast-radius piece — **account-level** suspension vs **secret-level** blast radius. Cross-link at publish time once that outline ships; do not link a non-existent URL now |
| `januscape-kvm-escape-vps-security-2026` | *(queued outline, 2026-07-16)* | sibling escape piece — **host-side isolation escape** vs **platform build-path isolation escape**. Cross-link at publish time; do not link a non-existent URL now |

**Link-integrity rule for the writer:** 6 of the 8 are live URLs verified on disk this run. The 2 marked *queued outline* are **not yet live** — the writer must add those anchors only if and when those articles exist, otherwise link to the sibling by title in prose without an href.

---

## 7. Self-Check (Pre-Commit)

| Check | Result |
|---|---|
| Banned-merchant zero | ✅ 0 occurrences of the excluded brand in this outline or the run record. Described by category only ("a permanently excluded budget/dedicated-hosting merchant"), never by name — including in the §1a triage row (canonical pitfall #53). |
| Banned-token self-reference | ✅ The self-check row is written generically; no banned literal appears inside the check description (canonical pitfall #2 / #48 — 6 prior recurrences). |
| English only | ✅ 0 CJK characters. No Chinese-version outline, no deprecated language-prefix path written anywhere (canonical pitfall #29 - describe the check generically, never print the literal). |
| Title length | ✅ **47 / 60** — computed with Python `len()` on the final string, not asserted (canonical pitfall #22/#44). |
| Description length | ✅ **148 / 155** — computed with Python `len()` on the final string. |
| Slug uniqueness | ✅ `railway-breach-2026-740k-api-key-heist` — 0 hits on disk, in `published[]`, in `drafts[]`, in `recent_topics[]`. |
| H2 count | ✅ 10 sections (requirement: 8-10). |
| FAQ count | ✅ 5 questions (requirement: 3-5). |
| RackNerd CTAs | ✅ 8 placements, every one pointing at `https://my.racknerd.com/aff.php?aff=16299`. |
| Cross-links | ✅ 8 targets — 6 live URLs verified on disk this run, 2 queued outlines flagged as publish-time-only (no dead hrefs). |
| Body-grep-0 capture check | ✅ `railway`, `distillation`, `740,000`, `740000`, `env var`, `token spend`, `llmjack`, `secret store`, `build system`, `isolation escape`, `mcp server`, `pentest`, `api key theft` → 0 hits across `src/pages/blog/` and `src/pages/vps/` (1 hit for `paas` in a single unrelated review). No published article or provider page covers this mechanism. |
| Published-angle collision | ✅ cleared against the 3 nearest neighbours — see below. |
| Queued-outline collision | ✅ cleared against the 3 nearest queued outlines — see below. |
| Affiliate-label integrity | ✅ the affiliate's live product line (rooted KVM VPS, own control panel, no managed secret store) genuinely answers the article's question; prices verified live today, not from the stale provider page. |
| Body-verified facts | ✅ every number in §1d traced to a body-fetched primary; the four bounded claims (§10 of the H2 plan) are labelled as estimates/bounds, not presented as settled facts. |
| GSC grounding | ✅ 90-day live GSC pulled this run: homepage absorbs **76.0% of impressions at pos 84.8**; head terms sit at pos 74-95. The article is written as a *specific-mechanism* piece because the site's head-term gap is structural, not a reason to force a listicle. |
| Pre-existing repo state | ✅ 2 tracked files already modified before this run (`src/pages/blog/dreamhost-breach-2026-password-reuse-vps.astro`, `tsconfig.json`) — **left untouched, not staged**. 25+ untracked orphan drafts — **left untouched**. Defensive `git add` of specific paths only; no `git add -A` (canonical pitfall #11). |

### Collision discrimination (nearest neighbours — cleared, not assumed)

| Axis | `dreamhost-breach-2026-password-reuse-vps` (published 2026-11-02) | This outline |
|---|---|---|
| **Secret type** | **Human passwords** (email/FTP/SFTP reset as a precaution) | **Machine API keys** (AI provider credentials) |
| **Failure mechanism** | third-party software vulnerability in a **file-manager server** | **isolation escape in a build path** + trusted-client scope failure |
| **Who is exposed** | account holders whose credentials may have been exposed | the *customer's downstream AI providers'* balances |
| **Action** | rotate a password | rotate a metered prepaid key, rank by blast radius, alert on spend |
| **Cost dimension** | none | **$740,000**, refund-negotiation matrix, resale value |

| Axis | `januscape-kvm-escape-vps-security-2026` (queued 2026-07-16) | This outline |
|---|---|---|
| **Escape layer** | KVM **guest-to-host** escape in the hypervisor | **platform build-path** filesystem-isolation escape in a PaaS |
| **Who owns the vulnerable code** | the hypervisor vendor | the PaaS vendor |
| **What's at risk** | the host kernel | **the customer's secrets**, fetched via a lateral-movement primitive |

| Axis | `hosting-account-suspension-blast-radius-2026` (queued 2026-11-02) | This outline |
|---|---|---|
| **Blast radius type** | **account-level** — one complaint, everything on the account goes dark | **secret-level** — one key, an unbounded metered balance |
| **Trigger actor** | provider-initiated action (legal notice) | an external threat actor |
| **Control** | you can move to another account | you can revoke one credential |

| Axis | `vps-pricing-trap-guide-2026` (published) / briefing item #2 | This outline |
|---|---|---|
| **Axis** | **price** (intro vs renewal) | **credential blast radius** |
| **Overlap** | briefing item #2 is the *same story the site already published* — rejected as a capture, not merely as an overlap | — |

---

## 8. Flagged for the user (not fixed from a daily-outline slot)

1. **`src/pages/vps/racknerd.astro` shows a stale price.** The provider page renders "starting at **$1.99/mo**" in the `<title>`, the meta description, the intro paragraph, the pros list and the CTA area — while the **live** RackNerd site says **VPS from $2.24/mo** (verified this run, `racknerd.com` 34,042 B). This article quotes only the live figure. The provider page needs a separate price-refresh commit; **do not edit live pages from a daily-outline run.**
2. **`published[]` ∩ `drafts[]` overlap = 2 slugs** (`best-vps-deals-codes-2026`, `webdock-vps-review-2026`) — a duplicate-queue landmine for the publish cron (canonical pitfall #39).
3. **Two live articles assert a Black Friday launch window that the primaries do not support** (flagged again on 2026-11-11; the Nov 9 piece is internally contradictory — "two weeks away" while naming a window 8 days past). Needs a publish-slot fix; not touched here.
4. **The vpstier provider-page pipeline is still dead** (weekly report, 2026-11-09): 69 `/vps/` pages but only 18 with any impressions; the homepage absorbs 76.0% of impressions at position 84.8. Two queued provider-review jobs have not run since June.
