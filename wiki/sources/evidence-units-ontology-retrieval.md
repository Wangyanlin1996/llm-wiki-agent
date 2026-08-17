---
title: "Evidence Units: 本体grounding文档组织实现解析器无关检索"
type: source
tags: [ontology-graph-retrieval]
sources: [evidence-units-ontology-retrieval]
source_file: raw/papers/evidence-units-ontology-retrieval.pdf
last_updated: 2026-08-17
arxiv_id: "2604.00500"
authors: ["Yeonjee Han"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

本文提出 Evidence Units（EU），一种解析器无关的流水线，将结构化文档（表格+标题、图+说明、方程+解释段落）组织为语义完整的文档块，而非将每个解析元素作为独立 chunk。EU 通过本体grounding将视觉资产与其上下文文本组合为语义凝聚单元，修复了元素级索引导致的语义碎片化问题。

## 解决的问题

结构化文档在检索时被碎片化——表格与标题分离、图与说明分离、方程与解释段落分离。元素级索引将每个解析元素视为独立 chunk，散落语义凝聚单元，导致检索精度下降。

## 方法与技术

1. **Evidence Unit 构建**：将视觉资产（表格/图/方程）与其上下文文本组合为语义完整单元
2. **本体grounding**：用本体类型/关系标注 EU，确保检索时概念一致性
3. **解析器无关**：不依赖特定文档解析器，适配多种文档格式
4. **上下文保持**：EU 内部保留结构关系，外部检索时作为原子单元

## 创新点

- 从"元素级索引"到"语义完整单元"的范式转变
- 本体grounding确保 EU 的概念一致性
- 解析器无关设计增强跨文档格式鲁棒性

## 关键引用

> "Element-level indexing treats every parsed element as an independent chunk, scattering semantically cohesive units across separate retrieval candidates." — 指出碎片化问题的根源

## 关联

- [[OntologyGraphRetrieval]] — 本体grounding文档组织用于精准检索
- [[og-rag-ontology-grounded]] — OG-RAG 同样用本体结构化检索，EU 专注文档组织层
- [[RetrievalEvaluation]] — EU 改善检索精度评估维度
