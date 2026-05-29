---
title: "NeuroSymbolicOntology"
type: concept
tags: [neuro-symbolic, ontology, intent-understanding, NLU]
sources: [noemmma]
last_updated: 2026-05-29
---

# NeuroSymbolicOntology

神经符号本体注入框架（Neuro-Symbolic Ontology-Enhanced Method），将结构化意图 Ontology 的符号知识嵌入神经语言模型的输入与输出表示中，实现小型 LLM 的高效多意图理解。

## 核心机制

三层注入策略：
- **Retrieval-Augmented Prompting** — 在输入端通过检索增强注入 Ontology 结构信息
- **Logit Biasing** — 在输出端通过 logits 偏置引导模型朝 Ontology 对齐的意图空间生成
- **可选分类头** — 在模型顶部添加基于 Ontology 结构的分类层

## 评测指标

[[SemanticIntentSimilarity]] (SIS) — 基于层次 Ontology 深度的评测指标，捕捉语义邻近度而非词表匹配。

## 关键结果

3B Llama + Ontology 增强在 MultiWOZ 2.3 歧义对话子集上达到 GPT-4 的 85%（vs 90%），能耗与内存仅为极小比例。

## 关联
- [[IntentUnderstanding]] — 神符号本体是意图理解的符号增强方法
- [[IntentSignalTheory]] — I*→P 信息损失可通过符号结构部分补偿
- [[IntentGrasp]] — IFT fine-tuning 与 Ontology 注入的对比策略