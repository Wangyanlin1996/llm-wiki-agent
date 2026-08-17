---
title: "KROMA: LLM+RAG增强本体匹配 (Ontology Matching with Knowledge Retrieval)"
type: source
tags: [ontology-graph-retrieval]
sources: [kroma-ontology-matching-rag]
source_file: raw/papers/kroma-ontology-matching-rag.pdf
last_updated: 2026-08-17
arxiv_id: "2507.14032"
authors: ["Lam Nguyen", "Erika Barcelos", "Roger French", "Yinghui Wu"]
year: 2025
venue: "arXiv"
citation_count: 0
---

## 概要

KROMA 提出一种新型本体匹配（Ontology Matching）框架，在 RAG 管线中利用 LLM 动态丰富 OM 任务的结构/词汇/定义知识上下文。为优化性能和效率，KROMA 集成双相似性优化——在保证匹配质量的同时降低计算开销。

## 解决的问题

现有本体匹配系统依赖手工规则或专用模型，适应性有限——无法动态适配不同本体的结构和词汇差异。

## 方法与技术

1. **RAG 管线增强 OM**：动态检索本体结构/词汇/定义知识丰富匹配上下文
2. **LLM 语义匹配**：LLM 利用检索到的本体知识判断概念等价性
3. **双相似性优化**：平衡匹配质量和计算效率
4. **适应性**：无需手工规则或专用模型，适配不同本体

## 创新点

- RAG 管线动态丰富 OM 上下文，替代静态规则
- 双相似性优化解决 OM 的效率-质量权衡
- LLM 语义判断替代结构相似度计算

## 关键引用

> "harnesses Large Language Models (LLMs) within a Retrieval-Augmented Generation (RAG) pipeline to dynamically enrich the semantic context of OM tasks" — RAG 增强本体匹配

## 关联

- [[OntologyGraphRetrieval]] — RAG 管线增强本体匹配检索
- [[ontologyrag-biomedical-code-mapping]] — OntologyRAG 同为本体+RAG，KROMA 专注匹配任务
- [[OntologyMatching]] — 本体匹配任务的 LLM+RAG 增强
- [[open-ontologies-stable-matching]] — 稳定匹配对齐，互补方法
