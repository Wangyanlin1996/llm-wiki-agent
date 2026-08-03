---
title: "TreeRec: 本体语义树引导意图驱动制品推荐"
type: source
tags: [ontology-intent-alignment]
sources: [treerec-intent-artifacts]
source_file: raw/papers/treerec-intent-artifacts.pdf
last_updated: 2026-08-03
arxiv_id: "2511.18343"
authors: ["Dongming Jin", "Zhi Jin", "Xiaohong Chen", "Zheng Fang", "Linyu Li", "Yuanpeng He", "Jia Li", "Yirang Zhang", "Yingtao Fang"]
year: 2025
venue: "arXiv"
citation_count: 0
doi: "10.48550/arXiv.2511.18343"
---

## 概要

本文研究开源软件生态中意图驱动的可复用制品推荐。构建了 IntentRecBench 基准覆盖三个代表性开源生态，系统比较了 5 个 LLM 和 6 个传统方法。发现 LLM 虽优于传统方法但精度低且推理成本高，因此提出 TreeRec——受软件工程本体语义组织启发的特征树引导推荐框架，通过 LLM 语义抽象将制品组织为层次语义树，实现意图与功能的对齐。

## 解决的问题

开源开发中大量可复用制品使开发者难以找到满足需求的制品。现有检索和学习方法自动化程度不足，LLM 虽能理解意图和执行语义对齐，但在大候选空间中精度低、推理成本高。核心问题是如何在保持 LLM 语义理解优势的同时降低候选空间、提升精度。

## 方法与技术

1. **IntentRecBench 基准构建**：覆盖三个代表性开源生态的意图驱动制品推荐基准
2. **系统比较**：5 个 LLM + 6 个传统方法的精度和效率全面对比
3. **TreeRec 框架**：受本体语义组织启发，使用 LLM 语义抽象将制品组织为层次语义树
4. **层次化推荐**：在语义树上执行意图-功能对齐，缩小推理空间

## 创新点

- 将软件工程中的本体语义组织思想迁移到 LLM 制品推荐，用层次语义树替代扁平候选空间
- TreeRec 框架与具体 LLM 解耦，具有跨模型泛化能力
- 首个意图驱动制品推荐基准 IntentRecBench

## 效果

- TreeRec 在多个生态中一致提升各 LLM 性能
- 证明跨生态的泛化能力和实际部署潜力
- LLM 超越传统方法，但 TreeRec 进一步解决了精度低和成本高问题

## 关键引用

> "LLMs have shown the potential to understand intentions, perform semantic alignment, and recommend usable artifacts." — 强调 LLM 意图理解和语义对齐能力

## 关联

- [[OntologyIntentAlignment]] — 本体语义树实现意图-功能对齐
- [[IntentUnderstanding]] — LLM 意图理解用于制品推荐
- [[DynamicOntologyConstruction]] — LLM 自动构建层次语义结构
- [[OntologySemanticLayer]] — 语义树作为制品组织的语义层
