---
title: "Intent Driven MnS"
type: concept
tags: [intent, management-service, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## 概要

Intent Driven Management Service (IDMS) 是3GPP定义的管理服务，允许消费者以意图（声明式"要什么"语句）表达期望的网络/服务结果，而生产者决定"如何"实现。它以更高的抽象层级替代了传统的规则/策略式管理。

## 关键能力

- **意图生命周期**：创建、删除、修改、查询、激活、去激活——均通过来自 [[TS28532]] 的通用 Provisioning MnS 操作实现
- **意图翻译**：生产者将意图翻译为可执行动作（策略、闭环、AI/ML机制）
- **意图报告**：生产者报告满足状态、冲突、可行性、探索结果、协商结果和效用结果
- **意图协商**：预评估（可行性检查、探索）和满足阶段（对结果的协商）
- **意图闭环**：意图可被翻译为驱动闭环自动化的策略（实现方式未标准化）

## 意图满足类别

- **意图部署**：满足新收到意图的步骤（初始设置）
- **意图保障**：维持持续质量要求的周期性动作（持续监控）

## 基于角色的意图类型

| 角色 | 意图类型 | 示例 |
|---|---|---|
| CSC (通信服务客户) | Intent-CSC | "为车辆启用V2X服务" |
| CSP (通信服务提供商) | Intent-CSP | "提供支持高速公路上500辆车辆的网络" |
| NOP (网络运营商) | Intent-NOP | "提供满足区域覆盖的无线网络" |

意图翻译链：CSC→CSP→NOP→NEP，每个层级翻译为更低层级的意图。

## 关联

- [[IntentIOC]] — 意图的信息对象类
- [[IntentExpectation]] — 期望的结构方式
- [[IntentReport]] — 结果的报告方式
- [[IntentHandlingFunction]] — 能力暴露
- [[IntentConflictResolution]] — 冲突处理
- [[IntentNegotiation]] — 协商机制
- [[IntentUtilityFunction]] — 偏好量化
- [[RulePolicyIntentRelation]] — 与策略/规则的关系
- [[PolicyMnS]] — 互补的策略式管理
- [[3GPP]] — 标准组织
- [[TS28532]] — 通用 Provisioning MnS 基础