---
title: "SPD-RAG：每文档一子智能体的检索增强生成"
type: source
tags: [multi-agent-long-context]
sources: [spd-rag]
source_file: raw/papers/spd-rag.pdf
last_updated: 2026-07-24
arxiv_id: "2603.08329"
authors: ["Yagiz Can Akay", "Muhammed Yusuf Kartal", "Esra Alparslan", "Faruk Ortakoyluoglu", "Arda Akpinar"]
year: 2026
venue: "arXiv.org"
citation_count: 2
doi: "10.48550/arXiv.2603.08329"
---

## 概要
SPD-RAG 是一种层次化多智能体框架，沿文档轴分解跨文档 QA 问题。每个文档由专用文档级 agent 处理，仅在其自身内容上操作以实现聚焦检索；coordinator 分发任务并聚合部分答案。Agent 输出通过 token 有界合成层合并（支持大规模语料的递归 map-reduce）。在 LOONG 基准上达到 Avg Score 58.1，超过 Normal RAG (33.0) 和 Agentic RAG (32.8)，而 API 成本仅为全上下文基线的 38%。

## 关键贡献
- 每文档一 agent 的文档级专业化 + coordinator 中心化融合
- Token 有界合成层支持递归 map-reduce 处理大规模语料
- LOONG 基准 Avg 58.1，API 成本仅 38%

## 关键引用
> "Each document is processed by a dedicated document-level agent operating only on its own content, enabling focused retrieval, while a coordinator dispatches tasks to relevant agents and aggregates their partial answers."

## 关联
- [[ChainOfAgents]] — SPD-RAG 沿文档轴分解而非文本分段
- [[MultiAgentRAG]] — 多智能体 RAG 的文档级专业化范式
- [[HierarchicalMapReduce]] — 层次化 map-reduce 处理大规模语料

## 矛盾
- (暂无)
