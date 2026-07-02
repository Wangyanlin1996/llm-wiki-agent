---
title: "Ex-GraphRAG：图增强 LLM 的可解释证据路由"
type: source
tags: ['semantic-retrieval', 'graphrag']
sources: [ex-graphrag]
source_file: raw/papers/ex-graphrag.pdf
last_updated: 2026-07-02
arxiv_id: "2605.21994"
authors: ["Yoav Kor Sade", "Arvindh Arun", "Rishi Puri", "Steffen Staab", "Maya Bechler-Speicher"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要
GraphRAG 中 GNN 编码器通过迭代邻域聚合纠缠节点贡献，无法忠实审计结构证据。Ex-GraphRAG 用 Multivariate Graph Neural Additive Network（M-GNAN）替代 GNN，实现编码器输出跨节点和特征组的精确分解。在 STaRK-Prime 上匹配黑盒性能。审计发现语义-结构不匹配：主导编码器输出的节点在检索子图中结构断连，移除低归因中间节点使多跳 QA 降 28%。

## 关键贡献
- M-GNAN 实现编码器输出精确分解替代 GNN
- 审计发现语义-结构不匹配
- 低归因中间节点移除导致 QA -28%

## 关联
- [[GraphRAG]] — 关联描述
- [[RetrievalAugmentedGeneration]] — 关联描述

## 矛盾
- (暂无)
