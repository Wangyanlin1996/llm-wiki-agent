---
title: "SIMAS：单 LLM 驱动多智能体系统的扩展行为"
type: source
tags: [multi-agent-long-context]
sources: [simas]
source_file: raw/papers/simas.pdf
last_updated: 2026-07-24
arxiv_id: "2606.00655"
authors: ["Jialin Li", "Zhouhong Gu", "Yin Cai", "Hongwei Feng"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
本文系统研究同质 MAS 性能随 agent 数量增加如何演化，提出 SIMAS 框架（顺序迭代多智能体系统）清晰观察扩展效应。关键发现：MAS 性能不随 agent 数单调提升而是递减回报模式，由协作协同与协调开销之间的权衡决定。性能退化源于协调开销而非仅仅是长上下文失败。有效 MAS 需要足够强大的基础 LLM，任务类型关键调节最优 agent 数，集体智能是策略性交互设计的涌现属性而非 agent 数量的保证结果。

## 关键贡献
- SIMAS 框架：顺序迭代 MAS 隔离协作变量观察扩展效应
- 发现 MAS 扩展定律：递减回报模式，非单调提升
- 协调开销 vs 长上下文失败的归因分析

## 关键引用
> "MAS performance does not scale monotonically with agent count but follows a pattern of diminishing returns, governed by a trade-off between collaborative synergy and coordination overhead."

## 关联
- [[MultiAgentLongContext]] — 多智能体扩展行为分析
- [[MASScalingLaw]] — 多智能体扩展定律
- [[CoordinationOverhead]] — 协调开销分析

## 矛盾
- (暂无)
