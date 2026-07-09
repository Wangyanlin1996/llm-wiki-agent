---
title: 'Latent Context Compilation: 潜在上下文编译'
type: source
tags:
- context-optimization
- lora
- long-context
sources:
- latent-context-compilation
source_file: raw/papers/latent-context-compilation.pdf
last_updated: 2026-07-09
arxiv_id: '2602.21221'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
长上下文 LLM 部署面临两难：分摊式压缩（amortized compression）对 OOD 泛化差；Test-Time Training 需要合成数据且修改模型权重，产生有状态参数阻碍并发服务。本文从"适应"转向"编译"——用 disposable LoRA 模块作为编译器，将长上下文蒸馏为紧凑的 buffer token（无状态、可移植的记忆制品）。

## 关键贡献
- 从"适应"（adaptation）到"编译"（compilation）的范式转换——生成无状态、可移植的记忆制品
- 用 disposable LoRA 模块作为编译器，将长上下文蒸馏为 buffer token
- 自对齐优化策略：用 context-agnostic 的随机查询正则化上下文重建任务
- 迫使压缩 token 停留在模型已有的指令遵循流形中，无需合成 QA 对
- Llama-3.1-8B 上 16x 压缩比仍保持细粒度细节和推理能力

## 方法细节
- **Disposable LoRA 编译器**：为每个长上下文实例化一个临时 LoRA 模块，训练它将上下文压缩为少量 buffer token
- **自对齐优化**：不使用合成 QA 对，而是用随机查询（context-agnostic）正则化重建任务——确保 buffer token 能响应任意查询而非过拟合特定问题
- **流形约束**：随机查询迫使压缩 token 不会偏离模型已有的指令遵循流形，保持泛化能力
- **无状态制品**：编译后的 buffer token 可跨请求复用，LoRA 模块用完即弃

## 关键引用
> "We shift from adaptation to compilation — producing stateless, portable memory artifacts."

## 关联
- [[ContextOptimization]] — 上下文优化方向
- [[CoACT]] — CoACT 用动作保持训练压缩器，本文用自对齐训练 LoRA 编译器
- [[MiASignature]] — 同为激活压缩，但 MiA 用次模函数选择概念而非 LoRA 编译

## 矛盾
- 与 Test-Time Training 的矛盾：TTT 修改模型权重产生有状态参数，本文强调无状态制品
