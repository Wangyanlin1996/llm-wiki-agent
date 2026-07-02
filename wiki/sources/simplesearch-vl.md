---
title: "SimpleSearch-VL：多模态 Agentic 深度搜索的简单配方"
type: source
tags: ['semantic-retrieval', 'agentic-retrieval', 'multimodal']
sources: [simplesearch-vl]
source_file: raw/papers/simplesearch-vl.pdf
last_updated: 2026-07-02
arxiv_id: "2606.31504"
authors: ["Ming Dai", "Zhihong Lu", "Jinjie Gu", "Jiedong Zhuang", "Yefeng Liu", "Wankou Yang", "Jian Wang", "Chunhua Shen"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要
高效可靠实用的多模态 agentic 搜索框架。核心思路：改进 agent 自身的搜索-验证过程而非扩展数据/工具/辅助组件。Factorized Adaptive Rollout（FAR）提升采样效率；证据验证推理显式评估检索视觉和文本线索相关性。仅 5K 监督工具交错轨迹 + 2K RL 数据，Qwen3-VL 8B/30B-A3B 分别提升 15.8/16.0 平均分，30B-A3B 与 agentic Gemini-3-Pro 竞争力相当。

## 关键贡献
- 改进搜索-验证过程而非扩展数据/工具
- FAR 提升采样效率+证据验证推理
- 5K SFT + 2K RL → +15.8/16.0 分，匹敌 Gemini-3-Pro

## 关联
- [[AgenticRetrieval]] — 关联描述
- [[RetrievalAugmentedGeneration]] — 关联描述

## 矛盾
- (暂无)
