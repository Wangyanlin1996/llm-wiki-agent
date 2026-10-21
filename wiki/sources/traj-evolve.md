---
title: "Traj-Evolve：肺癌早期检测患者轨迹建模的自演化多智能体系统"
type: source
tags: [multi-agent-long-context]
sources: [traj-evolve]
source_file: raw/papers/traj-evolve.pdf
last_updated: 2026-07-24
arxiv_id: "2606.02812"
authors: ["Sihang Zeng", "M. Thompson", "Ruth Etzioni", "M. Yetisgen"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
Traj-Evolve 针对纵向 EHR 需要推理稀疏、噪声和长上下文多模态序列的挑战，提出两种互补演化机制。ExPool 作为非参数记忆，索引拒绝采样推理轨迹以检索相似患者作为 few-shot 上下文；多智能体强化学习 (MARL) 通过 reward-ranked fine-tuning 参数化优化 agent 间和 agent-记忆协作。leave-one-out 交叉检索统一训练和推理行为。在肺癌预测任务上超越 9 个强基线。

## 关键贡献
- ExPool 非参数记忆：检索相似患者作为 few-shot 上下文
- MARL 参数化优化 agent 间 + agent-记忆协作
- 两种机制互补：ExPool 提升特异性，MARL 提升敏感性

## 关键引用
> "Traj-Evolve, a self-evolving multi-agent system with two complementary evolving mechanisms: an Experience Pool (ExPool) acts as a non-parametric memory, and multi-agent reinforcement learning (MARL) parametrically optimizes inter-agent and agent-memory collaboration."

## 关联
- [[MultiAgentLongContext]] — 多智能体处理长上下文 EHR 序列
- [[SelfEvolvingMAS]] — 自演化多智能体系统
- [[NonParametricMemory]] — 非参数记忆机制

## 矛盾
- (暂无)
