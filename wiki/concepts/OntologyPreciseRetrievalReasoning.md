---
title: "本体精准检索推理 (Ontology-Precise Retrieval Reasoning)"
type: concept
tags: [ontology-precise-retrieval]
sources: [satir-constraint-ir-clinical, deeprag-hierarchical-reasoning, ragged-events-reasoning, rag-ontology-relational-db, raredxr1-rare-disease]
last_updated: 2026-09-08
---

本体精准检索推理是指利用形式本体的类型/关系/约束结构实现超越纯向量相似度的精准检索导向推理。与"判断向"推理（verdict-oriented，如分类/判断）不同，本方向聚焦"检索向"（retrieval-oriented）——推理过程本身是检索-验证的迭代，本体的角色是提供约束满足的 binding requirements 而非 soft signals。关键方法包括：(1) 约束满足检索——将约束理解与满足分离，LLM 翻译为 SMT 公式再投影到关系代数（[[satir-constraint-ir-clinical]]）；(2) 层次化推理+过程监督——DeepSeek R1 hierarchical reasoning + RAG-Gym MDP + UMLS concept-level rewards（[[deeprag-hierarchical-reasoning]]）；(3) RAG 增强事件 KB+证明助手——RDF→Coq 翻译管线支持高阶推理（[[ragged-events-reasoning]]）；(4) 迭代 RAG 本体生成——FK-Guided Traversal + Judge-LLM in-loop 验证（[[rag-ontology-relational-db]]）；(5) 知识内化自主推理——RERS 从失败轨迹学习，无需 RAG（[[raredxr1-rare-disease]]）。核心发现：Inverse Calibration Principle——enhancement 效果与模型能力反向相关（[[ragged-events-reasoning]]），强模型 base generation 优于 RAG，弱模型呈 inverted-U pattern。与 [[OntologyGraphRetrieval]]（Round 15-16）的区别：后者聚焦本体图增强检索精度，本方向聚焦本体驱动推理过程的约束满足和过程监督。相关论文：[[satir-constraint-ir-clinical]]、[[deeprag-hierarchical-reasoning]]、[[ragged-events-reasoning]]、[[rag-ontology-relational-db]]、[[raredxr1-rare-disease]]。
