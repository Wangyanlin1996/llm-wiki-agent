---
title: "MINTEval"
type: source
tags: [agent-memory, multi-target, interference, evaluation]
date: 2026-05-18
source_file: raw/papers/minteval.md
last_updated: 2026-05-28
---

## 概要
MINTEval 评估长程 agent 系统中多目标干扰下的 memory 性能，揭示管理多个并发目标会产生交叉干扰，降低 memory 检索准确率。

## 核心论点
- 多目标目标产生 memory 干扰
- 现有 benchmark 假设单任务序列
- 干扰模式需要专门评估
- Memory 系统必须处理并发目标追踪

## 关键引述
> "Multi-target goals create memory interference" — 干扰发现：多目标产生记忆干扰

## 关联
- [[AgentMemory]] — MINTEval 在干扰条件下测试 agent memory
- [[MINTEval]] — 引入的评估框架
- [[PIRABench]] — 相关主动式意图评测基准对比
- [[PIRF]] — 主动式检索与多目标干扰相关