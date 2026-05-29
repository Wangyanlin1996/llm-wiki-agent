---
title: "ConversationStarterGeneration"
type: concept
tags: [conversation-starter, cold-start, personalized-generation, social-dialogue]
sources: [icebreaker]
last_updated: 2026-05-29
---

# ConversationStarterGeneration

对话开场语生成（Conversation Starter Generation）是指在零意图冷启动场景下，Agent 主动生成个性化开场语发起对话的新任务定义。

## 任务定义

- **场景**：零意图冷启动——无任何对话历史，仅有用户静态画像
- **目标**：生成能引起用户共振并引发交互的开场语
- **挑战**：在无用户输入的极端条件下实现意图推荐

## IceBreaker 两步握手框架

1. **共振感知兴趣蒸馏（Resonance-Aware Interest Distillation）** — 从用户画像提取兴趣标签，识别共振点
2. **交互导向生成（Interaction-Oriented Generation）** — 结合兴趣标签与交互策略生成开场语

## 工业验证

真实平台 A/B 测试 CTR 提升 9.425%，证明框架在社交对话场景的有效性。

## 关联
- [[IntentRecommendation]] — 对话开场语生成是意图推荐在冷启动条件下的特例
- [[PASK]] — PASK 的 DD-MM-PAS 与 IceBreaker 两步握手的对比
- [[PIRABench]] — GUI 场景 vs 社交对话场景的意图推荐