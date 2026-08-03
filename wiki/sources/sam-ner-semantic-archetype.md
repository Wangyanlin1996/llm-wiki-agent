---
title: "SAM-NER: 语义原型中介零样本NER (Semantic Archetype Mediation)"
type: source
tags: [ontology-semantic-grounding]
sources: [sam-ner-semantic-archetype]
source_file: raw/papers/sam-ner-semantic-archetype.pdf
last_updated: 2026-08-03
arxiv_id: "2605.03706"
authors: ["Ruichu Cai", "Juntao Gan", "Miao Mai", "Zhifeng Hao", "Boyan Xu"]
year: 2026
venue: "ACL 2026 Findings"
citation_count: 0
doi: "10.18653/v1/2026.findings-acl.2050"
---

## 概要

本文提出 SAM-NER，一个基于语义原型中介（Semantic Archetype Mediation）的三阶段框架，用于零样本命名实体识别（ZS-NER）。通过中间的、领域不变的原型空间稳定跨域迁移。当未见标签定义与 LLM 内在语义组织不对齐时，直接映射实体到细粒度目标标签会导致系统性语义漂移。

## 解决的问题

零样本 NER 在领域和 schema 迁移下表现脆弱。未见标签定义常与 LLM 内在语义组织不对齐，直接映射实体到细粒度目标标签引发系统性语义漂移，尤其在目标 schema 新颖或语义重叠时。

## 方法与技术

1. **实体发现（Entity Discovery）**：协同提取+共识去噪获取高覆盖、高保真实体跨度
2. **抽象中介（Abstract Mediation）**：将实体投影到从高层本体抽象蒸馏的通用语义原型空间
3. **语义校准（Semantic Calibration）**：通过约束的、定义对齐的推理将原型预测解析到目标域类型
4. **冻结 LLM 推理**：使用冻结 LLM 进行定义对齐推理，无需微调

## 创新点

- 引入中间原型空间作为语义对齐中介，而非直接从源域到目标域映射
- 从高层本体抽象蒸馏领域不变的原型空间
- 三阶段解耦设计：发现→中介→校准，每阶段可独立优化

## 效果

- 在 CrossNER 基准上一致超越强 ZS-NER 基线
- 跨域设置下显著改善
- ACL 2026 Findings 录用

## 关键引用

> "unseen label definitions often misalign with a large language model's (LLM's) intrinsic semantic organization" — 指出标签定义与 LLM 内在语义不对齐问题

## 关联

- [[OntologySemanticGrounding]] — 本体抽象作为语义中介空间
- [[OntologyIntentAlignment]] — 语义原型实现源-目标对齐
- [[LLMKGOntologySynergy]] — LLM 与本体抽象协同
- [[SemanticIntentSimilarity]] — 语义邻近度度量
