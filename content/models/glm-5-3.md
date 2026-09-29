---
title: "GLM-5.3"
description: "The August 2026 flagship: a post-training-only upgrade over GLM-5.2, a coding leap, and an unexpected cybersecurity story."
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [glm, glm-5-3, coding, benchmarks]
categories: [models]
---

GLM-5.3 is Z.ai's flagship model, released in August 2026. It is unusual for what it is not: there is no new base model underneath. Z.ai states plainly that GLM-5.3 uses the same base as [GLM-5.2](glm-5-family.md) and that every improvement comes from post-training.

## What changed

- **Coding.** On Z.ai's in-house Z.ai Code Bench, GLM-5.3 reports a 50 percent gain over GLM-5.2. On public suites, the company claims state-of-the-art results among open-weight models, naming Terminal Bench 3.0 and Agents' Last Exam (CLI).
- **Cybersecurity, unexpectedly.** As post-training scaled, so did abilities nobody optimized for. Z.ai reports that GLM-5.3 is the best model to date on the CyberGym vulnerability-discovery benchmark, that its advantage grows deeper into exploitation chains, and that in collaboration with security teams it was tested on real targets, surfacing 2,436 vulnerabilities including 1,097 of medium or high severity. The company also claims it matches "Mythos 5" in white-box code review, a comparison covered critically by trade press.

## The spec sheet

| | |
|---|---|
| Inputs | Text only |
| Context | 1,000,000 tokens |
| Max output | 128,000 tokens |
| Reasoning | Always on, `low` / `high` / `max` effort (disabling is no longer supported) |
| API price | $1.40 in / $0.26 cached / $4.40 out per 1M tokens |
| Weights | Published, under a custom license (not MIT) |

The reasoning change is a real migration constraint: applications that used `thinking.type: "disabled"` must switch to `enabled` with `low` effort, or requests will fail.

## The licensing turn

Through GLM-5.2 the series shipped under MIT, and the model card called it "pure open: no regional limits." GLM-5.3's weights landed under a custom "glm-5.3" license instead. Community coverage reported that providers above a revenue threshold now need a security review before use; the precise terms belong to the license text, not to this guide. The practical reading: if your compliance process assumes MIT, verify before you deploy. Note also that its sibling [GLM-5.3-Flash](glm-5-3-flash.md) stayed MIT, so "open" now depends on which model you pick.

## Should you care about 5.3 or 5.3-Flash?

Read them as a pair. GLM-5.3 is the capability ceiling for text and a cost structure three to nine times heavier than Flash; GLM-5.3-Flash is multimodal, MIT, and cheap. For most interactive products the Flash is the better default; reach for 5.3 when coding or long-horizon planning quality justifies the price.

## Sources

- [Release notes, 2026-08-18](https://docs.z.ai/release-notes/new-released) and [GLM-5.3 guide](https://docs.z.ai/guides/llm/glm-5.3)
- [GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3) (license field, evaluation results)
- [Artificial Intelligence News analysis, 2026-08-18](https://www.artificialintelligence-news.com/news/zhipu-glm-5-3-benchmarks-explained/)
- [SemiAnalysis inference coverage](https://inferencex.semianalysis.com/model/glm-5-3) (post-training-only, Yicai date)
- Community license discussion: The New Stack post (Aug 2026), ThursdAI roundups
