---
title: "OutOfScopeDetection"
type: concept
tags: [OOS-detection, open-set-recognition, intent-classification, L1-unknown-intent]
sources: [droid, deep-unknown-intent, cicc]
last_updated: 2026-06-23
---

# OutOfScopeDetection

越界意图检测（Out-of-Scope / Out-of-Domain Intent Detection）指判断用户输入是否不属于任何已知意图类别。是开放集意图识别（open-set intent recognition）的核心子任务，解决"识别到输入不属于已知"的问题。

## 与模糊层级的关系

覆盖 [[handling-vague-user-input|模糊输入三层层级]] 的 **L1 检测侧**：知道"不知道"，但不发现新意图也不澄清。是 L1 处理的第一步——先识别未知，再决定如何处理（拒绝/发现/澄清）。

## 技术路线

| 路线 | 方法 | 代表 |
|---|---|---|
| 密度新颖性检测 | 特征提取 + LOF 离群检测 | [[DeepUnknownIntent]] — BiLSTM+margin loss+LOF |
| 双表示 | 监督分类 + 对比原型，单一阈值 | [[DROID]] — 端到端双分支 |
| Conformal prediction | 预测集为空 = OOS | [[CICC]] — 有覆盖率保证的 OOS 检测 |

## 与意图发现/澄清的区别

| 维度 | OOS 检测 | 意图发现 | 意图澄清 |
|---|---|---|---|
| 输出 | 二元（已知/未知） | 新意图类别 | 澄清问题 |
| 后续动作 | 拒绝/转人工 | 扩展分类器 | 用户选择 |
| 代表 | [[DROID]] | [[GID]] | [[CICC]] |
| 覆盖层级 | L1 检测侧 | L1 发现侧 | L1+L2 澄清侧 |

## 核心挑战

- **分布假设脆弱**：现有方法依赖强分布假设，对校准敏感
- **低数据场景**：few-shot 下已知意图样本少，OOS 边界难学
- **阈值选择**：单一阈值需校准，过高漏检 OOS，过低误拒已知

## 关联
- [[IntentUnderstanding]] — OOS 检测是意图理解的开放集扩展
- [[handling-vague-user-input]] — 覆盖 L1 检测侧
- [[OpenWorldIntentDiscovery]] — 递进关系：OOS 检测 → 意图发现
- [[CICC]] — CICC 的 OOS 检测有覆盖率保证，优于纯阈值方法
