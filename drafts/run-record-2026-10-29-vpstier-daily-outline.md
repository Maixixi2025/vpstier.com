# Run Record — vpstier daily outline — 2026-10-29

**Cron ID:** `5fd2a36f2dc4` (vpstier-daily-outline, `45 9 * * *`)
**Run date:** 2026-10-29
**Outline produced:** `drafts/outline-2026-10-29-vpstier-daily.md`
**Slug:** `vps-ssh-security-host-key-checks-2026`
**Status:** `outline_pending_publish` — stopped before Astro/build/deploy, awaiting user `publish`
**Model:** MiniMax-M3.1-Flash via minimax-cn

---

## 1. Variant adjudication

**Variant-0 (briefing succeeded; selected the freshest dated substitute outside the briefing's own picks).**

The 2026-10-29 08:00 briefing produced two vpstier items. Both were rejected for hard-gate reasons, and a freshest-dated substitute was sourced from the same date window outside the briefing.

| # | Briefing item | Verdict | Gate that fired |
|---|---|---|---|
| 1 | Reddit r/VPS — "Contabo VDS down 3 days after a host compromise" | REJECTED | **walled primary.** `www.reddit.com`, `old.reddit.com` and `/.json` all return HTTP 403 "Blocked" from this sandbox (3 URLs × 2 attempts, 2026-10-29). The only body-verifiable 2026-10-21 item on that host is a **different story** (the PwnEscape kernel vulnerability forcing a reboot), not a compromise. A compromise claim on an unfetchable primary cannot be asserted. |
| 2 | Reddit r/VPS — "FOSS autobenchmarked 38 VPS types" | REJECTED | **off-shape + excluded merchant named in the subject list.** Benchmark-roundup shape; vpstier already carries the benchmark-vetting angle as a queued outline (2026-09-13). Off-shape re-surfaces are rejected permanently. |

**Selected substitute — the October 2026 Tor exit-relay SSH interception campaign** (disclosed 2026-10-21).

This is **not** a banned-pivot (no merchant ban is involved) and **not** a variant-7 walled-primary adoption (the substitute was body-fetched directly). It is a straight freshest-dated-substitute pick from the 2026-10-21..2026-10-28 window, corroborated across two independent fetchable outlets.

---

## 2. Source-verification ladder actually executed

| Source | Result | Bytes |
|---|---|---|
| `thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html` | HTTP 200 | 182,384 |
| `cyberinsider.com/tor-removes-hundreds-of-compromised-relays-used-to-hijack-ssh-logins/` | HTTP 200 | 213,236 |
| `tailscale.com/security-bulletins/` | HTTP 200 | 406,479 |
| `blog.torproject.org/` | HTTP 200 | 15,773 |
| Google News RSS (corroboration multiplier) | HTTP 200 | — |
| `www.reddit.com` + `old.reddit.com` + `/.json` (briefing item 1 + 2 primaries) | **HTTP 403 "Blocked"** | — |
| `bleepingcomputer.com` (5 URLs) | HTTP 403 | — |
| `darkreading.com`, `arstechnica.com`, `securityweek.com` | 403 / unreachable | — |
| `thehackernews.com` (PHP2Shell item, attempted) | 404 on guessed slug | — |
| `pasqualepillitteri.it` (PwnEscape) | RemoteDisconnected | — |
| `status.contabo.com`, `blog.gmo.jp`, `status.gmo.jp` | DNS not resolved | — |
| `zeabur.com`, `blog.zeabur.com` | unreachable | — |
| `blog.railway.com` (exact slug) | HTTP 404 | — |
| `helpnetsecurity.com` (DreamHost) | unreachable | — |
| `archive.org` / Wayback | not attempted — documented as unreachable in 7 consecutive prior runs | — |

**Body-fetchable sources used:** The Hacker News, CyberInsider, Tailscale's own advisory, Tor Project blog. **Corroboration multiplier:** Google News RSS — 11 distinct outlets across 2026-10-21..2026-10-25 for the Tor story (The Hacker News, Ars Technica, SC Media, Mezha, SecurityWeek, CyberSecurityNews, CyberInsider, The420.in, Forkast, TechGig, + one Google News "Other News" roundup).

**Rejected as competing candidates, with reasons:**
- **Tailscale SSH flaws (TS-2026-014/015/016/017), disclosed 2026-10-28, Tailscale 1.104.4** — genuinely fresher (yesterday) and fully body-verified via the vendor advisory. Rejected as the *primary* anchor because Tailscale SSH is a niche overlay feature, not a default VPS surface, and the audience overlap with vpstier's ICP is thin. **Held as a supporting datapoint for §6/§7** (socket-forwarding to the Docker socket and `tailscaled` local API is exactly the "root-only socket" escalation class that makes a compromised VPS worse).
- **DreamHost password-reset incident (2026-10-26/27)** — 9-outlet cluster, but the hosts are shared hosting, the forced-reset cause is officially unexplained, and the underlying `helpnetsecurity.com` body was unreachable. Fails the "named vendor statement" test the prior runs used.
- **GMO Internet / Onamae Desktop Cloud breach (2026-10-22 → 2026-10-28)** — 10+ outlets, strongest recency, but it is a **virtual desktop cloud for FX traders**, not VPS, and the affected population is not vpstier's ICP. Same ICP-drift rejection applied to the Railway, TiDB Cloud and Zeabur items.
- **Zeabur shutdown after two breaches (2026-10-20/22), 3.2M records / 321,810 accounts** — body-verifiable via multiple outlets, but the vendor is absent from `providers.json` and the shutdown-completion angle is closer to the already-queued `vps-provider-exit-warning-signs-2026` (2026-08-27) than to a new gap.

---

## 3. Fact bundle (17 facts, each traced to a body-fetched source)

| # | Fact | Source |
|---|---|---|
| 1 | ~3,000 Tor exits scanned with `exitmap`; 333 redirecting SSH to 12 interception servers | THN |
| 2 | 377 relays / 147 IPs / 59 operators matched the suspicious exit policy — "a policy match, not proof of compromise" | Tor analysis at 1AEO via CyberInsider |
| 3 | Peak 7.46% of Tor exit capacity by consensus weight | Tor directory-data analysis |
| 4 | Window 2026-10-01 → 2026-10-05; policy live ~52 hours on two relays moving ~3.4 TiB/day | THN |
| 5 | Cleared from consensus by 2026-10-05 17:00 UTC; none returned as of 2026-10-09 | Tor analysis |
| 6 | Exit-flag relay count fell ~370 between 10-03 and 10-05; not recovered by 10-18 | Tor Metrics |
| 7 | Attackers rewrote `torrc` to allow port 22 (342 relays that blocked it); 24 non-exit relays became exits | THN + CyberInsider |
| 8 | IMAPS/POP3S closed, POP3/IMAP opened — encrypted mail was not forced to plaintext (Tor picks an exit allowing the destination port; POP3/IMAP can still upgrade to TLS) | CyberInsider |
| 9 | Only **password** logins leak; key-based logins cannot be relayed (session-unique signature in the client's signature) | THN |
| 10 | Interception host key: ED25519, `SHA256:6baCZCPsl+AfQuujUS81fMEE/C7UeJ+AwjrImqmDB3E` | THN |
| 11 | Ebury 1.8.3 — OpenSSH backdoor/credential stealer active since 2009; ESET estimated ~400,000 infected servers (2024) | THN |
| 12 | Implant: single setuid file `/usr/lib/x86_64-linux-gnu/libkeyutils.so.1.10.2` + redirected symlink; `dpkg -V` and `debsums` do not detect it; sshd/sudo/PAM pass package checks | THN + CyberInsider |
| 13 | Ebury 1.8.3 post-dates ESET's public indicators (which stop at 1.8.2) | THN |
| 14 | Operator's own post-mortem (2026-10-07): one password reused for SSH login + `sudo` + backup passphrase, stored in plaintext, with password auth left enabled on the internet-facing management host — "the root cause was ours" | Zimmer via THN |
| 15 | Entry point: attacker logged in on **2026-08-28** with the operator account password on the first try, **root within five minutes**, Ebury installed; second host ~1 hour later | Zimmer via THN |
| 16 | Offline master keys were not offline — copies sat in a workstation backup on the management host, encrypted with the password the attacker already had | Zimmer via THN |
| 17 | Which hosts were hit | **Two different budget VPS providers** — management server (VPN gateway + SSH jump host) at Contabo; exit host "Switzerland2" (ran two exits) a FranTech VPS | THN |
| 18 | Operator's final action | retired every relay and the bridge, deleted both servers | Zimmer via THN |

**Facts deliberately NOT asserted:** no victim count exists (the source says so explicitly); the hosting-provider-breach theory is flagged in the source as *unconfirmed*, so it is not asserted; the two merchant names in the incident appear only as case-study facts.

---

## 4. Content-gap verification

Pre-write grep over **all 60** published blog articles and **all 55** queued outlines:

```
known_hosts              -> 0 hits
StrictHostKeyChecking    -> 0 hits
host key / host-key      -> 0 hits
Ebury                    -> 0 hits
key-based authentication -> 0 hits
tailscale / mesh / overlay-> 0 hits in state.json
```

Adjacent-queue overlap check (both fail to cover this angle):
- `vps-offsite-restore-backup-guide-2026` (2026-09-06) — data restore, not SSH auth.
- `virtualizor-bgp-hijack-supply-chain-vps-2026` (2026-09-09) — the control panel's **update channel** (BGP hijack of the software-update prefix), not SSH authentication.

**Slug collision:** `vps-ssh-security-host-key-checks-2026` is absent from `published[]`, `drafts[]` and `src/pages/blog/`.

---

## 5. Measurements

| Gate | Value | Limit | Result |
|---|---|---|---|
| Title | 57 | 30–60 | PASS |
| Description | 146 | 70–155 | PASS |
| H2 sections | 10 | 8–10 | PASS |
| FAQ | 5 | 3–5 | PASS |
| RackNerd CTA placements | 8 | ≥6 | PASS |
| Cross-links (all targets verified on disk) | 9 | — | PASS |
| Excluded-merchant token count in this document | 0 | = 0 | PASS |
| CJK character count in this document | 0 | = 0 | PASS |
| Deprecated language-prefix path in prose | 0 | = 0 | PASS |

**Title-suffix rule applied:** `src/layouts/BaseLayout.astro` contains a bare `<title>{title}</title>` with no `fullTitle` concatenation — the source title string IS the final title. No suffix budget was reserved and none is needed. (vpstier's rule, verified 2026-08-02, re-verified against the live file 2026-10-29.)

---

## 6. Cross-link path verification (all on disk)

```
/blog/vps-buying-guide/                          OK
/blog/vps-pricing-trap-guide-2026/                OK
/blog/best-north-america-vps-2026/                OK
/blog/best-asia-pacific-vps-2026/                 OK
/blog/cheap-vps-local-llm-inference-2026/         OK
/blog/ai-agent-vps-api-guide/                    OK
/blog/2026-shutdown-cloud-services-vps-migration/ OK
/blog/vps-price-hikes-2026-ramageddon/            OK
/blog/solusvm-price-hike-2026-cheap-vps-costs/    OK
```

Three queued slugs were **excluded** because they have no live URL yet: `digitalocean-outage-august-2026-multi-cloud-vps-fallback`, `vps-vs-vds-2026-which-to-choose`, `vps-offsite-restore-backup-guide-2026`.

---

## 7. Provider / affiliate handling

- **RackNerd** is the site's affiliate baseline and the primary CTA. Facts used are from `providers.json`: from $1.99/mo, 512MB–64GB RAM, 1–640GB SSD, 1TB–10TB bandwidth, 5 US datacenters, root access included, rating 4.2. Stamped "as of 2026-10-29".
- Every CTA names RackNerd as the site affiliate / budget baseline — **never** as the provider under review.
- The two merchant names appearing in the incident facts are the **case study**; they are not recommended and not presented as an affiliate destination. The article will state that the operator retired every relay and deleted both servers.
- Whitelisted-provider checks: `/vps/racknerd/`, `/vps/digitalocean/`, `/vps/vultr/`, `/vps/linode/`, `/vps/hostinger/`, `/vps/contabo/`, `/vps/buyvm/`, `/vps/ovhcloud/` — all exist.

---

## 8. Two-commit plan

**Commit 1** — `feat(drafts): vpstier daily outline 2026-10-29 (vps-ssh-security-host-key-checks-2026)`
```
git add drafts/outline-2026-10-29-vpstier-daily.md drafts/run-record-2026-10-29-vpstier-daily-outline.md
```
**Commit 2** — `chore(state): vpstier daily outline 2026-10-29 recorded (drafts_count 54 -> 55, last_run 2026-10-28 -> 2026-10-29)`
```
git add drafts/state.json
```

`git add -A` is **not** used — the repo carries a large orphan backlog (`??` outline/run-record files from 2026-08-01 through 2026-10-15, plus a `M tsconfig.json` that predates today).

**state.json write rules applied:** `publish_notes` on vpstier is a **STRING** (not a list) — append with `\n`; `drafts_count` is updated **after** the append in the same operation; `last_run` gets its own explicit assignment; the file is written with `ensure_ascii=False` to preserve Unicode.

---

## 9. Stop condition

The run stops at `outline_pending_publish`. No `.astro` file was written, no build was run, no deploy was attempted, and no `published[]` entry was created. The article-writing cron (`c49b9d5fb6aa`, Mondays) picks up the outline only after the user replies `publish`.

**Expected publish slot:** Monday 2026-11-02.
