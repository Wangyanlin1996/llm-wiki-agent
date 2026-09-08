---
title: "SCX Router: 任务本体驱动零样本模型选择（Streaming Zero-Shot Model Selection with Task Ontology）"
type: source
tags: [ontology-skill-routing]
sources: [scx-router-task-ontology]
source_file: raw/papers/scx-router-task-ontology.pdf
last_updated: 2026-09-08
arxiv_id: "2609.02292"
authors: ["Ihor Stepanov", "Aleksandr Smechov", "Mykhailo Shtopko", "Dmytro Vodianytskyi", "Oleksandr Lukashov"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
---

## 概要
SCX Router 把 LLM 模型选择重新定义为轻量级动态标签分类任务，而非额外的生成任务。其约 0.6B 参数的 checkpoint 基于 GLiClass 架构，用 Qwen3 causal decoder 配合 shallow bidirectional scorer，在不做 autoregressive generation 的情况下为每个候选 endpoint 输出 suitability score。同一 checkpoint 还预测 task type、difficulty、reasoning mode 与 expected output length，并支持自定义零样本标签。论文构建了含 23 family / 115 task type / 345 subtype 的 task ontology，并据此生成 150,000 个 verifier-scored 任务。

## 解决的问题
推理 endpoint 在质量、价格、延迟、上下文支持、工具使用与领域专长上高度异构，人工启发式难以维护。既有方案如 FrugalGPT（cascade）、RouteLLM（binary strong-vs-weak gate）要么固定为二选一 gating、要么把 routing 当作生成任务带来 decoding 延迟与输出格式方差，且无法在会话内复用对话状态来反复路由。

## 方法与技术
1. **Decoder-KV 持久/瞬态分离**：causal decoder 处理对话上下文，对话走持久 KV cache（仅增量编码新轮次），label tokens 作为 transient suffix 单独评分且不回写缓存，换 label 时不污染对话状态。
2. **GLiClass label-conditioned scorer**：在 Qwen3-0.6B causal backbone 后接 2-layer DeBERTa-v2 bidirectional encoder，从 separator 提取 request 表示和 label 表示，拼接后经共享 MLP 出 per-label logit。
3. **Multi-label 训练 + label shuffling**：用 masked binary cross-entropy，每行只 tokenize 标签并打二值目标，训练时打乱 label 顺序避免位置捷径。
4. **Task Ontology 三层结构**：family→task type→routable subtype（23/115/345），正交叠加 8 sector / 30 domain 领域轴与 8 个 cross-cutting 维度，组合出 10,350 个 design cell。
5. **Cache-aware 部署策略**：把 suitability 信号与增量成本、缓存可复用概率分离，安全/隐私/区域/工具权限作为 hard filter。

## 创新点
- **Multi-label 动态标签 vs 固定 binary gate**（vs RouteLLM 固定 strong/weak 二选一、FrugalGPT cascade escalation）——对可配置 roster 做 multi-label suitability 预测，标签是 in-band 输入。
- **Decoder-KV 持久会话缓存**（vs embedding/bi-encoder 需重嵌入全文、generative LLM router 需 decoding+parsing）——只编码新文本、重打 label 分。
- **将 routing 监督从 outcome 显式分离为多个独立预测头**——同一 checkpoint 同时输出 model suitability / task type / difficulty / reasoning mode / output length / hallucination。
- **Real-world task ontology + 165k 合成任务**——任务包含 dialogue state、工具、文件、repository 上下文与 acceptance criteria。

## 效果
- Dataset: LiveBench 1000-task | Metric: Top-1 score | Result: 0.707 | Baseline: 0.696 (fixed@1) | Δ: [+1.7%]
- Dataset: 8-endpoint routing | Metric: Macro F1 | Result: 0.7586 | Precision: 0.7688 / Recall: 0.7411
- Dataset: Difficulty (5-class) | Metric: Top-1/2/3 hit rate | Result: 0.507 / 0.748 / 0.873
- **Ablation**: k=1: 0.696→0.707 (+0.012); k=3: 0.837→0.824 (−0.013) — router 在 k=3 反而劣于 fixed，优势依赖候选模型间有意义分歧

## 关键引用
> "SCX Router differs along three axes. First, it performs multi-label suitability prediction over a configurable roster rather than a fixed binary gate." — Section 2.1, p.3

> "The decoder-KV design occupies a middle point: labels remain dynamic, the backbone is causal and cacheable, and the output is discriminative." — Section 2.2, p.3

> "These results support a narrower conclusion than 'routing always wins.' The router is most useful where candidate outcomes disagree and request semantics reveal that disagreement." — Section 10.3, p.16

## 关联
- [[OntologyGuidedQueryGeneration]] — 本体引导查询构造
- [[ModelRouting]] — Round 11 模型动态路由概念
- [[dynamic-ontology-llm-agents]] — Round 16 动态本体内核
- [[HyDRA]] — Round 11 混合动态路由
- [[routing-plateau]] — Round 11 路由准确率上限
