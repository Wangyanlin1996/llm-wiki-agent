---
title: "Intent Utility Function"
type: concept
tags: [intent, utility, negotiation, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## 概要

IntentUtilityFunction 是 3GPP TS 28.312 中的机制，允许 MnS consumer 以数学函数的形式表达定量偏好信息，使 producer 能够选择最大化多个 intent 整体满意度的解决方案。

## 组成部分

- **变量（Variables）**：量化满足的特定方面（例如 expectation target）
- **权重（Weights）**：定义每个变量的相对重要性（例如 latency 权重 > throughput 权重）
- **函数（Function）**：应用于变量的数学表达式（线性、对数、多项式、标量）
- **结果（Result）**：表示所达到的效用水平/满意度的输出

## 使用场景

- 当没有解决方案能完全满足所有 intent 时，utility function 帮助 producer 平衡权衡
- 可按单个 intent 定义或跨多个 intent 定义
- 当一个 intent 有多个 expectation 且具有不同 utility function 时，可进行聚合
- 当变量具有不同量纲（ms、Mbps、Joules）时，需要进行归一化

## 示例

- U1 = f(throughput, latency, packetLoss) — 单个 intent 的单个函数
- U2 = f(latency) 和 U3 = f(throughput) — 不同 expectation 的多个函数

## 模型

通过 IntentUtilityFormula IOC（由 [[IntentIOC]] 的 intentUtilityFormulaRef 属性引用）定义，包含 UtilityDefinition 和 UtilityParameter 数据类型。

## 关联

- [[IntentIOC]] — 通过 intentUtilityFormulaRef 引用 utility formula
- [[IntentDrivenMnS]] — 支持 utility function 的服务
- [[IntentNegotiation]] — 在协商期间使用 utility function
- [[IntentReport]] — 通过 intentUtilityReports 报告 utility 结果