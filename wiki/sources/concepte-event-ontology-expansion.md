---
title: "ConceptE: LLM概念化驱动事件本体扩展 (Event Ontology Expansion)"
type: source
tags: [ontology-matching-alignment]
sources: [concepte-event-ontology-expansion]
source_file: raw/papers/concepte-event-ontology-expansion.pdf
last_updated: 2026-08-03
arxiv_id: "2606.21048"
authors: ["Weicheng Ren", "Zixuan Li", "Long Bai", "Xiaolong Jin", "Jiafeng Guo", "Xueqi Cheng"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

本文提出 ConceptE，一个概念化增强的事件本体扩展框架。现有方法通过聚类上下文化触发词表示并将归纳簇附加到本体上，但本体扩展需要概念级语义，而上下文化触发词表示常将这些语义与表面上下文变异混淆。ConceptE 通过 LLM 提示生成简洁概念名称和描述，联合编码与触发词信息构建概念增强表示，实现与本体级推理对齐。

## 解决的问题

事件本体扩展旨在从数据中发现新兴事件类型并扩展到现有本体的适当位置。现有方法聚类上下文化触发词表示，但本体扩展需要概念级语义，触发词表示常将概念语义与表面上下文变异混淆，导致不稳定聚类和不可靠层次扩展。

## 方法与技术

1. **LLM 概念化**：用 LLM 提示句子和事件触发词，生成简洁概念名称和自然语言描述
2. **概念增强表示**：联合编码概念语义与触发词信息
3. **本体级推理对齐**：表示设计与本体级推理对齐
4. **三子任务统一**：事件聚类、层次扩展、类型命名

## 创新点

- 通过 LLM 概念化提取概念级语义，解决触发词表示的语义混淆
- 概念名称+描述联合编码，而非仅依赖触发词嵌入
- 支持本体一致类型命名，而非仅聚类和附加

## 效果

- 在 ACE、ERE、MAVEN 上一致超越 SOTA
- 事件聚类 BCubed-F1 提升达 **12.37%**
- 层次扩展 Taxo_F1 提升达 **6.48%**

## 关键引用

> "ontology expansion requires concept-level semantics that characterize event types, whereas contextualized trigger representations often conflate these semantics with surface contextual variation" — 指出概念级语义与表面变异混淆问题

## 关联

- [[OntologyMatching]] — 概念级语义对齐到本体层次
- [[DynamicOntologyConstruction]] — LLM 驱动本体扩展
- [[LLMKGOntologySynergy]] — LLM 与本体扩展协同
- [[OntologyReasoning]] — 本体级推理对齐
