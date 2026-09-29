---
title: "GLM 模型线"
description: "从 2022 年的 GLM-130B 到 2026 年的 GLM-5.3-Flash：每个重要版本的索引与对照。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [glm, models, open-source]
categories: [models]
layout: "layout-zai-zh"
---

GLM 意为 General Language Model。这条模型线从 2022 年的一项学术开源实验，走到了 2026 年支撑一家上市公司的产品组合。本页是索引，每一代都有独立章节。

## 当前旗舰

| 模型 | 发布 | 参数 | 上下文 | 许可 | 价格（输入/输出，每百万 token） |
|------|------|------|--------|------|-------------------------------|
| [GLM-5.3](glm-5-3.md) | 2026-08 | 5.2 基座 | 1M | 自定义（非 MIT） | $1.40 / $4.40 |
| [GLM-5.3-Flash](glm-5-3-flash.md) | 2026-08 | 320B 总 / 18B 激活 | 1M | MIT | $0.15 / $0.50 |
| [GLM-5.2](glm-5-family.md) | 2026-06 | 约 743B MoE | 1M | MIT | $1.40 / $4.40 |
| [GLM-5.1](glm-5-family.md) | 2026-04 | 5 世代基座 | 长时程 | MIT | $1.40 / $4.40 |
| [GLM-5](glm-5-family.md) | 2026-02 | 744B / 40B 激活 | 1M 级 | MIT | $1.00 / $3.20 |

## 完整年表

<ul class="z-timeline">
  <li><span class="t-date">2022-08</span><span class="t-body"><strong>GLM-130B</strong> - 开源双语预训练模型；ICLR 2023</span></li>
  <li><span class="t-date">2023-03</span><span class="t-body"><strong>ChatGLM-6B</strong> - 单卡可跑的开源对话模型；下载量逾千万</span></li>
  <li><span class="t-date">2023-06</span><span class="t-body"><strong>ChatGLM2-6B</strong> - 第二代</span></li>
  <li><span class="t-date">2023-10</span><span class="t-body"><strong>ChatGLM3</strong> - 第三代系列</span></li>
  <li><span class="t-date">2024-01</span><span class="t-body"><strong>GLM-4</strong> - 新基座；定调 2024 年的 DevDay 发布</span></li>
  <li><span class="t-date">2024-06 至 08</span><span class="t-body"><strong>GLM-4-9B、GLM-4V-9B、GLM-4-Plus</strong> - 开源小模型与更强的托管档位</span></li>
  <li><span class="t-date">2025-07</span><span class="t-body"><strong>GLM-4.5 与 Air</strong> - 「ARC」基座模型；开放权重路线的转折点</span></li>
  <li><span class="t-date">2025-08</span><span class="t-body"><strong>GLM-4.5V 与幻灯片/海报智能体</strong> - 视觉与智能体产品线</span></li>
  <li><span class="t-date">2025-09</span><span class="t-body"><strong>GLM-4.6</strong> - 2025 年的编程旗舰</span></li>
  <li><span class="t-date">2025-12</span><span class="t-body"><strong>GLM-4.6V、GLM-4.7、GLM-4.7-Flash</strong> - 视觉刷新；年末开源旗舰</span></li>
  <li><span class="t-date">2026-01</span><span class="t-body"><strong>GLM-Image、GLM-4.7-Flash</strong> - 在国产芯片上完成训练的图像生成</span></li>
  <li><span class="t-date">2026-02</span><span class="t-body"><strong>GLM-5、GLM-OCR</strong> - 工程化世代开启</span></li>
  <li><span class="t-date">2026-04</span><span class="t-body"><strong>GLM-5.1</strong> - 单次运行最长 8 小时的自主执行</span></li>
  <li><span class="t-date">2026-06</span><span class="t-body"><strong>GLM-5.2</strong> - 1M 无损上下文；MIT「纯开放」</span></li>
  <li><span class="t-date">2026-08</span><span class="t-body"><strong>GLM-5.3 与 GLM-5.3-Flash</strong> - 编程跃升与原生多模态 Flash</span></li>
</ul>

两个规律值得注意。第一是节奏：自 2025 年初以来，大约每三个月就有一个有分量的旗舰。第二是许可曲线：直到 GLM-5.2 都是 MIT，而 GLM-5.3 转向自定义许可，其 Flash 同代仍保持 MIT。[开源章节](../company/open-source.md)解释了这对使用者意味着什么。

本部分页面：[GLM-5.3](glm-5-3.md), [GLM-5.3-Flash](glm-5-3-flash.md), [GLM-5 世代](glm-5-family.md), [GLM-4.5 至 4.7](glm-4-x-era.md), [GLM-130B 至 GLM-4](earlier.md)。

## 来源

- [docs.z.ai 发布说明](https://docs.z.ai/release-notes/new-released)（官方年表）
- [Z.ai 定价页](https://docs.z.ai/guides/overview/pricing)
- Hugging Face 模型卡：[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)、[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)、[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)、[GLM-5](https://huggingface.co/zai-org/GLM-5)、[GLM-4.7](https://huggingface.co/zai-org/GLM-4.7)
- GitHub：[zai-org/GLM-130B](https://github.com/zai-org/GLM-130B)、[zai-org/ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B)
