---
title: "GLM-5 世代（5 / 5.1 / 5.2）"
description: "2026 年上半程的三次发布：从「写代码」到「写工程」的 GLM-5、可运行 8 小时的 5.1、以及 1M 上下文的 5.2。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [glm, glm-5, open-source, benchmarks]
categories: [models]
layout: "layout-zai-zh"
---

GLM-5 世代横跨 2026 年 2 月到 6 月，也是智谱的模型不再被描述为「编程工具」、而被描述为「工程系统」的转折点。三次发布，一条主线。

## GLM-5（2026 年 2 月）

世代的起手式。Z.ai 报告 744B 总参数、40B 激活，相比 GLM-4.5 的 355B/32B 翻倍，预训练数据量达 28.5 万亿 token。设计上融合了 DeepSeek 的稀疏注意力以提升 token 效率，同时保持长上下文质量；发布时直接对标 Claude Opus 4.5 的「代码逻辑密度与系统工程能力」。配套论文标题是《GLM-5: from Vibe Coding to Agentic Engineering》。两条超出评测表的事实引发关注：权重以 MIT 发布；多家独立分析指出该模型完全在华为昇腾芯片上训练。发布时，Hugging Face 社区将其评为 Artificial Analysis 上排名第一的开源权重模型。

## GLM-5.1（2026 年 4 月 7 日）

耐力版本。GLM-5.1 的卖点是时间维度：单次运行最长可自主工作 8 小时，覆盖规划、执行、迭代到交付。Z.ai 将稳定性归功于多轮 SFT、强化学习与过程质量评估框架，并称其与 Claude Opus 4.6 全面对齐。模型卡记录 SWE-bench Pro 58.4、Terminal Bench 2.0 63.5。

## GLM-5.2（2026 年 6 月 16 日）

上下文版本。GLM-5.2 引入一百万 token 的无损上下文窗口，直指长时程任务；稀疏注意力层把满上下文下每 token 的 FLOPs 降低 2.9 倍，调优后的 MTP 层把投机解码接受长度提升最多 20%。它的模型卡对许可措辞强硬：「纯开放：MIT 开源许可，无地域限制，无技术获取壁垒。」基准：SWE-bench Pro 62.1、Terminal Bench 2.1（Terminus-2）81.0，最佳框架 82.7；对照表包括 Qwen3.7-Max、MiniMax M3、DeepSeek-V4-Pro、Claude Opus 4.8、GPT-5.5 与 Gemini 3.1 Pro。它也是后来 [GLM-5.3](glm-5-3.md) 用后训练「软升级」的那块基座。

## 一张表看整个世代

| | GLM-5 | GLM-5.1 | GLM-5.2 |
|---|---|---|---|
| 发布 | 2026-02 | 2026-04 | 2026-06 |
| 参数 | 744B / 40B 激活 | GLM-5 规模 | 约 743B MoE |
| 关键词 | 工程化 | 8 小时自主 | 1M 上下文 |
| SWE-bench Pro | - | 58.4 | 62.1 |
| 许可 | MIT | MIT | MIT |

## 为什么重要

这一轮是 2026 年初资本市场叙事与技术叙事交汇的地方：一条足够好、可在合规硬件上训练、价格让西方前沿厂商难受的开放权重路线。此后的一切：[GLM-5.3 双雄](glm-5-3.md)、[上市之年](../history/engineering-era.md)，都建立在这三次发布建立的可信度之上。

## 来源

- [发布说明](https://docs.z.ai/release-notes/new-released) 与 [迁移指南](https://docs.z.ai/guides/overview/migrate-to-glm-new)
- 模型卡：[GLM-5](https://huggingface.co/zai-org/GLM-5)、[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)、[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)
- [arXiv 2602.15763](https://arxiv.org/abs/2602.15763)《GLM-5: from Vibe Coding to Agentic Engineering》
- [Hugging Face 博客：GLM-5，中国首家上市 AI 公司交付前沿模型](https://huggingface.co/blog/mlabonne/glm-5)
- 华为训练细节的独立报道：Towards AI、Bad Labels、llm-bento（2026-02）
