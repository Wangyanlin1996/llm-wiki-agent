---
title: "认知记忆机制（Cognitive Memory Mechanism）"
type: concept
tags: [memory-intent-clarification, cognitive-memory]
sources: [cops, janus]
last_updated: 2026-06-27
---

认知记忆机制是指受人类认知科学启发的层次化记忆架构，用于增强 LLM Agent 的意图理解能力。典型三层结构：感觉记忆（快速感知响应）、工作记忆（复杂认知处理）、长期记忆（历史交互存储）。

[[cops]]（CoPS）首次将认知三阶记忆应用于个性化搜索意图理解——从历史交互构建用户画像驱动个性化查询意图排序。[[janus]]（JANUS）在机器人辅助场景中使用类似的持久记忆三层（近期缓冲+核心记忆+归档检索）从欠明确请求中恢复，并用内部言语触发澄清。两者共同表明：层次化认知记忆结构比平面检索更有效地增强模糊意图理解。与 [[AgentMemory]] 的 Storage→Reflection→Experience 演化框架互补——后者强调时间演化，认知记忆强调功能分层。
