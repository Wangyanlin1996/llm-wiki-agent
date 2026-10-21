---
title: "Chain-of-Agents：多智能体协作处理长上下文任务"
type: source
tags: [multi-agent-long-context]
sources: [chain-of-agents]
source_file: raw/papers/chain-of-agents.pdf
last_updated: 2026-07-24
arxiv_id: "2406.02818"
authors: ["Yusen Zhang", "Ruoxi Sun", "Yanfei Chen", "Tomas Pfister", "Rui Zhang", "Sercan Ö. Arik"]
year: 2024
venue: "Neural Information Processing Systems"
citation_count: 261
doi: "10.48550/arXiv.2406.02818"
---

## 概要
Chain-of-Agents (CoA) 是一种利用多智能体协作处理长上下文任务的开创性框架。它由多个 worker agent 顺序处理文本分段，再由 manager agent 综合所有贡献。CoA 通过交错阅读与推理（interleave reading & reasoning）处理完整输入，同时通过为每个 agent 分配短上下文来缓解长上下文聚焦问题。在 QA、摘要和代码补全等长上下文任务上比 RAG、Full-Context 和多智能体 LLM 基线提升达 10%。

## 关键贡献
- 提出 Chain-of-Agents 框架：worker agents 顺序处理文本分段 → manager agent 综合输出
- 通过 interleaving reading and reasoning 实现完整输入处理，同时保持每个 agent 短上下文
- 在 QA、摘要、代码补全任务上比 RAG/Full-Context/多智能体基线提升达 10%

## 关键引用
> "CoA processes the entire input by interleaving reading and reasoning, and it mitigates long context focus issues by assigning each agent a short context."

## 关联
- [[GraphOfAgents]] — GoA 用信息论形式化 CoA 的压缩目标
- [[LSTMMAS]] — LSTM-MAS 受 CoA 启发，引入门控机制改进
- [[COSMIR]] — COSMIR 用结构化记忆替代 CoA 的自由文本传递

## 矛盾
- (暂无)
