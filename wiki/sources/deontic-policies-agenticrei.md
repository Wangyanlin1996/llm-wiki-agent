---
title: "Deontic Policies: OWL道义策略语言治理Agentic AI"
type: source
tags: [llm-agent-ontology, agent-governance]
sources: [deontic-policies-agenticrei]
source_file: raw/papers/deontic-policies-agenticrei.pdf
last_updated: 2026-07-25
arxiv_id: "2606.19464"
authors: ["Anupam Joshi", "Tim Finin", "Karuna Pande Joshi", "Lalana Kagal"]
year: 2026
venue: "IEEE ICWS 2026"
citation_count: 0
---

## 概要
自主 agentic AI 系统引入新的安全、隐私和合规挑战：能调用工具、操作数据、安装软件并跨组织边界协调的 agent 必须被完整的企业治理结构约束。现有策略引擎（XACML、Rego、Cedar）仅处理许可/禁止子集，不提供义务生命周期管理、元策略冲突解决、豁免和本体推理。本文提出 AgenticRei，基于 Rei 框架的道义策略语言，用 OWL 表达并由高性能逻辑引擎在 LLM 外部运行评估，同时治理工具调用和 agent 间消息。

## 关键贡献
- 基于 Rei 框架的道义策略语言，用 OWL 表达
- 实现义务生命周期管理、豁免、策略冲突解决、域类层次本体推理
- LLM 外部高性能逻辑引擎评估，同时治理工具调用和 agent 间消息
- 与 A2AS 等行业标准框架自然组合

## 关键引用
> "We use a deontic policy language built on the Rei framework, expressed as OWL (Web Ontology Language) and evaluated at runtime by a high-performance logic engine entirely outside the LLM."

## 关联
- [[OntologyFirstAgentDesign]] — 本体优先Agent设计方法论
- [[RuntimeGovernance]] — 运行时治理
- [[agentic-redux]] — 本体优先Agent设计
- [[ProofCarryingAgent]] — 动作证书+5检查点
- [[security-ontology-autonomous-networks]] — TM Forum安全本体

## 矛盾
- 无
