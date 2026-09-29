#!/usr/bin/env python3
"""Publish-artifact enhancements that the generator does not ship natively.

Runs in `make publish` after the build (and after strip-internal-nofollow).
Idempotent: safe to re-run on an already-enhanced artifact.

  1. hreflang: adds en / zh-CN / x-default alternates to every content page
     that has a counterpart in the other language tree.
  2. Graph page: injects the site theme override stylesheet and replaces the
     em dash in its title with a hyphen.
  3. Search index: regenerates search.json `s` fields from full body text so
     the built-in client matches body content, not just headings.
  4. Taxonomy archives: drops the duplicated heading and adds a page count
     on term archives.
  5. Sitemap: ensures /graph/ is listed.
"""
import html as html_mod
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
SITE = "https://z.filed.fyi"

changed = {}


def bump(key, n=1):
    changed[key] = changed.get(key, 0) + n


# ---------- 1) hreflang ----------
for p in PUB.rglob("index.html"):
    rel = p.relative_to(PUB).as_posix()
    if rel.startswith("tags/") or rel.startswith("categories/"):
        continue
    page_url = "/" + rel[: -len("index.html")]
    if page_url == "/graph/":
        continue
    if page_url.startswith("/zh/"):
        en_url = page_url[3:]
        zh_url = page_url
    else:
        en_url = page_url
        zh_url = "/zh" + page_url
    en_file = PUB / "index.html" if en_url == "/" else PUB / en_url.strip("/") / "index.html"
    zh_file = PUB / zh_url.strip("/") / "index.html"
    if not (en_file.exists() and zh_file.exists()):
        continue
    text = p.read_text(encoding="utf-8")
    if 'hreflang="x-default"' in text:
        continue
    links = (
        f'<link rel="alternate" hreflang="en" href="{SITE}{en_url}">\n'
        f'<link rel="alternate" hreflang="zh-CN" href="{SITE}{zh_url}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{SITE}{en_url}">\n'
    )
    if "</head>" in text:
        p.write_text(text.replace("</head>", links + "</head>", 1), encoding="utf-8")
        bump("hreflang_pages")

# ---------- 2) graph page ----------
gp = PUB / "graph/index.html"
if gp.exists():
    t = gp.read_text(encoding="utf-8")
    orig = t
    if "/assets/css/graph-theme.css" not in t:
        t = t.replace(
            '<link rel="stylesheet" href="../assets/graph/explorer.css">',
            '<link rel="stylesheet" href="../assets/graph/explorer.css">\n'
            '<link rel="stylesheet" href="../assets/css/graph-theme.css">',
            1,
        )
    t = t.replace("Knowledge Graph — Z.ai Field Guide", "Knowledge Graph - Z.ai Field Guide")
    if t != orig:
        gp.write_text(t, encoding="utf-8")
        bump("graph_page")

# ---------- 3) search index ----------
sj = PUB / "search.json"
if sj.exists():
    items = json.loads(sj.read_text(encoding="utf-8"))
    updated = 0
    for item in items:
        u = item.get("u", "")
        if not isinstance(u, str) or not u:
            continue
        if u.endswith("/"):
            f = PUB / "index.html" if u == "/" else PUB / u.strip("/") / "index.html"
        else:
            f = PUB / u.lstrip("/")
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8")
        m = re.search(r"<main\b.*?</main>", text, re.S)
        if not m:
            continue
        body = re.sub(r"<(script|style)\b.*?</\1>", " ", m.group(0), flags=re.S | re.I)
        body = re.sub(r"<[^>]+>", " ", body)
        body = html_mod.unescape(body)
        body = re.sub(r"\s+", " ", body).strip()
        if len(body) < 40:
            continue
        item["s"] = body[:1600]
        updated += 1
    if updated:
        sj.write_text(json.dumps(items, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        bump("search_items", updated)

# ---------- 4) taxonomy archives ----------
tax_pages = list((PUB / "tags").rglob("index.html")) + list((PUB / "categories").rglob("index.html"))
for p in tax_pages:
    t = p.read_text(encoding="utf-8")
    orig = t
    m = re.search(r'<h1 class="z-title">([^<]*)</h1>.*?<h2>([^<]*)</h2>', t, re.S)
    if m and m.group(1).strip() == m.group(2).strip():
        h1 = m.group(1).strip()
        t = t.replace(f"<h2>{m.group(2)}</h2>", "", 1)
        if h1.startswith(("Tag: ", "Category: ")):
            in_prose = t.split('<div class="z-prose"', 1)[-1]
            n = in_prose.count("<li>")
            if n:
                t = t.replace(
                    '<div class="z-prose">',
                    f'<div class="z-prose">\n<p class="tax-count">{n} pages</p>',
                    1,
                )
    if t != orig:
        p.write_text(t, encoding="utf-8")
        bump("taxonomy_pages")

# ---------- 5) sitemap ----------
sm = PUB / "sitemap.xml"
if sm.exists():
    x = sm.read_text(encoding="utf-8")
    if f"{SITE}/graph/" not in x and "</urlset>" in x:
        x = x.replace("</urlset>", f"  <url><loc>{SITE}/graph/</loc></url>\n</urlset>", 1)
        sm.write_text(x, encoding="utf-8")
        bump("sitemap")

# ---------- 6) search client: rank matches, raise the cap ----------
sjs = PUB / "assets/js/search.js"
if sjs.exists():
    t = sjs.read_text(encoding="utf-8")
    if "laFamilleSearchScoreV1" not in t and t.count("}).slice(0, 7);") == 1:
        repl = """}).map(item => {
                    const t = (item.t || "").toLowerCase();
                    const g = (item.g || []).some(x => x.toLowerCase().includes(query));
                    const h = (item.h || []).some(x => x.toLowerCase().includes(query));
                    const s = (item.s || "").toLowerCase().includes(query);
                    let score = 0;
                    if (t.includes(query)) score += 8;
                    if (g) score += 4;
                    if (h) score += 2;
                    if (s) score += 1;
                    return { item, score }; /* laFamilleSearchScoreV1 */
                }).sort((x, y) => y.score - x.score).map(x => x.item).slice(0, 12);"""
        t2 = t.replace("}).slice(0, 7);", repl, 1)
        if t2 != t:
            sjs.write_text(t2, encoding="utf-8")
            bump("search_client")

# ---------- 6b) search client: emit theme classes, not Tailwind utilities ----------
# The generator's search.js is written against Tailwind (`line-clamp-2`,
# `badge-xs`, `text-primary`, ...). This theme ships no Tailwind, so every one
# of those classes resolves to nothing: results lose their clamp, their accent
# colour, their tag chips, and their separators, and the whole snippet renders
# as one underlined block at body size. assets/css/zai.css already carries a
# complete set of `.search-result-*` rules that nothing was ever emitting.
#
# Remap the emitted class names onto those existing rules rather than adding a
# Tailwind shim, so the results match the rest of the theme. Idempotent: each
# rewrite is guarded by the source string being present.
CLASS_REMAP = {
    'className = "block p-4 hover:bg-base-200 text-sm focus-visible:bg-base-200 '
    'focus-visible:outline-none border-b border-base-200 last:border-0"':
        'className = "search-result-link"',
    'className = "font-bold text-base-content"':
        'className = "search-result-title"',
    'className = "text-xs font-medium text-primary mt-0.5"':
        'className = "search-result-section"',
    'className = "text-xs text-base-content/70 mt-1 line-clamp-2"':
        'className = "search-result-snippet"',
    'className = "flex flex-wrap gap-1 mt-1.5"':
        'className = "search-result-tags"',
    'className = "badge badge-xs badge-ghost text-[10px]"':
        'className = "search-result-tag"',
    'className = "p-2 text-base-content/50"':
        'className = "search-no-results"',
}

sjs2 = PUB / "assets/js/search.js"
if sjs2.exists():
    t = sjs2.read_text(encoding="utf-8")
    if "search-result-link" not in t:
        applied = 0
        for src, dst in CLASS_REMAP.items():
            if src in t:
                t = t.replace(src, dst)
                applied += 1
        # The remapped markup lives inside one <a>, so the tag row no longer
        # needs the padding it had when it was a separate flex row.
        if applied:
            sjs2.write_text(t, encoding="utf-8")
            bump("search_client_theme_classes", applied)

# ---------- 7) styled 404 ----------
page404 = PUB / "404.html"
html404 = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex">
<title>Page not found | Z.ai Field Guide</title>
<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
<style>
@font-face{font-family:"General Sans";src:url("/assets/fonts/GeneralSans-Variable.woff2") format("woff2");font-weight:200 700;font-style:normal;font-display:swap}
@font-face{font-family:"JetBrains Mono";src:url("/assets/fonts/JetBrainsMono-Variable.woff2") format("woff2");font-weight:100 800;font-style:normal;font-display:swap}
:root{--bg:#F4F4F2;--ink:#101113;--muted:#5B5D61;--line:#E2E3E0;--accent:#C93A18}
@media (prefers-color-scheme: dark){:root{--bg:#0E0F10;--ink:#ECECEA;--muted:#9DA0A5;--line:#26282B;--accent:#FF5C33}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"General Sans","PingFang SC","Hiragino Sans GB","Noto Sans CJK SC","Microsoft YaHei",system-ui,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:2rem}
.wrap{max-width:34rem}
.kicker{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin:0}
h1{font-size:clamp(2rem,5vw,3rem);font-weight:300;letter-spacing:-.02em;margin:.6rem 0 1rem}
p{color:var(--muted);line-height:1.7;margin:0 0 1.6rem}
.links{display:flex;flex-wrap:wrap;gap:.6rem}
a.btn{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:.8rem;text-decoration:none;color:var(--ink);border:1px solid var(--line);padding:.55rem .9rem}
a.btn:hover{border-color:var(--accent);color:var(--accent)}
</style>
</head>
<body><div class="wrap">
<p class="kicker">404</p>
<h1>That page is not here.</h1>
<p>The address may be mistyped, or the page may have moved. This guide is growing; try one of these doors instead.</p>
<div class="links">
<a class="btn" href="/">Home</a>
<a class="btn" href="/products/">Products</a>
<a class="btn" href="/models/">Models</a>
<a class="btn" href="/zh/">中文版</a>
</div>
</div></body>
</html>
"""
if (not page404.exists()) or page404.read_text(encoding="utf-8") != html404:
    page404.write_text(html404, encoding="utf-8")
    bump("page_404")

print("enhance-artifact:", ", ".join(f"{k}={v}" for k, v in sorted(changed.items())) or "nothing to do")
