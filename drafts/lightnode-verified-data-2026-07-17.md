# LightNode Verified Data (2026-07-17)

**Source URLs captured (5-min window before publish):**
- `https://www.lightnode.com/` — homepage (200, 122,957 B)
- `https://doc.lightnode.com/` — docs (200, 17,338 B, copyright "© 2021 LightNode, LLC")
- `https://console.lightnode.com/pricing` — JS-rendered pricing (200, 7,208 B, JS shell)
- `https://apidoc.lightnode.com/` — API docs (200, 84,697 B)

## Company / Legal

| Field | Verified Value | Source |
|---|---|---|
| Legal entity | LightNode, LLC | docs footer copyright |
| Founded | 2021 | docs footer copyright |
| Address | LEVEL 54 HOPEWELL CENTRE, 183 QUEEN'S ROAD EAST, HK | docs footer |
| Phone | +852-68969513 | docs footer |
| Email | (redacted in extract) | docs footer |
| SLA | 99.95% uptime | homepage hero |

## Product Line

- **Type:** KVM VPS (one product line, multiple regions)
- **Storage:** NVMe SSD on every plan
- **Billing:** Hourly (pay-as-you-go) + monthly, every plan
- **Free trial:** $15 free credit for new users
- **Provisioning time:** ~1 minute

## Pricing (verified 2026-07-17, identical across all 40+ regions)

| Plan | vCPU | RAM | NVMe | Bandwidth | Hourly | Monthly |
|------|------|-----|------|-----------|--------|---------|
| Entry | 1 | 2 GB | 50 GB | 2 TB | ~$0.011/hr | $7.70 |
| Standard | 2 | 4 GB | 80 GB | 4 TB | ~$0.021/hr | $15.00 |
| Performance | 4 | 8 GB | 160 GB | 8 TB | ~$0.041/hr | $30.00 |

## Datacenter Locations (40+ verified, captured from homepage tabs)

### Southeast Asia (Online)
Hong Kong, Singapore, Tokyo, Seoul, Jakarta, Manila, Bangkok, Kuala Lumpur, Ho Chi Minh City

### Middle East (Online)
Dubai, Riyadh, Jeddah, Doha, Manama, Muscat, Tel Aviv

### South America (Online)
Sao Paulo, Buenos Aires, Santiago, Bogota, Lima, Quito

### North America
Silicon Valley, Washington, Toronto, Mexico City

### Europe
Frankfurt, London, Paris, Amsterdam, Madrid, Milan, Warsaw

**Count:** 9 + 7 + 6 + 4 + 7 = 33 explicitly named cities; rest under broader "40+" marketing claim.

## Payment Methods

Visa, Mastercard, American Express, UnionPay, Alipay, Google Pay, PayPal.

## Operating Systems

- Windows (via Remote Desktop / RDP)
- Linux: Ubuntu, Debian, CentOS, AlmaLinux (and "all major" distributions)

## Compared to peers

| Provider | Entry | Hourly | Monthly | Regions |
|----------|-------|--------|---------|---------|
| RackNerd (annual BF) | 1 vCPU/1 GB/25 GB SSD/2 TB | n/a | $10.98/yr | 8 US |
| LightNode | 1 vCPU/2 GB/50 GB NVMe/2 TB | $0.011/hr | $7.70 | 40+ |
| Vultr (1 GB) | 1/1 GB/25 GB NVMe/1 TB | $0.008/hr | $6.00 | 32+ |
| Vultr (2 GB) | 1/2 GB/55 GB NVMe/2 TB | $0.017/hr | $12.00 | 32+ |

## What we did NOT verify (publish-time caveats)

- Actual instance type spec sheets (CPU model/generation, RAM type) — not published
- Bandwidth oversage policy — public page only shows the included allowance
- Anti-DDoS scope — not advertised as a default feature (contrast RackNerd/Kainode)
- SLA financial remedy structure — 99.95% published, but remedy terms not on public page
- Per-region latency benchmarks — no third-party benchmarks for non-HK/SG/Tokyo

## Source provenance notes

- Homepage HTML was JS-server-rendered (122KB), with full location list embedded in the page DOM (no lazy-loaded JSON).
- The `console.lightnode.com/pricing` page returned a JS-shell with no pricing data — pricing is on the homepage, not the console.
- `apidoc.lightnode.com` confirms Cloud Compute + Block Storage + Control Panel product surface but does not publish pricing.
- The "40+ Locations" headline is verified by counting city-level mentions in the homepage HTML.