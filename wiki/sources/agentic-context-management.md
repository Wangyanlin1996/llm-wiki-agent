---
title: "Agentic Context Management：将智能体记忆和成本视为生命周期与架构问题"
type: source
tags: [multi-agent-long-context]
sources: [agentic-context-management]
source_file: raw/papers/agentic-context-management.pdf
last_updated: 2026-07-24
arxiv_id: "2607.21503"
authors: []
year: 
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
本文指出生产 AI agent 的失败更多因为无法管理推理上下文中的内容（对话历史、大 prompt、工具定义、膨胀的工具输出），而非推理能力不足。Agent 淹没在自己累积的历史中。提出将上下文管理视为生命周期和架构问题，而非单纯的推理问题。提供了评估工具和研究数据。

## 关键贡献
- 将 agent 上下文管理从推理问题重构为生命周期+架构问题
- 识别上下文膨胀根源：对话历史/prompt/工具定义/工具输出
- 评估工具和研究数据开源

## 关键引用
> "Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context."

## 关联
- [[MultiAgentLongContext]] — 上下文管理的架构视角
- [[ContextLifecycle]] — 上下文生命周期管理
- [[AgentContextArchitecture]] — 智能体上下文架构

## 矛盾
- (暂无)
