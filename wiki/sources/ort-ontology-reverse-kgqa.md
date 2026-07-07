---
title: "ORT: 本体引导逆向思维增强KGQA"
type: source
tags: [ontology-qa, kgqa, ontology-reasoning]
sources: [ort-ontology-reverse-kgqa]
source_file: raw/papers/ort-ontology-reverse-kgqa.pdf
last_updated: 2026-07-07
arxiv_id: "2502.11491"
authors: ["Runxuan Liu", "Bei Luo", "Jiaqi Li", "Baoxin Wang", "Ming Liu", "Dayong Wu", "Shijin Wang", "Bing Qin"]
year: 2025
venue: ""
citation_count: 0
doi: ""
---

## 概要
ORT（Ontology-guided Reverse Thinking）受人类逆向思维启发，提出从目的（purpose）反向构建推理路径到条件（condition）的 KGQA 框架。通过 LLM 提取目的标签和条件标签，基于 KG 本体构建标签推理路径，再用路径引导知识检索。在 WebQSP 和 CWQ 上达到 SOTA。

## 关键贡献
- 提出逆向思维范式：从问题目的反向构建推理路径，而非传统的从实体正向扩展
- 利用 KG 本体构建标签推理路径，弥合抽象目的与具体实体之间的鸿沟
- 用标签推理路径引导知识检索，减少信息损失和冗余

## 关键引用
> "inspired by human reverse thinking, we propose Ontology-Guided Reverse Thinking (ORT), a novel framework that constructs reasoning paths from purposes back to conditions." — 核心创新点

## 五维分析

### 本体建模
利用**已有 KG 本体**（ontology）作为标签推理路径的骨架。本体定义了实体类型和关系的层次结构，ORT 在此基础上构建从目的标签到条件标签的推理路径。本体本身不是本文新建的，而是作为推理路径构建的结构化先验知识使用。

### 用户输入实体抽取
从自然语言问题中提取**目的标签**（purpose labels）和**条件标签**（condition labels）。目的标签捕获问题的意图（如"查找"、"比较"），条件标签捕获问题的约束（如特定属性值）。这一过程由 LLM 完成，是逆向推理的起点。

### 实体链接
通过**标签推理路径**间接实现实体链接：先在本体层面建立目的→条件的路径，再用路径引导从 KG 中检索具体实体。这避免了传统方法中直接用问题意图匹配具体实体时"目的抽象、实体具体"的鸿沟问题。

### 本体推理
核心推理是**逆向路径推理**：基于 KG 本体，从目的标签出发，沿着本体定义的类型和关系层次，反向构建到条件标签的推理路径。这解决了传统正向扩展中"目的难以匹配具体实体"的根本问题——先在本体抽象层面建立路径，再落地到具体实体。

### 任务完成
任务目标是多跳 KGQA。ORT 在 WebQSP 和 CWQ 上达到 SOTA，显著增强了 LLM 在需要多跳推理的 KGQA 任务上的能力。逆向路径减少了信息损失和冗余。

## 关联
- [[OntologyGuidedKGQA]] — 本体引导的KGQA核心范式
- [[ReverseThinkingReasoning]] — 逆向思维推理方法
- [[OPI]] — 同为本体引导KGQA，采用双向检索
- [[ORACLE]] — 同为本体驱动多跳推理

## 矛盾
- 无
