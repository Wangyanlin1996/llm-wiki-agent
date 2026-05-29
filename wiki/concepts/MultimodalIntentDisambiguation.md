---
title: "MultimodalIntentDisambiguation"
type: concept
tags: [multimodal, intent-disambiguation, cross-modal, VLM, egocentric-AI]
sources: [pp-clarifier, cocot, debate]
last_updated: 2026-05-29
---

# MultimodalIntentDisambiguation

多模态意图消歧（Multimodal Intent Disambiguation）指通过多模态信息（文本、视觉、语音、手势）消解用户意图中的歧义，实现更准确的意图理解。

## 模态歧义来源

- **文本歧义** — 不充分的语言表达（underspecified language）
- **视觉歧义** — 不完美的视觉数据（imperfect visual data）
- **指示手势歧义** — 指代性手势的不确定性（deictic gestures）
- **语音歧义** — 声调语言中文本歧义可通过语音线索消解

## 代表方法

- [[PP-Clarifier]] — 三模块零样本框架（文本/视觉/跨模态澄清器），4-8B 模型 +30%
- [[CoCoT]] — 认知三阶段推理（感知→情境→规范），多任务 +5-6%
- [[DEBATE]] — 中文语音-文本消歧数据集，通过语音线索消解文本歧义

## 核心挑战

单体 Vision-Language Model 面对多模态歧义输入时倾向于静默失败或产生幻觉（hallucinate responses），模块化分解和认知结构化是两种主流解决路径。

## 关联
- [[IntentUnderstanding]] — 多模态消歧是意图理解的核心子任务
- [[CognitiveChainOfThought]] — 认知结构化推理作为消歧策略
- [[SpeechTextDisambiguation]] — 语音模态的消歧特例
- [[NeuroSymbolicOntology]] — 符号结构注入作为文本模态消歧策略