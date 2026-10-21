---
title: "多智能体 RAG（Multi-Agent RAG）"
type: concept
tags: [multi-agent-long-context]
sources: [spd-rag, sleuth-long-doc, finlongdoc-agent]
last_updated: 2026-07-24
---

多智能体 RAG 将检索增强生成扩展到多智能体架构，通过文档级专业化或粗到细多智能体编排解决跨文档 QA 和长文档理解问题。SPD-RAG 采用每文档一 agent 的文档级专业化 + coordinator 中心化融合，支持递归 map-reduce 处理大规模语料。SLEUTH 编排 retriever + 4 协作 agent 进行粗到细多模态证据过滤和推理策略制定。FinLongDocAgent 在金融长文档中通过多智能体多轮 RAG 迭代检索、中间计算和跨轮验证。核心优势是在保持聚焦检索的同时实现跨文档证据综合。相关论文：[[spd-rag]], [[sleuth-long-doc]], [[finlongdoc-agent]]
