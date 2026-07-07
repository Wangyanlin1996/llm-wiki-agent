---
title: "处理不一致KG推理: 综述"
type: source
tags: [ontology-survey, kg-reasoning, inconsistency, ontology-reasoning]
sources: [inconsistency-kg-reasoning-survey]
source_file: raw/papers/inconsistency-kg-reasoning-survey.pdf
last_updated: 2026-07-07
arxiv_id: "2502.19023"
authors: ["Anastasios Nentidis", "Charilaos Akasiadis", "Angelos Charalambidis", "Alexander Artikis"]
year: 2025
venue: ""
citation_count: 0
doi: ""
---

## 概要
综述聚焦在不一致知识图谱上如何进行推理。KG 的 schema 通常由特定本体定义，推理是信息检索、问答和新知识推导的必需。但 KG 信息常通过（半）自动从自然语言提取或整合不同语义 schema 的数据集填充，导致不一致。综述分析三个互补方向：(a) 检测不一致部分、(b) 修复不一致 KG、(c) 不一致容忍推理。

## 关键贡献
- 系统综述不一致 KG 推理的三个方向：检测、修复、容忍
- 覆盖本体定义的 schema 推理与自动提取导致的不一致问题
- 讨论持续挑战和未来方向

## 关键引用
> "we focus on how to perform reasoning on inconsistent KGs, by analyzing the state of the art towards three complementary directions: a) the detection of the parts of the KG that cause the inconsistency, b) the fixing of an inconsistent KG to render it consistent, and c) the inconsistency-tolerant reasoning." — 三方向框架

## 五维分析

### 本体建模
综述覆盖**本体定义的 KG schema**：本体（ontologies）定义 KG 的数据 schema，包括概念层次、关系类型和约束规则。不一致问题源于自动提取或 schema 整合——本体约束被违反（如实体类型不兼容的关系被建立）。综述讨论了如何通过本体约束检测不一致。

### 用户输入实体抽取
综述未直接聚焦用户输入实体抽取，但讨论了自动提取（从自然语言）如何引入不一致——提取的实体和关系可能违反本体约束。

### 实体链接
综述讨论了**数据整合导致的不一致实体链接**：当不同数据集遵循不同语义 schema 时，实体链接可能产生冲突（同一实体被链接到不同类型，或不同实体被误链接为同一实体）。检测这些不一致链接是综述的核心方向之一。

### 本体推理
核心内容是**不一致容忍本体推理**：当 KG 包含不一致时，传统本体推理（如描述逻辑推理）可能产生矛盾结论。综述分析了三种策略：(1) 检测不一致部分并隔离；(2) 修复不一致（删除或修改导致不一致的三元组）；(3) 不一致容忍推理（在不一致存在的情况下仍得出有意义结论，如基于矛盾去耦的推理）。

### 任务完成
综述不直接涉及任务完成，但讨论的推理能力是 QA、信息检索和新知识推导的基础——这些是任务执行的核心组件。不一致容忍推理确保 KG 上的任务即使在数据不完美时也能可靠执行。

## 关联
- [[InconsistencyTolerantReasoning]] — 不一致容忍推理
- [[OntologyConstraintViolation]] — 本体约束违规
- [[NeuroSymbolicKGOntology]] — 本体引导KG纠错
- [[LLMKGResearchTrends]] — LLM-KG研究趋势
- [[LOM]] — 大本体模型

## 矛盾
- 无
