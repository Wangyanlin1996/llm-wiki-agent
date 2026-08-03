---
title: "RAG增强意图推理用于应用-网络交互 (RAG-Enabled Intent Reasoning)"
type: source
tags: [ontology-intent-alignment]
sources: [rag-intent-reasoning-network]
source_file: raw/papers/rag-intent-reasoning-network.pdf
last_updated: 2026-08-03
arxiv_id: "2505.09339"
authors: ["Salwa Mostafa", "Mohamed K. Abdel-Aziz", "Mohammed S. Elbamby", "Mehdi Bennis"]
year: 2025
venue: "EuCNC/6G Summit 2026"
citation_count: 3
doi: "10.1109/EuCNC/6GSummit68295.2026.11577380"
---

## 概要

本文提出一个上下文感知 AI 框架，利用机器推理（MR）、检索增强生成（RAG）和生成式 AI 技术来解释来自不同应用的意图并生成结构化网络意图。该框架支持通用/领域特定意图表达，克服了 LLM 和 vanilla-RAG 框架在意图翻译中的缺陷，指出为每个应用创建语义语言（即基于本体的语言）缺乏技术专长且不可扩展。

## 解决的问题

意图驱动网络（IBN）要求网络以用户语言沟通而非要求用户理解技术语言。不同应用各有专门需求和领域语言，为每个应用创建基于本体的语义语言缺乏技术专长且不可扩展。LLM 直接翻译意图存在幻觉和准确性问题，vanilla-RAG 也无法满足意图翻译需求。

## 方法与技术

1. **机器推理（MR）**：结合领域知识进行意图推理
2. **检索增强生成（RAG）**：检索相关上下文增强意图翻译
3. **生成式 AI**：生成结构化网络意图
4. **上下文感知框架**：支持通用和领域特定的意图表达

## 创新点

- 指出为每个应用构建本体语言不可扩展，提出用 MR+RAG 替代手工本体对齐
- 将机器推理与 RAG 结合，克服各自独立使用时的缺陷
- 支持通用/领域特定意图表达的灵活切换

## 效果

- 意图翻译性能超越 LLM 和 vanilla-RAG 框架
- 在应用-网络交互场景中验证有效性
- 为可扩展的意图驱动网络提供实用路径

## 关键引用

> "Creating semantic languages (i.e., ontology-based languages) and associating them with each application to facilitate intent translation lacks technical expertise and is neither practical nor scalable." — 指出手工本体对齐的不可扩展性

## 关联

- [[IntentUnderstanding]] — 意图推理与翻译
- [[OntologySemanticLayer]] — 本体语言用于意图表达的局限
- [[RetrievalAugmentedGeneration]] — RAG 增强意图理解
- [[IntentDrivenMnS]] — 3GPP 意图驱动管理服务
- [[intent-6g-orchestration]] — 同为意图驱动 6G 编排，但后者使用 TMF 本体+SHACL
