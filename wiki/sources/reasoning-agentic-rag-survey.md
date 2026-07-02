---
title: "推理 RAG 的 System 1 与 System 2：推理 Agentic RAG 综述"
type: source
tags: ['semantic-retrieval', 'agentic-retrieval', 'survey']
sources: [reasoning-agentic-rag-survey]
source_file: raw/papers/reasoning-agentic-rag-survey.pdf
last_updated: 2026-07-02
arxiv_id: "2506.10408"
authors: ["Jintao Liang", "Gang Su", "Huifeng Lin", "You Wu", "Rui Zhao", "Ziyue Li"]
year: 2025
venue: "arXiv"
citation_count: pending
---

## 概要
综述 Reasoning Agentic RAG，将方法分为两大系统：预定义推理（System 1，遵循固定模块化管线增强推理）和自主推理（System 2，模型在推理时自主编排工具交互）。分析两种范式下的代表技术，覆盖架构设计、推理策略和工具协调。讨论关键研究挑战并提出提升灵活性、鲁棒性和适用性的未来方向。与 AgentLoop 框架直接对应。

## 关键贡献
- System 1（预定义推理管线）vs System 2（自主工具编排）
- 推理 Agentic RAG 双范式分析
- 与 AgentLoop 编排器→Skill 执行→闭环验证直接对应

## 关联
- [[AgenticRetrieval]] — 关联描述
- [[RetrievalAugmentedGeneration]] — 关联描述

## 矛盾
- (暂无)
