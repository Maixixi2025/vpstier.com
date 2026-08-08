# vpstier Add-Provider-and-Review Run — 2026-08-08 (Linode / Akamai Connected Cloud)

## Result: SUCCESS

**Provider added:** Linode (developer-favorite cloud since 2003, Akamai-powered since 2022)

### Why Linode (dead-card repair priority)
The prompt's suggested provider list was STALE — all 13 suggested candidates (A2, Bluehost,
FastComet, ScalaHosting, ChemiCloud, DreamHost, GreenGeeks, SiteGround, HostPapa, InMotion,
TurnKey Internet, ServerPeacock, ZAP VPS) were already covered (51 providers on disk). Per the
vpstier runbook, I prioritized an actual **dead card**: `src/pages/vps/index.astro` had a card
linking to `/vps/linode` with NO `linode.astro` page — a Cloudflare soft-404 (HTTP 200 + homepage
fallback). **Linode** was chosen: highest-rating (4.5) dead card, major recognizable provider,
abundant verifiable public data.

### Files created
- `src/pages/vps/linode.astro` (provider card page, 7,003B → built 14,595B)
- `src/pages/blog/linode-vps-review-2026.astro` (long-form review, 18,776B → built 26,120B)
- `drafts/vpstier-add-provider-2026-08-08-linode.md` (this file)

### Files modified
- `src/data/providers.json` (+features[8] +vpsPlans[6] to existing linode entry)
- `src/pages/blog/index.astro` (+1 card at top of `const posts` array)

### Build
`NODE_OPTIONS=--max-old-space-size=768 npm run build` → **106 pages built** in 3.51s ✅
(the alias-sitemap post-build step also ran → dist/sitemap.xml with 106 URLs)

### Deploy
`npx wrangler pages deploy dist --project-name=vpstier-com --commit-dirty=true` →
**109 files uploaded (6 already)** in 3.35s ✅, deployment ID `aa40a306`
Preview: https://aa40a306.vpstier-com.pages.dev

### Pre-deploy drift check (CRITICAL)
Live sitemap: blog=43, vps=51. Local disk: blog=44, vps=52.
`live_only = []` → no live page would be deleted by the deploy. ✅

### Live URLs (verified HTTP 200 + correct title, 2026-08-08)
- https://vpstier.com/vps/linode/ (14,595B, title "Linode VPS Review 2026: $5/mo Nanode to $192/mo Plans")
- https://vpstier.com/blog/linode-vps-review-2026/ (26,120B, title "Linode VPS Review 2026: $5/mo Nanode to $192/mo Plans")
- /vps/ index now resolves the (previously dead) linode card → real page ✅
- Sitemap-0.xml + /sitemap.xml alias both 106 URLs incl both new pages ✅ (after ~40s propagation)
- Blog schema: FAQPage (5 Q) + Article + BreadcrumbList ✅

### Verified Data (2026-08-08)
- **Provider:** Linode (Akamai Connected Cloud); founded 2003; Akamai acquisition 2022 ($900M)
- **Entry:** Nanode 1GB $5/mo (1 vCPU, 1GB RAM, 25GB SSD, 1TB transfer), $0.0075/hr
- **Shared plans:** 2GB $12, 4GB $24, 8GB $48, 16GB $96 (NVMe begins here), 32GB $192
- **Networking:** 40Gbps uplinks, hourly + monthly billing, transparent renewal (intro=renewal)
- **Datacenters:** 11+ global (9 US + Frankfurt/London/Mumbai/Singapore/Sydney/Tokyo/Osaka)
- **Ecosystem:** Object Storage (S3), NodeBalancers, Block Storage, LKE K8s, API/CLI/Terraform
- **Missing:** no Windows, no custom ISO, no on-demand snapshots, no GPU on shared plans
- Sources: Akamai techdocs (shared-cpu page, official) + bestusavps.com 2026 review (verified plan table)

### Metrics validation (script)
- vps page: title 53/60, desc 145/155
- blog: title 53/60, desc 152/155, words 1418 (within site range 1369-2316), H2 x10, FAQ 5
- All internal links resolve (racknerd, vultr, hostinger, racknerd-deep-review confirmed on disk)

### Banned-provider self-audit: PASS
No Hetzner. No banned provider in any created/modified file. All CTAs → RackNerd affiliate link
(https://my.racknerd.com/aff.php?aff=16299) per policy.

### Hygiene: committed orphaned-but-live sources first (CRITICAL)
Prior add-provider runs (7-29 serverpeacock, 7-31 cloudzy, 8-03 hostarmada/1984/vpsdime) deployed
pages via wrangler but NEVER git-committed the sources. Commit `338b415` added 15 files
(5 provider .astro + 4 blog .astro + 2 prior run records + cloudzy data + package.json build-alias
+ pnpm-lock + scripts/alias-sitemap.mjs) BEFORE today's work, so a working-tree reset cannot
destroy the live-but-uncommitted pages (per the "commit after every publish" rule).

### state.json reconciliation
- Appended `linode-vps-review-2026` add-provider-and-review entry (published count 64→65)
- Reconciled STALE 2026-06-16 `linode` entry: it claimed `en_astro: src/pages/vps/linode.astro`
  existed, but the page was never created (dead card). Corrected published_at → 2026-08-08,
  added `reconciled_2026_08_08` note, set live_verified + deployment_id.
