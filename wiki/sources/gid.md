---
title: 'Generalized Intent Discovery: Learning from Open World Dialogue System'
type: source
tags:
- intent-discovery
- open-world
- OOD-detection
- clustering
- L1-unknown-intent
date: 2022-09-14
source_file: raw/papers/gid.pdf
last_updated: 2026-06-23
arxiv_id: '2209.06030'
authors:
- Yutao Mou
- Keqing He
- Yanan Wu
year: 2022
venue: EMNLP 2022
doi: 10.48550/arXiv.2209.06030
---
## 概要
GID（Generalized Intent Discovery）提出开放世界意图发现任务：将已有 in-domain (IND) 意图分类器扩展到包含 IND + OOD 意图的开放世界意图集。系统同时分类已标注的 IND 意图类，并**发现和识别新的未标注 OOD 意图类型**。构造了两个场景数据集并提出两种框架（pipeline 和 joint）。

## 覆盖的模糊层级

**覆盖 L1（意图本身未知）**。当用户输入不属于任何已知意图时，GID 不只是拒绝（OOS 检测）或猜测（NOEM³A），而是**从 OOD 查询中发现新意图类别**——将未知意图聚类成新类别并扩展分类器。

## 核心机制

两阶段框架：
1. **OOD 检测**：识别测试意图是否属于 OOD（不属于已知 IND 意图）
2. **OOD 发现**：对 OOD 查询聚类，发现新意图类型，增量扩展到分类器

两种框架：
- **Pipeline**：OOD 检测模块 → IND 分类器 + OOD 发现器分别处理
- **Joint**：联合训练 IND 分类和 OOD 发现

## 核心论点
- 传统意图分类基于预定义意图集，无法处理开放世界中的 OOD 查询
- OOD 查询不是噪声，而是**未来改进的方向**——包含用户真实但未覆盖的需求
- 意图发现应同时分类已知 + 发现未知，而非仅检测 OOD

## 关联
- [[IntentUnderstanding]] — GID 是意图理解中的开放世界发现方法
- [[handling-vague-user-input]] — 覆盖 L1，从未知中发现新意图
- [[NOEM³A]] — 对比：NOEM³A 在固定 ontology 内消歧 vs GID 发现 ontology 外的新意图
- [[ContinualGID]] — 后续工作：持续学习版 GID
