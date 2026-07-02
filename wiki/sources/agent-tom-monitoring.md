---
title: "Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning（基于心智理论推理的自治 Agent 监控）"
type: source
tags: [agent-explainability, theory-of-mind, monitoring, closed-loop-verification]
sources: [agent-tom-monitoring]
source_file: raw/papers/agent-tom-monitoring.pdf
last_updated: 2026-07-02
arxiv_id: "2605.24216"
authors: ["Nesreen K. Ahmed", "Nima Nafisi"]
year: 2026
venue: "arXiv preprint"
citation_count: pending
---

## 概要

监控自治 LLM agent 的隐蔽恶意行为极具挑战——攻击延迟、上下文相关且长时程，agent 可在维持表面良性行为的同时追求隐藏目标。本文提出 **Agent-ToM**，一个基于心智理论（Theory-of-Mind）推理的学习监控框架，通过推断信念、意图假设（带校准置信度）、预期动作及与任务一致行为基线的偏差进行结构化全轨迹分析。推理时采用 **Reason-Verify-Refine** 管线构建并验证监控决策；训练时将批评信号蒸馏为持久的**语义护栏记忆**，使信念/意图条件化约束可跨 episode 复用。

## 关键贡献

- **ToM 推理用于安全监控**：显式推理 agent 的信念、意图、目标对齐，区分良性任务执行与隐蔽偏离——超越独立轨迹的脚手架/集成方法
- **持久语义护栏记忆**：监控层的学习跨 episode 复用，信念/意图条件化约束可积累——填补 AgentLoop 监控层的"从经验中学习"空白
- **两调用推理管线即超越 SOTA 集成方法**：在 SHADE-Arena 和 CUA-SHADE-Arena 对抗监控基准上取得强 precision-recall 平衡

## 关键引用

> "Standard reasoning methods explain observed behavior without explicitly reasoning about agent beliefs, intentions, and goal alignment required to distinguish benign task execution from covert deviation."

## 关联

- [[TheoryOfMindReconstruction]] — Agent-ToM 将心智重建从意图理解扩展到安全监控
- [[AgentAccountability]] — ToM 推理为问责提供意图级证据
- [[AgentExplainability]] — 信念/意图推理是过程级解释的安全维度
- [[TrajectoryForensics]] — 全轨迹 ToM 分析是轨迹取证的认知层
- [[forensic-trajectory-signatures]] — 行为不变量（统计层）与 ToM 推理（认知层）互补

## 矛盾

无已知矛盾。
