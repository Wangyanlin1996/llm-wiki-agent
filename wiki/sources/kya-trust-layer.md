---
title: "KYA: A Framework-Agnostic Trust Layer for Autonomous Systems with Verifiable Provenance and Hierarchical Policy Composition（自治系统的框架无关信任层：可验证溯源与层次化策略组合）"
type: source
tags: [agent-explainability, trust-layer, verifiable-provenance, policy-composition, framework-agnostic]
sources: [kya-trust-layer]
source_file: raw/papers/kya-trust-layer.pdf
last_updated: 2026-07-02
arxiv_id: "2605.25376"
authors: ["Kolawole Quadri"]
year: 2026
venue: "arXiv preprint (code: veldt-kya on PyPI, Apache 2.0)"
citation_count: pending
---

## 概要

**KYA（Know Your Agents）** 是一个开源、框架无关的自治系统信任与治理层，由 5 个原语组成：(1) 四门入站 apply 管线；(2) 三通道多租户层次上的 only-tighten 组合代数；(3) **KYP（Know Your Principal）**——跨人类用户/AI agent/服务账号的信任评分模式级统一；(4) 基于 AIVSS 加性基线的可审计交互乘数放大；(5) 两轴委托归因：高风险委托的静态溢价+多 agent 扇出中实际委托不当行为的运行时借记。三者支柱（信任/治理/证据保证）使自治系统动作"被授权、策略合规、事后可验证"。原生适配 15+ agent 框架，4×9 跨后端矩阵全部通过，纯函数评分器 p99 亚毫秒，~1800 ops/sec。

## 关键贡献

- **框架无关信任层**：15+ agent 框架原生适配——直接填补 AgentLoop 跨框架治理空白
- **可验证溯源 + 层次化策略组合**：only-tighten 组合代数确保策略只收紧不放松——形式化治理保证
- **两轴委托归因**：静态风险溢价+运行时不当行为借记——为多 agent 扇出提供细粒度问责

## 关键引用

> "Where observability answers how long, how much, and what path, KYA answers was it authorized, did it conform, and can it be verified; it composes with observability rather than replacing it."

## 关联

- [[RuntimeGovernance]] — 本文是该概念的框架无关实现
- [[ExecutionProvenance]] — 可验证溯源与执行溯源互补：溯源=如何，KYA=是否授权/合规/可验证
- [[AgentAccountability]] — 两轴委托归因细化多 agent 问责
- [[CrossFrameworkMemorySharing]] — KYA 的 15+ 框架适配与跨框架记忆共享共享"框架无关"理念
- [[proof-carrying-agent]] — PCAA 动作证书+KYA 信任评分构成跨框架治理栈
- [[agentbound]] — AgentBound 治理回执+KYA 策略组合互补

## 矛盾

无已知矛盾。
