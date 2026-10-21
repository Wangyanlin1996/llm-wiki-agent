---
title: "NeurOWL: LLM神经符号框架解决不完整OWL本体推理"
type: source
tags: [ontology-reasoning]
sources: [neurowl]
source_file: raw/papers/neurowl.pdf
last_updated: 2026-07-25
arxiv_id: "2607.15776"
authors: ["Hui Yang", "Jiaoyan Chen", "Yiping Song", "Renate Schmidt", "Wen Zhang"]
year: 2026
venue: ""
citation_count: 0
---

## 概要
NeurOWL 是一个端到端神经符号框架，解决不完整 OWL 本体中的蕴含推理问题。给定一个不完整本体和一个候选（未被蕴含的）包含关系，NeurOWL 判断该包含关系是否语义上合理，并在合理时提供包含潜在缺失公理的逻辑解释。该任务统一了包含验证与本体溯因（ontology abduction），并通过移除预定义候选集的需求推广了后者。

## 关键贡献
- 提出 subsumption reasoning 问题，统一验证与溯因，无需预定义缺失公理候选集
- 利用 LLM 的文本语义和本体嵌入的形式语义进行联合推理
- 在多个领域的真实本体上展示了强鲁棒性

## 关键引用
> "This task unifies subsumption verification with ontology abduction, and generalizes the latter by removing the need for a predefined candidate set of missing axioms."

## 关联
- [[OntologyReasoning]] — 本体推理核心方法
- [[NeuroSymbolicOntology]] — 神符号本体注入框架
- [[inconsistency-kg-reasoning-survey]] — 不一致KG推理综述
- [[llm-kg-research-trends]] — LLM与KG交互研究趋势

## 矛盾
- 无
