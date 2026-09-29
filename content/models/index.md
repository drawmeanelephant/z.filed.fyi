---
title: "The GLM model line"
description: "Every major GLM release from GLM-130B in 2022 to GLM-5.3-Flash in 2026, with the flagships compared."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [glm, models, open-source]
categories: [models]
---

GLM stands for General Language Model, and the line runs from an academic open-source experiment in 2022 to models that anchor a listed company's product portfolio in 2026. This page is the index; each generation gets its own entry below.

## The current flagships

| Model | Released | Params | Context | License | Price (in/out per 1M) |
|-------|----------|--------|---------|---------|----------------------|
| [GLM-5.3](glm-5-3.md) | Aug 2026 | 5.2 base | 1M | custom (not MIT) | $1.40 / $4.40 |
| [GLM-5.3-Flash](glm-5-3-flash.md) | Aug 2026 | 320B total / 18B active | 1M | MIT | $0.15 / $0.50 |
| [GLM-5.2](glm-5-family.md) | Jun 2026 | ~743B MoE | 1M | MIT | $1.40 / $4.40 |
| [GLM-5.1](glm-5-family.md) | Apr 2026 | 5 base | long-horizon | MIT | $1.40 / $4.40 |
| [GLM-5](glm-5-family.md) | Feb 2026 | 744B / 40B active | 1M class | MIT | $1.00 / $3.20 |

## Full chronology

<ul class="z-timeline">
  <li><span class="t-date">Aug 2022</span><span class="t-body"><strong>GLM-130B</strong> - open bilingual pretrained model; ICLR 2023</span></li>
  <li><span class="t-date">Mar 2023</span><span class="t-body"><strong>ChatGLM-6B</strong> - single-GPU open chat model; millions of downloads</span></li>
  <li><span class="t-date">Jun 2023</span><span class="t-body"><strong>ChatGLM2-6B</strong> - second generation</span></li>
  <li><span class="t-date">Oct 2023</span><span class="t-body"><strong>ChatGLM3</strong> - third generation series</span></li>
  <li><span class="t-date">Jan 2024</span><span class="t-body"><strong>GLM-4</strong> - new base; the DevDay that anchored the 2024 lineup</span></li>
  <li><span class="t-date">Jun-Sep 2024</span><span class="t-body"><strong>GLM-4-9B, GLM-4V-9B, GLM-4-Plus</strong> - open small models plus stronger hosted tiers</span></li>
  <li><span class="t-date">Jul 2025</span><span class="t-body"><strong>GLM-4.5 + Air</strong> - "ARC" foundation models; the open-weights turn</span></li>
  <li><span class="t-date">Aug 2025</span><span class="t-body"><strong>GLM-4.5V, Slide/Poster Agent</strong> - vision and agentic surfaces</span></li>
  <li><span class="t-date">Sep 2025</span><span class="t-body"><strong>GLM-4.6</strong> - coding-focused flagship of 2025</span></li>
  <li><span class="t-date">Dec 2025</span><span class="t-body"><strong>GLM-4.6V, GLM-4.7, GLM-4.7-Flash</strong> - vision refresh; year-end open-source flagship</span></li>
  <li><span class="t-date">Jan 2026</span><span class="t-body"><strong>GLM-Image, GLM-4.7-Flash</strong> - image generation on domestic chips</span></li>
  <li><span class="t-date">Feb 2026</span><span class="t-body"><strong>GLM-5, GLM-OCR</strong> - the engineering generation</span></li>
  <li><span class="t-date">Apr 2026</span><span class="t-body"><strong>GLM-5.1</strong> - eight-hour autonomous runs</span></li>
  <li><span class="t-date">Jun 2026</span><span class="t-body"><strong>GLM-5.2</strong> - 1M lossless context; MIT "pure open"</span></li>
  <li><span class="t-date">Aug 2026</span><span class="t-body"><strong>GLM-5.3, GLM-5.3-Flash</strong> - coding leap plus native multimodal Flash</span></li>
</ul>

Two patterns are worth noticing. First, the cadence: roughly one meaningful flagship every three months since early 2025. Second, the license arc: MIT through GLM-5.2, then a custom license on GLM-5.3 while its Flash sibling stayed MIT. The [open source page](../company/open-source.md) covers what that means for users.

Pages in this section: [GLM-5.3](glm-5-3.md), [GLM-5.3-Flash](glm-5-3-flash.md), [the GLM-5 generation](glm-5-family.md), [the GLM-4.5 to 4.7 run](glm-4-x-era.md), [GLM-130B to GLM-4](earlier.md).

## Sources

- [docs.z.ai release notes](https://docs.z.ai/release-notes/new-released) (official chronology)
- [Z.ai pricing](https://docs.z.ai/guides/overview/pricing)
- Hugging Face model cards: [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3), [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash), [GLM-5.2](https://huggingface.co/zai-org/GLM-5.2), [GLM-5](https://huggingface.co/zai-org/GLM-5), [GLM-4.7](https://huggingface.co/zai-org/GLM-4.7)
- GitHub: [zai-org/GLM-130B](https://github.com/zai-org/GLM-130B), [zai-org/ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B)
