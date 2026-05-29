---
title: "Flexible Agent Alignment with Goal Inference from Open-Ended Dialog"
type: source
tags: [assistance-games, goal-inference, agent-alignment, preference-construction, LLM-agent]
date: 2025-08-20
source_file: raw/papers/good-agent-alignment.md
last_updated: 2026-05-29
---

## 概要
提出 Open-Universe Assistance Games (OU-AGs) 框架，将 Assistance Games 从固定预设偏好扩展到开放对话场景中的动态自然语言偏好分布，并设计 GOOD 方法从交互过程中提取和排序候选目标，利用 LLM 模拟用户进行概率推断，实现可解释、不确定性感知的偏好表示。

## 核心论点
- 传统 Assistance Games 假设固定预设偏好，不适用于开放对话中目标逐步修正、自然语言表达的场景
- 人类偏好是动态构建而非预先确定的（grounded in cognitive science accounts of preference construction）
- GOOD 通过在线目标推断实现数据高效的对齐，无需大规模离线偏好数据集

## 关键引述
> "Existing assistance game formulations assume fixed, predefined preferences, an assumption that breaks down in open-ended dialogue where goals are revised incrementally and expressed in natural language" — OU-AGs 的动机

> "GOOD produces semantically coherent goal representations and improves alignment with user intent across domains" — 三个领域评测结果

## 关联
- [[IntentUnderstanding]] — GOOD 解决意图理解中的目标推断问题
- [[AssistanceGames]] — OU-AGs 扩展的核心形式化框架
- [[IntentRL]] — RL 方法与 Assistance Games 形式化的对比
- [[IntentSignalTheory]] — I-hat（可观测代理）与 OU-AGs 中候选目标的关系