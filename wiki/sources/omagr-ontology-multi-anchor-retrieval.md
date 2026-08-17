---
title: "OMAGR: 本体引导多锚点图检索框架 (Ontology-Guided Multi-Anchor Graph Retrieval)"
type: source
tags: [ontology-graph-retrieval]
sources: [omagr-ontology-multi-anchor-retrieval]
source_file: raw/papers/omagr-ontology-multi-anchor-retrieval.pdf
last_updated: 2026-08-17
arxiv_id: "2606.11910"
authors: ["Xu Li", "Shuqi Tian", "Xun Han", "Kuncheng Zhao", "Xinyi Li"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

OMAGR 提出本体引导的多锚点图检索框架，解决交通法律责任确定中的多维度检索瓶颈。现有 RAG 方法将复杂法律查询压缩到单一路径，导致跨维度的相互依赖条款被忽略。OMAGR 利用本体结构定义多个检索锚点，在多个法律维度上并行检索，再通过图结构合并结果。

## 解决的问题

法律责任确定需要同时识别跨多个法律维度的相互依赖条款，但单轴 RAG 架构将复杂查询压缩为单一路径，丢失维度间依赖关系。

## 方法与技术

1. **本体引导多锚点**：从法律本体中识别多个检索维度锚点
2. **多维度并行图检索**：每个锚点独立检索，保留维度内结构
3. **图合并**：将多锚点检索结果在图结构中合并，保持跨维度依赖
4. **法律责任确定**：基于合并图推理法律责任归属

## 创新点

- 多锚点图检索打破单轴压缩瓶颈
- 本体结构定义检索维度，确保法律概念完整性
- 图合并保持跨维度依赖关系

## 关键引用

> "single axis architectures compress complex legal queries into a single pathway, causing interdependent statutory dimensions to be overlooked" — 多维度检索瓶颈的根源

## 关联

- [[OntologyGraphRetrieval]] — 本体引导多锚点图检索
- [[og-rag-ontology-grounded]] — OG-RAG 用超图最小集，OMAGR 用多锚点并行
- [[multicube-rag-multihop-qa]] — MultiCube 正交多维本体立方体，类似多维度思路
- [[OntologyIntentAlignment]] — 本体结构化法律意图到可执行条款
