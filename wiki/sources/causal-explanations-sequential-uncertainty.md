---
title: "Causal Explanations for Sequential Decision Making Under Uncertainty"
type: source
tags: [agent-explainability, causal-explanation, SCM, sequential-decision-making, uncertainty]
date: 2022-05-30
source_file: raw/papers/causal-explanations-sequential-uncertainty.pdf
arxiv_id: "2205.15462"
authors: ["Samer B. Nashed", "Saaduddin Mahmud", "Claudia V. Goldman", "Shlomo Zilberstein"]
venue: arXiv preprint (9 pages, 7 figures)
citation_count: pending
---

## Summary

本文引入基于结构因果模型（SCM）的随机序贯决策系统因果解释框架。该单一框架可识别多个语义不同的解释——这是此前不可能的。论文建立了 MDP 上因果推理的精确方法和近似技术，讨论了适用性和运行时界限。人类实验确认该方法的益处。

## Key Claims

- **基于 SCM 范式的因果解释框架**——统一处理随机序贯决策
- **单一框架识别多个语义不同的解释**——此前方法无法实现
- **精确方法 + 近似技术**：MDP 上的因果推理，含运行时界限
- 框架灵活性通过多个场景展示；人类实验验证解释的有效性
- 为 agent 行为提供"为什么"的因果回答，而非仅相关性

## Key Quotes

> "This single framework can identify multiple, semantically distinct explanations for agent actions -- something not previously possible."

## Connections

- [[CausalExplanation]] — 本论文是 SCM 因果解释的基础工作
- [[AgentExplainability]] — 因果解释是 agent 可解释性的核心方法
- [[cema-causal-explanations-mas]] — CEMA 将此框架扩展到多智能体系统
- [[counterfactual-mas-explanation]] — AXIS 使用反事实因果模型，同源思路
- [[ExplainablePlanning]] — 序贯决策因果解释与规划解释互补

## Contradictions

无已知矛盾。
