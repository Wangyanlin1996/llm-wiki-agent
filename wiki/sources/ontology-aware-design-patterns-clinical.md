---
title: "Ontology-Aware Design Patterns: 临床AI系统的七种本体感知设计模式"
type: source
tags: [semantic-layer, ontology-reasoning]
sources: [ontology-aware-design-patterns-clinical]
source_file: raw/papers/ontology-aware-design-patterns-clinical.pdf
last_updated: 2026-07-25
arxiv_id: "2604.01661"
authors: ["Florian Odi Stummer"]
year: 2026
venue: ""
citation_count: 0
---

## 概要
临床 AI 系统在结构上被文档工作流、计费激励和术语碎片化扭曲的健康数据上训练。先前工作刻画了扭曲机制：文档执行三力模型、AI 放大编码伪影的物化反馈循环、允许语义漂移积累的术语治理失败。但将这些洞察转化为可实现的软件架构仍是开放问题。本文提出 Gang-of-Four 模式语言中的七种本体感知设计模式，构建对本体扭曲有韧性的临床 AI 管线。

## 关键贡献
- 七种本体感知设计模式（Gang-of-Four 模式语言）
- Ontological Checkpoint（数据摄入验证）
- Dormancy-Aware Pipeline（低频信号保留）
- Drift Sentinel（持续漂移监控）
- Dual-Ontology Layer（并行表示维护）
- Reification Circuit Breaker（反馈环中断）
- Terminology Version Gate（术语演化管理）
- Regulatory Compliance Adapter（可插拔合规）

## 关键引用
> "Each pattern is specified with Problem, Forces, Solution, Consequences, Known Uses, and Related Patterns."

## 关联
- [[OntologySemanticLayer]] — 本体语义层
- [[OntologyReasoning]] — 本体推理核心方法
- [[qime-ontology-embeddings]] — 本体驱动可解释医学嵌入
- [[neuron-clinical-explainability]] — SNOMED CT本体增强临床可解释性

## 矛盾
- 无
