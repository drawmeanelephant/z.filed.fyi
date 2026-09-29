---
title: "AutoClaw"
description: "Z.ai 为 OpenClaw 打造的一键桌面客户端：它能做什么、内置哪些能力，以及它与 GLM 编程套餐、开放框架生态的关系。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [agents, ecosystem]
categories: [products]
layout: "layout-zai-zh"
---

AutoClaw 是 Z.ai 的桌面工作智能体，也是一个直白问题的答案：OpenClaw 这个开源个人智能体框架能力强大，但从零搭起来并不轻松。AutoClaw 把安装变成一步，附上精选技能库与 Z.ai 自家的浏览器自动化，并把整条链路接到 GLM 模型上。

## 它是什么

Z.ai 将 AutoClaw 定位为「AI agent for Work」，官方文档里则称它是基于 OpenClaw 框架的数字员工：约一分钟本地安装，无需开发环境、无需 API key，之后交给它的就是目标而不是提示词。它运行在桌面上，而不是一个网页产品；工作通过聊天与 IM 界面发生，而不是单一控制台。

产品于 2026 年 3 月 10 日发布，中文科技媒体称其为国内首个「真·一键安装」的本地版 OpenClaw；此后持续更新（本快照时为 1.17.8，2026 年 8 月 27 日）。

## 与 OpenClaw 的关系

OpenClaw 是独立的开源项目，不是 Z.ai 的产品：一个自托管的个人智能体框架，创建于 2025 年 11 月（早期几个月以 Clawdbot 之名存在，后因商标压力经历改名），MIT 许可，现由一个有广泛企业参与的非营利基金会治理。AutoClaw 是 Z.ai 面向该框架的客户端，其更新日志会同步 OpenClaw 内核版本；Z.ai 负责补上外围体验：预设技能、IM 集成与设备侧自动化。

## 它能做什么

Z.ai 把 AutoClaw 的能力组织为六个方向：

- **办公自动化。** Word、Excel、PPT、报告、会议纪要与结构化文档，背后是 50 余项内置技能。
- **内容运营。** 多平台起草与改写（Telegram 与 Instagram 帖子、Substack 长文、X 长贴、TikTok 脚本），从选题到排期。
- **投资研究。** 行情数据、公告文件、策略回测与结构化分析报告。
- **网页产品搭建。** 描述一个页面、dashboard 或内部工具，AutoClaw 产出可运行的前端代码并在浏览器中预览。
- **浏览器自动化。** 表单填写、截图、网页数据采集、控制台检查与定时浏览器任务，由 Z.ai 的 Browser-Use 能力驱动。
- **IM 集成。** 在聊天里 @ 助手分配工作；结果、文件与进度回流到会话中。

在六个方向之外，应用还叠加了多智能体「集群」工作流、产出可编辑视觉的设计智能体、部署平台连接器、定时任务与应用内收件箱。模型菜单以 GLM 系列为主（GLM-5.3-Flash、GLM-5.3、GLM-5.2 与 Turbo 变体），同时支持热切换其它厂商模型。

## 模型、会员与编程套餐

AutoClaw 与 GLM 编程套餐深度绑定：

- 新用户注册即得 2 亿 token 奖励（标注价值 24 美元）。
- 连接 AutoClaw 的编程套餐订阅者享有 150% 配额加成（限时）；每月登录可领加赠额度（Lite 5,000、Pro 10,000、Max 26,000）。
- 同时支持个人与团队套餐。

2026 年 9 月 3 日至 10 月 7 日，Z.ai 推出夜间活动：付费用户可在 23:00 至 09:00 通过 ZCode 与 AutoClaw 无限使用 GLM-5.3-Flash，不消耗配额。

## 平台与版本

- **桌面端。** macOS（Apple 芯片与 Intel）与 Windows 10 及以上。
- **中文版。** 在标准平台之外提供麒麟系统（x86 与 ARM）版本，并提供团队购买渠道。
- **移动端。** iOS 与 Android 伴侣应用，可查看并触发任务；另有网页工作区。

## 诚实说明

快照显示出几件事：下载链接由 JavaScript 生成，本手册只链接官方页面、不镜像安装包；截至 2026 年 9 月 29 日，套餐管理仍显示「即将推出」状态；国际版与中文版存在小差异（麒麟系统、团队购买）；与任何快速迭代的客户端一样，版本与额度请以官方页面为准。

## 来源

- [AutoClaw](https://autoclaw.z.ai/)（国际版）与 [AutoClaw（中文版）](https://autoclaw.zhipuai.cn/)
- [什么是 AutoClaw](https://autoclaw.z.ai/blog/product/what-is-autoclaw/)（产品博客）与[更新日志](https://autoclaw.z.ai/changelog/)
- [GLM 编程套餐：AutoClaw 配置](https://docs.z.ai/devpack/tool/autoclaw) 与[活动说明](https://docs.z.ai/devpack/notice/event-glm-5.3-flash)
- 模型菜单：[autoclaw.z.ai/models](https://autoclaw.z.ai/models/)；发布报道：IT之家（2026-03-10）
- 框架背景：[openclaw.ai](https://openclaw.ai/) 与 [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)
