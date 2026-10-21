---
title: "Agentic Redux: 本体优先Agent设计与可证明正确性"
type: source
tags: [llm-agent-ontology, agent-governance]
sources: [agentic-redux]
source_file: raw/papers/agentic-redux.pdf
last_updated: 2026-07-25
arxiv_id: "2606.04903"
authors: ["Aaron Sterling"]
year: 2026
venue: ""
citation_count: 0
---

## 概要
本文引入 LLM agent 架构 Agentic Redux，适用于需要线性可审计性的问题领域。使用类型 lambda 演算证明，在适当领域上运行时，Agentic Redux 执行在语义上保证正确，所有决策记录在仅追加账本中。提出了 Ontology-First Agent Design 方法论：人类专家用 Basic Formal Ontology（BFO）对问题域进行本体化，然后分配 LLM 推导 agent 和人在环角色来处理领域问题。在医疗计费合规和安全漏洞披露两个生产级领域验证。

## 关键贡献
- 用类型 lambda 演算证明 Agent 执行的语义正确性
- 提出 Ontology-First Agent Design 方法论（BFO 本体 → 角色 → agent）
- 所有决策记录在仅追加审计账本中
- 两个生产级领域验证：医疗计费合规、安全漏洞披露

## 关键引用
> "Using the typed lambda calculus, we prove that, run on appropriate domains, Agentic Redux executions are semantically guaranteed to be correct, with all decisions recorded in an append-only ledger."

## 关联
- [[OntologyFirstAgentDesign]] — 本体优先Agent设计方法论
- [[RuntimeGovernance]] — 运行时治理
- [[ProofCarryingAgent]] — 动作证书+5检查点
- [[AgentBound]] — 三权威保守组合
- [[deontic-policies-agenticrei]] — OWL道义策略语言治理

## 矛盾
- 无
