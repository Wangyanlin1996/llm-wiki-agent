---
title: "PromptEmbedder：双 LLM 软提示的高效可迁移文本嵌入"
type: source
tags: ['semantic-retrieval', 'embedding-models']
sources: [promptembedder]
source_file: raw/papers/promptembedder.pdf
last_updated: 2026-07-02
arxiv_id: "2605.28066"
authors: ["Yu-Che Tsai", "Kuan-Yu Chen", "Yuan-Hao Chen", "Yu-Han Chang", "Ching-Yu Tsai", "Yu-Hsiang Chuang", "Shou-De Lin"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要
双 LLM 框架解耦嵌入知识与特定主干权重。Prompting LLM 为冻结 Embedding LLM 生成指令感知软提示，通过连续松弛的可微生成过程确保对比训练中的完整梯度流。新架构适配仅需重训轻量线性对齐矩阵。MTEB 上与 LoRA 微调性能相当，GPU 内存降低 40%，训练加速 3.7 倍。建立可扩展、架构无关的 LLM 表示学习范式。

## 关键贡献
- 双 LLM 解耦嵌入知识与主干权重
- 新架构适配仅需重训轻量线性矩阵
- GPU -40%，训练 3.7x 加速，性能不降

## 关联
- [[EmbeddingModels]] — 关联描述
- [[DenseRetrieval]] — 关联描述

## 矛盾
- (暂无)
