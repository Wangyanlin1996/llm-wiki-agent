---
title: "OnePred: Next-Query Prediction via Recursive Intent Memory in Multi-Turn Conversations"
type: source
tags: [next-query-prediction, recursive-intent-memory, reinforcement-learning, multi-turn, NQP-Bench]
date: 2026-05-01
source_file: raw/papers/onepred.md
last_updated: 2026-05-29
---

## 概要
OnePred 提出递归意图记忆作为跨轮上下文机制，通过两阶段 RL 管线实现 Next-Query Prediction：第一阶段教模型预测下一查询，第二阶段教模型压缩冗余 token，token 消耗降低 22×，并附带 NQP-Bench 基准评测。

## 核心论点
- 多轮对话中的意图信息应以意图级表示而非原始 token 序列跨轮传递
- 两阶段 RL 管线优于直接端到端训练：先建立预测能力，再优化压缩效率
- 当前 Next-Query Prediction 缺乏系统基准，NQP-Bench 填补此空白

## 关键引述
> "token consumption reduced 22×" — 两阶段 RL 压缩效果

> "recursive intent memory as cross-turn context" — 核心设计理念

## 关联
- [[IntentRecommendation]] — Next-Query Prediction 属于意图推荐
- [[RecursiveIntentMemory]] — 核心机制：递归意图记忆
- [[IntentRL]] — 与 IntentRL 的两阶段 RL 方法对比
- [[AgentMemory]] — 递归意图记忆与通用 Agent Memory 的关系