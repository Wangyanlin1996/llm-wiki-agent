---
title: "PASK"
type: source
tags: [intent-recommendation, proactive-agent, long-term-memory]
date: 2026-04-09
source_file: raw/papers/pask.md
last_updated: 2026-05-28
---

## 概要
PASK 为 streaming proactive AI agents（流式主动式 AI 智能体）提出 DD-MM-PAS 范式（Demand Detection→Memory Modeling→Proactive Agent System，需求检测→记忆建模→主动式智能体系统），以 IntentFlow 实现 demand detection，配合 hybrid memory（workspace/user/global，混合记忆）和 PAS infra。它引入 LatentNeeds-Bench，并证明 IntentFlow 在延迟约束下匹配 Gemini3-Flash，同时识别更深层的意图。

## 核心论点
- Streaming proactive agents 需要系统化范式（DD-MM-PAS）
- IntentFlow 在延迟约束下匹配 Gemini3-Flash 的需求检测
- Hybrid memory（workspace/user/global）支持长期上下文
- LatentNeeds-Bench 提供来自用户授权数据的真实评估
- Proactive agents 识别超越表面查询的深层意图

## 关键引述
> "DD-MM-PAS as a general paradigm for streaming proactive AI agents" — 范式定义：作为流式主动式 AI 智能体的通用范式

> "IntentFlow matches leading Gemini3-Flash models under latency constraints while identifying deeper user intent" — 结果：IntentFlow 在延迟约束下匹配领先模型并识别更深层意图

## 关联
- [[IntentRecommendation]] — PASK 通过 DD-MM-PAS 实现主动式意图推荐
- [[PASK]] — intent-aware proactive agent 概念在此形式化
- [[DDMM-PAS]] — PASK 提出的系统化范式
- [[AgentMemory]] — hybrid memory 架构与 AgentMemory 机制相关
- [[LightMem]] — PASK 的 memory modeling 与 LightMem 的轻量级方案一致
- [[PIRABench]] — PIRA-Bench 评估与 PASK 相关的主动式意图推荐
- [[VitaBench2]] — VitaBench 2.0 的个性化需求与 PASK 的主动式范式一致

## 矛盾
- 与表面查询满足矛盾：PASK 证明识别超越表面查询的深层意图对 proactive agents 至关重要