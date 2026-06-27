---
title: "OpenWorldIntentDiscovery"
type: concept
tags: [intent-discovery, open-world, OOD, clustering, L1-unknown-intent]
sources: [gid, continual-gid, open-intent-discovery]
last_updated: 2026-06-23
---

# OpenWorldIntentDiscovery

开放世界意图发现（Open-World Intent Discovery）指从用户输入中**自动发现新意图类别**，不局限于预定义意图集。当用户输入不属于任何已知意图时，不是简单拒绝（OOS 检测）或静默猜测（[[NeuroSymbolicOntology|NOEM³A]]），而是**从未知查询中发现新意图**并扩展分类器。

## 与模糊层级的关系

覆盖 [[handling-vague-user-input|模糊输入三层层级]] 的 **L1（意图本身未知）**：当意图完全不在已有意图集中时，发现新意图而非强分配。

## 技术路线

| 路线 | 方法 | 代表 |
|---|---|---|
| 从零发现 | 无监督聚类从原始话语发现意图 | [[OpenIntentDiscovery]] — 依存解析 + 语义聚类 |
| IND+OOD 发现 | 已有 IND 意图集，从 OOD 查询发现新意图 | [[GID]] — OOD 检测 + 聚类发现 |
| 持续发现 | 多阶段增量发现新意图 | [[ContinualGID]] — 解决灾难性遗忘 |
| 意图发现+澄清 | 不确定时生成澄清问题缩小范围 | [[CICC]] — conformal prediction 保证覆盖率 |

## 与 OOS 检测的区别

- [[OutOfScopeDetection]] 只判断"是否未知"（二元检测），不发现新意图
- OpenWorldIntentDiscovery 进一步**从未知中发现新类别**（聚类+命名）
- 两者是递进关系：先 OOS 检测识别未知 → 再意图发现将未知聚类为新类别

## 关联
- [[IntentUnderstanding]] — 意图发现是意图理解的开放世界扩展
- [[handling-vague-user-input]] — 覆盖 L1 模糊层级
- [[NOEM³A]] — 对比：NOEM³A 在固定 ontology 内消歧 vs 开放世界发现 ontology 外新意图
- [[IntentSignalTheory]] — 发现新意图是恢复 I* 的一种方式（从群体行为中推断潜在意图）
