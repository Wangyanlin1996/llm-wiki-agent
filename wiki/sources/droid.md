---
title: 'DROID: Dual Representation for Out-of-Scope Intent Detection'
type: source
tags:
- OOS-detection
- open-set-recognition
- dual-representation
- L1-unknown-intent
date: 2025-10-15
source_file: raw/papers/droid.pdf
last_updated: 2026-06-23
arxiv_id: '2510.14110'
authors:
- Wael Rashwan
- Hossam M. Zawbaa
- Sourav Dutta
year: 2025
doi: 10.48550/arXiv.2510.14110
---
## 概要
DROID（Dual Representation for Out-of-Scope Intent Detection）提出端到端框架，学习两种互补表示：监督式 in-domain 分类器 + 对比式 open-set 原型网络。用单一校准阈值区分已知与 OOS 意图，无需后处理打分。在已知意图上提升 3-8%、OOS 意图上提升 8-20%，低数据场景增益最大。

## 覆盖的模糊层级

**覆盖 L1 的检测侧（识别"不属于已知意图"）**。DROID 解决的是 OOS 检测——判断输入是否不属于任何已知意图。但它**不发现新意图**（区别于 GID），也**不澄清**（区别于 CICC），只做"是/否已知"的二元判断。

## 核心机制

1. **双表示**：
   - 监督分类器分支：学习 in-domain 意图分类
   - 对比原型分支：学习 open-set 原型表示，增强已知/OOS 边界
2. **单一校准阈值**：推理时用一个阈值区分已知 vs OOS，避免后处理打分模块
3. **端到端训练**：两个分支联合训练，不依赖强分布假设或辅助校准

## 核心论点
- 现有 OOS 检测依赖强分布假设或辅助校准模块，脆弱且敏感
- 双表示 + 简单校准即可实现鲁棒可扩展的 OOS 检测
- 低数据场景（few-shot）增益最大

## 关联
- [[IntentUnderstanding]] — DROID 是意图理解中的 OOS 检测方法
- [[handling-vague-user-input]] — 覆盖 L1 检测侧（知道"不知道"但不发现新意图）
- [[GID]] — 对比：GID 发现新意图 vs DROID 只检测 OOS
- [[CICC]] — 对比：CICC 检测+澄清 vs DROID 只检测
- [[DeepUnknownIntent]] — 前序经典方法
