---
title: "电商意图理解：使用中心视角 (Usage-centric Intent Understanding)"
type: source
tags: [ontology-intent-alignment]
sources: [usage-centric-intent-ecommerce]
source_file: raw/papers/usage-centric-intent-ecommerce.pdf
last_updated: 2026-08-03
arxiv_id: "2402.14901"
authors: ["Wendi Zhou", "Tianyi Li", "Pavlos Vougiouklis", "Mark Steedman", "Jeff Z. Pan"]
year: 2024
venue: "EMNLP 2024"
citation_count: 10
doi: "10.48550/arXiv.2402.14901"
---

## 概要

本文聚焦电商场景中的用户意图理解，将意图定义为"客户如何使用产品"（predicative intent），将意图理解作为独立于产品本体的自然语言推理任务。识别了 SOTA 电商意图知识图谱 FolkScope 的两大弱点——类别刚性和属性模糊，并引入 Product Recovery Benchmark 验证这些弱点。

## 解决的问题

电商意图理解缺乏一致定义和准确基准。现有 SOTA 方法 FolkScope 意图知识图谱存在类别刚性（category-rigidity，无法跨类别推荐有用产品）和属性模糊（property-ambiguity，无法强对齐具有最理想属性的产品）两大弱点，限制了意图与产品的精确对齐。

## 方法与技术

1. **使用中心意图定义**：将意图定义为"客户如何使用产品"的 predicative 意图，作为自然语言推理任务
2. **FolkScope 弱点分析**：系统识别类别刚性和属性模糊两大局限
3. **Product Recovery Benchmark**：构建新颖评估框架和示例数据集
4. **本体无关推理**：意图理解独立于产品本体，避免本体刚性约束

## 创新点

- 重新定义电商意图为使用中心（usage-centric）而非产品中心，摆脱对产品本体的依赖
- 首次系统分析 FolkScope 意图 KG 的结构弱点
- 提出本体无关的意图理解范式，通过自然语言推理实现跨类别对齐

## 效果

- 在 Product Recovery Benchmark 上验证 FolkScope 的类别刚性和属性模糊弱点
- 证明本体刚性约束限制了意图与产品的跨类别对齐能力
- EMNLP 2024 录用，10 次引用

## 关键引用

> "We focus on predicative user intents as 'how a customer uses a product', and pose intent understanding as a natural language reasoning task, independent of product ontologies." — 核心主张：意图理解应独立于产品本体

## 关联

- [[OntologyIntentAlignment]] — 分析本体对齐意图的局限性
- [[IntentUnderstanding]] — 电商场景的意图理解
- [[SemanticIntentSimilarity]] — 意图语义邻近度度量
- [[NOEM³A]] — NOEM³A 用本体增强意图理解，本文反思本体刚性局限
