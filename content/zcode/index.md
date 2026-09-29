---
title: "ZCode"
description: "Z.ai's first-party coding workbench and the official harness for GLM-5.3: desktop app, browser, and terminal, with plugins and plan perks."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [coding, agents]
categories: [products]
---

ZCode is Z.ai's own coding tool: a multi-agent development environment built alongside GLM-5.3 and sold as the model's official harness. It is not a single app: it ships as a desktop client, a browser workspace, and a terminal agent, and it slots into the same GLM Coding Plan that powers the company's third-party compatibility push.

## What it is

Z.ai calls ZCode a full-featured agentic development environment (ADE) for long-horizon tasks, with a proprietary agent, multi-framework compatibility, and mobile remote control. In practice: you open a project (locally, over SSH, or in WSL), assign goals, and watch multiple agents plan, edit, run, and verify from whichever surface you prefer. The company positions it as the pairing to GLM-5.3, co-tuned with the model and BYOK-capable.

The code is open source: the repository (zai-org/ZCode, Apache-2.0) was created on September 20, 2026, and passed 7,000 stars within weeks (7,149 at the September 29 check).

## How it connects to the plan

ZCode is one of the tools the GLM Coding Plan supports, and a first-class one: subscribers get 1.5x usage when working through ZCode (AutoClaw gets the same treatment). Two mechanics are worth knowing:

- **Idle-time tasks.** Work queued to spare capacity runs without consuming plan quota. An active coding plan is required; raw API-key mode is not supported.
- **Campaign participation.** During the September 3 to October 7, 2026 window, paid users could run GLM-5.3-Flash overnight without burning quota, via ZCode or AutoClaw.

New users get a five-day trial with a daily token allowance (3M on GLM-5.3 plus 2M on GLM-5-Turbo during the trial, per the current docs).

## What ships inside

The feature surface is wide for a tool this young. The documented set includes: a goal mode for long-running objectives; subagents and command workflows; persistent memory and a project wiki; automations and scheduled tasks; idle-time queuing; remote development (SSH and WSL) and phone-based remote control; bot channels on WeChat and Feishu; usage statistics; edit history; safety confirmations for sensitive actions; MCP servers and skills; hooks; and a plugin system.

Plugins are the extensibility story. A plugin can bundle skills, commands, subagents, MCP servers, and hooks; ZCode ships with a curated public marketplace (the zai-org/zcode-plugins repository) plus support for personal marketplaces. Notably, it preloads the Claude Code plugin marketplace as well.

## Versions and cadence

ZCode is in rapid release: the version line reached 3.14.4 by the end of September 2026, and the changelog shows a weekly cadence, with office and coding mode switches, workflow orchestration, remote-control improvements, and safety fixes across the 3.10 to 3.14 stretch. There is also a formal feedback repository (zai-org/feedback) where user suggestions are tracked in public.

## Honest notes

Two caveats belong here. First, the open-sourcing is new and fast-moving: repository metadata, releases, and app downloads do not always move in lockstep, so treat version numbers as snapshots. Second, if you are choosing between ZCode and another harness, there is no official head-to-head benchmark to cite as of this snapshot; the honest framing is "the official harness with plan perks", not "proven faster than X".

## Sources

- [ZCode](https://zcode.z.ai/) (product site; defaults to Chinese, English available) and [changelog](https://zcode.z.ai/en/changelog)
- GitHub: [zai-org/ZCode](https://github.com/zai-org/ZCode), [zcode-plugins](https://github.com/zai-org/zcode-plugins), [feedback](https://github.com/zai-org/feedback)
- [GLM Coding Plan: ZCode docs](https://docs.z.ai/devpack/tool/zcode) and [idle-time tasks](https://zcode.z.ai/en/docs/idle-time-tasks)
- [Plugin docs](https://zcode.z.ai/en/docs/plugin) and [bot channel docs](https://zcode.z.ai/en/docs/bot-channel)
- [GLM Coding Plan overview](https://docs.z.ai/devpack/overview) and [campaign notice](https://docs.z.ai/devpack/notice/event-glm-5.3-flash)
