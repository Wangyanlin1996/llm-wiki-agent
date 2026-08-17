---
title: "OntologyRAG: 本体知识图谱+RAG实现生物医学代码映射"
type: source
tags: [ontology-graph-retrieval]
sources: [ontologyrag-biomedical-code-mapping]
source_file: raw/papers/ontologyrag-biomedical-code-mapping.pdf
last_updated: 2026-08-17
arxiv_id: "2502.18992"
authors: ["Hui Feng", "Yuntzu Yin", "Emiliano Reynares", "Jay Nanavati"]
year: 2025
venue: "arXiv"
citation_count: 0
---

## 概要

OntologyRAG 利用生物医学本体知识图谱增强 RAG，实现更快更好的生物医学代码映射——识别不同本体间概念的相似性或等价性。相比传统的本体领域微调语言模型方法，OntologyRAG 用 RAG 管线动态检索本体 KG 中的概念定义和关系，降低对领域特定微调的依赖。

## 解决的问题

生物医学代码映射需要识别不同本体间概念的等价/相似关系，传统方法依赖昂贵的领域微调语言模型，且映射质量不稳定。

## 方法与技术

1. **本体 KG 构建**：将生物医学本体（概念+关系）构建为知识图谱
2. **RAG 检索管线**：查询概念时动态检索本体 KG 中的定义/关系/层次
3. **概念等价检索**：基于本体结构语义判断跨本体概念等价性
4. **更快更好**：避免微调成本，同时提升映射质量和速度

## 创新点

- 用 RAG 管线替代本体领域微调，降低部署成本
- 本体 KG 结构语义增强概念等价判断精度
- 动态检索替代静态嵌入，适配本体更新

## 关键引用

> "Biomedical code mapping identifies similarity or equivalence between concepts from different ontologies" — 代码映射的核心任务定义

## 关联

- [[OntologyGraphRetrieval]] — 本体 KG 增强代码映射检索
- [[og-rag-ontology-grounded]] — OG-RAG 通用本体超图，OntologyRAG 专注本体间映射
- [[OntologyMatching]] — 本体匹配任务的 RAG 增强
- [[kroma-ontology-matching-rag]] — KROMA 同为本体匹配+RAG
