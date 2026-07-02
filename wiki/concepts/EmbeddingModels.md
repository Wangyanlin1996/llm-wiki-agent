---
title: "嵌入模型（Embedding Models）"
type: concept
tags: ['semantic-retrieval', 'embedding-models']
sources: ["teleembedbench", "llm2vec-gen", "promptembedder", "hteb-harder-embedding-bench"]
last_updated: 2026-07-02
---

嵌入模型为检索系统提供向量表示。范式从对比学习训练双编码器演进到：(1) 生成式嵌入——在 LLM 输出空间直接生成嵌入（[[llm2vec-gen]]）；(2) 双 LLM 软提示——解耦嵌入知识与主干权重（[[promptembedder]]）。评估从 MTEB 单分数扩展到多维度动态鲁棒性（[[hteb-harder-embedding-bench]]）。电信领域首个嵌入基准 TeleEmbedBench 揭示 LLM embedder 显著优于 sentence-transformer（[[teleembedbench]]）。相关论文：[[teleembedbench]]、[[llm2vec-gen]]、[[promptembedder]]、[[hteb-harder-embedding-bench]]
