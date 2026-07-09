---
title: 'TypeGo: 具身 Agent 的 OS 式运行时'
type: source
tags:
- execution-scheduling
- os-runtime
- embodied-agent
- latency-optimization
sources:
- typego-os-runtime
source_file: raw/papers/typego-os-runtime.pdf
last_updated: 2026-07-09
arxiv_id: '2607.05482'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
将 LLM 作为请求/响应预言机放在关键路径上，与实时控制和并发目标根本矛盾。TypeGo 是 OS 风格的 embodied agent runtime——LLM 规划结构化为多时间尺度异步循环与执行重叠。

## 关键贡献
- OS 风格的 embodied agent runtime——LLM 不在关键路径上
- Skill Kernel 在并发 per-task 进程间仲裁类型化物理子系统
- 调度器抢占并按源恢复或替换
- Speculative skill streaming 在进行中的运动后隐藏 LLM 延迟
- Fast first-action 路径在 1 秒内产生可见反馈
- Unitree Go2 上每步延迟降 50%，首动作时间降 73%

## 方法细节
- **多时间尺度异步循环**：LLM 规划（慢循环）与物理执行（快循环）解耦——规划在后台异步进行，执行不被阻塞
- **Skill Kernel**：类似 OS 内核管理硬件驱动——管理类型化物理子系统（行走、抓取、视觉），在并发 per-task 进程间仲裁资源
- **抢占式调度**：调度器可抢占当前执行的任务，按来源恢复或替换——高优先级任务可中断低优先级任务
- **Speculative Skill Streaming**：在当前运动执行期间，推测性地准备下一个 skill——如果推测正确则无缝衔接，如果错误则丢弃
- **Fast First-Action**：任务到达时立即执行一个合理的首动作（如向前走一步），在 1 秒内产生可见反馈，同时 LLM 在后台规划

## 关键引用
> "TypeGo treats the agent's physical body like an OS manages hardware — the LLM is taken off the critical path."

## 关联
- [[ExecutionScheduling]] — 执行调度方向
- [[ModelNativeArchitecture]] — 同为 OS 类比，ModelNativeArchitecture 做架构设计，TypeGo 做具体 runtime 实现
- [[AgentJITCompilation]] — Agent JIT 做规划模式复用，TypeGo 做 OS 式资源管理

## 矛盾
- 与"LLM 在关键路径上"的矛盾：TypeGo 表明 OS 式异步架构能将 LLM 移出关键路径
