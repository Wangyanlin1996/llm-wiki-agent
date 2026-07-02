---
title: "LLM2Vec-Gen：从大语言模型生成嵌入"
type: source
tags: ['semantic-retrieval', 'embedding-models']
sources: [llm2vec-gen]
source_file: raw/papers/llm2vec-gen.pdf
last_updated: 2026-07-02
arxiv_id: "2603.10913"
authors: ["Parishad BehnamGhader", "Vaibhav Adlakha", "Fabian David Schmidt", "Nicolas Chapados", "Marius Mosbach", "Siva Reddy"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要
提出自监督替代方案：不通过对比学习映射到新空间，而是在 LLM 输出空间直接生成嵌入。训练特殊 token 压缩 LLM 自身响应为固定长度嵌入，由无监督嵌入教师和重构目标指导。LLM 主干保持冻结，仅需无标注 query。MTEB 提升 8.8%。嵌入保留 LLM 响应空间语义，继承安全对齐（有害内容检索 -22.6%）和推理能力（推理密集检索 +35.6%），且可解码回文本实现可解释。

## 关键贡献
- 在 LLM 输出空间直接生成嵌入而非映射到新空间
- 冻结 LLM 主干，仅需无标注 query
- 继承安全对齐和推理能力，可解码可解释

## 关联
- [[EmbeddingModels]] — 关联描述
- [[DenseRetrieval]] — 关联描述

## 矛盾
- (暂无)
