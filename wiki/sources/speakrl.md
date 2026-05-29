---
title: "SpeakRL: Synergizing Reasoning, Speaking, and Acting with RL"
type: source
tags: [reinforcement-learning, proactive-clarification, agent, SpeakER, reasoning-speaking-acting]
date: 2025-12-01
source_file: raw/papers/speakrl.md
last_updated: 2026-05-29
---

## 概要
SpeakRL 通过 RL 增强 Agent 主动澄清意图的能力，奖励模型"问对的澄清问题"而非盲目执行。构建 SpeakER 合成数据集训练 Agent 在推理-说话-行动之间协同，任务完成率绝对提升 20.14%。

## 核心论点
- RL 训练应奖励有效澄清问题而非仅奖励任务执行结果，培养 Agent 主动澄清意图的能力
- 推理、说话、行动三者的协同是高效 Agent 的关键：先推理再澄清再行动
- SpeakER 合成数据集为 RL 训练提供覆盖澄清策略的场景

## 关键引述
> "task completion rate absolute improvement of 20.14%" — RL 澄清策略的效果

> "rewarding asking the right clarification questions" — RL 奖励设计理念

## 关联
- [[IntentRecommendation]] — RL 增强主动澄清属于意图推荐
- [[IntentRL]] — 与 IntentRL 的 RL 方法对比（两者都使用 RL 训练主动意图行为）
- [[AskBeforePlan]] — 澄清优先策略与 CEP 框架的对比