---
title: "RAIDER: Tool-Equipped LLM Agent for Robotic Action Issue Detection, Explanation and Recovery（机器人动作问题检测、解释与恢复的工具增强 Agent）"
type: source
tags: [agent-explainability, issue-detection, explanation-recovery, closed-loop, grounding]
sources: [raider-robot]
source_file: raw/papers/raider-robot.pdf
last_updated: 2026-07-02
arxiv_id: "2503.17703"
authors: ["Silvia Izquierdo-Badiola", "Carlos Rizzo", "Guillem Alenyà"]
year: 2025
venue: "arXiv preprint"
citation_count: pending
---

## 概要

随着机器人在动态人机环境中运行，提升其检测、解释和从动作相关问题恢复的能力变得关键。传统基于模型/数据驱动方法缺乏适应性，而更灵活的生成式 AI 方法难以将提取信息接地到真实世界约束。**RAIDER** 将 LLM 与接地工具集成，实现可适配高效的问题检测和解释。采用独特的"**Ground, Ask&Answer, Issue**"流程：动态生成上下文感知的前置条件问题并选择适当工具求解，实现定向信息收集。在模拟家居环境中超越依赖预定义模型、完整场景描述或独立训练模型的方法；其解释增强恢复成功率（含需人机交互场景），模块化架构含自纠正机制支持多场景适配。

## 关键贡献

- **检测→解释→恢复完整闭环**：直接对应 AgentLoop 的"结果整合→闭环验证→恢复"——少数覆盖完整闭环的论文
- **Ground-Ask&Answer-Issue 流程**：动态生成前置条件问题+工具选择，实现定向信息收集而非全场景描述
- **解释增强恢复**：解释不仅是事后说明，更是恢复成功的因果输入——支撑 AgentLoop 方向3+4联动

## 关键引用

> "RAIDER's explanations enhance recovery success, including cases requiring human interaction."

## 关联

- [[VerificationCoEvolution]] — 检测→解释→恢复是闭环验证的具身实例
- [[AgentExplainability]] — 解释驱动恢复是过程级解释的实用价值
- [[ExplainablePlanning]] — 前置条件问题是可解释规划的动作级实例
- [[grounded-continuation]] — 接地工具与运行时验证器共享"接地检查"理念
- [[IntentSignalTheory]] — "接地到真实世界约束"是 I*→P 信息损失的物理补偿

## 矛盾

无已知矛盾。
