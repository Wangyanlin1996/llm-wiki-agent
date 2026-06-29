---
title: "Towards Responsible and Explainable AI Agents with Consensus-Driven Reasoning"
type: source
tags: [agent-explainability, consensus-driven, responsible-ai, multi-model]
date: 2025-12-25
source_file: raw/papers/responsible-explainable-ai-agents.pdf
arxiv_id: "2512.21699"
authors: ["Eranga Bandara", "Tharaka Hewa", "Ross Gore", "Sachin Shetty", "Ravi Mukkamala", "Peter Foytik", "Abdul Rahman", "Safdar H. Bouk", "Xueping Liang", "Amin Hass", "Sachini Rajapakse", "Ng Wee Keong", "Kasun De Zoysa", "Aruna Withanage", "Nilaan Loganathan"]
venue: arXiv preprint
citation_count: pending
---

## Summary

本文提出面向生产级 agentic workflow 的 RAI+XAI Agent 架构，基于多模型共识与推理层治理。异构 LLM/VLM agent 联盟独立从共享输入生成候选输出，显式暴露不确定性、分歧和替代解释。专用推理 agent 执行结构化整合，强制安全与策略约束，缓解幻觉和偏见，产生可审计的、有证据支撑的决策。可解释性通过显式跨模型比较和保留中间输出实现，责任通过集中式推理层控制和 agent 级约束实现。

## Key Claims

- **现有 agentic AI 实现强调功能与可扩展性，但提供有限的决策理据理解或跨 agent 交互的责任执行机制**
- **多模型共识架构**：异构 LLM/VLM 独立生成 → 显式暴露分歧与不确定性 → 推理 agent 结构化整合
- **可解释性 = 跨模型比较 + 保留中间输出**——不是事后解释，而是过程透明
- **责任 = 集中推理层控制 + agent 级约束**——治理内嵌于架构
- 共识驱动推理在多领域提升鲁棒性、透明度和运营信任

## Key Quotes

> "Existing agentic AI implementations often emphasize functionality and scalability, yet provide limited mechanisms for understanding decision rationale or enforcing responsibility across agent interactions."

> "Explainability is achieved through explicit cross-model comparison and preserved intermediate outputs, while responsibility is enforced through centralized reasoning-layer control and agent-level constraints."

## Connections

- [[ConsensusDrivenReasoning]] — 本论文是该概念的核心实现
- [[AgentExplainability]] — 共识驱动是 agent 可解释性的架构级方案
- [[AgentAccountability]] — 推理层治理实现问责
- [[MultiAgentExplainability]] — 多模型共识扩展 MAS 解释
- [[trism-agentic-ai]] — TRiSM 框架与本架构的治理目标互补

## Contradictions

无已知矛盾。
