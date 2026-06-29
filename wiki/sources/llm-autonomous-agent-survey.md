---
title: "A Survey on Large Language Model based Autonomous Agents（基于 LLM 的自主智能体综述）"
type: source
tags: [agent-evaluability, LLM-agent, survey]
sources: [llm-autonomous-agent-survey]
source_file: raw/papers/llm-autonomous-agent-survey.pdf
last_updated: 2026-06-29
arxiv_id: "2308.11432"
authors: ["Lei Wang", "Chen Ma", "Xueyang Feng", "Xu Chen", "Yankai Lin", "Wayne Xin Zhao", "Ji-Rong Wen"]
year: 2024
venue: "Frontiers of Computer Science 2024"
citation_count: 3137
doi: "10.1007/s11704-024-40231-1"
---

## 概要

本综述系统回顾 LLM 自主智能体研究，提出一个涵盖既往大部分工作的统一框架，从整体视角梳理 LLM-based autonomous agents 的构造、应用与评测。综述将 agent 构造拆解为感知、规划、记忆、工具使用等模块，并明确把"解释"列为 agent 可信度的核心维度之一，呼吁建立覆盖 agent 全生命周期的解释框架。

## 关键贡献

- 提出 LLM 自主智能体的统一架构框架（感知—规划—记忆—工具—行动），整合既有工作。
- 系统梳理 agent 在社会科学、自然科学、工程领域的多样化应用。
- 总结常用 agent 评测策略，并明确将"解释性"（explainability）作为 agent 可信度的核心维度提出。

## 关键引用

> "we present a comprehensive survey... a unified framework that encompasses a majority of the previous work" — 统一架构主张

> 综述将解释列为 agent 可信度核心维度，并呼吁覆盖 agent 全生命周期的解释框架 — 支撑"Agent 可解释性"作为独立研究方向

## 关联

- [[LLMAutonomousAgent]] — 本综述是 LLM 自主智能体统一架构的权威来源
- [[AgentExplainability]] — 综述明确将解释列为 agent 可信度核心维度，为 Agent 可解释性方向提供理论背书
- [[AgentMemory]] — 综述的"记忆"模块与本知识库既有 Agent Memory 方向呼应

## 矛盾

- 无。本页元数据与外部引用清单（Wang, L. et al., Frontiers of Computer Science）一致。
