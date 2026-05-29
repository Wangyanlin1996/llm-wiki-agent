---
title: "IntentGrasp"
type: source
tags: [intent-understanding, benchmark, comprehensive, IFT]
date: 2026-05-09
source_file: raw/papers/intentgrasp.md
last_updated: 2026-05-28
---

## 概要
IntentGrasp 是一个全面评估 LLM 意图理解的 benchmark，源自 49 个语料库，覆盖 12 个领域，包含 262K 训练实例。对 20 个 LLM 的评估显示 All Set 得分低于 60%，Gem Set 得分低于 25%，其中 17/20 低于随机基线。Intentional Fine-Tuning (IFT，意图微调) 在 All Set 上带来 30+ F1 提升，Gem Set 上 20+ 提升，并具有强跨领域泛化能力。

## 核心论点
- LLM 意图理解严重不足（在困难案例上低于随机基线）
- IFT fine-tuning（意图微调）显著改善意图理解，具有跨领域泛化能力
- 人类表现约 81%，揭示巨大差距
- 12 领域覆盖展示任务多样性

## 关键引述
> "17 out of 20 tested models perform worse than a random-guess baseline (15.2%) on Gem Set" — 缺陷严重性：20 个测试模型中 17 个低于随机猜测基线
> "Intentional Fine-Tuning yields significant gains of 30+ F1 points on All Set and 20+ points on Gem Set" — 改善路径：IFT 带来显著 F1 提升

## 关联
- [[IntentUnderstanding]] — IntentGrasp 为意图理解建立评测基准
- [[IntentGrasp]] — 引入的评测基准概念
- [[IntPro]] — 相关的意图处理方法
- [[IntentSignalTheory]] — intent signals 的理论基础
- [[IntentDetectionLLM]] — 相关的 LLM 意图检测工作