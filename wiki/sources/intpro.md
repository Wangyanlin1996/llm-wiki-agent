---
title: "IntPro"
type: source
tags: [intent-understanding, proxy-agent, retrieval-conditioned, GRPO]
date: 2026-03-03
source_file: raw/papers/intpro.md
last_updated: 2026-05-27
---

## 概要
IntPro 是一个用于上下文感知 intent understanding 的 proxy agent，通过 retrieval-conditioned inference 适应个体用户。它将 intent explanations 存储在 per-user history library 中，通过 SFT + GRPO with tool-aware rewards 训练，在历史模式检索和直接推理之间取得平衡，覆盖三个多样化场景。

## 关键论点
- Intent understanding 应为动态过程（而非静态识别）
- 个体 intent history 提升准确性和泛化能力
- Retrieval-conditioned inference 实现 per-user 适应
- SFT+GRPO 训练使模型学会何时检索 vs. 直接推理

## 关键引述
> "existing approaches often treat intent understanding as a static recognition task, overlooking users' accumulated intent patterns" — 差距识别

> "IntPro achieves strong intent understanding performance with effective context-aware reasoning capabilities across different scenarios and model types" — 结果

## 关联
- [[IntentUnderstanding]] — IntPro 是上下文感知 IntentUnderstanding 的具体方法
- [[IntPro]] — proxy agent 概念在此形式化
- [[IntentSignalTheory]] — IST 的 intent objects 与 IntPro 的 per-user intent history 一致
- [[VitaBench2]] — VitaBench 2.0 评估与 IntPro 相关的个性化 intent understanding
- [[AgentMemory]] — per-user history library 与 AgentMemory 机制相关
- [[PIRABench]] — PIRA-Bench 评估 IntPro 可贡献的主动 intent

## 矩盾
- 与静态 intent recognition 矛盾：IntPro 论证 intent understanding 必须是动态且用户自适应的