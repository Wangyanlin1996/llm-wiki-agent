---
title: "Chain-of-Agents 中的 Chow-Liu 排序用于长上下文推理"
type: source
tags: [multi-agent-long-context]
sources: [chow-liu-coa]
source_file: raw/papers/chow-liu-coa.pdf
last_updated: 2026-07-24
arxiv_id: "2603.09835"
authors: ["Naman Gupta", "Vaibhav Singh", "Arun Iyer", "Kirankumar Shiragur", "Pratham Grover", "Ramakrishna Bairi", "Ritabrata Maiti", "Sankarshan Damle", et al.]
year: 2026
venue: "arXiv.org"
citation_count: 0
doi: "10.48550/arXiv.2603.09835"
---

## 概要
本文研究 Chain-of-Agents (CoA) 框架中的 chunk 排序问题。CoA 通过有界记忆近似处理长上下文，引入了有损信息瓶颈，使最终证据状态依赖于 chunk 处理顺序。作者使用 Chow-Liu 树学习优先处理强相关 chunk 的依赖结构，并通过广度优先遍历生成 chunk 排序。在三个长上下文基准上，该方法在答案相关性和精确匹配准确率方面持续优于默认文档排序和语义分数排序。发表于 ICLR 2026 Workshop MemAgents。

## 关键贡献
- 形式化 CoA 中的 chunk 排序问题：有界记忆近似引入有损信息瓶颈
- 使用 Chow-Liu 树学习 chunk 间依赖结构，广度优先遍历生成最优排序
- 在三个长上下文基准上持续优于默认排序和语义排序

## 关键引用
> "A breadth-first traversal of the resulting tree yields chunk orderings that reduce information loss across agents and consistently outperform both default document-chunk ordering and semantic score-based ordering."

## 关联
- [[ChainOfAgents]] — 直接优化 CoA 框架中的 chunk 排序
- [[COSMIR]] — 同一团队的 CoA 改进工作
- [[ChunkOrderingOptimization]] — chunk 排序优化的理论基础

## 矛盾
- (暂无)
