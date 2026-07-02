---
title: "TeleEmbedBench：电信 RAG 多语料嵌入基准"
type: source
tags: ['semantic-retrieval', 'embedding-models', 'telecom']
sources: [teleembedbench]
source_file: raw/papers/teleembedbench.pdf
last_updated: 2026-07-02
arxiv_id: "2604.17778"
authors: ["Pranshav Gajjar", "Vijay K Shah"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要
首个电信领域大规模多语料嵌入基准，覆盖 O-RAN Alliance 规范、3GPP 发布文档和 srsRAN 开源代码三语料，9,000 question-chunk pair，三种 chunk 大小（512/1024/2048 token）。自动化管线：一个 LLM 从文本块生成 query，另一个 LLM 严格标准验证。评测 8 个嵌入模型，发现 LLM-based embedder（Qwen3、EmbeddingGemma）在检索准确率和跨域干扰鲁棒性上显著优于传统 sentence-transformer。还引入 TeleEmbedBench-Clean 评测噪声查询鲁棒性。

## 关键贡献
- 首个电信嵌入基准：O-RAN+3GPP+srsRAN
- LLM embedder 显著优于 sentence-transformer
- 领域特定任务指令对源代码有益但对规范有害

## 关联
- [[EmbeddingModels]] — 关联描述
- [[RetrievalAugmentedGeneration]] — 关联描述
- [[IntentDrivenMnS]] — 关联描述

## 矛盾
- (暂无)
