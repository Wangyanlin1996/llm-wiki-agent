---
title: "HANSEL: Extracting Breadcrumbs from Web Agent Trajectories for Interactive Verification"
type: source
tags: [agent-explainability, interactive-verification, web-agent, trajectory]
date: 2026-06-17
source_file: raw/papers/hansel-web-agent-verification.pdf
arxiv_id: "2606.18671"
authors: ["Yujin Zhang", "Daye Nam"]
venue: arXiv preprint
citation_count: pending
---

## Summary

HANSEL（Highlighting Agent Navigation Steps as Evidence Links）将 web agent 的验证从"被动阅读"重构为"交互式验证"：从 agent 轨迹中提取证据页面和片段，呈现为可导航的交互视图（保留筛选状态、搜索查询、滚动位置）。当 agent 的答案无法追溯到任何已访问页面时，HANSEL 显式标记这一缺口。在 AssistantBench 和 Online-Mind2Web 的 45 个任务上达到 83.7% precision / 88.8% recall，轨迹体积减少 61.6%。

## Key Claims

- **现有透明机制（完整轨迹日志、源链接、截图、LLM 生成摘要）将验证视为被动阅读任务**——用户需在海量日志中筛选或信任可能不忠实的解释
- **将验证重构为交互活动**——用户可导航到证据页面并验证 agent 如何得出答案
- **不可追溯时显式标记缺口**——而非生成可能不忠实的解释来掩盖
- 技术评估：83.7% precision、88.8% recall 识别证据页面；轨迹体积减少 61.6%
- 用户研究（14人）：显著降低任务完成时间和感知努力；可用性、验证便利性、错误识别评分显著提高

## Key Quotes

> "Existing transparency mechanisms ... treat verification as a passive reading task, leaving users to sift through overwhelming logs or trust potentially unfaithful explanations."

> "When the agent's answer cannot be traced to any visited page, HANSEL explicitly flags this gap."

> "Reframing verification as an interactive activity, rather than passive consumption of agent explanations, leads to more efficient human oversight of AI agents."

## Connections

- [[ExecutionProvenance]] — HANSEL 是证据追踪的交互式实现
- [[AgentExplainability]] — 交互式验证是 agent 可解释性的新范式
- [[agent-traces-to-trust]] — HANSEL 实现了该综述呼吁的 evidence tracing
- [[AgentAccountability]] — 可追溯缺口标记增强问责

## Contradictions

- 与 LLM 生成摘要式解释的范式形成张力：HANSEL 认为被动阅读 LLM 摘要不足以验证，需交互式证据导航
