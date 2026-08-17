---
title: "可验证知识扩展: 检索增强SLM+形式概念分析(FCA)验证本体构建"
type: source
tags: [ontology-graph-retrieval]
sources: [verifiable-knowledge-expansion-fca]
source_file: raw/papers/verifiable-knowledge-expansion-fca.pdf
last_updated: 2026-08-17
arxiv_id: "2607.01773"
authors: ["Yujin Yang", "Heejung Lee"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

本文提出一种检索增强的小语言模型（SLM）框架，用形式概念分析（Formal Concept Analysis, FCA）作为符号验证循环实现可验证的知识扩展。从种子属性出发，FCA 在增长的形式上下文中提出蕴含，SLM 从文本中检索支撑证据，只有通过 FCA 验证的知识才被接受——解决 LLM 本体构建中输出不受支撑或不一致的问题。

## 解决的问题

本体构建需要决定哪些对象/属性/结构关系应被接受为有效知识。语言模型可以从文本提出结构，但输出可能不受支撑或不一致——缺乏验证机制。

## 方法与技术

1. **检索增强 SLM**：SLM 从文本中检索知识扩展候选
2. **FCA 符号验证循环**：形式概念分析作为符号验证器
3. **种子属性→蕴含→验证**：从种子属性出发，FCA 提出蕴含，SLM 检索证据
4. **可验证扩展**：只有通过 FCA 验证的知识才被接受

## 创新点

- FCA 作为符号验证器为 LLM 本体构建提供形式化保证
- 检索增强 SLM 在验证循环中提供证据支撑
- 只有验证通过的知识被接受，确保本体一致性

## 关键引用

> "uses formal concept analysis (FCA) as a symbolic verification loop for knowledge expansion" — FCA 符号验证循环

## 关联

- [[OntologyGraphRetrieval]] — 可验证本体构建支撑检索质量
- [[anchor-schema-agnostic-ontology]] — ANCHOR SHACL 验证，FCA 验证互补
- [[auto-ontology-construction-llm]] — 自动本体构建的验证增强
- [[OntologyReasoning]] — FCA 属于本体推理
