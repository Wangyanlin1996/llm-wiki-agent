---
title: "Ensemble QSP：层次记忆架构突破长程多智能体建模上下文限制"
type: source
tags: [multi-agent-long-context]
sources: [ensemble-qsp]
source_file: raw/papers/ensemble-qsp.pdf
last_updated: 2026-07-24
arxiv_id: "2607.07666"
authors: ["Shivendra G. Tewari", "H. Kimko"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
Ensemble QSP 是一个多智能体框架，采用三层层次记忆架构，通过限制每个状态类别容量并驱逐已完成工作，使注入上下文保持有界且在项目持续时间内恒定（中期项目状态中位数 301 tokens，最大 4,050，跨 104 次运行）。系统在领域专家 PI agent 下编排五个专家 worker agent，通过物理检查清单和结构化领域知识强制物理约束。实现了无需人工干预的自主药代动力学模型选择。

## 关键贡献
- 三层层次记忆架构：上下文有界（中位 301 tokens），不随项目时长增长
- 5 specialist worker agents + PI agent 编排，物理约束强制
- 跨低成本和前沿 LLM 的一致结果质量，领域无关架构

## 关键引用
> "A three-layer hierarchical memory architecture that keeps injected context bounded and constant in project duration (mid-term project state: median 301 tokens, max 4,050, across 104 runs)."

## 关联
- [[MultiAgentLongContext]] — 多智能体长程任务的上下文限制突破
- [[HierarchicalMemory]] — 层次记忆架构
- [[BoundedContextManagement]] — 有界上下文管理

## 矛盾
- (暂无)
