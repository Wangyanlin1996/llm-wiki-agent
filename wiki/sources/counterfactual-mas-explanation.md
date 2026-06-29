---
title: "Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour (AXIS)"
type: source
tags: [agent-explainability, counterfactual, multi-agent, LLM, autonomous-driving]
date: 2025-05-23
source_file: raw/papers/counterfactual-mas-explanation.pdf
arxiv_id: "2505.17801"
authors: ["Bálint Gyevnár", "Christopher G. Lucas", "Stefano V. Albrecht", "Shay B. Cohen"]
venue: arXiv preprint
citation_count: pending
---

## Summary

AXIS（Agentic eXplanations via Interrogative Simulation）利用反事实效应量模型和 LLM，通过让 LLM 用"whatif"和"remove"等提示盘问环境模拟器，多轮观察并综合反事实信息，生成以人为中心的多智能体策略动作解释。在自动驾驶 10 个场景、5 个 LLM 上评估，综合鲁棒性、主观偏好、正确性和目标/动作预测。相比基线，AXIS 在所有模型上解释正确性至少提升 7.7%，4 个模型目标预测准确率提升 23%。

## Key Claims

- **自主多智能体系统引发信任关切**——协调失败、目标错位等风险使可解释性对信任校准至关重要
- **LLM 盘问模拟器生成反事实解释**——"whatif"/"remove" 提示多轮交互，LLM 综合反事实信息
- **以人为中心的动作解释**——针对多智能体策略生成人类可理解的解释
- **综合评估方法论**：鲁棒性 + 主观偏好 + 正确性 + 目标/动作预测（外部 LLM 作为评估器）
- **性能提升**：解释正确性 +7.7%（所有模型）、目标预测 +23%（4个模型）、动作预测相当

## Key Quotes

> "AXIS generates human-centred action explanations for multi-agent policies by having an LLM interrogate an environment simulator using prompts like 'whatif' and 'remove'."

> "AXIS improves perceived explanation correctness by at least 7.7% across all models and goal prediction accuracy by 23% for four models."

## Connections

- [[CausalExplanation]] — AXIS 使用反事实因果模型
- [[MultiAgentExplainability]] — AXIS 是 MAS 行为解释的 LLM 增强方法
- [[cema-causal-explanations-mas]] — 同作者前序工作，CEMA→AXIS 从概率模型到 LLM 盘问
- [[AgentExplainability]] — 反事实解释是 agent 可解释性的核心方法
- [[ExplainablePlanning]] — 自动驾驶策略解释

## Contradictions

无已知矛盾。
