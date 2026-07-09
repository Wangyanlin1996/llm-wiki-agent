---
title: 'SAGA: 工作流原子化调度'
type: source
tags:
- execution-scheduling
- workflow-scheduling
- kv-cache-reuse
- gpu-scheduling
sources:
- saga-workflow-scheduling
source_file: raw/papers/saga-workflow-scheduling.pdf
last_updated: 2026-07-09
arxiv_id: '2605.00528'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
AI agent 每个任务执行数十到数百个链式 LLM 调用，但 GPU 调度器将每个调用视为独立——在步骤间丢弃数 GB 中间状态，端到端延迟膨胀 3-8x。SAGA 转向程序级调度——将整个 agent 工作流（而非单个推理调用）视为一等可调度单元。

## 关键贡献
- 程序级调度——将整个 agent 工作流视为可调度单元
- Agent Execution Graph 捕获工作流结构，预测跨工具调用边界的 KV cache 复用
- Session-affinity batching + work stealing 共置相关请求
- Agent Fair Share 任务完成时间公平性指标，有可证明的有界偏差保证
- 64 GPU 集群 SWE-bench + WebArena 上任务完成时间 1.64x 加速，GPU 内存利用率 1.22x，99.2% SLO 达成

## 方法细节
- **Agent Execution Graph**：将 agent 工作流建模为 DAG，节点是 LLM 调用，边是数据依赖（KV cache 可复用关系）
  - 预测跨工具调用边界的 KV cache 复用机会，达到 Bélády 最优离线策略的 1.31x
- **Session-affinity Batching**：将同一 agent session 的请求共置到同一 GPU，最大化 KV cache 复用
  - **Work Stealing**：空闲 GPU 可从繁忙 GPU "偷取"请求，保持全局负载均衡
- **Agent Fair Share**：以任务完成时间（而非请求数）为公平性指标——大任务和小任务获得可比的完成时间公平份额
  - 有可证明的有界偏差保证

## 关键引用
> "SAGA treats the entire agent workflow — not individual inference calls — as a first-class schedulable unit."

## 关联
- [[ExecutionScheduling]] — 执行调度方向
- [[INFRAMIND]] — INFRAMIND 做基础设施感知编排，SAGA 做工作流级调度
- [[TokenDance]] — TokenDance 做多 agent 间 KV 共享，SAGA 做单 agent 工作流内 KV 复用
- [[GoodServe]] — GoodServe 做 GPU 路由，SAGA 做工作流调度

## 矛盾
- 与"请求级调度"的矛盾：SAGA 表明工作流级调度能显著提升 KV 复用和公平性
