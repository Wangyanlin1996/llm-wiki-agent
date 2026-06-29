---
title: "Causal Past Logic for Runtime Verification of Distributed LLM Agent Workflows"
type: source
tags: [agent-explainability, runtime-verification, distributed-systems, causal-logic]
date: 2026-05-20
source_file: raw/papers/causal-past-logic-runtime-verification.pdf
arxiv_id: "2605.20923"
authors: ["Benedikt Bollig"]
venue: arXiv preprint (20 pages)
citation_count: pending
---

## Summary

本文扩展 ZipperGen agent 工作流框架，引入 Causal Past Logic（CPL）——一种过去时序逻辑，用于分布式 LLM agent 工作流中的条件守卫和循环。核心洞察：异步执行中，一个决策只能依赖于因果可见的事件——日志中较早出现的事件在本地可能仍然未知。CPL 守卫可检查另一 lifeline 的最新因果可见事件及其存储变量，作为源码级守卫在线评估并影响控制流。作者给出向量时钟监控器并证明本地计算的监控值与守卫的指称语义一致。

## Key Claims

- **分布式 LLM agent 工作流不应作为单一顺序日志监控**——异步执行中因果可见性是局部的
- **CPL 将运行时验证嵌入协调语言本身**，而非事后检查执行日志
- 守卫可检查其他 lifeline 的最新因果可见事件——标准过去时态模态（previous、since）+ 跨 lifeline 最新值视图
- 向量时钟监控器证明：本地计算的监控值 = 守卫在当前事件的指称语义
- 运行时验证成为协调语言的一部分，可在源码级影响控制流

## Key Quotes

> "Distributed LLM agent workflows should not be monitored as if they produced a single sequential log."

> "An event that appears earlier in some log may still be unknown locally."

> "Runtime verification becomes part of the coordination language itself, rather than a post-hoc check over an execution log."

## Connections

- [[ExecutionProvenance]] — CPL 提供运行时溯源的形式化逻辑基础
- [[AgentExplainability]] — 运行时验证是过程级可解释性的保障机制
- [[agent-traces-to-trust]] — CPL 实现"runtime guardrails"方向
- [[AgentAccountability]] — 因果可见性约束增强分布式问责

## Contradictions

无已知矛盾。
