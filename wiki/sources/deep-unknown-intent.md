---
title: Deep Unknown Intent Detection with Margin Loss
type: source
tags:
- unknown-intent-detection
- margin-loss
- BiLSTM
- LOF
- novelty-detection
- L1-unknown-intent
date: 2019-06-04
source_file: raw/papers/deep-unknown-intent.pdf
last_updated: 2026-06-23
arxiv_id: '1906.00434'
authors:
- Ting-En Lin
- Hua Xu
year: 2019
venue: ACL 2019
citation_count: 162
doi: 10.48550/arXiv.1906.00434
---
## 概要
提出两阶段未知意图检测方法：BiLSTM + margin loss 作为特征提取器学习判别性表示，再输入 LOF（Local Outlier Factor）密度新颖性检测算法检测未知意图。ACL 2019，162 引用，是未知意图检测的经典基线。

## 覆盖的模糊层级

**覆盖 L1 的检测侧**。与 DROID 类似，只检测"是否未知"，不发现新意图也不澄清。是 OOS 检测的早期经典工作。

## 核心机制

1. **Stage 1 — 特征提取**：BiLSTM + margin loss 训练，学习判别性特征表示（同类紧凑、异类分离）
2. **Stage 2 — 新颖性检测**：将特征向量输入 LOF（基于密度的离群检测），判断是否为未知意图

## 核心论点
- margin loss 使特征空间中同类紧凑、异类分离，有利于后续新颖性检测
- LOF 基于密度的方法不假设数据分布，比参数化方法更鲁棒
- 两阶段解耦：特征学习与新颖性检测分离，各自可优化

## 关联
- [[IntentUnderstanding]] — 未知意图检测的经典方法
- [[handling-vague-user-input]] — 覆盖 L1 检测侧
- [[DROID]] — 后续改进：DROID 用双表示替代 BiLSTM+LOF 两阶段
- [[GID]] — 对比：Deep Unknown Intent 只检测 vs GID 检测+发现
