# Kainode VPS — Verified Data (2026-07-16)

**Source URLs (re-crawled 2026-07-16 in the 5-min window before publish):**
- Homepage: https://kainode.com/ — 59,028B HTML; pricing carousel loaded with full data (NOT JS-shell fallback).
- VPS landing page: https://kainode.com/vps — 8,815B; Singapore-specific page, table is JS-rendered (only headers in initial HTML).
- Pricing page: https://kainode.com/pricing — 9,868B; same JS-rendered issue (table headers only).
- LowEndBox reference: https://lowendbox.com (Kainode article, surfaced in 7/15 briefing).

**Detected pricing model:** VDS (Virtual Dedicated Server) tier — daily pricing shown as "per day", renews at monthly rate. Three published plans + carousel-managed-VPS sub-listing. No KVM/OpenVZ/Virt的区别; the site uses "VDS" exclusively for the virtual-server product family.

**Pricing (verified 2026-07-16):**

| Plan | vCPU | RAM | NVMe | Bandwidth | Daily | Monthly (renewal) |
|------|------|-----|------|-----------|-------|-------------------|
| VDS Pro | 2 dedicated | 4 GB | 80 GB | 3 TB | $0.25/day | $16.99/mo |
| VDS Business (Popular) | 3 dedicated | 6 GB | 100 GB | 5 TB | $0.40/day | $19.52/mo |
| VDS Enterprise | 4 dedicated | 8 GB | 150 GB | 10 TB | $0.63/day | $29.99/mo |

Note: the homepage carousel shows a "Managed VPS" sub-tab that re-lists VDS Pro at $0.56/day for 3c/6GB/80GB/3TB. The unmanaged VDS Pro is $0.25/day for 2c/4GB/80GB/3TB. The article will reference the unmanaged VDS plans (canonical pricing).

**Datacenters (verified from homepage + VPS page):**
- Singapore (relaunched "is back" per homepage notice)
- Germany
- USA (Sheridan, WY registered business address)

**Company info:**
- Legal entity: 30 N Gould St Ste R, Sheridan, WY 82801, USA (per footer)
- Phone: +1 (307)-855-1647
- Email: support@kainode.com
- Active LowEndBox offer still running
- Copyright: 2025-26 (brand launched late 2025)

**Features (extracted from homepage + VPS page):**
- "Dedicated resources" — VDS plan names imply dedicated cores
- NVMe storage on all plans
- Anti-DDoS ("Secure DDoS Protection" hero feature)
- 99.9% uptime SLA (hero claim)
- Instant deployment, full admin access
- Multi-region support (3 DCs: Singapore / Germany / USA)
- Domain services, Shared Hosting, Email Server, Dedicated Server, Colocation also offered
- Payment terms: daily / weekly / monthly / yearly billing cycles available

**Verdict for vpstier audience:**
- ✅ Singapore DC is the headline differentiator — only RackNerd (LA), Vultr (worldwide), DigitalOcean (worldwide), HostNamaste (no SG), Yin-net (SG yes), Kamatera (worldwide), Cherry Servers (no SG) of the covered providers have Singapore. Among these, Kainode's $16.99/mo entry is between RackNerd's $11.99/yr promo and Vultr's $12/mo 1GB plan.
- ⚠️ Young brand (launched 2025), limited public review history beyond LowEndBox mention.
- ⚠️ Datacenter list is short (3 only) vs Vultr/DigitalOcean world-wide coverage.
- ⚠️ Only 3 plans published; no clear API/CLI automation story on the page.
- ⚠️ Terms/Refund policy linked but not crawled in this session (out of scope).

**Affiliate program:** Kainode's own affiliate program is not advertised on the homepage / VPS page / pricing page footer (no "Affiliates" link, no "Partners" link). Per vpstier policy, Kainode review uses the RackNerd fallback affiliate `https://my.racknerd.com/aff.php?aff=16299` for the closing CTA, with internal links to the Kainode VPS page where appropriate.

**Pricing ground truth timestamp:** 2026-07-16 (the prices in the table were scraped live from https://kainode.com/ in this same session).
