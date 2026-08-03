---
title: "本体语义grounding（Ontology Semantic Grounding）"
type: concept
tags: [ontology-semantic-grounding]
sources: [usd-scene-ontology-grounding, sam-ner-semantic-archetype]
last_updated: 2026-08-03
---

本体语义 grounding 是指将非结构化或半结构化输入（3D 场景、文本实体）映射到形式本体类的过程，使输入获得本体定义的类型、关系和约束语义。与本体对齐（ontology matching，本体间映射）不同，grounding 是从原始输入到形式本体的单向映射。[[usd-scene-ontology-grounding]] 证明 LLM 可零样本完成场景对象到 SOMA-HOME 本体的 grounding（90-96%），但依赖场景图语义线索而非几何信息。[[sam-ner-semantic-archetype]] 通过中间本体抽象原型空间稳定跨域 NER 迁移，避免标签定义与 LLM 内在语义不对齐导致的漂移。关联概念：[[LLMKGOntologySynergy]]、[[DynamicOntologyConstruction]]、[[OntologySemanticLayer]]。
