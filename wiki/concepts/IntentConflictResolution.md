---
title: "Intent Conflict Resolution"
type: concept
tags: [intent, conflict, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## 概要

3GPP TS 28.312 中的 Intent 冲突解决涵盖了三种冲突类型的检测和处理：target conflict（同一 expectation 内）、expectation conflict（同一 intent 内）和 intent conflict（不同 intent 之间）。冲突产生于为某个 target 执行的动作导致另一个 target 降级。

## 三种冲突类型

| 冲突类型 | 范围 | 示例 |
|---|---|---|
| Target conflict | 同一 expectation 中的两个 target | throughput↑ vs interference↓ |
| Expectation conflict | 同一 intent 中的两个 expectation | latency expectation vs throughput expectation |
| Intent conflict | 两个不同的 intent | 节能 intent vs 覆盖 intent |

## 解决机制

- **Suspension**：Producer 暂停冲突的 intent 或包含冲突的整个 intent
- **Recommendation**：Producer 推荐新的 intent（修改的 expectation、target 或缩小范围）
- **Preemption（抢占）**：intentPriority 和 intentPreemptionCapability 允许高优先级 intent 抢占低优先级 intent
- **Consumer 指导**：Consumer 可提供有序的 expectation 列表或明确的优先级
- **缩小范围**：Consumer 可缩小期望管理的实体范围以解决冲突

## 报告

冲突信息通过 [[IntentReport]] 的 intentConflictReports 属性报告，包含冲突类型和可能的解决方案。

## 与 Policy 冲突的比较

TS 28.556 中的 [[PolicyConflictDetection]] 检测新 policy 是否与已存储的 policy 冲突，并通过 notifyPolicyConflict 通知。Intent 冲突更为丰富——包含三个冲突层级，附带解决推荐和抢占机制。

## 关联

- [[IntentDrivenMnS]] — 执行冲突检测的服务
- [[IntentIOC]] — 可能发生冲突的 intent
- [[IntentExpectation]] — 可能发生冲突的 expectation/target
- [[IntentReport]] — 报告冲突信息的位置
- [[PolicyConflictDetection]] — 更简单的 policy 层级冲突机制