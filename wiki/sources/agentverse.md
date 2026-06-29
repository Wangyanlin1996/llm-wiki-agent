---
title: "AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors（多智能体协作与涌现行为）"
type: source
tags: [agent-evaluability, multi-agent, LLM-agent]
sources: [agentverse]
source_file: raw/papers/agentverse.pdf
last_updated: 2026-06-29
arxiv_id: "2308.10848"
authors: ["Weize Chen", "Yusheng Su", "Jingwei Zuo", "Cheng Yang", "Zhiyuan Liu", "Maosong Sun", "Jie Zhou"]
year: 2024
venue: "ICLR 2024"
citation_count: 0
citation_count_note: "pending — S2 API rate-limited at ingest time; to be backfilled"
doi: "10.48550/arXiv.2308.10848"
---

## 概要

AgentVerse 受人类群体动力学启发，提出一个可动态调整组成的多智能体框架，使 LLM 智能体群体作为"大于部分之和"的系统协同完成任务。实验表明该框架部署的多智能体群体优于单智能体，并揭示了协作过程中个体间的社会行为涌现。

## 关键贡献

- 提出可动态重组的多智能体协作框架，群体表现超越单智能体基线。
- 深入分析协作中涌现的社会行为（正面协同与负面行为），并讨论利用/抑制策略。
- 为多智能体交互中"中间决策"的可追溯性提供了实证基础。

## 关键引用

> "inspired by human group dynamics, we propose a multi-agent framework that can collaboratively and dynamically adjust its composition as a greater-than-the-sum-of-its-parts system" — 框架设计动机

## 关联

- [[LLMAutonomousAgent]] — AgentVerse 是 LLM 自主智能体在多智能体协作方向的代表工作
- [[AgentExplainability]] — 多智能体涌现行为论证：群体决策源头追溯需要对"中间决策"进行可解释性记录，支撑"跨域协商需要解释凭证"
- [[IntentUnderstanding]] — 多智能体协作中的意图协调与个体意图理解相关

## 矛盾

- 本页作者署名与外部引用清单标注（"Chen, Y. et al."）不符——论文真实第一作者为 Chen, W.，外部清单的作者归属有误。
- citation_count 因 Semantic Scholar API 在 ingest 时被限流（429）暂记为 0，待回填真实值。
