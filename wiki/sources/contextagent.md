---
title: "ContextAgent"
type: source
tags: [intent-understanding, proactive-agent, sensory-perception, wearable]
date: 2025-05-20
source_file: raw/papers/contextagent.md
last_updated: 2026-05-28
---

## 概要
ContextAgent 是首个结合感知信息（来自可穿戴设备的视频、音频）的上下文感知主动式 LLM agent，用于理解用户意图并预测主动式服务需求。ContextAgentBench 覆盖 9 个场景和 20 个工具的 1000 个样本，在主动式预测和工具调用准确率上分别提升 8.5% 和 6.0%。

## 核心论点
- 感知上下文（可穿戴设备视频/音频）显著增强主动式意图理解
- 用户画像+历史数据改善主动式服务预测
- 上下文感知主动性比基于规则的方法高出 8.5%/6.0%

## 关键引述
> "Context-aware proactivity outperforms rule-based approaches by 8.5%/6.0%" — 性能声明：上下文感知主动性优于基于规则的方法

## 关联
- [[IntentUnderstanding]] — ContextAgent 通过可穿戴设备感知用户意图
- [[ContextAgent]] — 引入的主动式 agent 概念
- [[IntentRecommendation]] — 通过上下文的主动式推荐
- [[PIRABench]] — 相关的主动式意图评测基准
- [[Satori]] — 类似的主动式意图建模 AR 助手