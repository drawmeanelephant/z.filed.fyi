---
title: "在 Z.ai 开发"
description: "Z.ai 开发者平台：兼容 OpenAI 的 API、SDK、完整模型菜单与官方定价表。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [api, glm, coding]
categories: [products]
layout: "layout-zai-zh"
---

docs.z.ai 是 Z.ai 面向开发者的入口。同一套模型家族，通过兼容 OpenAI 的 API 提供，并公开逐 token 的定价。

## 接口

请求走标准的 chat-completion 语义，迁移成本很低：把 OpenAI SDK 指向 Z.ai 的端点即可。Z.ai 还提供官方 Python 与 Java SDK、LangChain 集成文档，以及覆盖全部接口的 OpenAPI 描述。文档将流式输出、工具调用流、函数调用、结构化输出与上下文缓存列为一等能力，并提供对可复现性至关重要的控制项：新模型支持显式的推理强度档位，网页搜索工具按次计价。

## 模型菜单

以下为 Z.ai 官方定价页的费率（美元 / 每百万 token，输入 / 缓存 / 输出；2026-09-29 抓取）：

| 模型 | 输入 | 缓存 | 输出 | 备注 |
|------|------|------|------|------|
| GLM-5.3 | $1.40 | $0.26 | $4.40 | 旗舰，仅文本 |
| GLM-5.3-Flash | $0.15 | $0.03 | $0.50 | 多模态主力 |
| GLM-5.3-FlashX | $0.37 | $0.075 | $1.25 | 200 token/秒档 |
| GLM-5.2 / GLM-5.1 | $1.40 | $0.26 | $4.40 | 前代旗舰 |
| GLM-5 | $1.00 | $0.20 | $3.20 | 2026 年 2 月世代 |
| GLM-4.7 / GLM-4.6 / GLM-4.5 | $0.60 | $0.11 | $2.20 | 2025 开放权重线 |
| GLM-4.5-Air | $0.20 | $0.03 | $1.10 | 轻量文本 |
| GLM-4.6V | $0.30 | $0.05 | $0.90 | 视觉 |
| GLM-OCR | $0.03 | - | $0.03 | 版面解析 |
| GLM-4.7-Flash / GLM-4.5-Flash / GLM-4.6V-Flash | 免费 | 免费 | 免费 | 免费档 |

文本之外：GLM-Image 每张图片 0.015 美元，CogVideoX-3 视频 0.20 美元，GLM-ASR-2512 语音转写约每分钟 0.0024 美元。

## 不止是补全

平台还提供任务形态的智能体接口：幻灯片/海报智能体（beta，0.70 美元/百万 token）把研究变成设计稿；翻译服务支持术语表；视频特效模板生成短片；网页阅读器负责抓取与结构化页面。分词器与限流接口补齐了工具箱。

## 适合谁

如果你要把模型接进产品，这是按量计费的路径：与[编程套餐](../code/index.md)使用不同的密钥与配额，按生产负载而非按席位定价。如果只是体验模型，[chat.z.ai](../chat/index.md) 免费且即时。

## 来源

- [Z.ai 定价页](https://docs.z.ai/guides/overview/pricing) 与 [文档索引](https://docs.z.ai/llms.txt)（2026-09-29 抓取）
- [Chat Completion API 参考](https://docs.z.ai/api-reference/llm/chat-completion)
- [幻灯片/海报智能体文档](https://docs.z.ai/guides/agents/slide)
