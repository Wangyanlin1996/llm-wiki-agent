---
title: "Plug-and-Play Clarifier: A Zero-Shot Multimodal Framework for Egocentric Intent Disambiguation"
type: source
tags: [multimodal-disambiguation, egocentric-AI, zero-shot, VLM, cross-modal, AAAI-2026]
date: 2025-11-12
source_file: raw/papers/pp-clarifier.md
last_updated: 2026-05-29
---

## 概要
Plug-and-Play Clarifier 是模块化零样本多模态意图消歧框架，包含文本澄清器（对话驱动推理消解语言歧义）、视觉澄清器（实时引导用户调整拍摄位置）和跨模态澄清器（3D 指示手势接地识别指向对象）三个协同模块，使 4-8B 小模型意图澄清性能提升约 30%。

## 核心论点
- 自中心 AI Agent 的意图歧义源于三种模态的不完美信息叠加：不充分语言、不完美视觉、指示手势
- 现有单体 Vision-Language Model 静默失败或产生幻觉，无法有效消解多模态歧义输入
- 模块化分解为可独立解决的子任务，零样本设计使小模型竞争力显著提升

## 关键引述
> "our framework improves the intent clarification performance of small language models (4–8B) by approximately 30%, making them competitive with significantly larger counterparts" — 小模型竞争力提升

> "Existing monolithic Vision-Language Models (VLMs) struggle to resolve these multimodal ambiguous inputs, often failing silently or hallucinating responses" — 单体 VLM 的局限

## 关联
- [[IntentUnderstanding]] — 多模态意图消歧的典型方法
- [[MultimodalIntentDisambiguation]] — 核心概念：多模态意图消歧
- [[NeuroSymbolicOntology]] — 与 NOEM³A 的消歧策略对比
- [[ContextAgent]] — 两者都关注感官上下文在意图消歧中的作用