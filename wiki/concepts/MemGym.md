---
title: "MemGym"
type: concept
tags: [agent-memory, benchmark, long-horizon, memory-environment]
sources: [memgym]
last_updated: 2026-05-28
---

# MemGym

MemGym 是面向 LLM 智能体评估的长程记忆环境（long-horizon memory environment），提供压力测试记忆持久性和跨长时间交互序列检索的评估设置。

## 关键设计

- 长程环境：交互序列跨越较长时间段
- 记忆持久性测试：评估智能体在长时间内维持和检索信息的能力
- 揭示长交互中的记忆退化模式

## 在 [[AgentMemory]] 中的定位

MemGym 聚焦长程持久性而非演化，与 [[EvoMemory]]（演化记忆的流式基准）互补。连同 [[LoCoMo]]（长期对话）、[[ENPMRBench]]（主动检索）和 [[MINTEval]]（多目标干扰），MemGym 将评估版图从单基准（LoCoMo）扩展到覆盖不同记忆挑战的专门环境。