---
title: "From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents"
type: source
tags: [agent-explainability, execution-provenance, evidence-tracing, survey]
date: 2026-06-03
source_file: raw/papers/agent-traces-to-trust.pdf
arxiv_id: "2606.04990"
authors: ["Yiqi Wang", "Jiaqi Zhang", "Taotao Cai", "Zirui Liu", "Qingqiang Sun", "Zequn Sun", "Zhangkai Wu", "Manqing Dong", "Mingkai Zhang", "Xuefei Yin", "Yanming Zhu"]
venue: arXiv preprint (survey)
citation_count: pending
---

## Summary

本综述系统梳理 LLM agent 中"执行溯源（execution provenance）"与"证据追踪（evidence tracing）"两大基础概念，将其作为过程级问责（process-level accountability）的统一框架。作者将执行溯源定义为 agent 执行的类型化图（typed graph），将证据追踪定义为其在"证据-支撑"关系上的投影。该视角将检索接地、声明支撑、工具使用安全、记忆谱系、可观测性、调试、审计与恢复统一在一个框架内。

## Key Claims

- **最终答案准确率无法解释 agent 输出如何产生**：哪个证据支撑了哪条声明、工具调用是否合理、记忆如何影响后续决策、失败源于何处——这些问题需要过程级溯源而非结果级评测
- **执行溯源 = 类型化图**；**证据追踪 = 图在证据-支撑关系上的投影**——两个概念区分使"谁支撑了谁"可被显式查询
- 综述提出分类法覆盖：trace sources、evidence/execution units、provenance relations、tracing granularity/timing、representation forms、trust functions
- 方向包括：provenance representation、evidence attribution、tool-use provenance、runtime guardrails、provenance-bearing memory、observability、failure diagnosis
- 开放挑战：构建 provenance-aware、auditable、recoverable 的 agent 系统

## Key Quotes

> "Final-answer accuracy alone cannot explain how an output was produced, which evidence supported each claim, whether tool calls were justified, how memory influenced later decisions, or where failures originated."

> "We define execution provenance as the typed graph of an agent execution and evidence tracing as its projection onto evidence-support relations."

## Connections

- [[ExecutionProvenance]] — 本综述是该概念的最系统化定义
- [[AgentExplainability]] — 过程级问责是 agent 可解释性的核心维度
- [[LLMAutonomousAgent]] — 自主 agent 的规划/工具/记忆全链条均需溯源
- [[AgentAccountability]] — 溯源是问责的前提
- [[hansel-web-agent-verification]] — HANSEL 是交互式证据追踪的具体实现
- [[causal-past-logic-runtime-verification]] — CPL 是 runtime guardrails 的形式化实现

## Contradictions

无已知矛盾。
