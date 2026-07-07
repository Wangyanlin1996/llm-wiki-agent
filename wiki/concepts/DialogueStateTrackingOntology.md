---
title: "对话状态追踪本体 (Dialogue State Tracking Ontology)"
type: concept
tags: [task-oriented-dialogue, dst, entity-extraction, entity-linking, task-completion]
sources: [ontology-enhanced-slot-filling, zero-shot-open-vocab-dst, beyond-ontology-dst, vlk-rl-cross-domain-tod, opal-ontology-aware-tod, d3st-description-driven-tod]
last_updated: 2026-07-07
---

对话状态追踪本体（Dialogue State Tracking Ontology）是指在任务型对话系统中，本体定义的 slot 类型、值域和约束规则用于结构化对话状态的表示、更新和验证。本体为 DST 提供了"什么信息需要追踪"和"合法值是什么"的结构化定义。这一概念涵盖了从严格依赖预定义本体到完全无本体的完整谱系：本体增强 slot filling 利用预定义值域进行实体匹配（[[ontology-enhanced-slot-filling]]）；描述驱动 schema 用自然语言描述替代符号化本体（[[d3st-description-driven-tod]]）；开放词汇 DST 不依赖固定值域（[[zero-shot-open-vocab-dst]]）；无本体 DST 完全放弃预定义本体（[[beyond-ontology-dst]]）。关键发现是：**本体的价值在于约束而非限制——好的本体设计（如描述驱动、模块化）能兼顾约束可靠性和泛化灵活性**。

## 关联论文
- [[ontology-enhanced-slot-filling]] — 本体匹配实体链接
- [[zero-shot-open-vocab-dst]] — 开放词汇突破固定值域
- [[beyond-ontology-dst]] — 无本体DST
- [[vlk-rl-cross-domain-tod]] — 本体对齐约束感知状态
- [[opal-ontology-aware-tod]] — 本体三元组恢复预训练
- [[d3st-description-driven-tod]] — 描述驱动schema

## 关联概念
- [[OntologyAwareTOD]]
- [[DynamicOntologyConstruction]]
- [[IntentModularisation]]
