---
title: "多智能体 KV Cache 共享（Multi-Agent KV Cache Sharing）"
type: concept
tags: [multi-agent-long-context]
sources: [aaflow-plus, agent-primitives, sidequest, twin-agent]
last_updated: 2026-07-24
---

多智能体 KV Cache 共享是一种系统级优化策略，通过在多智能体系统间复用 KV cache 来避免重复计算长上下文的 prefill。AAFLOW+ 将 KV cache 提升为一等分布式对象，提供物化/传输/fork/组合/驱逐算子，实现零拷贝跨 agent 复用。Agent Primitives 通过 KV cache 内部通信替代自然语言传递，缓解长上下文多阶段交互中的信息退化。SideQuest 利用 LRM 自身推理 token 有用性来压缩 KV cache。Twin Agent 通过上下文残差压缩仅传递紧凑 hint。关键发现：在中等至高带宽网络上，KV 传输优于重新计算。相关论文：[[aaflow-plus]], [[agent-primitives]], [[sidequest]], [[twin-agent]]
