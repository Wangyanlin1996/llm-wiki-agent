---
title: "HAKARI-Bench：统一条件下检索架构与效率设置对比的轻量级基准"
type: source
tags: ['semantic-retrieval', 'hybrid-retrieval', 'evaluation']
sources: [hakari-bench]
source_file: raw/papers/hakari-bench.pdf
last_updated: 2026-07-02
arxiv_id: "2606.22778"
authors: ["Yuichi Tateno"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要

随着 RAG 和语义搜索的普及，选择合适的文本嵌入和检索配置变得重要但困难。大规模检索基准（MTEB、MMTEB）全面但太重，难以在开发中重复运行，且缺乏在生产时设置（降维、量化、重排）下跨多模型同条件对比的基础设施。HAKARI-Bench 是轻量级评估基础设施，将现有检索基准重建为小数据集（Nano-sets）：35 基准 / 551 检索任务 / 43 语言统一格式。每个任务共享语料库、查询、相关性标签和固定候选集的通用格式，支持五族检索模型（BM25、稠密、稀疏、晚交互、重排器）及其效率变体（Matryoshka 降维、int8/binary 量化、float 重排）在同条件下评估。"HAKARI"来自日语"秤"（衡量），反映基准的测量比较目标。评测 55 模型（稠密 33、稀疏 4、晚交互 6、重排器 11、BM25 1），在公共模型和交叉任务上，整体排名与 MTEB 检索 v2、MMTEB v2 检索和 English BEIR(full) 的 Spearman 相关性分别达 0.983、0.975、0.973，Pearson 达 0.981、0.969、0.974。Borda 分数聚合也保持高相关，证明 Nano-sets 高保真复现大规模评估排名。基准支持快速模型选择、回归检测和质量-效率 Pareto 前沿分析。

## 关键贡献

- **轻量级多语言多域检索评估基础设施**：35 基准 / 551 任务 / 43 语言 Nano-set 统一格式，使 551 检索任务在现实速度下可重复测量——解决大规模基准重复评估成本过高问题
- **五族检索模型 + 效率变体同条件对比**：首次在统一框架下同时评估 BM25/稠密/稀疏/晚交互/重排器及其降维、量化、重排变体——填补跨架构效率设置对比空白
- **排名复现性高保真验证**：通过三次独立对比证明 Nano-set 整体排名与 MTEB v2 / MMTEB v2 / BEIR(full) Spearman >0.97——为轻量级评估作为排名代理提供统计证据
- **质量-效率 Pareto 前沿**：揭示 binary 量化鲁棒性由训练特性决定（非规模或维度解释），重排器是否超越稠密随任务类型和架构变化——为部署决策提供可见的差异

## 关键引用

> "HAKARI-Bench is not a replacement for full evaluation; rather, it supports rapid model selection, regression detection, and reading the quality–efficiency Pareto frontier under the same conditions."

> "Robustness to binary quantization is determined by a model's training characteristics (not explained by size or dimension), and whether a reranker beats dense changes with the task type and architecture."

## 关联

- [[HybridRetrieval]] — 本文是该概念的评估基础设施，支持五族检索模型（含混合）统一对比
- [[RetrievalEvaluation]] — 本文是该概念的核心来源之一，提供轻量级高保真检索评估方法论
- [[bm25-corrective-rag]] — 后者在特定金融文档上对比 10 种策略，本文提供跨 35 基准的通用五族对比框架
- [[hteb-harder-embedding-bench]] — 两者均为嵌入/检索评估创新：本文轻量级跨架构对比，后者多维度动态鲁棒性
- [[rag-evaluation-survey]] — 后者综述 RAG 评估框架，本文为其提供具体的检索评估基础设施实例

## 矛盾

无已知矛盾。基准明确声明"非全量评估替代品"而是"快速排名代理"，保持方法论审慎。
