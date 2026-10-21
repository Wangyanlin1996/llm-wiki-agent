---
title: "DaoQL: 数据优先本体作为LLM的显式世界模型"
type: source
tags: [semantic-layer, llm-agent-ontology]
sources: [daoql-explicit-world-model]
source_file: raw/papers/daoql-explicit-world-model.pdf
last_updated: 2026-07-25
arxiv_id: "2607.17269"
authors: ["Zhanbo Li", "Shifeng Wu", "Xiangjin Meng", "Wenjie Cai"]
year: 2026
venue: ""
citation_count: 0
---

## 概要
LLM 在神经权重中隐式编码世界模型，在高精度领域（医疗、金融）暴露四个结构性风险：幻觉、冻结知识、可解释性差、可修改性差。本文提出数据优先本体：LLM 作为推理和语言引擎，确定性知识移入显式多模态数据库 DaoQL。形式化显式世界模型，在规则独立性、确定性评估和固定冲突解决下，显式模型提供可组合反事实可分解性的充分条件；隐式模型缺乏原子读/delta 语义，因此无可比架构保证。

## 关键贡献
- 数据优先本体：LLM 推理引擎 + 显式多模态数据库 DaoQL
- 形式化显式世界模型的可组合反事实可分解性充分条件
- 集成图、列、向量、全文引擎于单进程
- 五领域反事实实验（n=1250）：DaoQL+GPT-4o 达 94% 可组合反事实可分解性，比 GPT-4o 单独高 49 个百分点
- 明确分离可证明结构、初步实证证据和架构路线图主张

## 关键引用
> "Under rule independence, deterministic evaluation, and fixed conflict resolution, explicit models provide a sufficient condition for composable counterfactual decomposability; implicit models lack atomic read/delta semantics and therefore provide no comparable architectural guarantee."

## 关联
- [[OntologySemanticLayer]] — 本体语义层
- [[OntologyFirstAgentDesign]] — 本体优先Agent设计方法论
- [[semantic-training-gap]] — 本体嵌入工具层消除语义鸿沟
- [[auto-ontology-construction-llm]] — LLM+外部本体记忆层
- [[umodel-observability]] — 统一本体框架

## 矛盾
- 无
