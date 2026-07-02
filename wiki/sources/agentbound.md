---
title: "AgentBound: Verifiable Behavioral Governance for Autonomous AI Agents（自治 AI Agent 的可验证行为治理）"
type: source
tags: [agent-explainability, behavioral-governance, verifiable-receipts, authority-composition, machine-readable-credential]
sources: [agentbound]
source_file: raw/papers/agentbound.pdf
last_updated: 2026-07-02
arxiv_id: "2606.30970"
authors: ["Anuj Kaul", "Qianlong Lan", "Pranay Gupta"]
year: 2026
venue: "arXiv preprint"
citation_count: pending
---

## 概要

自治 AI agent 日益代表人类委托方执行有后果的动作（金融交易、外部通信、企业工作流）。现有 agent 基础设施依赖身份联合和委托授权来认证工作负载并控制资源访问，但**无法判断授权动作是否应在当前行为和操作上下文下执行**。**AgentBound** 是一个运行时治理框架，通过三个独立权威评估每个提议动作：委托授权、所有者签名行为宪章、站点动作契约。其判断通过形式化决策模型保守组合，决定动作应被允许、审查还是拒绝。为提供问责，AgentBound 生成**密码学可验证治理回执**，将每个动作绑定到管辖决策的确切委托、策略和语义制品，支持独立重放验证和策略溯源。

## 关键贡献

- **三权威保守组合**：委托授权×行为宪章×动作契约——超越单一身份/授权维度的治理
- **密码学可验证治理回执**：绑定动作到确切策略制品，支持独立重放验证——直接对应 AgentLoop 方向5（机器可读凭证）
- **常设委托**：长运行 agent 在持续刷新的治理策略下操作，保留可撤销性和有界权威

## 关键引用

> "Transforming governance from a process that must be trusted into one that can be independently verified."

## 关联

- [[RuntimeGovernance]] — 本文是该概念的权威组合实现
- [[AgentAccountability]] — 可验证回执使问责从信任转为验证
- [[ExecutionProvenance]] — 治理回执是执行溯源的策略层投影
- [[proof-carrying-agent]] — PCAA 动作证书与 AgentBound 治理回执互补：证书=动作级，回执=决策级
- [[blockchain-accountability-agents]] — 密码学回执+区块链防篡改构成完整问责链
- [[IntentReport]] — 治理回执可映射到 IntentReport 的冲突/可行性报告

## 矛盾

无已知矛盾。
