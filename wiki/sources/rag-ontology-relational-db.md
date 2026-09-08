---
title: "RIGOR: 关系数据库到本体的检索增强迭代生成（RAG of Ontologies from Relational Databases）"
type: source
tags: [ontology-precise-retrieval]
sources: [rag-ontology-relational-db]
source_file: raw/papers/rag-ontology-relational-db.pdf
last_updated: 2026-09-08
arxiv_id: "2506.01232"
authors: ["Nadeen Fathallah", "Mojtaba Nayyeri", "Athish A Yogi", "Ratan Bahadur Thapa", "Hans-Michael Tautenhahn"]
year: 2025
venue: "ISWC 2026"
citation_count: 0
---

## 概要
RIGOR（Retrieval-augmented Iterative Generation of RDB Ontologies）是一个 LLM-driven 迭代 RAG pipeline，将 relational database schemas 转换为 semantically rich OWL2DL ontologies，几乎无需人工干预。对每张表，RIGOR 先生成 deterministic direct mapping 保证 schema coverage，再通过三个检索源（relational schema/documentation、external domain ontologies、增量增长的 core ontology）enrichment。Gen-LLM 产出 provenance-annotated delta ontology fragments，由独立 Judge-LLM 验证并修正后整合。在三个数据库上的实验表明，RIGOR 在所有标准质量指标上一致优于 baseline methods。

## 解决的问题
从 relational database schema 自动构建 semantically rich OWL ontology 是 labor-intensive 的。现有自动化方法仅依赖 structural cues（表名、列名、datatypes、foreign-key constraints），产出缺乏 expressive axioms 的 shallow ontology。W3C Direct Mapping 和 R2RML 只做机械翻译；BootOX 需预存目标 ontology；RODI benchmark 显示 Karma、IncMap、MIRROR、D2RQ 均无法处理 implicit hierarchies。现有 LLM-based 方法针对 unstructured text，不处理 relational schema 特有挑战，BURR benchmark 显示 LLM 方法在 mapping precision/recall 上 underperform rule-based systems。

## 方法与技术
1. **FK-Guided Iterative Traversal**：按 foreign-key dependency graph 广度优先遍历（FK-BFS），root tables 优先处理；子表在所有引用的父表处理完毕后入队，确保每步可引用已建立的 classes。
2. **Direct Mapping + Delta Ontology**：每张表先用 clean() 预处理，再用 W3C Direct Mapping 生成确定性 OWL fragment 保证 100% schema coverage；Gen-LLM 在此基础上 enrichment，产出 delta ontology。
3. **三源 Dense Retrieval**：用 all-MiniLM-L6-v2 嵌入 + Faiss 索引，从 core ontology、textual documentation、external ontology repository 各检索 top-k=3 相关元素。
4. **Judge-LLM 双阶段验证**：Judge-LLM 按 14 criteria / 3 severity levels 评估 delta ontology，返回 Approved/Approved_With_Corrections/Rejected；deterministic graph validation 检查 type consistency、domain/range cardinality。失败后 retry budget k=2。
5. **Incremental Core Ontology Merging**：Gen-LLM 复用 core ontology 的 IRIs，merging 退化为 axiom-set union；每轮 validated delta ontology 并入 𝒪_t 供后续表检索。

## 创新点
- **Iterative RAG + Growing Core Ontology**（vs Non-Iterative single-pass retrieval 错误不可纠正）——每轮将 validated fragment 并入 core ontology 供后续表检索，实现 cross-table context accumulation。
- **Judge-LLM in-loop validation**（vs prior work 将 LLM-as-judge 仅作 post-hoc evaluator）——将 Judge-LLM 嵌入生成循环中，14 criteria, 3 severity levels, bounded retry。
- **Provenance-annotated Delta Ontology**——每个 ontology element 附带 prov:wasDerivedFrom assertion 引用源表/列，使 RIGOR ontology 可导出为 D2RQ mapping。
- **Gen-LLM 六操作语义增强**——Annotation、Hierarchy、Value documentation、Disjointness、Existential restrictions、External alignment——RIGOR 是唯一一致产生 disjointWith axioms 的方法。

## 效果
- Dataset: Liver Cancer | Metric: Avg. Score (LLM-Judge) | Result: 3.93 | Baseline: 2.05 (Direct Mapping) | Δ: [+91.7%]
- Dataset: eICU-CRD | Metric: Avg. Score | Result: 3.64 | Baseline: 0.67 (Non-Iterative) | Δ: [+443%]
- Dataset: eICU-CRD | Metric: Ranked 1st | Result: 31/31 (RIGOR) | Baseline: 0/31 (Non-Iterative)
- Dataset: eICU-CRD | Metric: OOPS! Pitfalls | Result: single digits (Claude/Mistral) | Baseline: 665 (Direct Mapping) | Δ: [~−99%]
- Dataset: ISWC/BURR | Metric: Class F1 | Result: 0.73 | Baseline: rule-based systems underperform
- Human experts: Ranked 1st 28/40 (70%)
- **Ablation**: Full RIGOR (all 3 retrieval sources) achieves highest external-ontology recall & F1

## 关键引用
> "RIGOR consistently produces one to two orders of magnitude fewer pitfalls than all other methods, with all three RIGOR variants achieving zero pitfalls on Chinook." — Section 4.7, Strategy 3

> "RIGOR is the only method that consistently produces annotation assertions, provenance triples, and SubClassOf axioms." — Section 4.7, Strategy 4

> "Laskowski et al. concluded that current LLM-based methods underperform rule-based systems on mapping recovery; RIGOR reverses this finding." — Section 4.7, Strategy 8

## 关联
- [[OntologyGuidedQueryGeneration]] — 本体引导查询构造
- [[auto-ontology-construction-llm]] — Round 13 LLM 外部本体记忆层
- [[ontoextend-ontology-extension]] — Round 16 需求驱动本体扩展
- [[automated-ontology-generation-multi-agent]] — Round 15 多 agent LLM 本体生成
- [[OntologyReasoning]] — Round 13 本体推理
