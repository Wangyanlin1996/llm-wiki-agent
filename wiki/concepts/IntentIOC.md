---
title: "Intent IOC"
type: concept
tags: [information-model, intent, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## 概要

Intent Information Object Class (IOC) 是3GPP TS 28.312中表示 MnS 消费者与 MnS 生产者之间意图的核心数据结构。它继承自 Top IOC（TS 28.622），封装了意图期望、管理状态、报告控制、优先级以及效用函数和隐式意图发现等高级特性。

## 属性

| 属性 | SQ | 可读 | 可写 | 不变 | 可通知 |
|---|---|---|---|---|---|
| intentExpectations | M | Yes | Yes | No | No |
| userLabel | M | Yes | Yes | No | No |
| intentMgmtPurpose | M | Yes | Yes | No | No |
| contextSelectivity | O | Yes | Yes | No | No |
| expectationSelectivity | O | Yes | Yes | No | No |
| intentContexts | O | Yes | Yes | No | No |
| intentReportControl | M | Yes | Yes | No | No |
| intentPriority | O | Yes | Yes | No | Yes |
| intentAdminState | CM | Yes | Yes | No | No |
| intentPreemptionCapability | CM | Yes | Yes | No | No |
| implicitIntentIndex | CM | Yes | Yes | No | No |
| consumerSatisfactionIndexThreshold | CO | Yes | Yes | No | No |
| intentReportReference | M | Yes | No | No | No |
| intentUtilityFormulaRef | CM | Yes | Yes | No | Yes |

## 关键属性定义

- **intentExpectations**：[[IntentExpectation]] 列表——表达期望结果的核心内容
- **intentAdminState**：ACTIVATED/DEACTIVATED——支持意图挂起机制（CM：条件必选）
- **intentPriority**：整数——用于意图间冲突解决的优先级
- **intentPreemptionCapability**：指示此意图是否可以抢占低优先级意图（CM）
- **contextSelectivity**：ALL_OF / ONE_OF / ANY_OF——如何在意图级上下文中进行选择
- **expectationSelectivity**：ALL_OF / ONE_OF / ANY_OF——如何在备选期望中进行选择（用于可行性验证）。**注意**：此属性的详细语义（ONE_OF = 满足任意一个期望，ANY_OF = 尽可能满足多个期望，ALL_OF = 满足全部期望）仅在 Stage 3 YAML（`TS28312_IntentNrm.yaml:246-250`）中定义，未在源文档 `[[28312-j50]]` 的 Stage 2 文本中显式描述
- **implicitIntentIndex**：布尔值——启用/禁用隐式意图信息发现
- **intentReportControl**：[[IntentReportControl]] dataType——指定报告类型、条件和频率
- **intentUtilityFormulaRef**：对 [[IntentUtilityFunction]] 实例的引用

## 意图处理状态生命周期

| 状态 | 转换触发条件 |
|---|---|
| ACKNOWLEDGED | Intent 实例已创建 |
| COMPLIANT | 可行性检查结果为"可行" |
| FULFILLMENT_FAILED | 可行性检查结果为"不可行"或生产者无法满足 |
| SUSPENDED | intentAdminState 设为 DEACTIVATED |
| FULFILLED | 生产者认为意图已满足 |
| DEGRADED | 之前已满足的意图不再符合要求 |
| TERMINATED | Intent 已删除 |

## 关联

- [[IntentDrivenMnS]] — 管理 Intent IOC 实例的管理服务
- [[IntentExpectation]] — 所包含的期望
- [[IntentReport]] — 关联的报告实例
- [[IntentHandlingFunction]] — 处理此意图的功能
- [[IntentUtilityFunction]] — 可选的效用公式引用
- [[3GPP]] — 标准组织
- [[TS28622]] — Top IOC 继承来源