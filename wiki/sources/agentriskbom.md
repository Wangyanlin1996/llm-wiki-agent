---
title: "AgentRiskBOM: A Risk-Scoping Security Bill of Materials for Agentic AI Systems（Agentic AI 系统的风险范围安全物料清单）"
type: source
tags: [agent-explainability, bill-of-materials, risk-scoping, machine-readable-credential, IEEE-Cyber-AI-2026]
sources: [agentriskbom]
source_file: raw/papers/agentriskbom.pdf
last_updated: 2026-07-02
arxiv_id: "2606.21877"
authors: ["Srimonti Dutta", "Akshata Kishore Moharir"]
year: 2026
venue: "IEEE Cyber-AI 2026"
citation_count: pending
---

## 概要

Agentic AI 系统检索私有上下文、调用工具、写文件、调用外部服务、与其他 agent 协调，可能无人批准即行动。现有物料清单制品（SBOM/AIBOM/MLBOM）改善依赖、模型元数据和训练溯源的透明度，但留下**agentic 透明度缺口**：能力不透明——缺少对部署 agent 能访问/记忆/更改/委托/事后证明的结构化说明。**AgentRiskBOM** 是面向工具使用 AI agent 的安全 BOM，作为 SBOM/AIBOM/MLBOM 之上的附加层，添加运行时权威字段：自治度、工具权限、记忆、凭据范围、批准门、审计信号、agent 间通信、外部动作能力。实现为 JSON-schema 制品，含可复现语料库、风险场景、评分器、差异检测器、控制映射器和报告。

## 关键贡献

- **能力不透明填补**：结构化说明 agent 能访问/记忆/更改/委托/证明——直接对应 AgentLoop 方向5（机器可读凭证）
- **JSON-schema 制品 + 差异检测**：检测 33 种结构化部署变异的权威漂移——为闭环治理提供漂移监测
- **16 能力维度 14 分 vs SBOM 1 分**：native-equivalent 覆盖远超传统 BOM

## 关键引用

> "Agentic AI security needs a machine-readable authority-and-risk artifact before incidents occur."

## 关联

- [[RuntimeGovernance]] — AgentRiskBOM 是运行时治理的制品层
- [[ExecutionProvenance]] — BOM 制品是执行溯源的部署时基线
- [[AgentAccountability]] — 能力清单使问责有据可查
- [[proof-carrying-agent]] — PCAA 动作证书（运行时）+AgentRiskBOM（部署时）构成全生命周期凭证
- [[agentbound]] — AgentBound 治理回执+AgentRiskBOM 能力清单互补
- [[TRiSM]] — AgentRiskBOM 是 TRiSM 五支柱中"风险管理"的制品实现

## 矛盾

无已知矛盾。
