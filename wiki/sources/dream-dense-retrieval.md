---
title: "DREAM：基于自回归建模的稠密检索嵌入"
type: source
tags: ['semantic-retrieval', 'dense-retrieval']
sources: [dream-dense-retrieval]
source_file: raw/papers/dream-dense-retrieval.pdf
last_updated: 2026-07-02
arxiv_id: "2606.24667"
authors: ["Yixuan Tang", "Yi Yang"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要
DREAM 探索是否可以用 LLM 的自回归 next-token prediction 目标为稠密检索提供监督。核心思路：如果文档包含与 query 相关的信息，条件化于该文档应使 LLM 更容易预测目标输出。DREAM 将检索器生成的 query-document 相似度分数注入冻结 LLM 的注意力头，通过注意力机制为检索器训练提供梯度。在 BEIR 和 RTEB 基准上，0.5B-3B 参数规模均超越基线。

## 关键贡献
- 自回归建模可为稠密检索提供无标注监督
- 检索器相似度分数注入 LLM 注意力头实现梯度回传
- BEIR+RTEB 跨尺度一致提升

## 关联
- [[DenseRetrieval]] — 关联描述
- [[RetrievalAugmentedGeneration]] — 关联描述

## 矛盾
- (暂无)
