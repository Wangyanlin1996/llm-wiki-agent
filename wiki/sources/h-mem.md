---
title: "H-Mem"
type: source
tags: [agent-memory, hybrid-memory, evolving-memory]
date: 2026-05-15
source_file: raw/papers/h-mem.md
last_updated: 2026-05-28
---

## 概要
H-Mem 引入了一种新型 hybrid memory（混合记忆）机制用于 agent memory 的进化与检索，组合多种记忆表征（事实、摘要、用户画像）以实现灵活检索与持续进化。

## 核心论点
- Hybrid representation（混合表征，事实+摘要+用户画像）覆盖不同推理需求
- Evolving mechanism 实现持续 memory 更新
- Retrieval 根据查询类型在不同表征间自适应

## 关键引述
> "Hybrid representation covers different reasoning needs" — 多表征设计理由：混合表征覆盖不同推理需求

## 关联
- [[AgentMemory]] — H-Mem 提出混合式 agent memory
- [[HMem]] — 引入的混合记忆概念
- [[LightMem]] — 轻量级 memory 作为一种表征类型
- [[Emem]] — 替代进化式 memory 对比