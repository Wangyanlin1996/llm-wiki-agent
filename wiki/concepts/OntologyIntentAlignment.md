---
title: "本体驱动意图对齐（Ontology-Driven Intent Alignment）"
type: concept
tags: [ontology-intent-alignment]
sources: [intent-driven-smart-manufacturing, treerec-intent-artifacts, geospatial-kg-multi-agent, rag-intent-reasoning-network, usage-centric-intent-ecommerce, birgat-multi-intent-slu]
last_updated: 2026-08-03
---

本体驱动意图对齐是指利用形式本体（ontology）的结构化语义约束，将用户自然语言意图精确映射到可执行的结构化表示（如 KG 节点、JSON 模型、语义框架）。与纯 LLM 意图理解不同，本体驱动对齐通过 ISA-95、TMF Intent Ontology 等领域标准提供操作语义保证，确保意图翻译结果与实际系统资源和约束一致。代表工作包括 [[intent-driven-smart-manufacturing]]（89.33% EM）、[[treerec-intent-artifacts]]（TreeRec 语义树）和 [[geospatial-kg-multi-agent]]（统一元数据本体中介层）。但也存在局限：[[usage-centric-intent-ecommerce]] 指出产品本体的类别刚性限制了跨类别意图对齐，[[rag-intent-reasoning-network]] 指出为每个应用手工构建本体语言不可扩展。关联概念：[[OntologySemanticLayer]]、[[IntentUnderstanding]]、[[NOEM³A]]。
