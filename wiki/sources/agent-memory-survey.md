---
title: "From Storage to Experience"
type: source
tags: [agent-memory, survey, LLM-agent, memory-evolution]
date: 2026-05-09
source_file: raw/papers/agent-memory-survey.md
last_updated: 2026-05-28
---

## 概要
本综述为 LLM agent memory 提出了一个新的进化框架，形式化为三个阶段：Storage（轨迹保存）、Reflection（轨迹精炼）和 Experience（轨迹抽象）。它弥合了碎片化的 OS 工程与认知科学视角，将主动探索和跨轨迹抽象识别为 Experience 阶段的前沿机制。

## 核心论点
- Agent memory 研究在 OS 工程与认知科学之间呈现碎片化
- Memory 进化遵循 Storage→Reflection→Experience 轨迹
- 三个核心驱动因素：长程一致性、动态环境、持续学习
- 前沿 Experience 阶段以主动探索和跨轨迹抽象为特征

## 关键引述
> "current research remains fragmented, oscillating between operating system engineering and cognitive science" — 碎片化诊断：当前研究在操作系统工程与认知科学之间摇摆

> "formalizing the development process into three stages: Storage, Reflection, and Experience" — 进化框架：将发展过程形式化为三个阶段

## 关联
- [[AgentMemory]] — 本综述为 AgentMemory 机制提供了进化框架
- [[EvoMemory]] — test-time evolution 与框架中的 Experience 阶段一致
- [[LightMem]] — SLM 驱动的轻量级 memory 符合 Storage→Reflection 进化路径
- [[Emem]] — episodic context reconstruction 代表向 Experience 阶段的转变
- [[IntentUnderstanding]] — Experience 阶段的主动探索与意图理解相关联
- [[IntentRecommendation]] — 跨轨迹抽象实现主动意图推荐

## 矛盾
- 与仅从 OS 工程视角看待 memory 的观点矛盾：本综述论证 memory 必须超越 storage 向 experiential abstraction（经验抽象）进化