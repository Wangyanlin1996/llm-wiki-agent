---
title: "DEBATE: A Dataset for Disentangling Textual Ambiguity in Mandarin Through Speech"
type: source
tags: [speech-disambiguation, Chinese, dataset, audio-language-model, textual-ambiguity]
date: 2025-06-09
source_file: raw/papers/debate.md
last_updated: 2026-05-29
---

## 概要
DEBATE 是首个中文语音-文本消歧数据集，包含 1001 个歧义语句×10 位说话人录制，通过语音线索（发音、停顿、重音、语调）消解文本歧义揭示说话者真实意图。评测三个 SOTA 大语音/音频语言模型，揭示机器与人类在理解口语意图上存在巨大性能差距。

## 核心论点
- 文本和视觉消歧已有大量研究，但语音消歧（Disambiguation Through Speech, DTS）仍严重缺乏高质量数据集
- 中文因声调语言特性，语音线索在文本歧义消解中尤为重要
- 当前大语音/音频语言模型在口语意图理解上远不及人类水平，揭示重要研究空白

## 关键引述
> "DEBATE represents the first effort of its kind and offers a foundation for building similar DTS datasets across languages and cultures" — 首个 DTS 数据集的意义

> "illustrating clear and huge performance gaps between machine and human understanding of spoken intent" — 机器与人类的差距

## 关联
- [[IntentUnderstanding]] — 语音模态的意图理解
- [[MultimodalIntentDisambiguation]] — 语音模态消歧作为多模态消歧的补充
- [[SpeechTextDisambiguation]] — 核心概念：语音-文本消歧