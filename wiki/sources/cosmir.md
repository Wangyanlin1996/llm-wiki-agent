---
title: "COSMIR：链式编排结构化记忆用于长上下文迭代推理"
type: source
tags: [multi-agent-long-context]
sources: [cosmir]
source_file: raw/papers/cosmir.pdf
last_updated: 2026-07-24
arxiv_id: "2510.04568"
authors: ["Naman Gupta", "S. Gowaikar", "Arun Iyer", "Kirankumar Shiragur", "Ramakrishna Bairi", "Rishikesh Maurya", "Ritabrata Maiti", "Sankarshan Damle", et al.]
year: 2025
venue: "arXiv.org"
citation_count: 1
doi: "10.48550/arXiv.2510.04568"
---

## 概要
COSMIR 针对 Chain-of-Agents (CoA) 中自由文本摘要传递丢失关键细节和放大早期错误的问题，用结构化记忆替代 ad hoc 消息传递。Planner agent 将用户查询分解为可检查的子问题；worker agents 通过固定微循环（Extract→Infer→Refine）处理文本分段并写入共享记忆；Manager agent 直接从记忆综合最终答案。在 HELMET suite 的长上下文 QA 上，COSMIR 减少了传播阶段的信息损失并提高了准确率。

## 关键贡献
- 用结构化记忆替代 CoA 中的自由文本摘要传递
- Planner→worker micro-cycle (Extract/Infer/Refine)→Manager 三阶段架构
- 提高长程聚合的忠实性和可审计性，减少传播阶段信息损失

## 关键引用
> "COSMIR replaces ad hoc messages with a structured memory. A Planner agent first turns a user query into concrete, checkable sub-questions."

## 关联
- [[ChainOfAgents]] — COSMIR 是 CoA 的结构化记忆改进
- [[ChowLiuCoA]] — 同一研究团队的 chunk 排序优化工作
- [[StructuredAgentMemory]] — 结构化智能体记忆的新范式

## 矛盾
- (暂无)
