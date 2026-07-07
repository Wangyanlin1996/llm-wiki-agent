---
title: "NLU++: 任务型对话NLU的多标签细粒度本体数据集"
type: source
tags: [task-oriented-dialogue, nlu, ontology-modeling, entity-extraction, task-completion]
sources: [nlu-plus-plus]
source_file: raw/papers/nlu-plus-plus.pdf
last_updated: 2026-07-07
arxiv_id: "2204.13021"
authors: ["Iñigo Casanueva", "Ivan Vulić", "Georgios P. Spithourakis", "Paweł Budzianowski"]
year: 2022
venue: "NAACL 2022 Findings"
citation_count: 0
doi: ""
---

## 概要
NLU++ 是面向任务型对话 NLU 的新数据集，提供比现有数据集更具挑战性的评估环境。分为 BANKING 和 HOTELS 两个域，提供细粒度域本体、大量多意图句子、intent 模块化（可组合成复杂意图）和更细粒度的 slot 集合。本体分为域特定和通用 intent 模块，促进跨域复用。在当前 SOTA NLU 模型上基准测试，证明数据集的挑战性。

## 关键贡献
- 细粒度域本体：大量多意图句子，intent 模块化设计
- 域特定+通用 intent 模块：促进跨域复用
- 由对话 NLU 专家收集、过滤和标注，高质量数据
- 基准测试证明挑战性，特别是在低数据场景下

## 关键引用
> "NLU++ provides fine-grained domain ontologies with a large set of challenging multi-intent sentences, introducing and validating the idea of intent modules that can be combined into complex intents" — intent模块化设计

## 五维分析

### 本体建模
**细粒度域本体**是核心创新：每个域（BANKING、HOTELS）有细粒度的 intent 和 slot 定义。关键创新是 **intent 模块化**（intent modularisation）——intent 分为域特定模块和通用模块，通用模块可跨域复用（如"确认"intent 在银行和酒店域都适用）。复杂 intent 由模块组合而成。本体设计灵感来自工业 TOD 系统的实际需求。

### 用户输入实体抽取
NLU++ 包含大量**多意图句子**——单个用户输入可能同时表达多个 intent（如"我想预订酒店，顺便问一下取消政策"）。这比传统单 intent 标注更接近真实场景，对实体抽取提出更高要求：需要识别属于不同 intent 的实体。

### 实体链接
细粒度 slot 集合使实体链接更具挑战性：用户输入中的实体需要被链接到更细粒度的 slot（如"king bed"链接到"room-bed-type"而非泛化的"room-preference"）。跨域通用 slot 模块允许同一实体在不同域中被复用。

### 本体推理
推理体现为**intent 模块组合推理**：用户输入可能需要将多个 intent 模块组合成复杂 intent。NLU++ 验证了 intent 模块化的有效性——模型可以学习组合模块，而非为每个复杂 intent 单独训练。

### 任务完成
任务目标是 NLU（intent 分类 + slot filling）的准确性和泛化能力。NLU++ 在低数据场景下特别有挑战性。intent 模块化和跨域复用设计使系统在数据不足时仍能有效工作——这对实际部署中的快速域扩展至关重要。

## 关联
- [[IntentModularisation]] — intent模块化
- [[FineGrainedOntology]] — 细粒度本体
- [[MultiIntentClassification]] — 多意图分类
- [[OPAL]] — 本体感知预训练TOD
- [[DialogueOntologyRelationExtraction]] — 对话本体关系抽取

## 矛盾
- 无
