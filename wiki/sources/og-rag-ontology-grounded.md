---
title: "OG-RAG: 本体grounding检索增强生成 (Ontology-Grounded RAG)"
type: source
tags: [ontology-graph-retrieval]
sources: [og-rag-ontology-grounded]
source_file: raw/papers/og-rag-ontology-grounded.pdf
last_updated: 2026-08-17
arxiv_id: "2412.15235"
authors: ["Kartik Sharma", "Peeyush Kumar", "Yunqing Li"]
year: 2024
venue: "arXiv"
citation_count: 0
---

## 概要

OG-RAG 提出一种本体grounding的检索增强生成方法，将领域文档构建为本体超图（ontology hypergraph）表示，每条超边封装一簇基于领域本体grounding的事实知识。检索时通过优化算法选取最小超边集，为 LLM 构造精准且概念grounding的上下文。实验表明 OG-RAG 将准确事实的召回率提升 55%，响应正确率提升 40%，同时加速 30% 的归因和 27% 的事実推理准确率。

## 解决的问题

现有 RAG 方法忽略结构化领域知识，导致上下文生成次优——LLM 难以适配医疗、法律、农业等需要事实推理和预定义流程的专业领域，而微调成本高昂。

## 方法与技术

1. **本体超图构建**：将领域文档按本体实体/关系组织为超图，每条超边封装一组互相关联的事实知识
2. **最小超边集检索**：优化算法选取覆盖查询语义的最小超边集，构建精准上下文
3. **概念grounding**：所有检索结果锚定到本体概念，保留实体间复杂关系
4. **领域无关管线**：适用于任何有预定义规则/流程的事实推理场景

## 创新点

- 超图表示替代 flat chunk，保留实体间多关系结构
- 最小超边集优化算法实现高效且精准的上下文检索
- 本体grounding确保检索结果概念一致，减少幻觉

## 效果

- 准确事实召回率 +55%
- 响应正确率 +40%（4种 LLM 一致）
- 归因速度 +30%，事实推理准确率 +27%

## 关键引用

> "OG-RAG constructs a hypergraph representation of domain documents, where each hyperedge encapsulates clusters of factual knowledge grounded using domain-specific ontology." — 超图表示的核心设计

## 关联

- [[OntologyGraphRetrieval]] — 本体图增强检索的核心方法
- [[RetrievalAugmentedGeneration]] — RAG 范式的本体增强变体
- [[anchor-schema-agnostic-ontology]] — ANCHOR 同样关注输入→本体图映射，OG-RAG 专注检索精度
- [[omd-graphrag]] — OMD-GraphRAG 本体引导提取，互补方向
