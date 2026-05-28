---
title: "Intent Handling Function"
type: concept
tags: [intent, capability, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## 概要

IntentHandlingFunction 是3GPP TS 28.312中的一个 IOC，表示 MnS 生产者内特定功能的意图处理能力。它暴露生产者可支持的 ExpectationObject 和 ExpectationTarget，使 MnS 消费者能在表达意图之前发现能力。

## 关键要点

- 实例仅由 MnS 生产者创建/修改/删除——消费者无法管理它们
- MnS 消费者查询 IntentHandlingFunction 以发现所支持的 ExpectationObject、ExpectationTarget 和值范围
- 可存在多个 IntentHandlingFunction 实例，各自支持不同领域（例如一个用于 RAN，一个用于 5GC）
- IntentHandlingFunction 实例的 DN 可用于查询其处理的全部 Intent 实例

## 能力暴露

IntentHandlingCapability dataType 包括：
- 所支持的 ExpectationObject 类型及对应 ExpectationTarget
- 所支持的目标值范围
- 可评估的备选期望的描述

## 关联

- [[IntentDrivenMnS]] — 提供这些功能的服务
- [[IntentIOC]] — 由此功能处理的意图
- [[IntentExpectation]] — 此功能支持的期望
- [[3GPP]] — 标准组织