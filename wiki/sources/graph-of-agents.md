---
title: "Graph of Agents：基于涌现多智能体协作的原则性长上下文建模"
type: source
tags: [multi-agent-long-context]
sources: [graph-of-agents]
source_file: raw/papers/graph-of-agents.pdf
last_updated: 2026-07-24
arxiv_id: "2509.21848"
authors: ["Taejong Joo", "Shu Ishida", "Ivan Sosnovik", "Bryan Lim", "S. Rezaei-Shoshtari", "Adam Gaier", "Robert Giaquinto"]
year: 2025
venue: "arXiv.org"
citation_count: 1
doi: "10.48550/arXiv.2509.21848"
---

## 概要
Graph of Agents (GoA) 将模型无关的长上下文建模形式化为压缩问题，提出信息论压缩目标。GoA 动态构建输入依赖的协作结构来最大化该目标。对于 Llama 3.1 8B 和 Qwen3 8B，在六个文档 QA 基准上，GoA 比 RAG 提升 5.7%，比固定协作结构的多智能体基线提升 16.35%。仅用 2K 上下文窗口，GoA 在 LongBench 上超越了 128K 上下文窗口的 Llama 3.1 8B。

## 关键贡献
- 将模型无关的长上下文建模形式化为信息论压缩问题
- 动态构建输入依赖的协作结构 (Graph of Agents) 最大化压缩目标
- 仅用 2K context 在 LongBench 上超越 128K Llama 3.1 8B，有效上下文长度剧增

## 关键引用
> "GoA improves the average F1 score of retrieval-augmented generation by 5.7% and a strong multi-agent baseline using a fixed collaboration structure by 16.35%."

## 关联
- [[ChainOfAgents]] — GoA 是 CoA 的原则性推广，用信息论形式化压缩目标
- [[MultiAgentLongContext]] — 多智能体长上下文建模的核心方法
- [[InformationTheoreticCompression]] — 信息论压缩目标的形式化基础

## 矛盾
- (暂无)
