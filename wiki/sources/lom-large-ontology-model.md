---
title: "LOM: 面向企业知识管理的大本体模型"
type: source
tags: [ontology-qa, enterprise-km, ontology-modeling, ontology-reasoning]
sources: [lom-large-ontology-model]
source_file: raw/papers/lom-large-ontology-model.pdf
last_updated: 2026-07-07
arxiv_id: "2602.00029"
authors: ["Yao Zhang", "Hongyin Zhu"]
year: 2026
venue: ""
citation_count: 0
doi: ""
---

## 概要
提出统一 construct-align-reason 框架——大本体模型（LOM）。从结构化数据库和非结构化文本构建双层企业本体，融合为综合企业本体。通过三阶段训练管线（本体指令微调→文本-本体接地→多任务指令调优）实现指令对齐推理。4B 参数 LOM 在复杂图推理上达到 89.47% 准确率，超越 DeepSeek-V3.2。

## 关键贡献
- 构建双层企业本体：结构化数据库层 + 非结构化文本层，融合为综合本体
- 提出三阶段训练管线：本体指令微调（结构理解）→文本-本体接地（节点语义编码）→多任务课程学习（语义推理）
- 4B 参数模型在复杂图推理上超越 DeepSeek-V3.2

## 关键引用
> "We first build a dual-layer enterprise ontology from structured databases and unstructured text, subsequently fusing these sources into a comprehensive enterprise ontology." — 双层本体构建

## 五维分析

### 本体建模
**双层企业本体**是核心创新：结构化数据库层提供严格的表结构和外键关系，非结构化文本层提供灵活的语义描述和隐式关系。两层融合为综合本体，兼顾结构化精确性和非结构化丰富性。本体涵盖企业实体类型、关系层次和推理规则，是完整的企业级本体工程。

### 用户输入实体抽取
通过**本体指令微调**训练 LLM 理解本体结构，使其能从用户查询中识别实体类型和关系。多任务指令调优阶段，模型学习从自然语言映射到本体查询操作（如子图匹配、路径推理）。

### 实体链接
通过**文本-本体接地**（text-ontology grounding）训练阶段实现：将自然语言文本中的实体描述映射到本体中的节点，强化节点语义编码。这使得 LLM 能将用户查询中的实体表述链接到本体中的精确实体。

### 本体推理
核心推理是**多任务指令调优后的语义推理**：模型在课程学习阶段逐步学习从简单到复杂的本体推理任务。复杂图推理包括多跳路径推理、子图模式匹配、跨类型关系推断等。89.47% 准确率超越 DeepSeek-V3.2 证明了本体结构+语言模型融合的有效性。

### 任务完成
任务目标是企业知识管理中的复杂问答。LOM 通过本体结构理解和语义推理能力的融合，在复杂图推理任务上取得 SOTA。本体提供了可推理的结构化知识基础，语言模型提供了自然语言理解和生成能力。

## 关联
- [[LargeOntologyModel]] — 大本体模型范式
- [[DualLayerOntology]] — 双层本体构建
- [[ORACLE]] — 动态本体+推理链
- [[KGPolicyCompliance]] — KG+本体政策推理
- [[NeuroSymbolicOntology]] — 神符号本体（已有wiki）

## 矛盾
- 无
