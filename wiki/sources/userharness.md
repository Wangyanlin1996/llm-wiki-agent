---
title: UserHarness：心智重建增强Agent心智理论
type: source
tags:
- intent-understanding
sources:
- userharness
source_file: raw/papers/userharness.pdf
last_updated: 2026-06-08
arxiv_id: '2605.27721'
authors:
- Cheng Qian
- Jiayu Liu
- Heng Ji
year: 2026
---
## 概要
UserHarness 将 ToM 推理重构为显式用户心智重建。分解用户心理状态、与外部环境的关系、以及由此产生的行动：跟踪用户观察→信念→意图→行动的完整链路。5 个基准上达 95.94% macro accuracy，比现有推理方法+15%，比最强 prompt-only harness+20%。

## 关键贡献
- 用户心智重建：从间接行为建模转向显式心理状态分解
- 观察→信念→意图→行动链路：结构化跟踪而非整体推理
- 嵌套信念：社会推理需要"他相信什么"的层次化建模

## 关键引用
> "Robust user understanding requires reasoning from the roots of the user's mind" — 心智重建比行为推断更根本

## 关联
- [[IntentSignalTheory]] — UserHarness 的信念→意图→行动链为 I*→I-hat→P→O 信号理论提供了具体重建策略
- [[IntentUnderstanding]] — 从行为推断升级到心智重建
- [[MultimodalIntentDisambiguation]] — UserHarness 的心智重建可与 PP-Clarifier 的多模态消歧互补

## 矛盾
- UserHarness 显式重建心智状态，而 [[IntentSignalTheory]] 证明 I* 中的私有意图无法从载体恢复——重建的是 I-hat 而非 I*