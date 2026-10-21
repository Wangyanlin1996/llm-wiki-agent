---
title: "Agent Primitives：多智能体系统的可复用潜在构建块"
type: source
tags: [multi-agent-long-context]
sources: [agent-primitives]
source_file: raw/papers/agent-primitives.pdf
last_updated: 2026-07-24
arxiv_id: "2602.03695"
authors: ["Haibo Jin", "Kuang Peng", "Ye Yu", "Xiaopeng Yuan", "Haohan Wang"]
year: 2026
venue: "arXiv.org"
citation_count: 6
doi: "10.48550/arXiv.2602.03695"
---

## 概要
Agent Primitives 受神经网络设计启发，将 MAS 架构分解为少量可复用的内部计算模式。实例化三个原语：Review、Voting and Selection、Planning and Execution。所有原语通过 KV cache 内部通信，缓解长上下文多阶段交互中的信息退化。Organizer agent 根据查询选择和组合原语，形成 primitive-based MAS。比单 agent 基线提升 12.0-16.5% 准确率，token 和延迟减少约 3-4x。

## 关键贡献
- 三个可复用原语：Review / Voting & Selection / Planning & Execution
- KV cache 内部通信替代自然语言，缓解长上下文信息退化
- +12.0-16.5% 准确率，token/延迟 -3~4x

## 关键引用
> "All primitives communicate internally via key-value (KV) cache, which improves both robustness and efficiency by mitigating information degradation across multi-stage interactions."

## 关联
- [[AAFLOWPlus]] — AAFLOW+ 将 KV cache 分布式化，Agent Primitives 聚焦原语抽象
- [[MultiAgentCommunication]] — 多智能体通信机制
- [[ReusableAgentBlocks]] — 可复用智能体构建块

## 矛盾
- (暂无)
