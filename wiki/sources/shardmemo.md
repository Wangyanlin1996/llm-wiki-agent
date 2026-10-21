---
title: "ShardMemo：基于 Masked MoE 路由的分片智能体记忆"
type: source
tags: [multi-agent-long-context]
sources: [shardmemo]
source_file: raw/papers/shardmemo.pdf
last_updated: 2026-07-24
arxiv_id: "2601.21545"
authors: ["Yang Zhao", "Chengxiao Dai", "Yue Xiu", "M. Kou", "Yuliang Zheng", "D. Niyato"]
year: 2026
venue: "arXiv.org"
citation_count: 1
doi: "10.48550/arXiv.2601.21545"
---

## 概要
ShardMemo 针对多智能体并发执行时集中索引和启发式分区成为瓶颈的问题，提出预算化分层记忆服务。Tier A 为 per-agent 工作状态，Tier B 为带 shard-local ANN 索引的分片证据，Tier C 为版本化技能库。Tier B 将 shard 探测建模为 masked MoE 路由，在路由或 ANN 搜索前通过结构化资格约束屏蔽不合格分片。在 LoCoMo 上比最强基线 GAM 提升 5.11-6.82 F1，在长上下文 HotpotQA 上达到 63.41/61.88/57.95 F1（56K/224K/448K tokens）。

## 关键贡献
- 三层分片记忆架构：Tier A (per-agent) / Tier B (sharded evidence) / Tier C (skill library)
- Masked MoE 路由：scope-before-routing 屏蔽不合格分片 + 成本感知门控
- LoCoMo +5.11~6.82 F1，HotpotQA 56K-448K tokens 稳定表现

## 关键引用
> "ShardMemo, a budgeted tiered memory service with Tier A per-agent working state, Tier B sharded evidence with shard-local approximate nearest neighbor (ANN) indexes, and Tier C, a versioned skill library."

## 关联
- [[AMAAdaptiveMemory]] — AMA 关注多粒度，ShardMemo 关注分片路由
- [[GovernedSharedMemory]] — 同为多智能体共享记忆管理
- [[MoERoutingMemory]] — MoE 路由用于记忆分片

## 矛盾
- (暂无)
