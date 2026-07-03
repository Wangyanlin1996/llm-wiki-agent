---
title: "多模态图 RAG：面向视觉富文档的长程理解"
type: source
tags: ['semantic-retrieval', 'graphrag', 'multimodal']
sources: [multimodal-graphrag]
source_file: raw/papers/multimodal-graphrag.pdf
last_updated: 2026-07-02
arxiv_id: "2606.28780"
authors: ["Yi-Cheng Wang", "Chu-Song Chen"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要

多模态大语言模型（MLLM）广泛应用于视觉文档理解，但长文档理解受限于上下文窗口。近期 MMRAG 通过检索相关页面缓解此问题，却难以处理需要文档级整体理解的问题。知识图谱（KG）能提供文档全局知识摘要，但现有 LLM 基于 KG 构造方法仅处理语言模态，视觉富文档的多模态知识图（MMKG）自动构造基本未被探索。本文提出 **KG4VD**——一种零样本的视觉富文档 MMKG 构造与使用方法：以页面级提取保留视觉与布局上下文，用自适应提取-反思循环应对页面间信息密度不均（稀疏标题页与密集表格页不应同等预算），并将提取的实体/关系锚定到具体页面区域以支持验证。检索时先以页面图像为入口点，再用个性化 PageRank（PPR）在文档级 MMKG 上查询自适应扩展。此外引入 **DLVQA** 基准，为文档级 VQA 提供参考摘要和支持事实以支持忠实性/完整性/简洁性的地面真值评估。在多跳 QA/VQA 基准和 DLVQA 上超越 MMRAG 与图方法基线。

## 关键贡献

- **KG4VD 零样本 MMKG 构造**：自适应提取-反思循环应对页面信息密度不均，布局组件锚定（Set-of-Marks 策略）使图元素可验证，页面图连接为文档级 MMKG 支持跨页推理
- **DLVQA 文档级 VQA 基准**：提供参考摘要与支持事实，将评估从 LLM-as-a-judge 的间接指标（全面性/多样性）提升到事实正确性的地面真值评估
- **页面锚定 + PPR 检索**：先检索相关页面图像为入口点，再在 MMKG 上做查询自适应个性化 PageRank 扩展，避免直接全图检索的噪声

## 关键引用

> "Automatically constructing MMKGs for visually rich documents introduces challenges beyond text-only graph construction. ... grounding extracted entities and relations to concrete page regions is crucial for verification."

## 关联

- [[GraphRAG]] — 本文是该概念的多模态扩展，将图增强检索从纯文本推进到视觉富文档
- [[RetrievalAugmentedGeneration]] — 解决 MLLM 上下文窗口限制下的长文档理解问题，是 MMRAG 的演进

## 矛盾

无已知矛盾。
