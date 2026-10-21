---
title: "WebSwarm：深度与广度网络搜索的递归多智能体编排"
type: source
tags: [multi-agent-long-context]
sources: [webswarm]
source_file: raw/papers/webswarm.pdf
last_updated: 2026-07-24
arxiv_id: "2607.08662"
authors: ["Xiaoshuai Song", "Lian Zhang", "Kangzhi Zhao", "Yutao Zhu", "Zhongyuan Wang", "Guanting Dong", "Jinghan Yang", "Han Li", et al.]
year: 2026
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
WebSwarm 是一种渐进递归委派框架，在推理期间联合构建任务分解、递归扩展和 agent 协作。动态实例化搜索节点，每个节点耦合局部目标和搜索模式。节点可自行解决目标或进一步委派子节点；解决后返回证据和结果向上传递，使父节点能进一步扩展、修订或聚合。WebSwarm 首先探测任务相关信息在 web 上的组织方式以引导后续节点扩展，并在同质兄弟节点间复用过程级经验。在 BrowseComp-Plus、WideSearch 等基准上持续超越单 agent 和多 agent 基线。

## 关键贡献
- 递归委派框架：任务分解 + 递归扩展 + agent 协作联合构建
- 动态节点实例化 + 过程级经验跨兄弟节点复用
- 解决单 agent 长轨迹上下文限制问题

## 关键引用
> "WebSwarm dynamically instantiates agentic search nodes, each coupling a local objective with a search mode that specifies how the node should organize search and collaboration."

## 关联
- [[SwarmResearch]] — 同为全局/局部上下文分离的编排框架
- [[RecursiveAgentDelegation]] — 递归智能体委派
- [[MultiAgentLongContext]] — 多智能体解决长搜索轨迹

## 矛盾
- (暂无)
