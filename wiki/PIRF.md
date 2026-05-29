---
title: "PIRF"
type: concept
tags: [intent-recommendation, proactive-agent, state-tracking, GUI-agent]
sources: [pira-bench]
last_updated: 2026-05-28
---

# PIRF — 主动意图推荐框架（Proactive Intent Recommendation Framework）

PIRF（Proactive Intent Recommendation Framework，主动意图推荐框架）是与 [[PIRABench]] 一同提出的记忆感知状态追踪（memory-aware state-tracking）框架，用于 GUI 上的主动意图推荐智能体。

## 核心设计

PIRF 针对主动意图推荐的三大独特挑战：

1. **多条交错意图线程** — 用户在任务间切换；PIRF 独立追踪每条线程
2. **误导性视觉输入** — 噪声 GUI 状态可能触发虚假意图检测；PIRF 利用记忆上下文过滤噪声
3. **用户偏好适配** — 主动推荐需要匹配个人用户习惯

## 架构

- 记忆感知状态追踪（memory-aware state tracking）：跨会话维护按用户和按线程的上下文
- 多任务线程管理：区分并优先排序并发的意图流
- 噪声过滤：利用累积记忆区分可行动事件与无关 GUI 变化

## 与 [[PIRABench]] 的关联

PIRF 作为 [[PIRABench]] 上评估的基线智能体框架，证明记忆感知追踪相比朴素 MLLM 方法显著提升主动意图推荐准确率。

## 跨方向关联

PIRF 将 [[IntentRecommendation]] 与 [[AgentMemory]] 关联 — 其记忆感知状态追踪本质上是智体记忆的一种专门形式，适配于 GUI 上的主动推荐，类似于 [[PASK]] 使用混合记忆（workspace/user/global）进行需求检测。