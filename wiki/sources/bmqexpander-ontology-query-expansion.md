---
title: "BMQExpander: UMLS本体知识+LLM查询扩展增强生物医学文档检索"
type: source
tags: [ontology-graph-retrieval]
sources: [bmqexpander-ontology-query-expansion]
source_file: raw/papers/bmqexpander-ontology-query-expansion.pdf
last_updated: 2026-08-17
arxiv_id: "2508.11784"
authors: ["Zabir Al Nazi", "Vagelis Hristidis", "Aaron Lawson McLean", "Jannat Ara Meem", "Md Taukir Azam Chowdhury"]
year: 2025
venue: "arXiv"
citation_count: 0
---

## 概要

BMQExpander 提出一种本体感知的查询扩展管线，将 UMLS Metathesaurus 中的医学知识（定义和关系）与 LLM 的生成能力结合，增强生物医学文档检索。系统利用本体层次结构和语义关系扩展用户查询，解决领域特定词汇和语义歧义导致的检索精度问题。

## 解决的问题

生物医学文档 QA 的检索阶段因领域特定词汇和用户查询中的语义歧义而充满挑战——用户查询与文档术语不匹配导致召回率低。

## 方法与技术

1. **UMLS 本体知识注入**：从 UMLS Metathesaurus 提取概念定义和关系
2. **LLM 查询扩展**：LLM 利用本体知识生成扩展查询术语
3. **本体层次利用**：利用 is-a 层次结构扩展/窄化查询语义
4. **检索增强**：扩展查询提升生物医学文档检索召回和精度

## 创新点

- 本体知识（定义+关系）+ LLM 生成能力的协同查询扩展
- 利用 UMLS 层次结构进行语义扩展/窄化
- 领域特定词汇不匹配的系统性解决

## 关键引用

> "combines medical knowledge - definitions and relationships - from the UMLS Metathesaurus with the generative capabilities of large language models (LLMs) to enhance retrieval effectiveness" — 本体知识+LLM 协同

## 关联

- [[OntologyGraphRetrieval]] — 本体层次结构增强查询扩展
- [[hyem-hyperbolic-ontology-retrieval]] — HyEm 同为生物医学本体检索，BMQExpander 专注查询扩展
- [[ontologyrag-biomedical-code-mapping]] — OntologyRAG 同为生物医学本体+RAG
- [[HybridRetrieval]] — 查询扩展增强混合检索
