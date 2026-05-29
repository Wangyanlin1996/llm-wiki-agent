---
title: "RECAP"
type: source
tags: [intent-understanding, intent-rewriting, agent-planning, benchmark]
date: 2025-09-04
source_file: raw/papers/recap.md
last_updated: 2026-05-28
---

## 概要
RECAP 将意图理解重新定义为 intent rewriting（意图重写）——将模糊的用户-agent 对话转化为简洁的目标表征以服务于 agentic planning（智能体规划）。它捕获了歧义、意图漂移、模糊性和混合目标对话等挑战，并提供基于 LLM 的评估器衡量规划效用。

## 核心论点
- Intent rewriting（意图重写，而非分类）是 agentic planning 的正确框架
- 歧义、漂移和混合目标需要重写而非检测
- 基于 DPO 的重写器比基于提示的方法改善规划效用

## 关键引述
> "Intent rewriting is the right framing for agentic planning" — 重构论点：意图重写才是智能体规划的合适框架

## 关联
- [[IntentUnderstanding]] — RECAP 重构了意图理解的方式
- [[RECAP]] — 引入的重写框架
- [[IntentRL]] — 意图的强化学习与重写相关
- [[AskBeforePlan]] — 主动式澄清与重写互补
- [[PersonalAlign]] — 个性化对齐与重写目标相关