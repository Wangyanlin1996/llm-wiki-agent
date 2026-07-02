---
title: "KbSD：Agentic 搜索中知识边界感知的自蒸馏行为校准"
type: source
tags: ['semantic-retrieval', 'agentic-retrieval']
sources: [kbsd-knowledge-boundary]
source_file: raw/papers/kbsd-knowledge-boundary.pdf
last_updated: 2026-07-02
arxiv_id: "2606.29863"
authors: ["Tao Feng", "Xinke Jiang", "Chao Wu"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要
解决 agentic search 中知识边界校准的奖励稀疏问题——何时信任参数记忆、何时依赖检索证据、何时弃答。KbSD 通过 hint 增强教师（架构相同但接收显式知识边界信号）生成校准推理示范，实现信息不对称自蒸馏。象限自适应蒸馏目标：集中整合用 reverse KL、多样拒绝用 forward KL、非对称象限用 Pareto 最优双向 KL。多基准上一致提升任务准确率和幻觉抑制。

## 关键贡献
- 知识边界校准三决策：信任记忆/依赖检索/弃答
- hint 增强教师信息不对称自蒸馏
- 象限自适应 KL：reverse/forward/bidirectional

## 关联
- [[AgenticRetrieval]] — 关联描述
- [[RetrievalAugmentedGeneration]] — 关联描述

## 矛盾
- (暂无)
