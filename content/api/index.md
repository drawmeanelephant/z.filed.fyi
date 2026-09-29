---
title: "Build on Z.ai"
description: "The Z.ai developer platform: OpenAI-compatible API, SDKs, the full GLM model menu, and official per-token pricing."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [api, glm, coding]
categories: [products]
---

docs.z.ai is the developer door into Z.ai. Behind it sits the same model family that powers chat and code, exposed as an OpenAI-compatible API with published per-token pricing.

## The interface

Requests go through standard chat-completion semantics, so the migration path is short: point an OpenAI SDK at the Z.ai endpoint and keep your code. Z.ai also ships official Python and Java SDKs, plus documented LangChain integration and an OpenAPI specification for everything else. The docs describe streaming, tool streaming, function calling, structured output, and context caching as first-class features, alongside capability toggles that matter for reproducibility: explicit reasoning effort levels on the newest models and a web-search tool priced per use.

## The model menu

Prices below are the official rates from Z.ai's pricing page, per million tokens in USD (input / cached input / output), as of September 29, 2026:

| Model | Input | Cached | Output | Notes |
|-------|-------|--------|--------|-------|
| GLM-5.3 | $1.40 | $0.26 | $4.40 | Flagship, text-only |
| GLM-5.3-Flash | $0.15 | $0.03 | $0.50 | Multimodal workhorse |
| GLM-5.3-FlashX | $0.37 | $0.075 | $1.25 | 200 tokens/s tier |
| GLM-5.2 / GLM-5.1 | $1.40 | $0.26 | $4.40 | Previous flagships |
| GLM-5 | $1.00 | $0.20 | $3.20 | February 2026 generation |
| GLM-4.7 / GLM-4.6 / GLM-4.5 | $0.60 | $0.11 | $2.20 | The 2025 open-weights line |
| GLM-4.5-Air | $0.20 | $0.03 | $1.10 | Light text |
| GLM-4.6V | $0.30 | $0.05 | $0.90 | Vision |
| GLM-OCR | $0.03 | - | $0.03 | Layout parsing |
| GLM-4.7-Flash / GLM-4.5-Flash / GLM-4.6V-Flash | Free | Free | Free | Free tiers |

Beyond text: GLM-Image generates images at $0.015 each, CogVideoX-3 videos cost $0.20, and GLM-ASR-2512 transcribes audio at roughly $0.0024 per minute.

## Beyond raw completions

The platform also exposes task-shaped agents rather than model endpoints. The Slide and Poster agent (beta, $0.70 per million tokens) turns research into designed slides; a translation service handles glossary-aware multilingual work; video-effect templates render short clips; and a web-reader endpoint fetches and structures pages for retrieval-style workflows. The tokenizer and rate-limit endpoints round out the toolbox.

## Who it is for

If you are wiring models into a product, this is the metered path: different keys and different quotas from the [coding plan](../code/index.md), priced for production rather than per-seat. If you mostly want to try the models, [chat.z.ai](../chat/index.md) is free and instant.

## Sources

- [Z.ai pricing](https://docs.z.ai/guides/overview/pricing) and [documentation index](https://docs.z.ai/llms.txt) (fetched 2026-09-29)
- [Chat completion API reference](https://docs.z.ai/api-reference/llm/chat-completion)
- [Slide/Poster agent docs](https://docs.z.ai/guides/agents/slide)
