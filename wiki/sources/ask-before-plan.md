---
title: "Ask-before-Plan"
type: source
tags: [intent-recommendation, proactive-planning, multi-agent, EMNLP]
date: 2024-06-18
source_file: raw/papers/ask-before-plan.md
last_updated: 2026-05-28
---

## 概要
Ask-before-Plan（EMNLP 2024 Findings）引入 Proactive Agent Planning（主动式智能体规划），要求 agents 预测澄清需求、调用工具获取信息并生成规划。CEP（Clarification-Execution-Planning，澄清-执行-规划）多 agent 框架配合 trajectory tuning（轨迹调优）和 memory recollection（记忆回溯）在 Ask-before-Plan benchmark 上超越基线方法。

## 核心论点
- 主动式 agents 应在模糊指令上先提问再规划
- CEP 多 agent 框架分离澄清、执行和规划
- Trajectory tuning + memory recollection 改善主动式规划
- 新 benchmark 用于真实主动式规划评估

## 关键引述
> "Proactive agents should ask before planning on ambiguous instructions" — 核心原则：主动式 agents 应在模糊指令上先提问再规划

## 关联
- [[IntentRecommendation]] — 主动式规划作为意图推荐
- [[AskBeforePlan]] — 引入的 CEP 框架
- [[IntentRL]] — 强化学习与 trajectory tuning 相关
- [[PIRABench]] — 主动式意图推荐评测基准关联