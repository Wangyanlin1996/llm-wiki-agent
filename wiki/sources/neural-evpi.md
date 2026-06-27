---
title: 'Learning to Ask Good Questions: Ranking Clarification Questions using Neural
  Expected Value of Perfect Information'
type: source
tags:
- clarification-question
- EVPI
- neural-network
- ranking
- StackExchange
- clarification
- L3
date: 2018-05-12
source_file: raw/papers/neural-evpi.pdf
last_updated: 2026-06-25
arxiv_id: '1805.04655'
authors:
- Sudha Rao
- Hal Daumé III
year: 2018
venue: NAACL 2018
doi: 10.48550/arXiv.1805.04655
---
## 概要

Rao & Daumé III (NAACL 2018) 提出**用神经网络基于 EVPI（期望完美信息价值）排序澄清问题**的开山之作。核心洞察：**好问题是其期望答案能提供有用信息的问题**。从 StackExchange 构建首个大规模澄清问答数据集（~77K 帖子），在 500 样本上经专家评估显著超越基线。本文是 EVPI 驱动澄清问题选择的**鼻祖**，[[SAGE-Agent]] 的 EVPI 问题选择机制直接继承自本文。

## 覆盖的模糊层级

**覆盖 L3（参数/细节缺失）**。StackExchange 场景中，用户发帖描述技术问题但缺少关键细节（如系统版本、错误日志、操作步骤），社区成员提出澄清问题以补全缺失信息。这与 [[AskBeforePlan]] 的 missing details 场景一致。不处理 L1（意图本身未知）或 L2（多候选歧义）——假设帖子意图明确（寻求技术帮助），只是细节不足。

## 核心机制

### 1. EVPI 理论灵感

论文将决策论中的**期望完美信息价值**（Expected Value of Perfect Information）引入澄清问题排序：

- 给定一个帖子（post）和候选澄清问题集，每个问题的价值 = **其答案的期望有用性**
- "有用"定义为：答案能帮助更好地解决原帖问题
- 这与 [[SAGE-Agent]] 的 EVPI 公式 `E_r[max_c π_c(t|q,r)] - max_c π_c(t)` 同源——前者用神经网络近似"答案有用性"，后者在工具参数域上显式计算信念提升

### 2. 神经网络架构

模型将帖子-问题-答案三元组编码为向量表示，学习排序澄清问题：

- **输入**：原帖 + 候选澄清问题（+ 该问题的潜在答案）
- **输出**：该澄清问题的质量分数（用于排序）
- **训练信号**：StackExchange 上社区实际采纳的澄清问题作为正例

### 3. StackExchange 数据集

| 维度 | 详情 |
|---|---|
| 总帖子对 | ~77K（帖子 + 澄清问题 + 答案） |
| 域 | askubuntu, unix, superuser |
| 数据来源 | StackExchange 社区自然交互 |
| 评估集 | 500 样本，专家人工评判 |
| 特色 | 首个大规模澄清问答数据集 |

### 4. 三子任务框架

论文隐含地将澄清交互分解为：
1. **识别需要澄清**（帖子存在信息缺口）
2. **生成/选择澄清问题**（EVPI 排序，本文核心）
3. **利用答案改进回答**（答案有用性评估）

这一分解后被 [[ClarifyWhenNecessary]] 显式提出为三子任务框架（when/what/how）。

## 关键结果

| 指标 | Neural EVPI | 基线 |
|---|---|---|
| 专家评估（500 样本） | 显著优于受控基线 | — |
| 数据集规模 | ~77K 帖子对 | 此前无大规模澄清问答数据集 |

（注：因 PDF 下载受限，具体数值结果来自 abstract 描述，未获取完整实验表格）

## 核心论点

- **EVPI 是澄清问题选择的正确原则**：好问题的判据不是"看起来相关"，而是"其答案的期望信息价值高"
- **StackExchange 是天然的澄清交互数据源**：社区成员自发提问以补全信息，构成大规模监督信号
- **神经网络可学习 EVPI 近似**：不必显式建模信念状态，可从数据中学习"什么样的澄清问题有用"

## 与知识库其他方法的对比

| 维度 | Neural EVPI | [[SAGE-Agent]] | [[ClarifyWhenNecessary]] | [[CICC]] |
|---|---|---|---|---|
| EVPI 形式 | 神经网络隐式近似 | 显式公式 `E_r[max_c π_c] - max_c π_c` | 无（用 intent-sim 熵） | 无（用预测集大小） |
| 不确定度空间 | 隐式（帖子-问题表示） | 工具参数域 | 意图分类空间 | 意图分类 softmax |
| 数据来源 | StackExchange 自然交互 | ClarifyBench 模拟 | QA/MT/NLI 任务 | 7 个意图分类数据集 |
| 统计保证 | 无 | 无（期望值） | 无 | 覆盖率 1-α |
| 年份 | 2018 | 2025 | 2023 | 2024 |

## 谱系意义

本文是 EVPI 驱动澄清的**起点**：

```
Neural EVPI (2018) — EVPI 排序澄清问题的概念起源
  ↓
SAGE-Agent (2025) — 在工具参数域上显式 EVPI + 冗余成本 + 停止判据
```

[[SAGE-Agent]] 明确引用本文作为 EVPI 灵感来源，将 Neural EVPI 的"用神经网络近似 EVPI"升级为"在结构化参数域上显式计算 EVPI"。

## 关键引述

> "Our model is inspired by the idea of expected value of perfect information: a good question is one whose expected answer will be useful."

> "We create a dataset of clarification questions consisting of ~77K posts paired with a clarification question (and answer) from three domains of StackExchange: askubuntu, unix and superuser."

## 关联

- [[SAGE-Agent]] — 直接继承者：将 Neural EVPI 的概念从隐式神经网络近似升级为结构化参数域上的显式 EVPI 计算
- [[ClarifyWhenNecessary]] — 精神继承者：将澄清交互显式分解为 when/what/how 三子任务，但用 intent-sim 替代 EVPI
- [[CICC]] — 同属"有原则澄清"谱系，但用共形预测而非 EVPI 提供保证
- [[handling-vague-user-input]] — EVPI 技术线的起源，L3 澄清先行
- [[AskBeforePlan]] — 同覆盖 L3（参数缺失），但用拓扑排序而非 EVPI 选择问题
- [[IntentSignalTheory]] — EVPI 的"答案有用性"对应 IST 中从 P 恢复 I* 的信息增益
