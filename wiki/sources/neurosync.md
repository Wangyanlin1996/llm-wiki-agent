---
title: "NeuroSync"
type: source
tags: [intent-understanding, intent-task-matching, HCI, UIST]
date: 2025-08-02
source_file: raw/papers/neurosync.md
last_updated: 2026-05-28
---

## 概要
NeuroSync（UIST 2025）提出 direct intent-task matching（直接意图-任务匹配）作为新的 human-LLM 交互范式，允许用户在代码生成之前检查和编辑 LLM 的理解。Bidirectional ambiguity（双向歧义，非线性意图通过线性 prompts 表达）导致意图-代码不对齐；knowledge distillation（知识蒸馏）提取 LLM 理解供直接操控。用户研究（N=12）显示对齐改善和认知负担降低。

## 核心论点
- Bidirectional ambiguity（双向歧义）导致意图-代码不对齐
- 对 LLM 理解的直接操控是一种可行范式
- Knowledge distillation（知识蒸馏）使提取 LLM 内部表征成为可能
- 用户研究确认对齐改善和认知负担降低

## 关键引述
> "Bidirectional ambiguity causes intent-code misalignment" — 问题框架：双向歧义导致意图与代码不对齐

## 关联
- [[IntentUnderstanding]] — NeuroSync 解决意图理解差距
- [[NeuroSync]] — 引入的意图-任务匹配范式
- [[IntentSignalTheory]] — 意图信号理论为双向歧义提供理论基础
- [[IntentCommunicationDesign]] — 传达设计与直接操控相关