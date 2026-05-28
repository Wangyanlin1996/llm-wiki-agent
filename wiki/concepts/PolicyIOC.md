---
title: "Policy IOC"
type: concept
tags: [information-model, policy, 5g]
sources: [28556-j00]
last_updated: 2026-05-22
---

## 概要

Policy 信息对象类（IOC）是 3GPP TS 28.556 中定义的核心数据结构，用于表示网络 Policy。它继承自 Top IOC（定义于 TS 28.622），封装了 Policy 的优先级、状态、类型和内容。

## 属性

| 属性 | 支持限定符 | 可读 | 可写 | 不变 | 可通知 |
|---|---|---|---|---|---|
| policyPriority | M（必选） | 是 | 是 | 否 | 是 |
| policyStatus | M | 是 | 是 | 否 | 是 |
| policyType | M | 是 | 是 | 否 | 是 |
| policyContent | M | 是 | 是 | 否 | 是 |

## 属性定义

- **policyPriority**：ENUM（LOW, Medium, High）— 指定 Policy 的优先级
- **policyStatus**：ENUM（ACTIVATED, DEACTIVATED），默认 DEACTIVATED — 表示 Policy 是否处于激活状态
- **policyType**：string，多重性 0..N — 指定 Policy 的类型（值在本规范中未定义）
- **policyContent**：[[PolicyContent]] dataType，多重性 1 — 标识条件-动作内容

## 通知

继承通用 Provisioning MnS 通知（notifyMOICreation、notifyMOIDeletion 等），并增加 notifyPolicyConflict 通知（参见 [[PolicyConflictDetection]]）。

## 关联

- [[PolicyMnS]] — 使用此 IOC 的管理服务
- [[PolicyContent]] — 所包含的 dataType
- [[3GPP]] — 定义标准组织
- [[TS28622]] — Top IOC 继承来源