---
title: "Intent-Driven Smart Manufacturing (本体对齐意图驱动智能制造)"
type: source
tags: [ontology-intent-alignment]
sources: [intent-driven-smart-manufacturing]
source_file: raw/papers/intent-driven-smart-manufacturing.pdf
last_updated: 2026-08-03
arxiv_id: "2602.12419"
authors: ["Takoua Jradi", "John Violos", "Dimitrios Spatharakis", "Lydia Mavraidi", "Ioannis Dimolitsas", "Aris Leivadeas", "Symeon Papavassiliou"]
year: 2025
venue: "IEEE ICKG 2025"
citation_count: 1
doi: "10.1109/ICKG66886.2025.00028"
---

## 概要

本文提出一个统一框架，将指令微调的 LLM 与本体对齐的知识图谱（KG）集成，用于 Manufacturing-as-a-Service（MaaS）生态系统中的意图驱动交互。通过在领域特定数据集上微调 Mistral-7B-Instruct-V02，将自然语言意图翻译为结构化 JSON 需求模型，并语义映射到基于 ISA-95 标准的 Neo4j 知识图谱，确保与制造流程、资源和约束的操作对齐。

## 解决的问题

智能制造环境的复杂性要求界面能将高层人类意图翻译为机器可执行操作。传统方法缺乏语义对齐机制，无法将自然语言意图精确映射到制造资源和流程约束。核心挑战是：如何在保证操作语义一致性的前提下，实现从自然语言到结构化制造需求的端到端翻译。

## 方法与技术

1. **LLM 指令微调**：在领域特定数据集上微调 Mistral-7B-Instruct-V02，训练其将自然语言意图翻译为结构化 JSON 需求模型
2. **本体对齐知识图谱**：构建基于 ISA-95 标准的 Neo4j 知识图谱，表示制造流程、资源和约束
3. **语义映射**：将 LLM 生成的 JSON 需求模型语义映射到 KG 节点，确保操作对齐
4. **Zero-shot 与 few-shot 对比基线**：与 zero-shot 和 3-shot 基线对比验证微调效果

## 创新点

- 将 LLM 意图翻译能力与本体对齐 KG 深度集成，而非仅用 LLM 或仅用 KG
- 采用 ISA-95 工业标准作为本体基础，确保与实际制造系统的操作兼容性
- 端到端从自然语言到 KG 节点的语义映射管线，实现可解释的人机交互

## 效果

- 精确匹配准确率（Exact Match）：**89.33%**
- 总体准确率：**97.27%**
- 显著优于 zero-shot 和 3-shot 基线
- 为可扩展、可解释、自适应的人机交互奠定基础

## 关键引用

> "This work lays the foundation for scalable, explainable, and adaptive human-machine" — 论文结尾，强调本体对齐意图翻译的工程价值

## 关联

- [[OntologySemanticLayer]] — ISA-95 本体作为制造域语义层
- [[IntentUnderstanding]] — 自然语言意图到结构化需求的翻译
- [[LLMKGOntologySynergy]] — LLM 与本体对齐 KG 的协同增强
- [[NOEM³A]] — 同为本体增强意图理解，但 NOEM³A 聚焦移动端轻量化
