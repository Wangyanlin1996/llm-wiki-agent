---
title: "CoDeR：超越语义相似度的局部约束兼容检索"
type: source
tags: ['semantic-retrieval', 'dense-retrieval']
sources: [coder-constraint-retrieval]
source_file: raw/papers/coder-constraint-retrieval.pdf
last_updated: 2026-07-02
arxiv_id: "2606.13204"
authors: ["Xingkun Yin", "Xuebin Tang", "Hongyang Du"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要
CoDeR 研究约束敏感查询的检索失败：文档在主题上接近 query 但支持相反的约束方向（如应排除的属性被满足）。提出将主题相关性约束兼容性分离：保留标准主题编码器覆盖候选，增加双编码器兼容性评分器，用词法极性监督训练。推理时无需外部 LLM 调用。在反义、否定、排除三个诊断集上，V@2 分别降低 20.59、23.53、5.77 分。

## 关键贡献
- 语义相似度作为相关性代理在约束敏感查询上失败
- 主题相关性与约束兼容性应分离建模
- 推理时无需 LLM 调用，V@2 降低 20.59-23.53 分

## 关联
- [[DenseRetrieval]] — 关联描述
- [[RetrievalEvaluation]] — 关联描述

## 矛盾
- (暂无)
