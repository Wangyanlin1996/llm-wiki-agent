---
title: "Machine-Coached Policy Revision in Adaptive Agent-Based Regulatory Simulation: A Controller-Level Contestability Layer（自适应 Agent 仿真中的机器辅导策略修订：控制器级可争议层）"
type: source
tags: [agent-explainability, contestability, defeasible-rules, policy-revision, interactive-xai]
sources: [contestability-layer]
source_file: raw/papers/contestability-layer.pdf
last_updated: 2026-07-02
arxiv_id: "2606.20700"
authors: ["Roberto Garrone"]
year: 2026
venue: "arXiv preprint"
citation_count: pending
---

## 概要

面向策略的 agent 基础模型（ABM）日益用于研究复杂自适应社会技术系统中的监管干预。但大多数诊断工作流是**事后的**：仿真后分析轨迹，但结果证据未系统反馈到策略控制器。本文提出一个轻量级**机器辅导策略修订层**：将策略决策表示为带显式冲突和优先级的**可废止规则**（defeasible rules），为控制器动作生成解释，并允许诊断失败转化为规则添加、移除或优先级变更。贡献不是新最优控制器，而是控制器级可争议性的仿真兼容操作化：策略决策可被解释、质疑、修订并在留出仿真中重新评估。

## 关键贡献

- **可废止规则 + 显式冲突/优先级**：策略决策表示为可争议的结构化规则——为 AgentLoop 方向4（交互式解释）提供形式化基础
- **诊断→修订闭环**：诊断失败系统反馈到策略控制器——超越事后分析，实现闭环可争议性
- **机器辅导 = 可解释自适应 ABM 的控制器级扩展**：与因果/信息论/轨迹诊断互补

## 关键引用

> "Policy decisions can be explained, challenged, revised, and re-evaluated in held-out simulation runs."

## 关联

- [[PolicyContestability]] — 本文是该概念的核心实现
- [[StructuredArgumentation]] — 可废止规则与论证图共享"可争议推理"基础
- [[AgentExplainability]] — 可争议性是交互式解释的治理维度
- [[ExplainablePlanning]] — 策略修订是可解释规划的闭环扩展
- [[intent-centric-se]] — 两者共同指向"意图为中心+可争议"的问责范式

## 矛盾

无已知矛盾。
