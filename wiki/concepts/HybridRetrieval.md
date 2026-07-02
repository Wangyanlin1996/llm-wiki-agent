---
title: "混合检索（Hybrid Retrieval）"
type: concept
tags: ['semantic-retrieval', 'hybrid-retrieval']
sources: ["telco-orag", "bm25-corrective-rag", "hakari-bench"]
last_updated: 2026-07-02
---

混合检索结合稀疏检索（BM25/词法）和稠密检索（神经网络），关键挑战是融合策略。在金融文档上 BM25 超越 SOTA 稠密检索，挑战语义搜索普遍占优假设（[[bm25-corrective-rag]]）。混合检索+神经重排两阶段管线在文本+表格文档上 Recall@5=0.816（[[bm25-corrective-rag]]）。电信场景中 3GPP 领域检索+Web 混合+神经路由实现 45% 内存节省（[[telco-orag]]）。HAKARI-Bench 提供五族检索模型统一对比框架（[[hakari-bench]]）。相关论文：[[telco-orag]]、[[bm25-corrective-rag]]、[[hakari-bench]]
