---
title: "Enhancing Target-Guided Proactive Dialogue via Scenario Modeling and Intent-Keyword Bridging"
type: source
tags: [target-guided-dialogue, proactive, scenario-modeling, intent-keyword, dialogue-system]
date: 2026-05-01
source_file: raw/papers/target-proactive-dialogue.md
last_updated: 2026-05-29
---

## 概要
提出会话场景建模（用户画像+领域知识）与意图关键词桥接（预测未来轮次意图关键词）双机制增强目标导向主动对话。场景建模构建对话上下文，意图关键词桥接引导对话走向，显著改善对话的主动性和信息性。

## 核心论点
- 目标导向对话需要场景建模将用户画像与领域知识整合为对话上下文
- 意图关键词桥接机制通过预测未来轮次的意图关键词，实现目标引导的主动对话
- 双机制协同使对话同时具备主动性（主动引导）和信息性（提供有价值内容）

## 关键引述
> "significant improvements in both proactivity and informativeness" — 双机制效果总结

## 关联
- [[IntentRecommendation]] — 目标导向主动对话属于意图推荐
- [[ConversationStarterGeneration]] — 与 IceBreaker 的冷启动场景对比
- [[PASK]] — PASK 的 DD-MM-PAS 与本文的场景建模对比
- [[IntentKeywordBridging]] — 核心概念：意图关键词桥接