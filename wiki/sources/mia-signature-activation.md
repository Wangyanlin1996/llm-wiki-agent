---
title: 'MiA-Signature: 全局激活签名压缩'
type: source
tags:
- context-optimization
- activation-compression
- rag
sources:
- mia-signature-activation
source_file: raw/papers/mia-signature-activation.pdf
last_updated: 2026-07-09
arxiv_id: '2605.06416'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
认知科学表明意识访问与全局点火（global ignition）相关，但个体无法直接访问所有激活内容——LLM 系统也面临类似张力：全局激活影响下游处理，但完整激活状态计算上不可行。本文提出 Mindscape Activation Signature (MiA-Signature)——查询诱导的全局激活模式的压缩表示。

## 关键贡献
- 提出 MiA-Signature——查询诱导的全局激活模式的压缩表示
- 用次模函数选择覆盖激活上下文空间的高层概念
- 可选通过工作记忆轻量迭代更新
- MiA-Signature 作为条件信号近似全激活状态效果，计算上可处理
- 集成到 RAG 和 agent 系统，在多个长上下文理解任务上一致提升

## 方法细节
- **查询诱导**：给定查询，激活模式由查询与上下文的交互决定，MiA-Signature 捕获这一交互模式
- **次模函数选择**：用次模函数（submodular function）从高层概念空间中选择覆盖激活上下文空间的子集——次模性保证贪心算法近似最优
- **工作记忆更新**：可选地通过轻量工作记忆模块迭代更新签名，适应对话演进
- **条件信号**：MiA-Signature 作为条件信号注入后续推理，近似全激活状态的效果

## 关键引用
> "MiA-Signature serves as a conditioning signal approximating the effect of the full activation state, while being computationally tractable."

## 关联
- [[ContextOptimization]] — 上下文优化方向
- [[LatentContextCompilation]] — 同为上下文压缩为紧凑表示，但机制不同：LoRA 编译 vs 次模选择
- [[RAG]] — 集成到 RAG 系统验证效果

## 矛盾
- 与"保留原始 token"类方法的矛盾：MiA-Signature 将上下文转换为激活签名，不保留原始文本
