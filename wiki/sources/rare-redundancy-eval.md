---
title: "RARE：高相似语料的冗余感知检索评估框架"
type: source
tags: ['semantic-retrieval', 'evaluation']
sources: [rare-redundancy-eval]
source_file: raw/papers/rare-redundancy-eval.pdf
last_updated: 2026-07-02
arxiv_id: "2604.19047"
authors: ["Hanjun Cho", "Jay-Yoon Lee"]
year: 2026
venue: "ACL 2026"
citation_count: pending
---

## 概要
解决高冗余语料（金融报告、法律条文、专利）评估失效问题。将文档分解为原子事实实现精确冗余追踪，CRRF 分别评分标准并按排名融合决策提升 LLM 数据生成可靠性。应用于金融/法律/专利语料，引入 RedQA：强检索器从 4-hop General-Wiki 66.4% PerfRecall@10 降至 4-hop 5.0-27.9%，揭示当前基准无法捕获的鲁棒性缺口。

## 关键贡献
- 高冗余语料导致检索评估失效
- 原子事实分解+CRRF 评分融合
- 强检索器在高相似语料上 PerfRecall 从 66.4% 降至 5-27.9%

## 关联
- [[RetrievalEvaluation]] — 关联描述
- [[RetrievalAugmentedGeneration]] — 关联描述

## 矛盾
- (暂无)
