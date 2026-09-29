---
title: "从 GLM-130B 到 GLM-4（2022-2024）"
description: "从学术到产品的岁月：最早的开源双语模型、ChatGLM 浪潮，以及 GLM-4 的 DevDay。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [glm, chatglm, open-source, history]
categories: [models]
layout: "layout-zai-zh"
---

在产品与上市之前，先有一条研究线。本页覆盖让智谱在机器学习圈内成名的那些模型。

## GLM-130B（2022 年 8 月）

一个 1300 亿参数的中英双语预训练模型，以开源形式发布，论文登上 ICLR 2023。以 2022 年的标准看，来自中国的这个规模的开源检查点是真正的新事物；该仓库至今仍是「GLM 早于聊天机器人浪潮」这一谱系论证的一部分。

## ChatGLM-6B（2023 年 3 月）

破圈之作。一个 60 亿参数的对话模型，能在单张 GPU 上运行，在 ChatGPT 热潮开始数周后开源。它积累了数万 GitHub 星标；据中文科技媒体回顾，累计下载量超过一千万。对中国的许多开发者而言，它是他们本地跑过的第一个大模型。ChatGLM2-6B（2023 年 6 月）与 ChatGLM3（2023 年 10 月）随后以约一个季度的节奏跟进。

## GLM-4（2024 年 1 月 16 日）

在 DevDay 活动上，智谱发布新一代基座模型 GLM-4，相比 ChatGLM 线性能大幅提升；当时媒体报道把它描述为最接近 GPT-4 级的国产模型。公司自此维持双轨：托管版 GLM-4 作为产品，小规模开源权重面向社区。

## 2024 年的开源节奏

- 2024 年 6 月：开源 GLM-4-9B 与视觉模型 GLM-4V-9B，多模态能力被描述为接近 GPT-4V 水平。
- 2024 年 7 月：视频生成，即 CogVideoX 系列。
- 2024 年 9 月：在 KDD 上发布 GLM-4-Plus 世代，以及 CogView3-Plus（图像）与 GLM-4V-Plus（视觉），构成延续到 2025 年的托管产品线。

在文本模型之外，这一阶段搭起了至今仍在的多模态货架：代码模型 CodeGeeX（2022，KDD 2023）、CogVLM（2023）、图像 CogView、视频 CogVideo、语音 GLM-4-Voice。当 2025 年的开放权重转折到来时，它有十年的实验室研究和一个完整模态货架可以调用。

## 来源

- [发布说明](https://docs.z.ai/release-notes/new-released)
- GitHub 仓库：[GLM-130B](https://github.com/zai-org/GLM-130B)、[ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B)、[ChatGLM2-6B](https://github.com/zai-org/ChatGLM2-6B)、[ChatGLM3](https://github.com/zai-org/ChatGLM3)、[GLM-4](https://github.com/zai-org/GLM-4)、[CodeGeeX](https://github.com/zai-org/CodeGeeX)
- 中文媒体回顾：PConline（2024-01-30）、腾讯新闻（2024-01-16）、掘金（2025-07-31）
