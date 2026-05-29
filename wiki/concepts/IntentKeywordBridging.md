---
title: "IntentKeywordBridging"
type: concept
tags: [intent-keyword, target-guided, proactive-dialogue, scenario-modeling]
sources: [target-proactive-dialogue]
last_updated: 2026-05-29
---

# IntentKeywordBridging

意图关键词桥接（Intent-Keyword Bridging）是在目标导向主动对话中，通过预测未来轮次的意图关键词来引导对话走向的机制。

## 核心思想

在目标导向对话中，Agent 需要主动引导对话朝特定目标方向前进。意图关键词桥接通过预测未来轮次应该出现的意图关键词，为对话生成提供明确的方向指引。

## 双机制协同

1. **会话场景建模（Scenario Modeling）** — 整合用户画像与领域知识构建对话上下文
2. **意图关键词桥接（Intent-Keyword Bridging）** — 预测未来轮次的意图关键词引导生成

场景建模提供"在哪里对话"，意图关键词桥接提供"朝哪里走"。

## 效果

显著改善对话的主动性（proactivity）和信息性（informativeness），实现目标导向的主动对话。

## 关联
- [[IntentRecommendation]] — 意图关键词桥接服务于目标导向的意图推荐
- [[ConversationStarterGeneration]] — 冷启动 vs 目标导向的意图引导对比
- [[PASK]] — DD-MM-PAS 的需求检测 vs 场景建模的用户画像