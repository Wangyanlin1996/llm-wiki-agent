---
title: "CORTEX: 本体语料图实现Web级语料跨域组织 (Ontological Corpus Graph)"
type: source
tags: [ontology-matching-alignment]
sources: [cortex-ontological-corpus-graph]
source_file: raw/papers/cortex-ontological-corpus-graph.pdf
last_updated: 2026-08-03
arxiv_id: "2606.30175"
authors: ["Chengtao Gan", "Xiaoke Guo", "Yushan Zhu", "Zhaoyan Gong", "Zhiqiang Liu", "Songze Li", "Huajun Chen", "Wen Zhang"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

本文提出 CORTEX（CORpus organizaTion through ontological corpus graph），首个将 Web 级语料构建从扁平文档过滤提升到结构化知识组织的框架。核心是本体语料图（OCG）——一个三层异构结构：质量精炼内容层、LLM 驱动自动演化的层次轻量本体层、以及支持任意分类分辨率下跨域关联的跨域对齐层。

## 解决的问题

大语言模型对数据规模和质量需求不断升级，不同训练阶段有不同数据需求。现有语料构建管线将语料限制为扁平、无差别的文档集合，缺乏系统化知识组织。需要一种结构化方法组织高质量语料并支持跨域关联。

## 方法与技术

1. **本体语料图（OCG）**：三层异构结构统一内容/本体/对齐
2. **质量精炼内容层**：质量过滤后的文档内容层
3. **层次轻量本体层**：LLM 驱动自动演化的层次化本体
4. **跨域对齐层**：支持任意分类分辨率下域间关联
5. **CortexBench**：跨域搜索推理基准，在 8 个前沿 LLM 上验证

## 创新点

- 首个将 Web 级语料从扁平过滤提升到结构化知识组织
- 三层 OCG 统一内容质量、本体层次和跨域对齐
- LLM 驱动自动本体演化，无需手工本体设计
- 跨域对齐层支持任意分类分辨率的域间关联

## 效果

- 发布 24.14B token 精炼语料及其 OCG
- CortexBench 在 8 个前沿 LLM 上验证质量精炼、域组织和跨域数据合成的有效性
- 完整代码库开源

## 关键引用

> "existing corpus construction pipelines confine the resulting corpora to flat, undifferentiated document collections, universally lacking systematic knowledge organization" — 指出现有语料构建缺乏知识组织

## 关联

- [[OntologySemanticLayer]] — 三层 OCG 作为语料语义层
- [[OntologyMatching]] — 跨域对齐层实现域间关联
- [[DynamicOntologyConstruction]] — LLM 驱动自动本体演化
- [[LLMKGOntologySynergy]] — LLM 与本体/KG 协同
