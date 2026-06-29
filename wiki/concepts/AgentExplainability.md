---
title: "Agent 可解释性（Agent Explainability）"
type: concept
tags: [agent-evaluability, explainability]
sources: [explainable-human-ai-interaction, llm-autonomous-agent-survey, agentbench, agentverse, agent-traces-to-trust, hansel-web-agent-verification, causal-past-logic-runtime-verification, three-level-llm-xai, explainable-ai-to-whom, responsible-explainable-ai-agents, blockchain-accountability-agents, argument-is-the-explanation, causal-explanations-sequential-uncertainty, trism-agentic-ai, cema-causal-explanations-mas, triex-multi-agent-llm-explanation, counterfactual-mas-explanation, policy-explanations-marl]
last_updated: 2026-06-29
---

Agent 可解释性指对 AI Agent 的推理步骤、工具使用、决策节点与闭环反馈等维度生成解释的能力，而非仅解释单步输出。[[llm-autonomous-agent-survey]] 明确将"解释"列为 agent 可信度的核心维度，并呼吁建立覆盖 agent 全生命周期的解释框架；[[explainable-human-ai-interaction]] 进一步提出"解释即规划"范式，要求 agent 解释对齐回路中人类的心智模型。[[agentbench]] 与 [[agentverse]] 的多阶段/多智能体实证则说明：agent 行为具有多阶段性，单步解释不足以诊断长程推理失败或追溯群体决策源头，解释必须沿信息转换节点展开。

Phase B 补充 14 篇真实文献后，本概念展开为四条互补主线：

**T1 信息转换可观测性** — [[ExecutionProvenance]]：[[agent-traces-to-trust]] 定义执行溯源与证据追踪分类法；[[hansel-web-agent-verification]]（HANSEL）实现交互式证据导航；[[causal-past-logic-runtime-verification]]（CPL）将运行时验证嵌入协调语言。

**T2 双受众分层解释** — [[StakeholderExplainability]]：[[explainable-ai-to-whom]] 揭示"利益相关者星座"差异化需求；[[three-level-llm-xai]] 提出三层框架（算法/领域→以人为中心→社会），LLM 担任跨层中介。

**T3 闭环验证溯因** — [[AgentAccountability]] + [[CausalExplanation]] + [[StructuredArgumentation]]：[[blockchain-accountability-agents]] 用区块链防篡改问责；[[responsible-explainable-ai-agents]] 用多模型共识治理；[[argument-is-the-explanation]] 用结构化论证实现可验证解释 + 自动幻觉检测；[[causal-explanations-sequential-uncertainty]] 基于 SCM 的因果解释基础工作。

**T4 多智能体解释** — [[MultiAgentExplainability]]：[[trism-agentic-ai]]（TRiSM 综述）系统化 MAS 可解释性治理；[[cema-causal-explanations-mas]]（CEMA）反事实因果解释；[[triex-multi-agent-llm-explanation]]（TriEx）三视角揭示说/信/做不匹配；[[counterfactual-mas-explanation]]（AXIS）LLM 盘问模拟器；[[policy-explanations-marl]] MARL 策略解释基础。

本概念承接 [[closed-loop-explainability-telecom-autonomous-networks]] 综合报告的理论需求。相关概念：[[ExplainablePlanning]]、[[LLMAutonomousAgent]]、[[ExecutionProvenance]]、[[StakeholderExplainability]]、[[CausalExplanation]]、[[StructuredArgumentation]]、[[MultiAgentExplainability]]、[[AgentAccountability]]、[[ConsensusDrivenReasoning]]。
