# Z.ai Field Guide

A bilingual (English + Chinese) static site about Z.ai and Zhipu AI: the company's
history, chat.z.ai, the GLM Coding Plan, and the GLM model line. Generated with
[la-famille](../../README.md), a static site generator written in Go.

## Build

With the la-famille binary available (set LA_FAMILLE to its path if needed):

```sh
la-famille --project-root . build                    # -> ./public/
la-famille --project-root . check                    # content validation
la-famille --project-root . rag --output "$PWD/public/rag-archive"
```

Or with make: `make build`, `make check`, `make rag`, `make publish`.

`make publish` runs two post-processing passes over the artifact: `scripts/strip-internal-nofollow.py` (internal links lose the sanitizer's `rel="nofollow"`; external links keep it) and `scripts/enhance-artifact.py` (hreflang alternates, graph theme injection, full-body search index, taxonomy cleanup, sitemap entry).

`public/` is the complete publish artifact. The site ships no external assets:
fonts and images are self-hosted.

## Structure

- `content/` English edition (site root). `content/zh/` Chinese edition (`/zh/`).
- `templates/` the custom "zai" theme (layouts + partials). EN pages use
  `layout-zai.html` by default; ZH pages set `layout: "layout-zai-zh"`.
- `assets/` theme CSS/JS, self-hosted fonts, images.

## Deploy

`.github/workflows/deploy.yml` builds the site and publishes it to Cloudflare
Pages on every push to `main` (and on manual dispatch).

- Generator: pinned release `v0.1.0-prealpha` of
  [drawmeanelephant/la-famille](https://github.com/drawmeanelephant/la-famille),
  downloaded and verified against the release `SHA256SUMS`.
- Pages project: `z-filed` → <https://z-filed.pages.dev/> (custom domain
  <https://z.filed.fyi/>).
- Required repository secrets: `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN`
  (set via `gh secret set`). The token needs Cloudflare Pages edit rights on the
  account. Values are never read by a local build.
- Each run runs `check` → `build` → `rag` → prune → `publish-check` and fails if
  `rag-content.md` comes out empty. That guard exists because a relative
  `--project-root` silently yields an empty RAG bundle (see B1 in
  [docs/HOMESTEAD.md](docs/HOMESTEAD.md)); the workflow keeps the project root
  at `.` and passes an absolute `--output`.
- Watch runs with `gh run list` / `gh run watch`.

## Notes

- This is an independent project. Not affiliated with Zhipu AI or Z.ai.
- Licensing placeholders: TBD by the repository owner.
