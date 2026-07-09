---
title: "执行调度优化（Execution Scheduling）"
type: concept
tags: ['scheduling', 'workflow', 'gpu-scheduling', 'os-analogy', 'parallel-execution']
sources: ["saga-workflow-scheduling", "dynamo-asset-orchestration", "co-coder-task-partitioning", "agent-jit-compilation", "typego-os-runtime", "model-native-architecture"]
last_updated: 2026-07-09
---

执行调度优化解决 AI agent 多步链式 LLM 调用的端到端延迟问题。核心矛盾：请求级调度与复合 AI 工作负载根本不匹配。

**六大范式**：
1. **工作流原子化调度** — [[SAGA]] 将整个 agent 工作流视为可调度单元，Agent Execution Graph 预测跨工具调用边界的 KV cache 复用，任务完成时间 1.64x 加速。
2. **Plan-then-Execute 并行化** — [[DynAMO]] 生成可验证工作流图，动态识别独立任务并行执行，延迟中位数降 1.6x。
3. **图分区任务分配** — [[CoCoder]] 将多 agent 编排形式化为图分区问题，捕获通信-计算 tradeoff，社区检测分区+依赖感知调度，pass rate +14.0%，wall-clock 2.10x。
4. **JIT 规划编译** — [[AgentJITCompilation]] 将编译器 JIT 思想引入 agent 规划，提前编译常用规划模式，运行时按需执行。
5. **OS 式 runtime** — [[TypeGo]] 将 LLM 移出关键路径，Skill Kernel 仲裁类型化物理子系统，speculative skill streaming 隐藏 LLM 延迟，每步延迟降 50%。
6. **统一架构框架** — [[ModelNativeArchitecture]] 提出 ICA 六层架构，双平面（概率执行+确定性控制）解决 LLM 是 CPU 还是 OS 的张力，三个 Amdahl 式启发式指导设计。

**关键洞察**：调度粒度正从"请求级"→"工作流级"→"程序级"。OS 类比（CPU=LLM、cache=KV、RAM=上下文、OS=agent框架）提供了统一设计语言。
