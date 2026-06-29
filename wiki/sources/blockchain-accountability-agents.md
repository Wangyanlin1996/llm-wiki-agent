---
title: "Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models"
type: source
tags: [agent-explainability, blockchain, accountability, robotics, LLM-explanation]
date: 2024-03-14
source_file: raw/papers/blockchain-accountability-agents.pdf
arxiv_id: "2403.09567"
authors: ["Laura Fernández-Becerra", "Miguel Ángel González-Santamarta", "Ángel Manuel Guerrero-Higueras", "Francisco Javier Rodríguez-Lera", "Vicente Matellán Olivera"]
venue: arXiv preprint
citation_count: pending
---

## Summary

本文提出面向 ROS 移动机器人的问责与可解释性架构，含两大组件：(1) 黑箱式问责组件——通过区块链技术实现防篡改；(2) 自然语言解释组件——利用 LLM 从黑箱数据生成解释。在三个自主导航场景中评估，证明即使面对自主 agent 在真实场景中的挑战，仍能从机器人动作的问责数据中获得连贯、准确、可理解的解释。

## Key Claims

- **自主 agent 部署在人机交互环境中引发安全关切**——理解事件背后的情况变得关键
- **区块链提供防篡改问责**——黑箱记录不可被事后修改
- **LLM 从问责数据生成自然语言解释**——弥合 agent 与用户之间的沟通鸿沟
- 解释增强信任与安全，作为预防故障、错误和误解的措施
- 三场景评估：问责和可解释性指标均证明方法有效性

## Key Quotes

> "Understanding the circumstances behind an event becomes critical, requiring the development of capabilities to justify their behaviors to non-expert users."

> "A black box-like element to provide accountability, featuring anti-tampering properties achieved through blockchain technology."

## Connections

- [[AgentAccountability]] — 区块链问责是问责架构的技术实现
- [[AgentExplainability]] — LLM 从问责数据生成解释
- [[ExecutionProvenance]] — 黑箱问责是执行溯源的物理实现
- [[responsible-explainable-ai-agents]] — 两者互补：区块链问责 + 共识推理

## Contradictions

无已知矛盾。
