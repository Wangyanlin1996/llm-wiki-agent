---
title: "NRM"
type: concept
tags: [nrm, information-model, network-resource, 5g]
sources: [28622-k20]
last_updated: 2026-05-22
---

## 概要

Network Resource Model（NRM）是 3GPP 在 TS 28.622 中定义的概念，即"一组 IOC 的集合，包含其关联、属性和操作，代表一组被管理的网络资源"。通用 NRM（TS 28.622）提供了基础 IOC 和数据类型，领域特定 NRM（如 5G 的 TS 28.541 等）在此基础上进行扩展。

## 结构

NRM 定义了：
- **IOC**（Information Object Classes，信息对象类）——网络资源的管理方面
- **关联**（Associations）—— IOC 之间的关系（引用属性、包含关系）
- **属性**（Attributes）—— IOC 的属性
- **操作**（Operations）—— 可在 IOC 实例上调用的管理服务
- **通知**（Notifications）—— IOC 实例的事件报告

NRM 实例（MIB — Management Information Base，管理信息库）由以下组成：
1. 命名空间（DN 包含层次）
2. 带属性的被管对象
3. 被管对象之间的关联

## 通用与领域特定

- **通用 NRM**（TS 28.622）：[[TopIOC]]、SubNetwork→子网络、ManagedElement→管理单元、ManagedFunction 等
- **5G NRM**（TS 28.541）：在通用基础上扩展 5G 特定 IOC（gNB, NRCellDU, AMF 等）
- **策略 NRM**（TS 28.556）：在通用基础上扩展 [[PolicyIOC]]
- **意图 NRM**（TS 28.312）：在通用基础上扩展 [[IntentIOC]], [[IntentReport]], [[IntentHandlingFunction]]

## 关键定义

> "网络资源（network resource）：为网络和服务管理目的，由 Information Object Class（IOC）所代表的离散实体。" — TS 28.622 第 3.1 节

> "Network Resource Model（NRM）：一组 IOC 的集合，包含其关联、属性和操作，代表一组被管理的网络资源。" — TS 28.622 第 3.1 节

## 关联

- [[TopIOC]] — 锚定 NRM 层次的根 IOC
- [[TS28622]] — 通用 NRM 规范
- [[5GNetworkManagement]] — 使用 NRM 的更广泛领域
- [[PolicyIOC]] — 策略特定的 NRM 扩展
- [[IntentIOC]] — 意图特定的 NRM 扩展