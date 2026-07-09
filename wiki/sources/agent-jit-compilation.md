---
title: 'Agent JIT Compilation: Agent 即时编译'
type: source
tags:
- execution-scheduling
- jit-compilation
- web-agent
- latency-optimization
sources:
- agent-jit-compilation
source_file: raw/papers/agent-jit-compilation.pdf
last_updated: 2026-07-09
arxiv_id: '2605.21470'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
Web agent 规划和调度中，LLM 推理延迟与多步规划累积导致端到端延迟高。本文将编译器 JIT（Just-In-Time）思想引入 agent 规划——提前编译常用规划模式，运行时按需执行。

## 关键贡献
- 将 JIT 编译思想从传统编译器引入 agent 规划
- 提前编译常用规划模式，运行时按需执行
- 针对_web agent 的延迟优化规划调度框架

## 方法细节
- **规划模式识别**：从历史执行轨迹中识别高频出现的规划模式（如登录→搜索→点击→提取）
- **模式编译**：将识别到的模式预编译为可执行模板——参数化关键变量
- **运行时匹配**：新任务到达时，先匹配已有编译模板；匹配成功则直接执行模板跳过 LLM 规划
- **按需编译**：未匹配的任务通过 LLM 规划，规划完成后新模式即时编译供未来复用

## 关键引用
> "We introduce JIT compilation from traditional compilers into agent planning — precompiling frequent planning patterns for on-demand execution."

## 关联
- [[ExecutionScheduling]] — 执行调度方向
- [[ModelNativeArchitecture]] — 同为编译器类比，ModelNativeArchitecture 做架构设计，Agent JIT 做规划优化
- [[TypeGo]] — TypeGo 做 OS 式 runtime，Agent JIT 做 JIT 式规划

## 矛盾
- 与"每次都重新规划"的矛盾：JIT 编译表明复用规划模式能显著降低延迟
