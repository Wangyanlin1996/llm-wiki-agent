---
title: "扩展稠密检索：LLM 标注训练数据的结构化挖掘与渐进课程"
type: source
tags: ['semantic-retrieval', 'dense-retrieval']
sources: [scaling-dense-retrieval]
source_file: raw/papers/scaling-dense-retrieval.pdf
last_updated: 2026-07-02
arxiv_id: "2606.23911"
authors: ["Md Omar Faruk Rokon", "Shasvat Desai", "Jhalak Nilesh Acharya"]
year: 2026
venue: "SIGIR 2026 E-Commerce Workshop"
citation_count: pending
---

## 概要
解决电商赞助搜索中稠密检索训练数据获取难题。利用异构检索系统的分歧作为结构化训练信号：全部系统一致的 easy positives、仅词法系统找到的 hard positives、恰好欺骗一个系统的 hard negatives。三模型级联标注达 89.1% 人工一致率，240M+ 训练样本五级难度渐进课程。Walmart 生产 A/B 测试：+5.1% NDCG@10、+2.80% 广告支出、+1.4% CTR。

## 关键贡献
- 异构检索系统分歧是天然结构化训练信号
- LLM 三模型级联标注达 89.1% 人工一致率
- 生产 A/B 测试验证：+5.1% NDCG@10，尴尬检索 8.7%→3.5%

## 关联
- [[DenseRetrieval]] — 关联描述
- [[RetrievalAugmentedGeneration]] — 关联描述

## 矛盾
- (暂无)
