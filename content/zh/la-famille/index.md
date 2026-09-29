---
title: "本站引擎 la-famille"
description: "生成本手册的 Go 静态站点生成器：它能做什么、从哪里获取、本站为什么选择它。"
author: "Z.ai Field Guide"
date: "2026-09-29"
tags: [la-famille, static-sites, go]
categories: [meta]
layout: "layout-zai-zh"
---

你正在阅读的每一页，都由 **la-famille** 生成——一个用 Go 编写的静态站点生成器。本小节诚实地记录这个工具：它能做什么、本站如何使用它，以及它还没有做什么。

## la-famille 是什么

一个单一的 Go 程序，把一个 Markdown 文件夹变成完整的静态站点：HTML 页面、分类归档、客户端搜索索引、链接图谱、RSS、站点地图、缺失链接的占位页（stub），以及面向大模型工具链的机器可读语料导出。它自带终端界面、增量构建缓存、内容检查器与发布产物校验器。它按设计就是本地优先：无框架、无 CDN、所有资源自托管。

用它自己的话说，设计宗旨是「把内容当作一张带链接的、机器可读的知识图谱」，而不是给博客引擎外挂一个图谱功能。

## 本站为什么用它

本手册是这个生成器第一次在自身文档之外的完整生产实践——一个刻意的测试：真实的目的地、两种语言、一套自定义主题。约束正是重点：

- **没有 i18n 框架的双语**。两棵内容树、镜像的路径、按语言区分的布局文件，以及主题层的语言切换（细节见[本站如何构建](how-this-site-works.md)）。
- **主题而非分叉**。「zai」主题完全位于本站的 `templates/` 与 `assets/` 目录；生成器本体未被修改，明暗模式、首屏与全部组件都是主题文件。
- **默认机器可读**。整份语料以面向语言模型设计的格式导出，链接见每页底部。

## 从哪里获取

项目在 [github.com/drawmeanelephant/la-famille](https://github.com/drawmeanelephant/la-famille) 开源，快速上手只需单文件：下载发布包、指向项目目录、构建。仓库的 `docs/` 目录有深入指南；本小节则是使用后的实地报告。

## 本小节其它页面

- [本站如何构建](how-this-site-works.md)：能力清单，附可直接打开的线上产物链接。
- [版本说明](colophon.md)：致谢、字体、来源政策与许可说明。
- [原始语料样例](raw-sample.md)：一个刻意保持原样提供的 Markdown 文件。

## 来源

- [la-famille 仓库](https://github.com/drawmeanelephant/la-famille)（README 与功能文档）
- 对随本站发布的构建产物的直接检查（2026-09-29）
