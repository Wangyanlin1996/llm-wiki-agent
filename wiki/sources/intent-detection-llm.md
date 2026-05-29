---
title: "Intent Detection in the Age of LLMs"
type: source
tags: [intent-understanding, intent-detection, LLM, hybrid-system, EMNLP]
date: 2024-10-02
source_file: raw/papers/intent-detection-llm.md
last_updated: 2026-05-28
---

## 概要
这篇 EMNLP 2024 论文将 LLM 适配于 intent detection（意图检测），通过 in-context learning 和 CoT prompting 与 SetFit transformer 模型对比。它提出基于不确定性路由的 hybrid system（混合系统），在 LLM 准确率的 2% 以内实现 50% 更低延迟。OOS detection（超范围检测）受标签范围和标签空间大小影响；使用内部 LLM 表征的两步方法获得 >5% OOS 检测提升。

## 核心论点
- Hybrid routing（混合路由，LLM+SetFit）在半延迟下达到近 LLM 准确率
- OOS detection 取决于标签范围和空间大小
- 内部 LLM 表征改善 OOS 检测 >5%
- 基于不确定性的路由适合生产部署

## 关键引述
> "Hybrid routing achieves within 2% of LLM accuracy with 50% less latency" — 实用效益：混合路由在半延迟下接近 LLM 准确率

## 关联
- [[IntentUnderstanding]] — 意图检测作为理解任务
- [[IntentDetectionLLM]] — 引入的混合检测方法
- [[IntentGrasp]] — 全面的评测基准对比
- [[IntPro]] — 意图处理与检测系统相关