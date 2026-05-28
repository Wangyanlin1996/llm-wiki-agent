---
title: "Evo-Memory"
type: source
tags: [agent-memory, benchmark, LLM-agent, test-time-learning]
date: 2025-11-20
source_file: raw/papers/evo-memory.md
last_updated: 2026-05-27
---

## 概要
Evo-Memory 引入了首个用于评估 LLM agents 中自进化 memory 的 streaming benchmark，要求 agents 在每次交互后搜索、适应和进化 memory，覆盖 10 个多样化数据集。它统一了 10+ memory modules，提出 ExpRAG（experience retrieval）和 ReMem（action-think-memory refine pipeline）基准，证明 test-time memory evolution 对长程 agent 性能至关重要。

## 关键论点
- Memory 管理与进化在 LLM agents 中研究不足
- 静态对话评估忽略了动态 memory 积累
- Test-time evolution（部署期间持续 memory 更新）至关重要
- ReMem pipeline 集成 reasoning-actions-memory 以实现持续改进

## 关键引述
> "Statefulness is essential for large language model (LLM) agents to perform long-term planning and problem-solving" — 核心动机

> "Evo-Memory structures datasets into sequential task streams, requiring LLMs to search, adapt, and evolve memory after each interaction" — 基准设计

## 关联
- [[AgentMemory]] — Evo-Memory 评估 AgentMemory 中描述的 memory 机制
- [[EvoMemory]] — 该基准本身是此处形式化的概念
- [[LoCoMo]] — Evo-Memory benchmark 中常用的评估基准
- [[A-MEM]] — 在 Evo-Memory 中评估的已有 memory 基准方法
- [[LightMem]] — 可受益于 Evo-Memory 评估的轻量级 memory 方案
- [[Emem]] — 解决 Evo-Memory 中识别的去上下文化问题的 episodic memory 范式

## 矩盾
- 与 static-memory 假设矛盾：Evo-Memory 证明静态对话评估忽略了动态 memory 积累