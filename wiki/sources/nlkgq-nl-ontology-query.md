---
title: "NLKGQ: OWL本体零样本LLM结构化查询生成 (NL to Ontology Query)"
type: source
tags: [ontology-graph-retrieval]
sources: [nlkgq-nl-ontology-query]
source_file: raw/papers/nlkgq-nl-ontology-query.pdf
last_updated: 2026-08-17
arxiv_id: "2607.18029"
authors: ["Blake G. Fitch", "Cato Elia Kurtz"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

NLKGQ（Natural Language Knowledge Graph Query）证明当领域词汇和语义被 OWL 本体良好捕获时，LLM 可以零样本生成准确的结构化查询——无需微调、检索增强或多 agent 编排。本文展示了本体 schema 作为 LLM 查询生成的语义锚点的价值。

## 解决的问题

研究者需要回答关于领域特定档案内容的临时问题，但缺乏编写结构化查询（SPARQL 等）的专业知识。

## 方法与技术

1. **OWL 本体语义捕获**：领域词汇和语义用 OWL 本体定义
2. **零样本 LLM 查询生成**：LLM 直接从 NL 生成结构化查询，无需微调
3. **本体 schema 锚定**：本体作为 LLM 的语义上下文，约束查询生成
4. **可重用框架**：适用于任何有 OWL 本体的领域

## 创新点

- 证明本体 schema 足以让 LLM 零样本生成准确结构化查询
- 无需微调/RAG/多agent，降低部署复杂度
- 本体作为"语义契约"连接 NL 和结构化查询

## 关键引用

> "when domain vocabulary and semantics are captured in a well-designed Web Ontology Language (OWL) ontology, Large Language Models (LLMs) can generate accurate structured queries zero-shot" — 核心论点

## 关联

- [[OntologyGraphRetrieval]] — 本体 schema 锚定 NL→结构化查询
- [[researcher-agents-kgqa]] — Researcher Agents 同为 NL→SPARQL，NLKGQ 零样本
- [[obda-query-abstraction]] — OBDA 查询抽象，互补方向
- [[OntologySemanticLayer]] — 本体作为语义接口层
