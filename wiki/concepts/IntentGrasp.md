---
title: "IntentGrasp"
type: concept
tags: [intent-understanding, benchmark, comprehensive, IFT]
sources: [intentgrasp]
last_updated: 2026-05-28
---

# IntentGrasp

IntentGrasp 是评估 LLM 意图理解能力的综合基准，源自 49 个语料库，涵盖 12 个多元领域，含 262,759 个训练实例。

## 规模与覆盖

- **All Set**：跨 12 个领域的 12,909 个测试案例
- **Gem Set**：470 个高难度案例（平衡且经难度筛选）
- **训练集**：262,759 个实例用于意图微调（Intentional Fine-Tuning，IFT）

## 关键发现

- 评估了 7 个家族的 20 个 LLM；All Set 得分低于 60%，Gem Set 得分低于 25%
- 20 个模型中有 17 个在 Gem Set 上的表现低于随机猜测基线（15.2%）
- 估计人类表现约 81.1% — 暴露巨大差距
- IFT 微调在 All Set 上带来 30+ F1 分提升，在 Gem Set 上带来 20+ F1 分提升
- 留一领域交叉实验展示强跨领域泛化能力

## 与 [[IntentUnderstanding]] 的关联

IntentGrasp 提供迄今为止对 [[IntentUnderstanding]] 最全面的评估，用 LLM 缺陷的实证证据补充 [[IntPro]]（按用户意图历史）和 [[IntentSignalTheory]]（理论框架）。它验证了 [[IntentSignalTheory]] 的不可逆意图丢失 — LLM 恰恰因为潜在意图（I*）无法从 prompt（P）中恢复而挣扎。