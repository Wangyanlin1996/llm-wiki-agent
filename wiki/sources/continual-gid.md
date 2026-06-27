---
title: 'Continual Generalized Intent Discovery: Marching Towards Dynamic and Open-world
  Intent Recognition'
type: source
tags:
- intent-discovery
- open-world
- continual-learning
- OOD
- L1-unknown-intent
date: 2023-10-16
source_file: raw/papers/continual-gid.pdf
last_updated: 2026-06-23
arxiv_id: '2310.10184'
authors:
- Xiaoshuai Song
- Yutao Mou
- Keqing He
year: 2023
venue: ACL 2023
doi: 10.48550/arXiv.2310.10184
---
## 概要
CGID（Continual Generalized Intent Discovery）扩展 GID 到持续学习场景：不再假设所有已知和未知意图数据同时可用，而是**增量地在不同阶段发现新意图**。解决真实世界中意图逐步涌现的动态需求，面向动态开放世界意图识别。

## 覆盖的模糊层级

**覆盖 L1（意图本身未知）**。与 GID 的区别：GID 是一次性发现，CGID 是**多阶段持续发现**——更接近真实场景（用户需求逐步涌现，非一次性全部出现）。

## 核心论点
- GID 假设所有数据同时可用，不满足真实世界的动态需求
- 意图发现应是增量的：新意图在不同阶段逐步涌现
- 持续发现面临**灾难性遗忘**挑战：学习新意图时不能忘记旧意图

## 关联
- [[IntentUnderstanding]] — CGID 是意图理解中的持续开放世界发现
- [[handling-vague-user-input]] — 覆盖 L1，持续发现新意图
- [[GID]] — 前序工作：GID 的一次性发现 → CGID 的持续发现
