---
title: '多 Agent 工具调用的有状态推理'
type: source
tags:
- cache-reuse
- kv-cache
- stateful-inference
- multi-agent
- tool-calling
sources:
- stateful-inference-multi-agent
source_file: raw/papers/stateful-inference-multi-agent.pdf
last_updated: 2026-07-09
arxiv_id: '2605.26289'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
多 agent 工具调用成为主导交互模式，但现有推理框架将每个工具调用视为独立请求——从头重新处理整个对话，即使 85-95% 的 prompt 与上一轮相同。本文将有状态推理架构从 O(n_t) per-turn 成本转为 O(Δ_t) delta-only 成本。

## 关键贡献
- 从 O(n_t) per-turn 成本转为 O(Δ_t) delta-only 成本
- 持久 KV cache 跨轮存活，仅摄入新 token 前进
- Radix prefix cache 扩展到交错多 agent 流量
- Prompt-lookup speculative decoder 加速结构化输出
- 6 轮 agent 工作流每轮 2.1x 更快，35 轮中位数轮 4.2x，端到端时间减半

## 方法细节
- **Delta-only 推理**：每轮只处理新增 token（工具输出+新指令），不重新处理已有对话——从 O(n_t) 降为 O(Δ_t)，其中 Δ_t ≪ n_t
- **持久 KV cache**：KV cache 跨轮次存活在 GPU 内存中——下一轮直接追加新 token 的 KV，不重新计算
- **Radix prefix cache 扩展**：标准 radix prefix cache 为单流设计，本文扩展到交错多 agent 流量——多个 agent 的 KV cache 共存，按 radix tree 组织
- **Prompt-lookup speculative Decoder**：工具调用输出通常是结构化的（JSON、代码）——用 prompt-lookup 推测解码（输入中查找与输出匹配的 n-gram）加速结构化输出生成

## 关键引用
> "Stateful inference reduces per-turn cost from O(n_t) to O(Δ_t) — only new tokens are ingested, 85-95% of the prompt is shared."

## 关联
- [[CacheReuse]] — 缓存复用方向
- [[TokenDance]] — TokenDance 做跨 agent KV 共享，本文做跨轮 KV 复用
- [[PRISMSchedulingMemory]] — PRISM 做调度-缓存协同，本文做有状态 KV 复用
- [[Leyline]] — Leyline 做缓存编辑，本文做缓存持久化

## 矛盾
- 与"每轮独立推理"的矛盾：85-95% 的 prompt 是共享的，有状态复用能 4.2x 加速
