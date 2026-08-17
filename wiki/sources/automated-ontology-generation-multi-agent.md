---
title: "自动本体生成: 多Agent LLM从非结构化文本构建形式本体"
type: source
tags: [ontology-graph-retrieval]
sources: [automated-ontology-generation-multi-agent]
source_file: raw/papers/automated-ontology-generation-multi-agent.pdf
last_updated: 2026-08-17
arxiv_id: "2604.23090"
authors: ["Abid Talukder", "Maruf Ahmed Mridul", "Oshani Seneviratne"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

本文通过对照实验研究多 agent LLM 从非结构化自然语言生成形式本体的架构设计选择。以保险合同为领域，首先建立单 agent LLM 基线并识别关键失败模式（关系提取差、类层次混乱），然后设计多 agent 架构解决这些问题——揭示哪些设计选择驱动生成质量以及现有方法为何失败。

## 解决的问题

从非结构化文本自动生成形式本体是知识工程的核心挑战。LLM 展现潜力，但不清楚哪些架构设计选择驱动生成质量，以及现有方法为何失败。

## 方法与技术

1. **单 agent 基线**：建立单 agent LLM 本体生成基线
2. **失败模式分析**：识别关系提取差、类层次混乱等关键失败
3. **多 agent 架构**：设计分工 agent 解决单 agent 失败
4. **对照实验**：保险合同领域的受控实验设计

## 创新点

- 系统性识别单 agent 本体生成的失败模式
- 多 agent 分工架构针对性解决每个失败
- 领域特定（保险合同）的实证验证

## 关键引用

> "it remains unclear which architectural design choices drive generation quality and why current approaches fail" — 研究动机

## 关联

- [[OntologyGraphRetrieval]] — 本体生成是输入→本体图管线的前端
- [[anchor-schema-agnostic-ontology]] — ANCHOR 本体发现，多 agent 本体生成
- [[auto-ontology-construction-llm]] — 自动本体构建的多 agent 变体
- [[teqodo-tod-ontology]] — TeQoDO LLM 自主构建本体，互补方向
