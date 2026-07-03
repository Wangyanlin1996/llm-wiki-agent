---
title: "RAG 综合综述：架构、增强与鲁棒性前沿"
type: source
tags: ['semantic-retrieval', 'rag-architecture', 'survey']
sources: [rag-comprehensive-survey]
source_file: raw/papers/rag-comprehensive-survey.pdf
last_updated: 2026-07-02
arxiv_id: "2506.00054"
authors: ["Chaitanya Sharma"]
year: 2025
venue: "arXiv"
citation_count: pending
---

## 概要

检索增强生成（RAG）通过在推理时检索外部证据来条件化生成，已成为增强 LLM 的重要范式，但引入了检索质量、接地保真度、管线效率和对抗噪声鲁棒性等新挑战。本综述提供 RAG 系统的综合合成，提出分类法将架构分为四类：retriever-centric（检索器为核心创新）、generator-centric（生成器为核心）、hybrid（联合协调）和 robustness-oriented（鲁棒性导向）。系统分析跨检索优化、上下文过滤、解码控制和效率增强的改进，在短形式和多跳 QA 任务上进行对比性能分析。综述形式化了 RAG 的数学基础：P(y|x) ≈ Σ P(y|x,d_i)·P(d_i|x)，分解为检索相关性 P(d_i|x) 和条件生成 P(y|x,d_i) 两个关键概率。检索器-centric 设计涵盖查询增强（分解、重写、生成式重表述）和检索粒度优化。综述回顾了最先进的评估框架和基准，揭示反复出现的权衡：检索精度与生成灵活性、效率与忠实度、模块化与协调性。开放挑战包括自适应检索架构、实时检索集成、多跳证据结构化推理和隐私保护检索机制。

## 关键贡献

- **RAG 架构四分类法**：retriever-centric / generator-centric / hybrid / robustness-oriented——基于核心创新发生位置的系统分类，为 RAG 设计提供结构化导航
- **检索-生成权衡的系统分析**：揭示检索精度 vs 生成灵活性、效率 vs 忠实度、模块化 vs 协调性三组反复出现的权衡——为架构选择提供决策框架
- **数学形式化与组件分解**：将 RAG 形式化为 P(y|x) = Σ P(y|x,d)·P(d|x)，明确检索相关性和条件生成两个关键概率——为系统性分析提供统一框架
- **评估框架与基准综述**：覆盖检索感知评估、鲁棒性测试和联邦检索设置——桥接传统 IR 评估与 LLM 驱动评估

## 关键引用

> "Integrating retrieval with generation introduces unique challenges: retrieval noise and redundancy can degrade output quality; misalignment between retrieved evidence and generated text can lead to hallucinations; and pipeline inefficiencies and latency make deployment costly at scale."

> "Our analysis reveals recurring trade-offs between retrieval precision and generation flexibility, efficiency and faithfulness, and modularity and coordination."

## 关联

- [[RetrievalAugmentedGeneration]] — 本文是该概念的核心综述，提供四分类法和数学形式化
- [[DenseRetrieval]] — 综述覆盖检索器-centric 设计，稠密检索是 RAG 检索组件的核心范式
- [[RetrievalEvaluation]] — 综述系统回顾 RAG 评估框架和基准，与该概念直接互补
- [[beyond-parameters-survey]] — 两者均为 RAG 综述：本文聚焦架构分类，后者聚焦 ICL→RAG→GraphRAG→CausalRAG 演进轴
- [[rag-security-privacy]] — 本文将隐私保护检索列为开放挑战，后者提供系统化安全威胁分析

## 矛盾

无已知矛盾。综述客观呈现各架构取向的权衡而非主张某一范式占优。
