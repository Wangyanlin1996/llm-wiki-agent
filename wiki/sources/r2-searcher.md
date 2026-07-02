---
title: "R²-Searcher：校准 Agentic 搜索的检索-推理边界"
type: source
tags: ['semantic-retrieval', 'agentic-retrieval']
sources: [r2-searcher]
source_file: raw/papers/r2-searcher.pdf
last_updated: 2026-07-02
arxiv_id: "2606.28566"
authors: ["Sheng Zhang", "Junyi Li", "Wenlin Zhang", "Xiaowei Qian", "Yichao Wang", "Yingyi Zhang", "Maolin Wang", "Yong Liu", "Xiangyu Zhao"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要
解决搜索 agent 多跳推理中检索-推理边界偏移问题。R²-Searcher 三大创新：(1) query-token 语义引导从检索内容提取精确事实构建细粒度推理上下文；(2) 检索反思机制评估和纠正每步检索后的边界偏差；(3) R²PO 端到端推理-反思引导 RL 算法，通过树探索联合优化两边界。7 个复杂多跳 QA 基准上显著超越 SOTA agentic search 方法。

## 关键贡献
- 检索-推理边界偏移是多跳推理失败主因
- query-token 引导证据建模+检索反思机制
- R²PO RL 算法联合优化检索和推理边界

## 关联
- [[AgenticRetrieval]] — 关联描述
- [[RetrievalAugmentedGeneration]] — 关联描述

## 矛盾
- (暂无)
