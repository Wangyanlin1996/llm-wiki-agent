---
title: "Husky: 统一开源语言Agent用于多步推理"
type: source
tags: [task-execution, action-ontology, multi-step-reasoning, task-completion]
sources: [husky-language-agent]
source_file: raw/papers/husky-language-agent.pdf
last_updated: 2026-07-07
arxiv_id: "2406.06469"
authors: ["Joongwon Kim", "Bhargavi Paranjape", "Tushar Khot", "Hannaneh Hajishirzi"]
year: 2024
venue: ""
citation_count: 0
doi: ""
---

## 概要
Husky 是一个整体性、开源的语言 agent，学习在统一动作空间上推理以解决涉及数值、表格和知识推理的复杂任务。迭代两个阶段：生成下一步动作→用专家模型执行动作并更新当前解。识别解决复杂任务的动作本体并策展高质量数据训练专家模型。在 14 个评估数据集上超越先前语言 agent，7B 模型匹配甚至超越 GPT-4。引入 HuskyQA 压力测试混合工具推理。

## 关键贡献
- 统一动作空间+动作本体：覆盖数值、表格、知识推理
- 两阶段迭代：动作生成→专家模型执行→状态更新
- 7B 模型匹配/超越 GPT-4
- HuskyQA：混合工具推理压力测试

## 关键引用
> "We identify a thorough ontology of actions for addressing complex tasks and curate high-quality data to train expert models for executing these actions." — 动作本体+专家模型

## 五维分析

### 本体建模
**动作本体**（ontology of actions）是核心设计：定义解决复杂任务所需的完整动作类型集合（如数值计算、表格查询、知识检索、工具调用等）。每个动作类型有明确的输入/输出规格和执行专家模型。本体是任务无关的——同一组动作可组合解决不同类型的复杂任务。

### 用户输入实体抽取
从用户任务中识别需要执行的动作序列。agent 将复杂任务分解为本体中定义的动作类型组合，每个动作有明确的输入参数（从任务描述中提取）。

### 实体链接
动作执行阶段实现实体链接：动作的输入参数被传递给对应的专家模型，专家模型在知识库/表格/计算器中链接具体实体。例如，知识检索动作将查询实体链接到知识库中的具体条目。

### 本体推理
推理体现为**动作序列规划**：agent 根据当前解状态推理下一步应执行哪个动作（从本体中选择）。迭代规划——每执行一个动作后重新评估状态，可能调整后续动作序列。这种动态规划优于静态的端到端推理，因为每步可以委托给专门的专家模型。

### 任务完成
任务目标是多步推理任务的端到端完成。14 个评估数据集上超越先前 agent，7B 模型匹配 GPT-4 证明动作本体+专家模型的有效性。HuskyQA 揭示了混合工具推理的挑战——检索缺失知识与数值推理的组合是当前 agent 的弱点。

## 关联
- [[ActionOntology]] — 动作本体
- [[ExpertModelExecution]] — 专家模型执行
- [[OntoBOT]] — 任务/动作本体（机器人场景）
- [[HEAR]] — 超图本体推理
- [[KML]] — 知识模块组合推理

## 矛盾
- 无
