---
title: "SwarmResearch：编排编码智能体进行开放式发现"
type: source
tags: [multi-agent-long-context]
sources: [swarmresearch]
source_file: raw/papers/swarmresearch.pdf
last_updated: 2026-07-24
arxiv_id: "2607.02807"
authors: ["Yuvraj Virk", "Zack Edds", "Chun Xia", "Lingming Zhang"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
SwarmResearch 是一种 orchestrator-subagent 架构，Shepherd Agent 使用全局上下文引导一群 Search Agent，每个在其各自的 git 分支上以局部上下文操作。解决了长程编码 agent 在单一长运行 agent 中积累上下文和仅暴露单一程序状态编辑的两个 harness 级设计问题。在开放式优化任务上，SwarmResearch 在 15 个任务中的 13 个上发现更好或相当的解决方案，通过更高级别探索实现。

## 关键贡献
- Shepherd Agent 全局上下文 + Search Agents 局部上下文 + git 分支隔离
- 解决长程 agent 上下文累积和单程序状态限制问题
- 15 个任务中 13 个发现更好/相当方案，orchestrator 引导的自适应并行

## 关键引用
> "SwarmResearch, an orchestrator-subagent harness in which a Shepherd Agent uses global context to steer a population of Search Agents, each operating with local context in their respective git branch."

## 关联
- [[GlobalLocalContextSplit]] — 全局/局部上下文分离范式
- [[MultiAgentLongContext]] — 多智能体长程编码任务
- [[OpenEndedDiscovery]] — 开放式发现的多智能体编排

## 矛盾
- (暂无)
