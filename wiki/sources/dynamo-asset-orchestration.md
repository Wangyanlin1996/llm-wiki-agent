---
title: 'DynAMO: 动态资产管理编排'
type: source
tags:
- execution-scheduling
- plan-then-execute
- parallel-execution
- industry40
sources:
- dynamo-asset-orchestration
source_file: raw/papers/dynamo-asset-orchestration.pdf
last_updated: 2026-07-09
arxiv_id: '2606.19382'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
LLM agent 提供 Industry 4.0 端到端自动化，但真实部署受限于延迟、并发不稳定性和安全风险。DynAMO 采用 Plan-then-Execute 架构生成可验证工作流图，支持 SequentialWorkflow 和 ParallelWorkflow——动态识别独立任务并行执行。

## 关键贡献
- Plan-then-Execute 架构生成可验证工作流图
- 支持 SequentialWorkflow（拓扑执行）和 ParallelWorkflow（依赖感知并发）
- 动态识别独立任务，保持结构正确性和安全性
- 6 个 AssetOpsBench 实验中并行执行延迟中位数降 1.6x（高可并行工作流达 1.8x）
- 结构化上下文裁剪降推理延迟 30%，故障注入下优雅降级

## 方法细节
- **Plan-then-Execute**：先将任务分解为工作流图（plan），再执行（execute）——执行前可验证图的正确性和安全性
- **SequentialWorkflow**：按拓扑序执行，适合有严格依赖的任务链
- **ParallelWorkflow**：动态分析依赖关系，识别无依赖的独立任务并发执行——通过依赖感知调度器保证执行顺序正确
- **结构化上下文裁剪**：根据当前执行步骤裁剪无关上下文，降低推理延迟 30%
- **故障降级**：故障注入下优雅降级而非崩溃——部分任务失败时继续执行可完成的任务

## 关键引用
> "DynAMO dynamically identifies independent tasks, maintaining structural correctness and safety while improving efficiency through controlled inference overlap."

## 关联
- [[ExecutionScheduling]] — 执行调度方向
- [[SAGA]] — SAGA 做 GPU 级工作流调度，DynAMO 做任务级工作流编排
- [[CoCoder]] — CoCoder 做任务分区，DynAMO 做工作流并行化

## 矛盾
- 与"全串行执行"的矛盾：DynAMO 表明依赖感知并行化能显著降低延迟
