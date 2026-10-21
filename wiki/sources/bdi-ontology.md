---
title: "BDI Ontology: 信念-欲望-意图本体设计模式与LLM逻辑增强生成"
type: source
tags: [llm-agent-ontology, ontology-reasoning]
sources: [bdi-ontology]
source_file: raw/papers/bdi-ontology.pdf
last_updated: 2026-07-25
arxiv_id: "2511.17162"
authors: ["Sara Zuppiroli", "Carmelo Fabio Longo", "Anna Sofia Lippolis", "Rocco Paolillo", "Lorenzo Giammei", "Miguel Ceriani", "Francesco Poggi", "Antonio Zinilli", "Andrea Giovanni Nuzzolese"]
year: 2025
venue: ""
citation_count: 0
---

## 概要
BDI（信念-欲望-意图）模型是 AI 和认知科学中表示理性 agent 的基石。本文提出形式化 BDI Ontology，作为模块化本体设计模式（ODP），通过信念、欲望、意图及其动态相互关系刻画 agent 的认知架构。本体通过与传统本体和模块化设计最佳实践对齐确保语义精度和可重用性。两条实验路线展示适用性：(1) 通过 Logic Augmented Generation（LAG）将本体与 LLM 耦合，评估本体接地对推理连贯性和一致性的贡献；(2) 集成到 Semas 推理平台，实现 RDF 三元组与 agent 心理状态的双向流（T2B2T 范式）。

## 关键贡献
- 形式化 BDI Ontology 作为模块化本体设计模式
- LLM + Logic Augmented Generation（LAG）评估本体接地的推理一致性
- Triples-to-Beliefs-to-Triples（T2B2T）范式实现 RDF 三元组与 agent 心理状态双向流
- 声明式与程序式智能的概念和操作桥梁

## 关键引用
> "The BDI Ontology acts as both a conceptual and operational bridge between declarative and procedural intelligence, paving the way for cognitively grounded, explainable, and semantically interoperable multi-agent and neuro-symbolic systems."

## 关联
- [[OntologyFirstAgentDesign]] — 本体优先Agent设计方法论
- [[NeuroSymbolicOntology]] — 神符号本体注入框架
- [[satori]] — BDI用户建模+多模态LLM
- [[AIDABDIStateModel]] — AIDA-BDI双重状态建模
- [[IntentDrivenMnS]] — 3GPP意图驱动管理服务

## 矛盾
- 无
