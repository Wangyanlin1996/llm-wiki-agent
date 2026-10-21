---
title: "DelTA：基于多级记忆的在线文档级翻译智能体"
type: source
tags: [multi-agent-long-context]
sources: [delta-translation-agent]
source_file: raw/papers/delta-translation-agent.pdf
last_updated: 2026-07-24
arxiv_id: "2410.08143"
authors: ["Yutong Wang", "Jiali Zeng", "Xuebo Liu", "Derek F. Wong", "Fandong Meng", "Jie Zhou", "Min Zhang"]
year: 2024
venue: "International Conference on Learning Representations"
citation_count: 29
doi: "10.48550/arXiv.2410.08143"
---

## 概要
DelTA 是一个文档级翻译 agent，采用多级记忆结构存储不同粒度和跨度的信息：Proper Noun Records、Bilingual Summary、Long-Term Memory 和 Short-Term Memory，由辅助 LLM 组件持续检索和更新。采用逐句翻译策略确保无遗漏。在翻译一致性和质量上显著超越强基线，一致性分数提升达 4.58 个百分点。发表于 ICLR 2025。

## 关键贡献
- 四级记忆结构：Proper Noun Records / Bilingual Summary / LTM / STM
- 逐句翻译策略 + 辅助 LLM 组件持续检索更新
- 一致性 +4.58pp，COMET +3.16，代词和上下文相关翻译准确率提升

## 关键引用
> "DelTA features a multi-level memory structure that stores information across various granularities and spans, including Proper Noun Records, Bilingual Summary, Long-Term Memory, and Short-Term Memory."

## 关联
- [[MultiAgentLongContext]] — 多级记忆处理文档级长上下文
- [[MultiLevelMemory]] — 多级记忆结构
- [[DocumentLevelProcessing]] — 文档级处理范式

## 矛盾
- (暂无)
