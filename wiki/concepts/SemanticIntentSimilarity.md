---
title: "SemanticIntentSimilarity"
type: concept
tags: [SIS, evaluation-metric, ontology, intent-understanding]
sources: [noemmma]
last_updated: 2026-05-29
---

# SemanticIntentSimilarity (SIS)

Semantic Intent Similarity (SIS) 是 NOEM³A 提出的基于层次 Ontology 深度的意图评测指标，用于衡量预测意图与真实意图之间的语义邻近度。

## 核心思想

传统评测指标基于词表匹配（exact match），无法捕捉语义上相近但词表不同的意图。SIS 利用意图 Ontology 的层次结构深度，计算两个意图在 Ontology 树中的路径距离，量化语义邻近度。

## 优势

- 即使预测意图与真实意图在词表层面不同，SIS 仍能反映其语义距离
- 鼓励模型朝语义正确的方向优化，而非仅追求词表精确匹配

## 关联
- [[NeuroSymbolicOntology]] — SIS 是 NeuroSymbolicOntology 框架的配套评测指标
- [[IntentUnderstanding]] — SIS 改善意图理解评测的语义敏感性