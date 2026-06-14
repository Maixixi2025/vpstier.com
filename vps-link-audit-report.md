# VPS Link Audit Report

**Date:** 2026-06-11  
**Scope:** `/root/vpstier-site/src/pages/` — all .astro files  
**Task:** Find links to VPS provider domains and flag those needing affiliate link replacement

---

## Summary of Issues Found

### CATEGORY A: WRONG LINK — Points to RackNerd affiliate instead of the actual provider

These VPS page files have CTA buttons that say "Visit [Provider Name]" but actually link to `https://my.racknerd.com/aff.php?aff=16299`. These are placeholder/template links that need to be replaced with each provider's own affiliate link.

| # | File | Lines | Button Text Says | Actually Links To |
|---|------|-------|-----------------|-------------------|
| 1 | `vps/buyvm.astro` | 29, 114 | "Visit BuyVM →" / "Sign Up..." | RackNerd affiliate |
| 2 | `vps/contabo.astro` | 30, 68 | "Visit Contabo →" / "Sign Up..." | RackNerd affiliate |
| 3 | `vps/turnkey-internet.astro` | 29, 111 | "Visit TurnKey Internet →" / "Sign Up..." | RackNerd affiliate |
| 4 | `vps/hostwinds.astro` | 28, 132 | "Visit Hostwinds →" / "Sign Up..." | RackNerd affiliate |
| 5 | `vps/hostpapa.astro` | 28, 86 | "Visit HostPapa →" / "Sign Up..." | RackNerd affiliate |
| 6 | `vps/siteground.astro` | 28, 131 | "Visit SiteGround →" / "Sign Up..." | RackNerd affiliate |
| 7 | `vps/greengeeks.astro` | 28, 85 | "Visit GreenGeeks →" / "Sign Up..." | RackNerd affiliate |
| 8 | `vps/dreamhost.astro` | 28, 85 | "Visit DreamHost →" / "Sign Up..." | RackNerd affiliate |
| 9 | `vps/upcloud.astro` | 29, 87 | "Visit UpCloud →" / "Sign Up..." | RackNerd affiliate |
| 10 | `vps/chemicloud.astro` | 28 (top CTA only) | "Visit ChemiCloud →" | RackNerd affiliate |
| 11 | `vps/bluehost.astro` | 28, 66 | "Visit Bluehost →" / "Sign Up..." | RackNerd affiliate |
| 12 | `vps/fastcomet.astro` | 29, 68 | "Visit FastComet →" / "Sign Up..." | RackNerd affiliate |
| 13 | `vps/inmotion-hosting.astro` | 28, 132 | "Visit InMotion →" / "Sign Up..." | RackNerd affiliate |
| 14 | `vps/a2-hosting.astro` | 30, 100 | "Visit A2 Hosting →" / "Sign Up..." | RackNerd affiliate |
| 15 | `vps/scalahosting.astro` | 30, 68 | "Visit ScalaHosting →" / "Sign Up..." | RackNerd affiliate |

**Total: 15 VPS page files × 2 CTAs each = ~30 links pointing to wrong provider**

---

### CATEGORY B: WRONG LINK in blog — Points to RackNerd instead of actual provider

| # | File | Line | Issue |
|---|------|------|-------|
| 16 | `blog/upcloud-review.astro` | 128 | Anchor text says "Sign up via UpCloud →" but links to `my.racknerd.com/aff.php?aff=16299` |

---

### CATEGORY C: DIRECT LINK (no affiliate parameter) — Needs affiliate link

| # | File | Line | Current URL | Action Needed |
|---|------|------|-------------|---------------|
| 17 | `blog/contabo-vps-review-2025.astro` | 102 | `https://www.contabo.com` | Replace with Contabo affiliate link |
| 18 | `blog/ai-agent-vps-api-guide.astro` | 48 | `https://www.contabo.com` | Replace with Contabo affiliate link |

---

### CATEGORY D: PLACEHOLDER LINK (needs real affiliate ID filled in)

| # | File | Line | Current URL | Issue |
|---|------|------|-------------|-------|
| 19 | `blog/interserver-deep-review.astro` | 101 | `https://www.interserver.net/r/XXXX` | `XXXX` is placeholder — needs real ID |
| 20 | `blog/ai-agent-vps-api-guide.astro` | 49 | `https://www.interserver.net/r/XXXX` | `XXXX` is placeholder — needs real ID |
| 21 | `blog/cloudways-review-20260528.astro` | 106 | `https://www.cloudways.com/?id=XXXX` | `XXXX` is placeholder — needs real ID |

---

### CATEGORY E: LINKS THAT ARE ALREADY CORRECT

| Provider | URL Pattern | Status |
|----------|-------------|--------|
| **RackNerd** | `my.racknerd.com/aff.php?aff=16299` | ✅ Correct everywhere |
| **Vultr** (blog pages) | `www.vultr.com/?ref=9148877` | ✅ Correct |
| **Vultr** (vps/vultr.astro) | `www.vultr.com/?ref=9785034` | ✅ Has affiliate ref (different from blog ref: 9148877 vs 9785034) |
| **DigitalOcean** | `m.do.co/c/6bda2b7bf62b` | ✅ Correct |
| **Hostinger** (vps page) | `www.hostinger.com?REFERRALCODE=2BDTANSONG7B` | ✅ Correct |
| **Hostinger** (blog) | `www.hostg.xyz/aff_sub5` | ✅ Correct |
| **InterServer** (vps page) | `www.interserver.net/r/1146513` | ✅ Correct |
| **Cloudways** (vps page) | `www.cloudways.com/en/partners.php?id=131662` | ✅ Correct |
| **HostDare** | `bill.hostdare.com/aff.php?aff=4307` | ✅ Correct |
| **Yecaoyun (野草云)** | `my.yecaoyun.com/aff.php?aff=6802` | ✅ Correct |
| **Yinnet (萤光云)** | `www.yin-net.com/aff.php?aff=379` | ✅ Correct |
| **CloudCone** | `app.cloudcone.com/?ref=14241` | ✅ Correct |
| **RackNerd** (blog CTA) | `my.racknerd.com/aff.php?aff=16299` | ✅ Correct |

---

### CATEGORY F: DOMAINS WITH NO MATCHES FOUND IN ANY FILE

These domains from the watchlist were not found in any `.astro` file:

- ~~`hostwinds.com`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`hostpapa.com`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`siteground.com`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`greengeeks.com`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`dreamhost.com`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`fastcomet.com`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`inmotion.com`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`a2hosting.com`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`scalahosting.com`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`chemicloud.com`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`bluehost.com`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`turnkeyinternet.net`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`upcloud.com`~~ — No direct links found (page uses RackNerd placeholder — see Cat A)
- ~~`buyvm.net`~~ — Only mentioned in plain text (vps/buyvm.astro line 84), not as a link
- `digitalocean.com` — No direct `digitalocean.com` links (uses `m.do.co/c/...` which is correct)
- `vultr.com` — No naked `vultr.com` links; all use `www.vultr.com/?ref=...` which is correct

---

## Recommended Action Plan

1. **High Priority (Category A):** Replace the 15 VPS provider pages' CTA links from the RackNerd affiliate link to each provider's own affiliate/marketing link. These are template placeholder links that were never customized.

2. **High Priority (Category B):** Fix `blog/upcloud-review.astro` line 128 — the CTA says "Sign up via UpCloud" but links to RackNerd.

3. **Medium Priority (Category C):** Add affiliate parameters to the 2 bare `www.contabo.com` links in blog articles.

4. **Low Priority (Category D):** Fill in the `XXXX` placeholders in interserver and cloudways blog review links with actual affiliate IDs.
