---
title: "语料感知的检索增强澄清问题生成"
type: source
tags: [memory-intent-clarification, RAG, conversational-search]
sources: [corpus-rag-clarifying]
source_file: raw/papers/corpus-rag-clarifying.pdf
last_updated: 2026-06-27
arxiv_id: "2409.18575"
authors: ["Antonios Minas Krasakis", "Andrew Yates", "Evangelos Kanoulas"]
year: 2024
venue: null
citation_count: null
doi: "10.48550/arXiv.2409.18575"
---

## 概要
本文研究用 RAG（Retrieval Augmented Language Models）生成语料感知的澄清问题。核心方法是联合建模用户查询和检索语料来端到端定位不确定性并生成澄清问题。发现现有数据集中搜索意图大多不被语料支撑，导致模型"幻觉"出不存在的意图。提出数据增强方法对齐 ground truth 澄清与检索语料，并探索推理时增强证据池相关性的技术。

## 关键贡献
- RAG 联合建模 query+corpus 端到端定位不确定性——检索语料作为"记忆"增强澄清
- 发现现有数据集的意图-语料不对齐问题，并提出数据增强解决方案
- 增加证据文档数量可拓宽澄清问题的广度

## 关键引用
> "We demonstrate the effectiveness of RAG in this process, emphasising their ability to jointly model the user query and retrieval corpus to pinpoint the uncertainty and ask for clarifications end-to-end" — RAG 作为记忆增强澄清

## 关联
- [[RetrievalAugmentedClarification]] — 与 [[rac]] 同属 RAG 增强澄清方向，本文更早提出
- [[IntentSimUncertainty]] — 检索语料定位不确定性与意图熵判断互补
- [[AgentMemory]] — 检索语料库可视为一种外部记忆，增强模糊意图理解

## 矛盾
- 发现现有澄清数据集存在系统性偏差（意图脱离语料），挑战了 prior work 的评测有效性
