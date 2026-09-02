---
title: "AgentMap: 联合等价与包含发现用于本体匹配（Joint Equivalence and Subsumption Discovery for Ontology Matching）"
type: source
tags: [ontology-graph-retrieval]
sources: [agentmap-ontology-matching]
source_file: raw/papers/agentmap-ontology-matching.pdf
last_updated: 2026-08-31
arxiv_id: "2607.27130"
authors: ["Yiping Song", "Jiaoyan Chen", "Renate A. Schmidt", "Hui Yang", "Wen Zhang"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
本文引入 Hybrid Ontology Matching（HOM）新任务，统一 equivalence 和 subsumption 发现，并提出基于 LLM 的多智能体框架 AgentMap。给定源本体中的概念，AgentMap 集成语义检索、层次搜索和协作式多智能体 LLM 推理，逐步探索目标本体，识别等价概念或最细粒度 subsumer。系统由三个专门化智能体组成：AgentES（初始等价筛选）、AgentEV（等价验证）、AgentSD（迭代 subsumption 发现），采用等价优先策略。在四个扩展的 OM 数据集上评估，AgentMap 在 HOM 设置和传统设置上均优于基线。

## 解决的问题
传统本体匹配（OM）系统仅能发现单一类型的语义对应关系——要么 equivalence 要么 subsumption——无法同时发现两种映射。现有系统如 LogMap、AML、BERTMap 和 GenOM 专注于 equivalence matching，而 BERTSub 等少数系统仅针对 subsumption matching 的候选排序。在实际知识集成场景中，源概念是否在目标本体中有精确匹配或仅有更宽泛的匹配事先未知，需要同时考虑两种关系类型。此外，BERTSub 假设正确 subsumer 已在候选列表中，仅评估候选排序而非本体范围的 subsumption 发现。

## 方法与技术
1. **双候选集语义检索**：提取概念文本信息（标签和同义词），使用 OpenAI text-embedding-3-small 编码为语义嵌入，按余弦相似度排序。构建两个候选集：小集合 C0（top-5，供 agent 模块 LLM 推理）和大集合 C+（top-20，供词法匹配）。
2. **三智能体等价优先推理流水线**：AgentES 接收源概念和 C0，通过 LLM 推理判断是否存在有效等价概念。若识别到等价候选，传递给 AgentEV。AgentEV 构建参考候选集（包含候选的直接父概念和子概念）通过 LLM 推理比较验证等价性。若未识别等价概念，触发 AgentSD。
3. **层次引导的迭代 subsumption 搜索**：AgentSD 在第 i 次迭代中对候选集进行 LLM 推理判断是否存在有效 subsumer。若未找到，通过收集候选集中所有概念的直接父概念更新候选集，逐层向上遍历本体层次结构，直到找到有效 subsumer 或达到最大迭代 d_max=2。
4. **词法匹配与冲突解决**：并行于 agent 推理，词法匹配模块在 C+ 上比较标签和同义词预测等价对应。冲突解决规则：词法匹配输出等价而 agent 输出 subsumer → 返回词法结果（等价优先）。
5. **HOM 基准数据集构建**：基于 OAEI Bio-ML 三个医学数据集和 HeLiS-FoodOn 数据集，将源概念重组为等价和 subsumption 两个不相交子集。

## 创新点
- **首次提出 Hybrid Ontology Matching（HOM）任务**（vs. 现有系统 LogMap/AML/BERTMap/BERTSub/GenOM 仅处理单一匹配类型）——统一 equivalence 和 subsumption 发现为单一任务。
- **分阶段多智能体推理替代单步 LLM 判断**（vs. LLM+Neighbour+CoT 基线在单次调用中同时决定等价和 subsumption）——消融显示移除层次搜索使 subsumption 准确率下降 58.2%。
- **本体结构引导的迭代搜索**（vs. BERTSub 假设正确 subsumer 在预定义候选列表中、嵌入方法被动排序）——AgentSD 逐层向上遍历本体层次，主动搜索而非被动排序，subsumption 准确率从 0.046 提升至 0.398（+765%）。
- **跨 LLM backbone 的框架有效性验证**：在 GPT-4.1-mini、Qwen2.5-32B/72B、Llama3.1-70B 上均稳定表现，表明改进主要来自推理框架而非 backbone LLM。

## 效果
- Dataset: SNOMED-FMA-Body | Metric: OverallAcc (HOM) | Result: 0.657 | Baseline: 0.634 (LLM+Neighbour+CoT) | Δ: [+3.6%]
- Dataset: SNOMED-NCIT-Pharm | Metric: OverallAcc (HOM) | Result: 0.523 | Baseline: 0.454 | Δ: [+15.2%]
- Dataset: SNOMED-FMA-Body | Metric: Acc_eq | Result: 0.957 | Baseline: 0.906 (AML) | Δ: [+5.6%]
- Dataset: SNOMED-NCIT-Pharm | Metric: Acc_eq | Result: 0.981 | Baseline: 0.919 (AML) | Δ: [+6.7%]
- Dataset: SNOMED-FMA-Body | Metric: Acc_sub | Result: 0.401 | Baseline: 0.191 (BERTSub) | Δ: [+110%]
- Dataset: SNOMED-NCIT-Pharm | Metric: Acc_sub | Result: 0.398 | Baseline: 0.046 (BERTSub) | Δ: [+765%]
- Dataset: NCIT-DOID-Disease | Metric: Acc_sub | Result: 0.564 | Baseline: 0.336 (BERTSub) | Δ: [+68%]
- **Ablation**: w/o Hierarchical Search: SubAcc 0.148 (−58.2%) — 层次搜索是 subsumption 的核心
- **Ablation**: w/o LM&CR: EqvAcc 0.941 (−1.7%) — 词法匹配冲突解决对等价贡献较小

## 关键引用
> "decomposing HOM into staged semantic decisions, combined with iterative ontology-guided search, is substantially more effective than single-step reasoning over a fixed candidate set" — Section 4.4, p.8

> "purely ranking is insufficient for subsumption matching and it requires progressively exploring the hierarchy through iterative agent-based reasoning" — Section 4.4, p.10

> "this staged decomposition, rather than candidate coverage or backbone strength, drives AgentMap's gains, suggesting iterative, structure-aware reasoning as a general principle for LLM agents over hierarchical structures" — Section 6, p.12

## 关联
- [[OntologyMatching]] — Round 14 本体匹配概念
- [[open-ontologies-stable-matching]] — Round 14 稳定匹配对齐
- [[anchor-schema-agnostic-ontology]] — Round 14 混合本体发现+SHACL 验证
- [[kroma-ontology-matching-rag]] — Round 15 RAG 增强本体匹配
- [[OntologyGuidedQueryGeneration]] — 本体引导查询构造
