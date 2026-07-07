---
title: "动态本体构建 (Dynamic Ontology Construction)"
type: concept
tags: [ontology-modeling, ontology-qa]
sources: [oracle-ontology-multihop, lom-large-ontology-model, teqodo-tod-ontology, dialogue-ontology-relation-extraction]
last_updated: 2026-07-07
---

动态本体构建（Dynamic Ontology Construction）是指根据具体任务或查询，利用 LLM 自动从数据中推断和构建本体结构——包括实体类型、关系定义和约束规则——而非依赖预定义的静态本体。这一范式解决了传统本体工程的两大瓶颈：(1) 人工本体构建成本高、耗时长；(2) 静态本体难以适应新域和新任务。关键方法包括：根据问题实时构建问题特定本体（[[oracle-ontology-multihop]]）、从结构化数据库和非结构化文本构建双层企业本体（[[lom-large-ontology-model]]）、LLM 用 SQL 能力从零构建 TOD 本体（[[teqodo-tod-ontology]]）、以及约束 CoT 解码的对话本体关系抽取（[[dialogue-ontology-relation-extraction]]）。动态本体构建代表了从"本体作为静态先验"到"本体作为可推导的结构化知识"的范式转变。

## 关联论文
- [[oracle-ontology-multihop]] — 问题特定动态本体
- [[lom-large-ontology-model]] — 双层企业本体融合
- [[teqodo-tod-ontology]] — LLM自主TOD本体构建
- [[dialogue-ontology-relation-extraction]] — CoT解码关系抽取

## 关联概念
- [[OntologyGuidedKGQA]]
- [[OntologyAwareTOD]]
- [[LLMKGOntologySynergy]]
