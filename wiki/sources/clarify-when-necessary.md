---
title: 'Clarify When Necessary: Resolving Ambiguity Through Interaction with LMs'
type: source
tags:
- clarification
- ambiguity
- uncertainty-estimation
- intent-sim
- task-agnostic
- LLM
- L2-L3
date: 2023-11-16
source_file: raw/papers/clarify-when-necessary.pdf
last_updated: 2026-06-25
arxiv_id: '2311.09469'
authors:
- Michael J.Q. Zhang
- Eunsol Choi
year: 2023
doi: 10.48550/arXiv.2311.09469
---
## 概要

Zhang & Choi (2023) 提出**任务无关的澄清交互框架**，将"何时澄清"显式建模为不确定性估计问题。核心贡献是 **intent-sim**——一种通过估计**用户意图分布熵**来判断澄清必要性的新颖方法。框架显式分解为三子任务（when/what/how），在 QA、机器翻译、NLI 三个 NLP 应用上验证。当仅允许对 10% 样例澄清时，intent-sim 能**将性能增益翻倍**（相比随机选择）。本文是 [[CICC]] 的**精神前身**——CICC 用共形预测替代 intent-sim 估计意图不确定性，提供了更强的统计保证。

## 覆盖的模糊层级

**覆盖 L2（多候选歧义）+ L3（参数/细节缺失）**。intent-sim 估计的是模型预测的多个"意图"分布的不确定性——当多个意图的预测概率接近（高熵）时，说明存在 L2 级歧义，需要澄清。同时，在 QA/MT/NLI 任务中，模糊性也包含 L3 级的细节缺失（如问题缺少限定条件）。

## 核心机制

### 1. 三子任务框架（when / what / how）

本文首次显式将澄清交互分解为三个独立子任务：

| 子任务 | 问题 | 本文方法 |
|---|---|---|
| **When**（何时澄清） | 给定输入，是否需要问用户？ | intent-sim 不确定性估计（核心贡献） |
| **What**（问什么） | 问哪个澄清问题？ | 从候选问题中选择/生成 |
| **How**（如何用答案） | 拿到答案后如何改进预测？ | 用澄清信息重新推理 |

这一框架后被多项工作采用，成为澄清交互的标准分解。

### 2. intent-sim：意图熵不确定性估计

**核心思想**：通过估计模型预测中**用户意图分布的熵**来判断澄清必要性。

- 传统方法（如 softmax entropy）直接用模型输出概率的熵 → 只反映模型对 top-1 预测的确信度
- intent-sim 的创新：**在意图空间而非输出空间估计不确定性**
  - 通过聚类模型输出为"意图簇"，计算簇间分布的熵
  - 高熵 = 多个意图可能 = 需要澄清
  - 低熵 = 意图明确 = 直接执行

**直觉**：同一个"正确答案"可能对应不同用户意图（如同一个翻译结果可能来自不同源句理解），intent-sim 捕捉这种意图层面的歧义，而非仅看输出层面的一致性。

### 3. 10% 澄清预算实验

| 方法 | 10% 预算下的性能增益 |
|---|---|
| 随机选择澄清样例 | 基线 |
| intent-sim 选择澄清样例 | **基线 × 2**（翻倍） |
| 传统不确定性方法 | 介于两者之间 |

关键发现：在有限澄清预算下（实际场景常见——不能每条都问用户），**选对"问哪些"比"问什么"更重要**。intent-sim 在"when"子任务上的优势直接转化为端到端性能提升。

### 4. 跨任务/跨模型鲁棒性

intent-sim 在三个异构 NLP 任务（QA/MT/NLI）和多种 LM 上均持续优于传统不确定性方法，证明其任务无关性。

## 关键结果

| 指标 | intent-sim | 基线 |
|---|---|---|
| 10% 预算性能增益 | 翻倍 | 1× |
| 跨任务鲁棒性 | QA/MT/NLI 均改进 | 传统方法不一致 |
| 跨模型鲁棒性 | 多种 LM 均有效 | — |

## 核心论点

- **"何时澄清"是澄清交互的瓶颈子任务**：选对问哪些样例比问什么问题更重要
- **意图空间的不确定性 > 输出空间的不确定性**：softmax entropy 只看 top-1 确信度，intent-sim 捕捉意图层面歧义
- **澄清交互应任务无关**：三子任务框架适用于 QA/MT/NLI 等多种 NLP 应用
- **有限预算下选择性澄清是实际部署的关键**：不能每条都问，必须选最有价值的问

## 与知识库其他方法的对比

| 维度 | Clarify When Necessary | [[CICC]] | [[SAGE-Agent]] | [[NeuralEVPI]] |
|---|---|---|---|---|
| 不确定度估计 | intent-sim（意图熵） | 共形预测集大小 | EVPI（参数域信念提升） | 神经网络隐式 |
| 统计保证 | 无 | 覆盖率 1-α | 无 | 无 |
| "何时澄清"判据 | intent-sim 熵 > 阈值 | 预测集大小 > 1 | EVPI 净增益 > 0 | EVPI 分数排序 |
| 任务类型 | 通用 NLP（QA/MT/NLI） | 意图分类 | 工具调用 | StackExchange QA |
| 预算控制 | 显式（10% 预算） | 隐式（α 参数） | 隐式（α 停止系数） | 排序 |
| 年份 | 2023 | 2024 | 2025 | 2018 |

## 谱系意义

本文是 intent-sim 驱动澄清的**起点**，也是 CICC 的直接精神前身：

```
Clarify When Necessary (2023) — intent-sim 估计意图熵判断何时澄清
  ↓
CICC (2024) — 用共形预测替代 intent-sim，提供统计保证
```

[[CICC]] 的核心改进：intent-sim 只能**排序**哪些样例需要澄清（无保证），而 CICC 的共形预测能**保证**真意图在候选集内（覆盖率 1-α）。但两者共享"在意图空间估计不确定性来决定何时澄清"的核心思想。

同时，本文的三子任务框架（when/what/how）也被后续工作广泛采用。

## 关键引述

> "We present a novel uncertainty estimation approach, intent-sim, that determines the utility of querying for clarification by estimating the entropy over user intents."

> "When only allowed to ask for clarification on 10% of examples, our system is able to double the performance gains over randomly selecting examples to clarify."

> "Our work lays foundation for studying clarifying interactions with LMs."

## 关联

- [[CICC]] — 直接继承者：用共形预测替代 intent-sim，从"排序"升级为"有统计保证的澄清"
- [[SAGE-Agent]] — 同属"有原则澄清"谱系，但用 EVPI 在参数域上选择问题
- [[NeuralEVPI]] — 同属澄清问题选择谱系，但用 EVPI 排序而非意图熵
- [[handling-vague-user-input]] — "何时澄清"子任务的代表性方法，L2-L3 覆盖
- [[AskBeforePlan]] — 同覆盖 L3，但用 prompt 二值判断而非不确定性估计
- [[IntentSimUncertainty]] — 本文提出的核心方法概念页
- [[IntentSignalTheory]] — intent-sim 的意图熵对应 IST 中 I* 的不确定度
