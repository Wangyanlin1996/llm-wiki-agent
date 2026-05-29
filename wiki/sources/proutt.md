---
title: "ProUtt: LLM-Driven Preference Data Synthesis for Proactive Prediction of Next User Utterance"
type: source
tags: [preference-data-synthesis, intent-tree, proactive-prediction, next-utterance, exploration-exploitation]
date: 2026-01-01
source_file: raw/papers/proutt.md
last_updated: 2026-05-29
---

## 概要
ProUtt 将对话历史建模为意图树，从 exploitation（沿已知意图分支预测）和 exploration（探索新意图分支）双视角生成推理轨迹，通过扰动与修正构造偏好数据，在 4 个基准上评测优于现有 Next User Utterance Prediction 方法。

## 核心论点
- 对话历史应组织为层次化意图树而非扁平序列，以捕捉意图的结构化演变
- exploitation 与 exploration 双视角推理轨迹生成覆盖已知与未知意图空间
- 扰动与修正构造偏好数据避免了人工标注成本，同时保持数据质量

## 关键引述
> "exploitation + exploration dual-view reasoning trajectory generation" — 双视角推理策略

## 关联
- [[IntentRecommendation]] — Next Utterance Prediction 属于意图推荐
- [[IntentTreeModeling]] — 核心概念：意图树建模
- [[RecursiveIntentMemory]] — 与 OnePred 的递归记忆对比
- [[IntentRL]] — RL 方法与偏好数据合成方法的对比