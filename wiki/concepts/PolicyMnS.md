---
title: "Policy MnS"
type: concept
tags: [policy, management-service, 5g]
sources: [28556-j00]
last_updated: 2026-05-22
---

## 概要

Policy 管理服务（Policy MnS）是 3GPP 定义的用于在 5G 移动网络中创建、管理和治理网络 Policy 的管理服务。它通过 MnS Producer–MnS Consumer 交互模型提供生命周期管理（创建、删除、更新、查询、激活、去激活）以及冲突检测/通知能力。

## 生命周期流程

| 流程 | MnS Consumer 动作 | MnS Producer 动作 |
|---|---|---|
| 创建 | 发送 createMOI 请求 | 创建并配置 Policy MOI |
| 删除 | 发送 deleteMOI 请求 | 删除 Policy MOI |
| 更新 | 发送 modifyMOIAttributes 请求 | 更新 Policy MOI |
| 查询 | 发送 getMOIAttributes 请求 | 查询 Policy MOI |
| 激活 | 发送 activation 请求 | 激活 Policy MOI |
| 去激活 | 发送 deactivation 请求 | 去激活 Policy MOI |

## 冲突检测

当 MnS Producer 收到新的或更新的 Policy 时，它会检查是否与已存储的 Policy 存在冲突。若检测到冲突，它将向 MnS Consumer 发送 notifyPolicyConflict 通知（参见 [[PolicyConflictDetection]]）。

## 信息模型

[[PolicyIOC]] 继承自 Top IOC，并携带四个必选属性：policyPriority、policyStatus、policyType 和 [[PolicyContent]]。

## 解决方案集

- **RESTful HTTP**：PUT（创建）、GET（查询）、PUT/PATCH（修改）、DELETE（删除）操作映射到 PoliMnS 资源 URI 上的 HTTP 方法
- **YANG/NETCONF**：使用来自 [[TS28532]] 的通用 Provisioning MnS 解决方案集

## 关联

- [[3GPP]] — 定义 Policy MnS 的标准化组织
- [[PolicyIOC]] — Policy 的信息对象类
- [[PolicyContent]] — 条件-动作数据类型
- [[PolicyConflictDetection]] — 冲突通知机制
- [[5GNetworkManagement]] — 更广泛的管理上下文
- [[TS28532]] — 引用的通用管理服务