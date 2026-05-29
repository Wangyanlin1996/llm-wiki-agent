---
title: "ETAPP"
type: source
tags: [intent-recommendation, personalized, tool-augmented, proactivity, ACL]
date: 2025
source_file: raw/papers/etapp.md
last_updated: 2026-05-28
---

## 概要
ETAPP（ACL 2025）从个性化（personalization）和主动性（proactivity）视角评估个性化工具增强的 LLMs，建立沙盒环境和 800 个测试案例覆盖多样用户画像。基于关键点的 LLM 评估减轻评判偏差；研究结果揭示了工具调用策略中个性化与主动性之间的权衡关系。

## 核心论点
- 个性化工具调用需要专门的评测基准
- 主动性与个性化是交织的维度
- 基于关键点的评估减轻 LLM-as-judge 偏差
- Fine-tuning（微调）改善个性化但影响主动性的方式不同
- 偏好设置策略需要仔细校准

## 关键引述
> "Proactivity and personalization are intertwined dimensions" — 关键洞察：主动性与个性化是交织的维度

## 关联
- [[IntentRecommendation]] — 个性化主动式推荐
- [[ETAPP]] — 引入的评估框架
- [[VitaBench2]] — 相关的个性化 agent 评测基准
- [[PersonalAlign]] — 个性化意图对齐对比
- [[PASK]] — 主动式 agent 技能套件对比