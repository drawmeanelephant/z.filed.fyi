---
title: "ZCode"
description: "Z.ai 第一方编程工作台、GLM-5.3 的官方 Harness：桌面应用、浏览器与终端三形态，附插件体系与套餐权益。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [coding, agents]
categories: [products]
layout: "layout-zai-zh"
---

ZCode 是 Z.ai 自家的编程工具：与 GLM-5.3 同期打造的多智能体开发环境，也是官方指定的 Harness。它不是一个单一应用：桌面客户端、浏览器工作区与终端智能体三种形态齐备，并接入与第三方兼容策略同源的 GLM 编程套餐。

## 它是什么

Z.ai 称 ZCode 是面向长时程任务的完整 agentic 开发环境（ADE）：自有智能体、多框架兼容与手机远程控制。实际用法是：打开一个项目（本地、SSH 或 WSL），分配目标，然后看着多个智能体规划、修改、运行与验证，在哪个界面操作都可以。公司把它定位为 GLM-5.3 的配套：与模型联合调优，支持 BYOK。

代码是开源的：仓库（zai-org/ZCode，Apache-2.0）创建于 2026 年 9 月 20 日，数周内星标超过 7,000（9 月 29 日核查时为 7,149）。

## 与编程套餐如何衔接

ZCode 是 GLM 编程套餐支持的工具之一，而且是第一梯队：通过 ZCode 使用可获得 1.5 倍用量（AutoClaw 待遇相同）。两个机制值得了解：

- **闲时任务。** 排队到空闲算力的任务不消耗套餐配额。需要有效的编程套餐；不支持裸 API-key 模式。
- **活动参与。** 在 2026 年 9 月 3 日至 10 月 7 日期间，付费用户可经 ZCode 或 AutoClaw 在夜间不消耗配额地运行 GLM-5.3-Flash。

新用户有五天试用，每日附赠 token 额度（试用期内 GLM-5.3 每日 300 万、GLM-5-Turbo 每日 200 万，以当前文档为准）。

## 内置能力

对一个这么年轻的产品来说，功能面相当宽。文档列出：面向长任务的目标模式；子智能体与命令工作流；持久记忆与项目 Wiki；自动化与定时任务；闲时队列；远程开发（SSH/WSL）与手机远程控制；微信与飞书机器人频道；用量统计；编辑历史；敏感操作的安全确认；MCP 服务与技能；hooks；插件体系。

插件是可扩展性的核心故事：一个插件可以打包技能、命令、子智能体、MCP 服务与 hooks；ZCode 自带精选公共市场（zai-org/zcode-plugins 仓库），也支持个人市场。值得一提的是，它同时预载了 Claude Code 插件市场。

## 版本与节奏

ZCode 迭代很快：版本线在 2026 年 9 月底到达 3.14.4，更新日志呈每周节奏，3.10 至 3.14 之间包含办公/编程模式切换、工作流编排、远程控制改进与安全修复。另设有公开的反馈仓库（zai-org/feedback），用户建议全程公开处理。

## 诚实说明

两点需要说明。其一，开源是近期的事且节奏很快：仓库元数据、发布记录与应用下载并不总是同步，版本号请视为快照。其二，如果要在 ZCode 与其它 Harness 之间选择，截至本快照没有可引用的官方对比评测；诚实的表述是「带套餐权益的官方 Harness」，而不是「已被证明快于某工具」。

## 来源

- [ZCode](https://zcode.z.ai/)（官网默认中文，另有英文版）与[更新日志](https://zcode.z.ai/en/changelog)
- GitHub：[zai-org/ZCode](https://github.com/zai-org/ZCode)、[zcode-plugins](https://github.com/zai-org/zcode-plugins)、[feedback](https://github.com/zai-org/feedback)
- [GLM 编程套餐：ZCode 文档](https://docs.z.ai/devpack/tool/zcode) 与[闲时任务](https://zcode.z.ai/en/docs/idle-time-tasks)
- [插件文档](https://zcode.z.ai/en/docs/plugin) 与[机器人频道文档](https://zcode.z.ai/en/docs/bot-channel)
- [GLM 编程套餐总览](https://docs.z.ai/devpack/overview) 与[活动说明](https://docs.z.ai/devpack/notice/event-glm-5.3-flash)
