# HOMESTEAD.md — the zai site build report and bug log

Execution record for Moonshot 1 ("The Homestead Program — ship a real site")
from `docs/MOONSHOTS.md`: a real destination (a bilingual field guide to
Z.ai / Zhipu AI), built entirely with la-famille, extended only in the theme
layer. This file is the honest residue: what worked, what fought back, and the
repro for each item.

Validated on: la-famille `dev` build from this checkout (`./bin/la-famille`),
2026-09-29, macOS (arm64), Go 1.27.1. **Superseded for operational purposes by
the pinned-release acceptance pass at the bottom of this file** — the moonshot
log below stays as history; the site now builds in CI from the pinned release.

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
Workaround in this site: the `Makefile` and deploy workflow keep
`--project-root .` (run from the site directory) and pass an **absolute**
`--output` pointing at `rag-archive/` **outside** `public/`; the publish step
copies `rag-content.md` into `public/rag-archive/` and both pipelines end with
`test -s public/rag-archive/rag-content.md` plus `scripts/check-rag-coverage.py`.
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
- The build now lives in its own repository (`z.filed.fyi`), and CI builds it on
  every push to `main` with the pinned release binary. See [README](../README.md#deploy).
- Data currency: model/product facts are sourced and dated on each page
  (snapshot 2026-09-29). Known tricky items are hedged in copy (GLM-5.3
  license terms, third-party pricing drift).
- ~~One safety-guard-denied `rm` left an inert nested directory
  (`sites/zai/sites/`) created by the B1 mis-invocation; remove manually when~~
  **RESOLVED** — the stray directory did not survive the move into this repo;
  the tree is clean. B1 itself is still open upstream, so CI keeps
  `--project-root .` with an absolute `--output` and asserts the bundle is
  non-empty.

## Publishing notes

- Live: GitHub Action (`.github/workflows/deploy.yml`) builds with the pinned
  release binary and deploys `public/` to Cloudflare Pages project `z-filed`
  on every push to `main` (and manual dispatch). Custom domain
  <https://z.filed.fyi/>.
- Keep `public/`, `rag-archive/`, and `.la-famille-cache.json` out of git
  (already ignored).
- `publish-check` runs clean; re-run it after content edits.

## Pinned-release acceptance pass — 2026-10-01

Focused acceptance-cleanup pass. No redesign, no content changes, no new
generator features; the only behavioral deltas are the content-only RAG
publication (below) and the added check scripts. This is the operational
record: what the site is actually built and shipped with.

### Source revision and binary

- Generator: **`la-famille v0.1.0-prealpha`**, release source commit
  `896ec96a51f988b0108aeda4e86ae75451dc3ac8`, release built
  `2026-08-25T14:26:07Z`. Pinned in `deploy.yml` (`LA_FAMILLE_VERSION`) and
  downloaded + `SHA256SUMS`-verified in CI on every run.
- Local validation binary: `la-famille_0.1.0-prealpha_darwin_arm64.tar.gz`,
  checksum-verified against the release manifest before use
  (`grep darwin_arm64 SHA256SUMS | shasum -a 256 -c -`). A `dev` build lying
  around (`/tmp/la-famille`, `--version` reports `commit: unknown`) was
  rejected for this pass — **always confirm `--version` prints the pinned tag
  before trusting a local binary**.
- Site source: this repository at the acceptance-pass commit (content frozen
  since the 2026-09-29 verification; see [VERIFICATION.md](VERIFICATION.md)).

### Artifact

`public/` as shipped: 86 `index.html` pages (29 EN + 29 ZH content pages,
tags/categories archives, `/graph/` explorer), `search.json` (85 entries,
full-body snippets), `sitemap.xml` (86 URLs), styled `404.html`, self-hosted
`assets/` (CSS/JS/fonts/images, cache-busted `?v=<sha256[:8]>` URLs), and
`rag-archive/` containing **only `rag-content.md`** (188,868 bytes).

### Content-only RAG (new in this pass)

The pinned release's `rag` command writes three files: `rag-content.md` (the
page corpus) plus `rag-system.md` (embeds `.github/workflows/deploy.yml`,
`freshness.yml`, and `README.md`) and `rag-config.md` (a full file/asset
inventory). Shipping all three published repo internals. Accepted workaround:

- `rag --output` now lands **outside** `public/` (`rag-archive/`, gitignored).
- Only `rag-content.md` is copied into `public/rag-archive/`; the site nav's
  "RAG archive" link points at that file, and `rag-content.md` contains no
  references to the withheld files (verified), so nothing dangles.
- Until the next deploy, the live site still serves the two extra files at
  their old URLs; the first deploy built from this flow removes them.

### Coverage proof

`scripts/check-rag-coverage.py` (wired into `make publish` and CI, after
`publish-check`): parses the export's `<file path="...">` blocks and compares
each against the source tree. Result on 2026-10-01: **58/58** source files
(29 EN + 29 ZH) embedded verbatim, **0 exclusions** (`RAG_EXCLUSIONS` in the
script is empty and is the required place to record any future intentional
omission), and `public/rag-archive/rag-content.md` byte-identical to the
export. The live corpus at `/rag-archive/rag-content.md` (downloaded
2026-10-01) is byte-identical to the local export (sha256 `917813ff…`), so
the deployed artifact matches the source tree.

### Deployment checks (compatible with the pinned release)

The pinned release has no strict-mode/audit flags beyond `check`,
`publish-check`, and the build warnings; site invariants are therefore
enforced site-side by `scripts/audit-artifact.py` (14 checks, run after
`make publish`; exit non-zero on failure) plus interactive verification in a
real browser. Results 2026-10-01: **14/14 pass**, all interactive checks pass.

| Area | Check | Result |
|---|---|---|
| Assets | No external resource loads (src/link-stylesheet/CSS url()/fetch) | pass |
| Assets | Every `/assets/` URL cache-busted, `?v=` == sha256(file)[:8] (live and local agree) | pass |
| Assets | Default-theme fill pruned (no `mascot-default.jpeg`, `theme.css`, …) | pass |
| Canonical | `rel=canonical` == `https://z.filed.fyi` + page path (86 pages; spot-checked live) | pass |
| Hreflang | `en` / `zh-CN` / `x-default` on every paired page | pass |
| Bilingual nav | `a#lang-switch` on every paired page, correct `hreflang`; `zai.js` maps every path 1:1 (root prefix present; trees mirror 29/29). Round-trip tested: `/products/` ⇄ `/zh/products/`, ZH page fully localized | pass |
| Search | `search.json` covers all 58 content pages (`raw-sample` excluded by design: `render: false`, served as raw `.md`, not a page); full-body snippets; client emits theme classes (`search-result-*`), results render styled and ranked (browser-verified EN+ZH) | pass |
| Graph | `/graph/` renders with theme injection; node click selects, fills metadata sidebar (tags, links, word count), updates `?node=` deep link. Live: 58/58 nodes, 146 edges | pass |
| Missing pages | `404.html` present in artifact; live `/this/page/does-not-exist/` and `/zh/nope/` return HTTP 404 with the styled custom page | pass |
| Sitemap | Lists all 86 page URLs including `/graph/` | pass |

### Accepted workarounds (current debt, all deliberate)

- **B1** — CI and Makefile use `--project-root .` + absolute `--output` +
  non-empty guard + coverage check. Cost: none day-to-day; revisit on bump.
- **B2** — Latin-only tag vocabulary (CJK tags are dropped upstream); the
  theme documents the rule.
- **B3** — `scripts/prune-unused-assets.sh` removes the generator's unused
  default-theme fill every build; delete when upstream makes the fill
  configurable.
- **B5** — ZH taxonomy labels swapped via CSS (`html[lang="zh-CN"]`), ZH
  footer index links hardcoded (no i18n seam upstream).
- **B6** — All `--output` values passed absolute; path semantics documented in
  the Makefile header.
- **Content-only RAG** — `rag-system.md`/`rag-config.md` withheld (see above).

### Recovery procedure

Rebuild and redeploy from scratch:

1. **Get the binary.** Take `LA_FAMILLE_VERSION` / `LA_FAMILLE_REPO` from
   `deploy.yml`; download `$base/SHA256SUMS` and the `darwin_arm64` (or
   `linux_amd64`) tarball from the release, verify with
   `grep <archive> SHA256SUMS | shasum -a 256 -c -`, extract, confirm
   `./la-famille --version` prints the pinned tag + commit.
2. **Rebuild locally.** `make publish LA_FAMILLE=/path/to/la-famille`. Expect:
   `check` 0 errors / 0 warnings; build ~85 pages; `publish-check` exit 0;
   `check-rag-coverage.py` 58/58, 0 exclusions, deployed copy identical.
3. **Audit the artifact.** `python3 scripts/audit-artifact.py` → 14/14 pass.
4. **Deploy.** Push to `main` (or `gh workflow run deploy.yml`). Watch with
   `gh run list --workflow=deploy.yml` / `gh run watch`. Required secrets:
   `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN` (Pages edit rights).
5. **Verify live.** `https://z.filed.fyi/rag-archive/rag-content.md` returns
   200 and is byte-identical to `rag-archive/rag-content.md`;
   `rag-system.md`/`rag-config.md` return 404; a bogus URL returns the styled
   404; one page's `?v=` asset hash matches `shasum -a 256` of the live file.
6. **Roll back** via Cloudflare Pages deployment history (dashboard →
   z-filed → deployments → previous deployment → restore), or revert the
   commit and let CI redeploy.

### Still open (human, not agent)

- Sign-off on publication scope, rights, and upkeep (licensing placeholders
  in the README are still TBD by the repository owner).
- A non-author reader attempting one English and one Chinese task (a
  bilingual reader covers both); an agent walkthrough is not a substitute.

## Audit enforcement + stale-bundle follow-up — 2026-10-01

Small technical follow-up to the pinned-release acceptance pass (PR #6, merged
as `e0597c1`). No content, route, artwork, branding, or publishing-behavior
changes; the acceptance work is turned from "a script you should remember to
run" into "a gate that runs and refuses to pass silently".

### Source revision

- Site: this repository, branch with this follow-up (parent `e0597c1`, the
  PR #6 merge); content unchanged since the 2026-09-29 verification.
- Generator: unchanged pinned release `la-famille v0.1.0-prealpha`
  (`896ec96a51f988b0108aeda4e86ae75451dc3ac8`, built `2026-08-25T14:26:07Z`),
  re-downloaded for this pass and verified against `SHA256SUMS` before use
  (`grep darwin_arm64 SHA256SUMS | shasum -a 256 -c -` → OK; `--version`
  prints the pinned tag + commit).

### What changed

- **`scripts/audit-artifact.py` is portable.** All hardcoded local checkout
  paths are gone; `public/` and `content/` resolve relative to the script's
  repository (`__file__` → parent's parent), the same convention the other
  site scripts already use. The audit now behaves identically from the repo
  root, a subdirectory, or anywhere else.
- **The audit fails closed.** Exit 0 = all checks passed; exit 1 = one or more
  checks failed; exit 2 = a required input is missing/empty/unreadable or the
  artifact has no pages (the audit refuses to pass vacuously on a missing or
  empty artifact instead of crashing after printing PASS lines).
- **Missing-page-stub check added** (compatible with the pinned release, no
  generator flags): the release writes an "Under Construction" / "Missing
  Page" stub page — and a `stub` node in the graph payload — for every
  dangling internal link, at exit 0. Two checks now refuse to publish one:
  no stub markers in any artifact HTML, and no `stub: true`/`type: "stub"`
  nodes in `graph/data.json`.
- Small honesty fix surfaced by the refactor: the search-coverage check now
  computes the expected page count from `content/` (56 counted pages + the two
  raw samples recorded in `SEARCH_EXCLUSIONS`, 85 index entries) instead of
  printing a hardcoded "58".
- **The audit is enforced**: it is the last step of `make publish` and of the
  deploy workflow's build step — after every artifact transformation
  (strip → enhance → prune → publish-check → RAG coverage), before
  upload/deploy. The workflow's `set -euo pipefail` turns any nonzero audit
  exit into a stopped job; nothing reaches the Upload/Deploy steps.
- **`scripts/test-audit-artifact.py`** (new, stdlib-only, also run in CI):
  32 tests covering path independence (real artifact audited identically from
  `/`, the repo root, and a nested cwd; fixture site likewise; a static
  assertion that no absolute local path appears in the audit source), the
  fail-closed gate (missing/empty inputs, empty artifact), 19 representative
  check failures, and enforcement (under `set -euo pipefail`, a failing audit
  ends the pipeline before the "upload" step; a passing one lets it proceed).

### Commands and results (2026-10-01, macOS arm64, pinned release binary)

| Check | Command | Result |
|---|---|---|
| Binary provenance | download + `shasum -a 256 -c` + `--version` | OK, pinned tag + commit printed |
| Full pipeline | `make publish LA_FAMILLE=<pinned binary>` | exit 0; check 0 err/0 warn; build 86 pages; coverage 58/58, 0 exclusions; **audit 16/16 pass** |
| Audit from another cwd | `cd / && python3 …/scripts/audit-artifact.py` | identical output, 16/16 pass |
| Regression tests | `python3 scripts/test-audit-artifact.py` | 32/32 OK |
| Failed-audit proof | `set -euo pipefail` pipeline with a leak re-introduced into a copy of the real artifact (audited from `/`) | exit 1, `FAIL rag-archive contains only rag-content.md`, no "upload" step reached; same property covered by `TestEnforcement` |

### Deployment identity (as observed)

- Deploy run: `deploy.yml` run 36943181276 (push of the PR #6 merge),
  2026-10-01T23:53:28Z, Cloudflare Pages project `z-filed`, branch `main`.
- Deployment-specific URL: `https://67703d17.z-filed.pages.dev` (116 files
  uploaded); custom domain `https://z.filed.fyi/`; pages.dev alias
  `https://z-filed.pages.dev/`.

### Observed live results — withheld RAG bundles (2026-10-01, GET, headers only)

`rag-content.md` (the one bundle that should exist) is 200 with a consistent
etag on all four URL classes — the controls are healthy. The withheld bundles:

| URL | Status | Content-type | Notable headers |
|---|---|---|---|
| `z.filed.fyi/rag-archive/rag-system.md` (exact) | **200** | text/markdown | `age` ≈ 2.1 h, `cache-control: public, s-maxage=604800`, etag `1519292e…` |
| `z.filed.fyi/rag-archive/rag-config.md` (exact) | **200** | text/markdown | `age` ≈ 2.1 h, `cache-control: public, s-maxage=604800`, etag `0bb8f075…` |
| same + `?cb=<timestamp>` (cache-busted) | 404 | text/html | `cache-control: no-store` |
| `z-filed.pages.dev/rag-archive/…` (both) | 404 | text/html | `cache-control: no-store` |
| `67703d17.z-filed.pages.dev/rag-archive/…` (both) | 404 | text/html | `cache-control: no-store` |

No bundle contents were downloaded or printed; only status, content type,
sizes, and cache headers were recorded.

**Caching layer.** The origin has the files: every URL that is not the exact
original path returns 404 from the current deployment (cache-busted custom
domain, pages.dev, deployment-specific URL). The exact original custom-domain
URLs serve a cached 200: a conditional GET with the cached etag returns 304,
`age` differs between requests (multiple edge entries), and the cached
response carries `s-maxage=604800` — a 7-day shared TTL — while current origin
responses carry `max-age=0, must-revalidate`. Conclusion: stale entries in the
Cloudflare edge cache for the custom hostname `z.filed.fyi`, keyed on the
exact URL (the query-string variants miss the entry). Removal **cannot** be
claimed from the cache-busted or pages.dev 404s alone; the exact URLs are the
user-visible truth, and they still serve the old bundles until the entries
expire or are purged (up to 7 days from when they were cached).

### Completed vs pending (this follow-up)

Completed:

- Portable, fail-closed audit with the stub check; enforced in `make publish`
  and the deploy workflow before upload/deploy; proven to block publication on
  failure; regression tests pass locally (32/32) and run in CI.
- Full pipeline revalidated with the pinned release; URL matrix recorded above.

Pending (needs the owner):

- **Purge approval — two URLs only**: the stale custom-domain entries for
  `https://z.filed.fyi/rag-archive/rag-system.md` and
  `https://z.filed.fyi/rag-archive/rag-config.md`. Scope is exactly these two
  files — no zone-wide purge, no DNS, cache-rule, or secret changes. With a
  token that has purge rights, the minimal call is:
  `POST /client/v4/zones/<zone_id>/purge_cache` with
  `{"files":["https://z.filed.fyi/rag-archive/rag-system.md","https://z.filed.fyi/rag-archive/rag-config.md"]}`.
  After an approved purge (or after the entries age out), repeat the exact-URL
  checks above and expect 404 on all four URL classes.
- Publication scope/rights/upkeep sign-off, and the non-author EN/ZH reader
  test — unchanged from the acceptance pass, still not done. Homestead is
  **not** fully accepted.

## Suggested follow-ups

1. Fix B1 (small, high leverage for binary-only sites).
2. Decide B2 direction (slugify vs document) — unblocks trilingual plans.
3. Make B3 configurable; delete this repo's prune workaround when it lands.
