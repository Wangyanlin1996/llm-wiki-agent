---
title: "OntoLearner: 首个统一本体学习框架与LLM基准"
type: source
tags: [ontology-reasoning, llm-enhancement]
sources: [ontolearner]
source_file: raw/papers/ontolearner.pdf
last_updated: 2026-07-25
arxiv_id: "2607.01977"
authors: ["Hamed Babaei Giglou", "Jennifer D'Souza", "Andrei Aioanei", "Nandana Mihindukulasooriya", "Sören Auer"]
year: 2026
venue: "Under review @ Nature Communications"
citation_count: 0
---

## 概要
OntoLearner 是首个统一的、跨域的 Python 框架，集成本体访问、LLM 驱动的学习管线和标准化基准测试。发布了 180 个机器可读本体（覆盖 22 个域），并提供管线就绪的数据集（含 train/dev/test 划分），支持三个核心本体学习任务：术语类型标注、分类发现和非分类关系抽取。大规模实证研究评估了 22 个检索模型和 12 个 LLM，发现失败模式随本体复杂度而非模型规模扩展。

## 关键贡献
- 首个统一本体学习框架，集成本体访问+LLM管线+标准化基准
- 180 个机器可读本体 × 22 域，首个大规模本体学习基础设施
- 22 检索模型 + 12 LLM 跨域评测
- 核心发现：主要瓶颈不是模型能力而是模型编码知识与本体组织方式之间的结构不匹配

## 关键引用
> "The primary bottleneck is not model capability, but a structural mismatch between how models encode knowledge and how ontologies organize it."

## 关联
- [[OntologyReasoning]] — 本体推理核心方法
- [[OntologyConstruction]] — 本体构建与演化
- [[llm-kg-research-trends]] — LLM与KG交互研究趋势
- [[neurowl]] — LLM增强不完整OWL推理

## 矛盾
- 无
