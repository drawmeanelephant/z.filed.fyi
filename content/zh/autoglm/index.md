---
title: "AutoGLM"
description: "Z.ai 的设备智能体线：直接操作真实 App 的手机智能体、开源的 Open-AutoGLM 框架，以及驱动它们的开源模型。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [agents, open-source]
categories: [products]
layout: "layout-zai-zh"
---

AutoGLM 是 Z.ai 技术栈里直接操作设备的那一支：它面向的不是桌面或代码库，而是手机屏幕：看清界面、决定点按哪里，并在真实 App 里把事情做完。它既是产品家族也是研究线，其开源支线 Open-AutoGLM 是公司星标最多的仓库之一。

## 这条线包含什么

三个面貌，同一个故事：

- 设备智能体平台本身：国际版 autoglm.z.ai，中国版 autoglm.zhipuai.cn，在国内以「报告与运营助手」定位。
- 手机智能体模型：AutoGLM-Phone-9B 及其多语言版本，2025 年 12 月公开。
- Open-AutoGLM：让任何人可以在自己设备上运行手机智能体的开源框架。

这个名字也出现在署名里：AutoClaw 自己的页脚写着「AutoClaw by AutoGLM」。

## 时间线

- **2024 年 10 月。** 公司演示了手机智能体的首条真实设备全流程操作链，其材料将其表述为该类工具的世界首次。
- **2025 年。** AutoGLM 2.0 发布，伴随公司的强化学习栈（MobileRL、ComputerRL、AgentRL）与云端虚拟手机沙箱。
- **2025 年 3 月。** AutoGLM 沉思预览版把深度研究与操作员能力带到国内对话产品。
- **2025 年 8 月。** 中文媒体报道手机智能体运行于 GLM-4.5，支持本地与云端。
- **2025 年 12 月。** Open-AutoGLM 开源（12 月 8 日）；AutoGLM-Phone-Multilingual 发布，可通过 ADB 在 50 多个 App 中执行任务。
- **2026 年。** 其 Browser-Use 能力进入 AutoClaw；春季还为编程套餐订阅者提供了云端 AutoGLM 权益。

## 开源支线：Open-AutoGLM

框架仓库（zai-org/Open-AutoGLM，Apache-2.0）创建于 2025 年 12 月 8 日，截至 2026 年 9 月 29 日核查时星标 26.3k。README 描述的是一套基于多模态屏幕理解与 ADB 控制（HarmonyOS 为 HDC）的手机助手框架，安全默认值值得一提：敏感操作需要确认，登录等环节由人接管。它为 iOS 与 Android 工作流提供 Midscene 集成，并声明仅供研究与学习使用。配套模型 AutoGLM-Phone-9B 与 AutoGLM-Phone-9B-Multilingual 为 MIT 许可，可在 Hugging Face 获取；多语言版本基于 GLM-4.1V-9B-Base。

## 平台说明

自行运行开源框架需要 Python 3.10 及以上、一台 Android 7.0+ 设备（或开启开发者模式的 HarmonyOS 设备），以及常规的 ADB/HDC 工具；模型也发布在 ModelScope。托管产品位于 autoglm.z.ai 与 autoglm.zhipuai.cn；中文侧还提供智谱AI输入法（Autotyper），一款语音优先的输入键盘。

## 诚实说明

两点提醒。其一，这条线历史上最响亮的说法（「世界首个」手机智能体）来自公司或媒体报道，本页按「据公司或据媒体」处理，而非独立核实。其二，公开记录并不均匀：国际版是 Z.ai 产品站中最简的一个，发布说明偏中文，活跃设备等指标未公布。单一来源的事实，本页会注明。

## 来源

- [AutoGLM](https://autoglm.z.ai/) 与 [AutoGLM 博客](https://autoglm.z.ai/blog)（时间线条目、开源公告）
- [Open-AutoGLM 仓库](https://github.com/zai-org/Open-AutoGLM)（星标、许可、创建日期、框架说明）
- [AutoGLM-Phone-9B-Multilingual](https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual)（许可、基座模型）
- [Z.ai 发布说明](https://docs.z.ai/release-notes/new-released)（AutoGLM-Phone-Multilingual，2025 年 12 月）
- [BigModel 编程套餐文档](https://docs.bigmodel.cn/cn/coding-plan/benefits/autoglm-openclaw)（云端 AutoGLM 权益）
- 中文媒体回顾：腾讯新闻（2025-08-27）、搜狐（2025-03-31）
