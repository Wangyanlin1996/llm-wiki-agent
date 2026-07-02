---
title: "Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations（LLM 对话的线性时间运行时验证器）"
type: source
tags: [agent-explainability, runtime-verification, dependency-graph, closed-loop-verification]
sources: [grounded-continuation]
source_file: raw/papers/grounded-continuation.pdf
last_updated: 2026-07-02
arxiv_id: "2605.14175"
authors: ["Qisong He", "Yi Dong", "Xiaowei Huang"]
year: 2026
venue: "arXiv preprint"
citation_count: pending
---

## 概要

在长对话中，LLM 可产出听起来合理但基于已被对话放弃的前提的下一语句。针对已部署 agent 的上下文操纵攻击正是利用此缺口。本文以一个维护显式**依赖图**的运行时验证器闭合此缺口：LLM 将每轮分类为来自四种形式主义（动态认知逻辑、溯因推理、意识逻辑、论证）的 8 种更新操作之一，符号引擎记录哪些声明依赖哪些证据。检查续接是否被支撑归约为图遍历；撤回通过同一图传播以标记失去支撑的结论，每轮成本线性且有形式化无冲突保证。在 LongMemEval-KU 上达 89.7% 准确率，撤回检查在微秒级而历史重放随对话长度线性增长。

## 关键贡献

- **线性时间运行时验证**：依赖图遍历检查续接支撑，每轮成本线性——适用于 AgentLoop 实时验证层
- **四种形式主义的 8 种更新操作**：动态认知逻辑+溯因+意识+论证统一为声明-证据依赖——超越单一逻辑的验证
- **soundness-faithfulness 分解**：结构检查构造性可靠，逐部署 LLM 提取忠实度是可测经验问题——为闭环验证提供形式化保证

## 关键引用

> "Checking whether a continuation is supported reduces to a graph walk; retraction propagates through the same graph to flag exactly the conclusions that lose support, with linear per-turn cost and a formal conflict-free guarantee."

## 关联

- [[VerificationCoEvolution]] — 本文是运行时验证的代表实现
- [[causal-past-logic-runtime-verification]] — 与 CPL 运行时验证互补：CPL 用因果时序逻辑，本文用依赖图+四形式主义
- [[ExecutionProvenance]] — 依赖图是执行溯源的声明-证据投影
- [[AgentExplainability]] — 运行时验证是过程级解释的形式化保障
- [[IntentSignalTheory]] — 上下文操纵攻击利用的"前提放弃"是 I*→P 信息损失的攻击实例

## 矛盾

无已知矛盾。
