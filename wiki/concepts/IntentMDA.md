---
title: "Intent-driven MDA"
type: concept
tags: [intent, mda, analytics, 5g]
sources: [28912-j00]
last_updated: 2026-05-22
---

## 概要

Intent-driven MDA（管理数据分析）是 3GPP TR 28.912 中研究的机制，其中 MDA 功能由 intent expectation 触发。当 intent MnS producer 接收到 intent 时，它检查 ExpectationTarget 是否在关联 MDA 功能的 supportedMDACapabilities 范围内，如果是，则通过 MDARequest 请求分析。

## 流程

1. Intent MnS producer 接收包含 ExpectationTarget 的 intent
2. 检查 target 是否在关联 MDA 功能的 supportedMDACapabilities 范围内
3. 如不支持 → 通知 consumer 由于缺乏 MDA 能力无法满足 intent
4. 如支持 → 创建 MDARequest（createMOI），分析范围基于 expectationObject，请求的 MDA 输出基于 expectationTarget，context 信息来自 intent
5. MDA 功能执行分析并返回报告
6. Intent MnS producer 使用 MDA 报告决定如何处理 intent 满足

## 示例

如果 intent 包含 dLLatencyTarget 或 uLLatencyTarget（如 TS 28.312 中的 Service Support Expectation），关联的 MDA 功能必须具备延迟分析能力。如缺乏此能力，该 intent 将被报告为无法满足。

## 关联

- [[IntentDrivenMnS]] — 集成 MDA 进行 intent 满足的服务
- [[IntentIOC]] — 触发 MDA 分析的 intent
- [[IntentExpectation]] — 其 target 驱动 MDA 范围的 expectation
- [[3GPP]] — 标准组织