---
title: "MOSS: 可审计Agentic记忆架构替代向量相似度搜索"
type: source
tags: [ontology-graph-retrieval]
sources: [moss-auditable-agentic-memory]
source_file: raw/papers/moss-auditable-agentic-memory.pdf
last_updated: 2026-08-17
arxiv_id: "2607.04391"
authors: ["Serge Lacasse", "Jeremie Hatier", "Alex Baker"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

MOSS（Memory-Orchestrated Semantic System）提出一种可审计的 agentic 记忆架构，agent 驱动对结构化关系数据库的检索，替代基于嵌入的相似度搜索。MOSS 是模型无关、存储无关、API 无关的——核心论点是 RAG 的不透明性（opaque by construction）是结构性缺陷，结构化关系存储提供可审计、可追溯的检索。

## 解决的问题

RAG 依赖嵌入相似度搜索，构造上不透明、难以审计，受限于向量表示的理论上限——无法解释为什么检索了某个 chunk，也无法追溯检索决策链。

## 方法与技术

1. **结构化关系数据库**：agent 检索结构化数据而非向量相似度
2. **可审计检索**：每次检索有明确的查询路径和决策链
3. **模型/存储/API 无关**：适配任意 LLM、存储后端和 API
4. **Agent 驱动检索**：agent 主动构造查询而非被动接收嵌入匹配

## 创新点

- 将"不透明"从 RAG 的固有特性重新定义为可解决的结构缺陷
- 结构化关系存储替代嵌入相似度，实现可审计检索
- Agent 主动查询替代被动嵌入匹配

## 关键引用

> "retrieval-augmented generation (RAG), relies on embedding-based similarity search, which is opaque by construction, difficult to audit, and bounded by the theoretical limits of vector representations" — RAG 的结构性缺陷

## 关联

- [[OntologyGraphRetrieval]] — 结构化检索替代向量相似度搜索
- [[worlddb-ontology-aware-memory]] — WorldDB 同为图记忆替代 flat 向量库
- [[AgentMemory]] — Agent 记忆的可审计架构演进
- [[og-rag-ontology-grounded]] — OG-RAG 本体超图检索，MOSS 结构化关系检索
