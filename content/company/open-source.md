---
title: "Open source"
description: "What Zhipu actually publishes: the repository inventory, the MIT-to-custom license arc, and the community artifacts that outlast any launch."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [open-source, glm, coding]
categories: [company]
---

Open source is not a side project at Zhipu; it is the distribution strategy. This page inventories what is actually on the shelf and how the licensing has evolved.

## The inventory

Star counts from GitHub, checked September 29, 2026. The organization is `zai-org` (formerly THUDM for the research repositories):

| Repository | What it is | Stars |
|------------|------------|-------|
| ChatGLM-6B | The 2023 single-GPU chat model that started the wave | 40.9k |
| Open-AutoGLM | Open phone-agent model and framework | 26.3k |
| ChatGLM2/3 | Subsequent open chat generations | 15.5k / 13.6k |
| CogVideo | Text-to-video, including CogVideoX | 13.0k |
| CodeGeeX (1 and 2) | Multilingual code generation | 8.8k / 7.5k |
| GLM-130B | The 2022 open bilingual pretrained model | 7.6k |
| GLM-OCR | Compact OCR model (2026) | 7.5k |
| GLM-5 | Flagship release repository | 7.2k |
| ZCode | Z.ai's coding agent harness | 7.1k |
| GLM-4 / GLM-4.5 | Series repositories | 7.1k / 4.4k |
| GLM-4-Voice | End-to-end speech | 3.2k |
| GLM-TTS, GLM-ASR, GLM-Image | Speech and image models (2025-2026) | 1.1k / 0.9k / 1.1k |

The research side (THUDM) adds the RL post-training framework slime (8.6k), AgentBench (3.8k), LongBench, LongWriter, and the P-tuning line.

The table is a curated shelf, not a complete census. Ten further repos sit above 1.1k stars and are left out here — most notably CogVLM (6.7k) and VisualGLM-6B (4.2k) from the 2023 vision line, plus CodeGeeX4 (2.6k), CogVLM2 (2.4k), GLM-V (2.4k), CogView (1.8k), ImageReward (1.7k), SCAIL-2 (1.2k), CogAgent (1.2k), and CogView4 (1.1k).

## The license arc

- **2022-2025: MIT where it mattered.** GLM-130B through GLM-5.2 shipped under permissive licenses; the GLM-5.2 card's own words are "Pure Open: no regional limits, technical access without borders."
- **August 2026: the turn.** [GLM-5.3](../models/glm-5-3.md) appeared under a custom "glm-5.3" license; community reporting said large-revenue providers need a security review, a detail worth verifying against the license text before enterprise deployment.
- **The exception that matters.** [GLM-5.3-Flash](../models/glm-5-3-flash.md), the model most products will actually use, is MIT.

## Reading the strategy honestly

Two framings coexist, and both are in evidence. The generous reading: a lab that puts frontier-adjacent weights in public hands faster than any western counterpart, at prices that expand access. The careful reading: "open weights" is not "open source," licensing now depends on which model you pick, and a listed company answers to shareholders for its IP decisions. A field guide should hold both.

## Sources

- [GitHub org: zai-org](https://github.com/zai-org) and [THUDM](https://github.com/THUDM) (repository data via GitHub API, 2026-09-29)
- Model cards for license fields: [GLM-5.2](https://huggingface.co/zai-org/GLM-5.2), [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3), [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)
- Community license discussion: [The New Stack (Aug 2026)](https://thenewstack.io/zai-glm-weights-license/), [smol.ai (Aug 2026)](https://news.smol.ai/)
