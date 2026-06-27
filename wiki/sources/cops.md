---
title: "CoPS：认知记忆驱动的个性化搜索"
type: source
tags: [memory-intent-clarification, cognitive-memory, personalized-search]
sources: [cops]
source_file: raw/papers/cops.pdf
last_updated: 2026-06-27
arxiv_id: "2402.10548"
authors: ["Yujia Zhou", "Qiannan Zhu", "Jiajie Jin", "Zhicheng Dou"]
year: 2024
venue: "WWW 2024"
citation_count: null
doi: "10.48550/arXiv.2402.10548"
---

## 概要
CoPS（Cognitive Personalized Search）将 LLM 与受人类认知启发的记忆机制集成，用于个性化搜索。认知记忆机制包含三层：感觉记忆（快速感知响应）、工作记忆（复杂认知响应）、长期记忆（存储历史交互）。处理新查询时三步走：识别重找行为、用相关历史信息构建用户画像、基于个性化查询意图排序文档。零样本场景下超越基线模型。

## 关键贡献
- 认知三阶记忆架构（感觉/工作/长期）直接用于搜索意图理解——记忆增强意图的典型范式
- 用户画像从历史交互记忆中构建，驱动个性化查询意图排序
- 零样本场景下有效，缓解数据稀疏问题

## 关键引用
> "The cognitive memory mechanism comprises sensory memory for quick sensory responses, working memory for sophisticated cognitive responses, and long-term memory for storing historical interactions." — 认知记忆三层架构

## 关联
- [[CognitiveMemoryMechanism]] — CoPS 首次将认知三阶记忆系统应用于搜索意图
- [[AgentMemory]] — 感觉/工作/长期三层与 LightMem 的 STM/MTM/LTM 形成对应
- [[IntentUnderstanding]] — 用户画像驱动个性化意图是记忆增强意图理解的直接体现
- [[RecursiveIntentMemory]] — CoPS 的历史记忆构建画像与 OnePred 的递归意图记忆互补

## 矛盾
- 与纯检索式记忆（如 [[rac]]）不同：CoPS 强调认知层次化记忆结构，而非平面语料检索
