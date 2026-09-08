---
title: "TROVE: 轨迹验证路由编辑的自适应技能编排（Adaptive Agent Skill Orchestration via Trace-Grounded Route Validation）"
type: source
tags: [ontology-loop-detection]
sources: [trove-trace-route-validation]
source_file: raw/papers/trove-trace-route-validation.pdf
last_updated: 2026-09-08
arxiv_id: "2609.05019"
authors: ["Tianxing Wang", "Mingming Zhao", "Shuai Huang", "Huiyang Xu", "Chaoyue Niu"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
---

## 概要
TROVE 提出基于执行轨迹的 Agent 技能编排方法，通过 trace-grounded 路线验证和编辑适应运行时结果变化。离线将评估过的工作流搜索轨迹蒸馏为原子/复合技能和 outcome-conditioned 转移图；在线将规划路线视为临时意图，每次仅提交一个 top-level 技能，再根据观察结果 retain/insert/replace 未执行后缀。在 6 个 benchmark×3 个 LLM 的 18 个设置中，15 个取得最优或并列最优分数，16 个耗时最短，相对 AFlow 在 16 个设置提升分数（最高+31.37%），在 16 个设置减少时间（最高86.7%）。

## 解决的问题
现有 Agent 工作流在执行前确定结构（AFlow 的 dataset-level 优化、MaAS 的 query-level 架构选择、LAS 的图约束调度），当中间结果使后续计划失效时（continuation invalidation），要么执行过时步骤导致错误累积，要么广泛重规划浪费计算并丢弃已完成进度。粗粒度策略完全替换工作流丢失有用进度；细粒度逐步重规划引入路由延迟和方差。这一"pre-execution commitment vs runtime mismatch"矛盾是核心编排瓶颈。

## 方法与技术
1. **Offline Experience Extraction**：从 AFlow 搜索轨迹提取原子技能（标准化接口：输入/artifacts/状态/约束），识别稳定局部片段提升为复合技能（需内部排序稳定+数据依赖一致+子目标连贯+可独立执行），outcome-dependent 续接保留在 transition graph。
2. **Skill Transition Graph**：转移边从评估过的局部工作流修改导出（非仅邻接），记录 score/time delta 作为离线比较证据，部署时提供 bounded 续接提示。
3. **One-Step Commitment**：planner 提出≤4个 top-level 技能的路线，controller 仅执行第一个，观察 boundary outcome 后决定后续——proposal horizon 跨多技能，commitment horizon 仅一个动作。
4. **Observation-Guided Route Update**：三操作——Retain（后续仍有效则保留，无 LLM 调用）、Insert（图查找返回 trace-supported 响应技能，解决即时 mismatch）、Replace（图 abstain 或需更广变更时 LLM replanner 生成 bounded 替换后缀，保留已完成前缀）。
5. **Iterative Execution with bounds**：重复 commit-observe-update，终止于最终结果产生或 bounded step/repetition/no-progress 约束（最多 6 个 top-level skill calls）。

## 创新点
- **首次将"continuation invalidation"形式化为独立编排问题**（vs AFlow 固定工作流、LAS predefined DAG 内调度）——提出 selective route editing 原则（保留已执行前缀+artifacts，仅修复无效后缀）。
- **复合技能抽象隐藏稳定局部决策**（vs ExpeL 文本洞察、Voyager 代码技能库）——同时保留 outcome-dependent 续接暴露给在线 controller。
- **Retain-Insert-Replace 三操作的中间粒度策略**——在粗粒度工作流重选（丢进度）和细粒度逐步重规划（延迟+方差）间开辟新设计空间。
- **Transition graph 边来自评估过的局部修改**（含 score/time delta）——提供有 grounding 的路由建议而非仅技能邻接。

## 效果
- Dataset: HumanEval (DeepSeek) | Metric: pass@1 | Result: 97.71% | Baseline: 93.89% (AFlow) | Δ: [+3.82%]
- Dataset: MATH | Metric: Accuracy | Result: 80.86% | Baseline: 74.07% | Δ: [+6.79%]
- Dataset: GSM8K | Metric: Time | Result: 9.63min | Baseline: 57.73min | Δ: [−83.3%]
- Token: 13.45M vs AFlow 21.11M | Δ: [−36.3%]
- **Ablation**: Without Offline: 92.37→77.86 (−14.51 acc), +9.26min
- **Ablation**: Without Composite: 92.37→78.63 (−13.74 acc), +8.94min
- **Ablation**: Without Replace: 92.37→90.84 (−1.53 acc), +15.79min — replace 主要影响效率非正确性

## 关键引用
> "Agents tend to optimize, select, or constrain execution structures before decisive runtime outcomes are observed. However, such pre-execution commitment creates an orchestration bottleneck: when intermediate evidence invalidates the pending continuation, agents must either execute stale steps or replan broadly." — Section 1, p.1

> "TROVE occupies the middle ground between these strategies. It treats a planner-generated route as provisional intent and commits to only one top-level skill at a time." — Section 3.1, p.4

> "Ablations further show that composite skills capture most offline benefits, insertion enables local correction, and suffix replacement primarily improves efficiency." — Section 1, p.2

## 关联
- [[RuntimeGovernance]] — Round 8 运行时治理
- [[ExecutionScheduling]] — Round 11 执行调度优化
- [[skillnet-ai-skills]] — 本轮技能网络
- [[workflow-to-skill]] — 本轮工作流到技能分解
- [[argus-agentic-reasoning-runtime]] — 本轮 Agent 推理 runtime
