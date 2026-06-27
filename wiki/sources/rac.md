---
title: "RAC：检索增强的语料锚定澄清问题生成"
type: source
tags: [memory-intent-clarification, RAG, conversational-search]
sources: [rac]
source_file: raw/papers/rac.pdf
last_updated: 2026-06-27
arxiv_id: "2601.11722"
authors: ["Ahmed Rayane Kebir", "Vincent Guigue", "Lynda Said Lhadj", "Laure Soulier"]
year: 2026
venue: "ECIR 2026"
citation_count: null
doi: "10.48550/arXiv.2601.11722"
---

## 概要
RAC（Retrieval-Augmented Clarification）提出用检索增强生成框架解决对话式搜索中的模糊意图澄清问题。核心洞察是：澄清问题必须锚定在底层语料库中，否则系统会问出语料无法回答的问题。RAC 先比较多种索引策略进行检索，再微调 LLM 利用检索上下文生成证据支撑的澄清问题，最后通过对比偏好优化（contrastive preference optimization）偏向有检索段支撑的问题。在 4 个基准上显著超越基线。

## 关键贡献
- 语料锚定（corpus-faithful）澄清问题生成框架——首次系统解决"澄清问题脱离语料"问题
- 对比偏好优化使模型偏向有证据支撑的澄清问题，而非无据的流畅问题
- 引入 NLI 和 data-to-text 衍生的新指标评估问题与上下文的锚定程度

## 关键引用
> "Without such grounding, systems risk asking questions that cannot be answered from the available documents." — 核心动机

## 关联
- [[RetrievalAugmentedClarification]] — RAC 是 RAG 增强澄清的代表性方法
- [[IntentSimUncertainty]] — RAC 的检索定位不确定性与 intent-sim 的意图熵互补
- [[ConformalIntentClarification]] — RAC 关注问题质量（锚定），CICC 关注问题时机（不确定度）
- [[StructuredUncertaintyClarification]] — SAGE-Agent 的 EVPI 量化与 RAC 的检索锚定代表两种互补路径

## 矛盾
- 与 [[IntentSimUncertainty]] 方向不同：intent-sim 在意图空间判断何时澄清，RAC 在语料空间判断澄清问题是否可答
