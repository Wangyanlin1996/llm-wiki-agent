---
title: "BayesianDisambiguation"
type: concept
tags: [Bayesian-experimental-design, information-gain, task-disambiguation, clarification, meta-cognitive-reasoning]
sources: [active-task-disambiguation]
last_updated: 2026-06-23
---

# BayesianDisambiguation

贝叶斯消歧——将任务消歧形式化为**贝叶斯实验设计**：每个澄清问题是一个"实验"，选择最大化**期望信息增益**的问题，逐步缩小可行解空间。由 [[ActiveTaskDisambiguation]] 提出。

## 核心思想

任务歧义 = 存在多个可行解，agent 无法确定用户想要哪个。消歧 = 通过提问缩小解空间。

贝叶斯实验设计框架：
1. **先验**：给定模糊查询，对可行解空间有先验信念
2. **实验**：每个澄清问题是一个实验
3. **信息增益**：选择最大化期望信息增益的问题
4. **后验更新**：用户回答后更新信念

## 元认知推理

关键发现：生成有效澄清问题需要**元认知推理**——不只在问题空间内推理，而是显式推理可行解空间。

- **隐式推理**（传统）：LLM 直接在问题空间生成问题
- **显式推理**（本文方法）：LLM 先显式推理解空间，再选择最能消除歧义的问题

信息增益导向的问题选择 > 仅在问题空间内推理的方法。

## 与其他有原则澄清方法的关系

| 方法 | 理论框架 | 不确定度度量 | 问题选择 |
|---|---|---|---|
| [[ConformalIntentClarification]] | 共形预测 | 预测集大小 | 集大→问 |
| [[StructuredUncertaintyClarification]] | EVPI | 期望确信度提升 | EVPI - 成本 |
| BayesianDisambiguation | 贝叶斯实验设计 | 解空间熵 | 最大化信息增益 |

三者都不依赖 prompting 启发式，而是用信息论/统计学的原则性判据选择问题。

## 关联
- [[ActiveTaskDisambiguation]] — 源论文
- [[ConformalIntentClarification]] — 有原则澄清三剑客
- [[StructuredUncertaintyClarification]] — 有原则澄清三剑客
- [[handling-vague-user-input]] — 有原则澄清三剑客之一
