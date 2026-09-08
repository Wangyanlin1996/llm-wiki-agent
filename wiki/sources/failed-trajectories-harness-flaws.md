---
title: "HARNESSFIX: 从失败轨迹诊断和修复 Agent Harness 缺陷（Diagnosing and Repairing Harness Flaws）"
type: source
tags: [ontology-loop-detection]
sources: [failed-trajectories-harness-flaws]
source_file: raw/papers/failed-trajectories-harness-flaws.pdf
last_updated: 2026-09-08
arxiv_id: "2606.06324"
authors: ["Mengzhuo Chen", "Junjie Wang", "Zhe Liu", "Yawen Wang", "Haiming Zheng"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
---

## 概要
HARNESSFIX 是一个 trace-grounded、diagnosis-driven 的 agent harness 修复框架，从失败 trajectory 中诊断并修复 harness flaws。它将 raw execution traces 和 harness artifacts 编译为 Harness-aware Trace Intermediate Representation (HTIR)，规范化碎片化 trajectory evidence 并捕获 step-level data-flow 和 control-flow 关系，再与 harness artifacts 对齐。随后将 failure 归因到 responsible steps 和 harness artifacts，将 recurring diagnoses 整合为 repair-oriented flaw records，最终映射到 scoped repair operators 并在 flaw-specific repair specifications 下生成 patches，通过 regression-aware validation 接受。在 GAIA、SWE-Bench Verified、AppWorld、Terminal-Bench 2.0 四个 benchmark 上，相对 initial harness 提升 6.3%–18.4%。

## 解决的问题
LLM agent 的可靠性不仅依赖 base model，还依赖 agent harness（ETCLOVG 七层 runtime infrastructure）。当失败发生时，修改 harness 比重训 model 更实际，但 harness improvement 极其困难：agent 行为在 runtime 通过 model inference 决定，failures 无法直接映射到 harness 实现的具体位置。现有 self-improving agents 和 automatic harness evolution 方法要么做 runtime supervision（暂时压制错误但不修复根因），要么 outcome-driven 优化（基于 final scores 修改 prompts/workflows 而不先定位 responsible evidence 和 failed harness layer）。

## 方法与技术
1. **HTIR (Harness-aware Trace Intermediate Representation)**：将 trajectory 建模为 TraceSteps（含 request/response message + role/status/artifact-state-effect 三派生注解），重构 cross-step TraceLinks（data-flow links 追踪信息传播、control-flow links 追踪执行决策），并通过 implementation anchors 将 runtime evidence 定位到具体 harness artifacts。
2. **Failure Attribution 四步法**：(a) symptom localization 从 final TraceStep 识别失败症状；(b) evidence backtracking 沿 links 回溯产生 candidate responsible TraceSteps；(c) candidate adjudication 审查每个候选的诊断 evidence 选定最终 responsible steps；(d) layer assignment 将 failure 归因到 ETCLOVG harness layers。
3. **Harness Flaw Consolidation**：按 implicated harness layers 索引诊断记录，将 overlapping layers 的记录作为 merge candidates，合并 root cause 和 supporting evidence 一致的记录为 recurring flaw records。
4. **Scoped Repair Operators**：基于 30 个开源 agent repo 和 ~57,780 条 records 的 empirical study 总结七层 repair operators（如 verification-gated finalization、tool-schema narrowing、loop guarding 等）；repair agent 从 flaw record 检索候选 operators。
5. **Patch Generation with Repair Specification + Regression-aware Validation**：specification 含 target/scope、edit constraints、required behavior；validation agent 先做 pre-validation，再在 held-out validation set 上评估 target flaw reduction 和 regression limit。

## 创新点
- **Trace-grounded diagnosis-driven repair vs outcome-driven prompt evolution**（vs GEPA reflective prompt evolution、SCOPE memory-guided prompt evolution、Meta-Harness optimization-based search）——先从 failed trajectory 中精确定位 responsible steps 和 failed harness layer，再做 scoped repair。
- **HTIR 对齐 runtime behavior 与 static harness artifacts**——通过 data-flow links + control-flow links + implementation anchors 将执行轨迹与可编辑 harness 实现对齐。
- **Scoped repair operators 约束 free-form editing**——基于 empirical study（30 repos, 57,780 records）总结的七层 repair operators 约束 patch 生成范围。
- **Cross-model transfer**——GPT-5 mini 上修复的 GAIA harness 直接迁移到 Claude/DeepSeek/Qwen/Gemini 仍有 5.5%–9.5% 一致正向增益，说明修复的是 model-agnostic 的 harness-level flaws。

## 效果
- Dataset: GAIA | Metric: TCR | Result: 61.7% | Baseline: 43.3% (H₀, GPT-5 mini) | Δ: [+18.4pp]
- Dataset: SWE-Bench Verified | Metric: TCR | Result: 57.3% | Baseline: 45.3% | Δ: [+12.0pp]
- Dataset: AppWorld | Metric: TCR | Result: 43.0% | Baseline: 36.7% | Δ: [+6.3pp]
- Dataset: Terminal-Bench 2.0 | Metric: TCR | Result: 26.5% | Baseline: 17.6% | Δ: [+8.9pp]
- Dataset: GAIA | Metric: TCR | Result: 61.7% | Baseline: 56.7% (Meta-Harness) | Δ: [+5.0pp] at 57.6M tokens vs 94.2M
- Cross-model transfer (GAIA): Claude +5.5pp; DeepSeek +7.8pp; Qwen +9.5pp; Gemini +8.9pp
- **Ablation**: Prompt-only repair: 50.6% (Δ=−11.1pp); w/o trace-grounded diagnosis: 51.1% (Δ=−10.6pp); w/o scoped operators: 50.6% (Δ=−11.1pp)
- Failure diagnosis: Full HTIR achieves 85.0% step accuracy, 81.3% anchor accuracy, 86.2% layer macro-F1 (vs raw trace 55.0%/53.8%/50.0%)

## 关键引用
> "Existing efforts on self-improving agents and automatic harness evolution only partially address this problem. One line of work focuses on runtime or supervisory optimization... While such strategies can improve observed performance, they often do so without fixing the underlying harness flaw." — Section I, p.1

> "The key idea of HARNESSFIX is to drive harness repair from fine-grained, trace-grounded failure diagnoses. It first localizes responsible runtime steps, maps their behavior to implicated harness flaws, and then translates those diagnoses into scoped repair specifications." — Section III, p.3

> "harness-related records account for approximately 45.3% of all collected development records, and all 30 repositories contain such changes." — Section II-B, p.3

## 关联
- [[RuntimeGovernance]] — Round 8 运行时治理
- [[ExecutionScheduling]] — Round 11 执行调度优化
- [[trove-trace-route-validation]] — 本轮 TROVE 轨迹路由验证
- [[argus-agentic-reasoning-runtime]] — 本轮 Agent 推理 runtime
- [[masc-metacognitive-self-correction]] — 本轮元认知自纠正
