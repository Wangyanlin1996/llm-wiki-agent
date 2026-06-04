---
title: "Reward-Driven Interaction: 用户满意度预测增强主动对话Agent"
type: source
tags: [intent-understanding]
sources: [reward-driven-interaction]
source_file: raw/papers/2505.18731.pdf
last_updated: 2026-06-04
---

## 概要
Reward-Driven Interaction 将用户满意度预测作为内在奖励信号驱动主动对话Agent，在检测潜在不满意时触发澄清问题。对比自监督学习任务帮助模型学习罕见表达表示和识别ASR错误；领域-意图分类辅助任务改善长尾领域表示。在DuerOS工业系统上验证。

## 关键贡献
- 用户满意度作为内在奖励信号——检测不满意时触发澄清
- 对比自监督学习辅助任务——罕见表达表示+ASR错误识别
- 领域-意图分类辅助任务——长尾领域表示改善
- DuerOS工业对话系统在线验证

## 关键引用
- 核心思想：将用户满意度预测转化为Agent的内在奖励驱动机制

## 关联
- [[IntentUnderstanding]] — 满意度预测作为意图理解的反馈信号
- [[IntentRL]] — 同为RL训练主动意图，但Reward-Driven用满意度而非意图图
- [[SpeakRL]] — 同为RL增强澄清能力，但Reward-Driven用满意度奖励而非澄清质量奖励

## 矛盾
- 弱标签引入偏差——传统方法在ASR错误和长尾领域下表现不佳