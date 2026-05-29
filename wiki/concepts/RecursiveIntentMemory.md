---
title: "RecursiveIntentMemory"
type: concept
tags: [recursive-intent-memory, next-query-prediction, multi-turn, RL]
sources: [onepred]
last_updated: 2026-05-29
---

# RecursiveIntentMemory

递归意图记忆（Recursive Intent Memory）是一种跨轮上下文机制，将多轮对话中的意图信息以意图级表示而非原始 token 序列传递，实现高效的跨轮意图推理。

## 核心思想

传统多轮对话将完整历史 token 序列作为上下文输入，导致 token 消耗随轮次线性增长。递归意图记忆将每轮对话压缩为意图级表示，递归地作为下一轮的上下文输入。

## OnePred 两阶段 RL 管线

1. **第一阶段：教预测** — 训练模型学习 Next-Query Prediction 能力
2. **第二阶段：教压缩** — 在保持预测质量的前提下优化 token 压缩（消耗降低 22×）

## 与 Agent Memory 的关系

递归意图记忆是 [[AgentMemory]] 在意图推荐场景的特化应用：将 STM/MTM/LTM 三层记忆结构简化为意图级递归传递。

## 关联
- [[IntentRecommendation]] — 递归意图记忆服务于意图推荐
- [[AgentMemory]] — 递归意图记忆与通用 Agent Memory 的关系
- [[IntentTreeModeling]] — 递归记忆 vs 层次化意图树的对比