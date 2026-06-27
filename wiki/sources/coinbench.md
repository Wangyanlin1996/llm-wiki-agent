---
title: COINBench：从个体到集体意图理解
type: source
tags:
- intent-understanding
sources:
- coinbench
source_file: raw/papers/coinbench.pdf
last_updated: 2026-06-08
arxiv_id: '2603.21329'
authors:
- Xiaozhe Li
- Tianyi Lyu
- Siyi Yang
- Yizhao Yang
- Yuxi Gong
- Jinxuan Huang
- Ligao Zhang
- Zhuoyi Huang
- Qingwen Liu
year: 2026
---
## 概要
COINBench 首次将意图理解从个体指令跟随扩展到集体意图提取——从多源公开讨论中提取共识、解决矛盾、推断潜在趋势。提出 COIN-TREE 层次认知结构和 COIN-RAG 检索增强验证。20 个 SOTA LLM 评测发现模型可处理表层聚合但难以达到深度意图合成所需的因果推理深度。

## 关键贡献
- 集体意图概念：从个体意图到群体共识/矛盾/趋势推断
- COIN-TREE：层次认知结构化（显式场景→深度因果推理）
- COIN-RAG：检索增强验证确保专家级分析精度

## 关键引用
> "COIN-BENCH establishes a new standard for advancing LLMs from passive instruction followers to expert-level analytical agents" — 从跟随到分析

## 关联
- [[IntentUnderstanding]] — COINBench 开辟全新子方向：集体意图而非个体意图
- [[IntentSignalTheory]] — 集体意图的 I* 是群体共识而非个体信念，信息损失机制不同
- [[SemanticIntentSimilarity]] — COIN-TREE 的层次结构与 SIS 指标的本体深度概念相似

## 矛盾
- COINBench 发现模型可表层聚合但深度因果推理差——与 [[NOEM³A]] 发现的"3B+Ontology→85%"形成对比，说明本体注入可能帮助深度推理