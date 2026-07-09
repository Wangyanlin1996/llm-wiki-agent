---
title: 'Prompt Codebooks: 离散本能词汇表上的 Prompt 优化'
type: source
tags:
- prompt-optimization
- discrete-optimization
- per-instance-routing
sources:
- prompt-codebooks-pco
source_file: raw/papers/prompt-codebooks-pco.pdf
last_updated: 2026-07-09
arxiv_id: '2605.28360'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
现有自动 prompt 优化将每个任务的 prompt 视为整体性、实例无关的字符串，通过全局编辑优化——产生脆弱更新且无法复用已学习的子行为。PCO 将 prompt 优化重新表述为有限自然语言"本能"词汇表上的离散学习。

## 关键贡献
- 将 prompt 优化重新表述为离散 codebook 上的学习——每个"本能"是一个自然语言片段
- Per-instance 路由使不同输入获得不同本能组合
- 编码器、生成器和 codebook 在 min-max 目标下联合训练
- 6 个基准上比零样本 +30.36pp，比 GEPA +3.34，prompt 长度比 MIPROv2 缩短 14.1x

## 方法细节
- **离散 Codebook**：维护一个有限的自然语言"本能"词汇表，每个本能是一个可复用的 prompt 子行为描述
- **LLM 编码器**：将每个输入实例路由到 codebook 中的少量条目子集——不同实例激活不同本能组合
- **生成器**：将选中的本能条目组合为完整 prompt，输入冻结的目标模型
- **批评者**：发出按归因分解的每变量文本梯度——指出哪个本能需要改进
- **Min-Max 目标**：语言值 min-max 优化——最大化最差实例的性能，保证鲁棒性

## 关键引用
> "PCO reformulates prompt optimization as discrete learning over a finite vocabulary of natural language 'instincts'."

## 关联
- [[PromptOptimization]] — Prompt 优化方向
- [[APEX]] — APEX 优化数据选择，PCO 优化 prompt 结构
- [[MASPO]] — MASPO 做 multi-agent 联合优化，PCO 做 per-instance 路由优化

## 矛盾
- 与"实例无关的全局 prompt"假设的矛盾：PCO 表明 per-instance 路由显著优于全局 prompt
