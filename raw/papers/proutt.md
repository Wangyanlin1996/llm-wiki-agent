---
title: "ProUtt: LLM-Driven Preference Data Synthesis for Proactive Prediction of Next User Utterance"
type: paper
tags: [preference-data-synthesis, intent-tree, proactive-prediction, next-utterance, exploration-exploitation]
authors: [Jinqiang Wang, Huansheng Ning, Jianguo Ding]
year: 2026
venue: null
citation_count: null
arxiv_id: "2601.09713"
doi: null
pdf_url: "https://arxiv.org/pdf/2601.09713"
sub_area: intent-recommendation
---

## 概要
将对话历史建模为意图树，从 exploitation（沿已知意图分支预测）和 exploration（探索新意图分支）双视角生成推理轨迹，通过扰动与修正构造偏好数据，在 4 个基准上评测优于现有 Next User Utterance Prediction 方法。

## 核心贡献
- 提出意图树建模方法，将对话历史组织为层次化意图结构而非扁平序列
- 设计 exploitation + exploration 双视角推理轨迹生成策略，兼顾已知意图预测与新意图探索
- 通过扰动与修正自动构造偏好数据，无需人工标注，在 4 个基准上优于现有方法