---
title: "SpeechTextDisambiguation"
type: concept
tags: [speech-disambiguation, Chinese, audio-language-model, textual-ambiguity]
sources: [debate]
last_updated: 2026-05-29
---

# SpeechTextDisambiguation

语音-文本消歧（Disambiguation Through Speech, DTS）指通过语音线索（发音、停顿、重音、语调）消解文本歧义，揭示说话者的真实意图。

## 为什么语音消歧重要

- 文本消歧和视觉消歧已有大量研究，但语音消歧缺乏高质量数据集
- 中文作为声调语言，语音线索在文本歧义消解中尤为关键
- 同一文本在不同语音表达下可能传达截然不同的意图

## DEBATE 数据集

首个中文语音-文本消歧数据集：
- 1001 个歧义语句 × 10 位说话人录制
- 覆盖发音、停顿、重音、语调四种语音消歧线索
- 评测揭示机器与人类在口语意图理解上的巨大差距

## 关联
- [[IntentUnderstanding]] — 语音模态的意图理解
- [[MultimodalIntentDisambiguation]] — 语音消歧作为多模态消歧的补充模态