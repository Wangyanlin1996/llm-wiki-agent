---
title: "超越参数：LLM 上下文增强技术综述"
type: source
tags: ['semantic-retrieval', 'rag-architecture', 'survey']
sources: [beyond-parameters-survey]
source_file: raw/papers/beyond-parameters-survey.pdf
last_updated: 2026-07-02
arxiv_id: "2604.03174"
authors: ["Prakhar Bansal", "Shivangi Agarwal"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要

LLM 在参数中编码了海量世界知识，但仍受静态知识、有限上下文窗口和弱结构化因果推理的根本限制。本综述以"推理时提供的结构化上下文程度"为统一轴线，系统覆盖四类上下文增强技术：in-context learning（ICL）、RAG、GraphRAG 和 CausalRAG。综述将三组失败差距映射到四种范式的覆盖：知识差距（参数中未编码的事实）、检索差距（相关证据未浮现）、推理差距（虽有相关证据但因果不连贯）。ICL 仅部分覆盖知识差距，RAG 覆盖知识和检索差距但推理有限，GraphRAG 增强关系推理和全局综合，CausalRAG 引入有向因果结构支持反事实推理。综述的方法论贡献包括：透明文献筛选协议、claim-audit 框架（将高影响声明链接到原始来源和置信度级别：高/中/新兴）、结构化跨论文证据综合表。定量证据矩阵明确标注指标定义和范围约束，区分高置信度发现（如"RAG 改善事实接地"——多基准验证）与新兴结果（如"CausalRAG 改善因果连贯"——有限规模证据）。最终提出面向部署的决策框架：何时用何种范式。

## 关键贡献

- **ICL→RAG→GraphRAG→CausalRAG 统一演进轴**：以结构化上下文程度为单轴，映射三组失败差距（知识/检索/推理）到四种范式覆盖——提供连贯的范式比较框架
- **claim-audit 框架**：将高影响技术声明链接到原始来源并标注置信度（高/中/新兴），区分多基准验证的成熟发现与窄基准的新兴结果——提高综述的方法论严谨性
- **定量证据矩阵**：明确标注指标定义、单位和范围约束，强调 within-study 比较不可跨论文直接排名——避免综述中常见的数值误读
- **部署导向决策框架**：Prompting 适合轻量窗口内任务、RAG 是事实接地默认、GraphRAG 适合多跳实体中心问题、CausalRAG 适合根因和高风险解释——为实践者提供范式选择指南

## 关键引用

> "We frame the progression from prompting to RAG, GraphRAG, and CausalRAG as a systematic response to these gaps. Each step introduces richer contextual structure and typically trades higher indexing complexity for better faithfulness and reasoning quality."

> "All numerical deltas in Table 2 are within-study comparisons under each cited paper's own models, dataset split, and evaluation protocol; they are not cross-paper rankings."

## 关联

- [[RetrievalAugmentedGeneration]] — 本文是该概念的核心综述之一，将 RAG 定位在 ICL→RAG→GraphRAG→CausalRAG 演进轴的中间位置
- [[GraphRAG]] — 本文将 GraphRAG 定位为 RAG 的结构化增强，覆盖关系推理和全局综合差距
- [[RetrievalEvaluation]] — claim-audit 框架为检索评估引入证据置信度分级方法论
- [[rag-comprehensive-survey]] — 两者均为 RAG 综述：本文聚焦范式演进轴，后者聚焦架构四分类法
- [[rag-security-privacy]] — 本文的部署决策框架与后者的部署感知安全分析互补

## 矛盾

无已知矛盾。综述明确标注 CausalRAG 的因果连贯改善证据为"中等置信度"（仅限单一案例研究），保持方法论审慎。
