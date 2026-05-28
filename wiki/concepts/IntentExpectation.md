---
title: "IntentExpectation"
type: concept
tags: [data-type, intent, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## 概要

IntentExpectation 是3GPP TS 28.312中的核心 dataType，表示对一组具有相同属性的 ExpectationObject 的需求、目标和上下文的组合。每个意图可包含一个或多个 IntentExpectation，允许消费者针对不同对象类型表达不同需求。

## 结构

IntentExpectation 包含：

- **expectationObject**：期望所针对的对象（如网络切片、无线网络、服务）
- **expectationTarget(s)**：期望特征，以 [targetName, condition, value range] 元组形式表达
- **context(s)**：目标应在何种条件下达成，同样以 [attribute, condition, value range] 元组形式表达

## ExpectationObject

对象可通过以下方式识别：
- 直接标识符（objectInstance）
- 对象上下文（objectContext）——属性/条件/值元组筛选期望对象，例如"city_ABC中所有网络切片" = [(location, =, city_ABC), (objectType, =, network slice)]

## ExpectationTarget

每个目标是一个三元组：**[targetName, condition, value range]**

示例：
| targetName | 条件 | 值范围 |
|---|---|---|
| 覆盖区域 | 大于 | 40 km半径 |
| 用户吞吐量 | 大于 | 2 Mbps |
| RAN能耗 | 小于 | X Joules |

## 上下文

上下文约束目标应在何时达成。与目标使用相同的元组结构但语义不同——条件触发管理任务而非结果。

示例："切换失败率 < 2% **当** 负载 > 80%" → target=(handoverFailureRate, <, 2%), context=(load, >, 80%)

上下文选择机制：ALL_OF / ONE_OF / ANY_OF——定义如何从多个重叠上下文中进行选择。

## 场景特定期望

TS 28.312 定义了以下场景特定的 IntentExpectation：
- 无线网络期望
- 无线服务期望
- 边缘服务支持期望
- 5GC网络期望
- 端到端网络优化期望
- 网络维护期望

## 关联

- [[IntentIOC]] — 包含 IntentExpectation(s)
- [[IntentDrivenMnS]] — 管理包含这些期望的意图的服务
- [[RulePolicyIntentRelation]] — 意图表达"要什么"，策略表达"怎么做"
- [[PolicyContent]] — 对比：PolicyContent = 条件+动作，IntentExpectation = 对象+目标+上下文