---
title: "FinLongDocAgent：金融报告中的文档级数值推理多智能体"
type: source
tags: [multi-agent-long-context]
sources: [finlongdoc-agent]
source_file: raw/papers/finlongdoc-agent.pdf
last_updated: 2026-07-24
arxiv_id: "2604.03664"
authors: ["Yi-Cheng Wang", "Wei-An Wang", "Chu-song Chen"]
year: 2026
venue: "arXiv.org"
citation_count: 0
doi: "10.48550/arXiv.2604.03664"
---

## 概要
FinLongDocAgent 是一种多智能体多轮 RAG 方法，用于金融长文档中的数值推理。它迭代地检索证据、执行中间计算并跨轮验证结果。针对年度报告超过 129K tokens 加剧的 context rot 问题和多步数值推理错误，该框架通过迭代检索和验证提升可靠性。引入 FinLongDocQA 数据集覆盖单表和跨表场景。

## 关键贡献
- 多智能体多轮 RAG 迭代检索 + 中间计算 + 跨轮验证
- 解决金融长文档 context rot 和多步数值推理错误
- 引入 FinLongDocQA 数据集覆盖单表和跨表数值推理

## 关键引用
> "We propose FinLongDocAgent, a Multi-Agent Multi-Round Retrieval-Augmented Generation (RAG) approach that iteratively retrieves evidence, performs intermediate calculations, and verifies results across rounds."

## 关联
- [[SPDRAG]] — 同为多智能体文档级 RAG 方法
- [[MultiAgentRAG]] — 多智能体 RAG 在金融领域的应用
- [[NumericalReasoning]] — 长文档数值推理

## 矛盾
- (暂无)
