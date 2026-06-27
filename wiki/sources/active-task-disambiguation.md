---
title: Active Task Disambiguation with LLMs
type: source
tags:
- task-disambiguation
- Bayesian-experimental-design
- information-gain
- clarification
- LLM
- L2-L3
date: 2025-02-06
source_file: raw/papers/active-task-disambiguation.pdf
last_updated: 2026-06-23
arxiv_id: '2502.04485'
authors:
- Katarzyna Kobalczyk
- Nicolas Astorga
- Tennison Liu
- Mihaela van der Schaar
year: 2025
doi: 10.48550/arXiv.2502.04485
---
## 概要
Active Task Disambiguation 将任务消歧形式化为**贝叶斯实验设计**（Bayesian Experimental Design）问题：通过提问澄清问题，LLM agent 逐步获取额外任务规格，缩小可行解空间。核心创新是让 LLM 生成**最大化信息增益**的针对性问题，将隐式推理转为显式的对解空间的元认知推理。

## 覆盖的模糊层级

**覆盖 L2（多候选歧义）+ L3（参数缺失）**。论文引入"任务歧义"的形式化定义，通过澄清问题缩小可行解空间。不处理 L1（意图本身未知）——假设任务类别已知，处理的是任务规格不充分。

## 核心机制

### 1. 任务歧义形式化定义

论文引入任务歧义的形式化定义：当任务的规格不充分时，存在多个可行解（viable solutions），agent 无法确定用户想要哪一个。消歧就是通过提问逐步缩小可行解空间。

### 2. 贝叶斯实验设计框架

将任务消歧建模为贝叶斯实验设计：
- **先验**：给定模糊查询，agent 对可行解空间有先验信念
- **实验**：每个澄清问题是一个"实验"
- **信息增益**：选择最大化期望信息增益的问题——即最能缩小解空间不确定度的问题
- **后验更新**：用户回答后更新对解空间的信念

### 3. 信息增益最大化的问题选择

核心方法：让 LLM 生成针对性问题，最大化信息增益。这要求 LLM 进行**元认知推理**（meta-cognitive reasoning）——不只是在问题空间内推理，而是显式推理可行解空间，选择最能消除歧义的问题。

**关键发现**：LLM 目前可能缺乏这种元认知推理能力。论文的方法通过将负载从隐式推理转移到显式推理来弥补。

### 4. 与"仅在问题空间推理"的对比

论文的实证结果表明：基于信息增益的问题选择比仅在问题空间内推理的方法更有效。后者只关注"生成好问题"，前者关注"生成能最大消除解空间歧义的问题"。

## 核心论点
- 任务消歧应通过贝叶斯实验设计框架形式化
- 澄清问题应最大化信息增益，而非仅凭语言质量
- LLM 需要元认知推理能力来选择有效问题——显式推理解空间优于隐式推理
- 信息增益导向的问题选择优于仅在问题空间内推理的方法

## 与知识库其他方法的对比

| 维度 | Active Task Disambiguation | [[CICC]] | SAGE-Agent | [[AskBeforePlan]] |
|---|---|---|---|---|
| 理论框架 | 贝叶斯实验设计 | 共形预测 | EVPI（贝叶斯决策论） | 拓扑排序 |
| 问题选择 | 最大化信息增益 | 预测集大小 | EVPI - 冗余成本 | 依赖序 |
| 不确定度空间 | 解空间 | 意图分类 | 工具参数域 | 对话+环境 |
| 统计保证 | 无 | 覆盖率 1-α | 无 | 无 |
| 元认知 | 是（显式推理解空间） | 否 | 是（显式信念） | 否 |

## 关键引述
> "We introduce a formal definition of task ambiguity and frame the problem of task disambiguation through the lens of Bayesian Experimental Design."

> "Our proposed approach of active task disambiguation enables LLM agents to generate targeted questions maximizing the information gain. Effectively, this approach shifts the load from implicit to explicit reasoning about the space of viable solutions."

> "generating effective clarifying questions requires LLM agents to engage in a form of meta-cognitive reasoning, an ability LLMs may presently lack."

## 关联
- [[CICC]] — 有原则澄清三剑客：共形预测（覆盖率保证）vs 贝叶斯实验设计（信息增益）
- [[SAGEAgent]] — SAGE-Agent 的基线之一；SAGE-Agent 在工具参数域上操作更结构化，ATD 在解空间上操作更通用
- [[AskBeforePlan]] — 对比：ATD 用信息增益选择问题 vs Ask-before-Plan 用拓扑排序
- [[handling-vague-user-input]] — 有原则澄清三剑客之一（共形/EVPI/贝叶斯）
- [[IntentSignalTheory]] — 信息增益对应从 P 中恢复 I* 的信息量
