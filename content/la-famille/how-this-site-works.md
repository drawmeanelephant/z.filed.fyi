---
title: "How this site works"
description: "A live tour of the la-famille features this guide exercises: taxonomies, the graph explorer, search, the RAG export, and the bilingual theme."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [la-famille, i18n, static-sites]
categories: [meta]
---

This page is the capability list, written against artifacts you can open right now. Everything below is generated from plain Markdown by la-famille; nothing is hand-maintained HTML.

## The capabilities, with live links

| Capability | Where to see it |
|------------|-----------------|
| Taxonomy archives (tags and categories, generated from frontmatter) | [/tags/](/tags/) and [/categories/](/categories/) |
| Interactive knowledge-graph explorer (search, filters, focus mode, deep links) | [/graph/](/graph/) |
| Client-side instant search (press `/` anywhere, or use the header box) | Try it on this page |
| RSS feed of dated pages | <a href="/feed.xml">/feed.xml</a> |
| Sitemap and crawler rules | <a href="/sitemap.xml">/sitemap.xml</a>, <a href="/robots.txt">/robots.txt</a> |
| Machine-readable corpus export for LLM use | <a href="/rag-archive/rag-content.md">/rag-archive/rag-content.md</a> |
| Raw Markdown passthrough (`render: false`) | [The raw sample](raw-sample.md) |

## Bilingual by composition, not framework

la-famille has no built-in internationalization. This site implements bilingual content with the generator's own primitives: two content trees (`content/` for English, `content/zh/` for Chinese) with mirrored slugs; per-page layout overrides so Chinese pages load `layout-zai-zh.html` with `lang="zh-CN"` baked into static HTML; and a small theme script that maps the current path to its counterpart language (`/models/` toggles to `/zh/models/`). No machine translation runs at build time, and no JavaScript is needed to read any page.

Two honest notes from the experiment. First, the generator's taxonomy normalizer only accepts latin script, so Chinese-language terms would be silently dropped; this site therefore uses one shared latin tag vocabulary across both editions, and the theme translates the visible "Tags" label to 标签. Both are recorded in the build log that ships with this repository. Second, because templates cannot see a page's URL, the home-page hero is expressed as a separate layout selected through frontmatter - a feature working exactly as intended, but the reason for the design is worth knowing.

## The theme

A fully custom "zai" theme: paper-and-ink light mode, a true dark mode with its own artwork, one vermilion accent, no rounded corners, and self-hosted fonts (General Sans and JetBrains Mono, licensed and included - see the [colophon](colophon.md)). Light and dark are switchable from the header and remembered across visits; the choice is applied before first paint, so there is no flash. Chinese text uses system CJK fonts to keep the page weight down.

<figure class="figure">
  <img src="/assets/img/graph-c.webp" alt="Abstract node-and-line artwork">
  <figcaption>The site ships three generated artworks; this one accompanies the graph explorer story.</figcaption>
</figure>

## The build, by the numbers

Snapshot from the build that produced the page you are reading: the full site compiles in well under a second on a laptop, from source to 50+ output files covering both languages, the graph explorer, taxonomy archives, and the corpus export. Rebuilds are incremental: unchanged pages reuse a content-addressed cache. Validation runs as part of the pipeline: a content checker for frontmatter, links, and orphans, plus a publish check that fails on non-resolvable references while reported stub pages stay visible as warnings.

## What this demonstrates

The claim this site was built to test: that a focused Go generator, extended only at the theme layer, can carry a real bilingual destination without a JavaScript framework, without external assets, and without the generator itself knowing anything about Chinese or about this theme. On the evidence of this build, the claim holds.

## Sources

- Direct inspection of this site's build output and configuration (2026-09-29)
- [la-famille repository](https://github.com/drawmeanelephant/la-famille)
