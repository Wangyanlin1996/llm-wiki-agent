---
title: "IceBreaker: Breaking the First-Message Barrier with Personalized Starters"
type: source
tags: [conversation-starter, cold-start, personalized-generation, CTR, ACL-2026]
date: 2026-04-01
source_file: raw/papers/icebreaker.md
last_updated: 2026-05-29
---

## 概要
IceBreaker 定义对话开场语生成新任务（零意图冷启动场景），提出两步握手框架：共振感知兴趣蒸馏从用户画像提取兴趣标签，交互导向生成结合兴趣与交互策略生成开场语。真实平台 A/B 测试验证 CTR 提升 9.425%。

## 核心论点
- 零意图冷启动场景下，Agent 必须在无任何对话历史的情况下主动发起个性化对话
- 对话开场语生成是意图推荐在极端条件下的特例：无用户输入、仅依赖静态画像
- 两步握手框架将兴趣提取与交互策略生成解耦，提高开场语的共振性和交互性

## 关键引述
> "CTR improvement of 9.425% in real-world A/B testing" — 工业验证结果

## 关联
- [[IntentRecommendation]] — 对话开场语生成属于意图推荐范畴
- [[ConversationStarterGeneration]] — 核心概念：对话开场语生成
- [[PASK]] — PASK 的 DD-MM-PAS 与 IceBreaker 的两步握手对比
- [[PIRABench]] — PIRA-Bench 关注 GUI 场景，IceBreaker 关注社交对话场景