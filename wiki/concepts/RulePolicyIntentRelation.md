---
title: "Rule-Policy-Intent Relation"
type: concept
tags: [intent, policy, rule, abstraction, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## 概要

3GPP TS 28.312 第 4.4 节描述的 Rule→Policy→Intent 关系表示管理抽象层次从"怎么做"到"要什么"的渐进转变：

- **Rule（规则）**：待执行的显式逻辑或公式 — 完全指定"怎么做"（例如：若 X > 阈值，执行命令 Y）
- **Policy（策略）**：条件动作规范 — 指定当条件发生时采取什么动作，但保留一定灵活性（例如：当吞吐量 < 5Mbps 时，采取优化动作）
- **Intent（意图）**：声明式目标规范 — 指定期望"要什么"结果，而不指定"怎么做"（例如：该区域平均吞吐量 > 5Mbps）

## 抽象谱系

```
Rule ←— "how" focus —→ Policy ←— shifting to "what" —→ Intent
  (explicit logic)       (condition-action)          (declarative goal)
```

当前电信系统主要处于 Rule/Policy 层级（聚焦"怎么做"）。5G 网络日益增长的复杂性驱动着向 Intent（聚焦"要什么"）的转变。

## 实际关系

- Intent 可以**翻译**为 Policy，用于闭环自动化（参见 [[IntentDrivenMnS]] 第 4.3 节）
- Policy 可以**翻译**为 Rule，用于执行
- Intent → Policy → Rule 是从抽象到具体的分解链
- [[PolicyMnS]] 和 [[IntentDrivenMnS]] 是互补的：Intent 表达目标，Policy 定义达成目标的条件动作

## 模型比较

| 方面 | Rule（规则） | Policy（策略）（[[PolicyIOC]]） | Intent（意图）（[[IntentIOC]]） |
|---|---|---|---|
| 聚焦点 | 怎么做 | 怎么做+要什么 | 要什么 |
| 模型 | 显式逻辑 | condition + action | expectationObject + target + context |
| 灵活性 | 无 | 条件性 | 声明式 |
| 实现方式 | 完全指定 | 部分指定 | 未指定 |

## 关联

- [[PolicyMnS]] — 中间抽象层级的 Policy 管理
- [[IntentDrivenMnS]] — 最高抽象层级的 Intent 管理
- [[PolicyIOC]] — Policy 数据结构
- [[IntentIOC]] — Intent 数据结构
- [[PolicyContent]] — Policy 的条件-动作模型
- [[IntentExpectation]] — Intent 的对象-目标-上下文模型
- [[5GNetworkManagement]] — 更广泛的管理领域