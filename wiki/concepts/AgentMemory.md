---
title: "Agent Memory"
type: concept
tags: [agent-memory, LLM-agent, memory-system, episodic-memory]
sources: [evo-memory, agent-memory-survey, lightmem, emem]
last_updated: 2026-05-27
---

# 智体记忆（Agent Memory）

智体记忆（Agent Memory）指基于 LLM 的智能体跨交互存储、检索和演化信息的机制。其发展已从被动轨迹存储走向主动经验抽象。

## 演化框架

据 [[agent-memory-survey]]，智体记忆经历三个阶段：
- **Storage（存储）**：原始轨迹保存 — 存储对话/行动历史
- **Reflection（反思）**：轨迹精炼 — 概括、提取、压缩
- **Experience（经验）**：轨迹抽象 — 跨轨迹聚合、主动探索

三大核心驱动力：长程一致性、动态环境、持续学习。

## 关键方法

- **[[EvoMemory]]**（Evo-Memory）：面向自演化记忆评估的流式基准；提出 [[ReMem]] 管线（action-think-memory refine）
- **[[LightMem]]**：SLM 驱动的轻量记忆，STM/MTM/LTM（短期/中期/长期记忆）三层架构；检索延迟 83ms，F1 比 [[A-MEM]] 提升 +2.5
- **[[Emem]]**：情景式上下文重建（Episodic Context Reconstruction），从预处理转向上下文保存；master+assistant 多智能体架构；F1 54%，超越 [[GAM]] 7.75%，token 减少 >70%

## 常用基准

- **[[LoCoMo]]**：长期对话记忆（Long-term Conversation Memory）基准 — 智体记忆系统的标准评估
- **Evo-Memory benchmark**：跨 10 个数据集的流式评估

## 跨方向关联

智体记忆是 [[IntentUnderstanding]]（按用户的意图历史）和 [[IntentRecommendation]]（主动意图检测需记忆过往交互与偏好）的基础。[[PASK]] 的 DD-MM-PAS 范式明确将记忆建模与主动推荐关联。

## 关键挑战

记忆预处理导致破坏性去上下文化（De-contextualization） — 将顺序依赖压缩为静态结构（embeddings、graphs）会切断深度推理所必需的上下文完整性（[[emem]]）。