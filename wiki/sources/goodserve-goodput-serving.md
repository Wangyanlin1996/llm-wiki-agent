---
title: 'GoodServe: Goodput 优化的异构服务'
type: source
tags:
- model-routing
- heterogeneous-gpu
- goodput-optimization
- slo-compliance
- request-migration
sources:
- goodserve-goodput-serving
source_file: raw/papers/goodserve-goodput-serving.pdf
last_updated: 2026-07-09
arxiv_id: '2605.16867'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
Agentic 应用中每次完整推理的及时完成至关重要，且推理越来越多在异构 GPU 上服务。需将入站推理请求路由到合适 GPU 使端到端延迟要求尽可能满足，实现高 goodput。GoodServe 采用 predict-and-rectify 路由策略。

## 关键贡献
- Predict-and-rectify 路由策略——预测+运行时纠正
- 估计请求输出长度和 GPU 服务状态
- Just-enough instance selection 启发式做高质量路由决策
- 周期性监控 SLO 违规风险，触发运行时请求迁移
- Goodput 比现有路由方法提升 27.4%

## 方法细节
- **Predict 阶段**：
  - 估计请求输出长度——基于 prompt 特征预测生成长度，用于估算总推理时间
  - 估计 GPU 服务状态——当前队列深度、GPU 利用率、历史延迟
  - **Just-enough Instance Selection**：选择刚好能满足 SLO 的 GPU 实例——不选过强的（浪费成本）也不选过弱的（违反 SLO）
- **Rectify 阶段**：
  - 周期性监控活跃请求的 SLO 违规风险——如果预测剩余时间+当前延迟可能超 SLO
  - 触发**运行时请求迁移**——将请求从当前 GPU 迁移到更快的 GPU
  - 迁移涉及 KV cache 传输——需要权衡迁移成本和 SLO 违规成本
- **Goodput 定义**：满足 SLO 的完成请求数 / 总请求数——不仅看吞吐量，更看及时完成率

## 关键引用
> "GoodServe uses predict-and-rectify routing — just-enough instance selection followed by runtime request migration to prevent SLO violations."

## 关联
- [[ModelRouting]] — 模型动态路由方向
- [[HyDRA]] — HyDRA 做模型路由，GoodServe 做 GPU 路由
- [[INFRAMIND]] — INFRAMIND 做全栈感知编排，GoodServe 做 GPU 级路由
- [[SAGA]] — SAGA 做工作流调度，GoodServe 做 GPU 级 goodput 优化

## 矛盾
- 与"静态路由"的矛盾：GoodServe 表明 predict-and-rectify 能 27.4% 提升 goodput
