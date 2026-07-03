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

通过对比学习微调 LLM 嵌入器会将输入和输出映射到新的表示空间，丢弃 LLM 的输出语义。LLM2VEC-GEN 提出一种自监督替代方案：不编码输入，而是编码 LLM 的潜在响应——直接在 LLM 输出空间生成嵌入。具体而言，向输入追加可训练的特殊 token（压缩 token），优化这些 token 的隐藏状态来压缩 LLM 自身响应为固定长度嵌入。训练由两个互补目标指导：(1) 嵌入对齐——将压缩 token 表示与无监督嵌入教师（LLM2Vec）对 LLM 响应的嵌入对齐；(2) 响应重构——冻结 LLM 以压缩 token 为软提示重构自身响应。LLM 主干全程冻结，仅需无标注 query 作为训练数据（LLM 自身生成响应，无监督教师提供对齐目标）。关键洞察：通过编码 LLM 的潜在响应而非输入，嵌入保留 LLM 响应空间的语义结构，继承安全对齐（有害内容检索降低 22.6%）和推理能力（推理密集检索提升 35.6%）。在 MTEB 上较无监督教师提升 8.8%，弥合 60% 到有监督方法的差距。嵌入还可解码回文本实现可解释。应用于 Llama-3.x、Qwen-2.5 和 Qwen-3 系列。

## 关键贡献

- **输出中心嵌入范式**：编码 LLM 潜在响应而非输入——保留 LLM 预训练获得的响应空间语义结构，而非对比学习投影到新空间
- **双目标自监督训练**：嵌入对齐（教师蒸馏）+ 响应重构（信息瓶颈）——仅训练压缩 token 和投影层，LLM 主干冻结，仅需无标注 query
- **继承安全对齐和推理能力**：嵌入保留 LLM 响应空间语义，有害内容检索降低 22.6%（AdvBench-IR），推理密集检索提升 35.6%（BRIGHT）——对比学习丢弃这些能力
- **可解码可解释嵌入**：压缩 token 可作为软提示让 LLM 重构响应——嵌入不仅是向量，还可解码回文本揭示语义内容

## 关键引用

> "Rather than encoding the input, the model should encode the LLM's potential response to that input. By keeping embeddings closer to the LLM's response space, this paradigm preserves capabilities that manifest in the model's responses."

> "LLM2VEC-GEN achieves state-of-the-art self-supervised performance on the Massive Text Embedding Benchmark (MTEB), improving by 8.8% over the unsupervised embedding teacher. Since the embeddings preserve the LLM's response-space semantics, they inherit capabilities such as safety alignment and reasoning."

## 关联

- [[EmbeddingModels]] — 本文是该概念的核心实现之一，提出输出中心嵌入范式替代输入中心对比学习
- [[DenseRetrieval]] — 嵌入模型是稠密检索的基础组件，本文的自监督训练降低对标注数据依赖
- [[promptembedder]] — 两者均为 LLM 嵌入创新：本文在输出空间生成嵌入，后者用双 LLM 软提示解耦知识与权重
- [[dream-dense-retrieval]] — 两者均利用 LLM 的生成能力为检索提供监督：DREAM 用 NTP loss 训练检索器，本文用响应蒸馏训练嵌入器
- [[hteb-harder-embedding-bench]] — 后者评估嵌入鲁棒性，本文的输出中心嵌入可能展现不同鲁棒性轮廓

## 矛盾

无已知矛盾。与输入中心对比学习范式的"编码输入 vs 编码响应"形成方法论分歧，实验表明输出中心嵌入在安全性和推理上继承 LLM 能力。
