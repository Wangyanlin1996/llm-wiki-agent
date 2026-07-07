---
title: "TeQoDO: Text-to-SQL任务型对话本体构建"
type: source
tags: [task-oriented-dialogue, ontology-construction, dst, task-completion]
sources: [teqodo-tod-ontology]
source_file: raw/papers/teqodo-tod-ontology.pdf
last_updated: 2026-07-07
arxiv_id: "2507.23358"
authors: ["Renato Vukovic", "Carel van Niekerk", "Michael Heck", "Benjamin Ruppik", "Hsien-Chin Lin", "Shutong Feng", "Nurul Lubis", "Milica Gasic"]
year: 2025
venue: "TACL"
citation_count: 0
doi: ""
---

## 概要
TeQoDO 提出一种 LLM 自主从零构建任务型对话（TOD）本体的方法。LLM 仅利用其固有的 SQL 编程能力结合模块化 TOD 系统概念（通过 prompt 提供），从数据库自动构建 TOD 本体。TeQoDO 超越迁移学习方法，其构建的本体在下游对话状态追踪（DST）任务上具有竞争力，并可扩展到更大型本体。

## 关键贡献
- LLM 自主从零构建 TOD 本体：仅用 SQL 编程能力 + 模块化 TOD 概念
- 超越迁移学习方法：证明 SQL 能力可迁移到本体构建
- 可扩展到大型本体：在 Wikipedia 和 arXiv 数据集上验证

## 关键引用
> "an LLM autonomously builds a TOD ontology from scratch using only its inherent SQL programming capabilities combined with concepts from modular TOD systems provided in the prompt." — 核心方法

## 五维分析

### 本体建模
**自动化本体构建**是核心创新：LLM 从数据库 schema 出发，通过 SQL 查询自动推断 TOD 本体——包括意图（intents）、slot 类型、slot 值域和 slot 间关系。模块化 TOD 系统概念（通过 prompt 提供）指导本体结构，确保构建的本体符合 TOD 系统的需求。本体规模可扩展到大型数据集。

### 用户输入实体抽取
本体构建过程中，LLM 从数据库中提取表名、列名、数据类型和外键关系作为本体实体。这些数据库元数据被转化为 TOD 本体中的 slot 和值域定义。

### 实体链接
通过构建的本体实现对话中的实体链接：DST 任务中，用户输入的实体值被映射到本体中定义的 slot。本体的质量直接影响 DST 的实体链接准确率——TeQoDO 构建的本体在 DST 上具有竞争力。

### 本体推理
推理体现为**SQL 到本体的结构推理**：LLM 通过编写 SQL 查询理解数据库的结构语义，然后将这种理解转化为 TOD 本体。SQL 的 JOIN、WHERE、GROUP BY 等操作隐含了实体间的关系，LLM 将这些关系提取为本体 slot 间的依赖和约束。

### 任务完成
任务目标是构建可用于 DST 的 TOD 本体。TeQoDO 本体在下游 DST 任务上具有竞争力，超越迁移学习方法。消融研究证明模块化 TOD 系统概念在 prompt 中的关键作用。可扩展性在 Wikipedia/arXiv 大型数据集上验证。

## 关联
- [[AutomatedOntologyConstruction]] — 自动本体构建
- [[DialogueOntologyRelationExtraction]] — 对话本体关系抽取
- [[OPAL]] — 本体感知预训练TOD
- [[BeyondOntologyDST]] — 无本体DST
- [[ZeroShotOpenVocabDST]] — 零样本开放词汇DST

## 矛盾
- 与 [[BeyondOntologyDST]] 存在张力：TeQoDO 证明本体构建的价值，Beyond Ontology 主张无预定义本体也可达 SOTA
