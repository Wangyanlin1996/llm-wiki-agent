---
title: "检索增强生成（Retrieval-Augmented Generation）"
type: concept
tags: ['semantic-retrieval', 'rag-architecture']
sources: ["rag-comprehensive-survey", "beyond-parameters-survey", "rag-security-privacy", "rag-evaluation-survey", "telco-orag", "bm25-corrective-rag", "reasoning-agentic-rag-survey", "r2-searcher"]
last_updated: 2026-07-02
---

检索增强生成（RAG）核心范式：retrieve → augment → generate。分类法将架构分为 retriever-centric、generator-centric、hybrid 和 robustness-oriented 四类（[[rag-comprehensive-survey]]）。演进路径 ICL→RAG→GraphRAG→CausalRAG（[[beyond-parameters-survey]]）。安全威胁覆盖检索/上下文构建/生成三阶段（[[rag-security-privacy]]）。评估方法需桥接传统指标与 LLM 驱动方法（[[rag-evaluation-survey]]）。在电信场景，混合检索+神经路由使开源 LLM 达 GPT-4 水平（[[telco-orag]]）。向 Agentic RAG 演进：System 1 预定义推理 vs System 2 自主编排（[[reasoning-agentic-rag-survey]]）。相关论文：[[rag-comprehensive-survey]]、[[beyond-parameters-survey]]、[[telco-orag]]、[[reasoning-agentic-rag-survey]]
