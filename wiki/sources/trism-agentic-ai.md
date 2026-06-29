---
title: "TRiSM for Agentic AI: A Review of Trust, Risk, and Security Management in LLM-based Agentic Multi-Agent Systems"
type: source
tags: [agent-explainability, trust, risk, security, multi-agent, governance, survey]
date: 2025-06-04
source_file: raw/papers/trism-agentic-ai.pdf
arxiv_id: "2506.04133"
authors: ["Shaina Raza", "Ranjan Sapkota", "Manoj Karkee", "Christos Emmanouilidis"]
venue: arXiv preprint (review)
citation_count: pending
---

## Summary

本综述系统分析 LLM 多智能体系统（AMAS）中的信任、风险与安全管理（TRiSM）。将 Gartner AI TRiSM 框架适配到 Agentic AI，围绕可解释性、ModelOps、安全、隐私及生命周期治理五大支柱展开。提出 Agentic AI 风险分类法（从协调失败到提示注入对抗操纵），引入两个新指标：组件协同评分（CSS）和工具利用效能（TUE）。

## Key Claims

- **Agentic AI 与传统 AI agent 的架构区别**——多智能体配置重新定义智能、自主、协作与决策
- **TRiSM 五大支柱适配**：可解释性、ModelOps、安全、隐私、生命周期治理——均需 contextualize 到 AMAS 挑战
- **风险分类法**：协调失败、提示注入对抗操纵等 AMAS 独特威胁
- **新指标**：CSS（量化 agent 间协作质量）、TUE（评估工作流中工具使用效率）
- **可解释性改进策略**与安全/隐私增强方法（加密、对抗鲁棒性、合规）
- 研究路线图：负责任开发与部署 Agentic AI 的关键方向

## Key Quotes

> "Agentic AI systems ... are redefining intelligence, autonomy, collaboration, and decision-making across enterprise and societal domains."

> "We introduce two novel metrics: the Component Synergy Score (CSS), which quantifies the quality of inter-agent collaboration, and the Tool Utilization Efficacy (TUE)."

## Connections

- [[MultiAgentExplainability]] — TRiSM 综述系统化 MAS 可解释性
- [[AgentExplainability]] — 可解释性是 TRiSM 五支柱之一
- [[AgentAccountability]] — 生命周期治理实现问责
- [[responsible-explainable-ai-agents]] — 共识推理架构是 TRiSM 治理的具体实现
- [[LLMAutonomousAgent]] — 综述区分 agentic AI 与传统 agent 架构

## Contradictions

无已知矛盾。
