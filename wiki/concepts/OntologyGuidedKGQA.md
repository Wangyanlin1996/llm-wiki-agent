---
title: "本体引导的知识图谱问答 (Ontology-Guided KGQA)"
type: concept
tags: [ontology-qa, kgqa, ontology-reasoning]
sources: [opi-ontology-kgqa, ort-ontology-reverse-kgqa, oracle-ontology-multihop, multicube-rag-multihop-qa]
last_updated: 2026-07-07
---

本体引导的知识图谱问答（Ontology-Guided KGQA）是指利用本体（ontology）的结构化知识——包括实体类型层次、关系类型约束、概念层次——来引导知识图谱问答中的推理路径搜索和答案约束验证。不同于纯向量匹配方法，本体引导方法利用类型约束缩减搜索空间、利用关系层次消除噪声路径、利用概念抽象弥合问题意图与具体实体之间的语义鸿沟。关键范式包括：关系中心本体图的双向检索（[[opi-ontology-kgqa]]）、逆向思维路径推理（[[ort-ontology-reverse-kgqa]]）、动态本体构建+一阶逻辑推理链（[[oracle-ontology-multihop]]）、以及正交多维本体立方体（[[multicube-rag-multihop-qa]]）。这些方法的共同洞察是：**本体的类型约束和关系层次是缩减 KGQA 搜索空间、提升推理可靠性的高效先验**。

## 关联论文
- [[opi-ontology-kgqa]] — 关系中心本体图+双向检索
- [[ort-ontology-reverse-kgqa]] — 本体引导逆向思维
- [[oracle-ontology-multihop]] — 动态本体+FOL推理链
- [[multicube-rag-multihop-qa]] — 本体立方体+查询分解

## 关联概念
- [[DynamicOntologyConstruction]]
- [[NeuroSymbolicKGModule]]
- [[LLMKGOntologySynergy]]
