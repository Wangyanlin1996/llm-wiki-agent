---
title: "Intent Signal Theory"
type: source
tags: [intent-understanding, intent-signal, computational-framework, theory]
date: 2026-05-20
source_file: raw/papers/intent-signal-theory.md
last_updated: 2026-05-27
---

## 概要
Intent Signal Theory (IST) 形式化了 AI 交互中缺失的 intent 层，区分四个对象：latent source intent (I*)、observable intent proxy (I-hat)、encoded carrier (P) 和 model output (O)。它证明了 Irreversible Intent Loss 定理，并将 prompt engineering 重新界定为 intent-protocol design，在 6 个 LLM、3 种语言和 3 个任务域上验证。

## 关键论点
- 当前 AI 模型混淆了四个不同的 intent 对象
- Carrier 中缺失的 private intent 无法恢复（Irreversible Intent Loss 定理）
- Prompt engineering 应被重新界定为 intent-protocol design
- Structural-fidelity splits 在多个 LLM 和语言上得到验证

## 关键引述
> "Current AI interaction models treat the prompt as the primary object of exchange, omitting a critical layer: the user's latent source intent" — 核心批评

> "The Theorem of Irreversible Intent Loss establishes that private intent absent from the carrier cannot be recovered beyond generic substitution" — 关键定理

## 关联
- [[IntentUnderstanding]] — IST 为 IntentUnderstanding 提供理论基础
- [[IntentSignalTheory]] — 此处形式化的计算框架
- [[IntPro]] — IntPro 的 per-user history 解决了 IST 所识别的 intent loss
- [[IntentRL]] — IntentRL 的主动澄清缓解了 Irreversible Intent Loss
- [[IntentRecommendation]] — 主动 recommendation 补偿缺失的 intent signals

## 矩盾
- 与 prompt-as-primary-object 观点矛盾：IST 论证 prompts 仅为 carriers，而非 intent 本身