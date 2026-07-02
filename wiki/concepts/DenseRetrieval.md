---
title: "稠密检索（Dense Retrieval）"
type: concept
tags: ['semantic-retrieval', 'dense-retrieval']
sources: ["dream-dense-retrieval", "scaling-dense-retrieval", "coder-constraint-retrieval", "armor-telecom-retriever"]
last_updated: 2026-07-02
---

稠密检索使用神经网络编码器将 query 和文档映射到稠密向量空间，通过相似度检索替代传统词法匹配（BM25）。核心范式从对比学习训练的双编码器发展到自回归建模（[[dream-dense-retrieval]]）和约束感知检索（[[coder-constraint-retrieval]]）。训练数据获取从人工标注演进到 LLM 标注的结构化挖掘（[[scaling-dense-retrieval]]）。在电信领域，查询侧检索器自适应优化（[[armor-telecom-retriever]]）成为低资源场景的关键路径。相关论文：[[dream-dense-retrieval]]、[[scaling-dense-retrieval]]、[[coder-constraint-retrieval]]、[[armor-telecom-retriever]]
