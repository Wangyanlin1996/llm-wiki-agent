---
title: "E-mem"
type: source
tags: [agent-memory, episodic-memory, multi-agent]
date: 2026-01-17
source_file: raw/papers/emem.md
last_updated: 2026-05-27
---

## 概要
E-mem 从 Memory Preprocessing 转向 Episodic Context Reconstruction，采用异构多 agent 层级架构，其中 assistant agents 维护未压缩的 memory 并在聚合前进行局部推理。在 LoCoMo 上实现 54% F1（超越 GAM 7.75%），同时降低 >70% token 成本。

## 关键论点
- Memory preprocessing 导致破坏性的去上下文化（de-contextualization）
- Episodic context reconstruction 为深度推理保留上下文完整性
- 多 agent 层级架构实现聚合前的局部推理
- 54% F1 超越 GAM 7.75%，同时降低 >70% token 开销

## 关键引述
> "prevalent memory preprocessing paradigms suffer from destructive de-contextualization" — 问题诊断

> "shifting from Memory Preprocessing to Episodic Context Reconstruction" — 范式转变

## 关联
- [[AgentMemory]] — E-mem 在 AgentMemory 研究中提出范式转变
- [[Emem]] — episodic context reconstruction 概念在此形式化
- [[LoCoMo]] — E-mem 在此基准上实现 54% F1 的主要评估基准
- [[GAM]] — E-mem 超越的基准方法，差距 7.75%
- [[EvoMemory]] — E-mem 的方法可在 Evo-Memory 的 streaming paradigm 下评估
- [[LightMem]] — 不同 memory 架构理念的替代轻量级方案

## 矩盾
- 与基于 preprocessing 的 memory 方案矛盾：E-mem 论证 preprocessing 导致破坏性去上下文化，主张 episodic context reconstruction