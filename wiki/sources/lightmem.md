---
title: "LightMem"
type: source
tags: [agent-memory, lightweight, SLM, memory-system]
date: 2026-04-09
source_file: raw/papers/lightmem.md
last_updated: 2026-05-28
---

## 概要
LightMem 提出由 Small Language Models (SLMs) 驱动的轻量级 agent memory（智能体记忆）系统，将在线检索与离线整合分离。它采用三层架构（STM/MTM/LTM）配合两阶段检索（vector coarse + semantic re-ranking，向量粗筛+语义重排），在 LoCoMo 上比 A-MEM 提升 ~2.5 F1，median retrieval latency（中位检索延迟）为 83ms。

## 核心论点
- SLM-driven memory 在远更低延迟下实现可比准确率
- Online/offline 分离实现 bounded-compute 的高效 memory 调用
- STM/MTM/LTM 三层 memory 覆盖从即时上下文到整合知识
- 通过 user identifiers 支持多用户
- 在 LoCoMo 上 F1 +2.5 over A-MEM，retrieval 83ms

## 关键引述
> "retrieval-based external memory systems incur low online overhead but suffer from unstable accuracy" — 问题陈述：基于检索的外部记忆系统在线开销低但准确率不稳定

> "LightMem modularizes memory retrieval, writing, and long-term consolidation, and separates online processing from offline consolidation" — 架构原则：将检索、写入与长期整合模块化

## 关联
- [[AgentMemory]] — LightMem 是轻量级 AgentMemory 的具体实例化
- [[LightMem]] — 此来源中形式化的概念与系统
- [[LoCoMo]] — LightMem 的主要评估基准
- [[A-MEM]] — LightMem 超越的基准方法，差距 2.5 F1
- [[Emem]] — 不同架构理念的替代 episodic memory 方案
- [[PASK]] — 可利用 LightMem 低延迟 memory 的主动 agent

## 矛盾
- 与重型 LLM memory 方案矛盾：LightMem 表明在适当架构下 SLM-driven memory 足够有效