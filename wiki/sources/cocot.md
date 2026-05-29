---
title: "Cognitive Chain-of-Thought (CoCoT): Structured Multimodal Reasoning about Social Situations"
type: source
tags: [cognitive-reasoning, multimodal, theory-of-mind, social-reasoning, intent-disambiguation, VLM]
date: 2025-07-27
source_file: raw/papers/cocot.md
last_updated: 2026-05-29
---

## 概要
CoCoT 提出认知 grounded 三阶段推理框架（Perception→Situation→Norm），将视觉语言模型的多模态社会推理结构化。在意图消歧、Theory of Mind、社会常识推理和安全指令遵循等多个任务上平均提升 5-6%，SFT 训练后模型内化推理模式无需显式 CoCoT 提示。

## 核心论点
- Naive Chain-of-Thought 在视觉接地的社会任务中失效，需要认知结构化的推理阶段
- 将推理分解为感知（提取接地事实）、情境（推断社会情境）、规范（应用社会规范）三阶段，实现可解释的社会推理
- SFT 训练使模型内化结构化推理模式而非仅遵循指令，推理时无需显式提示

## 关键引述
> "naive CoT breaks down in visually grounded social tasks, where models must perceive, understand, and judge all at once" — Naive CoT 的局限

> "supervised fine-tuning on CoCoT-structured traces yields 5-6% improvements without explicit CoCoT prompting at inference, demonstrating that models internalize the structured reasoning pattern" — SFT 内化效应

## 关联
- [[IntentUnderstanding]] — CoCoT 在多模态意图消歧任务上的应用
- [[CognitiveChainOfThought]] — CoCoT 的核心推理框架概念
- [[MultimodalIntentDisambiguation]] — 与 PP-Clarifier 的消歧策略对比
- [[NeuroSymbolicOntology]] — 符号结构（社会规范）与认知结构的对比