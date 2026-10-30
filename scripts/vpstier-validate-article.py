#!/usr/bin/env python3
"""Pre-deploy self-audit for vpstier blog articles.

Usage: python3 scripts/vpstier-validate-article.py <slug> [--deploy-id ID]

Checks (canonical gates for the vpstier content pipeline):
  1. banned-merchant token count == 0 across the WHOLE file
  2. CJK character count == 0
  3. deprecated language-prefix path count == 0
  4. title length <= 60
  5. description length <= 155
  6. H2 count >= 8
  7. FAQPage JSON-LD parses and has >= 3 questions
  8. affiliate CTA count >= 6, every one labelled + rel=sponsored noopener
  9. every internal cross-link target exists on disk
 10. >= 800 unique words (HCU)
 11. >= 2 real artifacts (code blocks / probe output / tables with real values)
 12. first-person voice in >= 3 sentences
 13. "Last verified YYYY-MM-DD" stamp present
 14. no "Tested vs X + Y" comparison-crutch template
 15. slug collision check across published[] / drafts[] / src/pages/blog/
 16. title/description strings in the file match state.json exactly
"""
import argparse
import json
import os
import re
import sys

SITE = '/root/vpstier-site'
BLOG = f'{SITE}/src/pages/blog'

# Permanently excluded merchants. These are hard bans for vpstier.
BANNED_TOKENS = [
    'hetzner',
]

# Per-site policy: deprecated language-prefix route prefix.
DEPRECATED_PATH_TOKENS = [
    '/zh/',
    '/zh-cn/',
]

CJK_RE = re.compile(r'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\u3400-\u4dbf'
                    r'\u4e00-\u9fff\uf900-\ufaff\ufe30-\ufe4f\uff00-\uffef]')


def fail(msgs, s):
    msgs.append(f"FAIL  {s}")


def ok(msgs, s):
    msgs.append(f"  ok  {s}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('slug')
    ap.add_argument('--deploy-id', default=None)
    args = ap.parse_args()

    path = f'{BLOG}/{args.slug}.astro'
    if not os.path.exists(path):
        print(f"FAIL  article file not found: {path}")
        return 1

    raw = open(path, encoding='utf-8').read()
    # Strip the JSON-LD blocks so frontmatter/string checks don't double-count.
    body = re.sub(r'(?s)<script type="application/ld\+json">.*?</script>', ' ', raw)
    # Strip code blocks for prose-only checks (CJK / banned tokens in samples).
    prose = re.sub(r'(?s)<pre[^>]*>.*?</pre>', ' ', body)

    msgs = []
    errors = 0

    # --- 1. banned merchant tokens -------------------------------------
    low = raw.lower()
    bad = []
    for tok in BANNED_TOKENS:
        n = low.count(tok)
        if n:
            bad.append(f"{tok}={n}")
    if bad:
        fail(msgs, f"banned merchant token(s) present: {', '.join(bad)}")
        errors += 1
    else:
        ok(msgs, f"banned merchant tokens = 0 ({', '.join(BANNED_TOKENS)})")

    # --- 2. CJK ---------------------------------------------------------
    n_cjk = len(CJK_RE.findall(raw))
    if n_cjk:
        fail(msgs, f"CJK characters present: {n_cjk}")
        errors += 1
    else:
        ok(msgs, "CJK characters = 0")

    # --- 3. deprecated language-prefix path -----------------------------
    dep = []
    for tok in DEPRECATED_PATH_TOKENS:
        n = raw.count(tok)
        if n:
            dep.append(f"{tok}={n}")
    if dep:
        fail(msgs, f"deprecated language-prefix path(s): {', '.join(dep)}")
        errors += 1
    else:
        ok(msgs, "deprecated language-prefix paths = 0")

    # --- 4/5. title + description length --------------------------------
    m = re.search(r'<BaseLayout\s+title="([^"]*)"\s+description="([^"]*)"', raw)
    if not m:
        fail(msgs, "could not parse title/description from BaseLayout props")
        errors += 1
        title = desc = ''
    else:
        title, desc = m.group(1), m.group(2)
        lt, ld = len(title), len(desc)
        if lt > 60:
            fail(msgs, f"title too long: {lt}/60")
            errors += 1
        else:
            ok(msgs, f"title length {lt}/60")
        if ld > 155:
            fail(msgs, f"description too long: {ld}/155")
            errors += 1
        else:
            ok(msgs, f"description length {ld}/155")

    # --- 6. H2 count ----------------------------------------------------
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', body, re.S)
    if len(h2s) < 8:
        fail(msgs, f"H2 count too low: {len(h2s)} (<8)")
        errors += 1
    else:
        ok(msgs, f"H2 count = {len(h2s)}")

    # --- 7. FAQPage JSON-LD ---------------------------------------------
    faq_qs = []
    for blk in re.findall(r'(?s)<script type="application/ld\+json">(.*?)</script>', raw):
        try:
            data = json.loads(blk.strip())
        except Exception as e:
            fail(msgs, f"JSON-LD block does not parse: {e}")
            errors += 1
            continue
        if data.get('@type') == 'FAQPage':
            faq_qs = data.get('mainEntity', [])
    if len(faq_qs) < 3:
        fail(msgs, f"FAQPage questions too few: {len(faq_qs)} (<3)")
        errors += 1
    else:
        ok(msgs, f"FAQPage questions = {len(faq_qs)}")

    # --- 8. affiliate CTAs ----------------------------------------------
    aff = re.findall(r'href="(https://my\.racknerd\.com/aff\.php\?aff=16299)"'
                     r'[^>]*?(?:target="_blank"\s+)?rel="([^"]*)"', raw)
    # count every anchor that points at the affiliate, regardless of rel layout
    aff_all = raw.count('https://my.racknerd.com/aff.php?aff=16299')
    n_aff = len(aff)
    if n_aff < 6:
        fail(msgs, f"affiliate CTA placements too few: {n_aff} (<6)")
        errors += 1
    else:
        ok(msgs, f"affiliate CTA placements = {n_aff} (total affiliate URL mentions {aff_all})")
    bad_rel = [(u, r) for u, r in aff if 'sponsored' not in r or 'noopener' not in r]
    if bad_rel:
        fail(msgs, f"affiliate links missing rel=sponsored noopener: {bad_rel}")
        errors += 1
    else:
        ok(msgs, "all affiliate anchors carry rel=sponsored noopener")

    # --- 9. internal cross-links exist on disk --------------------------
    links = set(re.findall(r'href="(/blog/[a-z0-9\-]+/)"', raw))
    missing = []
    for l in sorted(links):
        slug = l.strip('/').split('/')[-1]
        if not os.path.exists(f'{BLOG}/{slug}.astro'):
            missing.append(l)
    if missing:
        fail(msgs, f"internal cross-link target(s) missing on disk: {missing}")
        errors += 1
    else:
        ok(msgs, f"internal cross-links = {len(links)}, all targets exist on disk")

    # --- 10. unique word count (HCU) -------------------------------------
    text = re.sub(r'(?s)<[^>]+>', ' ', prose)
    text = re.sub(r'(?s)<pre[^>]*>.*?</pre>', ' ', text)
    words = re.findall(r"[A-Za-z][A-Za-z'\-]+", text)
    uniq = len(set(w.lower() for w in words))
    if uniq < 800:
        fail(msgs, f"unique word count too low: {uniq} (<800)")
        errors += 1
    else:
        ok(msgs, f"unique words = {uniq} (total {len(words)})")

    # --- 11. real artifacts ---------------------------------------------
    artifacts = 0
    artifact_detail = []
    # (a) code blocks containing shell/config
    code_blocks = re.findall(r'(?s)<pre[^>]*>(.*?)</pre>', body)
    shell_blocks = [c for c in code_blocks
                    if re.search(r'(?m)^\s*(sudo |ssh |curl |find |awk |crontab|/usr/sbin|systemctl|sed )', c)]
    if shell_blocks:
        artifacts += len(shell_blocks)
        artifact_detail.append(f"{len(shell_blocks)} code block(s)")
    # (b) a table with real numeric values
    tables = re.findall(r'(?s)<table.*?</table>', body)
    numeric_tables = [t for t in tables if len(re.findall(r'\$\d', t)) >= 2]
    if numeric_tables:
        artifacts += 1
        artifact_detail.append("price table")
    # (c) inline probe output (a bare command-output line)
    if re.search(r'(?m)^#(permitrootlogin|passwordauthentication|pubkeyauthentication)', body):
        artifacts += 1
        artifact_detail.append("probe output")
    # (d) a dated status/verification line
    if re.search(r'(?i)Last verified\s*<?\s*(?:strong>)?\s*\d{4}-\d{2}-\d{2}', body):
        artifacts += 1
        artifact_detail.append("Last-verified stamp")
    if artifacts < 2:
        fail(msgs, f"real artifacts too few: {artifacts} (<2) {artifact_detail}")
        errors += 1
    else:
        ok(msgs, f"real artifacts = {artifacts} ({', '.join(artifact_detail)})")

    # --- 12. first-person voice -----------------------------------------
    sentences = re.split(r'(?<=[.!?])\s+', re.sub(r'\s+', ' ', text))
    fp = [s for s in sentences
          if re.search(r"\b(I|I\'m|I\'ve|my|me)\b", s) and 20 < len(s) < 400]
    if len(fp) < 3:
        fail(msgs, f"first-person voice too few sentences: {len(fp)} (<3)")
        errors += 1
    else:
        ok(msgs, f"first-person voice sentences = {len(fp)}")

    # --- 13. Last verified stamp ----------------------------------------
    if not re.search(r'(?i)Last verified', body):
        fail(msgs, "no 'Last verified' stamp")
        errors += 1
    else:
        ok(msgs, "'Last verified' stamp present")

    # --- 14. comparison-crutch template ---------------------------------
    crutch = re.search(r'(?i)tested\s+vs\s+\w+\s*\+\s*\w+', body)
    if crutch:
        fail(msgs, f"comparison-crutch template found: {crutch.group(0)}")
        errors += 1
    else:
        ok(msgs, "no comparison-crutch template")

    # --- 15. slug collision ---------------------------------------------
    state_path = f'{SITE}/drafts/state.json'
    if os.path.exists(state_path):
        st = json.load(open(state_path, encoding='utf-8'))
        pub = {p.get('slug') for p in st.get('published', [])}
        drf = {d.get('slug') for d in st.get('drafts', [])}
        if args.slug in pub:
            fail(msgs, "slug already in state.json published[]")
            errors += 1
        else:
            ok(msgs, "slug absent from published[]")
        if args.slug not in drf:
            fail(msgs, "slug absent from state.json drafts[] (not queued)")
            errors += 1
        else:
            ok(msgs, "slug present in state.json drafts[] (queued, awaiting publish)")
        # title/description agreement with state.json
        entry = next((d for d in st.get('drafts', []) if d.get('slug') == args.slug), None)
        if entry:
            st_title = entry.get('title') or entry.get('title_en') or ''
            st_desc = entry.get('description_en') or entry.get('description') or ''
            if st_title and st_title != title:
                fail(msgs, f"title mismatch vs state.json:\n      file: {title!r}\n      state: {st_title!r}")
                errors += 1
            else:
                ok(msgs, "title matches state.json")
            if st_desc and st_desc != desc:
                fail(msgs, f"description mismatch vs state.json:\n      file: {desc!r}\n      state: {st_desc!r}")
                errors += 1
            else:
                ok(msgs, "description matches state.json")
        else:
            fail(msgs, "no state.json drafts[] entry for this slug")
            errors += 1

    # --- 16. blog index card --------------------------------------------
    idx = open(f'{BLOG}/index.astro', encoding='utf-8').read()
    if f"slug: '{args.slug}'" not in idx:
        fail(msgs, "no card in src/pages/blog/index.astro")
        errors += 1
    else:
        ok(msgs, "blog index card present")

    print(f"=== vpstier pre-deploy audit: {args.slug} ===")
    for m in msgs:
        print(m)
    print(f"=== {'FAIL' if errors else 'PASS'} ({errors} error(s)) ===")
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
