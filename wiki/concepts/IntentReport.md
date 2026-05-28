---
title: "Intent Report"
type: concept
tags: [intent, report, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## 概要

IntentReport 是3GPP TS 28.312中的一个 IOC，表示从 MnS 生产者向 MnS 消费者的意图报告信息。它由 MnS 生产者基于 [[IntentIOC]] 中指定的 IntentReportControl 创建。当意图被删除时，对应的 IntentReport 实例自动删除。

## 报告类型

| 报告类型 | 属性 | 内容 |
|---|---|---|
| 满足报告 | intentFulfilmentReport | 满足状态和目标达成值 |
| 冲突报告 | intentConflictReports | 冲突类型（意图/期望/目标）+解决方案 |
| 可行性检查报告 | intentFeasibilityCheckReport | 可行或不可行，附原因 |
| 探索报告 | intentExplorationReport | 预评估期间目标/上下文的最佳值 |
| 协商报告 | intentFulfilmentNegotiationReport | 满足阶段的替代方案和结果 |
| 效用报告 | intentUtilityReports | 效用函数计算结果 |

## 属性

所有报告属性均为 CM（条件必选）——仅在意图处理功能支持相应能力时存在。关键属性：

- intentFulfilmentReport、intentConflictReports、intentFeasibilityCheckReport、intentExplorationReport、intentFulfilmentNegotiationReport、intentUtilityReports（均为 CM，只读，可通知）
- lastUpdatedTime (M)
- intentReference (M, 只读) — 对关联 Intent 实例的 DN 引用

## 管理操作

| 操作 | IS 操作 |
|---|---|---|
| 查询意图报告 | getMOIAttributes |
| 订阅意图报告 | createMOI（在 NtfSubscriptionControl 上） |
| 通知意图报告 | notifyMOIAttributeValueChanges |
| 取消订阅意图报告 | deleteMOI |

## 关联

- [[IntentIOC]] — 此报告所属的意图
- [[IntentDrivenMnS]] — 产生报告的服务
- [[IntentConflictResolution]] — 报告中的冲突信息
- [[IntentNegotiation]] — 报告中的协商信息
- [[IntentUtilityFunction]] — 报告中的效用结果