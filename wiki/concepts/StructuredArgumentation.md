---
title: "结构化论证解释（Structured Argumentation for Explanation）"
type: concept
tags: [agent-explainability, argumentation, verification, trust, hallucination-detection]
sources: [argument-is-the-explanation]
last_updated: 2026-06-29
---

结构化论证解释指将 LLM 文本转化为论证图（argument graph），在每步推理上启用独立验证，从而提供机械可解释性和 LLM 自由文本解释都无法达到的验证层级。

**核心主张**：[[argument-is-the-explanation]] 提出"论证即解释"——人类是黑箱，但社会通过评估可验证论证运转。AI 可解释性应遵循此原则：利益相关者需要可验证的推理链，而非机械透明性。

**技术实现**：
- LLM 文本 → 论证图（AAEC 94.44 macro F1, AMT 0.81 macro F1，均超 SOTA）
- Bipolar Assumption-Based Argumentation 捕获支持/攻击关系
- **自动幻觉检测**：事实节点攻击论证，自动识别无支撑声明
- **测试时反馈迭代精炼**：无需重训练即可改进
- 多 agent 风险评估演示：专业 agent 透明协作

核心洞察：**可验证论证 > 机械透明性 > LLM 自由文本解释**。论证图使每步推理可独立检查，幻觉可被自动检测。相关概念：[[AgentExplainability]]、[[AgentAccountability]]、[[MultiAgentExplainability]]。
