---
title: "PA-Bridge: 桥接被动与主动——对话开场语推荐增强"
type: source
tags: [intent-recommendation]
sources: [pa-bridge]
source_file: raw/papers/2605.05855.pdf
last_updated: 2026-06-04
---

## 概要
PA-Bridge 利用用户主动表达打破被动推荐的回声室效应。传统对话开场语推荐依赖封闭曝光-点击循环，导致系统偏向流行但泛化的建议。PA-Bridge用对抗分布对齐器弥合被动开场语与主动查询的分布差距，语义离散器使流行度去偏算法可部署。SIGIR 2026录用；Feature Penetration Rate +0.54%，User Active Days提升。

## 关键贡献
- 发现回声室效应——封闭曝光-点击循环导致泛化推荐
- 利用用户主动表达（自由输入）打破回声室
- 对抗分布对齐器弥合被动推荐与主动查询的分布差距
- 语义离散器使流行度去偏算法可大规模流式部署
- SIGIR 2026录用，在线A/B测试验证

## 关键引用
> "harnessing user free will through active user expressions" — 核心范式转换

## 关联
- [[IntentRecommendation]] — 对话开场语推荐作为意图推荐的社交场景
- [[ConversationStarterGeneration]] — IceBreaker定义的开场语生成任务，PA-Bridge是其推荐增强
- [[IceBreaker]] — 同为对话开场语，但PA-Bridge从推荐角度而非生成角度

## 矛盾
- 回声室效应——被动推荐系统的结构性问题，需要主动表达打破