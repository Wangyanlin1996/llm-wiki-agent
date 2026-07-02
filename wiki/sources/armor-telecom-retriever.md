---
title: "ARMOR：低资源电信问答的自适应检索器优化"
type: source
tags: ['semantic-retrieval', 'dense-retrieval', 'telecom']
sources: [armor-telecom-retriever]
source_file: raw/papers/armor-telecom-retriever.pdf
last_updated: 2026-07-02
arxiv_id: "2606.29706"
authors: ["Heshan Fernando", "Quan Xiao", "Yan Xin", "Tianyi Chen"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要
电信 QA 是 RAG 的挑战性场景：证据碎片化分布在标准、论文、百科和 Web 文档中，答案常依赖技术表格、方程和专业协议语言。ARMOR 提出查询侧检索器自适应优化替代生成器微调：联合 RAG 似然目标（优化生成效用）和 InfoNCE 对比目标（改善语义检索几何），正则化适配查询编码器向冻结基础编码器靠拢。在电信专用检索和生成 QA 基准上验证有效。

## 关键贡献
- 查询侧检索器适配优于生成器微调
- RAG 似然 + InfoNCE 联合优化
- 正则化防止查询编码器偏离基础编码器

## 关联
- [[DenseRetrieval]] — 关联描述
- [[RetrievalAugmentedGeneration]] — 关联描述
- [[IntentDrivenMnS]] — 关联描述

## 矛盾
- (暂无)
