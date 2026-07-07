---
title: "本体感知任务型对话 (Ontology-Aware TOD)"
type: concept
tags: [task-oriented-dialogue, ontology-modeling, dst, task-completion]
sources: [opal-ontology-aware-tod, d3st-description-driven-tod, vlk-rl-cross-domain-tod, teqodo-tod-ontology, ontology-enhanced-slot-filling]
last_updated: 2026-07-07
---

本体感知任务型对话（Ontology-Aware TOD）是指利用本体（slot 类型、值域、intent 层次、slot 间约束）来结构化任务型对话系统的对话状态追踪（DST）和响应生成（RG）。本体为对话系统提供了结构化的知识基础：slot-value 对作为对话状态表示、intent 本体作为意图分类空间、slot 间约束作为推理规则。关键方法涵盖从本体感知预训练（[[opal-ontology-aware-tod]]）到描述驱动 schema（[[d3st-description-driven-tod]]）、从本体对齐 slot-value 约束感知 RL（[[vlk-rl-cross-domain-tod]]）到自动本体构建（[[teqodo-tod-ontology]]）、以及本体增强 slot filling（[[ontology-enhanced-slot-filling]]）。这一方向的核心张力在于：**固定本体提供可靠约束但限制泛化，开放/无本体提供灵活性但牺牲一致性**——多篇论文（[[zero-shot-open-vocab-dst]]、[[beyond-ontology-dst]]）探索了突破固定本体限制的路径。

## 关联论文
- [[opal-ontology-aware-tod]] — 本体感知预训练
- [[d3st-description-driven-tod]] — 描述驱动schema
- [[vlk-rl-cross-domain-tod]] — 本体对齐约束RL
- [[teqodo-tod-ontology]] — 自动本体构建
- [[ontology-enhanced-slot-filling]] — 本体增强slot填充

## 关联概念
- [[DialogueStateTrackingOntology]]
- [[DynamicOntologyConstruction]]
- [[IntentModularisation]]
