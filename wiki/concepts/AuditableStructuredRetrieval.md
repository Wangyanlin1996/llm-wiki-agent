---
title: "可审计结构化检索 (Auditable Structured Retrieval)"
type: concept
tags: [ontology-graph-retrieval]
sources: [moss-auditable-agentic-memory, worlddb-ontology-aware-memory]
last_updated: 2026-08-17
---

可审计结构化检索是指用结构化关系数据库/图结构替代嵌入相似度搜索，使每次检索有明确的查询路径和决策链——可审计、可追溯、不受向量表示理论上限约束。核心论点是 RAG 的不透明性（opaque by construction）是结构性缺陷，而非可接受的工程权衡。

[[moss-auditable-agentic-memory]] 的 MOSS 用结构化关系 DB 让 agent 主动构造查询，实现模型/存储/API 无关的可审计记忆。[[worlddb-ontology-aware-memory]] 的 WorldDB 用递归可组合图结构+本体感知写入时协调，在写入时而非读取时解决矛盾和替代，提供内容寻址不变量。两者共同指向：从"读取时向量匹配"到"写入时结构化协调+读取时精确查询"的范式转变。与 [[AgentMemory]] 的关系：可审计结构化检索是 agent 记忆架构从向量库到图结构的演进方向。
