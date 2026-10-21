---
title: "NEURON: SNOMED CT本体增强的临床可解释性神经符号系统"
type: source
tags: [llm-agent-ontology, neuro-symbolic]
sources: [neuron-clinical-explainability]
source_file: raw/papers/neuron-clinical-explainability.pdf
last_updated: 2026-07-25
arxiv_id: "2605.01189"
authors: ["Anuradha Chandrasekaran", "Dimitrios Zikos", "Mutlu Mete", "Alan Pang", "Brady D. Lund", "Kewei Sha"]
year: 2026
venue: ""
citation_count: 0
---

## 概要
临床 AI 采用受高性能模型黑箱/灰箱特性阻碍，缺乏本体接地和叙事透明性。NEURON 是神经符号系统，集成 SNOMED CT 本体信息结构表示与机器学习模型，弥合原始数据与医学术语之间的鸿沟。系统利用 RAG 接地 LLM 层综合 SHAP 特征归因和患者特定临床笔记，生成连贯的自然语言解释。在 MIMIC-IV 数据集上验证急性心力衰竭死亡率预测，AUC 从 0.74-0.77 提升到 0.84-0.88。

## 关键贡献
- SNOMED CT 本体 + ML + RAG 接地 LLM 三层集成
- SHAP 特征归因 + 患者临床笔记 → 连贯自然语言解释
- AUC 从 0.74-0.77 提升到 0.84-0.88
- 人类对齐度量显著超越原始 SHAP 可视化（0.85 vs 0.50）

## 关键引用
> "NEURON integrates SNOMED CT ontology-informed structural representations with machine learning models to bridge the gap between raw data and medical nomenclature."

## 关联
- [[NeuroSymbolicOntology]] — 神符号本体注入框架
- [[OntologyFirstAgentDesign]] — 本体优先Agent设计方法论
- [[qime-ontology-embeddings]] — 本体驱动可解释医学嵌入
- [[virf-verifiable-embodied]] — 安全本体驱动的神经符号架构

## 矛盾
- 无
