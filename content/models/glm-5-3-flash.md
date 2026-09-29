---
title: "GLM-5.3-Flash"
description: "Z.ai's natively multimodal workhorse: 320B parameters with 18B active, MIT licensed, and the model behind chat.z.ai."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [glm, glm-5-3, multimodal, open-source]
categories: [models]
---

GLM-5.3-Flash is the first native multimodal model in the GLM-5 series: Z.ai's own description is "frontier intelligence, flash cost." It is the default engine the company puts in front of consumers at chat.z.ai, and it is the model most enterprises will actually integrate.

## An architecture designed for cost

The numbers that matter: 320B total parameters with 18B activated per token, in a hybrid design combining sparse and linear attention. Z.ai calls it the first open-source frontier model to combine the two, and reports that the design cuts attention computation by 3.01x and KV-cache pressure by 4.44x versus GLM-5.3. A "manifold-constrained hyper-connections" (mHC) mechanism rounds out the scaling story, and unlike its flagship sibling, Flash starts from a freshly trained base model.

## What multimodality buys

The vision is not a bolt-on. Flash observes interfaces, rendering results, and interaction feedback, which lets it close the loop across code, browsers, and GUIs. In practice that means frontend and game development it can actually look at, Blender 3D scene work, and real-world device operation through Z.ai's BUA and CUA agent stacks. Beyond coding, it handles office and financial-research workflows end to end, producing finished PPTX, PDF, DOCX, and XLSX files.

## Benchmarks and price

Z.ai says Flash outperforms GLM-5.2 across public benchmarks at one tenth the API price and "approaches Claude Opus 4.8" on coding and agentic tests. The model card records 84.3 on Terminal Bench 2.1 (mini-swe-agent harness, 400K context). API pricing is $0.15 per million input tokens and $0.50 output, with a cached-input rate of $0.03. A faster FlashX tier (200 tokens/second) runs $0.37 / $1.25.

## The alias story

Before launch, a mystery model called "ox-alpha" appeared free on OpenRouter and lit up developer forums; when Z.ai revealed GLM-5.3-Flash days later, the community connected the dots, and the free run was widely read as a deliberate taste test. The model is MIT licensed, which makes it the most permissive frontier-class option in the current lineup.

## Where you meet it

chat.z.ai, by default. The GLM Coding Plan carries it on every tier with three times the quota of the flagship (see [Code on Z.ai](../code/index.md)), and during September and early October 2026 Z.ai ran an unlimited overnight usage campaign for Flash through its ZCode and AutoClaw tools. For API builders it is simply the cheap column in the [pricing table](../api/index.md).

## Sources

- [GLM-5.3-Flash guide](https://docs.z.ai/guides/vlm/glm-5.3-flash) and [release notes, 2026-08-26](https://docs.z.ai/release-notes/new-released)
- [GLM-5.3-Flash model card](https://huggingface.co/zai-org/GLM-5.3-Flash)
- [Z.ai pricing](https://docs.z.ai/guides/overview/pricing)
- Community: OpenRouter "ox-alpha" threads (Reddit r/LocalLLaMA, smol.ai, latent.space, Aug 2026)
