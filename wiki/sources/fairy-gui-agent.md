---
title: "Fairy：演化记忆 + 目标精炼驱动的鲁棒 Agent 系统"
type: source
tags: [memory-intent-clarification, evolutionary-memory, goal-refinement, GUI-agent]
sources: [fairy-gui-agent]
source_file: raw/papers/fairy-gui-agent.pdf
last_updated: 2026-06-27
arxiv_id: "2509.20729"
authors: ["Jiazheng Sun", "Ruimeng Yang", "Xu Han", "Jiayang Niu", "Mingxuan Li", "Te Yang", "Yongyong Lu", "Xin Peng"]
year: 2025
venue: null
citation_count: null
doi: "10.48550/arXiv.2509.20729"
---

## 概要
Fairy 是一个基于原则性工程框架的移动 GUI Agent，解决 Agent 系统缺乏鲁棒性、可观测性和可演化性的问题。框架包含三大组件：Runtime Goal Refinement（RGR）通过知识约束精炼 + 人在环澄清确保意图对齐；Observable Cognitive Architecture（OCA）通过组件解耦+逻辑分层+状态控制分离实现白盒可观测；Evolutionary Memory Architecture（EMA）通过执行-演化双循环实现可演化性。在模糊复杂任务基准 RealMobile-Eval 上，Fairy 超越最强 SOTA 基线 33.7%。

## 关键贡献
- Runtime Goal Refinement（RGR）：知识约束精炼 + 人在环澄清——记忆增强意图对齐的工程实现
- Evolutionary Memory Architecture（EMA）：执行-演化双循环记忆——记忆从被动存储到主动演化
- RealMobile-Eval 基准：专为模糊复杂任务设计，填补现有基准的空白
- 消融实验证实 RGR 防止意图偏差，EMA 对长期性能至关重要

## 关键引用
> "RGR ensures robustness and intent alignment via knowledge-constrained refinement and human-in-the-loop clarification" — 记忆+澄清驱动意图对齐

## 关联
- [[EvolutionaryMemoryArchitecture]] — EMA 的执行-演化双循环是记忆增强意图的新范式
- [[RuntimeGoalRefinement]] — RGR 的知识约束精炼+澄清与 [[AskBeforePlan]] 的澄清先行互补
- [[AgentMemory]] — EMA 的双循环与 Storage→Reflection→Experience 演化框架呼应
- [[MemoryForgettingStaleness]] — EMA 的演化策略与 STALE 的过期检测互补
- [[SimulationRealityGap]] — RealMobile-Eval 填补模糊任务评测空白，与 ProAgentBench 的真实数据评测呼应

## 矛盾
- 与 [[PromptBasedUncertaintyDecomposition]] 路径不同：Fairy 用工程化 RGR+EMA 架构，后者用 prompt 级不确定度分解
