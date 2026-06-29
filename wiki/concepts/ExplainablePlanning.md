---
title: "可解释规划（Explainable Planning）"
type: concept
tags: [agent-evaluability, explainable-planning, mental-model]
sources: [explainable-human-ai-interaction]
last_updated: 2026-06-29
---

可解释规划指从规划视角研究人机交互中的可解释性，核心思想是"解释即规划"：向人解释的过程本身可被建模为一个规划问题。[[explainable-human-ai-interaction]] 系统论述该范式，强调 AI agent 必须超越仅基于自身世界模型规划，而要考虑回路中人类的心智模型（mental model），利用心智模型要么顺应人类期望、要么通过解释性通信改变人类期望。

该范式为 [[AgentExplainability]] 中的"交互式解释"与"意图共创"提供了深层理论模型，也支撑闭环验证中"因果溯因"的解释生成。值得注意的是，同一套心智模型机制既可用于解释/对齐，也可用于混淆与欺骗，因此可解释规划需与形式化保障结合。
