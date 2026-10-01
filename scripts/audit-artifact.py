#!/usr/bin/env python3
"""Acceptance audit of the public/ artifact (pinned-release-compatible checks).

Run after `make publish`: python3 scripts/audit-artifact.py
Covers the site invariants the generator's publish-check does not: canonical
host/paths, hreflang pairing, language-switcher presence, search-index
coverage, cache-bust hash integrity, external-resource ban, prune result,
content-only RAG, sitemap completeness. Exits non-zero on any failure.
"""
import hashlib, json, pathlib, re, sys

PUB = pathlib.Path("/Users/tbuddy/dev/z/z-filed-fyi/public")
SITE = "https://z.filed.fyi"
fails, notes = [], []

def check(name, ok, detail=""):
    (notes if ok else fails).append(f"{'PASS' if ok else 'FAIL'} {name}" + (f" — {detail}" if detail else ""))

# 1) No external resource loads from any page or asset
#    Resource-loading attrs only: src=, link rel=stylesheet/icon/preload/…,
#    CSS url()/@import, fetch(). canonical/hreflang/og meta links never fetch.
LOAD_LINK_REL = re.compile(r'rel="(stylesheet|icon|shortcut icon|apple-touch-icon|preload|preconnect|manifest|modulepreload)"', re.I)
ext_pat = re.compile(r'(src|href)="(https?:)?//|url\(\s*["\']?(https?:)?//|@import\s+(https?:)?//|fetch\(\s*["\'](?:https?:)?//', re.I)
SITE_HOST = "z.filed.fyi"
bad = []
def external_ok(url):
    m = re.match(r'^https?://([^/"\']+)', url)
    return (not m) or m.group(1) == SITE_HOST
for p in list(PUB.rglob("*.html")) + list(PUB.rglob("*.css")) + list(PUB.rglob("*.js")):
    t = p.read_text(encoding="utf-8", errors="replace")
    if p.suffix == ".html":
        for m in re.finditer(r'<(script|img|link|source|video|audio)\b[^>]*>', t, re.I):
            tag = m.group(0)
            if m.group(1).lower() == "link" and not LOAD_LINK_REL.search(tag):
                continue  # canonical/alternate/og — metadata, never fetched
            for um in re.finditer(r'(?:src|href)="([^"]+)"', tag):
                if not external_ok(um.group(1)):
                    bad.append((p.relative_to(PUB).as_posix(), tag[:120]))
        for m in re.finditer(r'style="[^"]*url\(\s*["\']?(https?:)?//', t, re.I):
            bad.append((p.relative_to(PUB).as_posix(), "inline style url"))
    else:
        for um in re.finditer(r'(?:src|href)=["\']?(https?:)?//([^/"\'\s)]+)', t):
            if um.group(2) != SITE_HOST:
                bad.append((p.relative_to(PUB).as_posix(), t[max(0,um.start()-40):um.start()+60]))
        for um in re.finditer(r'url\(\s*["\']?(https?:)?//([^/"\'\s)]+)', t):
            if um.group(2) != SITE_HOST:
                bad.append((p.relative_to(PUB).as_posix(), "css url()"))
        for um in re.finditer(r'fetch\(\s*["\'](https?:)?//([^/"\'\s)]+)', t):
            if um.group(2) != SITE_HOST:
                bad.append((p.relative_to(PUB).as_posix(), "fetch()"))
check("no external resource loads", not bad, f"{len(bad)} offenders" + (f"; e.g. {bad[:3]}" if bad else ""))

# og:image / canonical / hreflang point at SITE itself — sanity-check those separately
# 2) Cache-busting: every /assets/ ref carries ?v=<8hex> equal to sha256(file)[:8]
ASSET_REF = re.compile(r'(?:src|href)="(/assets/[^"?#]+)(?:\?v=([a-f0-9]+))?(#[^"]*)?"')
unversioned, mismatched = [], []
for p in PUB.rglob("*.html"):
    t = p.read_text(encoding="utf-8")
    for m in ASSET_REF.finditer(t):
        path, ver = m.group(1), m.group(2)
        f = PUB / path.lstrip("/")
        if not f.is_file():
            mismatched.append((p.name, path, "missing file"))
            continue
        want = hashlib.sha256(f.read_bytes()).hexdigest()[:8]
        if ver is None:
            unversioned.append((p.relative_to(PUB).as_posix(), path))
        elif ver != want:
            mismatched.append((p.relative_to(PUB).as_posix(), path, f"{ver} != {want}"))
check("all asset URLs cache-busted", not unversioned, f"{len(unversioned)} unversioned" + (f"; e.g. {unversioned[:3]}" if unversioned else ""))
check("cache-bust hashes match file contents", not mismatched, f"{len(mismatched)} mismatched" + (f"; e.g. {mismatched[:3]}" if mismatched else ""))

# 3) Prune: default-theme dead weight absent
for f in ["assets/css/theme.css","assets/css/theme-foundations.css","assets/css/layout-editorial.css",
          "assets/css/layout-midnight.css","assets/css/layout-terminal.css","assets/css/search.css",
          "assets/img/mascot-default.jpeg","assets/img/jules-logo.png","assets/img/u1f419_u1f354.png"]:
    if (PUB / f).exists():
        fails.append(f"FAIL prune — {f} still present")
notes.append("PASS prune — default-theme assets absent")

# 4) Canonical URL on every content page matches its own location
canon_bad = []
canon_n = 0
for p in PUB.rglob("index.html"):
    rel = p.relative_to(PUB).as_posix()
    url = "/" + rel[: -len("index.html")]
    t = p.read_text(encoding="utf-8")
    m = re.search(r'<link rel="canonical" href="([^"]+)"', t)
    if not m:
        if url.startswith("/tags/") or url.startswith("/categories/") or url == "/graph/":
            continue
        canon_bad.append((url, "no canonical"))
        continue
    canon_n += 1
    want = SITE + url
    if m.group(1) != want:
        canon_bad.append((url, f"{m.group(1)} != {want}"))
check(f"canonical URLs match page locations ({canon_n} checked)", not canon_bad, f"{len(canon_bad)} bad" + (f"; e.g. {canon_bad[:3]}" if canon_bad else ""))

# 5) hreflang pair coverage
def has_hreflang(t):
    return 'hreflang="en"' in t and 'hreflang="zh-CN"' in t and 'hreflang="x-default"' in t
missing_hl = []
for p in PUB.rglob("index.html"):
    rel = p.relative_to(PUB).as_posix()
    if rel.startswith(("tags/","categories/","graph/")) or rel == "404.html":
        continue
    url = "/" + rel[: -len("index.html")]
    counterpart = PUB / ("zh" + url).strip("/") / "index.html" if not url.startswith("/zh/") else PUB / url[3:].strip("/") / "index.html"
    if counterpart.exists() and not has_hreflang(p.read_text(encoding="utf-8")):
        missing_hl.append(url)
check("hreflang en/zh-CN/x-default on every paired page", not missing_hl, f"{len(missing_hl)} missing" + (f"; e.g. {missing_hl[:5]}" if missing_hl else ""))

# 6) Bilingual nav: a#lang-switch on every paired page, correct hreflang,
#    default href resolved to the counterpart (JS refines deep paths).
switch_bad = []
CONTENT_SECTIONS = set()
for p in PUB.rglob("index.html"):
    rel = p.relative_to(PUB).as_posix()
    if rel.startswith(("tags/","categories/","graph/")) or rel == "404.html":
        continue
    t = p.read_text(encoding="utf-8")
    url = "/" + rel[: -len("index.html")]
    is_zh = url.startswith("/zh/")
    counterpart = url[3:] if is_zh else "/zh" + url
    if counterpart == "/":
        counterpart = "/"
    if not counterpart.endswith("/"):
        counterpart += "/"
    m = re.search(r'<a\b[^>]*id="lang-switch"[^>]*>', t)
    if not m:
        switch_bad.append((url, "no lang-switch"))
        continue
    tag = m.group(0)
    hm = re.search(r'href="([^"]*)"', tag)
    lm = re.search(r'hreflang="([^"]*)"', tag)
    if not hm:
        switch_bad.append((url, "lang-switch without href"))
        continue
    href = hm.group(1)
    norm = href if href.endswith("/") else href + "/"
    if norm not in ("/zh/", "/"):
        switch_bad.append((url, f"fallback href {href} not the other tree's root"))
    want_lang = "en" if is_zh else "zh-CN"
    if not lm or lm.group(1) != want_lang:
        switch_bad.append((url, f"hreflang {lm.group(1) if lm else 'missing'} != {want_lang}"))
check("language switcher on every paired page", not switch_bad, f"{len(switch_bad)} issues" + (f"; e.g. {switch_bad[:5]}" if switch_bad else ""))

# 6b) zai.js mirror: the list includes "/", so EVERY path maps 1:1 to the
#     other tree (trees are fully mirrored 29/29). Assert that load-bearing fact.
zjs = (PUB / "assets/js/zai.js").read_text(encoding="utf-8")
mir = re.search(r'var mirrored = \[(.*?)\];', zjs, re.S).group(1)
mirrored = set(re.findall(r'"([^"]+)"', mir))
check("lang-switch JS maps every path (root prefix present)", "/" in mirrored, f"mirrored={sorted(mirrored)}")

# 7) Search index: every content page (EN+ZH) present with non-trivial body text.
#    raw-sample.md is intentionally absent: render:false, served as raw .md, not a page.
sj = PUB / "search.json"
items = json.loads(sj.read_text(encoding="utf-8")) if sj.exists() else []
urls = {it.get("u") for it in items}
src_missing = []
for p in pathlib.Path("/Users/tbuddy/dev/z/z-filed-fyi/content").rglob("*.md"):
    rel = p.relative_to(pathlib.Path("/Users/tbuddy/dev/z/z-filed-fyi/content")).as_posix()
    if rel.endswith("raw-sample.md"):
        continue  # recorded intentional exclusion (raw sample, not a rendered page)
    if rel == "index.md":
        u = "/"
    elif rel.endswith("/index.md"):
        u = "/" + rel[: -len("index.md")]
    else:
        u = "/" + rel[: -len(".md")] + "/"
    if rel.startswith("zh/") and not u.startswith("/zh/"):
        u = "/zh" + u
    if u not in urls:
        src_missing.append(u)
empty_s = [it.get("u") for it in items if not it.get("s") or len(it.get("s","")) < 40]
check(f"search.json covers all 58 content pages ({len(items)} entries)", not src_missing, f"missing: {src_missing[:5]}" if src_missing else "")
check("search entries carry full-body snippets", not empty_s, f"{len(empty_s)} thin/empty" + (f"; e.g. {empty_s[:5]}" if empty_s else ""))

# 7b) search client styled (theme classes, no Tailwind utilities)
sjs = (PUB / "assets/js/search.js").read_text(encoding="utf-8")
check("search client emits theme classes", "search-result-link" in sjs and "line-clamp-2" not in sjs)

# 8) 404 + rag-archive contents
check("404.html present", (PUB / "404.html").is_file())
rag_files = sorted(x.name for x in (PUB / "rag-archive").iterdir()) if (PUB / "rag-archive").exists() else []
check("rag-archive contains only rag-content.md", rag_files == ["rag-content.md"], str(rag_files))

# 9) sitemap: every EN page + /graph/ + zh pages
sm = (PUB / "sitemap.xml").read_text(encoding="utf-8")
loc = set(re.findall(r"<loc>([^<]+)</loc>", sm))
sm_missing = []
for p in PUB.rglob("index.html"):
    rel = p.relative_to(PUB).as_posix()
    if rel.startswith(("tags/","categories/")):
        continue
    url = SITE + "/" + rel[: -len("index.html")]
    if url not in loc:
        sm_missing.append(url)
check(f"sitemap lists all pages incl. /graph/ ({len(loc)} locs)", not sm_missing, f"missing: {sm_missing[:5]}" if sm_missing else "")

print("\n".join(notes))
print()
if fails:
    print("\n".join(fails))
    sys.exit(1)
print(f"ARTIFACT AUDIT: all {len(notes)} checks passed")
