---
title: "Z.ai Field Guide"
description: "An independent, source-linked guide to Z.ai and Zhipu AI: chat.z.ai, the GLM Coding Plan, the GLM model line, and the company's full history."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [zhipu, glm, ecosystem]
categories: [meta]
layout: "layout-zai-home"
---

Z.ai is the international face of Zhipu AI (智谱), the Beijing lab that has been publishing GLM language models since 2022 and became the first listed large-model company in January 2026. This guide covers the whole arc: the research, the models, the products, and the record behind them.

<div class="card-grid">
  <a class="card" href="chat/">
    <span class="card-kicker">Product</span>
    <span class="card-title">Chat on Z.ai</span>
    <span class="card-body">The assistant at chat.z.ai, powered by GLM-5.3-Flash.</span>
  </a>
  <a class="card" href="code/">
    <span class="card-kicker">Product</span>
    <span class="card-title">Code on Z.ai</span>
    <span class="card-body">The GLM Coding Plan for Claude Code, OpenCode, and more.</span>
  </a>
  <a class="card" href="api/">
    <span class="card-kicker">Developer</span>
    <span class="card-title">Build on Z.ai</span>
    <span class="card-body">The OpenAI-compatible API platform and its pricing.</span>
  </a>
</div>

## What ships today

- **GLM-5.3** (August 2026) is the flagship: a post-training upgrade over GLM-5.2 that Z.ai reports as a 50 percent coding gain, with state-of-the-art results among open-weight models on benchmark suites such as Terminal Bench 3.0. It is also the release that showed unexpected cybersecurity capability, and the first flagship outside the MIT license the series used through GLM-5.2.
- **GLM-5.3-Flash** (August 2026) is the complementary release: a natively multimodal model with 320B total and 18B active parameters, MIT licensed, that powers chat.z.ai and runs at one tenth the price of the flagship.
- **chat.z.ai and the GLM Coding Plan** are the two front doors into that stack. The coding plan starts at 18 USD per month and is accepted by more than twenty agent harnesses, including Claude Code, Cline, OpenCode, and the ZCode and OpenClaw tools.

## The record

Zhipu began in June 2019 as a spin-out of Tsinghua University's Knowledge Engineering lab. It open-sourced GLM-130B in 2022, rode the ChatGLM wave in 2023, and turned open weights into a strategy with the GLM-4.5 line in 2025. The 2026 generation, the Hong Kong listing, and the A-share filing that followed are all documented in [the history section](history/).

## Explore

Beyond the three products, the guide carries the full model line ([Models](models/index.md)), the corporate record ([Company](company/index.md)), the platform map ([Ecosystem](ecosystem/index.md)), and the day-by-day history ([History](history/index.md)). This edition is also available in Chinese: [中文版](zh/index.md).

## How this guide is built

The site is generated with [la-famille](la-famille/), a static site generator written in Go, and every page lists its sources. It is an independent project: not affiliated with, endorsed by, or operated by Zhipu AI or Z.ai.

## Sources

- [z.ai](https://z.ai/) and [docs.z.ai release notes](https://docs.z.ai/release-notes/new-released)
- [GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3) and [GLM-5.3-Flash model card](https://huggingface.co/zai-org/GLM-5.3-Flash)
- [GLM Coding Plan overview](https://docs.z.ai/devpack/overview)
