---
title: "多智能体长上下文建模（Multi-Agent Long Context Modeling）"
type: concept
tags: [multi-agent-long-context]
sources: [chain-of-agents, graph-of-agents, lstm-mas, cosmir, chow-liu-coa, memagent-long-context, simas]
last_updated: 2026-07-24
---

多智能体长上下文建模是一种利用多个 LLM agent 协作处理超出单一模型上下文窗口限制的长输入的范式。核心思路是将长文本分解为分段，由不同 agent 分别处理，再通过共享记忆、结构化通信或递归委派进行信息聚合。代表性框架包括 Chain-of-Agents (CoA) 的顺序链式处理、Graph of Agents (GoA) 的信息论优化动态协作图、LSTM-MAS 的门控机制链式架构。关键挑战包括信息瓶颈与压缩损失、错误累积与幻觉传播、agent 间通信效率、以及扩展时的递减回报。相关论文：[[chain-of-agents]], [[graph-of-agents]], [[lstm-mas]], [[cosmir]], [[chow-liu-coa]], [[memagent-long-context]], [[simas]]
