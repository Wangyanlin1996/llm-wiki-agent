---
title: 'MASPO: 多 Agent 系统的联合 Prompt 优化'
type: source
tags:
- prompt-optimization
- multi-agent
- joint-optimization
sources:
- maspo-joint-mas-prompt
source_file: raw/papers/maspo-joint-mas-prompt.pdf
last_updated: 2026-07-09
arxiv_id: '2605.06623'
authors:
- et al.
year: 2026
venue: ICML 2026
citation_count: 0
---
## 概要
LLM 多 agent 系统中 agent 通过角色特定 prompt 编排，prompt 质量关键但跨交互 agent 联合优化非常困难——局部 agent 目标与全局系统目标不对齐。MASPO 自动迭代优化整个系统的 prompt，核心创新是联合评估机制。

## 关键贡献
- 自动迭代优化整个 MAS 的 prompt——而非逐 agent 独立优化
- 联合评估机制——不只看 prompt 的局部有效性，而看其促进下游 agent 成功的能力
- 弥合局部交互与全局结果的鸿沟，无需 ground-truth 标签
- 数据驱动进化 beam search 高效导航高维 prompt 空间
- 6 个任务上平均准确率提升 2.9

## 方法细节
- **联合评估机制**：评估一个 agent 的 prompt 时，不只看该 agent 的直接输出质量，而看其对下游 agent 成功的促进程度——例如 planner 的 prompt 好不好取决于 executor 能否成功执行其计划
- **无需 ground-truth**：利用 agent 间的交互信号作为隐式监督，不需要任务的标准答案
- **进化 Beam Search**：维护多个 prompt 候选集合（beam），每轮变异+评估+筛选，高效搜索高维联合 prompt 空间

## 关键引用
> "MASPO's joint evaluation mechanism measures not just local prompt effectiveness, but the ability to promote downstream agent success."

## 关联
- [[PromptOptimization]] — Prompt 优化方向
- [[PromptCodebooks]] — PCO 做 per-instance 路由，MASPO 做 multi-agent 联合优化
- [[SPEAR]] — SPEAR 单 agent 优化器，MASPO 多 agent 联合优化

## 矛盾
- 与"逐 agent 独立优化"的矛盾：MASPO 表明局部最优不等于全局最优
