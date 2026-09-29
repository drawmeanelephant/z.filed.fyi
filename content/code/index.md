---
title: "Code on Z.ai"
description: "The GLM Coding Plan: tiers, credits, supported tools like Claude Code, and ZCode, Z.ai's own coding harness."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [coding, agents, api]
categories: [products]
---

Z.ai sells coding through the GLM Coding Plan: a subscription that routes GLM-5.3 and GLM-5.3-Flash into whatever coding agent you already use, rather than a new editor you have to learn.

## The plan, in numbers

Z.ai's developer documentation defines three tiers, each with both a five-hour and a weekly credit allowance:

| Plan | 5-hour credits | Weekly credits |
|------|---------------|----------------|
| Lite | 2,000 | 10,000 |
| Pro | 12,000 | 60,000 |
| Max | 28,000 | 140,000 |

Pricing starts at 18 USD per month for Lite, with Pro and Max designed for higher-frequency work. Third-party trackers have recorded monthly list prices of roughly 80 USD and 168 USD for Pro and Max, and Z.ai periodically runs introductory discounts (a 30 percent promotion has been observed cutting prices to 12.60, 50.40, and 112 USD). Check [the live page](https://z.ai/subscribe) before buying; this guide records what sources said, not what the checkout will say tomorrow.

Credits are consumed by tokens, weighted per model: on the current multipliers, GLM-5.3 output counts at 24 and GLM-5.3-Flash output at 8, per ten thousand tokens. The five-hour pool refreshes on a rolling basis and the weekly pool resets every seven days.

## What it plugs into

The selling point is compatibility. Z.ai's documentation names Claude Code, Cline, OpenCode, Kilo Code, and Clawdbot/OpenClaw among supported harnesses, and independent trackers put the count past twenty tools, including ZCode, Cursor, and Zed-adjacent setups. All plans also bundle MCP servers for vision understanding, web search, web reading, and Zread (repository reading).

In September 2026 Z.ai ran a campaign giving paid users unlimited GLM-5.3-Flash through [ZCode](../zcode/index.md) and [AutoClaw](../autoclaw/index.md) overnight (23:00 to 09:00, September 3 to October 7) with doubled quotas elsewhere, which says as much about the company's growth ambitions as any benchmark table.

## ZCode and friends

[ZCode](../zcode/index.md) (zcode.z.ai) is Z.ai's first-party coding harness: a multi-agent coding workbench that reached 7,000+ GitHub stars within weeks of its September 2026 creation and has its own plugin marketplace. It is the natural companion to the plan, though the plan does not require it. The plan's other first-party client, [AutoClaw](../autoclaw/index.md), is covered on its own page. For team purchases, a Team Plan adds seat management, usage analytics, and budget controls.

Mobile and device automation is the other wing: [AutoGLM-Phone-Multilingual](../autoglm/index.md), released in December 2025, executes tasks across 50+ apps via ADB, and the open-source Open-AutoGLM framework has become one of the company's most-starred repositories.

## How to choose

If you already pay for a coding agent and just want stronger models behind it, the coding plan is the shortest path. If you want to build your own product on GLM, skip to the [API platform](../api/index.md): different keys, different limits, metered pricing. And if you are only curious what the models feel like, [chat.z.ai](../chat/index.md) is free.

## Sources

- [GLM Coding Plan overview](https://docs.z.ai/devpack/overview) and [Team Plan](https://docs.z.ai/devpack/teamplan)
- [Z.ai developer docs index](https://docs.z.ai/llms.txt) (tool compatibility list)
- Third-party pricing trackers: [rankllms.com](https://rankllms.com/), [techtrenderyusa.com](https://techtrenderyusa.com/), [zentor.ai](https://zentor.ai/) (prices drift; treat as snapshots)
- GitHub: [zai-org/ZCode](https://github.com/zai-org/ZCode), [zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)
- [GLM-5.3-Flash campaign notice](https://docs.z.ai/devpack/notice/event-glm-5.3-flash)
