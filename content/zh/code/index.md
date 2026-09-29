---
title: "在 Z.ai 编程"
description: "GLM 编程套餐：档位、配额、支持的 Claude Code 等工具，以及 ZCode 编程智能体。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [coding, agents, api]
categories: [products]
layout: "layout-zai-zh"
---

Z.ai 通过 GLM 编程套餐卖「编程」而不是「聊天」：一种订阅服务，把 GLM-5.3 与 GLM-5.3-Flash 接入你已经在用的编程智能体，而不是要求你换一个编辑器。

## 套餐的数字

Z.ai 开发者文档定义了三个档位，每个档位同时设有 5 小时与每周两档额度：

| 套餐 | 5 小时额度 | 每周额度 |
|------|-----------|----------|
| Lite | 2,000 | 10,000 |
| Pro | 12,000 | 60,000 |
| Max | 28,000 | 140,000 |

价格自每月 18 美元（Lite）起，Pro 与 Max 面向更高频的使用。第三方追踪站记录到 Pro 与 Max 的月费约为 80 与 168 美元，Z.ai 也周期性推出折扣（曾观察到 30% 的促销价：12.60、50.40 与 112 美元）。购买前请以[实时页面](https://z.ai/subscribe)为准：本手册记录来源当天的数据，而不是结账页面明天的数据。

额度按 token 消耗折算，不同模型有不同系数：当前系数下，GLM-5.3 的输出按 24、GLM-5.3-Flash 的输出按 8 计（每万 token）。5 小时额度滚动刷新，每周额度每七天重置。

## 能接入什么

卖点是兼容性。Z.ai 官方文档点名了 Claude Code、Cline、OpenCode、Kilo Code 与 Clawdbot/OpenClaw 等工具，第三方统计称支持的工具超过二十种，包括 ZCode、Cursor 等。所有档位都附带视觉理解、网页搜索、网页阅读与 Zread（代码库阅读）MCP 服务。

2026 年 9 月，Z.ai 还推出活动：付费用户在 9 月 3 日至 10 月 7 日期间，每天 23:00 至次日 09:00 可通过 [ZCode](../zcode/index.md) 与 [AutoClaw](../autoclaw/index.md) 无限使用 GLM-5.3-Flash，其它智能体配额翻倍。这条消息比任何评测表都更能说明公司的增长意图。

## ZCode 与伙伴

[ZCode](../zcode/index.md)（zcode.z.ai）是 Z.ai 的第一方编程智能体：一个多智能体工作台，2026 年 9 月发布后数周内 GitHub 星标超过 7,000，并拥有自己的插件市场。它是编程套餐的自然搭配，但并非必需；套餐的另一款第一方客户端 [AutoClaw](../autoclaw/index.md) 另有专属页面。面向团队，Team Plan 提供席位管理、用量分析与预算控制。

设备自动化是另一翼：[AutoGLM-Phone-Multilingual](../autoglm/index.md)（2025 年 12 月发布）可通过 ADB 在 50 多个应用中执行任务，其开源框架 Open-AutoGLM 是公司星标最多的项目之一。

## 如何选择

如果你已经在为编程智能体付费，只想要更强的模型，编程套餐是最短路径。如果你要构建自己的产品，请转到 [API 平台](../api/index.md)：不同的密钥、不同的限制、按 token 计费。如果只是想体验模型，[chat.z.ai](../chat/index.md) 免费。

## 来源

- [GLM 编程套餐总览](https://docs.z.ai/devpack/overview) 与 [Team Plan](https://docs.z.ai/devpack/teamplan)
- [Z.ai 开发者文档索引](https://docs.z.ai/llms.txt)（工具兼容列表）
- 第三方价格追踪：[rankllms.com](https://rankllms.com/)、[techtrenderyusa.com](https://techtrenderyusa.com/)、[zentor.ai](https://zentor.ai/)（价格会变动，视为快照）
- GitHub：[zai-org/ZCode](https://github.com/zai-org/ZCode)、[zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)
- [GLM-5.3-Flash 活动说明](https://docs.z.ai/devpack/notice/event-glm-5.3-flash)
