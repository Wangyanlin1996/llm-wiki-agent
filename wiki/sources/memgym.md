---
title: "MemGym"
type: source
tags: [agent-memory, benchmark, long-horizon, memory-environment]
date: 2026-05-20
source_file: raw/papers/memgym.md
last_updated: 2026-05-28
---

## 概要
MemGym 为 LLM agents 引入了长程记忆环境，提供压力测试 memory 持久性与检索的评估设置，覆盖扩展交互序列中的记忆退化模式。

## 核心论点
- 现有 benchmark 过短，无法评估 memory 持久性
- 长程环境揭示 memory 退化模式
- 需要新的评估范式用于 memory-in-the-wild（真实场景记忆）测试

## 关键引述
> "Existing benchmarks are too short for evaluating memory persistence" — 基准差距识别：现有评测基准过短

## 关联
- [[AgentMemory]] — MemGym 评估 agent memory 系统
- [[MemGym]] — 引入的 benchmark 概念
- [[EvoMemory]] — 进化式 memory 在长程设置下测试
- [[LoCoMo]] — 相关长上下文 memory benchmark 对比