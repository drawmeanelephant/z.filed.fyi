---
title: "AutoGLM"
description: "Z.ai's device-agent line: phone agents that operate real apps, the open-source Open-AutoGLM framework, and the models behind them."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [agents, open-source]
categories: [products]
---

AutoGLM is the part of Z.ai's stack that operates devices rather than desktops or repositories: agents that read a phone screen, decide what to tap, and carry out tasks inside real apps. It is a product family and a research line at once, and its open-source wing, Open-AutoGLM, is one of the company's most-starred repositories.

## What the line covers

Three surfaces, one story:

- The device-agent platform itself, at autoglm.z.ai internationally and autoglm.zhipuai.cn in China, where it is positioned as a report and operations assistant.
- The phone-agent models: AutoGLM-Phone-9B and its multilingual sibling, published openly in December 2025.
- Open-AutoGLM, the open framework that lets anyone run the phone agent on their own devices.

The name also travels as a credit line: AutoClaw's own footer reads "AutoClaw by AutoGLM".

## The arc

- **October 2024.** The company demonstrates the first full real-device operation chain for its phone agents, which its material presents as a world first for this class of tool.
- **2025.** AutoGLM 2.0 ships alongside the company's reinforcement-learning stack (MobileRL, ComputerRL, AgentRL) and a cloud virtual-phone sandbox.
- **March 2025.** A preview of AutoGLM 沉思 brings deep-research and operator behavior to the domestic chat surfaces.
- **August 2025.** Chinese press describes the phone agent running on GLM-4.5, locally or in the cloud.
- **December 2025.** Open-AutoGLM is open-sourced (December 8), and AutoGLM-Phone-Multilingual arrives with support for tasks across 50+ apps via ADB.
- **2026.** The line's Browser-Use capability shows up inside AutoClaw, and a cloud AutoGLM benefit runs for Coding Plan subscribers during the spring.

## Open-AutoGLM, the open wing

The framework repository (zai-org/Open-AutoGLM, Apache-2.0) was created on December 8, 2025, and had gathered 26.3k stars by the September 29, 2026 check. Its README describes a mobile-assistant framework built on multimodal screen understanding and ADB control (HDC on HarmonyOS), with safety defaults worth noting: sensitive actions require confirmation, and flows like logins stay with the human. It integrates with Midscene for iOS and Android workflows, and it is published for research and learning use. The companion models, AutoGLM-Phone-9B and AutoGLM-Phone-9B-Multilingual, are MIT licensed and available on Hugging Face; the multilingual variant builds on GLM-4.1V-9B-Base.

## Platform notes

Running the open framework takes Python 3.10 or newer and an Android 7.0+ device (or a HarmonyOS device with developer mode) plus the usual ADB or HDC tooling; the models also live on ModelScope. The hosted product is at autoglm.z.ai and autoglm.zhipuai.cn, and the Chinese surface also ships 智谱AI输入法 (Autotyper), a voice-first keyboard.

## Honest limits

Two cautions. First, some of the strongest claims in this line's history (the "world's first" phone-agent framing) come from the company or from press coverage, and this page carries them as attributed, not as independently verified. Second, the public record is uneven: the international surface is the thinnest of Z.ai's product sites, release notes lean Chinese, and usage metrics such as active devices are not published. Where facts rest on a single source, they say so.

## Sources

- [AutoGLM](https://autoglm.z.ai/) and [the AutoGLM blog](https://autoglm.z.ai/blog) (timeline entries, open-sourcing announcement)
- [Open-AutoGLM repository](https://github.com/zai-org/Open-AutoGLM) (stars, license, creation date, framework notes)
- [AutoGLM-Phone-9B-Multilingual](https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual) (license, base model)
- [Z.ai release notes](https://docs.z.ai/release-notes/new-released) (AutoGLM-Phone-Multilingual, December 2025)
- [BigModel coding plan docs](https://docs.bigmodel.cn/cn/coding-plan/benefits/autoglm-openclaw) (cloud AutoGLM benefit)
- Chinese press retrospectives: 腾讯新闻 (2025-08-27), 搜狐 (2025-03-31)
