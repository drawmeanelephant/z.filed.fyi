---
title: "The GLM-5 generation"
description: "GLM-5, GLM-5.1, and GLM-5.2: the 2026 run that took Zhipu's models from coding assistants to engineering systems."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [glm, glm-5, open-source, benchmarks]
categories: [models]
---

The GLM-5 generation spans February to June 2026 and marks the point where Zhipu's models stopped being described as coding tools and started being described as engineering systems. Three releases, one story.

## GLM-5 (February 2026)

The generation's opening move. Z.ai reports 744B total parameters with 40B active, doubling the size of GLM-4.5's 355B/32B, and pretraining on 28.5 trillion tokens. The design integrates DeepSeek's sparse attention for token efficiency while keeping long-context quality, and the release is openly benchmarked against Claude Opus 4.5 on "code-logic density and systems-engineering capability." The accompanying paper is titled "GLM-5: from Vibe Coding to Agentic Engineering." Two facts made headlines beyond the benchmark table: the weights shipped under MIT, and multiple independent analyses state the model was trained entirely on Huawei Ascend chips. At launch, the Hugging Face community ranked it the top open-weight model on Artificial Analysis.

## GLM-5.1 (April 7, 2026)

The endurance release. GLM-5.1's headline is temporal: it can work independently for up to eight hours in a single run, covering planning, execution, iterative refinement, and delivery. Z.ai attributes the stability to multi-turn SFT, RL, and a process-quality evaluation framework, and cites alignment with Claude Opus 4.6 on agentic engineering. The model card records 58.4 on SWE-bench Pro and 63.5 on Terminal Bench 2.0.

## GLM-5.2 (June 16, 2026)

The context release. GLM-5.2 introduced a one-million-token lossless context window aimed squarely at long-horizon tasks, with sparse attention layers cutting per-token FLOPs by 2.9x at full context and a tuned MTP layer improving speculative-decoding acceptance by up to 20 percent. Its model card is emphatic about licensing: "Pure Open: an MIT open-source license, no regional limits, technical access without borders." Benchmarks: 62.1 on SWE-bench Pro, 81.0 on Terminal Bench 2.1 (Terminus-2 harness) and 82.7 best-reported, with comparison rows against Qwen3.7-Max, MiniMax M3, DeepSeek-V4-Pro, Claude Opus 4.8, GPT-5.5, and Gemini 3.1 Pro. It is also the base model that [GLM-5.3](glm-5-3.md) later upgraded the soft way, through post-training alone.

## The generation in one table

| | GLM-5 | GLM-5.1 | GLM-5.2 |
|---|---|---|---|
| Released | Feb 2026 | Apr 2026 | Jun 2026 |
| Parameters | 744B / 40B active | GLM-5 scale | ~743B MoE |
| Signature | Engineering focus | 8-hour autonomy | 1M context |
| SWE-bench Pro | - | 58.4 | 62.1 |
| License | MIT | MIT | MIT |

## Why it mattered

This run is where the valuation narrative of early 2026 met the technology: an open-weight line good enough that enterprises could build on it, on hardware the export-control regime permits, at prices Western frontrunners could not match. Everything after it - the [GLM-5.3 pair](glm-5-3.md), the [IPO year](../history/engineering-era.md) - builds on the credibility these three releases created.

## Sources

- [Release notes](https://docs.z.ai/release-notes/new-released) and [migration guide](https://docs.z.ai/guides/overview/migrate-to-glm-new)
- Model cards: [GLM-5](https://huggingface.co/zai-org/GLM-5), [GLM-5.1](https://huggingface.co/zai-org/GLM-5.1), [GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)
- [arXiv 2602.15763](https://arxiv.org/abs/2602.15763) "GLM-5: from Vibe Coding to Agentic Engineering"
- [Hugging Face blog: GLM-5, China's first public AI company ships a frontier model](https://huggingface.co/blog/mlabonne/glm-5)
- Reported Huawei-training detail: Towards AI, Bad Labels, llm-bento summaries (Feb 2026)
