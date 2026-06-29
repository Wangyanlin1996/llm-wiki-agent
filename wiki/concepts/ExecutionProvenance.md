---
title: "执行溯源与证据追踪（Execution Provenance & Evidence Tracing）"
type: concept
tags: [agent-explainability, provenance, evidence-tracing, accountability]
sources: [agent-traces-to-trust, hansel-web-agent-verification, causal-past-logic-runtime-verification]
last_updated: 2026-06-29
---

执行溯源（execution provenance）指将 agent 执行表示为类型化图（typed graph），记录每个执行单元的来源、依赖和输出；证据追踪（evidence tracing）是该图在"证据-支撑"关系上的投影，回答"哪个证据支撑了哪条声明"。[[agent-traces-to-trust]] 综述将两者统一为过程级问责（process-level accountability）的基础，连接检索接地、声明支撑、工具使用安全、记忆谱系、可观测性、调试、审计与恢复。

**三种实现路径**：
- **交互式证据导航** — [[hansel-web-agent-verification]]（HANSEL）将验证从被动阅读重构为交互活动，提取证据页面为可导航视图，不可追溯时显式标记缺口。83.7% precision / 88.8% recall。
- **运行时因果逻辑验证** — [[causal-past-logic-runtime-verification]]（CPL）将运行时验证嵌入协调语言本身，用向量时钟监控器证明本地监控值与指称语义一致，而非事后检查日志。
- **分类法与方法论** — [[agent-traces-to-trust]] 提出覆盖 trace sources、provenance relations、tracing granularity/timing、trust functions 的完整分类法。

核心洞察：**最终答案准确率无法解释 agent 输出如何产生**——过程级溯源是可信 agent 的必要条件。相关概念：[[AgentExplainability]]、[[AgentAccountability]]、[[ExplainablePlanning]]。
