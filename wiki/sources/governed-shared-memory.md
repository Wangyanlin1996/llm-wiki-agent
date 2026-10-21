---
title: "多智能体 LLM 系统的治理共享记忆"
type: source
tags: [multi-agent-long-context]
sources: [governed-shared-memory]
source_file: raw/papers/governed-shared-memory.pdf
last_updated: 2026-07-24
arxiv_id: "2606.24535"
authors: ["Yanki Margalit", "Nurit Cohen-Inger", "Erni Avram", "Ran Taig", "Oded Margalit"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
本文形式化了 fleet-memory 问题，识别了四种基础失效模式：未授权泄漏、陈旧传播、矛盾持续和溯源崩溃。定义了显式系统级原语：scoped retrieval、temporal supersession、provenance tracking 和 policy-governed memory propagation。这些原语在 MemClaw 生产级多租户记忆服务中实现，并通过 ArgusFleet 评估。关键发现：长上下文检索本身不足以支撑生产级多智能体记忆，治理共享记忆需要显式系统级抽象。

## 关键贡献
- 形式化 fleet-memory 问题 + 四种失效模式（泄漏/陈旧/矛盾/溯源）
- 四个系统级原语：scoped retrieval / temporal supersession / provenance tracking / policy-governed propagation
- 生产级 MemClaw 实现 + ArgusFleet 评估，100% depth-four 溯源链重建

## 关键引用
> "Long-context retrieval alone is insufficient for production multi-agent memory. Governed shared memory demands explicit systems-level abstractions."

## 关联
- [[ShardMemo]] — ShardMemo 关注分片路由，本文关注治理原语
- [[MultiAgentMemory]] — 多智能体记忆管理的系统级视角
- [[FleetMemoryProblem]] — fleet-memory 问题形式化

## 矛盾
- (暂无)
