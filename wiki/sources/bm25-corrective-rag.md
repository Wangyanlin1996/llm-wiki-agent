---
title: "从 BM25 到 Corrective RAG：文本与表格文档的检索策略基准"
type: source
tags: ['semantic-retrieval', 'hybrid-retrieval']
sources: [bm25-corrective-rag]
source_file: raw/papers/bm25-corrective-rag.pdf
last_updated: 2026-07-02
arxiv_id: "2604.01733"
authors: ["Meftun Akarsu", "Recep Kaan Karaman", "Christopher Mierbach"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要
在金融 QA 基准上系统对比 10 种检索策略（稀疏、稠密、混合融合、交叉编码器重排、查询扩展、索引增强、自适应检索），23,088 query / 7,318 文档。关键发现：(1) 混合检索+神经重排两阶段管线 Recall@5=0.816；(2) BM25 在金融文档上超越 SOTA 稠密检索，挑战语义搜索普遍占优假设；(3) 查询扩展和自适应检索对精确数值查询收益有限。

## 关键贡献
- 混合+重排两阶段管线 Recall@5=0.816
- BM25 在金融文档上超越 SOTA 稠密检索
- 查询扩展对精确数值查询收益有限

## 关联
- [[HybridRetrieval]] — 关联描述
- [[RetrievalEvaluation]] — 关联描述

## 矛盾
- (暂无)
