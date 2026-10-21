---
title: "SLEUTH：解决证据稀疏性的长文档理解智能体上下文工程"
type: source
tags: [multi-agent-long-context]
sources: [sleuth-long-doc]
source_file: raw/papers/sleuth-long-doc.pdf
last_updated: 2026-07-24
arxiv_id: "2511.22850"
authors: ["Keliang Liu", "Zizhi Chen", "Mingcheng Li", "Jingqun Tang", "Dingkang Yang", "Lihua Zhang"]
year: 2025
venue: "arXiv.org"
citation_count: 13
doi: "10.48550/arXiv.2511.22850"
---

## 概要
SLEUTH 是一个多智能体框架，用于解决长文档理解中证据稀疏性的问题。它编排一个 retriever 和四个协作 agent，通过粗到细的过程工作：识别检索页面中的关键文本和视觉线索，过滤显著视觉证据（如表格和图表），分析查询以制定推理策略，最终合成精炼的、证据密集的多模态上下文生成最终预测。SLEUTH 是模型无关且可扩展的，与先进 VLM backbone 配合时在多个长文档基准上持续提升性能并达到 SOTA。

## 关键贡献
- Retriever + 4 协作 agent 的粗到细多智能体框架
- 解决长文档中多模态证据稀疏性：关键线索识别 + 视觉证据过滤 + 推理策略制定
- 模型无关、可扩展，在多个长文档基准上达到 SOTA

## 关键引用
> "SLEUTH orchestrates a retriever and four collaborative agents in a coarse to fine process, ultimately synthesizes a distilled, evidence dense multimodal context to generate the final prediction."

## 关联
- [[MultiAgentLongContext]] — 多智能体长文档理解框架
- [[AgenticContextEngineering]] — 智能体上下文工程范式
- [[MultimodalLongDocument]] — 多模态长文档理解

## 矛盾
- (暂无)
