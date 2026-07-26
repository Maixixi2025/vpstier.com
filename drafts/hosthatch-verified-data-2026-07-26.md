# HostHatch verified data — 2026-07-26

## Official sources checked
- https://hosthatch.com/products
- https://docs.hosthatch.com/features/
- https://docs.hosthatch.com/networking/
- https://docs.hosthatch.com/api/
- https://hosthatch.com/terms-of-service
- https://hosthatch.com/contact
- https://status.hosthatch.com/

## Editorially safe facts
- HostHatch LLC, Tampa, Florida mailing address.
- Current official documentation matrix lists 14 compute regions: Amsterdam, Chicago, Hong Kong, London, Los Angeles, New York, Oslo, Seoul, Singapore, Stockholm, Sydney, Tokyo, Vienna, Zurich.
- Compute plans advertise AMD EPYC CPUs and NVMe storage, starting at $4/mo for 2GB RAM, 10GB NVMe, 1 fair-share core, and up to 1TB transfer (500GB in several APAC locations).
- Value points: 8GB/$9, 16GB/$15, 32GB/$29; 96GB plan advertised at $69/mo.
- Storage VMs start at $5/mo for 1TB HDD and reach $38/mo for 10TB.
- Routed public IPv6 /64 per VM; same-region VLAN/VXLAN private networking; private traffic excluded from public transfer; jumbo frames up to MTU 9000.
- Public API documentation exists, but access is limited to selected users.
- Seven-day VPS refund policy is conditional on a documented HostHatch-caused fault; it is not a no-questions-asked trial.
- Public material reviewed does not state a contractual uptime percentage or service-credit schedule.
- Inbound and outbound traffic both count toward transfer; overage is listed at $4/TB and exhausted VMs may be rate-limited to 5Mbps.

## Do not claim
- Do not publish an uptime percentage or SLA credit schedule.
- Do not claim unrestricted API access.
- Do not claim all regions have identical transfer quotas.
- Do not claim a specific hypervisor unless separately verified.
- Do not claim snapshots, backups, or block storage are currently available without account-level confirmation.
- Do not claim payment methods beyond what is explicitly confirmed.

## Selection rationale
Task-prompt suggestions were stale/covered. HostHatch fills a useful gap: high-RAM AMD EPYC pricing, 1TB storage VMs, broad non-mainstream regional coverage, routed IPv6, and private networking. It was selected over weaker or unverified candidates because its current documentation exposes a usable product and region matrix.
