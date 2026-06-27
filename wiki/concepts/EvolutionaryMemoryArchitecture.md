---
title: "演化记忆架构（Evolutionary Memory Architecture）"
type: concept
tags: [memory-intent-clarification, evolutionary-memory]
sources: [fairy-gui-agent]
last_updated: 2026-06-27
---

演化记忆架构（EMA）是指通过执行-演化双循环实现记忆主动演化的架构设计。执行循环处理当前任务，演化循环从执行经验中提取、更新和遗忘记忆，使 Agent 在长期交互中持续改进意图理解能力。

[[fairy-gui-agent]]（Fairy）提出 EMA 作为其三大框架之一，消融实验证实 EMA 对长期性能至关重要。与 [[AgentMemory]] 的 Storage→Reflection→Experience 演化框架呼应——后者描述记忆的时间演化阶段，EMA 提供工程化的双循环实现。与 [[MemoryForgettingStaleness]]（STALE, ScrapMem）互补——后者关注记忆的过期和遗忘，EMA 关注记忆的主动演化和更新。与 [[ProceduralMemory]]（Memp）的程序性记忆蒸馏形成对比——EMA 是通用记忆演化，Memp 是"如何做"技能的专门蒸馏。
