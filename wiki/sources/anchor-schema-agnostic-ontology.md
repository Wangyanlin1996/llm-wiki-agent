---
title: "ANCHOR: 混合本体发现的无schema依赖KG构建 (Schema-Agnostic Ontology Discovery)"
type: source
tags: [ontology-matching-alignment]
sources: [anchor-schema-agnostic-ontology]
source_file: raw/papers/anchor-schema-agnostic-ontology.pdf
last_updated: 2026-08-03
arxiv_id: "2606.01208"
authors: ["Seonwoo Kim", "Jinwoo Kim", "Daegyu Kang", "Daeseong Kim", "Insup Lee"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

本文提出 ANCHOR，一个无 schema 依赖的网络威胁情报（CTI）知识图谱构建系统，桥接 LLM 和形式本体 schema。核心是混合本体发现——一种搜索-导航机制动态探索大规模本体 schema，配合 SHACL 验证强制 schema 合规的类型分配。实验在 UCO、STIX 和 MALOnt 三种 schema 上验证，本地 LLM 接近企业 LLM 性能，实现隐私保护的 CTI 分析。

## 解决的问题

现有本体对齐 CTI 提取面临三大挑战：(1) schema 特定管线需在 schema 变化时手工重配；(2) 基于提示的 schema 包含在大本体（如 UCO）上无法扩展；(3) 依赖企业 LLM API 与敏感内部事件数据的隐私约束冲突。

## 方法与技术

1. **混合本体发现**：搜索-导航机制动态探索大规模本体 schema
2. **SHACL 验证**：强制 schema 合规的类型分配
3. **无 schema 依赖**：同一管线适配 UCO/STIX/MALOnt 三种 schema
4. **本地 LLM 支持**：本地 LLM 接近企业 LLM 性能，支持隐私保护

## 创新点

- 搜索-导航机制替代 prompt 包含整个 schema，解决大本体扩展性问题
- SHACL 验证确保类型分配的 schema 合规性
- 本地 LLM 达到企业 LLM 性能，支持隐私敏感场景部署
- 单管线适配多种本体 schema，无需手工重配

## 效果

- 在 UCO、STIX、MALOnt 三种 schema 上超越现有基线
- 本体类型和 schema 合规性显著提升
- 本地 LLM 接近企业 LLM 性能
- 实现隐私保护的高保真 CTI 分析

## 关键引用

> "prompt-based schema inclusion that fails to scale on large ontologies such as UCO" — 指出 prompt 包含大本体的扩展性瓶颈

## 关联

- [[OntologyMatching]] — 混合本体发现用于 schema 对齐
- [[OntologySemanticLayer]] — 本体 schema 作为语义约束层
- [[LLMKGOntologySynergy]] — LLM 与形式本体 schema 桥接
- [[OntologyReasoning]] — SHACL 验证属于本体推理
