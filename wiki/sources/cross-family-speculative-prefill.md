---
title: 'Cross-Family Speculative Prefill: 跨族推测式预填充'
type: source
tags:
- context-optimization
- speculative-prefill
- prompt-compression
sources:
- cross-family-speculative-prefill
source_file: raw/papers/cross-family-speculative-prefill.pdf
last_updated: 2026-07-09
arxiv_id: '2603.02631'
authors:
- et al.
year: 2026
venue: ICLR 2026 Workshop
citation_count: 0
---
## 概要
Agentic LLM 工作流中重复推理步骤和多调用循环导致 prompt prefill 成本高。现有 speculative prefill 方法用注意力估计 token 重要性做免训练 prompt 压缩，但假设 draft 模型与 target 模型共享 tokenizer——实际 agent 管线经常使用没有同族小模型的异构模型栈。本文研究跨模型族 speculative prefill 的可行性。

## 关键贡献
- 首次研究跨模型族 speculative prefill——用一个模型族的轻量 draft 模型为不同族的 target 模型做 prompt 压缩
- 在 Qwen/LLaMA/DeepSeek 多种组合上实验验证
- 发现基于注意力的 token 重要性估计能可靠跨族迁移
- 保留 90-100% 全 prompt 基线性能，TTFT 大幅降低

## 方法细节
- **注意力估计**：用 draft 模型前向传播获取各 token 的注意力分数，作为重要性估计
- **跨族迁移**：尽管 draft 和 target 模型架构、tokenizer 不同，注意力模式反映的 token 重要性具有跨族一致性
- **Token 剪枝**：根据注意力分数排序，保留 top-k token 作为压缩 prompt 送入 target 模型
- **免训练**：不需要任何训练数据或微调，纯推理时操作

## 关键引用
> "Attention-based token importance estimates transfer reliably across model families, despite architectural and tokenizer differences."

## 关联
- [[ContextOptimization]] — 上下文优化方向
- [[CoACT]] — CoACT 训练专用压缩器，本文用免训练注意力估计
- [[SpeculativeDecoding]] — 推测解码的相关概念

## 矛盾
- 挑战"speculative prefill 需要同族模型"的假设——跨族同样有效
