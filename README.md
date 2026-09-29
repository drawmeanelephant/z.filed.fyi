# Z.ai Field Guide

A bilingual (English + Chinese) static site about Z.ai and Zhipu AI: the company's
history, chat.z.ai, code.z.ai, and the GLM model line. Generated with
[la-famille](../../README.md), a static site generator written in Go.

## Build

With the la-famille binary available (set LA_FAMILLE to its path if needed):

```sh
la-famille --project-root . build                    # -> ./public/
la-famille --project-root . check                    # content validation
la-famille --project-root . rag --output "$PWD/public/rag-archive"
```

Or with make: `make build`, `make check`, `make rag`, `make publish`.

`public/` is the complete publish artifact. The site ships no external assets:
fonts and images are self-hosted.

## Structure

- `content/` English edition (site root). `content/zh/` Chinese edition (`/zh/`).
- `templates/` the custom "zai" theme (layouts + partials). EN pages use
  `layout-zai.html` by default; ZH pages set `layout: "layout-zai-zh"`.
- `assets/` theme CSS/JS, self-hosted fonts, images.

## Notes

- This is an independent project. Not affiliated with Zhipu AI or Z.ai.
- Licensing placeholders: TBD by the repository owner.
