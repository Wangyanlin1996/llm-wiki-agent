---
title: "CEMA: Causal Explanations for Sequential Decision-Making in Multi-Agent Systems"
type: source
tags: [agent-explainability, causal-explanation, multi-agent, counterfactual, autonomous-driving]
date: 2023-02-21
source_file: raw/papers/cema-causal-explanations-mas.pdf
arxiv_id: "2302.10809"
authors: ["Balint Gyevnar", "Cheng Wang", "Christopher G. Lucas", "Shay B. Cohen", "Stefano V. Albrecht"]
venue: AAMAS 2024
citation_count: pending
---

## Summary

CEMA（Causal Explanations in Multi-Agent systems）框架为动态序贯多智能体系统中 agent 的决策创建因果自然语言解释，以构建更可信的自主 agent。与假设固定因果结构的前人工作不同，CEMA 仅需要前向模拟系统状态的概率模型，通过模拟反事实世界识别 agent 决策背后的显著原因。在自动驾驶运动规划任务上评估，证明即使在大量其他 agent 存在时也能正确鲁棒地识别原因。用户研究显示 CEMA 解释对参与者的信任有积极影响。发布 HEADD 数据集。

## Key Claims

- **不假设固定因果结构**——仅需要前向模拟的概率模型，更具适用性
- **反事实世界模拟识别显著原因**——counterfactual simulation 找到"如果不是因为X，agent 不会做这个决策"
- **多 agent 场景鲁棒**——即使大量其他 agent 存在仍正确识别原因
- **用户研究验证**：CEMA 解释对自动驾驶信任有积极影响，评分与高质量人工基线解释相当
- **HEADD 数据集**：发布收集的解释及标注

## Key Quotes

> "Unlike prior work that assumes a fixed causal structure, CEMA only requires a probabilistic model for forward-simulating the state of the system."

> "CEMA's explanations have a positive effect on participants' trust in autonomous vehicles and are rated as high as high-quality baseline explanations elicited from other participants."

## Connections

- [[CausalExplanation]] — CEMA 是因果解释在 MAS 中的扩展
- [[MultiAgentExplainability]] — CEMA 是 MAS 解释的核心方法
- [[AgentExplainability]] — 因果自然语言解释增强 agent 可信度
- [[causal-explanations-sequential-uncertainty]] — CEMA 扩展该单 agent 框架到多 agent
- [[counterfactual-mas-explanation]] — AXIS 同作者后续工作，反事实+LLM
- [[ExplainablePlanning]] — 自动驾驶运动规划解释与规划解释互补

## Contradictions

无已知矛盾。
