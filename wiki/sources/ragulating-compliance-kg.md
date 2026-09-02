---
title: "RAGulating Compliance: 多智能体知识图谱用于监管合规问答（Multi-Agent KG for Regulatory QA）"
type: source
tags: [ontology-graph-retrieval]
sources: [ragulating-compliance-kg]
source_file: raw/papers/ragulating-compliance-kg.pdf
last_updated: 2026-08-31
arxiv_id: "2508.09893"
authors: ["Bhavik Agarwal", "Hemant Sunil Jomraj", "Simone Kaplunov", "Jack Krolick", "Viktoria Rojkova"]
year: 2025
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
本文提出一个多智能体（multi-agent）框架，将 Knowledge Graph（KG）的 SPO 三元组与 RAG 结合，用于监管合规问答（regulatory compliance QA）。系统首先从监管文档中提取三元组，经清洗、归一化、去重后嵌入至统一向量数据库，同时保留原始文本段落作为 provenance。检索阶段在三元组级别进行 kNN 搜索，将匹配的三元组及其关联文本一并送入 LLM 生成答案。在 Electronic Code of Federal Regulations（eCFR）数据上的评估表明，三元组在高精度检索和跨章节导航上显著优于纯文本方法。

## 解决的问题
监管合规领域（如 FDA 医疗器械/药品合规）要求高精度、可验证的问答，但 LLM 存在 hallucination 风险且缺乏领域特异性。现有 RAG 在开放域 QA 表现好，但在监管合规场景——需结构化（KG）与非结构化文本融合——仍被低估和未充分探索。传统 KG 依赖预定义 ontology（如 DBpedia、YAGO），在法规快速演变场景下初始化开销大、适应性差。核心缺口：在无需 ontology 的前提下，通过多智能体从监管文档自动提取、清洗、嵌入三元组，并融合 RAG 实现可追溯、可验证的合规问答。

## 方法与技术
1. **Ontology-free 三元组提取 + provenance 关联**：将语料分割为原子文本段落，对每段用 LLM 信息提取管线提取 SPO 三元组；定义 linking 函数将每个三元组关联至其源文本段落集合，确保可审计性。
2. **三元组嵌入 + 统一向量数据库**：将每个三元组拼接为文本表示 `f(ti)=concat(si,pi,oi)`，用基于 BERT（在 eCFR 上训练）的 embedding 模型编码为向量；向量库存储嵌入、三元组本身和关联文本，实现图推理与文本检索的统一存储。
3. **多智能体编排架构**：两组 agent——KG 构建 agent（文档摄入、三元组提取、归一化/清洗/去重、存储索引）和 QA agent（三元组 kNN 检索、story 构建/合成、答案生成），各 agent 独立运行可单独优化。
4. **Triplet-level kNN 检索 + 文本证据回溯**：查询嵌入后在向量库中用 cosine similarity 做 kNN 搜索取 top-k 三元组，再通过 linking 函数检索关联文本段落，将三元组 + 文本一同送入 LLM 生成答案。
5. **检索子图可视化**：提供三元组子图的交互式可视化，展示跨章节的法规关联。

## 创新点
- **vs. DBpedia/YAGO（预定义 ontology KG）**：采用 ontology-free / schema-light 的 bottom-up 提取策略，适应法规快速演变、数据格式多变，减少初始化开销。
- **vs. 纯文本 RAG**：在 triplet 级别嵌入和检索，捕获"who-did-what-to-whom"核心结构，同时保留文本 provenance 实现可审计性。
- **vs. 单一 LLM QA**：引入多智能体架构将摄入、提取、清洗、索引、检索、生成解耦，实现模块化可扩展。
- **vs. 传统 RAG 评估**：提出导航度量（Navigational Metric）量化三元组跨章节连通性。

## 效果
- Dataset: eCFR | Metric: Section Overlap (θ=0.75) | Result: 0.2888 (With Triplets) | Baseline: 0.1684 (Without Triplets) | Δ: [+71.5%]
- Dataset: eCFR | Metric: Average Degree (Navigation) | Result: 1.6080 | Baseline: 1.2939 | Δ: [+24.3%]
- Dataset: eCFR | Metric: Avg. Shortest Path | Result: 1.3300 | Baseline: 2.0167 | Δ: [−34.0% faster]
- Dataset: eCFR | Metric: Answer Accuracy (1-5 scale) | Result: 4.73 | Baseline: 4.71 | Δ: [+0.4%]
- **Ablation**: 低相似度阈值下（θ=0.50）Without Triplets 反而更高，说明纯文本检索召回宽泛但精度低；严格阈值 θ=0.75 下 With Triplets 大幅领先，证明三元组在高精度检索场景优势显著
- **Ablation**: 答案准确性提升微小（4.71→4.73），主要价值在于检索精度和导航连通性

## 关键引用
> "an alternative 'schema-light' approach defers rigid schemas in favor of flexible bottom-up extraction. This method quickly adapts to new data domains, reduces initial overhead, and allows partial schemas to emerge naturally, making it especially valuable in regulatory settings where rules evolve rapidly." — Section 3, p.2

> "By examining both structured (triplet) facts and verbatim textual evidence, the LLM generates a more accurate and explainable response." — Section 4.5, p.4

> "Triplets yield highest accuracy at higher threshold. Triplets network significantly enhances connectivity and navigation." — Table 1 caption, p.8

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[AuditableStructuredRetrieval]] — 可审计结构化检索
- [[og-rag-ontology-grounded]] — Round 15 本体超图最小超边集检索
- [[moss-auditable-agentic-memory]] — Round 15 结构化关系DB替代嵌入搜索
- [[RAG]] — 检索增强生成概念
