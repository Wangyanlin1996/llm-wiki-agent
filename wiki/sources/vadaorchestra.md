---
title: "VADAOrchestra: Neurosymbolic Orchestration of Adaptive Reasoning Workflows（自适应推理工作流的神经符号编排）"
type: source
tags: [agent-explainability, neurosymbolic, orchestration, verifiable-trace, KR2026]
sources: [vadaorchestra]
source_file: raw/papers/vadaorchestra.pdf
last_updated: 2026-07-02
arxiv_id: "2606.22485"
authors: ["Teodoro Baldazzi", "Luigi Bellomarini", "Andrea Coletta", "Michela Iezzi", "Carsten Maple", "Alessandro Pesare", "Emanuel Sallinger"]
year: 2026
venue: "KR 2026"
citation_count: pending
---

## 概要

真实世界决策很少遵循固定脚本，而是随上下文和数据变化演化的动态推理过程。传统业务流程管理（BPM）提供严格性、确定性和可审计性，但难以运行时适配；基于 LLM 的 agentic 系统带来灵活性，但本质不透明、不可靠且在大数据集上扩展性差。**VADAOrchestra** 是一个神经符号框架，将复杂工作流建模为演化推理过程：LLM 编排器增量规划并适配工作流，编码为 Datalog+/- 片段的逻辑程序（谓词=工具调用，规则=预定义领域依赖+按需合成的逻辑构造），所有逻辑推理由最先进的 Datalog+/- 符号引擎执行。这提供**可验证推理轨迹**，支撑全过程的可审计性和可复现性。

## 关键贡献

- **LLM 编排 + 符号推理解耦**：LLM 负责高层编排（灵活），符号引擎负责推理执行（可验证）——填补 synthesis 报告方向2"LLM 编排 vs 经典 HTN/PDDL"的空白
- **可验证推理轨迹**：逻辑程序天然提供可审计、可复现的推理链——直接对应 AgentLoop 方向5（机器可读凭证）
- **按需逻辑构造合成**：规则不仅预定义，还可在运行时按需合成以处理中间结果——超越静态 HTN 分解

## 关键引用

> "This approach provides a verifiable reasoning trace, supporting the auditability and reproducibility of the entire process."

## 关联

- [[NeurosymbolicOrchestration]] — 本文是该概念的核心实现
- [[ExecutionProvenance]] — 逻辑程序轨迹是执行溯源的形式化载体
- [[AgentExplainability]] — 神经符号编排提供可验证推理链
- [[StructuredArgumentation]] — Datalog+/- 逻辑规则与论证图互补
- [[ExplainablePlanning]] — LLM+符号编排是可解释规划的新范式（vs 经典 HTN/PDDL）

## 矛盾

无已知矛盾。与纯 LLM 编排的"灵活性 vs 可审计性"权衡形成解决方案——通过解耦实现两者兼得。
