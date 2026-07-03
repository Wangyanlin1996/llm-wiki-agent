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

GraphRAG 用消息传递 GNN 编码从知识图谱检索的子图，但由于 GNN 通过迭代邻域聚合纠缠节点贡献，编码器输出无法做逐节点闭式分解，因此无法忠实审计哪些结构证据真正到达了模型。事后可解释方法（GNNExplainer、SubgraphX、GAT 注意力）仅提供近似，其忠实性无法保证，且注意力权重与因果影响特征相关性差。本文提出 **Ex-GraphRAG**：用 **M-GNAN**（Multivariate Graph Neural Additive Network）替代 GNN 编码器——将 GNAN 的加性分解从逐特征扩展到特征组，适配 GraphRAG 中高维嵌入向量（单个维度无独立语义）。M-GNAN 的重要性分数是编码器输出的精确偏和而非事后近似。在 STaRK-Prime 上该可审计编码器匹配黑盒性能。利用它审计证据路由，发现**语义-结构不匹配**：主导编码器输出的节点在检索子图中结构断连，仅靠低归因中间节点（药物类别、通路标识、共享蛋白家族）作为结构桥梁连接——移除这些桥梁使多跳 QA 降级高达 28%。该不匹配对任何不透明编码器不可见，对检索剪枝、上下文构造和故障诊断有直接意义。

## 关键贡献

- **M-GNAN 内在可分解编码器**：将 GNAN 加性分解扩展到特征组嵌入，使逐节点重要性成为编码器输出的精确偏和而非事后近似，集成进 G-Retriever 框架
- **语义-结构不匹配的发现**：审计揭示主导编码器输出的节点结构断连，低归因中间节点充当桥梁——移除桥梁使多跳 QA 降 28%，该不匹配对不透明编码器不可见
- **可审计编码器的新能力**：在 STaRK-Prime 匹配黑盒性能的同时启用检索调试、重要性引导的上下文构造、多粒度归因

## 关键引用

> "The nodes that dominate the encoder's output are structurally disconnected in the retrieved subgraph, held together by low-attribution intermediaries whose removal degrades multi-hop QA by up to 28%."

## 关联

- [[GraphRAG]] — 本文是该概念的可解释性核心贡献，首次使 GraphRAG 的 GNN 编码器内在可审计
- [[RetrievalAugmentedGeneration]] — 审计能力为 GraphRAG 的检索剪枝、上下文构造和故障诊断提供精确归因
- [[AgentExplainability]] — 内在可分解编码器为图增强 LLM 提供忠实（非近似）的归因，呼应 agent 可解释性需求

## 矛盾

无已知矛盾。语义-结构不匹配的发现挑战了"语义重要性高的节点在检索子图中也结构连通"的隐含假设。
