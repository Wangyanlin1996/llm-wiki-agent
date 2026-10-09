---
title: "Neural Reasoning for Robust Instance Retrieval in SHOIQ（Ebr：嵌入鲁棒推理器）"
type: source
tags: [ontology-reasoning, llm-reasoner-hybrid, neuro-symbolic]
sources: [neural-shqoi-instance-retrieval]
source_file: raw/papers/neural-shqoi-instance-retrieval.pdf
last_updated: 2026-10-09
arxiv_id: "2510.20457"
authors: ["Louis Mozart Kamdem Teyou", "Luke Friedrichs", "N'Dah Jean Kouagou", "Caglar Demir", "Yasir Mahmood", "Stefan Heindorf", "Axel-Cyrille Ngonga Ngomo"]
year: 2025
venue: "K-CAP 2025"
citation_count: 2
---

## 概要

Ebr（Embedding-Based Reasoner）是基于知识图谱嵌入（KGE）的神经推理器，用于在**不一致与不完整**的知识库上做鲁棒的实例检索与概念学习。Ebr 不是嵌入模型，而是推理框架：利用 KGE 学习实体/关系向量表示，将 SHOIQ 描述逻辑的构造子映射为嵌入空间的集合运算（阈值化链接预测 + 集合论运算），从而近似符号推理器结果。实验显示 Ebr 仅需检索原子概念与存在限制的实例即可检索/近似任意 SHOIQ 概念实例，且在注入噪声（不一致）与缺失断言（不完整）的知识库上持续优于符号推理器。

## 解决的问题

概念学习依赖符号推理器（Pellet、FaCT++、HermiT）做实例检索，但真实知识库**很少完整或一致**：不一致时符号推理器要么停机要么（逻辑上）蕴含一切导致推理无用；不完整时无法推断缺失断言（如 Bob 的 person 成员）。DBpedia 等真实本体即含冲突断言。现有神经方法要么限于简单逻辑、要么只支持专用查询。需要一个能"在古典方法失效处"做推理的数据驱动替代。

## 方法与技术

1. **知识图谱构造**：将本体公理映射为三元组——C(a)≡(a,rdf:type,C)、r(x,y)≡(x,r,y)、C⊑D≡(C,rdfs:subClassOf,D)、r⊑s≡(r,rdfs:subPropertyOf,s)。
2. **神经链接预测器**：训练 KGE 模型 φ_Θ，用 sigmoid 将评分转概率 φ(x,r,y)=σ(φ_Θ)，设阈值 γ 判定断言真假——与符号推理的关键差异（噪声断言可被预测为假而排除）。
3. **SHOIQ 神经语义**：概念构造子映射为集合运算——原子概念 A={x|φ(x,rdf:type,A)≥γ}、⊓→交集、⊔→并集、¬→补集、∃r.C→{x|∃y...}、∀r.C→¬(∃r.¬C)、≥n s.C→计数阈值、{o}→单例；复杂 TBox 公理由组件三元组的组合重建语义。
4. **三任务评测协议**：Task1 完整一致数据上的实例检索（Jaccard）；Task2 噪声/不完整注入下的鲁棒性；Task3 概念学习（接入 OCEL/CELOE/CLIP/EvoLearner，F1）。

## 创新点

- 首次将 KGE 嵌入语义扩展到**表达性 SHOIQ 全构造子**（含基数约束、nominals、逆角色），超越传统链接预测任务范畴。
- 相对符号推理器：在噪声（不一致）知识库上可继续运作，而 Pellet/HermiT/JFact 直接失效（报告 *）；相对 FIC/Structural（DL-Learner 的不一致容忍推理器），Ebr 在多数数据集上表现更优。
- 阈值 γ 稳健：实验显示 γ 变化对 Jaccard 影响可忽略——免微调的实用优势。

## 效果

- **完整一致数据**：ComplEx d=128 起所有 SHOIQ 概念类型 Jaccard 达 **1.00**（Carcinogenesis/Mutagenesis/Semantic Bible/Family）；Carcinogenesis 合取 C⊓D 从 d=32 的 0.37 → d=64 的 0.99 → d=128 的 1.00。
- **噪声（不一致）鲁棒性**：Carcinogenesis/Mutagenesis/Vicodi 注入 1–2% 噪声（≥1000 损坏公理），符号推理器失效，Ebr 保持高 Jaccard；概念学习 Carcinogenesis 10% 不一致下所有学习器 F1=1.00（vs Pellet *）。
- **不完整鲁棒性**：各数据集不完整度 20–80% 下 Ebr 多数情况下 Jaccard 高于或持平其他推理器。
- **运行时间**：Vicodi 概念检索 Ebr 78.1s vs HermiT 300.2s；小数据集 0.01–0.1s。硬件：2×H100-80G，最大数据集仅 ~16GB 显存。
- 数据集：Carcinogenesis (22,372 inds)、Mutagenesis (14,145)、Semantic Bible (724)、Vicodi (33,238)、Family (202)、Father (6)。

## 关键引用

> "Our reasoner relies on embeddings to approximate the results of a symbolic reasoner. We show that Ebr solely requires retrieving instances for atomic concepts and existential restrictions to retrieve or approximate the set of instances of any concept in the description logic SHOIQ." — Abstract

> "In contrast to [22] and analogously to the classical seminaïve algorithm for Datalog [1], our procedure aims at minimising redundant computation..." — (嵌入语义核心，Section 3.2/3.3)

> "On the Carcinogenesis dataset, EBR achieved perfect F1-scores (1.00) across all learners, surpassing both FIC and Structural." — Section 5.4

## 关联

- [[OntologyReasoning]] — 神经推理器是本概念页"神经符号替代符号推理"路线的代表实现（针对不一致/不完整）。
- [[dl-ontologies-probabilistic-circuits]] — 互补路线：Ebr 用嵌入近似推理，电路方法用编译到可微电路近似推理。
- [[InconsistencyTolerantReasoning]] — Ebr 是"嵌入容忍不一致推理"的核心证据（Pellet 失效处 F1 1.00）。
- [[embedding-inconsistency-tolerant]] — 均用嵌入处理不一致本体；Ebr 关注实例检索鲁棒性，该文关注公理排序的 MCS 选择。
