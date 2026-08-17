---
title: "本体引导去重感知KG构建: 文档流→验证知识图谱"
type: source
tags: [ontology-graph-retrieval]
sources: [ontology-dedup-kg-construction]
source_file: raw/papers/ontology-dedup-kg-construction.pdf
last_updated: 2026-08-17
arxiv_id: "2607.28662"
authors: ["Vaibhav Dangaich", "Kevin Lewis", "Kundeshwar Pundalik"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

本文提出一个生产级提取层，将实时文档流转换为对齐到形式本体的验证知识图谱。系统解决 LLM 提取的不一致性问题：类型词汇跨文档碎片化、同一人多种名称变体、关系重复、同名不同人被静默混淆。本体引导的去重和类型规范化确保 KG 质量。

## 解决的问题

LLM 从非结构化文档提取实体/关系流畅但不一致：类型词汇跨文档碎片化、同名实体重复、同名不同人混淆——导致 KG 质量不可靠。

## 方法与技术

1. **本体引导类型规范化**：用形式本体定义的类/关系规范提取结果类型
2. **去重感知提取**：检测并合并跨文档的重复实体/关系
3. **实体消歧**：区分同名不同人，合并同人不同名
4. **生产级提取层**：处理实时文档流，持续维护 KG

## 创新点

- 本体引导去重解决 LLM 提取的不一致性
- 类型规范化统一跨文档碎片化词汇
- 生产级实时文档流处理

## 关键引用

> "type vocabularies fracture across documents, the same person surfaces under several name variants, relationships duplicate, and distinct individuals who share a name risk silent conflation" — LLM 提取的四大不一致性

## 关联

- [[OntologyGraphRetrieval]] — 本体引导 KG 构建为精准检索提供高质量图谱
- [[anchor-schema-agnostic-ontology]] — ANCHOR 同为输入→本体图 KG 构建
- [[cortex-ontological-corpus-graph]] — CORTEX 本体语料图，互补方向
- [[auto-ontology-construction-llm]] — 自动本体构建+验证管线
