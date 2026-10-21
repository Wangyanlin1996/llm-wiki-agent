---
title: "多智能体上下文管理（Multi-Agent Context Management）"
type: concept
tags: [multi-agent-long-context]
sources: [ama-adaptive-memory, shardmemo, governed-shared-memory, ensemble-qsp, agentic-context-management]
last_updated: 2026-07-24
---

多智能体上下文管理关注如何在多智能体系统中有效管理、共享和治理上下文信息。核心挑战包括记忆粒度对齐（AMA 的多粒度记忆）、分片路由效率（ShardMemo 的 masked MoE 路由）、共享记忆治理（Governed Shared Memory 的 scoped retrieval/provenance tracking）、以及上下文有界性（Ensemble QSP 的三层层次记忆保持中位 301 tokens）。生产级系统需要将上下文管理视为生命周期和架构问题而非单纯推理问题。相关论文：[[ama-adaptive-memory]], [[shardmemo]], [[governed-shared-memory]], [[ensemble-qsp]], [[agentic-context-management]]
