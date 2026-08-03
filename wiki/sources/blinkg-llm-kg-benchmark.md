---
title: "BLINKG: LLM集成知识图谱生成基准 (LLM-Integrated KG Generation Benchmark)"
type: source
tags: [ontology-matching-alignment]
sources: [blinkg-llm-kg-benchmark]
source_file: raw/papers/blinkg-llm-kg-benchmark.pdf
last_updated: 2026-08-03
arxiv_id: "2605.19518"
authors: ["Carla Castedo", "Enrique Iglesias", "Manuel Lama", "Alberto Bugarin-Diz", "Maria-Esther Vidal", "David Chaves-Fraga"]
year: 2026
venue: "arXiv"
citation_count: 1
doi: "10.48550/arXiv.2605.19518"
---

## 概要

本文提出 BLINKG，一个评估 LLM 将数据 schema 映射到本体概念能力的基准。KG 生成需识别输入数据源与本体术语间的语义等价，现有声明式方案（RML、SPARQL-Anything）已帮助泛化，但 schema 元素与本体术语对齐仍需复杂转换和大量手工工作。BLINKG 包含基于真实用例的递增复杂度场景，评估多个 SOTA LLM 的映射能力。

## 解决的问题

知识图谱生成是知识工程师最耗时的工作之一，需要识别输入数据源与本体术语间的语义等价。虽有 LLM 辅助自动化 KG 构建，但缺乏标准化框架评估 LLM 建立数据 schema 与本体概念对应关系的能力。

## 方法与技术

1. **递增复杂度场景**：基于真实用例构建从简到复杂的场景集
2. **多 LLM 评估**：广泛评估多个 SOTA LLM 的 schema-本体映射能力
3. **映射能力维度**：评估 LLM 识别数据 schema 元素与本体概念对应关系的能力
4. **需求定义**：定义 (半)自动 LLM 驱动 KG 构建的需求集

## 创新点

- 首个专门评估 LLM schema-本体映射能力的标准化基准
- 递增复杂度场景设计揭示 LLM 能力边界
- 定义 (半)自动 LLM 驱动 KG 构建的需求集，开辟新研究方向

## 效果

- SOTA LLM 在简单场景中提供有前景的方案
- 在复杂场景中性能仍有限
- 为评估 LLM 当前 KG 构建能力提供标准化框架

## 关键引用

> "aligning input schema elements with ontology terms still involves intricate transformations and requires considerable manual effort" — 指出 schema-本体对齐的核心挑战

## 关联

- [[OntologyMatching]] — schema 与本体概念映射属于本体对齐
- [[LLMKGOntologySynergy]] — LLM 与 KG/本体协同
- [[OntologySemanticLayer]] — 本体作为数据 schema 的语义层
- [[DynamicOntologyConstruction]] — LLM 自动化本体相关构建
