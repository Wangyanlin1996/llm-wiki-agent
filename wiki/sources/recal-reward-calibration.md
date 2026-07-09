---
title: 'ReCal: RL 路由的奖励校准'
type: source
tags:
- model-routing
- reward-calibration
- reinforcement-learning
- credit-assignment
sources:
- recal-reward-calibration
source_file: raw/papers/recal-reward-calibration.pdf
last_updated: 2026-07-09
arxiv_id: '2606.12479'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
RL-based 路由通过交互反馈优化路由策略，但在难度异构的任务下难以提供信息丰富且可比较的学习信号。多目标（正确性、格式行为）聚合为单一标量奖励导致模糊信用分配和冲突优化信号；奖励信号跨实例变异性大引入优化偏差偏向平凡样本。ReCal 提出分层奖励分解机制和分布感知优化策略。

## 关键贡献
- 分层奖励分解机制——解决多目标聚合的模糊信用分配
- Component-wise advantage estimation——分离各奖励分量的优势
- 分布感知优化策略——方差感知重加权和 per-dataset 标准化
- 7 个数据集上一致提升路由性能和训练稳定性

## 方法细节
- **分层奖励分解**：
  - 将多目标奖励（正确性、格式行为等）分解为分层组件
  - 每个组件独立计算优势（advantage）——而非聚合后计算
  - 避免一个目标的噪声淹没另一个目标的信号
- **Component-wise Advantage Estimation**：
  - 对每个奖励分量分别估计优势函数
  - 组合时加权而非简单求和——权重反映各分量的信息量
- **分布感知优化**：
  - **方差感知重加权**：高方差样本（难度极端的）权重降低，低方差样本（中等难度）权重提高——避免优化偏向平凡样本
  - **Per-dataset 标准化**：不同数据集的奖励尺度不同——标准化到可比范围，避免大数据集主导优化

## 关键引用
> "ReCal decomposes multi-objective rewards hierarchically and calibrates optimization with variance-aware reweighting and per-dataset standardization."

## 关联
- [[ModelRouting]] — 模型动态路由方向
- [[RoutingPlateau]] — RoutingPlateau 分析路由上限，ReCal 优化 RL 路由训练
- [[HyDRA]] — HyDRA 用监督学习路由，ReCal 用 RL 路由
- [[INFRAMIND]] — INFRAMIND 用 RL 做编排，ReCal 的奖励校准可应用于此

## 矛盾
- 与"单一标量奖励"的矛盾：ReCal 表明多目标聚合导致模糊信用分配
