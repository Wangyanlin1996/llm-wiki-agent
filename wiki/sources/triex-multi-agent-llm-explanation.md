---
title: "TriEx: A Game-based Tri-View Framework for Explaining Internal Reasoning in Multi-Agent LLMs"
type: source
tags: [agent-explainability, multi-agent, tri-view, belief-state, game-based, ACL2026]
date: 2026-04-21
source_file: raw/papers/triex-multi-agent-llm-explanation.pdf
arxiv_id: "2604.20043"
authors: ["Ziyi Wang", "Chen Zhang", "Wenjun Peng", "Qi Wu", "Xinyu Wang"]
venue: ACL 2026 Main
citation_count: pending
---

## Summary

TriEx 提出三视角可解释性框架，用对齐的工件（artifacts）工具化序贯决策：(i) 绑定到动作的结构化第一人称自我推理、(ii) 随时间更新的关于对手的显式第二人称信念状态、(iii) 基于环境参考信号的第三人称预言机审计。该设计将解释从自由叙述转变为可跨时间和视角比较、检查的证据锚定对象。使用不完全信息策略游戏作为受控测试床，揭示 agent 说什么、信什么、做什么之间的系统性不匹配。

## Key Claims

- **LLM agent 的可解释性在交互式、部分可观察设置中尤其具挑战性**——决策依赖演化信念和其他 agent
- **三视角对齐工件**：第一人称自我推理 + 第二人称信念状态 + 第三人称预言机审计
- **解释从自由叙述变为证据锚定对象**——可跨时间和视角比较、检查
- **系统性不匹配**：agent 说什么、信什么、做什么之间存在系统性偏差——揭示解释忠实性问题
- 可解释性是交互依赖属性（interaction-dependent property），需多视角证据锚定评估
- 不完全信息策略游戏作为受控测试床

## Key Quotes

> "This design turns explanations from free-form narratives into evidence-anchored objects that can be compared and checked across time and perspectives."

> "Revealing systematic mismatches between what agents say, what they believe, and what they do."

> "Explainability as an interaction-dependent property."

## Connections

- [[MultiAgentExplainability]] — TriEx 是 MAS 解释的三视角框架
- [[AgentExplainability]] — 信念状态追踪扩展 agent 可解释性
- [[cema-causal-explanations-mas]] — 两者都关注 MAS 决策解释，CEMA 用因果，TriEx 用三视角
- [[counterfactual-mas-explanation]] — 互补：反事实 vs 三视角信念追踪
- [[ExecutionProvenance]] — 三视角工件是执行溯源的多视角实现

## Contradictions

- 揭示"解释忠实性"问题：agent 的自我推理叙述与其信念/行为不一致——对依赖 LLM 自我解释的方法构成挑战
