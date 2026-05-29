---
title: "Satori"
type: source
tags: [intent-understanding, proactive-agent, AR-assistant, BDI]
date: 2024-10-16
source_file: raw/papers/satori.md
last_updated: 2026-05-28
---

## 概要
Satori 是一个主动式 AR 助手，集成 Belief-Desire-Intention (BDI，信念-愿望-意图) 框架与多模态 LLM，为物理任务提供上下文适宜的指导。它在无需手动配置的情况下匹配 Wizard-of-Oz 性能，改善了 AR 辅助的泛化能力。

## 核心论点
- BDI framework 为 AR 实现主动式意图建模
- Multi-modal LLM + BDI 无需手动配置即可匹配 WoZ 性能
- 无需手动启发式规则
- 主动式 AR 指导改善任务完成率

## 关键引述
> "Multi-modal LLM + BDI matches WoZ performance without manual configurations" — 关键结果：多模态 LLM 配合 BDI 无需手动配置即可匹配 Wizard-of-Oz 性能

## 关联
- [[IntentUnderstanding]] — Satori 通过 BDI 框架建模意图
- [[Satori]] — 引入的主动式 AR 助手概念
- [[ContextAgent]] — 类似的感知驱动的主动式 agent
- [[IntentRecommendation]] — 通过 AR 指导的主动式推荐