---
title: "Retrieval-State Lock-In: 诊断 RAG 检索状态锁定失败模式（Diagnosing Retrieval-State Lock-In in RAG）"
type: source
tags: [ontology-graph-retrieval]
sources: [retrieval-state-lock-in]
source_file: raw/papers/retrieval-state-lock-in.pdf
last_updated: 2026-08-31
arxiv_id: "2606.22728"
authors: ["Sahib Julka"]
year: 2026
venue: "arXiv preprint (LMU Munich)"
citation_count: 0
doi: ""
---

## 概要
本文命名并诊断了 RAG 系统中的 retrieval-state lock-in 失败模式：当 retriever 反复返回相同 degenerate retrieval state（空的或 coherent 但错误的），重复采样无法暴露错误，answer-state agreement 被误读为 confidence。作者将 confidence 分解为三个独立对象——answer-state uncertainty、evidence-state uncertainty 和 retrieval-state uncertainty，分别用 SD-UQ、SEU 和 GPS 评分。在 OntoGraphRAG（ontology-guided KG-RAG）系统上六个 QA 数据集实验显示，42%的 KG-RAG 错误和 59%的 dense retrieval 错误携带零 answer dispersion（silent errors），answer-only 方法 structural ceiling 上最多 recall 41-58%错误。

## 解决的问题
现有 black-box uncertainty estimators（semantic entropy、SelfCheckGPT 及 RAG-integrated variants）通过采样答案一致性判断 confidence，但当 retrieval 反复返回相同 defective state 时，答案一致是因为 error stable 而非因为正确——这个问题在 deployed RAG 中被识别但缺乏 name、measurable signature 和 prevalence bound。FRANQ 分离 factuality/faithfulness 但 operates on flat-text RAG，不暴露三路 graph-side 分解；SURE-RAG 评分 evidence-set sufficiency 但不评估 retrieval 是否 concentrated around wrong symbolic trace；R2C 通过 perturbation 测量 dispersion 但不处理 unperturbed retrieval 几乎不移动的 lock-in；Ca2KG 通过 counterfactual prompting 研究 KG-RAG overconfidence 但不提供 prevalence estimate。

## 方法与技术
1. **三对象 confidence 分解**：将 RAG confidence 形式化为 `p(r,c,s|q) = p(s|q)·p(c|q,s)·p(r|q,c,s)`，分别对应 answer-state、evidence-state 和 retrieval-state。当 `p(c|q)` 近 degenerate（lock-in regime）时，采样只暴露 decoder variability 而非 evidence variability。定义 silent error 为 wrong answer with zero observed answer-state dispersion。
2. **SD-UQ (answer-state, 新提出)**：Question-conditioned embedding-dispersion 评分。先用正交投影矩阵将 question 方向从 answer embeddings 中投影去除，然后对 centered projected matrix 做 thin SVD，取 top-k 奇异值的 geometric mean。
3. **GPS (retrieval-state, 新提出)**：Graph Path Support 评分，测量答案实体从问题实体在 retrieved KG 中的可达性。`GPS(q,a) = 1 − Σ w_a·γ^{L_a−L̂(q)}·1[e_reachable] / Σ w_a`，L_a 是最短 qualifying path length，L̂(q) 是期望 reasoning depth。GPS=0（full support）到 GPS=1（no support）。
4. **SEU (evidence-state, 新 operationalization)**：Support Entailment Uncertainty，normalized entailment-contradiction deficit。`s = (n_E − n_C)/K`，SEU = (1−s)/2。用 NLI 模型分类每个 chunk。
5. **合取审计规则**：只有当三个检查全部 concur 时认证答案为 low-risk：SD-UQ 在 lower half、SEU≤0.5、GPS≤0.5。唯一 data-dependent threshold 是 SD-UQ 的 per-dataset median。

## 创新点
- **与 semantic entropy 和 SelfCheckGPT 等 answer-state-only 方法不同**：提出三对象分解框架——answer-only 方法在 lock-in 时 structural ceiling 上最多 recall 41-58%的错误，因为 silent errors 的 DSE=0 无 within-question disagreement signal。
- **与 FRANQ 和 SURE-RAG 不同**：GPS 是首个 graph-side retrieval-state 诊断，直接检查 matched entities、typed triples、paths 是否 support 答案，并通过 route logging 分离 absence vs. presence lock-in。
- **与 BRINK 不同**（发现 KG-RAG 在 graph incomplete 时 fall back on parametric memory）：将这一现象在 retrieval time operationalize 为 absence lock-in，并新增 presence lock-in（populated but wrong-coherent neighbourhood）变体。
- **与 R2C 不同**（通过 perturbation 测量 dispersion）：关注 unperturbed retrieval 几乎不移动的 lock-in 机制——interventional dose-response 将 chunk overlap 从 0.67 降至 0.29 但 SD-UQ AUROC 保持 0.18，证明 collapse 非 chunk-level artefact。

## 效果
- Dataset: Pooled (6 snapshots) | Metric: Silent error rate (DSE=0) | Result: 42% adaptive KG / 59% dense / 84% strict | Baseline: N/A
- Dataset: Pooled | Metric: Conjunctive audit rule precision | Result: 91.9% (86/1117 selected) | Baseline: 69.7% (accept-all) | Δ: [+22.2%] | Coverage: 7.7%
- Dataset: RealMedQA (clinical) | Metric: Conjunctive rule precision | Result: 100% (48/48) | Coverage: 22%
- Dataset: All 6 snapshots | Metric: KG vs Dense clean accuracy gap | Result: No statistically detectable gap (paired McNemar, all p≥0.12)
- **Ablation**: SD-UQ AUROC (strict vs adaptive): 0.233 vs 0.52, bootstrap 95% CI [0.28, 0.73]
- **Ablation**: 48/66 wrong = silent; 48/48 silent = empty-retrieval (absence lock-in)
- **Ablation**: Single-family gate vs conjunctive: SD-UQ alone 81.4%; conjunctive 91.9% (Δ +10.5%)

## 关键引用
> "When retrieval keeps returning the same context, resampling explores decoder variation but not evidence variation, so agreement reports decoder stability, not correctness." — Section 3.1, p.4

> "The KG-specific risk is auditable wrongness: a silent error arrives with matched entities, typed paths, and provenance anchors, making the system look structurally auditable while it is wrong." — Section 7.2, p.12

> "A system can produce low-variance answers from the wrong subgraph, retrieve a plausible path whose passages do not entail the answer, or retrieve good evidence while the answer remains unstable." — Section 3.3, p.5

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[RetrievalEvaluation]] — Round 9 检索评估概念
- [[retrieval-state-lock-in]] — 本页
- [[beyond-probabilistic-rag-limitations]] — 同轮 RAG 局限性理论分析
- [[is-graphrag-needed]] — Round 9 检索-生成差距
- [[coverage-not-averages]] — Round 9 语义分层检索评估
