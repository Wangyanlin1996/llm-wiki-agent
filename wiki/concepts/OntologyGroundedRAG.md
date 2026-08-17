---
title: "本体grounding RAG (Ontology-Grounded RAG)"
type: concept
tags: [ontology-graph-retrieval]
sources: [og-rag-ontology-grounded, cyberbot-ontology-grounded-rag, ontologyrag-biomedical-code-mapping, fair-graphrag-semantic-data, rag-autoconfig-industrial-fieldbus]
last_updated: 2026-08-17
---

本体grounding RAG 是指在 RAG 管线中用形式本体约束检索过程，确保检索结果不仅"表面相关"，而且"概念grounding且域适切"。核心区别于普通 RAG：普通 RAG 用向量相似度检索 chunk，忽略结构化领域知识；本体grounding RAG 将领域文档组织为本体超图/图结构，检索时用本体类型/关系约束确保结果的概念一致性。

代表性方法包括：本体超图最小超边集检索（[[og-rag-ontology-grounded]]，recall+55%）、本体约束 RAG 的可信教育问答（[[cyberbot-ontology-grounded-rag]]）、本体 KG 增强的生物医学代码映射（[[ontologyrag-biomedical-code-mapping]]）、FAIR 原则+本体 schema 约束的 GraphRAG（[[fair-graphrag-semantic-data]]）、ECLASS 本体图+混合检索的工业设备配置（[[rag-autoconfig-industrial-fieldbus]]）。这些方法共同表明：本体grounding将检索从"相似度匹配"提升到"概念一致性验证"，在医疗/法律/工业/网络安全等事实推理场景中显著优于 vanilla RAG。与 [[RetrievalAugmentedGeneration]] 的演进关系：本体grounding是 RAG 的结构化领域知识增强方向。
