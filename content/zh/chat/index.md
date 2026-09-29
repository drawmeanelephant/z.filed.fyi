---
title: "在 Z.ai 对话"
description: "chat.z.ai 是什么，GLM-5.3-Flash 在其中能做什么，以及如何开始使用。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [chat, glm-5-3]
categories: [products]
layout: "layout-zai-zh"
---

chat.z.ai 是 Z.ai 面向消费者的助手产品。自 2026 年 8 月起，它的默认引擎是 GLM-5.3-Flash，也就是 Z.ai 同时以权重形式公开发布的多模态模型。

## 你可以用它做什么

它被定位为通用助手，而不是单纯的聊天窗口。根据 Z.ai 官方文档与站点描述，它的职责包括：

- **智能体任务**。助手执行多步任务而不仅是单轮回答：浏览网页、读取文件，并产出成品，例如由专门智能体生成的[幻灯片与海报](https://docs.z.ai/guides/agents/slide)，该智能体融合了信息检索、内容结构化与版面设计。
- **软件与文档**。从提示词到网站、从提示词到代码的工作流，以及办公产出：GLM-5.3-Flash 的指南将 PPTX、PDF、DOCX 与 XLSX 列为支持的专业工作流输出格式。
- **研究**。网页搜索是内置工具（API 定价为每次调用 0.01 美元），答案因此可以建立在抓取的页面上，而不只是模型记忆。
- **长时程任务**。Z.ai 称 Flash 能够跨越多步执行而不丢失目标，这项能力可以追溯到 GLM-5.2 世代的百万级上下文。

## 引擎

GLM-5.3-Flash 是 GLM-5 系列中的首个原生多模态模型：它能观察界面、渲染结果与交互反馈，Z.ai 借此打通代码、浏览器与 GUI 之间的闭环。它采用线性与稀疏注意力混合架构，320B 总参数、18B 激活参数，MIT 许可，API 价格低至每百万输入 token 0.15 美元。更完整的介绍见[模型章节](../models/glm-5-3-flash.md)。

## 如何开始

直接打开 [chat.z.ai](https://chat.z.ai/) 即可，免费体验是默认入口。付费选项通过[订阅页面](https://z.ai/subscribe)提供；重度编程用户更适合独立的[编程套餐](../code/index.md)，按配额而非按聊天计费。

## 坦诚的边界

以下限制值得直说：标注 beta 的功能可能变化；可用性可能因地区而异；网页界面不会暴露 API 的所有参数（例如推理强度与上下文上限）。任何需要可复现的结果，请优先使用 [API](../api/index.md)。

## 来源

- [z.ai](https://z.ai/)（产品定位与默认模型，2026-09-29 抓取）
- [GLM 幻灯片/海报智能体文档](https://docs.z.ai/guides/agents/slide)
- [GLM-5.3-Flash 指南](https://docs.z.ai/guides/vlm/glm-5.3-flash) 与 [模型卡](https://huggingface.co/zai-org/GLM-5.3-Flash)
- [API 定价](https://docs.z.ai/guides/overview/pricing)
