---
title: "覆盖率而非均值：可信检索评估的语义分层"
type: source
tags: ['semantic-retrieval', 'evaluation']
sources: [coverage-not-averages]
source_file: raw/papers/coverage-not-averages.pdf
last_updated: 2026-07-02
arxiv_id: "2604.20763"
authors: ["Andrew Klearman", "Radu Revutchi", "Rohin Garg", "Rishav Chakravarti", "Samuel Marc Denton", "Yuan Xue"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要

检索质量是 RAG 准确性与鲁棒性的主要瓶颈，但当前评估依赖启发式构造的 query 集，引入隐含的内在偏差。本文将检索评估形式化为统计估计问题：当评估 query 来自在检索 regime 上结构性异质的总体时，忽略该结构会导致有偏估计与误导性置信。论文通过 BEIR 中 NFCorpus 的实证分析揭示——大量高文档量的语义聚类仅被极少量甚至零 query 覆盖（例如 26 个聚类占语料 17.3% 但仅 1.1% 的 query），而这些欠覆盖区域恰恰是检索性能最弱之处，使聚合指标系统性高估真实检索质量。为此提出**语义分层（semantic stratification）**：用 LLM 提取实体构造语义图、用 Leiden 社区检测形成可解释全局聚类，并沿语义层与结构层（相关性离散度）定义检索 regime，为缺失层系统生成 query。该框架提供跨检索 regime 的形式化语义覆盖保证、可解释的失败模式可见性，并证明分层评估比聚合指标更稳定透明、更支撑可信决策。

## 关键贡献

- **检索评估的统计估计形式化**：将评估建模为分层统计估计，证明当某 regime 在评估集中完全缺失时产生不可约偏差——即使增大评估集也无法消除
- **语义分层框架**：基于实体聚类 + Leiden 社区检测构造语料级语义结构，沿语义层和结构层（相关性离散度）定义检索 regime，系统为缺失层生成 query
- **实证揭示覆盖缺口**：NFCorpus 中 17.3% 语料占比的语义区域仅获 1.1% query 覆盖，欠覆盖聚类 nDCG@10 更低却被聚合指标掩盖

## 关键引用

> "If a retrieval regime S_k is entirely missing from the evaluation set ... its contribution is systematically excluded, yielding irreducible bias regardless of evaluation set size."

## 关联

- [[RetrievalEvaluation]] — 本文是该概念的核心方法论贡献，提供检索评估的形式化统计估计视角与覆盖保证
- [[RetrievalAugmentedGeneration]] — 检索质量是 RAG 准确性的主要瓶颈，本文改进的评估方法直接服务于 RAG 系统可靠性
- [[rare-redundancy-eval]] — 互补关系：本文从语料语义覆盖维度、后者从高冗余相似度维度共同揭示聚合指标的失效

## 矛盾

无已知矛盾。
