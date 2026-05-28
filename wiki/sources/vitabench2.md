---
title: "VitaBench 2.0"
type: source
tags: [intent-understanding, intent-recommendation, benchmark, personalized-agent]
date: 2026-05-26
source_file: raw/papers/vitabench2.md
last_updated: 2026-05-27
---

## 概要
VitaBench 2.0 评估长期用户交互中的个性化与主动 agent 行为，要求 agents 从碎片化交互中提取、利用和更新用户偏好。它揭示了 SOTA 模型与实际个性化需求之间的巨大差距。

## 关键论点
- 现有基准忽略了从真实交互中推断偏好
- 个性化需要从碎片化异构数据中提取偏好
- 主动性意味着识别缺失信息并主动获取
- 即使 SOTA 模型也远不能满足实际个性化需求

## 关键引述
> "user intent is often reflected in fragmented daily interactions and requires both personalized modeling and proactive interaction" — 挑战定义

> "real-world personalization remains highly challenging even for state-of-the-art models, revealing a substantial gap" — 关键发现

## 关联
- [[IntentUnderstanding]] — VitaBench 2.0 评估个性化的 IntentUnderstanding
- [[IntentRecommendation]] — VitaBench 2.0 中的主动性与 IntentRecommendation 相关
- [[VitaBench2]] — 此处形式化的基准概念
- [[PIRABench]] — GUI 语境下主动 intent 的互补基准
- [[PASK]] — 主动 agent 范式受 VitaBench 2.0 需求评估
- [[AgentMemory]] — 长期 memory 对 VitaBench 2.0 的个性化至关重要
- [[IntPro]] — per-user adaptation 与 VitaBench 2.0 的个性化需求一致

## 矛盾
- 与 SOTA 模型已足够的假设矛盾：VitaBench 2.0 暴露出显著的个性化差距