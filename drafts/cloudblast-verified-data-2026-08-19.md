# Cloudblast — Verified Data (2026-08-19)

Source: lowendbox.com article "Cloudblast: 4GB VPS for Only €4.03/Month in USA, NL, and Hong Kong With UNLIMITED BANDWIDTH!" (raindog308, Aug 12 2026 @ 12:14 pm) + cloudblast.io/pricing (verified 2026-08-19, HTTP 200, 721,656 chars).

## Company snapshot
- Brand: Cloudblast (cloudblast.io)
- New entrant, surfaced in LowEndBox 2026-08-12 — first major editorial coverage
- Console-based cloud VPS (hourly billing + prepaid)
- Accepts credit cards (Stripe), crypto (including Monero / XMR), AliPay
- Discounted VPS with 10 Gbit/s network, no commitment

## Datacenters (3 active, 1 announced)
| Code | City | Country | Status | Test IPv4 | Operator |
|---|---|---|---|---|---|
| AMS5 | Amsterdam | Netherlands | Active | 89.34.230.32 | Digital Realty |
| SLC1 | Salt Lake City | United States (Utah) | Active | 192.166.82.235 | (own facility) |
| Hong Kong | Hong Kong SAR | China (APAC) | Active | 178.83.121.94 | Eons Data |
| Birmingham | Birmingham | United Kingdom | Coming soon | n/a | n/a |

## Pricing tiers (cloudblast.io/pricing, verified 2026-08-19)

All tiers: AMD EPYC CPU, NVMe storage, 10 Gbps network port, 1 IPv4 + /64 IPv6, hourly billing.

| Plan | €/month | €/hour | vCPU | RAM | NVMe | Bandwidth |
|---|---|---|---|---|---|---|
| VMA11 | €3.6 | €0.0049 | 1x AMD EPYC | 3 GB | 20 GB | Unlimited (US/NL); 1TB (HK) |
| VMA21 | €4.8 | €0.0067 | 2x AMD EPYC | 4 GB | 30 GB | Unlimited (US/NL); 1TB (HK) |
| VMA31 | €7.2 | €0.010 | 3x AMD EPYC | 6 GB | 40 GB | Unlimited (US/NL); 1TB (HK) |
| VMA41 | €9.6 | €0.014 | 4x AMD EPYC | 8 GB | 40 GB | Unlimited (US/NL); 1TB (HK) |
| VMA51 | €19.2 | €0.027 | 8x AMD EPYC | 16 GB | 60 GB | Unlimited (US/NL); 1TB (HK) |
| VMA61 | €28.8 | €0.040 | 8x AMD EPYC | 24 GB | 60 GB | Unlimited (US/NL); 1TB (HK) |
| VMA71 | €38.4 | €0.054 | 10x AMD EPYC | 32 GB | 140 GB | Unlimited (US/NL); 1TB (HK) |
| VMA81 | €78.8 | €0.109 | 16x AMD EPYC | 64 GB | 200 GB | Unlimited (US/NL); 1TB (HK) |

LowEndBox special (LEB21): 4 GB RAM / 2 vCPU / 30 GB NVMe / Unlimited BW (US/NL) / 10 Gbps / 1x IPv4 + /64 IPv6 / KVM-Proxmox — €4.03/mo, hourly €0.00598. Corresponds to VMA21 in the standard tier list (price difference reflects promo discount).

## Add-ons
- Backups: €0.09/GB/mo
- Additional IPv4: €2.5/mo (or €0.00347/hour)
- Block storage: €0.15/GB/mo

## Host node specs (from LowEndBox Datacenter/Network section)
- AMD EPYC 7551P node: 512 GB RAM, 2× 2 TB SSD NVMe, 10 Gbit/s network
- AMD EPYC 7C13 node: 700 GB RAM, 2× 3 TB SSD NVMe, 10 Gbit/s network
- AMD EPYC 7663 node: 380 GB RAM, 4 TB SSD NVMe, 10 Gbit/s network

## Built-in features (from cloudblast.io homepage + pricing page)
- DDoS protection as standard (no separate subscription)
- 10 Gbps network port on every instance
- Hourly billing + prepaid plans
- Automatic backups (panel-managed)
- Self-service panel: deploy / delete / resize / rebuild
- Free /64 IPv6 on every plan
- IPv4 included (1 per instance)
- One-click apps: Coolify, CyberPanel, Dokploy, FastPanel, n8n, Nextcloud, Nginx, OpenClaw, Plausible, Pritunl, Pterodactyl, Supabase, Traefik, WordPress, Hermes Agent
- AI products: CloudTerm (free AI SSH/SFTP/RDP terminal), MCP Plug

## Differentiation vs vpstier-covered competitors
- vs **RackNerd** ($1.99/mo entry, unmanaged KVM) — Cloudblast starts €3.6/mo but includes **DDoS protection standard + 10 Gbps port** vs RackNerd's 1 Gbps + no bundled DDoS
- vs **Vultr** ($5/mo entry, NVMe, hourly) — Cloudblast undercuts at 4 GB tier (€4.8 vs Vultr's $24 for 4 GB); but Vultr has 32+ global DCs vs Cloudblast's 3
- vs **HostHatch** ($4/mo entry, EPYC, 14 regions) — Cloudblast cheaper at 4GB (€3.6) but HostHatch has 14 regions vs 3
- vs **Linode (Akamai)** ($5/mo Nanode) — Linode has 11+ DCs + mature GPU tiers; Cloudblast is bare-bones cheaper + DDoS included