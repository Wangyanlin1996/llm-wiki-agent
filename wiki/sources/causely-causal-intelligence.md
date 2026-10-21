---
title: "Causely: 本体表示驱动的因果智能层提升SRE工作流"
type: source
tags: [semantic-layer, llm-agent-ontology]
sources: [causely-causal-intelligence]
source_file: raw/papers/causely-causal-intelligence.pdf
last_updated: 2026-07-25
arxiv_id: "2605.18327"
authors: ["Dhairya Dalal", "Endre Sara", "Ben Yemini", "Christine Miller", "Shmuel Kliger"]
year: 2026
venue: ""
citation_count: 0
---

## 概要
部署到 SRE 工作流的 AI agent 目前从查询时原始可观测性遥测理解环境状态，付出 token、延迟和推理可靠性的语义解释税。Causely 提出因果智能层，维护环境拓扑、属性依赖和因果关系的结构化表示，锚定到管理环境的本体表示。Causely 将原始遥测转化为实时可查询模型，提供 AI agent 安全诊断、评估影响和行动所需的语义和因果基础。在 24 微服务 OpenTelemetry demo 应用中进行受控故障注入基准研究。

## 关键贡献
- 因果智能层：环境拓扑+属性依赖+因果关系 → 本体表示
- 原始遥测 → 实时可查询语义模型
- MTTD 降低 63%，token 消耗降低 60%，工具调用降低 78%
- 调查足迹压缩 4.8x，API 成本降低 57%
- 根因诊断准确率从 75% 提升到 100%

## 关键引用
> "Causely transforms raw telemetry into a live, queryable model providing the semantic and causal foundation AI agents require to diagnose, evaluate impact, and act safely in production."

## 关联
- [[OntologySemanticLayer]] — 本体语义层
- [[umodel-observability]] — 统一本体框架重塑可观测性
- [[semantic-training-gap]] — 本体嵌入工具层消除语义鸿沟
- [[CausalExplanation]] — 因果解释

## 矛盾
- 无
