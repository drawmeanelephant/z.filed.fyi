---
title: "The GLM-4.5 to 4.7 run"
description: "How the July 2025 to January 2026 releases turned open weights into Zhipu's strategy, model by model."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [glm, glm-4, open-source, history]
categories: [models]
---

Between July 2025 and January 2026 Zhipu shipped a model roughly every other month, and the pattern it established - frontier-adjacent quality, open weights, aggressive pricing - set up everything that followed.

## GLM-4.5 and GLM-4.5-Air (July 28, 2025)

The pivot release. GLM-4.5 was branded as an "ARC" foundation model (agentic, reasoning, coding) with doubled parameter efficiency over its predecessor, and it shipped with one-click compatibility for the Claude Code framework - an interoperability bet that paid off when coding-agent adoption exploded. The same week, Zhipu rebranded its international platform as Z.ai. The lineage: 355B total parameters with 32B active for the flagship, with GLM-4.5-Air as the compact sibling.

## GLM-4.5V (August 11, 2025)

A 100B-scale open-source vision reasoning model covering video understanding, visual grounding, and GUI agents, with a new thinking mode. This is the line that matures into the multimodal Flash model a year later.

## GLM-4.6 (September 30, 2025)

The 2025 coding flagship, described by Z.ai as "the leading coding model in China" at release. Independent summaries note a 355B parameter scale and MIT licensing, and it became the default engine across Z.ai's surfaces for the rest of the year.

## GLM-4.6V (December 8, 2025)

A vision refresh with a 128K context window and state-of-the-art claims on image-text tasks.

## GLM-4.7 and GLM-4.7-Flash (December 22, 2025, and January 19, 2026)

The year closed with GLM-4.7: open-source state-of-the-art on major coding and reasoning benchmarks according to Zhipu, with stronger long-context understanding and agentic coding. The model card records 73.8 on SWE-bench Verified. Its Flash companion arrived in January as a free-tier model; a paid FlashX tier followed as a low-cost option.

## What the run proved

Three things became visible across these releases: that open weights could be a distribution strategy rather than a giveaway, that Claude Code compatibility was a doorway to millions of developers, and that the price-performance gap to closed frontier models was closing. The [coding plan](../code/index.md) business and the [GLM-5 generation](glm-5-family.md) are direct products of this six-month run.

## Sources

- [Release notes](https://docs.z.ai/release-notes/new-released) (official dates and descriptions)
- Model cards: [GLM-4.7](https://huggingface.co/zai-org/GLM-4.7), [GLM-4.5](https://github.com/zai-org/GLM-4.5)
- [Wikipedia: Z.ai](https://en.wikipedia.org/wiki/Z.ai) (rebrand date)
- PR wire coverage of GLM-4.7 and GLM-4.5 launches (Dec 2025; Jul 2025)
