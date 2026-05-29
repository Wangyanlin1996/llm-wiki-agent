---
title: "AssistanceGames"
type: concept
tags: [assistance-games, agent-alignment, goal-inference, preference-construction]
sources: [good-agent-alignment]
last_updated: 2026-05-29
---

# AssistanceGames

Assistance Games 是一种形式化框架，将 Agent 对齐问题建模为协作博弈：Agent 通过观察人类行为推断人类偏好并协助实现目标。

## 传统 Assistance Games

假设固定、预设的偏好空间，Agent 在已知偏好分布下优化协助策略。适用于偏好明确、有限的场景。

## Open-Universe Assistance Games (OU-AGs)

[[GOOD]] 扩展 Assistance Games 到开放对话场景：
- 偏好不再是固定预设，而是通过自然语言在交互中动态构建的分布
- 目标可以被逐步修正和扩展（open-ended dialogue）
- 基于认知科学的偏好建构理论（preference construction）

## GOOD 方法

从开放对话中提取和排序候选目标：
- 利用 LLM 模拟用户进行概率推断
- 实现可解释、不确定性感知的偏好表示
- 无需大规模离线偏好数据集

## 关联
- [[IntentUnderstanding]] — 目标推断是意图理解的形式化基础
- [[IntentRL]] — RL 方法与 Assistance Games 形式化的互补
- [[IntentSignalTheory]] — I-hat（可观测代理）与 OU-AGs 中候选目标的关系