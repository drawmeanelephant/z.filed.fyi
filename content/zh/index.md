---
title: "Z.ai 参考手册"
description: "关于 Z.ai 与智谱 AI 的独立参考：公司历史、chat.z.ai、GLM 编程套餐与 GLM 模型线；每页均附来源。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [zhipu, glm, ecosystem]
categories: [meta]
layout: "layout-zai-home-zh"
---

Z.ai 是智谱 AI（Zhipu AI）的国际平台。这家来自北京的公司自 2022 年起持续发布 GLM 系列模型，并于 2026 年 1 月成为全球首家上市的大模型公司。本手册覆盖完整的脉络：研究、模型、产品，以及它们留下的公开记录。

<div class="card-grid">
  <a class="card" href="chat/">
    <span class="card-kicker">产品</span>
    <span class="card-title">在 Z.ai 对话</span>
    <span class="card-body">chat.z.ai 助手，由 GLM-5.3-Flash 驱动。</span>
  </a>
  <a class="card" href="code/">
    <span class="card-kicker">产品</span>
    <span class="card-title">在 Z.ai 编程</span>
    <span class="card-body">GLM 编程套餐：支持 Claude Code 等工具。</span>
  </a>
  <a class="card" href="api/">
    <span class="card-kicker">开发者</span>
    <span class="card-title">在 Z.ai 开发</span>
    <span class="card-body">兼容 OpenAI 的开发者平台及其定价。</span>
  </a>
</div>

## 今天在运行的产品

- **GLM-5.3**（2026 年 8 月）是旗舰模型：在 GLM-5.2 的基座之上仅通过后训练升级，据 Z.ai 公布在自研评测 Z.ai Code Bench 上带来 50% 的编程能力提升，并在 Terminal Bench 3.0 等公开基准上取得开源模型最优结果。它同时展示了超出预期的网络安全能力，也是该系列首次采用自定义许可（而非 MIT）的旗舰。
- **GLM-5.3-Flash**（2026 年 8 月）是配套发布：原生多模态、320B 总参数 / 18B 激活参数、MIT 许可，既驱动 chat.z.ai，也以旗舰十分之一的价格提供服务。
- **chat.z.ai 与 GLM 编程套餐** 是通往这套能力的两扇门。编程套餐每月 18 美元起，目前可接入包括 Claude Code、Cline、OpenCode、ZCode 与 OpenClaw 在内的二十余种智能体工具。

## 记录

智谱于 2019 年 6 月从清华大学知识工程实验室独立创业；2022 年开源 GLM-130B，2023 年经历 ChatGLM 浪潮，2025 年以 GLM-4.5 系列确立开放权重路线。2026 年的 GLM-5 世代、港股上市以及随后的 A 股进程，都记录在[历史部分](history/index.md)中。

## 探索

除三款产品之外，手册还包含完整的[模型线](models/index.md)、[公司档案](company/index.md)、[生态地图](ecosystem/index.md)与分阶段的[历史](history/index.md)。本站同样提供英文版：[English edition](/)。

## 本站如何构建

本站由 [la-famille](la-famille/index.md) 生成，这是一个用 Go 编写的静态站点生成器；每一页都列出所使用的来源。本站是独立项目，与智谱 AI、Z.ai 无隶属关系。

## 来源

- [z.ai](https://z.ai/) 与 [docs.z.ai 发布说明](https://docs.z.ai/release-notes/new-released)
- [GLM-5.3 模型卡](https://huggingface.co/zai-org/GLM-5.3) 与 [GLM-5.3-Flash 模型卡](https://huggingface.co/zai-org/GLM-5.3-Flash)
- [GLM 编程套餐文档](https://docs.z.ai/devpack/overview)
