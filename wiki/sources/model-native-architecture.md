---
title: '模型原生计算架构 (ICA)'
type: source
tags:
- execution-scheduling
- system-architecture
- os-analogy
- amdahl-law
sources:
- model-native-architecture
source_file: raw/papers/model-native-architecture.pdf
last_updated: 2026-07-09
arxiv_id: '2606.00288'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
LLM 正从模型技术转向系统技术。缓存复用、上下文容量、agent 调度、权限控制等工程挑战类似经典计算机系统问题，但各层文献缺乏统一模型。本文将 LLM 视为 CPU、KV cache 为处理器缓存、上下文窗口为主存、agent 框架为操作系统的类比，提出 Intelligent Computing Architecture (ICA)。

## 关键贡献
- 提出六层功能架构 ICA——每层有接口契约和设计公理
- 双平面架构解决 LLM 是 CPU 还是 OS 的张力
- 概率执行平面（能计算什么）+ 确定性控制平面（应计算什么）
- 三个 Amdahl 式设计启发式：Semantic Locality、Context Budget、Agent Speedup

## 方法细节
- **类比映射**：
  - LLM = CPU（执行单元）
  - KV cache = 处理器缓存（L1/L2 cache）
  - 上下文窗口 = 主存（RAM）
  - Agent 框架 = 操作系统（OS）
- **六层架构**：每层有明确的接口契约（输入/输出格式）和设计公理（不变量约束）
- **双平面架构**：
  - 概率执行平面——LLM 驱动，回答"能计算什么"（what can be computed）
  - 确定性控制平面——传统代码驱动，回答"应计算什么"（what should be computed）
  - 每层通过分级交叉（graded crossing）连接两个平面
- **三个设计启发式**（类比 Amdahl 定律）：
  - Semantic Locality——语义局部性：相关概念应在上下文中邻近放置
  - Context Budget——上下文预算：上下文窗口是稀缺资源，需预算分配
  - Agent Speedup——Agent 加速比：agent 并行化的收益上限由串行部分决定

## 关键引用
> "ICA resolves the tension of whether LLM is CPU or OS through a dual-plane architecture — probabilistic execution plane and deterministic control plane."

## 关联
- [[ExecutionScheduling]] — 执行调度方向
- [[TypeGo]] — TypeGo 是 OS 式 runtime 的具体实现，ICA 是架构框架
- [[AgentJITCompilation]] — Agent JIT 用编译器类比，ICA 用 OS 类比
- [[SAGA]] — SAGA 的工作流调度是 ICA 架构中 OS 层的具体实现

## 矛盾
- 与"各层独立设计"的矛盾：ICA 表明需要统一架构框架指导各层协同设计
