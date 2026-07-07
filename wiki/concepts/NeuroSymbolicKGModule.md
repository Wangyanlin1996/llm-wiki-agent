---
title: "神经符号知识模块 (Neuro-Symbolic Knowledge Module)"
type: concept
tags: [ontology-reasoning, neuro-symbolic, task-execution]
sources: [kml-procedural-video-qa, neuro-symbolic-kg-ontology, titan-graph-reasoning-cti, hear-hypergraph-enterprise]
last_updated: 2026-07-07
---

神经符号知识模块（Neuro-Symbolic Knowledge Module）是指将知识图谱/本体中的关系类别学习为可组合的神经模块，并通过符号引擎执行可验证推理的混合架构。核心思想是将"关系推理"分解为"神经模块负责从非结构化输入中检索关系证据"和"符号引擎负责在结构化知识上确定性执行推理"两个解耦阶段。关键实例包括：知识模块学习将 KG 关系类别学习为可组合模块（[[kml-procedural-video-qa]]）、本体引导的后提取纠错构建神经符号 KG（[[neuro-symbolic-kg-ontology]]）、路径规划器+图执行器的双阶段推理（[[titan-graph-reasoning-cti]]）、以及分层超图本体的证据驱动推理循环（[[hear-hypergraph-enterprise]]）。神经符号模块的优势在于兼顾灵活性和可验证性——LLM 提供自然语言理解灵活性，符号引擎提供推理确定性。

## 关联论文
- [[kml-procedural-video-qa]] — 知识模块组合推理
- [[neuro-symbolic-kg-ontology]] — 本体引导KG纠错
- [[titan-graph-reasoning-cti]] — 路径规划+图执行
- [[hear-hypergraph-enterprise]] — 超图本体推理循环

## 关联概念
- [[ActionOntologyAgent]]
- [[OntologyGuidedKGQA]]
- [[NeuroSymbolicOntology]] (已有wiki)
- [[NeurosymbolicOrchestration]] (已有wiki)
