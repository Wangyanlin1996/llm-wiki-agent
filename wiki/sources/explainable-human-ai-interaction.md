---
title: "Explainable Human-AI Interaction: A Planning Perspective（可解释人机交互：规划视角）"
type: source
tags: [agent-evaluability, explainable-planning, mental-model]
sources: [explainable-human-ai-interaction]
source_file: raw/papers/explainable-human-ai-interaction.pdf
last_updated: 2026-06-29
arxiv_id: "2405.15804"
authors: ["Sarath Sreedharan", "Anagha Kulkarni", "Subbarao Kambhampati"]
year: 2024
venue: "Morgan & Claypool Publishers"
citation_count: 0
citation_count_note: "S2 reports 0; as a 2024 monograph, citation count undercounted on S2"
doi: "10.48550/arXiv.2405.15804"
---

## 概要

本书从规划视角系统论述人机交互中的可解释性，提出"解释即规划"思想：AI agent 不仅要基于自身世界模型规划，还必须考虑回路中人类的心智模型（mental model），利用这些心智模型要么顺应人类期望、要么通过解释性通信改变人类期望。书中也指出同样的心智模型可用于混淆与欺骗。

## 关键贡献

- 系统提出"解释即规划"范式：向人解释的过程本身可建模为一个规划问题。
- 强调 agent 解释必须对齐回路中人类的心智模型，而非仅基于自身模型生成解释。
- 区分"顺应人类期望"与"通过解释性通信改变人类期望"两种解释策略；并讨论心智模型用于欺骗的反面。

## 关键引用

> "AI agents need to go beyond planning with their own models of the world, and take into account the mental model of the human in the loop" — 心智模型对齐主张

> "the AI agent can use these mental models to either conform to human expectations, or change those expectations through explanatory communication" — 解释性通信的双向作用

## 关联

- [[AgentExplainability]] — 本书是 Agent 可解释性方向的直接理论来源，定义"解释即规划"范式
- [[ExplainablePlanning]] — 本书系统阐述可解释规划，是该概念的核心来源
- [[IntentUnderstanding]] — "顺应/改变人类期望"与意图理解—意图共创的上游概念相关

## 矛盾

- citation_count 在 Semantic Scholar 上为 0，因本书为 2024 年专著（monograph），S2 对书籍的引用统计普遍偏低，不代表实际影响力。
