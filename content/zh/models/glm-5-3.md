---
title: "GLM-5.3"
description: "2026 年 8 月旗舰：仅靠后训练升级、编程能力跃升，以及一段意料之外的网络安全能力故事。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [glm, glm-5-3, coding, benchmarks]
categories: [models]
layout: "layout-zai-zh"
---

GLM-5.3 是 Z.ai 的旗舰模型，发布于 2026 年 8 月。它的特别之处在于「不是什么」：底下没有新基座。Z.ai 明确说明 GLM-5.3 沿用 [GLM-5.2](glm-5-family.md) 的基座，全部提升来自后训练。

## 变化在哪里

- **编程能力**。在 Z.ai 自研的 Z.ai Code Bench 上，GLM-5.3 相对 GLM-5.2 提升 50%。在公开基准上，公司声称取得开源权重模型中的最优结果，点名了 Terminal Bench 3.0 与 Agents' Last Exam (CLI)。
- **意外的网络安全能力**。随着后训练规模扩大，没人专门优化的能力一起涨了。Z.ai 报告 GLM-5.3 在 CyberGym 漏洞发现基准上取得该系列最好成绩，且在漏洞利用链上越深入、相对 GLM-5.2 的优势越大；与安全团队合作在真实目标上测试期间，共发现 2,436 个漏洞，其中 1,097 个为中高危。公司还称其在白盒代码审查上可比「Mythos 5」，该说法被行业媒体以批判性视角报道。

## 规格表

| | |
|---|---|
| 输入 | 仅文本 |
| 上下文 | 1,000,000 token |
| 最大输出 | 128,000 token |
| 推理 | 始终开启，`low` / `high` / `max` 三档（不再支持关闭） |
| API 价格 | $1.40 输入 / $0.26 缓存 / $4.40 输出（每百万 token） |
| 权重 | 已发布，采用自定义许可（非 MIT） |

推理设置的变动是真实的迁移成本：使用 `thinking.type: "disabled"` 的应用必须改为 `enabled` 并将 `reasoning_effort` 设为 `low`，否则请求会失败。

## 许可的转折

直到 GLM-5.2，该系列一直使用 MIT 许可，模型卡自称「纯开放：无地域限制」。GLM-5.3 的权重则改用自定义的「glm-5.3」许可。社区报道称，收入超过一定规模的供应商需要先行安全审查；准确条款以许可原文为准。实际含义是：如果你的合规流程默认 MIT，部署前请逐条核对。另注意其同代兄弟 [GLM-5.3-Flash](glm-5-3-flash.md) 仍然是 MIT，所以「是否开放」取决于你选哪一个模型。

## 选 5.3 还是 5.3-Flash

把它们当作一对看。GLM-5.3 是文本能力上限，成本约为 Flash 的三到九倍；GLM-5.3-Flash 多模态、MIT、便宜。多交互的产品默认选 Flash；当编程或长时程规划质量值得溢价时，再上 5.3。

## 来源

- [发布说明 2026-08-18](https://docs.z.ai/release-notes/new-released) 与 [GLM-5.3 指南](https://docs.z.ai/guides/llm/glm-5.3)
- [GLM-5.3 模型卡](https://huggingface.co/zai-org/GLM-5.3)（许可字段、评测结果）
- [Artificial Intelligence News 分析，2026-08-18](https://www.artificialintelligence-news.com/news/zhipu-glm-5-3-benchmarks-explained/)
- [SemiAnalysis inference 报道](https://inferencex.semianalysis.com/model/glm-5-3)（后训练发布、Yicai 时间）
- 社区许可讨论：[The New Stack（2026-08）](https://thenewstack.io/zai-glm-weights-license/)
