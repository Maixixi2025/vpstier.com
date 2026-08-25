#!/usr/bin/env node
// Post-build: alias Astro's @astrojs/sitemap output as /sitemap.xml + /sitemap-v2.xml.
//
// Why: @astrojs/sitemap writes /sitemap-index.xml + /sitemap-N.xml by default.
// Many tools (GSC, Ahrefs, Bing, etc.) probe /sitemap.xml — without an alias,
// they 404 (or worse, fall through to the homepage, which manifests in GSC as
// "9 pages indexed" — the homepage's internal links).
//
// Strategy: merge all generated sitemap chunks into both /sitemap.xml and
// /sitemap-v2.xml so:
//   - /sitemap.xml preserves existing GSC submission (no churn)
//   - /sitemap-v2.xml gives GSC a fresh path to crawl when the old sitemap
//     stats are stuck (forces a fresh download + contents recompute).
// If content grows beyond the integration's entryLimit (default 45k), this
// script still works — it just merges more chunks.
//
// Idempotent. Safe to re-run. Run after `astro build`.

import { readFile, writeFile, readdir } from 'node:fs/promises';
import { join } from 'node:path';

const DIST = new URL('../dist/', import.meta.url).pathname;

async function main() {
  const files = await readdir(DIST);
  const chunks = files.filter(f => /^sitemap-\d+\.xml$/.test(f)).sort();

  if (chunks.length === 0) {
    console.error('[alias-sitemap] No sitemap-N.xml chunks found, skipping');
    process.exit(0);
  }

  // Extract every <loc>...</loc> from each chunk and re-emit as a single
  // <urlset>. Keeps lastmod per URL.
  const allLocs = [];
  for (const f of chunks) {
    const xml = await readFile(join(DIST, f), 'utf8');
    const urlBlocks = xml.match(/<url>[\s\S]*?<\/url>/g) || [];
    for (const block of urlBlocks) {
      const locMatch = block.match(/<loc>([^<]+)<\/loc>/);
      const lastmodMatch = block.match(/<lastmod>([^<]+)<\/lastmod>/);
      if (locMatch) {
        const lastmod = lastmodMatch ? `<lastmod>${lastmodMatch[1]}</lastmod>` : '';
        allLocs.push(`<url><loc>${locMatch[1]}</loc>${lastmod}</url>`);
      }
    }
  }

  const out = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allLocs.join('\n')}
</urlset>
`;

  // Write both paths. /sitemap.xml preserves any existing GSC submission;
  // /sitemap-v2.xml gives GSC a fresh path to crawl (workaround for GSC stale
  // stats issue where submitted/indexed counters don't refresh).
  await writeFile(join(DIST, 'sitemap.xml'), out, 'utf8');
  await writeFile(join(DIST, 'sitemap-v2.xml'), out, 'utf8');
  console.log(`[alias-sitemap] Wrote dist/sitemap.xml + dist/sitemap-v2.xml with ${allLocs.length} URLs (from ${chunks.length} chunks)`);
}

main().catch(err => {
  console.error('[alias-sitemap] Failed:', err);
  process.exit(1);
});
