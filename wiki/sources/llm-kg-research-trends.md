---
title: "LLM与知识图谱交互研究趋势: 综述"
type: source
tags: [ontology-survey, llm-kg, ontology-generation, kg-validation, ontology-reasoning]
sources: [llm-kg-research-trends]
source_file: raw/papers/llm-kg-research-trends.pdf
last_updated: 2026-07-07
arxiv_id: "2406.08223"
authors: ["Hanieh Khorashadizadeh", "Fatima Zahra Amara", "Morteza Ezzabady", "Frédéric Ieng", "Sanju Tiwari", "Nandana Mihindukulasooriya", "Jinghua Groppe", "Soror Sahri", "Farah Benamara", "Sven Groppe"]
year: 2024
venue: ""
citation_count: 0
doi: ""
---

## 概要
综述研究 LLM 与知识图谱的协同关系，对推进 AI 在理解、推理和语言处理方面的能力至关重要。覆盖 KG 问答、本体生成、KG 验证、以及通过 LLM 增强 KG 准确性和一致性。检查 LLM 在生成描述性文本和自然语言查询中的角色。通过结构化分析（LLM-KG 交互分类、方法论、协同使用和潜在偏见）提供新洞察。

## 关键贡献
- 系统综述 LLM-KG 协同关系
- 覆盖 KG QA、本体生成、KG 验证、KG 增强
- LLM-KG 交互分类法
- 讨论 LLM 在生成描述性文本和 NL 查询中的角色

## 关键引用
> "This survey investigates the synergistic relationship between Large Language Models (LLMs) and Knowledge Graphs (KGs), which is crucial for advancing AI's capabilities in understanding, reasoning, and language processing." — 核心主题

## 五维分析

### 本体建模
综述覆盖**LLM 驱动的本体生成**：LLM 可从文本自动生成本体结构（概念层次、关系定义）。也讨论了**KG 验证**——LLM 帮助验证 KG 是否符合本体约束。LLM 与本体的交互是双向的：LLM 可生成本体，本体也可增强 LLM 的推理能力。

### 用户输入实体抽取
综述讨论了 LLM 在**从自然语言提取实体和关系填充 KG** 中的角色。LLM 的理解能力使其能从非结构化文本中提取结构化三元组，但提取质量需要 KG 验证机制保障。

### 实体链接
综述覆盖了 **KG QA 中的实体链接**：LLM 将自然语言查询中的实体链接到 KG 中的实体。综述分析了不同方法的优缺点，以及 LLM 如何改善传统实体链接的准确性和覆盖范围。

### 本体推理
综述讨论了 **LLM+KG 的联合推理**：LLM 提供自然语言理解和灵活推理，KG/本体提供结构化知识和可验证推理。两者结合的协同效应——LLM 帮助 KG 推理处理模糊和非结构化输入，KG 帮助 LLM 推理避免幻觉和确保事实一致性。

### 任务完成
综述不直接涉及单一任务完成，但覆盖了 LLM-KG 协同在信息检索、QA、决策等任务中的应用。这些任务是 HCI Q&A 和任务执行场景的基础。综述的分析框架帮助理解如何选择和组合 LLM-KG 交互模式以优化任务完成。

## 关联
- [[LLMKGSynergy]] — LLM-KG协同
- [[OntologyGeneration]] — 本体生成
- [[KGValidation]] — KG验证
- [[InconsistencyKGReasoningSurvey]] — 不一致KG推理综述
- [[LOM]] — 大本体模型
- [[OPI]] — 本体引导KGQA
- [[NeuroSymbolicOntology]] — 神符号本体（已有wiki）

## 矛盾
- 无
