---
title: "共识驱动推理（Consensus-Driven Reasoning）"
type: concept
tags: [agent-explainability, consensus, multi-model, responsible-ai, governance]
sources: [responsible-explainable-ai-agents]
last_updated: 2026-06-29
---

共识驱动推理指通过异构模型的独立生成、显式分歧暴露和结构化整合，为 agentic workflow 提供可审计、有证据支撑的决策的架构模式。

**核心机制**（[[responsible-explainable-ai-agents]]）：
1. **独立生成** — 异构 LLM/VLM agent 联盟从共享输入独立生成候选输出
2. **分歧暴露** — 显式暴露不确定性、分歧和替代解释
3. **结构化整合** — 专用推理 agent 强制安全/策略约束，缓解幻觉和偏见
4. **可审计输出** — 保留中间输出 + 跨模型比较 = 可解释性

**与单模型解释的区别**：共识架构不依赖单一模型的自我解释（[[triex-multi-agent-llm-explanation]] 揭示自我叙述与信念/行为的系统性不匹配），而是通过跨模型比较提供外部验证。可解释性来自过程透明（保留中间输出）而非事后解释。

核心洞察：**共识驱动 = 多模型独立 + 分歧显式化 + 集中推理治理**。责任通过集中式推理层控制和 agent 级约束实现，而非依赖个体模型的善意。相关概念：[[AgentExplainability]]、[[AgentAccountability]]、[[MultiAgentExplainability]]、[[trism-agentic-ai]]。
