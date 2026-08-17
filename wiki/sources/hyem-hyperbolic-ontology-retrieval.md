---
title: "HyEm: 双曲空间本体层次感知查询自适应检索 (Hyperbolic Ontology Retrieval)"
type: source
tags: [ontology-graph-retrieval]
sources: [hyem-hyperbolic-ontology-retrieval]
source_file: raw/papers/hyem-hyperbolic-ontology-retrieval.pdf
last_updated: 2026-08-17
arxiv_id: "2604.09550"
authors: ["Ou Deng", "Shoji Nishimura", "Atsushi Ogihara", "Qun Jin"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

HyEm 解决生物医学 RAG 中的本体层次感知grounding挑战：HPO、DO、MeSH 等资源使用深层 is-a 分类层次，但生产系统依赖欧式嵌入和 ANN 索引。HyEm 是一个轻量检索框架，用双曲嵌入编码本体层次结构，同时通过查询自适应机制在双曲/欧式检索间切换——层次相关查询用双曲，实体中心查询用欧式。

## 解决的问题

双曲嵌入适合层次表示但面临两大障碍：(1) 缺乏原生向量数据库支持；(2) 在实体中心查询（层次无关）上表现不佳。现有系统无法兼顾层次感知和实体中心检索。

## 方法与技术

1. **双曲嵌入编码本体层次**：将 is-a 分类树嵌入双曲空间，保持层次距离
2. **欧式向量索引**：用欧式 ANN 索引近似双曲距离，绕过向量库原生支持缺失
3. **查询自适应切换**：根据查询类型动态选择双曲（层次相关）或欧式（实体中心）检索
4. **轻量设计**：无需重训嵌入模型，作为插件增强现有 RAG 管线

## 创新点

- 查询自适应机制解决双曲嵌入"一刀切"问题
- 欧式索引近似双曲距离绕过向量库限制
- 层次感知grounding提升生物医学本体检索精度

## 关键引用

> "resources like HPO, DO, and MeSH use deep is-a taxonomies, yet production stacks rely on Euclidean embeddings and ANN indexes" — 指出现有系统与本体结构的失配

## 关联

- [[OntologyGraphRetrieval]] — 本体层次结构编码增强检索精度
- [[EmbeddingModels]] — 双曲嵌入作为欧式嵌入的层次感知替代
- [[og-rag-ontology-grounded]] — OG-RAG 用超图，HyEm 用双曲空间编码层次
- [[qime-ontology-embeddings]] — QIME 本体驱动嵌入，互补方向
