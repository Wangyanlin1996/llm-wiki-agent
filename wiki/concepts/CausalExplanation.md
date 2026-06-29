---
title: "因果解释（Causal Explanation）"
type: concept
tags: [agent-explainability, causal, counterfactual, SCM, sequential-decision]
sources: [causal-explanations-sequential-uncertainty, cema-causal-explanations-mas, counterfactual-mas-explanation]
last_updated: 2026-06-29
---

因果解释指基于结构因果模型（SCM）或反事实模拟，为 agent 的序贯决策提供"为什么"的因果回答（而非仅相关性）的方法。

**单 agent 基础**：[[causal-explanations-sequential-uncertainty]] 引入基于 SCM 的随机序贯决策因果解释框架，单一框架可识别多个语义不同的解释——此前不可能。建立 MDP 上因果推理的精确方法和近似技术。

**多 agent 扩展**：[[cema-causal-explanations-mas]]（CEMA）将因果解释扩展到动态序贯多智能体系统。不假设固定因果结构，仅需要前向模拟的概率模型，通过反事实世界模拟识别显著原因。用户研究验证对自动驾驶信任有积极影响。

**LLM 增强**：[[counterfactual-mas-explanation]]（AXIS）让 LLM 用"whatif"/"remove"提示盘问环境模拟器，多轮综合反事实信息生成以人为中心的 MAS 动作解释。解释正确性 +7.7%，目标预测 +23%。

核心洞察：**因果解释从"假设固定因果结构"演进到"仅需前向模拟"再到"LLM 盘问模拟器"**——适用性逐步扩大，从单 agent 到多 agent，从概率模型到 LLM 交互。相关概念：[[AgentExplainability]]、[[MultiAgentExplainability]]、[[ExplainablePlanning]]。
