---
title: "法律时序图检索 (Legal Temporal Graph RAG)"
type: concept
tags: [ontology-graph-retrieval]
sources: [ontology-driven-graph-rag-legal, beyond-probabilistic-rag-limitations]
last_updated: 2026-08-31
---

法律时序图检索是指针对法律规范的 hierarchical、temporal 和 institutional 结构特点，用 ontology-driven graph RAG 实现确定性检索的范式。核心洞察是法律正确性不是 semantic similarity 问题，而是 validity grounding 问题——哪个 norm 在特定日期、特定 hierarchical context 中有效、由什么 institutional act 产生。标准 RAG 的三种 pathology：(1) mereological blindness（未保持 part-whole 结构）、(2) diachronic blindness（未处理历时性演变）、(3) causal opacity（未提供 provenance chain）。SAT-Graph RAG 的四个架构承诺：C1 ontological primacy（primary data objects 是 legal-domain entities 而非 text fragments）、C2 event reification（立法事件是一等 queryable entity）、C3 bitemporal correctness（valid time 和 transaction time 独立可查询）、C4 deterministic interaction protocol（暴露 domain-specific typed primitives）。关键创新是聚合式版本传播（Aggregation, 非 Composition）——复用未变更子组件的已有 CTV，避免数据冗余。相关论文：[[ontology-driven-graph-rag-legal]]（SAT-Graph RAG 实现）、[[beyond-probabilistic-rag-limitations]]（理论分析三种 pathology）。与 [[IntentDrivenMnS]]（3GPP 意图管理）的声明式目标表达跨域共鸣——法律规范的"what/when/how"分离与意图管理的"what vs how"抽象层次呼应。
