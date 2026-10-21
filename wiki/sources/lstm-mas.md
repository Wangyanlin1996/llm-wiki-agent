---
title: "LSTM-MAS：受 LSTM 启发的长上下文理解多智能体系统"
type: source
tags: [multi-agent-long-context]
sources: [lstm-mas]
source_file: raw/papers/lstm-mas.pdf
last_updated: 2026-07-24
arxiv_id: "2601.11913"
authors: ["Yichen Jiang", "Peng Ye", "Jiakang Yuan", "Chongjun Tu", "Lei Bai", "Tao Chen"]
year: 2026
venue: "arXiv.org"
citation_count: 1
doi: "10.48550/arXiv.2601.11913"
---

## 概要
LSTM-MAS 从 LSTM 架构汲取灵感，设计了一种链式多智能体系统来处理长上下文。每个节点包含 worker agent（分段理解）、filter agent（冗余减少）、judge agent（连续错误检测）和 manager agent（全局信息传播与保留），分别对应 LSTM 的输入门、遗忘门、恒定误差传送带和输出门。这种设计实现了跨文本段落的受控信息传输和选择性长期依赖建模。相比 CoA，在 NarrativeQA 提升 97.97%，Qasper 提升 65.75%，HotpotQA 提升 122.19%。

## 关键贡献
- 将 LSTM 门控机制映射到多智能体架构：worker=input gate, filter=forget gate, judge=CEC, manager=output gate
- 受控信息传输 + 选择性长期依赖建模，有效避免错误累积和幻觉传播
- 在 5 个长上下文基准上相比 CoA 提升 10.80%-122.19%

## 关键引用
> "LSTM-MAS organizes agents in a chained architecture, where each node comprises a worker agent for segment-level comprehension, a filter agent for redundancy reduction, a judge agent for continuous error detection, and a manager agent for globally regulates information propagation and retention."

## 关联
- [[ChainOfAgents]] — LSTM-MAS 是 CoA 的门控改进版本
- [[GatedMemoryMechanism]] — LSTM 门控启发的记忆机制
- [[MultiAgentLongContext]] — 多智能体长上下文理解的新范式

## 矛盾
- (暂无)
