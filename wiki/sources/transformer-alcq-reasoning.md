---
title: "Transformer-based Language Models for Reasoning in the Description Logic ALCQ（DELTAD：表达性DL推理基准）"
type: source
tags: [ontology-reasoning, llm-reasoner-hybrid, benchmark]
sources: [transformer-alcq-reasoning]
source_file: raw/papers/transformer-alcq-reasoning.pdf
last_updated: 2026-10-09
arxiv_id: "2410.09613"
authors: ["Angelos Poulis", "Eleni Tsalapati", "Manolis Koubarakis"]
year: 2024
venue: "arXiv (Boston U / ATC / NKUA)"
citation_count: 1
---

## 概要

DELTAD（Description Logics with TrAnsformers）是**基于表达性描述逻辑 ALCQ** 的 384K 样例自然语言数据集，用于系统评估 transformer 语言模型的逻辑推理能力。数据集沿两个维度扩展：推理深度（reasoning depth）与语言复杂度（linguistic complexity）。实验显示：监督微调的 DeBERTa 模型可在 DELTAD 上**掌握蕴含检查任务**；GPT-3.5/GPT-4 在少量样本（9 shots）few-shot 提示下性能也显著提升。与大多数基于短 FOL 片段（少量逻辑算子/量词）的基准相比，ALCQ 同时支持存在、全称与数量约束及布尔算子。

## 解决的问题

transformer 语言模型的逻辑推理评测长期依赖简单基准——从短 FOL 句子片段生成、只含少数逻辑算子与量词，无法评估表达性推理。需要回答三个问题：(1) TLM 能否在表达性 DL（ALCQ）上下文上做推理？(2) 性能是否受所需推理深度影响？(3) 形式语言的片段是否足以评测推理能力（语言复杂度是否影响）？——特别是 ALCQ 中 linguistically complex 的句子对模型的挑战。

## 方法与技术

1. **ALCQ 形式化**：用支持存在（∃）、全称（∀）、数量（≥n/≤n）约束及标准布尔算子的 ALCQ 生成概念知识、事实与推理问题。
2. **DELTAD 数据集**：384K 样例（context-question-answer-depth-linguistic_complexity），沿推理深度（reasoning depth）与语言复杂度（linguistic complexity）两个受控维度扩展——系统性而非零散样例。
3. **三类推理回答**：True/False/Unknown 三分蕴含检查任务。
4. **评测协议**：监督微调 DeBERTa-based 模型 vs GPT-3.5/GPT-4 few-shot prompting（9 shots）。
5. **受控消融维度**：按推理深度与语言复杂度分层报告性能，定位模型在哪个维度退化。

## 创新点

- 首个用**表达性 ALCQ**（数量约束 + 布尔 + 量词）构建的规模化（384K）自然语言 DL 推理基准，超越常见 FOL 小片段基准。
- 双维度受控扩展（推理深度 × 语言复杂度）首次在 DL 语境下系统分离"逻辑难度"与"语言难度"。
- 证明小模型（DeBERTa 微调）可在表达性 DL 蕴含检查上达标，同时展示 few-shot GPT 的显著可提升性。

## 效果

- **数据集规模**：384K 样例（ALCQ 表达力，含存在/全称/数量约束与布尔算子）。
- **DeBERTa 微调**：在 DELTAD 上掌握蕴含检查任务（entailment checking）。
- **GPT few-shot**：9 shots 提示下 GPT-3.5/GPT-4 性能显著提升。
- **维度分析**：性能随推理深度与语言复杂度变化，语言复杂度高的上下文更具挑战性。

## 关键引用

> "We construct the natural language dataset, DELTAD, using the expressive description logic language ALCQ. DELTAD comprises 384K examples and increases in two dimensions: i) reasoning depth, and ii) linguistic complexity." — Abstract

> "We show that the DeBERTa-based model fine-tuned on our dataset can master the entailment checking task. Moreover, the performance of GPTs can improve significantly even when a small number of samples is provided (9 shots)." — Abstract

## 关联

- [[OntologyReasoning]] — 评测 transformer 在表达性 DL 上的推理，是本概念页"LLM 推理能力评测"的神经侧实证。
- [[ontology-grounded-reasoner-benchmarks]] — 互补：DELTAD 关注模型推理能力本体无关评测，后者关注本体接地+推理器验证的评测。
- [[NeuroSymbolicOntology]] — 揭示 LLM 对 DL 符号语义的掌握程度，支撑神符号注入的必要性论证。
- [[llm-active-learning-owl]] — 均涉及 LLM 与 DL 语义的交互；DELTAD 测"能否推理"，该文用"推理查询辅助建模"。
