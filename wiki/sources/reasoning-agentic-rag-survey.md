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

检索增强生成（RAG）通过集成外部检索克服 LLM 的静态预训练知识局限，但早期基于静态管线的 RAG 在真实世界场景（复杂推理、动态检索、多模态集成）中力不从心。近期领域转向 **Reasoning Agentic RAG**——将决策与自适应工具使用直接嵌入检索过程的范式。本综述将方法分为两大系统：**System 1 预定义推理**（遵循固定模块化管线增强推理，如路由触发、循环反馈、树状层次、混合模块），快速结构化但缺乏灵活性；**System 2 自主推理**（模型在推理时自主编排工具交互，含基于提示的 ReAct/Self-Ask 与基于训练的 Search-R1/R1-Searcher/DeepResearcher），慢速审议但自适应。该二分类比认知科学的双系统理论。综述分析两种范式下的代表技术，覆盖架构设计、推理策略和工具协调，并讨论关键研究挑战与提升灵活性、鲁棒性、适用性的未来方向。

## 关键贡献

- **System 1 vs System 2 双范式分类法**：将 Reasoning Agentic RAG 系统分为预定义推理（结构化、模块化、规则驱动）与自主推理（自主、自适应、模型驱动决策），并对应认知科学双系统理论
- **预定义推理四变体**：路由触发（RAGate 条件检索）、循环反馈（Self-RAG 自反思迭代）、树状层次（RAPTOR 递归摘要）、混合模块（Adaptive-RAG/Modular-RAG 可组合模块）
- **自主推理双实现策略**：基于提示（ReAct 交错推理与工具使用、Self-Ask 分解、Search-O1 生成中检索）与基于训练（DeepRetrieval 查询重写、Search-R1/R1-Searcher 两阶段结果驱动 RL、ReZero 持久重试、DeepResearcher 开放网络训练）

## 关键引用

> "Agentic RAG treats retrieval not as a one-off pre-processing step, but as a dynamic, context-sensitive operation guided by the model's ongoing reasoning process."

## 关联

- [[AgenticRetrieval]] — 本文是该概念的双范式理论框架，System 1/System 2 分类法直接定义了 agent 驱动检索的设计空间
- [[RetrievalAugmentedGeneration]] — 描绘 RAG 从静态管线向 Agentic RAG 的演进路径，是 RAG 概念的发展综述

## 矛盾

无已知矛盾。
