---
title: "WorldDB: 本体感知写入时协调的向量图世界记忆引擎"
type: source
tags: [ontology-graph-retrieval]
sources: [worlddb-ontology-aware-memory]
source_file: raw/papers/worlddb-ontology-aware-memory.pdf
last_updated: 2026-08-17
arxiv_id: "2604.18478"
authors: ["Harish Santhanalakshmi Ganesan"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

WorldDB 提出一种向量图世界记忆引擎，通过本体感知的写入时协调解决 flat 向量库的碎片化问题。相比 Graphiti、Memento、Hydra DB 等双时态知识图谱系统，WorldDB 增加了递归组合、节点内容寻址不变量和本体感知协调——在写入时而非读取时解决矛盾和替代关系。

## 解决的问题

RAG over flat 向量库将事实碎片化为 chunk，丢失跨会话身份、无替代/矛盾概念。现有双时态 KG 系统的图仍然是 flat 的——无递归组合、无节点内容寻址不变量。

## 方法与技术

1. **向量图世界**：将记忆表示为递归可组合的图结构，而非 flat chunk
2. **本体感知写入时协调**：写入时用本体类型/关系约束解决矛盾和替代
3. **内容寻址不变量**：节点内容寻址确保一致性
4. **双时态 + 本体**：结合双时态元数据（有效时间）和本体类型约束

## 创新点

- 从"读取时过滤"到"写入时协调"的范式转变
- 递归图组合替代 flat chunk，保留事实间结构关系
- 本体感知协调在写入时解决矛盾/替代

## 关键引用

> "RAG over flat vector stores fragments facts into chunks, loses cross-session identity, and has no first-class notion of supersession or contradiction" — flat 向量库的根本缺陷

## 关联

- [[OntologyGraphRetrieval]] — 本体感知图结构替代 flat 向量库
- [[og-rag-ontology-grounded]] — OG-RAG 超图检索，WorldDB 图世界记忆引擎
- [[moss-auditable-agentic-memory]] — MOSS 同为可审计记忆替代向量搜索
- [[AgentMemory]] — Agent 记忆架构的本体感知演进
