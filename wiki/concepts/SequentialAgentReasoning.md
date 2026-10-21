---
title: "顺序智能体推理（Sequential Agent Reasoning）"
type: concept
tags: [multi-agent-long-context]
sources: [chain-of-agents, lstm-mas, cosmir, chow-liu-coa]
last_updated: 2026-07-24
---

顺序智能体推理是一种多智能体长上下文处理范式，将长输入分解为分段，由多个 worker agent 顺序处理，每个 agent 读取分段并更新有界共享记忆，最后由 manager agent 综合输出。Chain-of-Agents (CoA) 是该范式的奠基性工作，COSMIR 用结构化记忆替代自由文本传递以减少信息损失，LSTM-MAS 引入 LSTM 门控机制（worker/filter/judge/manager 对应 input/forget/CEC/output gate）实现受控信息传输。Chow-Liu 排序进一步优化了分段处理顺序以最小化信息瓶颈。相关论文：[[chain-of-agents]], [[lstm-mas]], [[cosmir]], [[chow-liu-coa]]
