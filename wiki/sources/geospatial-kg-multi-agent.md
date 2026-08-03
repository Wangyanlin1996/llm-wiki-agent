---
title: "地理空间数据发现：KG驱动多Agent本体语义中介 (Geospatial KG Multi-Agent)"
type: source
tags: [ontology-intent-alignment]
sources: [geospatial-kg-multi-agent]
source_file: raw/papers/geospatial-kg-multi-agent.pdf
last_updated: 2026-08-03
arxiv_id: "2603.20670"
authors: ["Ruixiang Liu", "Zhenlong Li", "Ali Khosravi Kazazi"]
year: 2026
venue: "arXiv"
citation_count: 1
doi: "10.48550/arXiv.2603.20670"
---

## 概要

本文提出一个知识图谱驱动的多 Agent 框架，用于智能地理空间数据发现。框架引入统一地理空间元数据本体作为语义中介层，对齐跨平台异构元数据标准，并构建地理空间元数据知识图谱显式建模数据集及其多维关系。在结构化表示基础上，采用多 Agent 协作架构执行意图解析、知识图谱检索和答案合成，形成从用户查询到结果的可解释闭环发现流程。

## 解决的问题

地理空间数据生态高度分布式、异构且语义不一致。现有数据目录和门户主要依赖关键词搜索，语义支持有限，无法捕获用户意图，导致检索性能弱。核心问题是异构元数据标准间的语义对齐和意图感知的数据发现。

## 方法与技术

1. **统一地理空间元数据本体**：作为语义中介层对齐跨平台异构元数据标准
2. **地理空间元数据知识图谱**：显式建模数据集及其多维关系
3. **多 Agent 协作架构**：执行意图解析 → KG 检索 → 答案合成的闭环流程
4. **可解释发现流程**：从用户查询到结果的端到端可追溯

## 创新点

- 将本体作为语义中介层用于地理空间元数据对齐，而非仅作为词汇表
- 多 Agent 架构将意图解析、KG 检索和答案合成解耦为独立可解释步骤
- 统一了数据发现从关键词匹配到意图感知语义检索的范式转换

## 效果

- 显著提升意图匹配精度、排序质量、召回率和发现透明度
- 对比传统系统在代表性用例中全面改进
- 为下一代智能自主空间数据基础设施提供实践基础

## 关键引用

> "keyword-based search with limited semantic support, which often fails to capture user intent" — 指出现有系统无法捕获用户意图的核心痛点

## 关联

- [[OntologySemanticLayer]] — 统一元数据本体作为语义中介层
- [[IntentUnderstanding]] — 多 Agent 意图解析
- [[OntologyIntentAlignment]] — 本体对齐异构标准实现意图匹配
- [[LLMKGOntologySynergy]] — KG 与多 Agent 协同增强数据发现
