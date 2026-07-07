---
title: "TITAN: 网络威胁情报的图可执行推理"
type: source
tags: [ontology-qa, graph-reasoning, threat-intelligence, ontology-reasoning]
sources: [titan-graph-reasoning-cti]
source_file: raw/papers/titan-graph-reasoning-cti.pdf
last_updated: 2026-07-07
arxiv_id: "2510.14670"
authors: ["Marco Simoni", "Aleksandar Fontana", "Andrea Saracino", "Paolo Mori"]
year: 2025
venue: ""
citation_count: 0
doi: ""
---

## 概要
TITAN（Threat Intelligence Through Automated Navigation）是一个将自然语言网络威胁查询与结构化知识图谱上的可执行推理连接起来的框架。它集成了路径规划模型（从文本预测逻辑关系链）和图执行器（遍历 TITAN 本体检索事实答案和支撑证据）。基于 MITRE 构建类型化双向图，引入 88209 样本数据集。

## 关键贡献
- 路径规划模型：从自然语言查询预测逻辑关系链
- 图执行器：在 TITAN 本体上确定性地遍历推理路径，检索答案和证据
- 基于 MITRE 的类型化双向图：威胁、行为、防御之间可逆推理
- 88209 样本数据集，配对自然语言问题、可执行推理路径和 Chain-of-Thought 解释

## 关键引用
> "It integrates a path planner model, which predicts logical relation chains from text, and a graph executor that traverses the TITAN Ontology to retrieve factual answers and supporting evidence." — 双组件架构

## 五维分析

### 本体建模
构建**TITAN 本体**，基于 MITRE ATT&CK 框架。本体定义了网络威胁领域的关键实体类型（威胁技术、行为、防御措施、攻击组织等）及其关系。关键特征是**类型化双向图**：关系是双向的，允许在威胁→行为→防御之间可逆推理，不同于传统单向检索。

### 用户输入实体抽取
从自然语言威胁查询中，**路径规划模型**预测逻辑关系链。这包括识别查询中的关键实体（威胁名称、技术ID等）和它们之间的预期关系序列。路径规划模型本质上是将自然语言映射到本体关系序列的实体抽取器。

### 实体链接
通过**图执行器**（graph executor）实现实体链接：路径规划模型预测的关系链在本体图上执行遍历，将抽象关系链落地到具体实体节点。执行器确定性地遍历图，确保推理路径在图上可执行，不产生幻觉。

### 本体推理
核心推理是**路径规划+图执行的双阶段推理**：路径规划模型（神经网络）负责从文本预测"应该沿哪些关系走"，图执行器（符号引擎）负责在本体图上确定性地执行这条路径。这种神经-符号分离确保了推理的可执行性和确定性，同时保留了自然语言理解的灵活性。

### 任务完成
任务目标是网络威胁情报问答。TITAN 使模型能够生成语法有效、语义连贯的推理路径，可在底层图上确定性地执行。与传统检索系统不同，TITAN 的推理是可验证的——每一步都有图上的对应操作。

## 关联
- [[TITANOntology]] — TITAN本体（MITRE衍生）
- [[PathPlannerGraphExecutor]] — 路径规划+图执行架构
- [[NeuroSymbolicOrchestration]] — 神经符号编排（已有wiki）
- [[VADAOrchestra]] — LLM编排+符号引擎（已有wiki）
- [[OPI]] — 本体引导路径推理

## 矛盾
- 无
