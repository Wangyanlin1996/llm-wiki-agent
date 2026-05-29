---
title: "PIRA-Bench"
type: source
tags: [intent-recommendation, proactive-agent, GUI-agent, benchmark]
date: 2026-03-09
source_file: raw/papers/pira-bench.md
last_updated: 2026-05-28
---

## 概要
PIRA-Bench 引入首个面向 GUI 上 Proactive Intent Recommendation Agents（主动式意图推荐智能体）的评测基准，具有包含多个交织 intents、噪声片段和 user profile contexts 的复杂轨迹。它提出 PIRF，一个用于多线程管理的 memory-aware state-tracking framework（记忆感知状态追踪框架），推动从 reactive（响应式）向 proactive（主动式）GUI agent 范式转变。

## 核心论点
- 当前 GUI agents 纯属 reactive（响应式，需要显式指令）
- Proactive intent recommendation 需要从连续视觉输入中检测可执行事件
- 复杂轨迹包含多个交织 intents 和噪声
- PIRF framework 通过 memory-aware state tracking 管理多任务线程
- Proactive GUI agents 需要 user profile context 以实现偏好感知检测

## 关键引述
> "Current GUI agents operate under a reactive paradigm requiring explicit user instruction" — 问题陈述：当前 GUI agents 在响应式范式下运作

> "PIRA-Bench serves as an initial step toward robust proactive GUI-based personal assistants" — 贡献：作为迈向稳健的主动式 GUI 个人助手的初步步骤

## 关联
- [[IntentRecommendation]] — PIRA-Bench 在 GUI 语境下评估主动式意图推荐
- [[PIRABench]] — 此处形式化的基准概念
- [[PIRF]] — 与 PIRA-Bench 同时提出的 memory-aware state-tracking framework
- [[IntentUnderstanding]] — 检测可执行事件需要意图理解
- [[VitaBench2]] — 评估个性化主动式 agents 的互补基准
- [[AgentMemory]] — PIRF 的 memory-aware state tracking 与 AgentMemory 机制相关

## 矛盾
- 与 reactive GUI agent 范式矛盾：PIRA-Bench 证明主动式意图检测对有效的 GUI assistants 是必要的