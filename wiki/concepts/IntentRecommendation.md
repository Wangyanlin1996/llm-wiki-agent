---
title: "Intent Recommendation"
type: concept
tags: [intent-recommendation, proactive-agent, GUI-agent, intent-detection]
sources: [intentrl, pira-bench, pask, vitabench2]
last_updated: 2026-05-27
---

# Intent Recommendation

Intent Recommendation 指 AI 智能体基于推断的用户意图主动检测并建议行动，从被动范式（需显式指令）转向主动范式（智能体预判需求）。

## 范式转变

当前 GUI 和对话智能体以被动方式运作（[[PIRABench]] 指出此问题）。主动范式需要：
- 从连续输入（视觉、对话）中检测可行动事件
- 使推荐适配用户偏好和画像
- 管理多条交错意图线程
- 处理噪声和模糊的输入片段

## 关键方法

- **[[IntentRL]]**：RL 训练的主动智能体，在深度研究前进行意图澄清；shallow-to-deep 意图精炼图；两阶段 RL（离线对话 + 在线模拟器）；超越闭源 DR 澄清模块
- **[[PIRABench]]**：首个面向 GUI 主动意图推荐的基准；提出 [[PIRF]] 记忆感知状态追踪框架；含交错意图的复杂轨迹
- **[[PASK]]**：DD-MM-PAS 范式（Demand Detection → Memory Modeling → Proactive Agent System）；[[IntentFlow]] 需求检测；混合记忆（workspace/user/global）；[[LatentNeeds-Bench]] 真实世界评估

## DD-MM-PAS 范式

[[PASK]] 论文提出流式主动智能体的通用范式：
1. **DD**（Demand Detection）：[[IntentFlow]] 从流式交互中检测用户需求
2. **MM**（Memory Modeling）：混合记忆（workspace、user、global）用于长期上下文
3. **PAS**（Proactive Agent System）：闭环检测-记忆-行动基础设施

## 跨方向关联

Intent Recommendation 依赖 [[AgentMemory]] 存储过往交互和用户偏好（[[PASK]] 混合记忆、[[PIRF]] 状态追踪）。它也需要 [[IntentUnderstanding]] 在推荐前推断潜在意图（[[IntentRL]] 在研究前澄清意图）。

## 关键挑战

真实世界的意图跨多条线程碎片化且交错 — 智能体须从噪声中辨析可行动事件，同时维持偏好感知的推荐（[[PIRABench]]）。