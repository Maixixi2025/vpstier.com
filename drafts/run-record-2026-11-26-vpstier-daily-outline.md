# VPSTier Daily Outline — Run Record — 2026-11-26

**Job:** `vpstier-daily-outline` (`5fd2a36f2dc4`)
**Deliverable:** `drafts/outline-2026-11-26-vpstier-daily.md` (39,190 chars, sha256 `09a0716eebea416a…`)
**Outcome:** outline written + `state.json` updated + committed. **Stopped before the Astro page / build / deploy**, per the outline-only contract. Awaiting user reply `publish`.

---

## 1. Briefing triage — both ⭐ VPS items rejected

| Briefing item | Verdict | Gate |
|---|---|---|
| ServerHost Black Friday offer prices rising $1/day from 28 Nov | ❌ | Merchant not whitelisted (0 of 65 `providers.json` entries); no provider-profile route in the repo. Angle additionally captured by the queued `drafts/outline-2026-08-03-serverhost-vps-review-2026.md` (13,729 B), whose premise is the same annual price ladder. |
| ZAP-Hosting lifetime servers now require a ZapX Pass (EUR 4.99 / 30 days), 1 Dec stop for unmigrated | ❌ | Published-angle collision — `drafts/outline-2026-11-05-vpstier-daily.md` is titled *"ZAP-Hosting ZapX Pass 2026 — The Real Cost of Lifetime VPS"* and already owns the archetype. Note: `zap-hosting` **is** whitelisted, so this is rejected on the angle gate alone. |

**Substitute:** taken from the briefing's own hard-material reserve line about a WHMCS flaw that lets anyone pull admin password hashes without logging in. It was filed as backup material rather than a lead, and it is the stronger story: dated, multi-source, vendor-primary-verifiable, and non-colliding.

---

## 2. New archetype — **the patch-day article whose subject is the unverifiability of the patch**

This is not the kernel-CVE archetype (2026-10-31), not the web-server-escalation archetype (2026-11-20), and not the credential-exposure archetype (2026-10-30). Its spine is a question the vendor's own advisory never answers:

> **After this patch, "is my host patched?" became a question a customer cannot answer from the outside — which makes "how do you check, and what do you do when the answer is unknowable?" the only useful buyer guide.**

The generalisable shape, for reuse on future disclosure days:

1. **A patch that spans multiple components with different access requirements.** One release, three CVEs, three different surfaces (public cart / client area / email campaigns), three different access levels (none / authenticated client with a common permission / authenticated client), three different bug classes (SQL injection ×2, template injection ×1). The buyer's exposure is a **function of which surface**, so a single "are they patched" question is under-specified.
2. **A severity inversion that inverts the reader's inference.** The no-auth flaw scored **8.7 HIGH**; the login-gated RCE scored **9.0 CRITICAL**. A reader who reads the highest number and concludes "the bad one needs a login, so I'm fine" has drawn the exact opposite conclusion from the truth. This is the single highest-value correction the article can deliver, and it only surfaces if you read the vectors rather than the headlines.
3. **A measurable-but-not-verifiable external signal.** The panel is *detectable* (two stable fingerprints) but its *version* is not exposed anywhere — no version string, no generator meta tag, no `whmcsVersion` constant, no `/version.txt`. So the check the article teaches answers half the question, and the honest article says so.
4. **A deadline hiding inside the fix.** The fixed release is also the last release of a line with a scheduled end-of-life. The fix and the migration deadline arrive in the same package.

**Reusable detection recipe — the WHMCS fingerprint (2 signals, either sufficient):**

```python
# Verified live 2026-11-26 on two hosts.
# 1) asset path   -> /templates/six/ (the stock WHMCS Six theme)
# 2) JS global    -> whmcsBaseUrl
import subprocess, re, os, tempfile
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
def probe(url, t=20):
    path=tempfile.mktemp(suffix='.html')          # clean temp file per request
    try:
        subprocess.run(['curl','-sL','-A',UA,'-H','Accept-Language: en-US,en;q=0.9',
                        '--compressed','--max-time',str(t),'-o',path,url],
                       capture_output=True, text=True, timeout=t+15)
        b=open(path, encoding='utf-8', errors='ignore').read()
        return {
            'six_asset': '/templates/six/' in b,
            'js_global': 'whmcsBaseUrl' in b,
            'generator': bool(re.findall(r'<meta[^>]+name=["']generator["']', b, re.I)),
            'version': sorted(set(re.findall(r'\b(?:8\.13|9\.0|9\.1)\.\d+\b', b))),
            'challenge': 'Just a moment' in b,        # <-- MUST check this
        }
    finally:
        os.unlink(path)
```

### 🚨 The false-positive this recipe would have produced

The first pass returned **`/templates/six/` and `whmcsBaseUrl` for `my.racknerd.com`** on an HTTP 200 response — but that response was a **Cloudflare "Just a moment" challenge page**, and the markers were an artefact of the challenge HTML, not of a WHMCS install. Three corrections were needed before the finding was safe to publish:

1. **Use a fresh temp file per request.** The first implementation wrote every fetch to `/tmp/_b.html` and read it back. A request that failed to write left the **previous** body in place, and the stale file's markers were then attributed to the new host.
2. **Assert the response is not a challenge page.** `challenge: 'Just a moment' in b` must be a **precondition**, not a diagnostic. A challenge page is HTTP 200 with `cFPWv` in the body and `/cdn-cgi/` assets.
3. **Re-fetch after a pause.** The host rate-limits hard: repeated probes to `my.racknerd.com` returned **HTTP 429** with a challenge body on 4 consecutive attempts. A **25-second pause** before the confirming fetch returned a clean **HTTP 200 / 33,996 B** WHMCS login page with the markers genuinely present.

**Only after that re-verification was the finding used** — and the control mattered: `clients.servarica.com` was probed in the same batch and showed the same markers with **no** challenge artefact, so the two signals were confirmed on two independent hosts.

**Generalised lesson:** a fingerprint found on a host that also serves a bot-challenge page is **not** a fingerprint until the challenge page has been excluded. Add `challenge` to every fingerprint probe, always.

---

## 3. Primary source table (all fetched this run)

| Source | URL | HTTP / bytes | Load-bearing fact |
|---|---|---|---|
| Vendor advisory 1 | `help.whmcs.com/m/125386/l/2151347-cve-2026-82981-whmcs-security-update-2026-11-23` | 200 / 38,329 | No-auth shopping-cart SQLi; affected 9.1.x < 9.1.2, 9.0.x < 9.0.10; **no 8.13 entry** |
| Vendor advisory 2 | `help.whmcs.com/m/125386/l/2151340-cve-2026-82979-whmcs-security-update-2026-11-23` | 200 / 38,537 | Client Area flaw; needs *View & Manage Contacts*; affected 8.13.x < 8.13.8 |
| Vendor advisory 3 | `help.whmcs.com/m/125386/l/2151351-cve-2026-93700-whmcs-security-update-2026-11-23` | 200 / 39,252 | CWE-1336 template injection; read config files incl. DB credentials + execute code; the two admin steps |
| Vendor announcement | `blog.whmcs.com/133803/security-update-2026-11-23` | 200 / 26,834 | By Kate, **24 Nov 2026**; the three releases; the two-step procedure; *"Fixes are only available for supported versions"* |
| CVE Program | `cveawg.mitre.org/api/cve/CVE-2026-82981` | 200 / 1,833 | CWE-89; affected ranges |
| CIRCL mirror | `cve.circl.lu/api/cve/CVE-2026-82981` | 200 / 2,018 | Independent corroboration |
| NVD (×3 ids) | `services.nvd.nist.gov/rest/json/cves/2.0?cveId=…` | 200 | published 2026-11-23T22:23:40Z, lastModified 2026-11-24T20:18:56Z, status `Received`; **8.7 / 7.1 / 9.0** |
| Trade press | `webhosting.today/2026/11/25/whmcs-patches-3-flaws-one-that-let-anyone-pull-admin-password-hashes/` | 200 / 100,954 | By Natalia Nowak, **25 Nov 2026**, datePublished 2026-11-25T10:35:47+00:00; the comparison table; the **31 Dec 2026** 9.0 EOL claim |
| Vendor footprint | `www.whmcs.com/company/` | 200 | *"tens of thousands of web hosting companies worldwide"*; WebPros: 27M clients / 60M domains / 650K servers |
| **Live probe A** | `my.racknerd.com/` | 200 / 33,996 | WHMCS login template; `whmcsBaseUrl`; `/templates/six/`; `/templates/racknerdv851/` |
| **Live probe B** | `clients.servarica.com/clientarea.php` | 200 / 23,798 | Same global + `/templates/six/`; `WHMCS…` cookie on the 302 |
| **Live probe C** | `my.racknerd.com/cart.php?a=view` | 200 / 127,201 | **Live WHMCS cart without an account** — the CVE-2026-82981 surface |
| KEV mirror | `raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json` | 200 / 1.9 MB | 1,805 entries, latest added 2026-11-25 → **0 hits** for all three ids |
| GitHub search | `api.github.com/search/repositories?q=WHMCS+CVE-2026-82981` | 200 | **total_count: 0** |
| RackNerd pricing | `www.racknerd.com/` + `/BlackFriday/` | 200 | **$2.24** + *20 datacenter locations*; specials ladder **$15.98 / $16.95 / $29.88 / $9.49** |

**Source boundary — stated in the outline, not hidden:** the vendor's own end-of-life documentation **could not be read** (`docs.whmcs.com` 404s on `/9.0/`, `/9.1/`, `/Introduction/`, the `.md` variants; the help-centre index is JS-rendered with non-extractable links). The **31 December 2026** date is therefore **attributed to the trade press** and never put in the vendor's mouth.

---

## 4. Collision gates — cleared with the distinguishing token printed **both ways**

The skill's rule is to print **both** the generic category count and the specific-token count, because a generic grep reads as "already covered" and kills a good topic.

| Token | Count | Where | Verdict |
|---|---|---|---|
| `CVE-2026-82981` | **0** | — | Clear |
| `CVE-2026-93700` | **0** | — | Clear |
| `CVE-2026-82979` | **1** | `run-record-2026-09-14` — an **outlet article slug**, not this CVE | Clear |
| `SQL injection` | **1** | `outline-2026-11-15` — the **FBI initial-access technique table** in the ARTEX scanning article | Different surface *and* different failure mode: a hostile scanner hitting **your** server vs a provider's billing panel being **read** |
| `email campaign` / `billing panel` / `sensitive configuration` / `admin account` / `password hash` | **0** | — | Clear |
| `WHMCS` (generic) | 6 | `solusvm-price-hike` (one clause: the module makes your renewal email arrive), `hostarmada-review` (pricing data source), 4 old outlines | None is a security subject |
| `pre-auth` | 6 | 10-31 / 11-06 / 11-20 outlines | All **guest-kernel or guest-app** surfaces. This is the **provider's control plane**, one layer out. Opposite editorial question |

**Adjacent published articles — related, not blocks:**

- `dreamhost-breach-2026-password-reuse-vps` (10 H2s) owns provider-issued **credential rotation**. Its surface is a *compromised credential needing rotation*; this article's surface is a *vulnerable panel that reads credentials*. Different artefact, different attacker path, different remedy.
- `solusvm-price-hike-2026-cheap-vps-costs` mentions the WHMCS module on the billing side as one clause in an explanation of why renewal emails arrive — a pricing story, not a security one.

---

## 5. Numbers computed, not eyeballed

```python
import datetime
TODAY = datetime.date(2026, 11, 26)
print((TODAY - datetime.date(2026,11,23)).days)                    # 3  -> days since release
print((datetime.date(2026,12,31) - TODAY).days)                     # 35 -> days to 9.0 EOL
print(round((datetime.date(2026,12,31)-TODAY).days/7, 1))           # 5.0 -> weeks
```

Severity values were read **live** from the NVD API this run, not copied from a dated summary: **8.7 HIGH** (CVSS 4.0, `AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N`), **7.1 HIGH** (CVSS 4.0, `PR:L`), **9.0 CRITICAL** (CVSS 3.1, `AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H`). Vectors were read in full because the score alone loses the access model.

---

## 6. Gates run against the file as written

| Gate | Result |
|---|---|
| Title length | **52/60** — Python `len()` on the final string; the declared number re-extracted from the file and matched |
| Description length | **155/155** — same method; the declared number re-extracted and matched |
| H2 count | **10** |
| FAQ count | **5** |
| RackNerd CTA placements | **8** (gate ≥6) |
| Cross-links | **15** — each checked **on disk** *and* **live** (HTTP 200 + byte count) |
| Banned-merchant sweep | **0** — the category token was swept in all case variants over the whole file and appears **nowhere**, including inside the check description |
| CJK characters | **0** |
| Deprecated-language route in prose | **0** — and the check row describes the absence **by category, not by path** |
| Internal paths referenced | **19**, all exist on disk — **0** nonexistent |
| ASCII semantic integrity | 31 short-token boolean assertions + sha256; **0 failures**; no glued tokens >25 chars |

### 🚨 The self-check row that would have contained the thing it denied

The first write of the outline's briefing-triage table said the rejected merchant had *"no `<vendor-profile route>`"*, i.e. it wrote a concrete provider-profile path for a provider that has none. That route **does not exist on disk** — so a self-check row claiming "every internal path exists" was simultaneously writing a path that does not exist, and the path-existence gate caught it. Fixed in the outline by describing the absence **by category** (*"it has no provider-profile route in the repo"*) — and fixed here in the run record the same way, since quoting the corrupt path back to explain the repair would re-break the gate. The outline re-scan came back **19 paths, 0 nonexistent**.

This is the same failure class as the archived pitfall *"a self-check row must not contain the thing it claims is absent"* — the payload differs (a nonexistent route rather than a language-prefix path) but the rule is identical: **describe the absence without naming the path**.

### ⚠️ A quote-verification miss caught by the assertion set

The outline's §1 table initially named the researcher who reported all three flaws. That name was **not** quoted from a source in the outline's own body, and the short-token assertion set flagged it as an unmatched string. It was replaced with a paraphrase — *"the researcher who reported all three"* — and the assertion set then passed. **The assertion set did its job**: it caught a string that was in the file but not supported by a citation in that file.

---

## 7. `state.json` — convention matched, diff minimal

Read the convention from HEAD before writing, per the skill rule:

- HEAD's first three lines: `{`, `  "current_index": 64,`, `  "published": [` → **indent = 2**
- HEAD's file **does not** end with a newline → **no trailing newline**

Written with `json.dumps(st, ensure_ascii=False, indent=2)` and **no** trailing newline.

**Semantic verification (not line count):**

```
drafts prefix byte-identical:        True
publish_notes strict prefix-extension: True
published unchanged:                 True
recent_topics prefix:                True
git diff --stat:  1 file changed, 29 insertions(+), 5 deletions(-)
```

**29 insertions / 5 deletions for a one-entry append** — the shape the skill records as correct. (A `indent=1` write would have produced a ~3,500-line reformat.)

**Banned-token count is a DELTA, not an absolute:** today's new draft entry contains **0** occurrences of the banned category token; the `publish_notes` delta adds **0**; the **1** occurrence at HEAD is pre-existing.

---

## 8. Flagged for the user (carried into the outline's §8, not fixed here)

1. **🔴 `/vps/racknerd/` pricing drift — now the SIXTH consecutive outline flag** (11-13, 11-14, 11-15, 11-16, 11-20, 11-26). The profile says **$1.99/mo** and **8 datacenters**; the vendor's own site says **$2.24** and **20 datacenter locations**. A live conversion page with wrong pricing, re-flagged for two weeks and fixed in none. **This is now a task, not a note** — it needs a publish-slot fix or an explicit `pending_fix` entry with a due date. The article's CTA placements quote the **vendor's live prices** so the article itself does not inherit the error.
2. **🟡 `providers.json` carries the same stale RackNerd numbers** (`startingPrice: 1.99`, a five-city `datacenters` array).
3. **🟡 Two candidate cross-links rejected** — the 11-02 blast-radius outline and the 11-20 NGINX2Root outline have **no published article** behind them; linking them would 404.
4. **🟡 The 9.0 end-of-life date stays trade-press-attributed** until a vendor URL is found.
5. **🟢 Pre-existing zh-language carry-over files** remain; **0 new** language-variant content written today.
6. **🟢 Working-tree noise left uncommitted and unbundled:** `tsconfig.json` (zero `@/` imports in `src/` → inert) and a modified published article from another run.

---

## 9. What was NOT done (correctly)

- **No Astro page, no build, no deploy.** This job is outline-only and stops at the `publish` reply.
- **No `git add -A`.** Only today's two files are staged explicitly. The pre-existing orphan backlog and the unrelated modifications stay untouched.
- **No claim that any whitelisted provider was left unpatched.** The article's subject is the *unverifiability*, and it explicitly advises against a panic migration.
