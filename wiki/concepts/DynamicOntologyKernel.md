---
title: "动态本体内核 (Dynamic Ontology Kernel)"
type: concept
tags: [ontology-graph-retrieval]
sources: [dynamic-ontology-llm-agents, ontology-project-memory-coding, owlpath-bug-repair]
last_updated: 2026-08-31
---

动态本体内核是指为 LLM agent 任务自动构建 task-oriented ontology schema + typed reasoning functions，作为 agent 访问数据的唯一通道（kernel）。与传统 descriptive ontology 仅描述"域中存在什么"不同，动态本体内核将 ontology 作为 semantic-procedural contract：既约束 agent 可调用的概念（schema），又通过 typed functions 约束可执行的计算（function composition）。核心特征包括：(1) 自动从任务描述和训练数据构造 schema，用 HermiT reasoner 做形式化验证；(2) judge-driven iterative refinement 诊断并修复 schema 和 function 本身的缺陷，而非 response-level 修正；(3) chunk-map-merge KG instantiation 通过 primary key 等价类合并消除跨 chunk 重复。相关论文：[[dynamic-ontology-llm-agents]]（OaK 框架）、[[ontology-project-memory-coding]]（MOOSEDev 编码 Agent 记忆）、[[owlpath-bug-repair]]（OwlPath OWL2 reasoning layer）。与 [[OntologyFirstAgentDesign]]（Round 13）的 BFO 本体+类型 lambda 演算正确性证明形成方法论对比——两者都将本体作为 agent 设计的核心，但 OaK 强调自动构建+迭代精修，Agentic Redux 强调形式化正确性保证。
