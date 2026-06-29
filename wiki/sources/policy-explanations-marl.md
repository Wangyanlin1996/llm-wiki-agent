---
title: "Toward Policy Explanations for Multi-Agent Reinforcement Learning"
type: source
tags: [agent-explainability, multi-agent, MARL, policy-explanation, foundational]
date: 2022-04-26
source_file: raw/papers/policy-explanations-marl.pdf
arxiv_id: "2204.12568"
authors: ["Kayla Boggess", "Sarit Kraus", "Lu Feng"]
venue: IJCAI 2022
citation_count: pending
---

## Summary

本文提出多智能体强化学习（MARL）的两种策略解释方法：(i) 关于 agent 协作和任务序列的策略摘要、(ii) 回答 agent 行为查询的语言解释。在三个 MARL 领域的实验证明方法可扩展性。用户研究显示生成的解释显著提升用户性能和满意度等主观评分指标。

## Key Claims

- **现有可解释 RL 多聚焦单 agent 设置**——不适合多智能体环境的挑战
- **两种策略解释**：策略摘要（协作+任务序列）+ 语言解释（行为查询回答）
- **三个 MARL 领域验证可扩展性**
- **用户研究**：解释显著提升用户性能 + 满意度等主观评分
- 解释 agent 决策对提升系统透明度、用户满意度和促进人-agent 协作至关重要

## Key Quotes

> "Existing works on explainable reinforcement learning mostly focus on the single-agent setting and are not suitable for addressing challenges posed by multi-agent environments."

> "The generated explanations significantly improve user performance and increase subjective ratings on metrics such as user satisfaction."

## Connections

- [[MultiAgentExplainability]] — 本论文是 MARL 策略解释的基础工作
- [[AgentExplainability]] — 策略解释是 agent 可解释性的核心维度
- [[cema-causal-explanations-mas]] — 两者都关注 MAS 解释，本文用策略摘要/语言，CEMA 用因果
- [[ExplainablePlanning]] — 协作任务序列解释与规划解释互补

## Contradictions

无已知矛盾。
