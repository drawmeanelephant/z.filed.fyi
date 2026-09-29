---
title: "开源"
description: "智谱究竟发布了什么：仓库清单、MIT 到自定义许可的曲线，以及比发布更长寿的社区资产。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [open-source, glm, coding]
categories: [company]
layout: "layout-zai-zh"
---

开源在智谱不是副项目，而是分发策略。本页盘点货架上实际有什么，以及许可如何演变。

## 仓库清单

星标数来自 GitHub，核对于 2026 年 9 月 29 日。组织名为 `zai-org`（研究仓库历史上属 THUDM）：

| 仓库 | 内容 | 星标 |
|------|------|------|
| ChatGLM-6B | 2023 年掀起浪潮的单卡对话模型 | 40.9k |
| Open-AutoGLM | 开放的手机智能体模型与框架 | 26.3k |
| ChatGLM2/3 | 后续开源对话世代 | 15.5k / 13.6k |
| CogVideo | 文生视频，含 CogVideoX | 13.0k |
| CodeGeeX 1/2 | 多语言代码生成 | 8.8k / 7.5k |
| GLM-130B | 2022 年开源双语预训练模型 | 7.6k |
| GLM-OCR | 轻量 OCR 模型（2026） | 7.5k |
| GLM-5 | 旗舰发布仓库 | 7.2k |
| ZCode | Z.ai 的编程智能体 | 7.1k |
| GLM-4 / GLM-4.5 | 系列仓库 | 7.1k / 4.4k |
| GLM-4-Voice | 端到端语音 | 3.2k |
| GLM-TTS、GLM-ASR、GLM-Image | 语音与图像模型（2025-2026） | 1.1k / 0.9k / 1.1k |

研究侧（THUDM）还有 RL 后训练框架 slime（8.6k）、AgentBench（3.8k）、LongBench、LongWriter，以及 P-tuning 系列。

## 许可曲线

- **2022-2025：关键的模型都是 MIT**。GLM-130B 到 GLM-5.2 均使用宽松许可；GLM-5.2 模型卡的原话是「纯开放：无地域限制，无技术获取壁垒」。
- **2026 年 8 月：转折**。[GLM-5.3](../models/glm-5-3.md) 采用自定义「glm-5.3」许可；社区报道称高收入规模的供应商需要安全审查，企业部署前建议以许可原文逐条核对。
- **重要的例外**：[GLM-5.3-Flash](../models/glm-5-3-flash.md)——多数产品实际会用的那个模型——是 MIT。

## 诚实地解读策略

两种解读同时存在，且都有证据。宽厚的解读：一家把接近前沿的权重比任何西方同行都更快交到公众手里的实验室，价格还扩大了可及性。审慎的解读：「开放权重」不等于「开源」，许可现在取决于你选哪个模型，而上市公司要为 IP 决策对股东负责。一份参考手册应当同时保留两者。

## 来源

- [GitHub 组织：zai-org](https://github.com/zai-org) 与 [THUDM](https://github.com/THUDM)（仓库数据经 GitHub API 核对，2026-09-29）
- 许可字段来源：[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)、[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)、[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) 模型卡
- 社区许可讨论：[The New Stack（2026-08）](https://thenewstack.io/zai-glm-weights-license/)、[smol.ai（2026-08）](https://news.smol.ai/)
