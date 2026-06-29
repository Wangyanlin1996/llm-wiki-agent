---
title: "多智能体可解释性（Multi-Agent Explainability）"
type: concept
tags: [agent-explainability, multi-agent, MAS, MARL, trust]
sources: [cema-causal-explanations-mas, triex-multi-agent-llm-explanation, counterfactual-mas-explanation, policy-explanations-marl, trism-agentic-ai]
last_updated: 2026-06-29
---

多智能体可解释性指为多智能体系统（MAS）中的协作、竞争和涌现行为生成解释的能力。多智能体环境因复杂交互、部分可观察性和行为涌现而比单 agent 解释更具挑战性。

**四种互补方法**：
- **策略摘要 + 语言解释** — [[policy-explanations-marl]]（IJCAI 2022）是 MARL 策略解释的基础工作：策略摘要（协作+任务序列）+ 语言解释（行为查询）。用户研究验证显著提升用户性能和满意度。
- **因果反事实** — [[cema-causal-explanations-mas]]（CEMA, AAMAS 2024）不假设固定因果结构，通过反事实世界模拟识别显著原因；[[counterfactual-mas-explanation]]（AXIS）让 LLM 盘问模拟器生成反事实解释。
- **三视角对齐** — [[triex-multi-agent-llm-explanation]]（TriEx, ACL 2026）用三视角工件（第一人称自我推理 + 第二人称信念状态 + 第三人称预言机审计）揭示 agent 说什么/信什么/做什么的系统性不匹配。
- **治理框架** — [[trism-agentic-ai]]（TRiSM 综述）将可解释性作为 AMAS 信任/风险/安全管理的五大支柱之一，引入 CSS 和 TUE 指标。

核心洞察：**可解释性是交互依赖属性（interaction-dependent property）**——TriEx 揭示 agent 自我叙述与信念/行为的系统性不匹配，挑战依赖 LLM 自我解释的方法。MAS 解释需多视角证据锚定。相关概念：[[AgentExplainability]]、[[CausalExplanation]]、[[AgentAccountability]]。
