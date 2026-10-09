---
title: "An Embedding-based Approach to Inconsistency-tolerant Reasoning with Inconsistent Ontologies（基于嵌入的不一致容忍推理）"
type: source
tags: [ontology-reasoning, robustness, neuro-symbolic]
sources: [embedding-inconsistency-tolerant]
source_file: raw/papers/embedding-inconsistency-tolerant.pdf
last_updated: 2026-10-09
arxiv_id: "2304.01664"
authors: ["Keyu Wang", "Site Li", "Jiaye Li", "Guilin Qi", "Qiu Ji"]
year: 2023
venue: "IJCKG 2023"
citation_count: 2
---

## 概要

本文提出基于**公理嵌入**的不一致容忍推理方法：在描述逻辑本体上，用句嵌入（BERT 类）与知识图谱嵌入（TransE 类）两种方法把公理翻译为语义向量，据此计算公理间语义相似度；再定义基于嵌入的最大一致子集（MCS）选择方法，用它定义不一致容忍的推理关系。论文通过若干逻辑性质展示推理关系的合理性，并在多个本体上实验，证明嵌入方法**优于基于 MCS 的现有不一致容忍推理方法**（如怀疑式推理与基数最大一致子集推理）。

## 解决的问题

本体不一致是不一致构造/演化/融合的自然结果，用不一致本体推理会得到无意义答案。自然应对是选取最大一致子集（MCS）推理，但**已有 MCS 选择方法很少考虑公理语义**，导致推理能力弱、回答质量差。经典怀疑式（skeptical）推理与基数最大一致子集推理把公理等权对待；通用单调选择关系（如 [26]）限于命题逻辑，迁移到描述逻辑不平凡。核心问题：如何用公理语义（可靠性差异）理性地选择 MCS 用于推理。

## 方法与技术

1. **句嵌入方法（Sentence-embedding）**：将公理翻译为自然语言句子，用预训练 transformer（BERT 类）编码为语义向量，Cosine 相似度度量公理间语义。
2. **知识图谱嵌入方法（KG-embedding）**：将本体结构表示为知识图谱三元组，用 TransE 类模型学习嵌入，计算公理语义相似度。
3. **基于嵌入的 MCS 选择**：利用公理语义相似度定义可靠性排序，选择（更可靠的）最大一致子集——公理不再是等权重的符号。
4. **不一致容忍推理关系**：基于所选 MCS 定义推理关系，并考察若干逻辑性质（rationality）证明合理性。
5. **实验评测**：在多个本体（含 OpenCyc 案例）上对比怀疑式推理、基数 MCS 推理等基线。

## 创新点

- 首次将**公理语义嵌入**引入不一致本体的 MCS 选择——相对已有方法（逻辑闭包/权重/频率/信任）本质差异：公理在连续向量空间中可比语义可靠性。
- 提供两种互补编码（语言语义 vs 结构语义），覆盖公理语义的不同侧面。
- 推理关系具备可考察的逻辑性质，不只是启发式——在不一致容忍推理中少见。

## 效果

- **数据集**：多个不一致本体（含 OpenCyc 案例公理：ArtifactualFeatureType(Monument) 等四公理不一致）。
- **对比基线**：优于基于 MCS 的现有不一致容忍推理方法（怀疑式推理、基数最大一致子集推理）。
- **两种嵌入编码**：句嵌入与 KGE 嵌入均有效，结构/语言语义互补。
- 逻辑性质验证支撑推理关系合理性。

## 关键引用

> "A natural way to reason with an inconsistent ontology is to utilize the maximal consistent subsets of the ontology. However, previous studies on selecting maximal consistent subsets have rarely considered the semantics of the axioms, which may result in irrational inference." — Abstract

> "We first propose a sentence-embedding-based method and a knowledge-graph-embedding-based method for translating axioms into semantic vectors to calculate semantic similarities among axioms." — Abstract

> "The experimental results show that our embedding-based method can outperform existing inconsistency-tolerant reasoning methods based on maximal consistent subsets." — Abstract

## 关联

- [[OntologyReasoning]] — 不一致容忍推理是本概念页处理"不完整/不一致本体"推理挑战的代表路线。
- [[InconsistencyTolerantReasoning]] — MCS 选择 + 嵌入语义排序是不一致容忍推理的核心技术之一。
- [[falcon-inconsistent-alc]] — 并列为不一致处理神经路线：FALCON 多模型近似蕴含，该文语义排序 MCS。
- [[neural-shqoi-instance-retrieval]] — 均用嵌入处理不一致；Ebr 走链接预测集合语义，该文走公理向量语义。
