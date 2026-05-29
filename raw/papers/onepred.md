---
title: "OnePred: Next-Query Prediction via Recursive Intent Memory in Multi-Turn Conversations"
type: paper
tags: [next-query-prediction, recursive-intent-memory, reinforcement-learning, multi-turn, NQP-Bench]
authors: [Jiangwang Chen, Bowen Zhang, Zixin Song]
year: 2026
venue: null
citation_count: null
arxiv_id: "2605.23668"
doi: null
pdf_url: "https://arxiv.org/pdf/2605.23668"
sub_area: intent-recommendation
---

## 概要
提出递归意图记忆作为跨轮上下文机制的两阶段 RL 管线 OnePred：第一阶段教模型预测下一查询，第二阶段教模型压缩冗余 token，token 消耗降低 22×，并附带 NQP-Bench 基准评测 Next-Query Prediction 能力。

## 核心贡献
- 设计递归意图记忆机制，将跨轮对话上下文压缩为意图级表示而非原始 token 序列
- 提出两阶段 RL 管线：先教预测（学习下一查询预测能力），再教压缩（减少冗余 token 消耗降低 22×）
- 构建 NQP-Bench 基准，系统评测多轮对话中的 Next-Query Prediction 能力