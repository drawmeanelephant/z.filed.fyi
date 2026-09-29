---
title: "生态"
description: "GLM 模型在哪里运行：智能体工具、MCP 服务、云服务商，以及它们所处的竞争格局。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [ecosystem, agents, coding]
categories: [company]
layout: "layout-zai-zh"
---

模型家族的价值取决于它能接进多少场景。智谱的生态策略异常偏向互操作：在开发者已经在用的工具里与他们相遇。

## 智能体工具

GLM 编程套餐宣称兼容二十余种编程智能体。官方点名的包括 Claude Code、Cline、OpenCode 与 Kilo Code；Z.ai 文档还把 Clawdbot/OpenClaw 与自家的 ZCode 并列列出——后者是公司的第一方编程智能体（2026 年 9 月上线后数周内星标超过 7,000，并拥有自己的插件市场）。第三方统计把 Cursor、Zed 流水线等也计入名单。潜台词是：让模型去找开发者，而不是要求开发者换工具。

## 工具与协议

所有编程套餐档位都附带视觉理解、网页搜索、网页阅读与 Zread（代码库阅读）MCP 服务，智能体工作流无需胶水代码即可获得检索与感知能力。API 平台把同样的能力作为计价工具提供。

## 基础设施

- **云与推理服务商**。GLM-5.x 模型卡列出的服务伙伴包括 Together、Novita、DeepInfra 与 Featherless——开放权重领域常见的一组名字。
- **芯片**。多家独立分析称 2026 年的旗舰世代全程在华为昇腾芯片上训练；Z.ai 也表示 GLM-Image 完全基于国产算力训练。无论对地缘政治持何种看法，这是一个在这个规模上西方没有对应物的供应链事实。
- **设备**。AutoGLM 系列把技术栈延伸到手机：AutoGLM-Phone-Multilingual 通过 ADB 在 50 多个应用中执行任务，开源仓库 Open-AutoGLM 是公司星标最多的项目之一。

## 竞争格局

GLM-5.2 的基准表自己列出了对照：Qwen3.7-Max（阿里）、MiniMax M3、DeepSeek-V4-Pro、Claude Opus 4.8、GPT-5.5 与 Gemini 3.1 Pro——提醒人们智谱在两线作战：与国内实验室争夺心智，与西方前沿实验室在开放权重的价格-性能上较量。Flash 发布期间的社区评论（「开放模型正在追上来」）捕捉了情绪；最终裁决应交给基准表，而不是情绪。

## 手册止于何处

生态每周都在变。这里的一切都带日期与来源；请把它当作快照，并沿文中的一手来源链接查看当前状态。

## 来源

- [GLM 编程套餐总览](https://docs.z.ai/devpack/overview) 与 [文档索引](https://docs.z.ai/llms.txt)
- 模型卡：[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)、[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)（服务商列表）
- [GitHub：zai-org](https://github.com/zai-org)（ZCode、Open-AutoGLM、插件市场）
- 训练硬件报道：Towards AI、Bad Labels（2026-02）；[发布说明](https://docs.z.ai/release-notes/new-released)（GLM-Image、AutoGLM-Phone）
- 社区视角：latent.space（2026-08-22）、smol.ai（2026-08-24）
