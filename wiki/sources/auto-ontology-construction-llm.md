---
title: "Automatic Ontology Construction: LLM外部本体记忆层与生成-验证-修正管线"
type: source
tags: [llm-agent-ontology, ontology-construction]
sources: [auto-ontology-construction-llm]
source_file: raw/papers/auto-ontology-construction-llm.pdf
last_updated: 2026-07-25
arxiv_id: "2604.20795"
authors: ["Pavel Salovskii", "Iuliia Gorshkova"]
year: 2026
venue: ""
citation_count: 0
doi: "10.5281/zenodo.19696042"
---

## 概要
本文提出混合智能系统架构，用外部本体记忆层扩展 LLM。系统不依赖参数知识和向量 RAG，而是使用 RDF/OWL 表示构建和维护结构化知识图谱，实现持久、可验证和语义接地的推理。核心贡献是从异构数据源（文档、API、对话日志）自动构建本体的管线：实体识别→关系抽取→规范化→三元组生成→SHACL/OWL 约束验证→持续图谱更新。推理时 LLM 在结合向量检索、图谱推理和外部工具交互的复合上下文上运行。

## 关键贡献
- LLM + 外部本体记忆层架构，RDF/OWL 表示
- 从异构数据源自动构建本体管线：抽取→规范化→验证→更新
- 生成-验证-修正管线，LLM 输出可形式化验证
- Tower of Hanoi 基准：本体增强在多步推理场景中显著提升性能

## 关键引用
> "Instead of relying solely on parametric knowledge and vector-based retrieval (RAG), the proposed approach constructs and maintains a structured knowledge graph using RDF/OWL representations, enabling persistent, verifiable, and semantically grounded reasoning."

## 关联
- [[OntologyConstruction]] — 本体构建与演化
- [[OntologyFirstAgentDesign]] — 本体优先Agent设计方法论
- [[DynamicOntologyConstruction]] — 动态本体构建
- [[ontolearner]] — 首个统一本体学习框架
- [[neurowl]] — LLM增强不完整OWL推理

## 矛盾
- 无
