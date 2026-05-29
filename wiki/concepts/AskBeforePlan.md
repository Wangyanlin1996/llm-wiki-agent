---
title: "AskBeforePlan"
type: concept
tags: [intent-recommendation, proactive-planning, multi-agent, clarification-first]
sources: [ask-before-plan]
last_updated: 2026-05-28
---

# 澄清先行（Ask-before-Plan）

澄清先行（Ask-before-Plan）引入主动智能体规划（Proactive Agent Planning） — 要求智能体在制定计划前预测澄清需求、调用工具收集信息，然后再生成计划。CEP（Clarification-Execution-Planning，澄清-执行-规划）多智能体框架将这些角色分离。

## CEP 框架

- **澄清智能体（Clarification Agent）**：识别用户指令模糊之处并提出澄清问题
- **执行智能体（Execution Agent）**：调用工具收集规划所需信息
- **规划智能体（Planning Agent）**：基于澄清后的意图和收集的信息生成最终计划
- **轨迹调优（Trajectory tuning）**：用于静态澄清和执行智能体
- **记忆回溯（Memory recollection）**：用于动态执行智能体

## 与 [[IntentRecommendation]] 的关联

澄清先行是 **澄清先行主动规划（clarification-first proactive planning）** 的奠基工作，确立了智能体应在行动前解决模糊性的原则。这直接支撑了 [[IntentRL]]（深度研究前的主动意图澄清），并通过提供规划骨架补充了 [[PIRABench]]（GUI 上的主动意图推荐）。