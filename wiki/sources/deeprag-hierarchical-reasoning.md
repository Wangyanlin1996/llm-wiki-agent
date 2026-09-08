---
title: "DeepRAG: 层次化推理与过程监督的生物医学多跳问答（Hierarchical Reasoning + Process Supervision for Biomedical QA）"
type: source
tags: [ontology-precise-retrieval]
sources: [deeprag-hierarchical-reasoning]
source_file: raw/papers/deeprag-hierarchical-reasoning.pdf
last_updated: 2026-09-08
arxiv_id: "2506.00671"
authors: ["Yuelyu Ji", "Hang Zhang", "Shiven Verma", "Hui Ji", "Chun Li"]
year: 2025
venue: "BioCreative IX at IJCAI 2025"
citation_count: 0
---

## 概要
DeepRAG 是一个整合 DeepSeek R1 hierarchical reasoning 与 RAG-Gym process-level supervision 的框架，面向 MedHopQA 生物医学多跳问答任务。通过将复杂查询分解为精确子查询，并引入基于 UMLS ontology 的 concept-level reward signals 来增强生物医学准确性。在 MedHopQA 数据集上的评估表明，DeepRAG 在 Exact Match 和 Concept Accuracy 上均显著优于 baseline models。

## 解决的问题
生物医学多跳问答需要跨基因、疾病、治疗等异构来源的顺序推理，现有 LLM 难以处理此复杂性。DeepSeek 虽具备层次化推理能力，但不显式管理多层级推理依赖关系；RAG-Gym 提供过程级奖励优化，但使用 LLaMA backbone 缺乏对生物医学查询的层次化分解精度。两者单独使用均无法充分满足生物医学多跳 QA 的需求。

## 方法与技术
1. **两阶段层次化推理管线**：Reasoning Module 生成结构化答案大纲，识别需外部检索的 claim；Query Module 据此构造精确子查询，优化检索过程。
2. **Hierarchical Indicators**：显式跟踪嵌套推理依赖和查询层级，清晰划分推理路径并优化检索聚焦。
3. **Process Supervision via MDP**：将问答过程建模为 Markov Decision Process，每个子查询作为离散 action，RAG-Gym 通过三类奖励（Sufficiency Reward、Utility Reward、Redundancy Penalty）引导检索与生成。
4. **Concept-Level Rewards**：基于 UMLS semantic matching 的奖励信号，强化语义精度和生物医学准确性，确保检索和生成信息与精确生物医学概念对齐。
5. **DPO 微调**：使用 ChatGPT-4o 生成约 1,000 条标注查询轨迹，通过 Direct Preference Optimization 调整模型参数。

## 创新点
- **层次化推理模块 + 指示器**（vs standalone DeepSeek 不显式跟踪多层级嵌套依赖）——mitigate reasoning redundancy。
- **Backbone 替换**（vs RAG-Gym 的 LLaMA）——将 LLaMA 替换为 DeepSeek R1 distilled variant，显著提升生物医学子查询精度。
- **Concept-Level Rewards（UMLS-based）**（vs RAG-Gym 原有三类奖励无语义级奖励）——针对生物医学术语精度设计。

## 效果
- Dataset: MedHopQA | Metric: EM | Result: 62.4% | Baseline: 54.3% (DeepSeek) | Δ: [+8.1%]
- Dataset: MedHopQA | Metric: EM | Result: 62.4% | Baseline: 57.7% (RAG-Gym) | Δ: [+4.7%]
- Dataset: MedHopQA | Metric: Concept Accuracy | Result: 71.8% | Baseline: 66.5% (DeepSeek) | Δ: [+5.3%]
- Dataset: MedHopQA | Metric: Concept Accuracy | Result: 71.8% | Baseline: 68.3% (RAG-Gym) | Δ: [+3.5%]
- **Ablation**: w/o Hierarchical Reasoning: EM 57.4% (−5.0) — 层次化推理贡献最大
- **Ablation**: w/o Concept-Level Rewards: Concept Accuracy 67.6% (−4.2) — 对 Concept Accuracy 影响最大

## 关键引用
> "Our framework employs DeepSeek R1, a distilled version of LLaMA optimized for hierarchical reasoning, particularly suited for complex biomedical multi-hop queries." — Section 2.1, p.2

> "The integration of hierarchical reasoning outputs from DeepSeek into RAG-Gym transforms the question-answering process into a sequential Markov Decision Process (MDP)." — Section 2.2, p.2

> "Replacing the vanilla LLaMA in RAG-Gym with DeepSeek R1 significantly enhances the precision of the generated sub-queries." — Section 3.5, p.4

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[r2-searcher]] — Round 9 多跳推理检索-推理边界校准
- [[kbsd-knowledge-boundary]] — Round 9 知识边界校准三决策
- [[ontology-evidence-path-kgqa]] — Round 16 本体引导证据路径推理
- [[deeproot-kg-multi-agent]] — Round 16 KG 协调多 Agent 医疗推理
