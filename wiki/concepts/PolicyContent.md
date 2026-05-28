---
title: "PolicyContent"
type: concept
tags: [data-type, policy, 5g]
sources: [28556-j00]
last_updated: 2026-05-22
---

## 概要

PolicyContent 是 3GPP TS 28.556 中定义的 dataType，通过条件-动作对（condition-action pair）表示网络 Policy 的核心逻辑。当条件满足时，触发对应的动作。

## 属性

| 属性 | 支持限定符 | 可读 | 可写 | 不变 | 可通知 |
|---|---|---|---|---|---|
| condition | M（必选） | 是 | 是 | 否 | 是 |
| action | M（必选） | 是 | 是 | 否 | 是 |

## 属性定义

- **condition**：标识 Policy 的触发条件。类型取决于具体的 Policy 实现（标准中未指定）。
- **action**：标识当条件满足时要执行的动作。类型同样取决于具体的 Policy 实现。

## 关联

- [[PolicyIOC]] — 将 PolicyContent 作为其 policyContent 属性包含
- [[PolicyMnS]] — 管理具有此结构的 Policy 的管理服务
- [[5GNetworkManagement]] — 更广泛的管理领域