---
title: "OBDA查询抽象: 本体数据访问中的最小完备与最大可靠抽象"
type: source
tags: [ontology-reasoning, semantic-layer]
sources: [obda-query-abstraction]
source_file: raw/papers/obda-query-abstraction.pdf
last_updated: 2026-07-25
arxiv_id: "2606.24618"
authors: ["Michel Leclère", "Marie-Laure Mugnier", "Guillaume Pérution-Kihli"]
year: 2025
venue: "KR 2025"
citation_count: 0
doi: "10.24963/kr.2025/43"
---

## 概要
在本体数据访问（OBDA）中，多个数据源通过映射集成到本体。本文研究查询抽象问题：将数据查询翻译到本体层。由于完美抽象可能不存在，先前工作引入了最小完备抽象和最大可靠抽象的概念。本文在带有限不等式和标记数据库常数的 UCQ 扩展中研究抽象，该扩展不增加感兴趣问题的复杂度，但能表达最小完备抽象，因此在完美抽象存在时也能表达。

## 关键贡献
- 在带不等式扩展的 UCQ 中形式化查询抽象问题
- 证明该扩展不增加复杂度但能表达最小完备抽象
- 通过与数据交换中 maximum recovery 的新联系刻画最大可靠抽象
- KR 2025 发表

## 关键引用
> "While this extension does not lead to an increased complexity of the problems of interest, it is able to express minimally complete abstractions, hence perfect abstractions when they exist."

## 关联
- [[OntologyReasoning]] — 本体推理核心方法
- [[OntologySemanticLayer]] — 本体语义层
- [[kg-gap-overlap-benchmark]] — KG任务就绪性基准

## 矛盾
- 无
