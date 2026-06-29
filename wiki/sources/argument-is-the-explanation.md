---
title: "The Argument is the Explanation: Structured Argumentation for Trust in Agents"
type: source
tags: [agent-explainability, structured-argumentation, trust, multi-agent, hallucination-detection]
date: 2025-10-03
source_file: raw/papers/argument-is-the-explanation.pdf
arxiv_id: "2510.03442"
authors: ["Ege Cakar", "Per Ola Kristensson"]
venue: arXiv preprint (submitted to IAAI-26)
citation_count: pending
---

## Summary

本文主张 AI 可解释性应遵循人类社会原则：人类是黑箱，但社会通过评估可验证的论证运转。提出使用结构化论证（structured argumentation）提供解释和验证层级——既非机械可解释性也非 LLM 生成解释所能达到。管线将 LLM 文本转化为论证图，在每步推理上启用验证。在 AAEC 数据集上达 94.44 macro F1（+5.7），AMT 上达 0.81 macro F1（+~0.07）。使用 Bipolar ABA 捕获支持/攻击关系，通过事实节点攻击论证实现自动幻觉检测。

## Key Claims

- **"论证即解释"**——利益相关者需要可验证的推理链，而非机械透明性
- **结构化论证提供 LLM 生成解释无法达到的验证层级**：每步推理可独立检查
- **Bipolar Assumption-Based Argumentation** 捕获支持/攻击关系 → 自动幻觉检测（事实节点攻击论证）
- **验证机制支持测试时反馈迭代精炼**——无需重训练
- 多 agent 风险评估演示：专业 agent 透明协作完成风险评估
- SOTA: AAEC 94.44 macro F1 (+5.7), AMT 0.81 macro F1 (+~0.07)

## Key Quotes

> "Humans are black boxes -- we cannot observe their neural processes, yet society functions by evaluating verifiable arguments. AI explainability should follow this principle."

> "Stakeholders need verifiable reasoning chains, not mechanistic transparency."

> "Enabling automatic hallucination detection via fact nodes attacking arguments."

## Connections

- [[StructuredArgumentation]] — 本论文是该概念的核心实现
- [[AgentExplainability]] — 论证式解释是 agent 可解释性的新范式
- [[AgentAccountability]] — 可验证推理链增强问责
- [[MultiAgentExplainability]] — 多 agent 风险评估中透明协作
- [[responsible-explainable-ai-agents]] — 两者都关注可信 agent 架构

## Contradictions

- 与"机械可解释性"范式形成张力：本文认为机械透明性不是正确的解释方向，可验证论证才是
- 与"LLM 生成解释"范式形成张力：本文认为自由文本解释不可验证，需结构化论证
