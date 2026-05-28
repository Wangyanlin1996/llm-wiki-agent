---
title: "Intent Understanding"
type: concept
tags: [intent-understanding, human-AI-interaction, context-aware, intent-recognition]
sources: [intpro, intent-signal-theory, vitabench2, intent-communication-design]
last_updated: 2026-05-27
---

# Intent Understanding

Intent Understanding 在 AI 智能体中指从情境上下文推断用户意图，超越静态识别，走向动态、上下文感知和个性化推理。

## 理论框架

- **[[IntentSignalTheory]]**（IST）：形式化四个对象 — I*（潜在源意图）、I-hat（可观测代理）、P（编码载体）、O（模型输出）。证明 **Irreversible Intent Loss** 定理：载体中缺失的私有意图不可恢复。将 prompt engineering 重新定义为意图协议设计。
- **Intent Communication Design Space**（[[intent-communication-design]]）：Transparency（what）× Abstraction（when）× Modality（how）— 跨旁观者、协作和共享控制场景的智能体-人类意图通信多维框架。

## 关键方法

- **[[IntPro]]**：带检索条件意图推断的代理智能体；按用户的意图历史库；SFT + GRPO 训练配合工具感知奖励；评估何时检索过往模式 vs. 直接推断
- **[[VitaBench2]]**：面向个性化+主动智能体评估的基准；揭示 SOTA 与实用个性化之间的显著差距

## 从静态到动态

传统 Intent Understanding 将其视为静态识别（[[IntPro]] 指出此差距）。当前方法强调：
- 上下文感知推理：兼顾即时上下文与深层动机
- 个体适配：通过按用户意图模式实现个性化
- 主动识别缺失信息

## 跨方向关联

Intent Understanding 是 [[IntentRecommendation]] 的前提 — 理解潜在意图才能主动推荐行动。[[VitaBench2]] 桥接理解与推荐两个方向。[[IntentRL]] 训练智能体在行动前先澄清意图。

## 关键挑战

用户的潜在源意图（I*）常在可观测 prompt（P）中缺失，形成无法完全恢复的信息缺口（[[IntentSignalTheory]] Irreversible Intent Loss）。