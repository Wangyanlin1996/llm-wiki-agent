---
title: "Intent-driven SON Orchestration"
type: concept
tags: [intent, son, orchestration, 5g]
sources: [28912-j00]
last_updated: 2026-05-22
---

## 概要

Intent-driven SON（自组织网络）Orchestration 是 3GPP TR 28.912 中研究的机制，其中 SON 功能由 intent expectation 驱动。SON orchestrator 根据参数和 context 是否引用网络控制参数或 KPI，将接收到的 intent 分为三种类型，并在 SON 执行中检测矛盾。

## SON 的 Intent 类型

| 类型 | 参数 | Context | 示例 |
|---|---|---|---|
| Type 1 | 网络控制参数 | 无或控制参数 | 增大小区 TXP；使小区 TXP 恒定 |
| Type 2 | KPI | 无或 KPI | 降低小区干扰；提高小区吞吐量 |
| Type 3 | 混合（控制参数 + KPI） | 混合 | 使小区 TXP 恒定且降低干扰 |

如果 intent 不属于以上三种类型，SON orchestration 将通知 consumer 该 intent 无法通过 SON 执行。

## 矛盾检测

SON orchestration 可检测不同 expectation 的 target 之间的矛盾。这些矛盾通过 FulfilmentInfo 或 intent report 中的属性报告给 intent MnS consumer，表明在 SON orchestration 中检测到的矛盾（不同于 intent 层级的冲突）。

## 关联

- [[IntentDrivenMnS]] — 可利用 SON orchestration 进行 intent 满足的服务
- [[IntentIOC]] — 正在被 orchestrate 的 intent
- [[IntentExpectation]] — 为 SON 分类的 expectation
- [[IntentConflictResolution]] — 相关但不同（SON 矛盾 vs intent 冲突）
- [[3GPP]] — 标准组织