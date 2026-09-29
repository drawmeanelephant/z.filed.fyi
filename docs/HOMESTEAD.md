# HOMESTEAD.md — the zai site build report and bug log

Execution record for Moonshot 1 ("The Homestead Program — ship a real site")
from `docs/MOONSHOTS.md`: a real destination (a bilingual field guide to
Z.ai / Zhipu AI), built entirely with la-famille, extended only in the theme
layer. This file is the honest residue: what worked, what fought back, and the
repro for each item.

Validated on: la-famille `dev` build from this checkout (`./bin/la-famille`),
2026-09-29, macOS (arm64), Go 1.27.1.

## Build summary

| Check | Command | Result |
|-------|---------|--------|
| Build | `./bin/la-famille --project-root sites/zai build` | 73 content pages + graph explorer, 32-46 ms, cache=miss, 0 warnings |
| Content check | `./bin/la-famille --project-root sites/zai check` | 0 errors, 0 warnings, 0 orphans |
| Publish check | `./bin/la-famille --project-root sites/zai publish-check` | exit 0, full manifest (74 `index.html`) |
| RAG export | `cd sites/zai && ../../bin/la-famille --project-root . rag --output "$PWD/public/rag-archive"` | `rag-content.md` 138,633 bytes |
| Artifact audit | grep for `src=http`, `url(http`, `fetch(`, `@import`, protocol-relative | no external fetches from any page or asset |

## Findings (bugs, limitations, rough edges)

Severity: S1 blocks use, S2 forces workarounds, S3 friction/DX.
Status: as of 2026-09-29.

### B1 (S2) `rag` bundles are empty when `--project-root` is a relative subdirectory — ON FILE
Files: `internal/ragexport/export.go` (candidate area; not root-caused).

Repro (observed):
```
cd <repo root>
./bin/la-famille --project-root sites/zai rag --output "$PWD/sites/zai/public/rag-archive"
# logs "Created rag-content.md" but:
wc -c sites/zai/public/rag-archive/*   # rag-content.md 0, rag-system.md 0, rag-config.md 107
```
Counterfactual (same inputs, different CWD):
```
cd sites/zai
../../bin/la-famille --project-root . rag --output "$PWD/public/rag-archive"
wc -c public/rag-archive/*             # 138,633 / 1,240 / 1,504
```
Impact: the README's documented invocation silently produces an empty archive
for any site whose project root is not the current directory. Only "Created ..."
log lines; no warning. A deploy could ship an empty RAG bundle unnoticed.
Workaround in this site: the `Makefile` `rag` target runs from the site
directory and passes an absolute `OUTPUT`.
Related observation: a `--output` value that is itself project-root-relative
(e.g. `--output sites/zai/public/rag-archive`) nests the result under the
project root; absolute `--output` behaves.

### B2 (S2) Non-latin (CJK) taxonomy terms are dropped — ON FILE
Files: taxonomy normalization (warn emitted during build and check).

Repro:
```yaml
# content/zh/page.md
tags: [起始]
```
Observed: `level=WARN msg="Dropped unusable tag" original=起始 ... "normalizes to
an empty value, which cannot be published as a path"`; the term never reaches
`/tags/`.
Impact: native-language taxonomies are impossible for CJK content; bilingual
sites must adopt a latin tag vocabulary (which this site does, and documents in
the theme).
Suggestion: slugify/transliterate, or fail loudly with a documented rule.

### B3 (S2) Runtime asset fill copies unused default-theme assets into every build — ON FILE
Observed in `public/assets/` after a clean build of a site that ships its own
complete theme and references none of these:
`css/theme.css`, `css/theme-foundations.css`, `css/layout-editorial.css`,
`css/layout-midnight.css`, `css/layout-terminal.css`,
`img/mascot-default.jpeg` (1.4 MB), `img/jules-logo.png`,
`img/u1f419_u1f354.png`.
Impact: every project's publish artifact carries ~1.5 MB of dead weight;
"clean artifact" requires a project-side prune step (this site ships
`scripts/prune-unused-assets.sh`).
Suggestion: fill only what the configured layout/features reference, or make
the fill set configurable.

### B4 (S3, by design) Templates cannot see the page URL or "is home"
Consequence: the home-page hero is expressed as extra layouts
(`layout-zai-home*.html`) selected via frontmatter — a working per-page layout
feature, but worth documenting as the intended mechanism for URL-conditioned
renderings.

### B5 (S3) Taxonomy strings are English-only
`taxonomy.NavLinks` appends "Tags"/"Categories" labels and `PageTagLinks`
appends a "Tags:" prefix with no localization hook. Workaround used: the theme
renders its own localized nav and swaps the visible label for zh via CSS
(`html[lang="zh-CN"] .page-tags strong`). A future i18n seam (per-page
language or label override) would remove the need.

### B6 (S3) `--output` path semantics surprise
Applies to `rag` and `publish-check`: values are resolved against the project
root, while the rest of the CLI (and intuition) suggests CWD. Passing the same
root-relative path the README shows, from a parent directory, duplicates
prefixes (`sites/zai/sites/zai/...`). Documented correct forms are in the
site Makefile; a CLI note or normalization would help.

### B7 (S3) Prune-audit nuance
The reference check for "unused assets" counts any textual match, so a file
referenced only inside another soon-to-be-removed file survives
(`theme-foundations.css` is mentioned in `layout-editorial.css`'s comment).
Minor; listed so the prune script's next iteration knows.

## Deviations & assumptions (explicit)

- Bilingual without an i18n engine: two content trees, mirrored slugs,
  per-language layouts, theme-level switcher. Latin-only shared taxonomy
  (B2). ZH footer carries hardcoded localized index links because
  `.Site.SiteLinks` labels are global.
- The build lives at `sites/zai/` inside the la-famille checkout (platform
  workspace binding); the user-designated GitHub repo `z.filed.fyi` is the
  publication target — migration is prepared but not executed from here.
- Data currency: model/product facts are sourced and dated on each page
  (snapshot 2026-09-29). Known tricky items are hedged in copy (GLM-5.3
  license terms, third-party pricing drift).
- One safety-guard-denied `rm` left an inert nested directory
  (`sites/zai/sites/`) created by the B1 mis-invocation; remove manually when
  convenient.

## Publishing notes

- Launch option A: GitHub Action (build with the la-famille release binary,
  upload `public/`), then any static host or Pages.
- Launch option B: Cloudflare Pages, build command pointing at the binary with
  `--project-root .`.
- Keep `public/` and `.la-famille-cache.json` out of git (already ignored).
- `publish-check` runs clean; re-run it after content edits.

## Suggested follow-ups

1. Fix B1 (small, high leverage for binary-only sites).
2. Decide B2 direction (slugify vs document) — unblocks trilingual plans.
3. Make B3 configurable; delete this repo's prune workaround when it lands.
