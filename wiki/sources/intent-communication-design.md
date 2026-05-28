---
title: "Designing Intent Communication"
type: source
tags: [intent-understanding, intent-communication, human-agent, design-space]
date: 2025-10-28
source_file: raw/papers/intent-communication-design.md
last_updated: 2026-05-27
---

## 概要
本文为 intent communication 引入多维设计空间，沿三个维度展开：Transparency（传达什么）、Abstraction（何时传达）和 Modality（如何传达），应用于旁观者交互、协作任务和共享控制场景。它弥合了 intent 内容与 communication 实现之间的鸿沟，为可迁移的 agent-human 交互奠定基础。

## 关键论点
- Intent communication 方式僵化、agent 特定且范围狭窄
- 传达什么/如何/何时很少被系统性地关联
- Transparency×Abstraction×Modality 设计空间生成跨域策略
- 连接 intent 内容与实现使交互更安全、更直觉

## 关键引述
> "existing models of what to communicate are rarely linked to systematic choices of how and when to communicate" — 鸿沟诊断

> "our design space provides a foundation for designing safer, more intuitive, and more transferable agent-human interactions" — 贡献

## 关联
- [[IntentUnderstanding]] — 设计空间指导 IntentUnderstanding 如何被传达
- [[IntentSignalTheory]] — IST 的 carrier 概念与 Transparency×Abstraction×Modality 一致
- [[IntPro]] — IntPro 的 per-user adaptation 受益于结构化的 intent communication

## 矛盾
- 与 agent 特定的僵化 communication 矛盾：设计空间主张系统化、可迁移的 intent communication 策略