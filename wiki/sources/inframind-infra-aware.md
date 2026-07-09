---
title: 'INFRAMIND: 基础设施感知编排'
type: source
tags:
- model-routing
- infrastructure-aware
- multi-agent
- scheduling
- slo-compliance
sources:
- inframind-infra-aware
source_file: raw/papers/inframind-infra-aware.pdf
last_updated: 2026-07-09
arxiv_id: '2606.11440'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
现有 多 agent LLM 编排（从暴力集成到学习路由器）基于任务和模型特征选择模型和拓扑，但不考虑服务基础设施的运行时状态。在共享 GPU 集群并发负载下，这种基础设施盲性导致系统性资源利用不足。INFRAMIND 让整个多 agent 栈基础设施感知。

## 关键贡献
- 让整个多 agent 栈基础设施感知——不只路由器，planner 和 executor 也感知
- Infra-aware planner 根据实时系统负载条件化拓扑和角色选择
- Infra-aware executor 每步观察 per-model 队列深度、缓存利用率和响应延迟
- Budget-aware scheduler 重排模型队列使紧急请求优先
- 层次化受约束 MDP，RL 端到端求解
- 低负载 +7.6pp 准确率 / 7x 低延迟，高负载 99.9% SLO 合规（所有基线低于 50%）

## 方法细节
- **Infra-aware Planner**：
  - 根据实时系统负载选择多 agent 拓扑——拥堵时偏向简单图（fewer agents），低负载时丰富图（more agents）
  - 条件化角色选择——拥堵时选轻量模型，低负载时选重量模型
- **Infra-aware Executor**：
  - 每步观察 per-model 队列深度、缓存利用率、响应延迟
  - 据此决定调用哪个模型和推理多深——例如队列深时选替代模型，缓存利用率高时选有缓存的模型
- **Budget-aware Scheduler**：
  - 重排模型队列使紧急请求优先
  - 考虑剩余预算（时间、token）——接近预算上限时降级到更便宜的模型
- **层次化受约束 MDP**：
  - 上层 MDP：planner 做拓扑和角色选择
  - 下层 MDP：executor 做每步模型选择
  - 约束：SLO、预算、安全
  - RL 端到端求解——联合优化准确率、延迟、SLO 合规

## 关键引用
> "INFRAMIND makes the entire multi-agent stack infrastructure-aware — not just the router, but the planner and executor observe real-time system state."

## 关联
- [[ModelRouting]] — 模型动态路由方向
- [[HyDRA]] — HyDRA 做能力感知路由，INFRAMIND 做基础设施感知编排
- [[SAGA]] — SAGA 做工作流调度，INFRAMIND 做基础设施感知编排
- [[GoodServe]] — GoodServe 做 GPU 路由，INFRAMIND 做全栈感知

## 矛盾
- 与"基础设施盲路由"的矛盾：INFRAMIND 表明高负载下基础设施感知能将 SLO 合规从 <50% 提升到 99.9%
