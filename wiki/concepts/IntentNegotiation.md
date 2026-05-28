---
title: "Intent Negotiation"
type: concept
tags: [intent, negotiation, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## 概要

3GPP TS 28.312 中的 Intent 协商使 MnS consumer 和 MnS producer 之间能够进行协作交互，以找到满足 intent 的最佳方式。协商分为两个阶段：预评估阶段（intent 提交前）和满足阶段（提交后）。

## 预评估阶段

| 能力 | 描述 |
|---|---|
| Intent feasibility check（可行性检查） | 检查提议的 intent 是否能被 producer 支持 |
| Intent exploration（探索） | 寻找与 producer 能力对齐的 target/context 最佳值 |

两种探索场景：
1. 探索单个 target/context 的最佳值
2. 探索多个 target/context 的最佳组合值（例如平衡节能与吞吐量）

## 满足阶段

| 能力 | 描述 |
|---|---|
| 检查可满足的结果 | 获取 producer 可交付的可能结果列表 |
| 检查最佳可能结果 | 在保持其他不变的情况下，找到特定或所有 target 的最佳结果 |
| 推荐可满足的结果 | Producer 提供推荐的 target/context |
| 建议偏好结果 | Consumer 在多个替代方案中建议偏好，可能附带 utility function 或满意度指标 |

## IS 操作

| 操作 | IS 映射 |
|---|---|
| Intent feasibility check | createMOI |
| Intent exploration | createMOI |
| Intent 满足协商 | createMOI / modifyMOIAttributes |

## 关联

- [[IntentDrivenMnS]] — 提供协商的服务
- [[IntentIOC]] — 正在协商的 intent
- [[IntentReport]] — 协商报告
- [[IntentUtilityFunction]] — 在协商中用于偏好量化
- [[IntentConflictResolution]] — 冲突可能触发协商