---
title: "NOEM³A: A Neuro-Symbolic Ontology-Enhanced Method for Multi-Intent Understanding in Mobile Agents"
type: source
tags: [neuro-symbolic, ontology, multi-intent, mobile-agent, intent-disambiguation, NLU]
date: 2025-11-24
source_file: raw/papers/noemmma.md
last_updated: 2026-05-29
---

## 概要
NOEM³A 提出神经符号本体增强的多意图消歧框架，通过 Retrieval-Augmented Prompting、Logit Biasing 和可选分类头三层注入策略，将结构化意图 Ontology 嵌入紧凑语言模型的输入与输出表示。在 MultiWOZ 2.3 的歧义/高难度对话子集上，3B Llama 模型达到 GPT-4 的 85% 准确率（vs 90%），同时提出基于层次 Ontology 深度的 Semantic Intent Similarity (SIS) 评测指标。

## 核心论点
- 符号意图结构注入是小型 LLM 实现高效多意图理解的关键策略，无需依赖大型模型
- 现有评测指标基于词表匹配无法捕捉语义邻近度，SIS 基于 Ontology 深度能更准确衡量意图相似性
- Ontology 增强模型产出更具接地性和消歧性的多意图解释，优于纯神经方法

## 关键引述
> "a 3B Llama model with ontology augmentation approaches GPT-4 accuracy (85% vs 90%) at a tiny fraction of the energy and memory footprint" — 验证符号对齐作为高效 On-Device NLU 策略

> "Semantic Intent Similarity (SIS) based on hierarchical ontology depth, capturing semantic proximity even when predicted intents differ lexically" — SIS 指标设计理念

## 关联
- [[IntentUnderstanding]] — NOEM³A 是意图理解方向的神经符号增强方法
- [[NeuroSymbolicOntology]] — 核心技术框架：神经符号本体注入
- [[IntentGrasp]] — 多意图理解的评测基准对比
- [[IntentSignalTheory]] — I*→P 信息损失与符号结构补偿的关系