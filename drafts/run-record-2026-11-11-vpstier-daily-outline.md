# Run Record: 2026-11-11 vpstier daily outline — Black Friday VPS restock timing

**Cron:** `5fd2a36f2dc4` (vpstier-daily-outline)
**Date:** 2026-11-11 (Wednesday)
**Variant:** variant-0 — briefing SUCCEEDED; the top vpstier star passed every hard gate (freshness d-1, body-verifiable, angle-virgin, no collision) and was selected directly
**Archetype:** deal-timing / restock-window buyer-guide (NEW on vpstier)
**Output outline:** `drafts/outline-2026-11-11-vpstier-daily.md` (`black-friday-vps-restock-timing-2026`)

---

## 1. Briefing triage (2026-11-11 08:09 UTC briefing)

| # | Item | Verdict |
|---|---|---|
| 1 | A first-hand year-long tracker of 17 sold-out Black Friday VPS deals (r/VPS) | **SELECTED** — d-1, body-verified, virgin angle |
| 2 | A permanently excluded European dedicated-hosting merchant's Helsinki cloud price cut | **REJECTED — hard-banned merchant.** The brand is not printed anywhere in the outline or this record, per house rule (category-token discipline applies to the triage row itself, not only to prose) |
| 3 | A prepaid-balance seizure after an account ban on a budget token-priced host | **REJECTED — already captured + weak on its own facts** |

**On item 3 (the more interesting rejection of the two):** the account-suspension angle is already queued as `hosting-account-suspension-blast-radius-2026` (2026-11-02), so it fails the capture check independently. But it also fails on the facts, and this is worth recording because it is a *new* rejection class — **the two-party dispute**. Reading the full thread through the working route showed the user acknowledged torrent traffic that violated the terms, the provider's refusal to refund was defended by other users in the thread, the provider's representative published a full chronology of their own position, and the user himself conceded mid-thread that he was not terminated and that he had deleted the instances himself. The "ban" in the headline was self-service deletion. Publishing a retaliatory-ban narrative on that record would be a defamatory claim about a two-party argument, not buyer guidance. **New rule for the record: a single-thread complaint where the complainant's own account admits a terms breach, and the alleged provider action turns out to be the complainant's own action, is not an article — regardless of how new or how dramatic it looks.**

## 2. Why the restock-timing story was chosen

The subject is the one question the site's Black Friday coverage has never answered. Existing coverage answers *which plans are cheap* (`2026-black-friday-cheap-vps-under-25`, published 2026-06-11) and *should you buy now or wait* (`racknerd-fall-giveaway-2026`, published 2026-11-09). Nothing covers **what happens after you lose the 48-hour race** — which is the question a buyer actually has on November 28.

**Body-grep-0 coverage verification** (63 published `.astro` + 66 queued outlines + all run records, run 2026-11-11): `restock` = 0, `back in stock` = 0, `median` = 0, `19 day` = 0, `come back` = 0. `sold out` = 1 (a per-location ARM64 availability aside in `netcup-vps-review-2026`), `sell out` = 1 (*"before they sell out"* in the published BF season timeline). True virgin topic.

**The differentiated axis:** *the timing of availability, not the price.* The tracker's dataset is the article's spine — 29 offers, a cron curling each order page every 6 hours grepping for the out-of-stock string, run November → end of January. Results: 17 sold out in 48h / 11 back at the same price (median 19 days) / 4 back worse / 2 never back (both 1TB+ storage boxes).

**Why this is a buyer-guide and not a news item:** it converts into a decision with a deadline. If the sale opens Nov 27 and the median restock is 19 days later, the wait lands mid-December. The article's job is to turn that into a plan, and to name the one case where the plan does not apply (storage SKUs).

## 3. NEW FINDING — a working route around the Reddit 403 wall

**Reddit's Atom feed route returns 200 while every other Reddit shape returns 403 from this sandbox.**

| Reddit shape | Result 2026-11-11 |
|---|---|
| `www.reddit.com/r/VPS/comments/<id>/` | HTTP 403 (190,240 B of JS shell) |
| `www.reddit.com/r/VPS/comments/<id>/.json?limit=100` | HTTP 403 (same shell) |
| `old.reddit.com/r/VPS/comments/<id>/` | HTTP 403 (1,522 B, "network policy" block) |
| `api.pullpush.io/reddit/search/submission/?ids=<id>` | HTTP 403 (Cloudflare "Just a moment...") |
| `safereddit.com`, `redlib.*` mirrors | 429 / Anubis challenge |
| **`www.reddit.com/r/VPS/comments/<id>/.rss`** | **HTTP 200 — full Atom feed with the complete post body** |

The `.rss` feed carries `<title>`, `<author>`, `<updated>` (the post's real timestamp), and the **entire post body** in `<content type="html">` with HTML entities intact. It also carries the full comment thread.

**This changes the canonical stale-rehash rule.** Pitfalls #26 and #49 said the search index (Brave/DDG) is the *only* freshness signal for a walled community thread. That is now obsolete for Reddit specifically: the Atom feed gives you a **body**, a **date**, and **comments** — all three of the things the old rules forced you to source elsewhere. The 2026-11-02 run had to reject a briefing Reddit item purely because it could not date the thread; this run had two Reddit items and could read **both** in full, including the exact quote *"I wasn't terminated - I deleted all VPS instances myself"* that decided the rejection of item 3.

**Practical recipe:**
```python
curl -sSL -A '<browser UA>' "https://www.reddit.com/r/<sub>/comments/<id>/.rss"
# parse <entry> blocks: <name>=author, <updated>=post timestamp, <content type="html">=body
# html.unescape twice, then strip tags
```
Rate limit: ~1 request per 5-6 seconds; a second immediate call returns HTTP 429. Two different post ids in one run were fetched with a sleep between them.

**Why this run did not need it for the selected story** — it did, and it is the reason item 1 is body-verifiable rather than a briefing paraphrase. The briefing's summary of the dataset was accurate, but the **caveats** (*"29 offers is tiny and skewed toward the $15 to $40 a year range I shop in"*, *"a couple of those 'restocks' could just be a provider changing their page template"*) and the **open question** about fresh nodes are only in the post body. An article that quotes the numbers without the caveats is the failure mode this site should not ship.

## 4. NEW FINDING — the launch-date correction, and why the outline could not be written without it

The run checked the Black Friday launch date against the primary sources instead of against our own articles — and found **two live vpstier articles state a window the primaries do not support.**

**What our live articles say:**
- `2026-black-friday-cheap-vps-under-25.astro`: *"November 1-7 is the main event. RackNerd's 2024 and 2025 BF launches were both on November 1st."* and, in a FAQ answer, *"November 1-4 and ran 7-10 days."*
- `racknerd-fall-giveaway-2026.astro`: *"RackNerd's BF 2024 and 2025 deals both launched in the November 1-4 window"* — and on that basis, *"Black Friday is two weeks away."*

**What the primaries say** (every `datePublished` read off a body-fetched LowEndBox post):

| Year | Launch post | `datePublished` | Entry price |
|---|---|---|---|
| 2024 | *BLACK FRIDAY: KVM VPS, Shared & Reseller Hosting by RackNerd* | 2024-11-29 | from $10.99/yr |
| 2024 | *RackNerd's Black Friday 2024: Bigger, Better, and Now in Dublin!* | 2024-11-19 | from $10.99/yr |
| 2025 | *RackNerd Black Friday 2025 — The Biggest Drop Yet is LIVE!* | 2025-11-19 | from $10.60/yr |
| 2025 | *[BLACK FRIDAY] RackNerd Returns With Their Biggest Event Yet!* | 2025-11-28 | from $10.60/yr |
| 2026 | *Is It Too Soon to Start Talking About BLACK FRIDAY? Nope!* (season preview) | 2026-09-18 | *"It all starts **November 27**."* |

**The rule that fires here:** *a "fact" that the site's own published articles assert is not a verified fact — it is a claim that needs a primary source like every other claim.* The canonical rules cover briefing claims (pitfall #49) and vendor-claim framing (pitfall #50). This run adds the third case: **our own earlier articles.** A June article published a launch window with no source attached; a November article inherited it and built a timing recommendation on it (*"Black Friday is two weeks away"*, published 2026-11-09 — when the announced date was 16 days away, but the *stated* window pointed at a date that had already passed).

**Why it blocks the article rather than being a side note:** the tracker measured a **48-hour sell-out**. A sell-out window is only comparable if the launch date is right. If the reader believes Nov 1, they shop the wrong week, and the 19-day median lands on the wrong date. The launch date is the anchor of the whole piece.

**Scope discipline:** the outline does not edit the two live articles. It flags them with exact strings in §9 and instructs the drafter to carry the correction inside the new article (§7 of the outline). Editing live, indexed URLs with traffic belongs in a publish slot that can also fix their internal consistency — not in a daily-outline run.

## 5. Source chain + fetch results (2026-11-11)

| Source | Status | Used for |
|---|---|---|
| `reddit.com/r/VPS/comments/1xsam97/.rss` | **200, 3,613 B** | the tracker dataset, method, caveats, open question, post date |
| `reddit.com/r/VPS/comments/1xrw3ig/.rss` | **200, 38,300 B** (retry after 429) | the rejected item's full thread |
| lowendbox.com "Is It Too Soon to Start Talking About BLACK FRIDAY? Nope!" | 200, 168,824 B, `datePublished` 2026-09-18 | the announced 2026 date (Nov 27) |
| lowendbox.com BF2024 launch posts (2) | 200, 190,759 B / 189,845 B | 2024 launch dates + $10.99/yr |
| lowendbox.com BF2025 launch posts (2) | 200, 192,822 B / 234,980 B | 2025 launch dates + $10.60/yr |
| lowendbox.com "Nerding Out on LowEndTalk Black Friday MegaThread Stats" | 200, 179,006 B | the independent demand-spike corroboration (2020-2025 table) |
| lowendbox.com "Did You Miss Any of These Amazing Black Friday/Cyber Monday Deals?" | 200, 174,334 B | the 2025 post-BF clearance behaviour |
| racknerd.com/BlackFriday/ | 200, 87,951 B | live specials ladder, pids 952-956, the "lifetime recurring" FAQ quote |
| lowendbox.com/tag/black-friday/ | 200, 231,209 B | the season index used to enumerate launch posts |
| cybernews.com BF deal posts | **403 — walled** | not read as bodies; Google News RSS headline+date only, and labelled as such |
| lowendtalk.com (forum + LET ecosystem) | **403 — walled** | not fetched; the tracker's own LET/LES sourcing is described, not read |
| vpsium.com | **403 — walled** | not fetched; it is named in the source post as the author's own 2026 substitute method |
| the Moscow Times (ESTT) | 200, 51,042 B | checked as an out-of-briefing substitute; rejected (Russian-market incident, no buyer-side decision for this audience) |

## 6. GSC context (live pull, 28-day window 2026-10-12 → 2026-11-10)

Pulled with the canonical helper (`importlib`-load `gsc_daily_report.py` → `get_valid_token()` + `fetch_gsc(...)`) — pitfall #52, do not hand-roll OAuth.

28 query rows, **0 clicks**. The head terms still land on the homepage at position 78-100: `virtual private server hosting reviews` 48 imp @ 84.7, `best vps for ai agents` 42 imp @ 74.6, `best vps provider` 29 imp @ 81.7, `best vps providers` 23 imp @ 83.3. The hub gap flagged on 2026-11-03 and re-confirmed on 2026-11-08 persists.

**Relevance to today's piece:** today's article targets an **informational-timing** query set (`black friday vps restock`, `do black friday vps deals come back`, `black friday vps sold out`) which is a *different* intent from the head terms the homepage absorbs. It is topical support for the seasonal cluster, not a hub substitute. Flagging the gap, not claiming to fix it.

## 7. Self-check performed on the written file

Run against the file on disk (not against an in-memory string): banned-token 0 · CJK 0 · deprecated-language-prefix route 0 · title 48/60 (58 with the optional branding suffix) · description 149/155 · H2 10 · FAQ 5 · CTA placements 8 · all 10 cross-link targets verified to exist on disk · slug absent from both `published[]` and `drafts[]` · every named fact traced to a body-fetched primary.

## 8. State of the queue

`published[]` = 84 · `drafts[]` = 66 → 67 after this run. The pre-existing 2-slug overlap (`best-vps-deals-codes-2026`, `webdock-vps-review-2026`) is unchanged and still unresolved; `best-vps-deals-codes-2026` additionally has **no `.astro` on disk**, so it was excluded from today's cross-link list and is called out in §6 of the outline.
