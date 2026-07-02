---
title: "HTEB：超越一维静态鲁棒性的更难文本嵌入基准"
type: source
tags: ['semantic-retrieval', 'embedding-models', 'evaluation']
sources: [hteb-harder-embedding-bench]
source_file: raw/papers/hteb-harder-embedding-bench.pdf
last_updated: 2026-07-02
arxiv_id: "2605.28190"
authors: ["Manuel Frank", "Haithem Afli"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要
挑战 MTEB 单分数评估的静态标量鲁棒性假设，提出多维度动态评估框架。三个可解释轴：词法/风格、长度、语言，通过 LLM 在评估时随机变换输入。16 开源嵌入模型/32 数据集/42 语言/4,800 人类评分。发现：(1) 模型展现特定且部分解耦的鲁棒性轮廓；(2) 规模提升绝对分数但不缩小原始与变换评估差距；(3) 英文数据集比多语言更敏感。

## 关键贡献
- 嵌入鲁棒性是多维动态属性而非静态标量
- 三轴评估：词法/风格、长度、语言
- 规模不缩小原始与变换评估差距

## 关联
- [[EmbeddingModels]] — 关联描述
- [[RetrievalEvaluation]] — 关联描述

## 矛盾
- (暂无)
