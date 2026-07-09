---
title: 'Leyline: Agentic 推理的 KV 缓存指令'
type: source
tags:
- cache-reuse
- kv-cache
- cache-editing
- rope-correction
sources:
- leyline-kv-directives
source_file: raw/papers/leyline-kv-directives.pdf
last_updated: 2026-07-09
arxiv_id: '2606.01065'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
现代 KV cache 管理假设 chatbot 工作负载——prompt 到达一次、缓存仅追加增长。Agentic LLM 打破假设：失败工具调用重试、过期输出丢弃、轨迹转向——相同内容移到新位置使精确前缀缓存失效。Leyline 用声明式指令分离"编辑什么"与"如何保持位置正确"。

## 关键贡献
- 声明式指令 4-tuple 分离"编辑什么"与"如何保持位置正确"
- 支持两种编辑模式：in-place splice 和 prefix-trimmed re-prefill
- 架构无关接口通过闭式 RoPE 旋转校正恢复注意力数学
- Splice kernel 提升 replay cache-hit +11.2pp，延迟降 241ms
- 十行截断规则提升 agentic solve rate +14.3pp（debug-gym）

## 方法细节
- **声明式指令 4-tuple**：(what, where, mode, constraint)
  - what：编辑什么内容（删除/替换/插入）
  - where：编辑位置（哪些 KV block）
  - mode：编辑模式（in-place splice 或 prefix-trimmed re-prefill）
  - constraint：约束条件（如保持语义不变）
- **In-place Splice**：在缓存中原地替换/删除 KV block——适用于语义等价的替换
- **Prefix-trimmed Re-prefill**：截断受影响的前缀部分，重新 prefill——适用于语义遗忘
- **闭式 RoPE 旋转校正**：编辑后 KV block 的位置编码需要调整——通过闭式 RoPE（Rotary Position Embedding）旋转校正恢复注意力数学正确性
- **架构无关接口**：指令接口与模型架构无关，路由到每架构的专用内核实现

## 关键引用
> "Leyline separates 'what to edit' from 'how to keep positions correct' — closed-form RoPE rotation restores attention math."

## 关联
- [[CacheReuse]] — 缓存复用方向
- [[SAECache]] — SAECache 做缓存淘汰，Leyline 做缓存编辑
- [[TokenDance]] — TokenDance 做多 agent 间 KV 共享，Leyline 做单 agent 内 KV 编辑
- [[VeriCache]] — VeriCache 做无损压缩，Leyline 做有损编辑但保证注意力正确

## 矛盾
- 与"缓存仅追加增长"的假设矛盾：Agentic 工作负载需要主动编辑缓存
