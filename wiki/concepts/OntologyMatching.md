---
title: "本体匹配与对齐（Ontology Matching & Alignment）"
type: concept
tags: [ontology-matching-alignment]
sources: [open-ontologies-stable-matching, anchor-schema-agnostic-ontology, blinkg-llm-kg-benchmark, llm-ontology-engineering-legal-kg, cortex-ontological-corpus-graph, concepte-event-ontology-expansion, virtualset-typed-ontology-worlds]
last_updated: 2026-08-03
---

本体匹配与对齐是指在异构本体、数据 schema 或知识表示之间建立语义等价映射的技术。传统方法依赖复杂信号权重调优，而 [[open-ontologies-stable-matching]] 发现稳定 1:1 匹配是对齐质量主导因素（F1=0.832），信号权重在稳定匹配下无关紧要。LLM 时代的新趋势包括：[[anchor-schema-agnostic-ontology]] 的混合本体发现机制动态探索大本体 schema；[[blinkg-llm-kg-benchmark]] 评估 LLM schema-本体映射能力；[[cortex-ontological-corpus-graph]] 的三层跨域对齐层；[[concepte-event-ontology-expansion]] 的 LLM 概念化驱动本体扩展。反直觉发现：[[open-ontologies-stable-matching]] 揭示 LLM 读原始 OWL 文件（F1=0.323）比不读文件（F1=0.431）更差，MCP 工具结构化访问（F1=0.717）提供质变模式。关联概念：[[OntologyReasoning]]、[[OntologySemanticLayer]]、[[LLMKGOntologySynergy]]、[[DynamicOntologyConstruction]]。
