---
title: "CognitiveChainOfThought"
type: concept
tags: [cognitive-reasoning, chain-of-thought, multimodal, social-reasoning, VLM]
sources: [cocot]
last_updated: 2026-05-29
---

# CognitiveChainOfThought (CoCoT)

认知 Chain-of-Thought（Cognitive Chain-of-Thought, CoCoT）是将视觉语言模型的多模态社会推理通过认知 grounded 三阶段结构化的推理框架。

## 三阶段推理

1. **Perception（感知）** — 从视觉和文本输入中提取接地的事实（grounded facts）
2. **Situation（情境）** — 推断社会情境（social situations），理解上下文含义
3. **Norm（规范）** — 应用社会规范（social norms），做出合乎社会期望的判断

## 与 Naive CoT 的区别

Naive Chain-of-Thought 在视觉接地的社会任务中失效，因为模型必须同时感知、理解和判断。CoCoT 将这三者分解为有序的认知阶段。

## SFT 内化效应

在 CoCoT 结构化轨迹上进行 SFT 后，模型内化推理模式（+5-6%），推理时无需显式 CoCoT 提示——模型学会了"如何思考"而非仅遵循"如何回答"的指令。

## 关联
- [[IntentUnderstanding]] — CoCoT 在意图消歧任务上的应用
- [[MultimodalIntentDisambiguation]] — 认知结构化作为消歧策略
- [[NeuroSymbolicOntology]] — 符号结构（社会规范）vs 认知结构（推理阶段）