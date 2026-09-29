---
title: "GLM-5.3-Flash"
description: "Z.ai 的原生多模态主力：320B 总参数、18B 激活、MIT 许可，也是 chat.z.ai 背后的模型。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [glm, glm-5-3, multimodal, open-source]
categories: [models]
layout: "layout-zai-zh"
---

GLM-5.3-Flash 是 GLM-5 系列中首个原生多模态模型，Z.ai 对它的定位是「前沿智能，闪电成本」。它也是公司摆在消费者面前的默认引擎（chat.z.ai），大概率会是多数企业实际集成的那个模型。

## 为成本而生的架构

关键数字：320B 总参数、每 token 激活 18B，采用稀疏与线性注意力混合设计。Z.ai 称其为首个把两者结合的开源前沿模型，并报告该设计相较 GLM-5.3 将注意力计算降低 3.01 倍、KV 缓存压力降低 4.44 倍。另一项「流形约束超连接」（mHC）机制补全了扩展性叙事；与旗舰不同，Flash 从全新的基座模型训练而来。

## 多模态买到了什么

这里的视觉能力不是外挂。Flash 能观察界面、渲染结果与交互反馈，从而在代码、浏览器与 GUI 之间形成闭环。落到实践：它能「看见」自己写的前端与游戏；支持 Blender 3D 场景；通过 Z.ai 的 BUA 与 CUA 智能体栈操作真实设备。编程之外，它还能端到端处理办公与金融研究工作流，输出成品的 PPTX、PDF、DOCX 与 XLSX。

## 基准与价格

Z.ai 称 Flash 以旗舰十分之一的 API 价格在公开基准上全面超过 GLM-5.2，并在编程与智能体评测上「接近 Claude Opus 4.8」。模型卡记录 Terminal Bench 2.1 得分 84.3（Claude Code 框架）。API 定价为每百万输入 token 0.15 美元、输出 0.50 美元，缓存输入 0.03 美元。更快的 FlashX 档（200 token/秒）为 $0.37 / $1.25。

## 别名故事

发布之前，一个叫「ox-alpha」的神秘模型免费出现在 OpenRouter 上，点燃了开发者社区；数日后 Z.ai 揭晓 GLM-5.3-Flash，社区把线索拼了起来，普遍将此解读为一次刻意的试水。该模型采用 MIT 许可，是当前产品线中许可最宽松的前沿级选项。

## 在哪里遇见它

默认情况下是 chat.z.ai。GLM 编程套餐的每个档位都包含它，配额是旗舰的三倍（见[在 Z.ai 编程](../code/index.md)）；2026 年 9 月至 10 月初，Z.ai 还为其推出了通过自家 ZCode 与 AutoClaw 工具的夜间无限量活动。对 API 开发者而言，它就是[定价表](../api/index.md)里最便宜的那一列。

## 来源

- [GLM-5.3-Flash 指南](https://docs.z.ai/guides/vlm/glm-5.3-flash) 与 [发布说明 2026-08-26](https://docs.z.ai/release-notes/new-released)
- [GLM-5.3-Flash 模型卡](https://huggingface.co/zai-org/GLM-5.3-Flash)
- [Z.ai 定价页](https://docs.z.ai/guides/overview/pricing)
- 社区：OpenRouter「ox-alpha」讨论（Reddit r/LocalLLaMA、smol.ai、latent.space，2026-08）
