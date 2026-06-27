---
title: IntentVLM：视频语言前逆建模意图识别
type: source
tags:
- intent-understanding
sources:
- intentvlm
source_file: raw/papers/intentvlm.pdf
last_updated: 2026-06-08
arxiv_id: '2604.24002'
authors:
- Hamed Rahimi
- Clemence Grislain
- Adrien Jacquet Cretides
- Olivier Sigaud
- Mohamed Chetouani
year: 2026
---
## 概要
IntentVLM 提出两阶段视频语言框架用于开放词汇意图识别。受认知科学前逆建模启发，将意图理解分解为目标候选生成（forward）+结构化推理选择（inverse），有效减少潜在推理中的幻觉。在 IntentQA 和 Inst-IT Bench 上达 SOTA 80%，超越基线 30%，达到人类水平。

## 关键贡献
- 前逆建模两阶段：forward 生成候选 → inverse 结构化选择
- 开放词汇意图识别：不依赖预定义意图类别
- 减少幻觉：候选生成+选择机制避免自由推理的幻觉问题

## 关键引用
> "This structured reasoning approach enhances open-vocabulary intention understanding without catastrophic forgetting" — 结构化推理优势

## 关联
- [[IntentUnderstanding]] — IntentVLM 将意图理解从文本扩展到视频语言模态
- [[CognitiveChainOfThought]] — CoCoT 的感知→情境→规范三阶段与 IntentVLM 的 forward→inverse 两阶段互补
- [[MultimodalIntentDisambiguation]] — IntentVLM 的视频意图识别与 PP-Clarifier 的多模态消歧形成多模态矩阵

## 矛盾
- IntentVLM 的两阶段分解假设意图可从视觉行为推断，但 [[IntentSignalTheory]] 的 Irreversible Intent Loss 指出私有意图可能不可观测