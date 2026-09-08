---
title: "Argus: 面向长程任务的通用 Agent 推理 Runtime（General-Purpose Agentic Reasoning Runtime）"
type: source
tags: [ontology-loop-detection]
sources: [argus-agentic-reasoning-runtime]
source_file: raw/papers/argus-agentic-reasoning-runtime.pdf
last_updated: 2026-09-08
arxiv_id: "2608.05144"
authors: ["Boxiu Li", "Zimo Wen", "Yijia Fan"]
year: 2026
venue: "arXiv preprint (Technical Report)"
citation_count: 0
---

## 概要
Argus 是一个面向 long-horizon 任务的 persistent agentic runtime，核心抽象是在 durable project state 上执行 bounded missions 的四角色循环（Manager → Planner → Engineer → Reviewer）。它提出 "evidence-governed progressive evolution"，通过 verification-gated admission 机制使 candidate memories、skills、procedures、verifiers 和 rejected routes 在通过 role-owned review 和 task-native verifier evidence 后才可复用。模型权重保持固定，self-evolution 发生在 persistent runtime state 和 control policy 层面。在七个 GPT-5.5 benchmark arenas 上保持有效，SWE-Bench Pro 达到约 78%（对比 Direct Copilot 的 59%）。

## 解决的问题
现有 self-improving agents 在 supervision signal dense 的场景中有效，但真正重要的研究任务往往 underdefined：objective 在开始时无法精确陈述，正确的 measurement 本身是问题的一部分，可用反馈稀疏、延迟且存争议。prior work 如 ReAct、SWE-agent、OpenHands 假设 objective 已给定；AI Scientist、CycleResearcher 等将交互扩展到迭代研究流程，但都假设目标不变。当 score 无法信任时，pivoting（目标修正）应被允许但需 verification 使其与 goal drift 区分开。

## 方法与技术
1. **Working contract Kt = (ι, ot, ct, vt)**：将 standing intent（ι）、current objective（ot）、constraints（ct）、verification criteria（vt）分离，通过 ManagerAdmit operator 在 evidence、authority 和 provenance 要求下执行 material refinement。
2. **Four-role state machine M→P→E⇄R→M**：Manager 锚定 objective 和 campaign state，Planner 选择下一个 work unit，Engineer 实现并评估，Reviewer 在需要独立审查时发出 completion verdict。
3. **Verification-gated runtime self-evolution**：candidate updates 仅在 authorized role 检查 artifacts 和 task-native evidence 后才进入 persistent state；admission gate 可包含 official verifier、independent Reviewer 或 explicitly allowed Engineer self-review。
4. **Stage dynamics**：legal transitions 为 {hold, advance, rollback}；accepted Stages 保留 attempted routes、measurements、verdicts；rejected branches 作为 verified exclusions 保留。
5. **Dense-intelligence density ρI(T)**：将 token throughput 按 ηr（relevant reasoning）、ηa（effective action）、ηv（valid verification）三因子加权。

## 创新点
- **Verified pivoting**（vs prior work 的 fixed objective）——将 pivoting 从 goal drift 中区分出来，需有 evidence 支持 previous route 不可达或 misspecified，通过 explicit role boundary 进入。
- **Verification-gated fixed-model self-evolution**（vs Reflexion/Voyager/MemGPT 仅做 session-level 持续化）——model weights 不变，evolution 发生在 persistent state 和 control policy 层面。
- **Contract refinement 的 typed/logged/role-owned surfaces**——每次 material change 都有 author、precondition 和 audit trail。
- **Endogenous harnessing 诊断**——识别出 Planner 早期决策会变为后续 Engineer/Reviewer 的不可变约束这一"category confusion"问题，指出 bottleneck 是 methodological 而非 cognitive。

## 效果
- Dataset: SWE-Bench Pro | Metric: Accuracy | Result: ~78% | Baseline: 59% (Direct Copilot) | Δ: [+19pp] | at 1.41× aggregate Tokens
- Dataset: SWE-Bench Pro (longitudinal) | Metric: Tokens/task | Result: 2.33M (mature) | Baseline: 2.95M (startup) | Δ: [−21%]
- Dataset: SWE-Bench Pro (longitudinal) | Metric: Time/task | Result: 7.25 min | Baseline: 8.52 min | Δ: [−15%]
- Reviewer intervention: 466/731 tasks invoked Reviewer; 43 revision requests → 34 recoveries (79.1%) → 22 strict rescues (51.2%)
- **Ablation**: RWKV6 kernel optimization: forward latency 0.199ms→0.168ms (1.18×)
- **Ablation**: Materials (MOF) generation: best-of-K (K=8) 55.21% vs Feynman–Kac 52.38% (+2.83pp)

## 关键引用
> "What these share is not difficulty but underdefinition: at the moment work starts, nobody, human or machine, can state the objective precisely enough to optimize against it." — Section 1, p.1

> "A pivot should not reset the campaign. The runtime self-evolves the approach between the standing intent and the current operational contract." — Section 1, p.2

> "The binding constraint on this class of system is methodological rather than cognitive, which is also why the remedy is a change in authority routing rather than a stronger model." — Section 7.5, p.22

## 关联
- [[RuntimeGovernance]] — Round 8 运行时治理
- [[VerificationCoEvolution]] — Round 8 验证协同演化
- [[trove-trace-route-validation]] — 本轮 TROVE 轨迹路由验证
- [[gubernaut-homeostatic-controller]] — 本轮确定性控制器
- [[failed-trajectories-harness-flaws]] — 本轮 harness 缺陷修复
