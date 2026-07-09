---
title: 'TwinRouterBench: 步级路由基准'
type: source
tags:
- model-routing
- benchmark
- step-level-routing
- agent-evaluation
sources:
- twinrouterbench-step-routing
source_file: raw/papers/twinrouterbench-step-routing.pdf
last_updated: 2026-07-09
arxiv_id: '2605.18859'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
LLM 路由在长时程应用（coding agent、深度研究、computer-use agent）中最重要——单用户请求触发多次模型调用。但现有路由基准只在 one-shot prompt 上评估——不暴露中间 agent 步骤的路由可见前缀，不测试更便宜替代是否保持下游任务成功。TwinRouterBench 是步级路由基准，双轨设计。

## 关键贡献
- 步级路由基准——首次评估 agent 中间步骤的路由
- 双轨设计：静态轨（快速离线迭代）+ 动态轨（端到端验证）
- 静态轨：970 个路由可见前缀，确定性算术评分（无在线 LLM judge）
- 动态轨：完整 500 例 SWE-bench Verified 上运行路由器
- 支持快速离线迭代+端到端验证

## 方法细节
- **静态轨**：
  - 970 个"路由可见前缀"——agent 执行过程中的中间上下文，路由器在此点做模型选择
  - 来源：SWE-bench/BFCL/mtRAG/QMSum/PinchBench 520 实例
  - 配执行验证的目标层级——每个前缀有"应该路由到什么级别模型"的标注
  - **确定性算术评分**：不用在线 LLM judge，用确定性规则计算路由准确率——快速、可重复
- **动态轨**：
  - Harness 在完整 500 例 SWE-bench Verified 上运行路由器
  - 每次 LLM 调用从锁定池选具体模型——模拟真实路由场景
  - 成功以官方任务解决率和实际 API 支出衡量——同时评估质量和成本
- **双轨互补**：
  - 静态轨：快速迭代路由器设计，无需运行完整 agent
  - 动态轨：验证静态轨上表现好的路由器在端到端任务上是否真正有效

## 关键引用
> "TwinRouterBench is a step-level routing benchmark — existing benchmarks only evaluate one-shot prompts, missing intermediate agent steps where routing matters most."

## 关联
- [[ModelRouting]] — 模型动态路由方向
- [[RoutingPlateau]] — RoutingPlateau 分析路由上限，TwinRouterBench 提供更好的评估工具
- [[HyDRA]] — HyDRA 是被评估的路由方法之一
- [[GoodServe]] — GoodServe 做 GPU 路由，TwinRouterBench 做模型路由评估

## 矛盾
- 与"one-shot 路由评估"的矛盾：TwinRouterBench 表明步级路由评估才能反映真实场景
