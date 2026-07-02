---
title: "Proof-Carrying Agent Actions: Model-Agnostic Runtime Governance for Heterogeneous Agent Systems（携证 Agent 动作：异构 Agent 系统的模型无关运行时治理）"
type: source
tags: [agent-explainability, proof-carrying, runtime-governance, action-certificate, machine-readable-credential]
sources: [proof-carrying-agent]
source_file: raw/papers/proof-carrying-agent.pdf
last_updated: 2026-07-02
arxiv_id: "2606.04104"
authors: ["Zexun Wang"]
year: 2026
venue: "arXiv preprint"
citation_count: pending
---

## 概要

Agent 系统通过控制点差异极大的运行时执行：本地编码工具、框架 SDK、托管 agent 平台、API 网关、仅观察者集成。同一高风险动作（如外部发布数据）在一个运行时是 shell 命令，在另一个是工具调用，在第三个是托管会话转移——使"什么动作被授权、凭谁的权威、何种批准语义、执行后有何证据"难以一致回答。**Proof-Carrying Agent Actions（PCAA）** 是以**动作证书**（而非厂商原生会话记录）为中心的运行时中立治理模型，围绕 5 个检查点组织：动作前可准入性、动作开启、假设捕获、批准、结果闭环。证书绑定到可移植动作信封、运行时/批准回执和可重放证明。

## 关键贡献

- **动作证书取代厂商会话记录**：跨运行时一致的治理原语——直接填补 synthesis 报告方向5"无电信标准定义解释序列化"的空白
- **5 检查点 + 外部性感知**：pre-action admissibility→action open→assumption capture→approval→outcome closure，证书携带边界事实（目标可见性/账户溯源）
- **显式可执行性类别**：批准由显式 enforceability classes 描述而非单一 reviewed/unreviewed 位——超越二元审批

## 关键引用

> "What action was authorized, under whose authority, with what approval semantics, and with what evidence after execution?"

## 关联

- [[RuntimeGovernance]] — 本文是该概念的核心实现
- [[ExecutionProvenance]] — 动作证书是执行溯源的可移植序列化载体
- [[AgentAccountability]] — 携证执行使问责从"可信过程"变为"可独立验证"
- [[blockchain-accountability-agents]] — 区块链防篡改+动作证书互补：不可篡改记录+可验证理据
- [[agentbound]] — AgentBound 的三权威与 PCAA 的 5 检查点互补
- [[IntentReport]] — PCAA 动作证书可映射到 3GPP IntentReport 的可行性/满足报告

## 矛盾

无已知矛盾。
