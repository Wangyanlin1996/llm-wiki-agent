---
title: "LLM辅助本体工程与法国法律知识图谱构建 (LLM Ontology Engineering + Legal KG)"
type: source
tags: [ontology-matching-alignment]
sources: [llm-ontology-engineering-legal-kg]
source_file: raw/papers/llm-ontology-engineering-legal-kg.pdf
last_updated: 2026-08-03
arxiv_id: "2607.24551"
authors: ["Genesis Montenegro", "Mokhtar Boumedyen Billami", "Catherine Faron", "Fabien Gandon", "Pierre Monnin"]
year: 2026
venue: "SEMANTiCS 2026"
citation_count: 0
---

## 概要

本文提出一个两阶段 LLM 辅助工作流用于法国维护法规：首先从 SEMLEG 核心本体进行本体工程，然后构建本体接地的法国法律知识图谱。第一阶段从分层语料样本中开放提取类型化实体和三元组，通过嵌入融合规范化标签，归纳候选对象属性及其签名。第二阶段使用结果本体指导全语料的三组提取和 RDF 图构建。

## 解决的问题

维护法规是难以针对特定案例利用且难以集成到操作系统的复杂法律文本。需要一种自动化方法从法律文本中构建本体接地知识图谱，同时保证本体工程的质量（类对齐、谓词规范化、签名合规）。

## 方法与技术

1. **两阶段工作流**：本体工程（从样本提取）→ KG 构建（在全语料上提取）
2. **开放提取**：从分层语料样本提取类型化实体和三元组
3. **嵌入融合规范化**：通过 embedding-based fusion 规范化标签
4. **对象属性归纳**：归纳候选对象属性及其签名（domain 和 range）
5. **封闭提取**：用结果本体指导全语料的三元组提取和 RDF 图构建

## 创新点

- 两阶段开放-封闭提取策略：先开放探索归纳本体，再封闭引导全量提取
- 嵌入融合标签规范化减少重复实体和谓词
- 自动归纳对象属性签名（domain/range），而非手工定义

## 效果

- GPT-4.1 和 mistral-large-2512 展现稳健结构化输出
- 类对齐接近完整
- 融合后重复实体和谓词大幅减少
- 不到 20% 三组引入未见属性
- 较低的精确签名合规率揭示现有谓词的新 domain-range 组合

## 关键引用

> "predicate normalization and the validation of newly observed relation signatures as key refinement steps" — 指出谓词规范化和签名验证是工业场景关键精炼步骤

## 关联

- [[OntologyMatching]] — 类对齐和标签规范化属于本体对齐
- [[DynamicOntologyConstruction]] — LLM 自动构建本体
- [[LLMKGOntologySynergy]] — LLM 与本体工程协同
- [[OntologySemanticLayer]] — 本体接地的法律知识图谱
