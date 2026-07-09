---
title: 'Co-Coder: 内聚感知任务分区'
type: source
tags:
- execution-scheduling
- task-partitioning
- graph-partitioning
- multi-agent
sources:
- co-coder-task-partitioning
source_file: raw/papers/co-coder-task-partitioning.pdf
last_updated: 2026-07-09
arxiv_id: '2606.00953'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
多 agent LLM 系统通过并行化和上下文隔离分解复杂任务（如编码），但增加 agent 引入 agent 间通信开销——可能抵消效率增益。Co-Coder 将多 agent 编排形式化为图分区问题，捕获通信-计算 tradeoff。

## 关键贡献
- 将多 agent 编排形式化为图分区问题——捕获通信-计算 tradeoff
- 从静态分析构建依赖图，隔离结构性 hub 文件
- 通过社区检测分区图，依赖感知调度器执行
- 28 个真实任务上 pass rate +14.0%，wall-clock 2.10x 加速，API 成本 -35%
- 依赖最密集的项目增益最大

## 方法细节
- **依赖图构建**：从代码仓库的静态分析（import 关系、函数调用、类继承）构建文件级依赖图
- **Hub 文件隔离**：识别高连接度的结构性 hub 文件（如公共 utils），单独处理避免成为通信瓶颈
- **社区检测分区**：用图社区检测算法（如 Louvain）将文件集群分为若干 agent 负责区——区内高内聚、区间低耦合
- **依赖感知调度**：调度器感知跨 agent 依赖，按依赖顺序执行——被依赖的 agent 先完成，依赖方后启动
- **通信-计算 tradeoff**：分区越多→并行度越高但通信开销越大；分区越少→通信少但并行度低

## 关键引用
> "Co-Coder formalizes multi-agent orchestration as a graph partitioning problem capturing the communication-computation tradeoff."

## 关联
- [[ExecutionScheduling]] — 执行调度方向
- [[DynAMO]] — DynAMO 做工作流并行化，Co-Coder 做任务分区优化
- [[MASPO]] — MASPO 优化 multi-agent prompt，Co-Coder 优化 multi-agent 任务分配

## 矛盾
- 与"更多 agent 更快"的直觉矛盾：Co-Coder 表明通信开销可能抵消并行化增益
