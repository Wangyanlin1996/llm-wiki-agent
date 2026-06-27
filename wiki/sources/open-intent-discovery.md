---
title: Open Intent Discovery through Unsupervised Semantic Clustering and Dependency
  Parsing
type: source
tags:
- intent-discovery
- unsupervised
- semantic-clustering
- dependency-parsing
- L1-unknown-intent
date: 2021-04-26
source_file: raw/papers/open-intent-discovery.pdf
last_updated: 2026-06-23
arxiv_id: '2104.12114'
authors:
- Pengfei Liu
- Youzhang Ning
- King Keung Wu
year: 2021
venue: EMNLP 2021
doi: 10.48550/arXiv.2104.12114
---
## 概要
提出无监督语义聚类方法解决开放意图发现问题：从自然语言话语集合中自动发现意图，无需预定义意图或标注。结合依存解析提取关键语义成分，再用聚类算法发现意图类别。EMNLP 2021。

## 覆盖的模糊层级

**覆盖 L1（意图本身未知）**。从零开始发现意图——不假设意图集存在，从原始话语中无监督地发现意图类别。与 GID 的区别：GID 已有 IND 意图集并发现 OOD 新意图；本方法**从零开始**，无任何预定义意图。

## 核心机制

1. **依存解析**：从话语中提取关键语义成分（动词-名词对等），作为意图的核心表达
2. **语义聚类**：对提取的语义成分聚类，每个簇代表一个发现的意图
3. **意图命名**：根据簇内代表性词语为发现的意图自动命名

## 核心论点
- 为新领域设计意图集耗时且需领域专家，应自动化
- 依存解析提取的语义成分比原始话语更适合聚类
- 无监督方法可从零发现意图，降低新领域部署成本

## 关联
- [[IntentUnderstanding]] — 无监督意图发现方法
- [[handling-vague-user-input]] — 覆盖 L1，从零发现意图
- [[GID]] — 对比：本方法从零发现 vs GID 在已有 IND 基础上发现 OOD
- [[NOEM³A]] — 对比：NOEM³A 需预定义 ontology vs 本方法自动发现意图集
