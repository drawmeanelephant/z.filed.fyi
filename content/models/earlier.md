---
title: "GLM-130B to GLM-4 (2022-2024)"
description: "The academic-to-product years: the first open bilingual models, the ChatGLM wave, and the GLM-4 DevDay."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [glm, chatglm, open-source, history]
categories: [models]
---

Before the products and the listings, there was a research line. This page covers the models that made Zhipu's name inside machine-learning circles.

## GLM-130B (August 2022)

A 130-billion-parameter bilingual (Chinese-English) pretrained model released openly, presented at ICLR 2023. In 2022, an open model of that scale from China was genuinely novel, and the repository remains part of the lineage argument that GLM predates the chatbot wave.

## ChatGLM-6B (March 2023)

The breakout. A 6-billion-parameter chat model that ran on a single GPU, released as open source weeks after ChatGPT-mania began. It accumulated tens of thousands of GitHub stars and, per Chinese tech press retrospectives, more than ten million cumulative downloads - for many developers in China it was the first large model they ever ran locally. ChatGLM2-6B (June 2023) and ChatGLM3 (October 2023) followed at roughly quarterly cadence.

## GLM-4 (January 16, 2024)

At its DevDay event, Zhipu announced GLM-4 as a new-generation base model with dramatically improved performance over the ChatGLM line - press coverage at the time framed it as the domestic model closest to GPT-4 class, roughly a year after the chatbot wave began. The company maintained a dual track from here: hosted GLM-4 tiers as products, and smaller open weights for the community.

## The 2024 open cadence

- June 2024: GLM-4-9B and the vision-capable GLM-4V-9B open-sourced, with multimodal quality described as approaching GPT-4V level.
- July 2024: video generation, the CogVideoX line.
- September 2024: at KDD, the GLM-4-Plus generation plus CogView3-Plus (images) and GLM-4V-Plus (vision), forming the hosted lineup that carried into 2025.

Alongside the text models, the period built a multimodal portfolio that still exists: CodeGeeX for code (2022, KDD 2023), CogVLM (2023), CogView for images, CogVideo for video, and GLM-4-Voice for speech. When the open-weights turn arrived in 2025, it had a decade of bench research and a full modality shelf to build on.

## Sources

- [Release notes](https://docs.z.ai/release-notes/new-released)
- GitHub repositories: [GLM-130B](https://github.com/zai-org/GLM-130B), [ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B), [ChatGLM2-6B](https://github.com/zai-org/ChatGLM2-6B), [ChatGLM3](https://github.com/zai-org/ChatGLM3), [GLM-4](https://github.com/zai-org/GLM-4), [CodeGeeX](https://github.com/zai-org/CodeGeeX)
- Chinese tech press retrospectives: PConline (2024-01-30), Tencent News (2024-01-16), Juejin (2025-07-31)
