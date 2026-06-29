---
title: "LLM 自主智能体（LLM Autonomous Agent）"
type: concept
tags: [agent-evaluability, LLM-agent, architecture]
sources: [llm-autonomous-agent-survey, agentbench, agentverse]
last_updated: 2026-06-29
---

LLM 自主智能体指以大语言模型为核心、具备感知—规划—记忆—工具使用—行动闭环的自主系统。[[llm-autonomous-agent-survey]] 提出涵盖既往大部分工作的统一架构框架，将 agent 构造拆解为感知、规划、记忆、工具使用等模块；[[agentbench]] 为此类 agent 的多阶段能力（推理、规划、工具调用、长程决策）提供 8 环境评测基准；[[agentverse]] 则将单 agent 扩展为可动态重组的多智能体协作群体，揭示社会行为涌现。

该概念是本知识库 Agent 方向的架构基底，连接 [[AgentMemory]]（记忆模块）、[[IntentUnderstanding]]（感知/意图理解模块）与 [[AgentExplainability]]（可信度/解释维度）。agent 行为的多阶段性正是"解释必须沿信息转换节点展开"的实证基础。
