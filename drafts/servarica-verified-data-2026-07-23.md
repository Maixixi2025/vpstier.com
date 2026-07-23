# ServaRica Verified Data — 2026-07-23

**Source:** Live website probes 2026-07-23 via browser_navigate (ServaRica uses JS-rendered pricing tables; raw curl returns no $ prices in HTML body).
**URLs probed:**
- https://servarica.com/vps → NVMe VPS page (HTTP 200, 7.5 MB JS-rendered)
- https://servarica.com/nvme-vps/ → "NVMe VPS - ServaRica" (HTTP 200, full table)
- https://servarica.com/v3-kvm-slices/ → "V3 KVM Slices - ServaRica" (HTTP 200, full table)
- https://servarica.com/nvme-vds/ → "NVMe VDS - ServaRica" (HTTP 200, full table)
- https://servarica.com/storage-servers/ → "Storage Servers - ServaRica" (HTTP 200, full table)
- https://servarica.com/about/ → "About - ServaRica" (HTTP 200, founder info)
- https://servarica.com/faq/ → "FAQ - ServaRica" (HTTP 200, 12 Q&A, all expanded)

**Founded:** 2010 (Hani founded after postaRICA project; "by early 2010" per About page)
**Operator:** Rica Web Services Inc. ("© Copyright 2025 by Rica Web Services Inc. All Rights Reserved.")
**HQ:** 350 Rue de Louvain O, Suite 203C, Montreal QC H2N 2E8, Canada
**Phone:** +1 (514) 800-5409
**Email:** support@servarica.com
**Datacenter:** Montreal, Quebec, Canada (single location; 100% Hydro-Quebec renewable)

## Differentiator (Tier 2 batch-probe pick, 2026-07-23)

- **Canadian operator + Montreal-only footprint** — single hand-curated datacenter, 100% Hydro-Quebec renewable energy (Hydro-Québec is 99% renewable: water dams)
- **Cold-weather free cooling** — state-of-the-art cooling that depends on Canadian cold, reducing energy + heat
- **AMD EPYC across the board** — all 4 product lines are EPYC (no Xeon, no Ryzen consumer parts)
- **"Unified Plans" thesis** — supersedes older VDS/hybrid/NVMe storage; all unified plans have dedicated cores
- **Custom automation stack** — "Xenica" (their own automation software) for VM lifecycle, multi-homed network with own ASN + routers
- **Full SLA tiers** — 99.9%/99%/97%/95% uptime with progressive 15/30/50/100% monthly refund
- **Disallowed content:** adult/pornography, public proxies, IRC servers (except by case), gambling, TOR exit nodes (intermediate nodes OK)

## Verified pricing (live 2026-07-23)

### NVMe VPS — 1Gbps, AMD EPYC, 10 plans
| Plan | RAM | CPU | BW | NVMe | Monthly | Yearly |
|---|---|---|---|---|---|---|
| EPYC - Wildbeest NVMe Storage 1 | 3 GB | 2 | 12TB 1Gbps | 250 GB | $7 | $77 |
| EPYC - Wildbeest NVMe Storage 2 | 6 GB | 4 | 24TB 1Gbps | 500 GB | $14 | $154 |
| EPYC - Swordfish NVMe Storage 1 | 3 GB | 4 | 12TB 1Gbps | 400 GB | $9 | $99 |
| EPYC - Swordfish NVMe Storage 2 | 12 GB | 4 | 24TB 1Gbps | 1200 GB | $27 | $297 |
| EPYC - NVMe Cub | 4 GB | 2 | 12TB 1Gbps | 40 GB | $5 | $55 |
| EPYC - Flying Fish NVMe | 4 GB | 4 | 12TB 1Gbps | 200 GB | $5 | $48 |
| EPYC - NVMe Cheetah | 6 GB | 4 | 12TB 1Gbps | 80 GB | $7 | $77 |
| EPYC - NVMe Cheetah 2 | 18 GB | 4 | 12TB 1Gbps | 240 GB | $20 | $220 |
| NVMe Cheetah 3 | 60 GB | 8 | 12TB 1Gbps | 800 GB | $60 | $660 |
| EPYC - NVMe Tiger | 10 GB | 4 | 12TB 1Gbps | 150 GB | $10 | $110 |

### V3 KVM Slices — 10Gbps, AMD EPYC Milan (latest gen, "320% more perf/$ vs v2")
| Plan | RAM | CPU | BW | NVMe | Monthly | Yearly |
|---|---|---|---|---|---|---|
| V3 KVM Slice 2 | 2 GB | 2 | 6TB 10Gbps | 60 GB | $4 | $44 |
| V3 KVM Slice 4 | 4 GB | 4 | 12TB 10Gbps | 120 GB | $6 | $66 |
| V3 KVM Slice 6 | 6 GB | 6 | 18TB 10Gbps | 180 GB | $8 | $88 |
| V3 KVM Slice 8 | 8 GB | 8 | 24TB 10Gbps | 240 GB | $10 | $110 |
| V3 KVM Slice 12 | 12 GB | 12 | 36TB 10Gbps | 360 GB | $14 | $154 |
| V3 KVM Slice 16 | 16 GB | 16 | 48TB 10Gbps | 480 GB | $18 | $198 |
| V3 KVM Slice 24 | 24 GB | 24 | 72TB 10Gbps | 720 GB | $26 | $286 |
| V3 KVM Slice 32 | 32 GB | 32 | 96TB 10Gbps | 960 GB | $34 | $374 |
| V3 KVM Slice 40 | 40 GB | 40 | 120TB 10Gbps | 1200 GB | $42 | $462 |
| V3 KVM Slice 48 | 48 GB | 48 | 144TB 10Gbps | 1440 GB | $50 | $550 |

### NVMe VDS — Dedicated CPU cores, 1Gbps, AMD EPYC
| Plan | RAM | CPU | BW | NVMe | Monthly | Yearly |
|---|---|---|---|---|---|---|
| Octopus VDS 1 | 8 GB | 2 | 12TB 1Gbps | 70 GB | $8 | $88 |
| Octopus VDS 2 | 16 GB | 4 | 24TB 1Gbps | 150 GB | $15 | $165 |
| Octopus VDS 3 | 32 GB | 8 | 24TB 1Gbps | 300 GB | $30 | $330 |

### Storage Servers — ZFS RAIDZ2, HDD-backed
| Plan | Storage | BW | Monthly | Yearly |
|---|---|---|---|---|
| BigStorage 2TB Starter | 2 TB | 100Mbps unmetered OR 1Gbps / 4TB cap | $10 | $120 (Save 50%) |
| BigStorage Silver | 5 TB (assumed scale-up) | 100Mbps unmetered OR 1Gbps / 4TB cap | $55 | $660 (Save 50%) |
| BigStorage Gold | 10 TB (assumed scale-up) | 100Mbps unmetered OR 1Gbps / 4TB cap | $120 | $1440 (Save 50%) |

Note: Storage Server page renders exact storage sizes behind a JS component; yearly pricing shows 50% off (10/55/120 USD/mo vs 20/110/240 list).

## Payment methods (verified 2026-07-23 from FAQ)
- PayPal ✓
- Alipay ✓ (rare for North American provider)
- Major credit cards (VISA, Master Card) ✓
- Cryptocurrencies (Bitcoin, Ether, etc.) ✓
- Checks sent by mail (for amounts >$200)
- Bank transfers (for amounts >$200)

## Setup time (from FAQ)
- Virtual Server setup: usually 10 minutes
- Some orders require billing fraud-screening: can take several hours

## SLA (from FAQ)
- 99.9% and above → normal operation
- 99.0% and above → 15% refund of monthly charges
- 97.0% and above → 30% refund of monthly charges
- 95.0% and above → 50% refund of monthly charges
- Less than 95% → 100% refund of monthly charges

## Network (from FAQ)
- Multi-homed network (multiple internet providers for redundancy)
- Own ASN + own routers (per "Expansions" history on About page)
- "Looking Glass" at https://ping.servarica.com/
- Speedtest at https://speedtest.servarica.net

## Team (from About page, 2024/2025 hires)
- Hani — Founder
- Mohamed Ali — Team Lead
- Giannis — Sr. System Engineer
- Sathish — Sr. System Engineer
- Orwah — Sr. Developer
- Gokul — System Engineer
- Hari — Assoc. System Engineer
- Fayis — Jr. System Engineer
- Soundes — Developer

## Why this pick (vs the other 9 fresh candidates probed)
- **HostZealot** (986K): JS-rendered pricing, no prices in HTML body
- **PhoenixNAP** (913K): Bare-metal focused, no consumer VPS product line
- **ServaRica** ← picked
- **Hostworld** (131K, £ pricing): UK-only, GBP-only pricing — VPSTier is USD-focused
- **Gcore** (443K): Enterprise CDN/cloud focus, complex pricing
- **psychz** (60K): Bare-metal/DDoS, VPS not core offering
- **datapacket** (431K): Dedicated server focus
- **time4vps** (403): Geo-blocked / bot-blocked (CF)
- **justhost/hostgator**: 403 (same CF block)

ServaRica was selected for:
1. Clean public pricing table (4 distinct product lines, all EPYC, USD-denominated)
2. Differentiated narrative (Canadian operator + Hydro-Quebec renewable + single Montreal DC + full SLA + crypto + Alipay)
3. Public domain WHOIS-verifiable operator (Rica Web Services Inc., Montreal address on footer)
4. Full SLA with progressive refunds (rare at this price tier)
5. Wholly original operator story (not a reseller, founder still active)
