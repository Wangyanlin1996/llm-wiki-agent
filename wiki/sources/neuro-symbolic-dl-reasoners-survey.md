---
title: "Neuro-Symbolic RDF and Description Logic Reasoners: The State-Of-The-Art and Challenges（神经符号推理器综述）"
type: source
tags: [ontology-reasoning, neuro-symbolic, survey]
sources: [neuro-symbolic-dl-reasoners-survey]
source_file: raw/papers/neuro-symbolic-dl-reasoners-survey.pdf
last_updated: 2026-10-09
arxiv_id: "2308.04814"
authors: ["Gunjan Singh", "Sumit Bhatia", "Raghava Mutharaju"]
year: 2023
venue: "Compendium of Neuro-Symbolic Artificial Intelligence"
citation_count: 4
---

## 概要

这是神经符号**演绎推理**（deductive reasoning）在 RDF 与描述逻辑上的系统综述，覆盖 RDF(S)、EL、ALC、OWL 2 RL 等语言。它梳理了传统推理器（tableau 演算、规则推理）在大而表达性本体上扩展性差、对噪声不一致本体无能为力的困境，以及神经符号方法如何结合神经网络学习能力与符号系统推理能力应对这些挑战。综述明确界定范围：只讨论在本体上做演绎推理的技术，排除知识图谱补全（KGC）、本体学习/补全、断言预测等非演绎任务。

## 解决的问题

本体越做越大、表达性越来越强（OWL 2 DL/SROIQ），推理复杂度随之上升，传统推理器在大型表达性本体上扩展性差。同时自动化知识库构建让"大而表达性"的本体变得容易，但**常含噪声且不一致**，传统推理器无法处理。需要系统梳理：神经符号演绎推理有哪些技术？它们解决什么任务、有何局限与适用边界？——此前缺乏统一视角。

## 方法与技术

1. **传统推理器分类**：按优化类型分预处理、模型构造、推理任务相关优化三类；基于 tableau 演算与基于规则的推理方法。
2. **神经符号演绎推理技术梳理**：按支持的推理语言（RDF(S)、EL、ALC、OWL 2 RL）组织；讨论神经网络学习能力与符号推理能力的结合方式（嵌入语义、神经近似推理器等）。
3. **任务视角**：每项工作按采用的技术、处理的任务整理成概览表。
4. **互补工作**：推理器评测挑战赛（reasoner evaluation challenges）与本体基准（ontology benchmarks）。
5. **边界划定**：明确排除 KGC、本体学习/补全、近似类定义、断言预测——只保留下述领域的演绎推理。

## 创新点

- 首个（至 2023 年）系统梳理**神经符号演绎推理**（非 KGC/补全）在 RDF/DL 上的综述，明确划定任务边界。
- 按推理语言粒度（RDF(S)/EL/ALC/OWL 2 RL）组织技术，给出"表达力 vs 神经符号支持度"的对照全景。
- 指出该领域支撑语言的空白（SROIQ 等表达性 DL 的神经符号推理工作稀缺），并为后续工作（如 Ebr、Baobab、FALCON）提供定位坐标系。

## 效果

- 覆盖语言：RDF(S)、EL、ALC、OWL 2 RL（神经符号演绎推理已支持的语言谱系）。
- 任务梳理：按技术类型与任务形成系统表格，识别表达性 DL（SROIQ）神经符号支持的空白。
- 框架性结论：传统推理器在大/表达性/不一致本体上的双重失效（扩展性 + 不一致）是神经符号方法的主要动机。
- 与推理器评测（OWL2Bench 等）与本体基准结合，构成推理器生态全图。

## 关键引用

> "However, as ontologies grow larger and more expressive, reasoning complexity increases, and traditional reasoners struggle to perform efficiently. ... such ontologies are often noisy and inconsistent, and the conventional ontology reasoners cannot deal with such ontologies." — Abstract / Section 1

> "We exclude works that use machine learning techniques for knowledge graph completion (KGC)... Specifically, we discuss only those works that focus on deductive reasoning over ontologies." — Section 1

> "the body of work in the neuro-symbolic reasoning category is limited. Hence, we only briefly discuss the ontology languages that are supported by neuro-symbolic reasoning techniques such as RDF(S), EL, ALC, and OWL 2 RL." — Section 1

## 关联

- [[OntologyReasoning]] — 神经符号推理器的奠基综述，为本概念页的"神经符号替代符号推理"路线提供全景坐标。
- [[neural-shqoi-instance-retrieval]] — Ebr 属于综述谱系的"嵌入近似推理"族，并扩展到综述标注的空白（表达性 DL）。
- [[falcon-inconsistent-alc]] — FALCON 属于"神经近似模型生成"族，回应综述指出的不一致处理缺口。
- [[owl2dl-differentiable-circuits]] — Baobab 属于"知识编译"族，把综述中 SROIQ 支持空白推向非 Horn 全特征。
