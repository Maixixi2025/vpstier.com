# RamNode Verified Data — 2026-07-22

**Use case:** Tier 2 fresh add — long-running boutique now under InMotion Hosting ownership, transparent pricing across 4 tiers (Lite/Standard/Premium/Storage/VDS), hourly billing.

## Source URLs (verified live 2026-07-22)
- Homepage: https://ramnode.com/ — HTTP 200, 35KB, registered trademark notice confirms InMotion Hosting ownership
- Pricing: https://ramnode.com/pricing/ — HTTP 200, 42KB, full price matrix across 4 product lines
- About: https://ramnode.com/about/ — HTTP 200, 35KB, mission + datacenter list

## Company facts
- **Brand:** RamNode® (registered trademark)
- **Operator:** InMotion Hosting, Inc. (per footer trademark notice: "RamNode® is a registered trademark of InMotion Hosting, Inc.")
- **Founded:** Brand traces back to 2012 as a boutique VPS provider; integrated into InMotion Hosting circa 2024-2025
- **Tagline:** "Powerful servers at an outstanding value, backed by 24/7 expert support"
- **Support:** 24/7 chat + ticket, real engineers

## Datacenter locations (verified 2026-07-22)
Per About page + pricing region codes:
- **Atlanta, GA (USA East)**
- **New Jersey (USA East)**
- **Seattle, WA (USA West)**
- **Los Angeles, CA (USA West)**
- **The Netherlands (EU)**

Region codes referenced: EWR (Newark/NJ), LAX (Los Angeles), SEA (Seattle), NLX (Netherlands), ATL (Atlanta).

## Pricing matrix (live 2026-07-22, USD)

### Lite VPS (IPv6-only) — Currently only in EWR, LAX, NLX (SEA coming soon)
| RAM  | vCPU | NVMe | Bandwidth | Price       |
|------|------|------|-----------|-------------|
| 1 GB | 1    | 15 GB| 500 GB    | $2/mo       |
| 2 GB | 1    | 20 GB| 500 GB    | $3/mo       |

### Standard VPS (SSD, virtualized compute)
| RAM    | vCPU | SSD    | Bandwidth | Price      |
|--------|------|--------|-----------|------------|
| 512 MB | 1    | 20 GB  | 1 TB      | $4/mo      |
| 1 GB   | 1    | 40 GB  | 2 TB      | $5/mo      |
| 2 GB   | 2    | 80 GB  | 4 TB      | $10/mo     |
| 3 GB   | 2    | 100 GB | 6 TB      | $15/mo     |
| 4 GB   | 4    | 120 GB | 8 TB      | $20/mo     |
| 6 GB   | 4    | 160 GB | 10 TB     | $30/mo     |
| 8 GB   | 4    | 180 GB | 12 TB     | $40/mo     |
| 16 GB  | 8    | 260 GB | 14 TB     | $80/mo     |

### Premium VPS (NVMe + faster CPUs)
| RAM    | vCPU | NVMe   | Bandwidth | Price      |
|--------|------|--------|-----------|------------|
| 2 GB   | 2    | 80 GB  | 6 TB      | $14/mo     |
| 4 GB   | 4    | 120 GB | 10 TB     | $24/mo     |
| 6 GB   | 4    | 160 GB | 12 TB     | $36/mo     |
| 8 GB   | 4    | 200 GB | 14 TB     | $48/mo     |
| 16 GB  | 8    | 400 GB | 16 TB     | $96/mo     |
| 32 GB  | 16   | 600 GB | 18 TB     | $192/mo    |

### Storage VPS (HDD, optimized for backup/archival)
| RAM    | vCPU | HDD     | Bandwidth | Price      |
|--------|------|---------|-----------|------------|
| 512 MB | 1    | 160 GB  | 2 TB      | $4/mo      |
| 1 GB   | 2    | 325 GB  | 4 TB      | $6/mo      |
| 2 GB   | 2    | 650 GB  | 8 TB      | $12/mo     |
| 3 GB   | 2    | 1000 GB | 10 TB     | $17/mo     |
| 4 GB   | 2    | 1350 GB | 20 TB     | $22/mo     |
| 8 GB   | 4    | 2650 GB | 50 TB     | $43/mo     |
| 12 GB  | 4    | 4000 GB | 150 TB    | $64/mo     |

### VDS (Virtual Dedicated Servers, dedicated CPU cores)
| RAM    | vCPU         | NVMe   | Bandwidth | Price      |
|--------|--------------|--------|-----------|------------|
| 8 GB   | 2 dedicated  | 200 GB | 10 TB     | $50/mo     |
| 16 GB  | 4 dedicated  | 400 GB | 20 TB     | $90/mo     |
| 32 GB  | 8 dedicated  | 800 GB | 40 TB     | $170/mo    |
| 64 GB  | 16 dedicated | 1600 GB| 60 TB     | $320/mo    |

### Block Storage add-on (EWR, LAX, NLX only)
- $0.85/mo per 10 GB
- $0.085/GB/mo, billed hourly
- Attaches to cloud servers via API

## Payment
PayPal, Credit Card, **Crypto**, **Alipay** (Alipay support is unusual for US VPS — China-friendly)

## Differentiators vs other providers in vpstier
1. **Crypto + Alipay** payment stack — unusual at this price tier; RackNerd/Hostinger do not accept Alipay
2. **Hourly billing + pay-as-you-go credit pool** — no monthly lock-in (RackNerd requires annual prepay)
3. **Lite IPv6-only tier at $2/mo** — cheapest entry in vpstier's US/EU mix (BandwagonHost starts at $19.99/yr annual)
4. **VDS dedicated-CPU tier from $50/mo** — competes with CrownCloud Ryzen 9950X ($15/mo) and LightNode ($7.70/mo) but with reserved CPU cores
5. **InMotion Hosting parent** — financial backing of a long-established LA-based hosting company (~2001) — risk profile different from pure indie providers like Zappiehost
6. **5 datacenters** in 2 continents — fewer than Vultr (32+) or LightNode (40+) but covers US East/West + EU core

## Cons / risks
1. **No APAC datacenter outside SEA-coming-soon** — APAC buyers should still consider LightNode (40+ locations) or Vultr
2. **Storage tiers are HDD** — archival only, not for hot data
3. **Lite tier is IPv6-only** — buyer behind legacy IPv4-only firewall will not connect
4. **Standard tier SSD (not NVMe)** — Premium tier is the NVMe path, $14/mo entry
5. **Transfer caps are tighter than competitors** — RackNerd's $10.98/yr annual has unmetered 1Gbps; RamNode caps at 14TB/month on highest tier
6. **No GPU instances** — pure CPU compute

## Recommended use case (vs RackNerd baseline)
- **Best for:** developers wanting hourly billing without annual lock-in; US East/West + NL coverage; crypto + Alipay payers
- **Skip if:** you want the absolute cheapest VPS (RackNerd annual-special floor $10.98/yr wins), need APAC presence, or want unmetered bandwidth on a budget tier
