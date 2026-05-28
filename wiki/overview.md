---
title: "概览"
type: synthesis
tags: []
sources: [28556-j00, 28312-j50, 28622-k20, 28912-j00, 28914-j00]
last_updated: 2026-05-28
---

# 概览

## 5G 网络管理：策略与意图

本 wiki 涵盖两个互补的 3GPP 5G 网络管理规范：

- **TS 28.556** ([[PolicyMnS]]) — 策略管理："什么条件下采取什么动作"
- **TS 28.312** ([[IntentDrivenMnS]]) — 意图管理："要达到什么结果，不指定怎么做"

### 抽象层级

[[RulePolicyIntentRelation]] 描述了管理范式的渐进转变：

```
Rule（显式逻辑）→ Policy（条件+动作）→ Intent（声明式目标）
       "怎么做"            "怎么做+要什么"          "要什么"
```

Policy ([[PolicyIOC]]) 使用简单的**条件-动作**模型 ([[PolicyContent]])。Intent ([[IntentIOC]]) 使用更丰富的 **ExpectationObject + ExpectationTarget + Context** 模型 ([[IntentExpectation]])。意图可以翻译为策略以驱动闭环自动化，但反向不行——策略无法表达抽象目标。

### 策略管理（TS 28.556）

[[PolicyIOC]] 实例有四个必选属性：policyPriority (LOW/Medium/High)、policyStatus (ACTIVATED/DEACTIVATED)、policyType、policyContent。生命周期通过 [[TS28532]] 的通用 Provisioning MnS 管理。[[PolicyConflictDetection]] 提供单级冲突通知 (notifyPolicyConflict)。

### 意图管理（TS 28.312）

[[IntentIOC]] 实例承载 intentExpectations、intentAdminState、intentPriority、intentReportControl 以及高级特性（intentPreemptionCapability、implicitIntentIndex、intentUtilityFormulaRef）。意图生命周期有六个状态：ACKNOWLEDGED → COMPLIANT → FULFILLED → DEGRADED（SUSPENDED 和 FULFILLMENT_FAILED 为替代路径）。

意图期望按用户角色分类：
- **Intent-CSC** — 通信服务客户（CSC）表达服务期望
- **Intent-CSP** — 通信服务提供商（CSP）表达网络期望
- **Intent-NOP** — 网络运营商（NOP）表达子网络期望

意图翻译链跨角色：CSC→CSP→NOP→NEP。

### 冲突处理对比

| 特征 | Policy (TS 28.556) | Intent (TS 28.312) |
|---|---|---|
| 冲突层级 | 单级（策略 vs 策略） | 三级（目标、期望、意图） |
| 解决方式 | 仅通知 | 抢占、建议、协商 |
| 通知方式 | notifyPolicyConflict | IntentReport with conflictReports |

### 意图高级特性

- **[[IntentNegotiation]]** — 预评估（可行性检查、探索）与满足阶段（替代结果、最优结果）
- **[[IntentUtilityFunction]]** — 数学偏好表达（变量、权重、函数、结果），用于定量方案选择
- **[[IntentReport]]** — 六类报告：满足、冲突、可行性、探索、协商、效用
- **[[IntentHandlingFunction]]** — Producer 能力暴露（支持的对象、目标、值范围）

### 标准上下文

两个规范都属于 [[5GNetworkManagement]] 族（TS 28.x 系列），由 [[3GPP]] TSG SA5 制定。它们复用 [[TS28532]] 的通用 Provisioning MnS，并继承 [[TS28622]] 中定义的 [[TopIOC]]。

### 基础：通用 NRM（TS 28.622）

TS 28.622 提供了基础 [[NRM]] 信息模型。[[TopIOC]] 是 IOC 继承层次的根——所有领域特定 IOC（Policy、Intent、IntentReport、IntentHandlingFunction）都通过 TopX 继承它（必选 objectClass + objectInstance 属性）。关键基础 IOC 包括 SubNetwork（管理实体集合）、ManagedElement（网元表示）、ManagedFunction（功能子类化）、NtfSubscriptionControl（通知订阅），以及通用数据类型（GeoArea、TimeWindow、SchedulingTime）。

### 研究报告：TR 28.912（Rel-18）和 TR 28.914（Rel-19）

规范性 TS 28.312 特性源于两份研究 TR：

- **TR 28.912**（Rel-18）：研究了意图驱动 RAN 节能、三级冲突分类、5GC 期望、[[IntentReport]] IOC、闭环组成、[[IntentHandlingFunction]]、[[IntentSONOrchestration]]、[[IntentMDA]]、AI/ML 能力映射、TM Forum 协作
- **TR 28.914**（Rel-19）：研究了增强无线服务/网络期望、隐式意图报告、意图降级 (PreferenceWeight)、带满意度指数的 [[IntentUtilityFunction]]、满足阶段的 [[IntentNegotiation]]、意图探索、可行性检查 (intentMgmtPurpose)、网络维护意图、厂商扩展指南