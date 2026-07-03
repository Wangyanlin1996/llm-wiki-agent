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

RAG 系统的生成质量严重依赖检索质量，但混合文本和表格的异构文档上缺乏现代检索方法的系统对比。本工作在金融 QA 基准 T2-RAGBench 上系统评测 10 种检索策略（23,088 query / 7,318 文档），覆盖稀疏（BM25）、稠密（text-embedding-3-large）、混合融合（RRF）、交叉编码器重排（Cohere Rerank v4.0 Pro）、查询扩展（HyDE、Multi-Query）、索引增强（Contextual Retrieval）和自适应检索（CRAG）。关键发现：(1) 混合检索+神经重排两阶段管线 Recall@5=0.816、MRR@3=0.605，大幅超越所有单阶段方法（混合 RRF 0.695、BM25 0.644、稠密 0.587）；(2) BM25 在金融文档上超越 SOTA 稠密检索，挑战语义搜索普遍占优假设——精确术语（公司名、指标标签、财年）提供强检索信号而语义嵌入可能稀释；(3) 查询扩展（HyDE）甚至低于原始稠密检索（0.544 vs 0.587），因 LLM 生成的假设文档幻觉了似是但错误的金融数字；(4) Contextual Retrieval 一致改善稠密（+2.8pp）和混合（+2.2pp）；(5) CRAG 63% 查询触发纠正路径但仍不及简单混合融合。消融研究覆盖融合方法（CC α=0.5 最优）和重排器深度（50 候选最优）。

## 关键贡献

- **混合+重排两阶段管线 Recall@5=0.816**：系统证明两阶段管线（混合 RRF 检索 50 候选 → 交叉编码器重排 top-10）大幅超越单阶段——为异构文档 RAG 提供最优实践
- **BM25 超越 SOTA 稠密检索的实证**：在金融文档上 BM25 全指标超越 text-embedding-3-large——挑战语义搜索普遍占优假设，揭示精确术语匹配在领域文档上的优势
- **查询扩展对精确数值查询的负收益**：HyDE 因幻觉金融数字降低检索质量，Multi-Query 因查询已充分具体化而收益可忽略——为查询扩展的适用边界提供实证
- **可操作的成本-精度建议**：融合方法（CC α=0.5 或 RRF k=10）、重排器深度（50 候选最优）、Contextual Retrieval 一致增益——为实践者提供具体配置指南

## 关键引用

> "BM25 outperforms state-of-the-art dense retrieval on financial documents, challenging the common assumption that semantic search universally dominates."

> "Financial questions require precise numerical reasoning; LLM-generated hypothetical documents introduce noise by hallucinating plausible but incorrect financial figures, pulling the embedding away from the true relevant context."

## 关联

- [[HybridRetrieval]] — 本文是该概念的核心实证研究，系统证明混合检索+重排在异构文档上的优势
- [[RetrievalEvaluation]] — 多维评估（Recall@k/MRR/nDCG/MAP + Number Match + 配对 bootstrap 显著性检验）为检索评估提供方法论标杆
- [[telco-orag]] — 两者均为混合检索实践：本文金融文档场景揭示 BM25 优势，后者电信场景揭示领域检索+Web 混合优势
- [[hakari-bench]] — 后者提供五族检索模型统一对比框架，本文的 10 策略对比为特定文档类型的实践选择提供证据
- [[scaling-dense-retrieval]] — 本文证实词法系统与 ANN 嵌入模型的分歧（BM25 超越稠密），后者利用这种分歧作为训练信号

## 矛盾

与"语义搜索普遍优于词法搜索"的流行假设直接矛盾——在金融文档（精确术语密集）上 BM25 全指标超越 SOTA 稠密检索，统计显著（p<0.001 配对 bootstrap 检验）。
