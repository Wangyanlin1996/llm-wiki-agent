---
title: "IntentRL"
type: source
tags: [intent-recommendation, proactive-agent, reinforcement-learning]
date: 2026-02-03
source_file: raw/papers/intentrl.md
last_updated: 2026-05-27
---

## 概要
IntentRL 训练主动 agents 在启动深度研究前澄清用户 latent intents，解决自主性-交互困境。它采用 shallow-to-deep intent refinement graph 和两阶段 RL（offline dialogues + online rollouts with user simulator），超越闭源 DR agents 的内置 clarify modules。

## 关键论点
- Deep research agents 在模糊查询上面临自主性-交互困境
- 研究前的主动 intent 澄清改善结果
- Shallow-to-deep intent refinement graph 扩展训练数据
- 两阶段 RL（offline+online simulator）实现强 intent clarification
- 超越闭源 DR agents 的内置 clarify modules

## 关键引述
> "high autonomy on ambiguous user queries often leads to prolonged execution with unsatisfactory outcomes" — 困境描述

> "IntentRL trains proactive agents to clarify latent user intents before starting long-horizon research" — 方法概述

## 关联
- [[IntentRecommendation]] — IntentRL 通过 RL 实现主动 IntentRecommendation
- [[IntentRL]] — RL 训练的主动 intent clarification 概念在此形式化
- [[IntentUnderstanding]] — intent clarification 是 IntentUnderstanding 的一种形式
- [[PIRABench]] — PIRA-Bench 评估与 IntentRL 相关的主动 intent recommendation
- [[PASK]] — 主动 agent 范式与 IntentRL 的主动澄清一致

## 矛盾
- 与完全自主假设矛盾：IntentRL 证明在深度研究前主动澄清 intent 产生更好结果