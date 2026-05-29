---
title: "InnerThoughts"
type: concept
tags: [intent-recommendation, proactive-agent, inner-thoughts, multi-party]
sources: [inner-thoughts]
last_updated: 2026-05-28
---

# 内隐思维（Inner Thoughts）

内隐思维（Inner Thoughts）框架为 AI 配备与外显通信并行运行的持续内隐思维流（covert train of thoughts），建模表达这些思维的内驱力（intrinsic motivation）。这使得智能体能在多方对话中主动参与，而非仅依赖轮流发言线索。

## 关键机制

- **内隐思维过程（covert thought process）**：AI 维护评估相关性和表达动力的内部独白
- **内驱力建模（intrinsic motivation modeling）**：决定 AI 何时有有价值的内容可补充
- **外显-内隐并行（overt-covert parallelism）**：内隐思维指导外部对话中何时说、说什么

## 评估结果

用户研究显示在以下维度显著超越基线：
- 拟人化（Anthropomorphism）
- 连贯性（Coherence）
- 智能感（Intelligence）
- 轮流适当性（Turn-taking appropriateness）

## 与 [[IntentRecommendation]] 的关联

内隐思维为 [[IntentRecommendation]] 提供认知层面的机制 — 智能体不是检测表层意图信号，而是形成自身理解和主动贡献的动力。这与 [[PASK]] 的 DD-MM-PAS 范式中需求检测为内部过程相呼应，并通过添加持续内部推理维度补充了 [[IntentRL]] 的意图澄清。