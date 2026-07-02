---
title: "GraphRAG 是否必要？从基础 RAG 到图/Agent 解决方案"
type: source
tags: ['semantic-retrieval', 'graphrag']
sources: [is-graphrag-needed]
source_file: raw/papers/is-graphrag-needed.pdf
last_updated: 2026-07-02
arxiv_id: "2606.25656"
authors: ["Long Chen", "Ryan Razkenari", "Yuxuan Zhou", "Yuan Tian", "Rahul Ghosh", "Venkatesh Pappakrishnan", "Disha Ahuja", "Vidya Sagar Ravipati"]
year: 2026
venue: "ACL 2026 GEM Workshop"
citation_count: pending
---

## 概要
引入 9 种标准化 RAG 场景评估框架，在半结构化知识库上对比 Regular RAG、GraphRAG、Modular RAG 和 Agentic RAG。提出新型上下文工程方法解决 GraphRAG/Agentic RAG 的上下文溢出，token 使用降低 19-53%。关键发现：检索-生成差距——扩展检索不比例提升生成质量，检索导向指标高估了高级检索的收益。为构建生产级智能 RAG 系统提供数据驱动洞察。

## 关键贡献
- 9 种 RAG 场景标准化对比框架
- 上下文工程方法降低 19-53% token
- 检索-生成差距：扩展检索≠提升生成

## 关联
- [[GraphRAG]] — 关联描述
- [[RetrievalAugmentedGeneration]] — 关联描述
- [[RetrievalEvaluation]] — 关联描述

## 矛盾
- (暂无)
