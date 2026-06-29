---
title: "Agent 问责架构（Agent Accountability Architecture）"
type: concept
tags: [agent-explainability, accountability, blockchain, consensus, governance]
sources: [blockchain-accountability-agents, responsible-explainable-ai-agents, agent-traces-to-trust, trism-agentic-ai, argument-is-the-explanation]
last_updated: 2026-06-29
---

Agent 问责架构指为自主 agent 的行为提供不可篡改的行为记录、决策理据审计和责任执行机制的系统设计。问责是可解释性的前提——没有可靠的执行记录，解释就无从验证。

**三种实现路径**：
- **区块链防篡改问责** — [[blockchain-accountability-agents]] 用区块链技术实现 ROS 移动机器人的黑箱问责组件，确保行为记录不可被事后修改；LLM 从问责数据生成自然语言解释。
- **共识驱动推理治理** — [[responsible-explainable-ai-agents]] 用多模型共识架构：异构 LLM/VLM 独立生成 → 显式暴露分歧 → 推理 agent 结构化整合。责任通过集中式推理层控制和 agent 级约束实现。
- **可验证论证问责** — [[argument-is-the-explanation]] 用结构化论证图使每步推理可独立检查，事实节点攻击论证实现自动幻觉检测。

**治理框架**：[[trism-agentic-ai]]（TRiSM）将问责纳入 AMAS 五大支柱的生命周期治理；[[agent-traces-to-trust]] 综述将执行溯源与证据追踪统一为过程级问责的基础。

核心洞察：**问责 = 不可篡改记录 + 可审计理据 + 责任执行**。区块链确保记录完整性，共识推理确保决策透明性，结构化论证确保推理可验证性。相关概念：[[AgentExplainability]]、[[ExecutionProvenance]]、[[ConsensusDrivenReasoning]]。
