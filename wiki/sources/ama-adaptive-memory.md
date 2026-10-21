---
title: "AMA：多智能体协作的自适应记忆"
type: source
tags: [multi-agent-long-context]
sources: [ama-adaptive-memory]
source_file: raw/papers/ama-adaptive-memory.pdf
last_updated: 2026-07-24
arxiv_id: "2601.20352"
authors: ["Weiquan Huang", "Zixuan Wang", "Hehai Lin", "Sudong Wang", "Bo Xu", "Qian Li", "Beier Zhu", "Linyi Yang", et al.]
year: 2026
venue: "Annual Meeting of the Association for Computational Linguistics"
citation_count: 4
doi: "10.48550/arXiv.2601.20352"
---

## 概要
AMA 利用协调的 agent 群体管理多粒度记忆。采用层级记忆设计，动态将检索粒度与任务复杂度对齐。Constructor 和 Retriever 联合实现多粒度记忆构建和自适应查询路由；Judge 验证检索内容的相关性和一致性，证据不足时触发迭代检索或检测到逻辑冲突时调用 Refresher；Refresher 执行针对性更新或移除过时条目。在长上下文基准上显著超越 SOTA 基线，同时比全上下文方法减少约 80% token 消耗。

## 关键贡献
- 多智能体协作管理多粒度记忆：Constructor/Retriever/Judge/Refresher
- 层级记忆设计动态对齐检索粒度与任务复杂度
- 比全上下文方法减少~80% token，保持检索精度和长期记忆一致性

## 关键引用
> "AMA employs a hierarchical memory design that dynamically aligns retrieval granularity with task complexity."

## 关联
- [[MemAgentLongContext]] — MemAgent 用 RL 训练单 agent，AMA 用多 agent 协作
- [[ShardMemo]] — ShardMemo 从分片角度解决记忆管理
- [[AdaptiveMemoryGranularity]] — 自适应记忆粒度

## 矛盾
- (暂无)
