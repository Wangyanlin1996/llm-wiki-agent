---
title: "VirtualSet: 类型化本体世界作为LLM生成目标 (Typed Ontology Worlds)"
type: source
tags: [ontology-matching-alignment]
sources: [virtualset-typed-ontology-worlds]
source_file: raw/papers/virtualset-typed-ontology-worlds.pdf
last_updated: 2026-08-03
arxiv_id: "2607.18821"
authors: ["Qunhui Zhang"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

本文提出 VirtualSet，一个实时、接收者类型的本体世界接口和 LLM 生成目标。模型不输出 SQL，而是输出基于实体-边世界的集合表达式。通用约束投影（GCP）在执行前检查表达式，future this 通过集合链保留具体接收者类型，将无效字段、边、接收者和动作转为 token 锚定类型错误。支持守护决策：动作先在模拟世界运行，世界变化事件需外部批准才能实际化。

## 解决的问题

LLM 读写企业数据时，SQL 给出延迟错误信号——幻觉字段或关系可能执行并返回看似合理的错误答案，而不正确写入在执行后无法安全评估。需要一种在执行前就能捕获类型错误的语义接口。

## 方法与技术

1. **类型化本体世界接口**：替代 SQL，模型输出基于实体-边世界的集合表达式
2. **通用约束投影（GCP）**：执行前检查表达式，捕获无效字段/边/接收者/动作
3. **接收者类型保留**：future this 通过集合链保留具体接收者类型
4. **双路径执行**：类型清洁读取用 SQL 快速路径或有界流解释，奇偶校验检查
5. **守护决策**：动作先在模拟世界运行，世界变化事件需外部批准

## 创新点

- 用类型化本体世界替代 SQL 作为 LLM 生成目标，将错误信号从执行后提前到执行前
- GCP 通用约束投影在执行前捕获类型错误
- 守护决策机制：模拟世界预执行 + 外部批准实际化
- 接收者类型通过集合链保留，而非丢失

## 效果

- BIRD 基准（1072 问题）：**67.5%** 准确率 vs 直接 SQL 63.5%（+4.0pp，McNemar p=0.00117）
- 类型清洁表达式无引擎误计算
- 30 个体守护语料中拦截 **20/20** 幻觉动作体，零误报

## 关键引用

> "SQL gives a late error signal: hallucinated fields or relations can execute and return plausible wrong answers" — 指出 SQL 延迟错误信号问题

## 关联

- [[OntologySemanticLayer]] — 类型化本体世界作为语义接口层
- [[OntologyReasoning]] — GCP 约束投影属于本体推理
- [[OntologyFirstAgentDesign]] — 本体从知识源提升为生成目标
- [[SemanticTrainingGap]] — 同为类型约束消除幻觉，但本方法在查询层
