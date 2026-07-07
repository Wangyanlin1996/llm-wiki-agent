---
title: "LLM-KG本体协同 (LLM-KG Ontology Synergy)"
type: concept
tags: [ontology-survey, llm-kg, ontology-generation, ontology-reasoning]
sources: [llm-kg-research-trends, lom-large-ontology-model, kg-policy-compliance, inconsistency-kg-reasoning-survey, neuro-symbolic-kg-ontology]
last_updated: 2026-07-07
---

LLM-KG本体协同（LLM-KG Ontology Synergy）是指 LLM 与知识图谱/本体之间的双向增强关系：LLM 可以从文本自动生成本体、填充 KG、验证 KG 一致性；KG/本体则为 LLM 提供结构化知识基础，增强推理的事实一致性和可验证性。这一协同关系覆盖 KG 问答、本体生成、KG 验证和 KG 增强四个核心方向。[[llm-kg-research-trends]] 系统综述了这一协同关系；[[lom-large-ontology-model]] 通过三阶段训练将本体结构与语言模型深度融合；[[kg-policy-compliance]] 发现 LLM 自发现的 schema 可匹配形式化本体；[[inconsistency-kg-reasoning-survey]] 分析了自动提取导致的不一致及容忍推理；[[neuro-symbolic-kg-ontology]] 提出本体引导的后提取纠错。核心洞察是：**LLM 提供自然语言理解灵活性和非结构化知识覆盖，KG/本体提供结构化约束和可验证推理——两者的协同优于任一单独使用**。

## 关联论文
- [[llm-kg-research-trends]] — LLM-KG协同综述
- [[lom-large-ontology-model]] — 大本体模型融合
- [[kg-policy-compliance]] — LLM自发现schema
- [[inconsistency-kg-reasoning-survey]] — 不一致KG推理综述
- [[neuro-symbolic-kg-ontology]] — 本体引导KG纠错

## 关联概念
- [[DynamicOntologyConstruction]]
- [[OntologyGuidedKGQA]]
- [[NeuroSymbolicKGModule]]
- [[NeuroSymbolicOntology]] (已有wiki)
