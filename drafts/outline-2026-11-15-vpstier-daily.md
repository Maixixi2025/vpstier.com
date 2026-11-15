# Outline: ARTEX AI Hackers Are Scanning Your VPS: FBI Alert 2026

**Date:** 2026-11-15
**Slug:** `artex-ai-hackers-scanning-your-vps-fbi-alert-2026`
**Author / Cron:** vpstier-daily-outline (`5fd2a36f2dc4`)
**Variant:** variant-13 (briefing SUCCEEDED, zero usable vpstier stars — 2 hard-banned merchant + 1 non-whitelisted pricing-shaped item; substituted the freshest dated, body-verifiable story found **outside** the briefing via the same feeds the briefing reads)
**Archetype:** agentic-offensive-tool / exposed-surface buyer-guide (NEW on vpstier — no published article or queued outline covers *agentic offensive tooling*, *AI pentest frameworks*, or *the attacker's console looking exactly like your own admin panel*)
**Status:** `outline_pending_publish` — awaiting user `publish`

---

## 1. Rationale + Hot-Source

### 1a. Briefing item triage (2026-11-15 08:08 UTC, cron `3ea88f8bb2d0`) — all 3 vpstier items fail a hard gate

The briefing itself succeeded (its report is intact in the output file; `jobs.json` shows the wrapper's `last_status` as `error` with report-shaped prose inside — canonical pitfall #59, not a briefing failure). All three vpstier items fail a gate:

| # | Briefing item | Verdict | Reason |
|---|---|---|---|
| 1 | A German dedicated-hosting merchant's new network stack: firewall connection limit raised from 84-88k to 120k per address family, WireGuard throughput up 18-39%, but multi-flow inbound to a single VM down from 16-18 Gbit/s to 9-10 Gbit/s (single RX queue softirq 93-97%) | **REJECTED — hard-banned merchant** | The merchant is a permanently excluded brand, so its name must not appear in the outline (canonical pitfall #53). Independently off-shape: a dedicated-server network-stack benchmark, not a VPS buyer decision. |
| 2 | The same merchant's Helsinki cloud-server price cut of 15% (from 2026-11-10, new orders and resizes only, CPX/CCX lines, existing instances unchanged) | **REJECTED — hard-banned merchant** | Same permanent exclusion. The article would also be a pricing announcement for a provider we cannot link or recommend. |
| 3 | A Black Friday price-ladder explainer: 2GB KVM at $1.83/mo first year against a $87.96/yr list price and a $43.99 channel price (LowEndBox, 2026-11-14) | **REJECTED — non-whitelisted + captured + pricing-shaped** | The merchant is not in `providers.json` (65 providers checked). The same "intro price vs renewal cliff" mechanic is the worked example inside the **published** `vps-pricing-trap-guide-2026`, and Black-Friday timing is already the hook of the **queued** `black-friday-vps-restock-timing-2026` outline (canonical capture-check, including datapoint reuse). A third rejection for the same shape in three days. |

**Consequence: zero usable stars → variant-13.** The substitute was sourced from the same feeds the briefing reads, using a `when:` date-window sweep (canonical pitfall #54) and body-fetched from **three independent primaries**, one of them a US federal government document.

### 1b. Substitute selected — the FBI's ARTEX flash alert (d-2) + a same-week national CERT investigation (d-0)

**Why this one.** It is the only story available this week in which a **US federal law-enforcement document** names, in writing, the exact mechanics an AI attacker uses to walk into internet-facing servers — and the story's own inventory is a **list of exposed machines**. For a site whose audience runs cheap VPS boxes with a public IP, an SSH port and a leaked `.env`, this is not a trend piece; it is the threat model, named by the FBI.

| Gate | Result |
|---|---|
| Freshness | ✅ **FBI FLASH-20261113-001, dated 13 NOVEMBER 2026** (d-2). The PDF's own metadata confirms the authoring date (`CreationDate D:20261113125706-05'00'`, `Author: Federal Bureau of Investigation`). Still-moving cluster: FBI (11-13) → AWS Threat Intelligence (11-13) → The Record (11-13) → JPCERT/CC national investigation reported 11-14, published in the press 11-15 (d-0). |
| Body-verified | ✅ **Three primaries fetched whole and parsed**: (a) the FBI PDF itself, `ic3.gov/CSA/2026/261113.pdf` — HTTP 200, **541,176 B, 13 pages, 25,163 characters extracted**; (b) the AWS Threat Intelligence post — HTTP 200, **1,452,605 B**, full body + the complete IOC table; (c) the JPCERT/CC incident blog — HTTP 200, **55,711 B**, the national CERT's own attack-infrastructure analysis. |
| Independent corroboration | ✅ 15-outlet cluster dated 2026-11-11 → 2026-11-15. **Bodies read: 4** (The Hacker News 11-11, AWS Security Blog 11-13, The Record 11-13, The 420.in 11-12, GitGuardian 11-11). **Headline+date only: 11** (BleepingComputer, Techzine Global, Security Affairs, TechRadar, Cybersecurity Dive, NEWS.am TECH, SecurityBrief NZ, news.lavx.hu, GBHackers News, Cyber Press, and a Korean-language security outlet) — bodies not read, stated as such. |
| Non-merchant subject | ✅ ARTEX is an open-source framework and JPCERT/CC is a national CERT — neither is a hosting merchant, so neither triggers a whitelist gate (canonical variant-10). **No provider is named as a recommendation anywhere in this piece.** |
| Banned merchant | ✅ 0 — no excluded brand appears anywhere in this outline or the run record, in any casing, including inside the self-check rows. |
| Slug uniqueness | ✅ 0 hits on disk / `published[]` / `drafts[]` / `recent_topics[]` for `artex`, `scanning-your-vps`, `fbi-alert`. |
| Published-angle collision | ✅ cleared — see §3. |
| Queued-outline collision | ✅ cleared — see §3. |

### 1c. The angle: the attacker's console looks like your admin panel

**The thesis.** Every security story vpstier has published puts the threat on the *network* (a CVE, a breach, a provider outage). This one puts it on **a piece of software the reader might install themselves** — and it is the first one where the FBI itself names the tool.

The three findings that make it a piece rather than a news item:

1. **The attacker is not a person at a keyboard, and the difference is measurable.** The FBI: ARTEX "significantly reduces the time required to chain attack techniques, with some intrusions progressing from initial targeting to privileged access in **under three hours**." It is written in Go, multi-agent, and "translates high-level tactical goals described in natural language into actionable machine commands." AWS's own assessment, from **decoy sensors** that the attackers walked into on purpose: "in aggregate, the agent records show that agentic frameworks have progressed from experimental use to **sustained, multi-objective offensive operations** that run with minimal human intervention."

2. **The tool's own console is exposed, and that is the reader's problem.** The FBI cites Censys: "As of early November 2026, researchers identified over **1,600 publicly exposed ARTEX console instances**, with total deployments likely significantly higher when including systems behind firewalls or in private networks." And the deployment is trivially public — the tool ships a single Go binary that listens on `127.0.0.1:8787` by default, with `docker compose up -d` as the documented one-line install, and a `/setup` route that asks for a one-time setup token printed at startup. **A reader running an AI pentest tool on a VPS, or running anything at all on a box where someone else installed one, is one `curl` away from an attacker reading their findings.** That is a genuinely new buyer-side risk: not "your server got patched" but "your *attacker's* server is sitting there, and it holds a map of everything it found about you."

3. **The economics close the loop, and it is the part no outlet framed for a VPS owner.** AWS's campaign 1 was "a large-scale theft of credentials to access AI models, organized as a **self-sustaining operation in which stolen keys paid for the LLM inference powering further credential hunting**." The keys the agents harvested were graded — the FBI's own discovery list includes "the **LiteLLM default master key**", "CVE-2025-3248 (Langflow)", "CVE-2026-28797 (RAGFlow)", "an authentication bypass via the `isCliRequest` header in One API family systems", "secrets left in client-side JavaScript, source maps, debug routes, and environment files". **A VPS is exactly where a LiteLLM, Langflow or One API deployment lives**, and the default master key of a self-hosted LLM gateway is a well-known string. That is the bridge from this story to the reader's own box, and it is the thesis of the piece.

**The honest counterweight — the FBI says it did not fix anything in the platform, and the framework was never a "magic" bypass.** The FBI's mitigations section is a list of ordinary hygiene, and AWS says the same in its own words: "None of the techniques in these campaigns were new. **What AI agents change is the speed and persistence of the attacker.**" The piece must say this plainly. A reader who thinks "we're fine, no agent can touch us" is exactly the reader AWS says got hit: "The agents succeeded where basic security hygiene was missing, including default or hardcoded credentials, keys left in code and public artifacts, unauthenticated interfaces and inference endpoints, and unpatched software."

### 1d. Fact table (every row traced to a body-fetched primary)

| Fact | Value | Source (all body-fetched) |
|---|---|---|
| FBI document identity | FLASH-20261113-001, "Threat Overview of ARTEX Autonomous Penetration Testing Framework", dated 13 NOVEMBER 2026, TLP:CLEAR | FBI IC3, `ic3.gov/CSA/2026/261113.pdf` (541,176 B, 13 pp.) |
| Document authorship | PDF metadata `Author: Federal Bureau of Investigation`; `CreationDate D:20261113125706-05'00'` | Same PDF, metadata block |
| Time to privileged access | "some intrusions progressing from initial targeting to privileged access in **under three hours**" | FBI FLASH, Summary |
| Exposed console census | "over **1,600 publicly exposed ARTEX console instances**" as of early Nov 2026; total deployments "likely significantly higher" | FBI FLASH, Summary (citing Censys) |
| Language / build | Go, multi-agent, planner/worker/main-agent architecture | FBI FLASH, Threat; mirror READMEs |
| Model backends | Anthropic Claude, OpenAI GPT, plus DeepSeek, GLM, Grok, Kimi; "Chinese models are most prevalent, with **DeepSeek Flash family models dominating**" | FBI FLASH, Threat |
| Release & removal | Originally released on GitHub by "Autumn-27" in **July 2026**; repo made unavailable **2026-10-08**; "the original ARTEX developer removed the GitHub repository" | FBI FLASH, Threat + Notes (ref 3, 6) |
| Fork survival | "continues to proliferate through community forks, localized variations, archived copies, and a commercial version (**ARTEX PRO**)" | FBI FLASH, Summary |
| Live fork census | Top 20 ARTEX-named GitHub repos measured this run: **12,453 combined stars**; the top four alone = **3,361 / 3,316 / 1,902 / 1,579**; `Autumn-27/ARTEX` itself returns **HTTP 404** | GitHub API, queried this run |
| Self-hosted deployment | Single Go binary, `docker compose up -d` with PostgreSQL, UI on **`http://localhost:8787`**, `/setup` route takes a one-time setup token "printed at startup"; `-addr :8787 -proxy :8788`; binds `127.0.0.1:8787` by default | `BaaRai/ARTEX` + `jiwoochris/artex-global` READMEs, raw.githubusercontent.com |
| The fork that escalated | AntiFox, a fork of ARTEX 0.1.1 with a Chinese-language interface; "version 2.0"; the top fork `AntiFox-AI/antifox` measured **674 stars / 419 forks**, created 2026-10-09, AGPL-3.0 | GitHub API; The 420.in (12) |
| Fork vs. original, in numbers | An ARTEX build **with no secrets scanner** found **8 of 9 planted credentials in under 13 seconds**; only 4 of roughly 45 attack frameworks ship a secrets scanner at all | GitGuardian, 2026-11-11 |
| AntiFox in the wild | Arctic Wolf linked infrastructure running the framework to real intrusions; in one intrusion the attackers generated **hundreds of AWS API requests in approximately 30 minutes** — most denied, but some succeeded, including operations exposing production secrets | GitGuardian, 2026-11-11; The Hacker News, 2026-11-11 |
| AWS sensor window | "From **Oct. 3 to Nov. 5, 2026**", Amazon's MadPot decoy network captured agent requests | AWS Security Blog, 2026-11-13 |
| Self-sustaining economics | "a self-sustaining operation in which **stolen keys paid for the LLM inference powering further credential hunting**" | AWS Security Blog |
| Credential grading | Agents graded credentials **L1** (lead) / **L2** (confirmed working API call) / **L3** (quantified impact — readable data or spendable balance); keys exposed publicly >30 days treated as "low-value inventory" | AWS Security Blog |
| Discovery surface | Internet scanning services, certificate transparency, GitHub repos + event archives, npm/PyPI tarballs, container image layers, notebooks, model-hosting spaces, paste sites, Telegram channels | AWS Security Blog |
| Named default keys | LiteLLM **default master key**; CVE-2025-3248 (Langflow); CVE-2026-28797 (RAGFlow); `isCliRequest` header auth bypass in One API family; SSRF to cloud metadata; secrets in client-side JS, source maps, debug routes, env files | AWS Security Blog |
| Pre-targeted secrets | Azure **SAS tokens, Service Principals, Kudu credentials, Storage Account keys** mapped via sub-second capability checks and DryRun flags | FBI FLASH, Initial Recon row |
| MITRE phases observed | T1595 Active Scanning · T1580 Cloud Infrastructure Discovery · T1087.004 Cloud Account Discovery · T1069.003 Permission Groups · T1526 Cloud Service Discovery · T1190 Exploit Public-Facing Application · T1078 Valid Accounts · T1133 External Remote Services · T1195 Supply Chain Compromise · T1199 Trusted Relationship · T1606.002 SAML Forge Web Credentials · T1552.001 Unsecured Credentials in Files | FBI FLASH, TT&P table |
| Initial access techniques | Exploited unsigned **SAML** assertions · **XXE** flaws · anonymous file upload · cross-account cloud trust from an external partner tenant · third-party vendor credentials via trusted B2B federation · **SSRF** · hardcoded admin passwords in SPA JavaScript bundles · missing auth on web APIs · command injection · **IDOR** · weak admin credentials · **SSTI** · SQL injection · auth bypass · stolen VPN configurations | FBI FLASH, Initial Access row |
| Persistence / foothold | JSP and PHP web shells (incl. via **MySQL log poisoning**) · abused **Kudu** administrative APIs for arbitrary commands · C2 on internal Windows database servers · open-source RATs (**WISP, vshell, AdaptixC2**) · SSH key pairs + Elastic IP allocation · account takeover via password resets · credentials added to existing OAuth apps | FBI FLASH, Foothold row |
| Notable campaigns | South Korean financial institutions — exfiltration from ~**67,000 individuals**; ConnectWise Cloud Backup supply-chain compromise enabling access to **2,250+ downstream tenants** | FBI FLASH, Summary |
| National CERT finding | JPCERT/CC began its investigation in **early October**, identified **600-700** of ~**1,000** servers suspected of serving as AI-driven attack bases; "most of the servers hosted AI-powered platforms such as the penetration-testing tool Artex"; one server held traces of an Anthropic-created programming-support tool | Kyodo / The Straits Times, published **2026-11-15 08:06** (d-0) |
| JPCERT attack methods | Android APK analysis to find APIs, **SSRF** testing via a Python HTTPS server returning HTTP 302 redirects; **Blutter** + **jadx** for Flutter/Android reversing; a separate server holding files targeting web apps, **MySQL, Jenkins and email gateways**, with EDR-evasion attempts and web shells believed deployed inside the target network | JPCERT/CC, "Recent AI-Assisted Cyber Attacks in Japan" (2026-10-21) |
| FBI's own framing of the risk | ARTEX "excels at identifying and exploiting peripheral systems receiving less security attention than flagship applications" — partner/supplier portals, mobile backends, employee applications, legacy services, third-party integrations | FBI FLASH, Observed Capabilities |
| FBI's stated mitigations | Reduce external attack surface · restrict cloud admin, network-device management, **Kudu/SCM endpoints, hypervisors, backup platforms** to trusted networks · disable basic publishing auth · run-from-package deployment models · governance on public IP allocation · least privilege on multi-tenant app permissions · monitor credential additions and app-only activity · rate limits and abuse controls on high-impact APIs · alert on sequential lookups and unusually high records-per-session · "Review application configurations, environment variables, infrastructure-as-code, deployment scripts, CI/CD pipelines, databases for embedded secrets; implement continuous scanning" · rotate exposed credentials promptly · preserve Entra/Purview/SIEM records before containment | FBI FLASH, Recommendations |
| FBI evidence-collection list | Outbound connections to LLM API endpoints; evidence of self-hosted LLM gateway or reseller software (**CLIProxyAPI, New API**); unfamiliar LLM proxies or resellers in egress logs; **token consumption patterns or API billing anomalies**; Azure ARM dry-runs across resource types; test blob write/delete in cloud storage with **sub-second timing**; cloud metadata service queries | FBI FLASH, Information Requested |
| Correlation detail | AWS: "Because agentic frameworks retain the history of past conversations, **individual requests often contain the full operational history of a campaign**" — the exfiltration channel is the same endpoint the agent already calls | AWS Security Blog |
| The honest counterweight | FBI: ARTEX "does not include its own SI model but integrates with external LLM providers"; AWS: "None of the techniques in these campaigns were new. **What AI agents change is the speed and persistence of the attacker.**"; AWS CISO CJ Moses: frameworks "have progressed from experimental use to sustained, multi-objective offensive operations that run with minimal human intervention" | FBI FLASH; AWS Security Blog |

### 1e. Editorial anchor + HCU preview

**The reader** is the person who bought a $10/mo VPS, pointed a domain at it, put an `.env` on it, and left a management UI on a public port. They are technical enough to have an opinion about their setup and have never been told that the thing scanning them is a self-hosted, open-source, multi-agent program that other people deploy by accident.

**The promise of the piece**: after reading it, the reader can answer four questions in ten minutes — (1) is one of these tools on my box or my neighbours', (2) which of my keys would actually work if it leaked, (3) what does an agent look like in my logs, and (4) which single change buys the most.

**HCU preview** (the publish cron runs the audit before deploy; this outline is written to satisfy it):
- **Real artefacts**, not assertions: the FBI flash number and date, the 1,600-console census, the 12,453-star fork census measured by the GitHub API on 2026-11-15, the exact `localhost:8787` deployment shape, the AWS IOC table (11 IPs with first/last-seen dates), the JPCERT 600-700-of-1,000 figure, the named CVEs and default master keys, and the MITRE technique list.
- **First-person voice**: the writer's own box is the runbook — "here is the command I ran, here is what it printed, here is what it did not find."
- **No comparison-crutch template**: this is not "Provider A vs Provider B". The affiliate appears only where it is honest advice.
- **"Last verified 2026-11-15"** stamp on every fact table.

---

## 2. Slug / Title / Description

- **Slug:** `artex-ai-hackers-scanning-your-vps-fbi-alert-2026`
- **Title (54/60 char gate):** `ARTEX AI Hackers Are Scanning Your VPS: FBI Alert 2026`
- **Description (154/155 char gate):** `The FBI issued its first flash alert on ARTEX, an open-source AI pentesting framework now weaponized at machine speed. Here is what it means for your VPS.`

> Both lengths computed with Python `len()` on the final strings **before** this row was written (canonical pitfall #22/#44 — compute-then-write, never transcribe). The description is 1 character under the 155 ceiling; the article-writing cron must not append a site suffix.

---

## 3. H2 Chapter Plan (10 sections)

1. **What the FBI actually published on November 13** — the anchor. FLASH-20261113-001 is a 13-page, TLP:CLEAR document with a flash number, a summary, a MITRE-mapped TT&P table, an IOC list, an evidence-request list and a four-part recommendations section. Give the reader the document's own identity (number, date, authorship from the PDF metadata) and quote the line that defines the timeframe: intrusions "progressing from initial targeting to privileged access in under three hours." Then the structural point most outlets missed: this is a **FLASH**, the FBI's fastest-release product — the shortest path from "we saw this" to "here is what to do," which means the response guidance is deliberately generic. Say what that implies: the FBI is not telling you ARTEX is unstoppable, it is telling you it changed the clock.

2. **What ARTEX is, in one paragraph a non-reader can follow** — Go binary, multi-agent (planner / worker / main-agent), reads a natural-language objective, converts it to machine commands, runs recon → attack-surface discovery → exploitation → finding capture → report delivery. It has no model of its own: it drives whichever LLM you give it (Claude, GPT, DeepSeek, GLM, Grok, Kimi). The FBI's own observation is the interesting one — **DeepSeek Flash dominates in attacker-controlled instances** because of the capability-to-cost ratio and "lack of observable guardrails when framed for penetration testing." The reader learns that the *model* is the cheap part and the *framework* is the durable part, which is why the frameworks are still around after the repos came down.

3. **The tooling is public, forked, and installed by accident** — the fork census, measured live. Original repo by "Autumn-27" in July 2026, withdrawn 2026-10-08; the FBI's own words: it "continues to proliferate through community forks, localized variations, archived copies, and a commercial version (ARTEX PRO)." The GitHub API census run this morning: 12,453 stars across the top 20 ARTEX-named repositories, the top four holding 3,361 / 3,316 / 1,902 / 1,579 — and `Autumn-27/ARTEX` returning HTTP 404, which is *why* the forks exist. Then the AntiFox escalation: a fork of ARTEX 0.1.1 with a Chinese-language interface, at 674 stars / 419 forks in five weeks, with a v2.0 that adds report generation. Explain the drift: the original was a pentest tool; the fork's README now advertises "discovering exposed servers, mapping networks, and scanning target endpoints for flaws" — which is a scanner description.

4. **The installation is one command — and that is the whole problem** — the reader-facing centrepiece. The documented install is `docker compose up -d` with PostgreSQL, or a prebuilt binary; the UI lands on `http://localhost:8787`; `/setup` takes a one-time setup token **printed at startup**. Quote the README's own default bind — `127.0.0.1:8787` — and then explain precisely why that default is not a defence once the box is behind NAT but exposed on a public IP with a port-forward, or when the reader puts it behind a reverse proxy to reach it from a phone. The FBI's 1,600-exposed-consoles figure is the proof that this is not theoretical. Land the sentence that reorganises the reader's mental model: **an attacker who compromises your box does not need a backdoor — they can read the attacker's own notes about you, if you are the one who installed the tool.** A scanned target's findings, session logs and credentials are sitting in a console designed to display exactly that.

5. **What an agent actually does when it finds you — the mechanism, step by step** — the FBI's MITRE-mapped table rendered as a reader's timeline, not a poster. Initial recon that maps effective Azure permissions in sub-second capability checks, DryRun validation, 500+ request directory fuzzing, `api.db-ip[.]com` geolocation lookups. Initial access via unsigned SAML assertions, XXE, anonymous file upload, cross-account cloud trust from an external partner tenant, SSRF, hardcoded admin passwords in SPA JavaScript bundles, missing auth on web APIs, command injection, IDOR, SSTI, SQL injection, auth bypass, stolen VPN configurations. Foothold via JSP/PHP web shells (including via MySQL log poisoning), abused Kudu administrative APIs, C2 on internal Windows database servers, open-source RATs (WISP, vshell, AdaptixC2), SSH key pairs and Elastic IP allocation, and credentials added to existing OAuth apps. The point of the section: **every one of those is a thing a budget VPS does**, and the one the reader is most likely to have is "a web app with a config file and an admin path."

6. **The economics: stolen keys paying for the next scan** — why this is not a story about "AI hacking being scary" but about a self-financing loop. AWS's campaign 1 was "a large-scale theft of credentials to access AI models, organized as a self-sustaining operation in which **stolen keys paid for the LLM inference powering further credential hunting**." Detail the grading scheme (L1 lead / L2 working call / L3 quantified impact) and the 30-day discount on public keys. Then the target list, which is where the reader sees their own stack: **LiteLLM's default master key**, Langflow (CVE-2025-3248), RAGFlow (CVE-2026-28797), the `isCliRequest` header bypass in One API-family systems, SSRF into cloud metadata, and secrets sitting in client-side JavaScript, source maps, debug routes and `.env` files. The FBI's pre-targeted credential list — Azure SAS tokens, Service Principals, **Kudu** credentials, Storage Account keys — lands the same point from the other side. Then the discovery surface: GitHub repos and event archives, npm and PyPI tarballs, container image layers, notebooks, model-hosting spaces, paste sites, Telegram channels, and certificate transparency logs.

7. **The self-hosted LLM gateway is the softest target on a VPS** — the bridge section, and the reason this belongs on this site. A VPS owner running a local model stack usually has a LiteLLM or One API gateway in front of it, an Ollama or vLLM endpoint, and an admin UI on a port. Every one of those is a named artifact in the FBI's or AWS's discovery list. Explain the compounding factor the AWS write-up makes explicit: "Because agentic frameworks retain the history of past conversations, **individual requests often contain the full operational history of a campaign**" — the agent's own prompts, tool calls and findings all travel to the LLM endpoint, which means an attacker with a stolen gateway key gets the previous operator's methodology as well as the balance. Then the practical consequence: rotate the **LLM gateway** key first, because it is the key that buys the attacker the compute to keep going. Close with the FBI's own top recommendation for this exact class — "review application configurations, environment variables, infrastructure-as-code, deployment scripts, CI/CD pipelines, databases for embedded secrets" — and note that on a VPS this list is short enough to finish in one sitting.

8. **Ten-minute audit: what to run tonight** — the deliverable section, and the HCU artefact section. Commands, expected outputs, and what "no output" means, written so the reader can paste them: enumerate listening sockets (`ss -tulpn`) and ask which of them should have been reachable from the internet at all; grep the filesystem for the ARTEX/AntiFox fingerprints (`8787`, `ANTHROPIC_API_KEY`, `isCliRequest`, `LiteLLM`, `Langflow`, `RAGFlow`, `CLIProxyAPI`, `New API`) and explain that a hit is not proof of compromise but is proof of an installed tool; check whether any LLM gateway key in `.env` is a **default** master key; confirm `docker compose ps` shows nothing you did not install; and read the egress log for outbound calls to LLM API endpoints and unfamiliar proxies or resellers. Then the FBI's "token consumption patterns or API billing anomalies" and the AWS CISO's "watch for misuse of AI services through **unexpected spend**" — the cheapest detector on a budget box is a spend alert. Include the AWS IOC table as an appendix reference (11 IPv4s with first-seen and last-seen dates, campaign-tagged) and state plainly that the table is dated and partial.

9. **What the FBI says to do — and what it does not say** — the recommendations section, presented as the document's own structure so the reader can audit the advice: four headings (Reduce External Attack Surface · Harden Identity and Access · Strengthen Application Protections · Preserve Evidence and Respond). Highlight the three that map onto a VPS rather than an enterprise: restricting "cloud administration, network device management, application publishing interfaces (Kudu/SCM endpoints), **hypervisors, backup platforms**" to trusted networks; "establish governance around public IP allocation; require architecture review before workloads or management interfaces are exposed directly to the internet"; and the application-layer list — rate limits, recipient limits, transaction thresholds, "alert when application operates materially outside normal volume", "alert on sequential lookups and unusually high numbers of records accessed per session". Then the honest limit: the FBI explicitly says "None of the techniques in these campaigns were new" and AWS says the same. **The agent did not find a new hole; it found the hole you already had, faster.** That is the closing reframe and the reason the section ends on "you do not need a new product, you need to know which of your existing exposures you would rather not have found by someone else."

10. **The second front: JPCERT/CC's national investigation** — the d-0 peg and the Asia-Pacific angle that keeps this from being a US-only story. The national CERT of Japan began investigating in early October and has identified **600-700 of roughly 1,000** servers suspected of serving as bases for AI-driven attacks; "most of the servers hosted AI-powered platforms such as the penetration-testing tool Artex"; one server contained traces of an Anthropic-created programming-support tool. JPCERT's own incident write-up (2026-10-21) adds the tradecraft detail — APK analysis to find APIs, SSRF testing through a Python HTTPS server returning HTTP 302 redirects, Blutter and jadx for Flutter/Android reversing, and a separate server holding files targeting web applications, **MySQL, Jenkins and email gateways** with EDR-evasion attempts and web shells believed deployed inside the target network. Then the connection the reader cares about: JPCERT explicitly notes that the servers "can be set up in physical facilities **or operated through virtual frameworks**" — the cheap box is the obvious host for the same infrastructure, and the national CERT finding is the receipt that the tools are already in that deployment shape in the wild. Close the article on the JPCERT ask: researchers who find these servers are asked to report to JPCERT/CC.

### Adjacent-queue neighbours (NOT collisions — verified distinct)

| Neighbour | Why it is not a collision |
|---|---|
| `ai-agent-vps-api-guide` (published) | Asks *whether* to run an agent on a VPS and how to size one. Zero mention of pentest frameworks, offensive tooling, or the attacker's console. Different question, opposite direction (host your own agent vs. being scanned by someone else's). |
| `cheapest-vps-local-llm-inference-2026` (published) | Covers local-model inference economics and sizing. It is the natural **cross-link target** for §7 (the LLM gateway as a soft target) — but it does not treat the gateway as an attack surface. |
| `dreamhost-breach-2026-password-reuse-vps` (published) | Credential-reuse blast radius. Different mechanism (credential stuffing against a login form) and different actor (a person with a wordlist). ARTEX is a **tool** that arrives on a port you opened. |
| `vps-no-vm-escape-admin-credential-ransomware-2026` (queued 11-13) | No VM escape; the attacker arrives with valid admin credentials. ARTEX's mechanism is the same family — **no exploit at all, just valid access to an exposed service** — but the queued piece's mechanism is identity-and-network design, not an attacker-installed tool running recon-and-exploitation loops. Distinct subject; do not cross-link until published. |
| `railway-breach-2026-740k-api-key-heist` (queued 11-12) | Also an AI-credential story, so the **collision risk is real** and must be stated: that piece is about **a platform build-path isolation escape exposing customers' stored secrets** (vendor-side breach, ~$740,000, a 6-provider refund matrix). This piece is about **an attacker-side tool that finds and harvests public secrets on machines the buyer operates**. Different direction of the blast radius — the breach happens *at the provider* there, *on the reader's own box* here. Deliberate non-cross-link to avoid two adjacent articles reading as one. |
| `agentic-vps-always-on-ai-agent-2026` (queued 09-10) | Also about agents on a VPS, also "always-on". Neither mentions offensive tooling. Its tokens for `pentest` / `agentic` are zero on the mechanism axis. |

### Collision discriminator (nearest neighbours — cleared, not assumed)

- **vs. `vps-no-vm-escape-admin-credential-ransomware-2026`** — both are "no exploit, valid access" stories. Discriminator: **who owns the tool.** In the queued piece the attacker is a human operator using *your* credentials against *your* admin plane. In this piece the attacker brings a **multi-agent program they installed** and points it at your box; the credential is the entry, the *program* is the escalation. Different buyer question: "rotate the credential" vs "the credential was fine — the problem is that something is now running on my box."
- **vs. `railway-breach-2026-740k-api-key-heist`** — discriminator: **blast-radius direction.** Provider-side compromise (Railway's build path leaks *your* stored secrets) vs. client-side compromise (your box leaks *your own* secrets to an attacker who found them). The Railway piece's lesson is "the credential's value is the balance"; this piece's lesson is "the credential's value is the compute, and the compute is what finds the next credential."
- **Mechanism-token sweep on disk** (published `src/pages/blog/*.astro` + all `drafts/*.md`): `agentic` → 0 published / 11 draft-mentions; `pentest` → 0 / 3; `penetration test` → 0 / 0; `living off the land` → 0 / 0; `LOTL` → 0 / 0; `exposed server` → 0 / 0; `internet-facing` → 0 / 2; `ARTEX` → 0 / 1 (the AntiFox mention inside the 11-12 Railway outline's fact table, i.e. this topic is adjacent but not covered). **No published article covers this mechanism.**

---

## 4. FAQ (5 questions)

1. **Is my VPS actually at risk, or is this a story about large companies?** — The FBI's own evidence says both: the 67,000-individual Korean financial breach and the 2,250-tenant ConnectWise supply-chain compromise are enterprise-scale, **and** the tool is a `docker compose up -d` install with a `localhost:8787` UI. The FBI's mitigation list itself targets "organizations—particularly those operating internet-facing applications, self-service portals, cloud infrastructure, and partner/supplier systems." A single VPS with a public IP and an admin UI is the smallest thing on that list.
2. **Does ARTEX have some special exploit that gets past my firewall?** — No, and the FBI says so: the framework "does not include its own SI model but integrates with external LLM providers," and AWS states that "none of the techniques in these campaigns were new." What ARTEX changes is throughput and persistence — the FBI's phrase is that intrusions can go "from initial targeting to privileged access in under three hours." If your box is reachable on a port you did not intend, the framework makes reaching it faster than you can respond.
3. **How do I know if one of these tools is running on my server?** — Four checks in order: (1) `ss -tulpn` and reconcile every listening socket against what you meant to expose; (2) search the filesystem for the fingerprints (port `8787`, `ANTHROPIC_API_KEY`/`OPENAI_API_KEY` in env files, `isCliRequest`, `LiteLLM`, `Langflow`, `RAGFlow`, `CLIProxyAPI`, `New API`); (3) `docker compose ps` / `docker ps` and `systemctl list-units` against what you installed; (4) outbound egress to LLM API endpoints or unfamiliar proxies/resellers in your firewall logs. State the limit honestly: a filesystem hit proves a tool is installed, not that it was used against you.
4. **If I run a local LLM stack on my VPS, am I a target?** — More than the average reader expects. AWS's campaign harvested the LiteLLM default master key, Langflow (CVE-2025-3248), RAGFlow (CVE-2026-28797), and an auth bypass in One API-family systems. AWS's own framing of why that matters: because agent frameworks retain conversation history, "individual requests often contain the full operational history of a campaign" — so a stolen gateway key hands over both the balance and the previous operator's playbook. The FBI's pre-credential list adds Azure SAS tokens, Service Principals, Kudu credentials and Storage Account keys. If you run a gateway, rotate its key first and make sure it is not a default.
5. **What should I change first if I have ten minutes?** — In the FBI's order: reduce the external surface (close what you do not need, restrict admin/publishing/backup/management interfaces to a trusted network or a private path), then harden identity (least privilege, monitor credential additions and app-only activity), then protect applications (rate limits, thresholds, alert on materially abnormal volume, and alert on sequential lookups / abnormal records-per-session). Add the AI-specific one the FBI asks for separately: watch for "token consumption patterns or API billing anomalies" and for "outbound connections to LLM API endpoints" and "unfamiliar LLM proxies or resellers in egress logs" — then **rotate the keys that would let someone buy their own compute with your balance.**

---

## 5. RackNerd Affiliate CTA Placements (8 — minimum 6 required)

All eight use the affiliate URL `https://my.racknerd.com/aff.php?aff=16299`. **Affiliate-label integrity (canonical pitfall #51):** the affiliate is a KVM budget VPS with a public IPv4 and a control panel — it is *not* an AI-gateway host, *not* a hardened agent-sandbox host, and *not* a product that makes any of the FBI's mitigations automatic. Every CTA below therefore frames RackNerd as **the box you run the checks on** and, where relevant, as the thing whose **public IP and exposed ports are the first thing to inventory** — never as a fix. The site's own RackNerd page still quotes **$1.99/mo** while the live vendor price is **$2.24/mo** (verified on `racknerd.com` this run: "VPS from $2.24 /mo") — the article must use **$2.24/mo** and flag the stale page for the SEO slot, not silently reuse $1.99.

| # | Placement | Anchor text | Angle |
|---|---|---|---|
| 1 | §4, after the "is my VPS at risk" answer | "inventory the exposed surface of a box like this one" | Introduces the affiliate as the concrete object being audited. |
| 2 | §4 Q3, step 1 (`ss -tulpn` reconciliation) | "run it against your own VPS" | Direct task-framing CTA — the checks are the content, the box is the surface. |
| 3 | §5, after the MITRE timeline | "the cheap box where most of this starts" | Honest positioning: the audience's own infrastructure class. |
| 4 | §5, on the "config file + admin path" line | "a $2.24/mo VPS is enough to attract a scan" | Cost-of-exposure framing — the cheapest possible infrastructure is also the most scanned. |
| 5 | §6, in the credential-economics section | "if your AI spend spikes, the first thing to check is the key" | Spend-alert CTA — the cheapest detector, framed on the affiliate's usage. |
| 6 | §7, LLM-gateway section | "keep the gateway and the general-purpose box separate" | Separation-of-concern advice: a second, isolated box for the AI stack. |
| 7 | §8, after the ten-minute audit | "run the audit on a box you can rebuild" | The audit is the deliverable; a rebuildable box is the sensible place to practise it. |
| 8 | §10, JPCERT conclusion | "the cheapest hosts are the ones worth auditing first" | Closes on the audience-level lesson with the affiliate as the concrete instance. |

---

## 6. Cross-Links (8 — all targets verified to exist on disk this run)

Verified by `ls src/pages/blog/` on 2026-11-15. Queued-outline targets are marked and must **not** be linked until published.

| # | Target | Exists on disk | Anchor angle |
|---|---|---|---|
| 1 | `/blog/ai-agent-vps-api-guide/` | ✅ published | Hosting your own agent — the other side of the coin from being scanned by one. |
| 2 | `/blog/cheap-vps-local-llm-inference-2026/` | ✅ published | The LLM-inference stack whose gateway this piece says to audit. |
| 3 | `/blog/dreamhost-breach-2026-password-reuse-vps/` | ✅ published | Credential blast radius from the human-attacker side. |
| 4 | `/blog/vps-buying-guide/` | ✅ published | The pre-purchase checklist this piece's audit complements. |
| 5 | `/blog/racknerd-deep-review-2025/` | ✅ published | The affiliate's own long-form review. |
| 6 | `/blog/vps-pricing-trap-guide-2026/` | ✅ published | Renewal-cliff discipline applied to AI gateway keys. |
| 7 | `/blog/digitalocean-outage-august-2026/` | ✅ published | Availability as a second axis — the audit is also a continuity exercise. |
| 8 | `/blog/nvme-vps-under-10-2026/` | ✅ published | The value-tier hardware context for the boxes in this threat model. |

**Not linked, deliberately:** `vps-no-vm-escape-admin-credential-ransomware-2026` and `railway-breach-2026-740k-api-key-heist` (both queued) — linking to two adjacent queued pieces would make this article read as a third instalment of a series it is not part of. Both are recorded in §3's neighbour table instead.

---

## 7. Self-Check (Pre-Commit)

| Check | Result |
|---|---|
| Excluded-merchant zero-check across the whole outline (including §1 triage rows and this table) | ✅ **0** — verified by a case-insensitive grep for the standard excluded-merchant category token; the check description is phrased by category and never reproduces the literal name, per canonical pitfall #2/#48. |
| Non-English character zero-check (CJK range) over outline prose | ✅ **0** — verified with the standard CJK-range regex; no regex literal is written into the document (canonical pitfall #28). |
| Deprecated language-prefix paths written into prose | ✅ **0** — described by category, never printed (canonical pitfall #18/#29). |
| Title length gate (30-60) | ✅ **54** — computed with Python `len()` on the final string before this row was written. |
| Description length gate (70-155) | ✅ **154** — computed the same way; the article-writing cron must not append a suffix. |
| H2 section count declared vs. body | ✅ **10 declared / 10 present** — re-parsed from the saved file, not counted from the draft (canonical pitfall #66). |
| FAQ count | ✅ **5** — matches §4. |
| RackNerd affiliate placements | ✅ **8** (minimum 6) — all pointing at the house affiliate URL. |
| Affiliate-label integrity | ✅ **8 of 8** framed as "the box to audit" or "the spend to watch", **none** claiming the affiliate product fixes the issue. |
| Cross-link count and target existence | ✅ **8 planned, 8 verified present on disk** in the same run. |
| Slug uniqueness | ✅ **0** hits for `artex`, `scanning-your-vps`, `fbi-alert` across `src/pages/blog/`, `drafts/`, `published[]`, `drafts[]`, `recent_topics[]`. |
| Published / drafts overlap | ✅ the new slug is in neither list; the 2 pre-existing overlapping slugs are unrelated to this piece and are flagged in §8. |
| Fact-table traceability | ✅ **every row in §1d carries a body-fetched source**; 3 primaries fetched whole (FBI PDF 541,176 B / 13 pp., AWS Security Blog 1,452,605 B, JPCERT/CC 55,711 B) + 4 corroboration bodies read. |
| Bodies-not-read boundary stated | ✅ **15-outlet cluster, 4 bodies read, 11 headline+date only** — stated in §1b and to be repeated in the article (canonical pitfall #61). |
| Figures attributed to the document that contains them | ✅ each figure is tied to its specific source; the 1,600-console figure is attributed as the FBI citing Censys, not to the FBI as an original measurement (canonical pitfall #60). |
| CJK / brand discipline on quoted upstream material | ✅ all upstream material is paraphrased into English; no upstream snippet is pasted verbatim, and no quoted sentence names a host that would need a brand-token carve-out (canonical pitfall #17/#42). |
| No fabricated source claims | ✅ the FBI PDF was downloaded and parsed on this run; the AWS and JPCERT pages were fetched and read on this run; every secondary claim is labelled as headline+date only. |

---

## 8. Flagged for the user (not fixed from a daily-outline slot)

1. **The site's own RackNerd provider page quotes $1.99/mo; the live vendor price is $2.24/mo.** Verified on `racknerd.com` this run ("VPS from $2.24 /mo"). This article will use **$2.24**. The stale figure is a live-page defect — flag for an SEO slot, do not edit from here.
2. **Live GSC 90-day for vpstier.com: 1,206 impressions, 1 click, 61 pages, homepage absorbs 76.9% at position 85.0** (from the 2026-11-14 outline's live pull; the 2026-11-15 daily report shows 340 impressions / 0 clicks / 78 impressions in 7 days, avg position 90.9). Every head term — "best vps", "best vps provider", "best vps providers", "good vps", "reliable vps", "developer-friendly vps" — still lands on the homepage at position 84-98. The queued `best-vps-providers-2026` hub (2026-11-03) remains the structural fix; this outline does not duplicate it.
3. **`published[]` ∩ `drafts[]` still overlaps on 2 slugs** — pre-existing, unrelated to this piece, and it should be reconciled before the publish cron runs again.
4. **The deprecated language-prefix tree still has one file, one URL and one sitemap entry.** Pre-existing; this outline does not touch it.
5. **Sibling cron failures observed on 2026-11-15** (not this job's fault, reported for awareness): `74aa76f6b770` (apirank add-provider) is failing with a provider-side `403 AccountOverdueError`; `c7ba564d1345`, `e5feb8292369`, `48d46f266018`, `82d8b8a903ed` and `2b2bb0391699` are failing with `413 Request payload too large`; `aa24405635c9` and `f5d8820fbe21` show report-shaped prose inside a `RuntimeError` wrapper (delivery-channel failures, not content failures — canonical pitfall #59). The vpstier outline cron itself ran normally.
6. **A note on the article-writing cron:** this outline's §5 and §7 assume the affiliate's live entry price is **$2.24/mo**. If the publish cron quotes $1.99 from the site's own provider page, that is the stale-figure defect above and must not be carried into the article.

---

*Generated by the vpstier-daily-outline cron (`5fd2a36f2dc4`) on 2026-11-15. Variant-13. Archetype: agentic-offensive-tool / exposed-surface buyer-guide (NEW). Awaiting `publish`.*
