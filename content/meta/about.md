---
title: "About this guide"
description: "What this site is, who made it, how sources are handled, and four myths corrected with references."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [zhipu, la-famille]
categories: [meta]
---

This is an independent field guide to Z.ai and Zhipu AI: the company, the models, the products, and the public record. It is not affiliated with, endorsed by, or operated by Zhipu AI or Z.ai, and it sells nothing.

## The method

- **Sources on every page.** Each page ends with the specific sources used for its claims: official documentation and model cards first, then reputable press, then community reports, always labeled.
- **Dated facts.** Where something is a snapshot (prices, star counts, market caps), the page says so and gives the check date.
- **Hedged where the record hedges.** Claims that rest on a single source or on press reporting rather than primary documents are written as "reported" or attributed inline.
- **Corrections welcome.** This is a static site with a version history; the [colophon](../la-famille/colophon.md) explains how the corpus is published and where the raw text lives.

## Four myths, corrected

1. **"ChatGLM was just a ChatGPT clone."** The lineage traces to GLM pretraining research from 2021 and GLM-130B in August 2022, with a published ICLR paper. The details are in [the model pages](../models/earlier.md).
2. **"Z.ai is a different company."** Z.ai is Zhipu's international brand, adopted in July 2025 with the GLM-4.5 launch.
3. **"Everything from Zhipu is MIT licensed."** MIT covered the line through GLM-5.2, and covers GLM-5.3-Flash today; the GLM-5.3 flagship carries a custom license. See [open source](../company/open-source.md).
4. **"Open weights and open source are the same thing."** They are not, and the difference became practically relevant in August 2026. Being precise about it is part of this guide's job.

## Why it exists

The site doubles as a working demonstration of [la-famille](../la-famille/index.md), a static site generator written in Go: bilingual content trees, taxonomy archives, a knowledge-graph explorer, and a machine-readable corpus export, all generated from plain Markdown. If you came for the tooling story rather than the Z.ai story, start at [How this site works](../la-famille/how-this-site-works.md).

## Sources

- All claims on this page are sourced on the pages they link to.
