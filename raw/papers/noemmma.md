---
title: "NOEM³A: A Neuro-Symbolic Ontology-Enhanced Method for Multi-Intent Understanding in Mobile Agents"
type: paper
tags: [neuro-symbolic, ontology, multi-intent, mobile-agent, intent-disambiguation, NLU]
authors: [Ioannis Tzachristas, Aifen Sui]
year: 2025
venue: null
citation_count: null
arxiv_id: "2511.19780"
doi: "10.48550/arXiv.2511.19780"
pdf_url: "https://arxiv.org/pdf/2511.19780"
sub_area: intent-understanding
---

## 概要
提出神经符号本体增强的多意图理解框架 NOEM³A，将结构化意图 Ontology 注入紧凑语言模型的输入与输出表示中，3B Llama 模型达到 GPT-4 的 85% 准确率（vs 90%），并提出基于层次 Ontology 深度的 Semantic Intent Similarity (SIS) 评测指标。

## 核心贡献
- 设计 Retrieval-Augmented Prompting + Logit Biasing + 可选分类头的三层注入策略，将符号意图结构嵌入 LLM 的输入与输出
- 提出 Semantic Intent Similarity (SIS) 评测指标，基于层次 Ontology 深度捕捉语义邻近度，克服词表匹配的局限性
- 在 MultiWOZ 2.3 的歧义/高难度对话子集上验证 3B Llama + Ontology 增强达到 GPT-4 水平（85% vs 90%），能耗与内存仅为极小比例