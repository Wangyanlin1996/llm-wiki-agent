---
title: "检索状态锁定 (Retrieval-State Lock-In)"
type: concept
tags: [ontology-graph-retrieval]
sources: [retrieval-state-lock-in, beyond-probabilistic-rag-limitations]
last_updated: 2026-08-31
---

检索状态锁定是 RAG 系统中的一种隐蔽失败模式：当 retriever 反复返回相同 degenerate retrieval state（空的或 coherent 但错误的），重复采样无法暴露错误，answer-state agreement 被误读为 confidence。核心洞察是 RAG confidence 必须分解为三个独立对象——answer-state uncertainty（采样答案变异）、evidence-state uncertainty（检索文本是否支持答案）和 retrieval-state uncertainty（图检索状态是否提供 graph support）——而传统 answer-only 方法（semantic entropy、SelfCheckGPT）在 lock-in 时 structural ceiling 上最多 recall 41-58% 错误。锁定分两种变体：absence lock-in（empty route，检索返回空）和 presence lock-in（populated but wrong-coherent neighbourhood，检索返回连贯但错误的子图）。合取审计规则（三检查全部通过才认证 low-risk）在 7.7% 覆盖率下达 91.9% precision。相关论文：[[retrieval-state-lock-in]]、[[beyond-probabilistic-rag-limitations]]。与 [[RetrievalEvaluation]]（Round 9）的统计估计方法互补——后者关注检索质量评估方法论，本概念关注检索失败的诊断和检测。
