---
title: "本站如何构建"
description: "la-famille 能力实地巡览：分类归档、知识图谱、搜索、RAG 导出与双语主题，附线上链接。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [la-famille, i18n, static-sites]
categories: [meta]
layout: "layout-zai-zh"
---

本页是能力清单，每一项都对应一个你现在就能打开的产物。以下全部由 la-famille 从纯 Markdown 生成，没有任何手工维护的 HTML。

## 能力清单（附线上链接）

| 能力 | 在哪里看 |
|------|----------|
| 分类归档（由 frontmatter 中的 tags 与 categories 生成） | <a href="/tags/">/tags/</a> 与 <a href="/categories/">/categories/</a> |
| 交互式知识图谱浏览器（搜索、过滤、聚焦模式、深链） | <a href="/graph/">/graph/</a> |
| 客户端即时搜索（任意页面按 `/`，或使用顶栏搜索框） | 就在本页试试 |
| 带日期的页面 RSS | <a href="/feed.xml">/feed.xml</a> |
| 站点地图与爬虫规则 | <a href="/sitemap.xml">/sitemap.xml</a>、<a href="/robots.txt">/robots.txt</a> |
| 面向大模型的机器可读语料导出 | <a href="/rag-archive/rag-content.md">/rag-archive/rag-content.md</a> |
| 原始 Markdown 直出（`render: false`） | [原始样例](raw-sample.md) |

## 双语是组合出来的，不是框架给的

la-famille 没有内置国际化。本站用生成器自己的原语实现双语：两棵内容树（`content/` 英文、`content/zh/` 中文）、镜像路径；按页面覆盖布局，让中文页加载 `layout-zai-zh.html`，把 `lang="zh-CN"` 直接写进静态 HTML；一小段主题脚本把当前路径映射到对应语言（`/models/` 可以切到 `/zh/models/`）。构建期没有机器翻译，阅读任何页面都不需要 JavaScript。

两条来自实践的诚实备注。第一，生成器的分类规范化只接受拉丁字符，中文词条会被静默丢弃；因此本站两种语言共用一套拉丁标签词表，主题负责把可见的「Tags」标签替换为「标签」。第二，由于模板无法感知页面 URL，首页的 Hero 区域表达为一个单独布局文件，通过 frontmatter 选择——功能完全符合设计，但知道这个原因本身有价值。

## 主题

完整定制的「zai」主题：纸与墨的浅色模式、带专属配图的深色模式、单一朱红强调色、全直角、自托管字体（General Sans 与 JetBrains Mono，许可随附，见[版本说明](colophon.md)）。明暗可在顶栏切换并跨访问记忆；选择在首次绘制前应用，因此没有闪烁。中文使用系统 CJK 字体以控制页面体积。

<figure class="figure">
  <img src="/assets/img/graph-c.webp" alt="抽象的节点与连线图案">
  <figcaption>本站内置三幅生成图像；这一幅对应知识图谱的叙事。</figcaption>
</figure>

## 构建数字

生成本页的那次构建的快照：完整站点在笔记本电脑上不到一秒完成编译，从源码到 50 多个输出文件，覆盖两种语言、图谱浏览器、分类归档与语料导出。重建是增量的：未变化的页面复用内容寻址缓存。校验内建于流水线：内容检查器负责 frontmatter、链接与孤立页；发布检查会在引用无法解析时失败，而占位页（stub）仅作为警告保留。

## 这份演示证明了什么

本站要检验的命题：一个专注的 Go 生成器，只在主题层做扩展，就能承载一个真实的双语目的地——不用 JavaScript 框架、不依赖外部资源，生成器本身甚至不知道中文和这套主题的存在。以这次构建的证据看，命题成立。

## 来源

- 对本站构建输出与配置的直接检查（2026-09-29）
- [la-famille 仓库](https://github.com/drawmeanelephant/la-famille)
