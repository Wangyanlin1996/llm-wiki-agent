---
title: "双曲本体嵌入检索 (Hyperbolic Ontology Embedding Retrieval)"
type: concept
tags: [ontology-graph-retrieval]
sources: [hyem-hyperbolic-ontology-retrieval]
last_updated: 2026-08-17
---

双曲本体嵌入检索是指将本体的 is-a 层次树嵌入双曲空间（Poincare ball/hyperboloid），利用双曲空间的指数体积增长特性天然适配层次结构——层次越深，双曲距离越能区分。相比欧式嵌入，双曲嵌入能更好保持本体层次关系，提升层次感知检索精度。

关键挑战是：(1) 缺乏原生双曲向量数据库支持；(2) 实体中心查询（不涉及层次）上双曲嵌入可能劣于欧式。[[hyem-hyperbolic-ontology-retrieval]] 提出 HyEm 框架用欧式 ANN 索引近似双曲距离绕过向量库限制，并用查询自适应机制在双曲/欧式间切换。与 [[EmbeddingModels]] 的关系：双曲嵌入是欧式嵌入的层次感知变体；与 [[qime-ontology-embeddings]] 互补：QIME 将本体维度映射为临床 yes/no 问题，HyEm 将层次结构编码为双曲距离。
