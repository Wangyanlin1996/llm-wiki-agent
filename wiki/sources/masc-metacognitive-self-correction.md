---
title: "MASC: 多智能体系统的元认知自纠正（Metacognitive Self-Correction via Prototype-Guided Reconstruction）"
type: source
tags: [ontology-loop-detection]
sources: [masc-metacognitive-self-correction]
source_file: raw/papers/masc-metacognitive-self-correction.pdf
last_updated: 2026-09-08
arxiv_id: "2510.14319"
authors: ["Xu Shen", "Qi Zhang", "Song Wang", "Zhen Tan", "Xinyu Zhao"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
---

## 概要
MASC 是一个面向 LLM-based multi-agent systems (MAS) 的 metacognitive framework，实现 real-time、unsupervised、step-level 的 error detection 和 self-correction。它将检测重新定义为 history-conditioned anomaly scoring，通过两个互补设计实现：Next-Execution Reconstruction 从 query 和 interaction history 预测下一步 embedding 以捕获 causal consistency；Prototype-Guided Enhancement 学习 normal-step embedding 的 prototype prior 以在 sparse context 下稳定 reconstruction。当异常步骤被标记时，MASC 触发 correction agent 修正 acting agent 的输出，防止错误向下游传播。在 Who&When benchmark 的 w/o GT 设定下，MASC 达到最高 8.47% AUC-ROC 提升。

## 解决的问题
LLM-based MAS 中单个 agent 的错误会通过协作结构 cascade 传播并导致系统级性能崩溃——预实验显示单个 agent 错误可造成 over 50% 性能下降。现有方法依赖额外 verification agent 或通过 RL post-train specialized LLM，但前者需要大量监督、后者需要 costly training pipelines 且 task-specific optimization 限制了 scalability。核心挑战在于：(1) fine-grained supervision 稀缺；(2) 错误信号高度 context-dependent；(3) 许多错误发生在早期步骤，此时 contextual information 有限。

## 方法与技术
1. **Next-Execution Reconstruction**：给定到 step t-1 的 history，通过 frozen LLM 编码 context sequence 并经 learnable linear projection 预测 step t 的 embedding；anomalous steps 因违反 causal consistency 会产生更大的 prediction-realization deviation。
2. **Prototype-Guided Enhancement**：维护一个 learnable prototype vector p 作为 normal step embeddings 的 centroid；通过 single-head attention update（p 作 query，reconstructed embeddings 作 keys/values）；在 early steps history 稀疏时提供 stable anchor。
3. **Training objective** = L_recon + λ·L_proto，仅在 normal trajectories 上无监督训练：L_recon 为 MSE，L_proto 为 1-cos；anomaly 在 inference time 通过更大的 residual 自然显现。
4. **Anomaly scoring** s(t) = α·‖ˆx_t − x_t‖₂ + β·(1−cos(ˆx_t, p))：结合 L2 reconstruction error 和 cosine prototype misalignment，高于 threshold θ 触发 intervention。
5. **Anomaly-triggered self-correction**：当 s(t)>θ 时，dedicated correction agent 被触发，以 H_{t-1}、O_t 和 correction instruction 为输入生成修正输出，替换原始输出并更新 history。

## 创新点
- **将 step-level error detection 形式化为 history-conditioned unsupervised anomaly detection**（vs LLM-as-detector 需 prompt LLM 判断、supervised models 需 error labels）——完全不需要 error labels，仅在 normal trajectories 上训练。
- **Next-Execution Reconstruction 而非 input reconstruction**——不同于图像/时序领域的 reconstruction-based anomaly detection，MASC 预测 next step embedding 以利用 agent interaction 的 causal structure。
- **Prototype prior 解决 early-step 问题**——针对 errors 在 trajectory 前 20% 出现频率高但 history 不足的困难，引入 prototype 作为 normality 的 stable reference。
- **Plug-and-play architecture-agnostic integration**——MASC 作为 metacognitive layer 可直接插入 Chain/Complete Graph/Random/Debate 等 MAS topology。

## 效果
- Dataset: Who&When (handcrafted, w/o GT) | Metric: AUC-ROC | Result: 77.84% (LLaMA-3.1-8B) | Baseline: 65.79% | Δ: [+12.05pp]
- Dataset: Who&When (automated, w/o GT) | Metric: AUC-ROC | Result: 75.62% | Baseline: 65.39% | Δ: [+10.23pp]
- Dataset: AgentErrorBench (GAIA) | Metric: AUC-ROC | Result: 86.78% | Baseline: 84.26% (AgentDebug) | Δ: [+2.52pp]
- Dataset: AgentErrorBench (WebShop) | Metric: AUC-ROC | Result: 80.36% | Baseline: 74.38% | Δ: [+5.98pp]
- Dataset: GSM8K (MASC+Debate) | Metric: Accuracy | Result: 93.39% | Baseline: 91.40% (Debate) | Δ: [+1.99pp]
- **Ablation**: Remove reconstruction → AUC-ROC 大幅下降，model 失去捕获 step 间 causal dependency 的能力
- **Ablation**: Remove prototype → AUC-ROC 下降，especially in early steps where historical context is limited

## 关键引用
> "A single step in a multi-agent trajectory is rarely separable from errors without history... the inter-cluster distance is extremely small (e.g., 0.25), while the intra-cluster distance remains large (1.45), indicating isolation is insufficient." — Section 2.2, p.3

> "Instead of reconstructing the input, we leverage the causal structure of agent interactions. Given the history up to step t−1, the module predicts the representation of the next execution step, t." — Section 3.2, p.4

> "a single agent's error can cause system-level performance to drop by over 50%, underscoring the urgent need for mechanisms that support real-time error detection and correction." — Section 1, p.1

## 关联
- [[RuntimeGovernance]] — Round 8 运行时治理
- [[TrajectoryForensics]] — Round 8 轨迹取证
- [[agent-tom-monitoring]] — Round 8 ToM 推理监控
- [[gubernaut-homeostatic-controller]] — 本轮确定性控制器
- [[argus-agentic-reasoning-runtime]] — 本轮 Agent 推理 runtime
