---
title: "Aligning Provenance with Authorization: A Dual-Graph Defense for LLM Agents（溯源与授权对齐：LLM Agent 的双图防御）"
type: source
tags: [agent-explainability, provenance, authorization, dual-graph, prompt-injection-defense, machine-readable-credential]
sources: [provenance-authorization]
source_file: raw/papers/provenance-authorization.pdf
last_updated: 2026-07-02
arxiv_id: "2605.26497"
authors: ["Peiran Wang", "Ying Li", "Yuan Tian"]
year: 2026
venue: "arXiv preprint"
citation_count: pending
---

## 概要

LLM agent 在邮件管理、金融交易、代码执行等高风险场景中通过工具调用与外部世界交互，必须读取攻击者可控制的外部数据源；通过间接提示注入，攻击者在数据中嵌入恶意指令操纵 agent 执行未授权操作。现有防御要么做工具调用级值检查而不追踪参数值来源，要么从单一视角分析执行轨迹而无干净授权基线比较。本文提出 **AuthGraph**，一个双图对齐防御框架：构建**注入推理图**（建模实际执行轨迹的信息溯源，含可能被操纵的归属）和**授权图**（源于隔离干净上下文中的用户意图，信息论上不可能被注入影响）；图对齐检查器结构化比较两图以检测工具级和参数源级偏差。在 AgentDojo 上将攻击成功率从 40% 降至 1%。

## 关键贡献

- **溯源 vs 授权双图对齐**：首个在参数源级结构化比较授权规格与执行溯源的防御——为 AgentLoop 方向5提供溯源-授权对齐原语
- **信息论不可注入的授权基线**：干净上下文派生授权图，信息论上不可能被注入影响——形式化安全保证
- **细粒度注入检测不牺牲灵活性**：参数源级而非仅工具级检测

## 关键引用

> "AuthGraph is the first agent security defense to structurally compare authorization specifications against execution provenance at the parameter-source level."

## 关联

- [[RuntimeGovernance]] — 溯源-授权对齐是运行时治理的安全实例
- [[ExecutionProvenance]] — 注入推理图是执行溯源的攻击感知投影
- [[AgentAccountability]] — 双图对齐使"授权 vs 实际执行"偏差可审计
- [[proof-carrying-agent]] — PCAA 动作证书+AuthGraph 双图构成"证书+对齐"治理栈
- [[IntentSignalTheory]] — 授权图源自用户意图，是 I*→P 信息损失的安全补偿
- [[grounded-continuation]] — 依赖图验证器与 AuthGraph 双图共享"图对齐检查"理念

## 矛盾

无已知矛盾。
