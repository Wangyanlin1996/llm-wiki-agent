---
title: "Telco-oRAG：面向电信查询的混合检索与神经路由 RAG 优化"
type: source
tags: ['semantic-retrieval', 'hybrid-retrieval', 'telecom']
sources: [telco-orag]
source_file: raw/papers/telco-orag.pdf
last_updated: 2026-07-02
arxiv_id: "2505.11856"
authors: ["Andrei-Laurentiu Bornea", "Fadhel Ayed", "Antonio De Domenico", "Nicola Piovesan", "Tareq Si Salem", "Ali Maatouk"]
year: 2025
venue: "arXiv"
citation_count: pending
---

## 概要
面向 3GPP 标准的电信 RAG 框架。引入混合检索策略：3GPP 领域专用检索 + Web 搜索，配合术语增强查询精炼和神经路由器实现内存高效检索。3GPP 相关问题准确率提升 17.6%，词表查询提升 10.6%，内存使用降低 45%。使开源 LLM 在电信基准上达到 GPT-4 水平。与 wiki 的 [[IntentDrivenMnS]] 生态完全契合。

## 关键贡献
- 3GPP 领域检索+Web 混合检索策略
- 神经路由器实现 45% 内存节省
- 开源 LLM 达 GPT-4 电信准确率

## 关联
- [[HybridRetrieval]] — 关联描述
- [[RetrievalAugmentedGeneration]] — 关联描述
- [[IntentDrivenMnS]] — 关联描述

## 矛盾
- (暂无)
