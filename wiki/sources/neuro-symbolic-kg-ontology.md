---
title: "Better Later Than Sooner: 本体引导的后提取纠错构建神经符号知识图谱"
type: source
tags: [ontology-qa, kg-construction, neuro-symbolic, ontology-reasoning]
sources: [neuro-symbolic-kg-ontology]
source_file: raw/papers/neuro-symbolic-kg-ontology.pdf
last_updated: 2026-07-07
arxiv_id: "2605.29168"
authors: ["Lorenzo Loconte", "Timothy Hospedales", "Cristina Cornelio"]
year: 2026
venue: ""
citation_count: 0
doi: ""
---

## 概要
提出一种本体引导的神经符号知识图谱构建框架，结合开放域抽取、基于嵌入的类型和谓词规范化、以及针对性的 LLM 本体违规纠错。通过将纠错推迟到后提取阶段，避免重复 LLM 调用，大幅减少 token 消耗，同时提升 KG 一致性并保持下游 QA 质量。最终展示提取的 KG 适合符号查询（SPARQL）。

## 关键贡献
- 提出"后提取纠错"策略：不在抽取阶段强制本体约束，而是在抽取完成后统一纠错，减少 LLM 调用
- 基于嵌入的类型和谓词规范化（canonicalization），统一同义实体和关系
- 验证提取的 KG 适合 SPARQL 符号查询，测量图模式出现频率

## 关键引用
> "By deferring corrections to a post-extraction stage, our method avoids repeated LLM calls, substantially reducing token usage while improving KG consistency and preserving downstream QA quality." — 核心设计理念

## 五维分析

### 本体建模
使用**通用常识本体约束**（commonsense ontology constraints）作为 KG 一致性的验证基准。本体定义了实体类型间的合法关系（如"人"不能"位于""抽象概念"）。框架本身不构建新本体，而是用已有本体约束检测和纠错抽取结果中的违规。

### 用户输入实体抽取
从文档中**开放域抽取**实体和关系三元组。使用 LLM 进行初始抽取，不做本体约束——刻意允许抽取阶段产生可能的违规，留待后提取阶段统一处理。这是一种"先抽取后约束"的策略。

### 实体链接
通过**基于嵌入的规范化**（embedding-based canonicalization）实现实体链接：将抽取的类型和谓词映射到嵌入空间，聚类同义表达，统一指代同一本体概念的不同表面形式。这是实体链接的嵌入方法，而非传统的 mention-to-KG 链接。

### 本体推理
核心推理是**本体违规检测与纠错**：检查抽取的 KG 三元组是否违反本体约束（如类型不兼容的关系），然后针对性地用 LLM 纠正违规三元组。纠错是"外科手术式"的——只修改违规部分，保留正确部分。最终用 SPARQL 验证 KG 的符号可查询性。

### 任务完成
任务目标是构建可用于符号查询的高质量 KG。通过后提取纠错减少 token 消耗、提升 KG 一致性，同时保持下游 QA 质量。SPARQL 图模式分析验证了 KG 的符号查询适用性。

## 关联
- [[OntologyGroundedKGConstruction]] — 本体引导KG构建
- [[PostExtractionCorrection]] — 后提取纠错策略
- [[EmbeddingCanonicalization]] — 嵌入规范化实体链接
- [[OMD-GraphRAG]] — 本体引导提取（已有wiki）
- [[LOM]] — 大本体模型

## 矛盾
- 无
