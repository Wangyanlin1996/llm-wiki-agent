---
title: "DeepRoot: KG 协调多智能体治疗推理（KG-Coordinated Multi-Agent for Therapeutic Reasoning）"
type: source
tags: [ontology-graph-retrieval]
sources: [deeproot-kg-multi-agent]
source_file: raw/papers/deeproot-kg-multi-agent.pdf
last_updated: 2026-08-31
arxiv_id: "2606.15931"
authors: ["Zijian Carl Ma", "Sean J. Wang", "Sijbren Kramer", "Li Erran Li"]
year: 2026
venue: "ICML 2026 Workshop (GenBio / ACM CAIS)"
citation_count: 0
doi: ""
---

## 概要
DeepRoot 是一个多智能体 LLM 系统，通过联合构建和利用经验证的知识图谱（KG），将历史医学文本转化为可审计的药物发现线索。系统分为 Assembly 阶段（7 个专门化智能体填充 Neo4j 知识图谱）和 Discovery 阶段（通过 Critic 和 Discovery 智能体进行 Cypher 子图遍历来评估治疗声明）。在《神农本草经》语料上，DeepRoot 恢复了 21 个留出 compound–disease 治疗对中的 10 个（R@20=47.6%），远超 raw-corpus LLM 的 4.8%，且幻觉率仅 7–10%，远低于 tool-calling LLM 的 87%。

## 解决的问题
历史医学文献（如《神农本草经》）包含前本体论散文（pre-ontological prose）和非标准分类法（idiosyncratic taxonomies），无法直接用于现代生物医学流水线。现有 LLM agent 系统——无论是 tool-calling、RAG 还是 agentic deep-research——都无法将这类文本大规模转化为可验证的药物发现线索。先前方法如 TCMChat、Evi-BERT 将文本视为纯分类问题，缺乏基于验证生物学证据或机制本体的推理链；OpenTCM 虽采用 Graph-RAG 架构，但其构建依赖专家监督和纯 LLM 生成的输出，且未对图谱与智能体分解进行消融实验。

## 方法与技术
1. **七智能体 Assembly 流水线**：Extractor 从原始文本提取 Source/Malady/Preparation 节点；Auditor 规范化源并归档未通过子串验证的证据；三个 Linker 将实体锚定到 COCONUT2.0/PubChem（化合物）、ChEMBL（靶点）、Open Targets（靶点-疾病关联）；Malady-Disease Mapper 采用 generate-then-verify 协议；Reviewer 归档孤儿和域外实体。
2. **Neo4j 知识图谱 Schema**：6 种节点类型（Source, Traditional Malady, Modern Disease, Chemical Compound, Biological Target, Preparation Method）和 7 种边类型。治疗声明可验证当其机制环闭合：Source→Traditional Malady→Modern Disease 且 Source→Chemical Compound→Biological Target→同一 Modern Disease。
3. **实体身份坍缩机制**：化合物身份使用 RDKit 计算的 InChIKey，靶点身份使用 ChEMBL ID，现代疾病身份使用规范名称并回填 ICD-10/MeSH/SNOMED/MONDO/DOID 编码。所有写入均为基于身份的幂等 MERGE 操作。
4. **Discovery 阶段 Cypher 遍历**：Critic Agent 使用 Neo4j Cypher 进行子图遍历来评估治疗声明的机制合理性；Discovery Agent 基于 KG 路径进行候选化合物重排序。
5. **盲恢复实验设计**：删除 KNOWN_TREATS 边及所有立体化学兄弟节点后，让系统从 87–1,954 个候选化合物（中位数 835）中重新排序，对比 random R@20≈2.4% 验证 KG 支持发现能力。

## 创新点
- **首次将 grounding 和 reasoning 作为可分离轴进行组合**：Graph-only 推理幻觉率 0%但推理连贯性最低（RC=2.69），LLM-only 连贯性较高但幻觉率 13%，DeepRoot KG+LLM 是唯一在两个轴上同时获胜的条件——对比 Tool-call LLM（可访问相同 API 但幻觉率 87%）。
- **Agent 式 KG 构建替代推理时 API 调用**：DeepRoot Assembly 为一次性调用（约$0.25/语料），而 Tool-call LLM 在推理时访问相同 API 仍产生 87%幻觉率，表明构建验证 KG 能以推理时查询无法实现的方式抑制幻觉。
- **与 OpenTCM 对比**：OpenTCM 依赖专家监督和纯 LLM 生成的输出构建图谱，DeepRoot 通过 7 个智能体结合 LLM 规范化与策展生物数据库严格验证。
- **自置信度受检索精度约束**：LLM 基线自置信度 0.87（高幻觉），DeepRoot 自置信度 0.48（与其 source recall@3=0.41 对齐）。

## 效果
- Dataset: 神农本草经 (21 held-out pairs) | Metric: R@20 | Result: 47.6% | Baseline: 4.8% (raw-corpus LLM) | Δ: [+891%]
- Dataset: 神农本草经 | Metric: R@10 | Result: 33.3% | Baseline: 4.8% | Δ: [+594%]
- Dataset: 30 source→malady claims | Metric: Overall score [1,5] | Result: 3.83 (DeepRoot Pro) | Baseline: 2.47 (Tool-call LLM) | Δ: [+55%]
- Dataset: 30 claims | Metric: Hallucination rate | Result: 0.07 (DeepRoot Flash) | Baseline: 0.87 (Tool-call LLM) | Δ: [−92%]
- Dataset: 30 claims | Metric: Reasoning coherence (RC) | Result: 3.97 (DeepRoot Pro) | Baseline: 2.69 (Graph-only) | Δ: [+48%]
- **Ablation**: Edge perturbation 50% → Critic confidence converges to raw LLM baseline; >50% → score drops to 0.30
- **KG stats**: 21,111 nodes / 52,467 edges

## 关键引用
> "Our results suggest that building a verified knowledge graph suppresses hallucination in a way that querying those resources at inference time does not." — Section 4, p.4

> "Around 50% perturbation, the critic's confidence converges with the raw LLM baseline, suggesting that the KG signal has been degraded enough that the critic behaves similarly to an LLM without structured graph support." — Section 3.1, p.2

> "For corpora that predate modern ontologies, retrieval-augmented and tool-using agents need a construction pass first, rather than on-demand calling." — Section 4, p.4

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[OntologyGroundedRAG]] — 本体 grounding RAG
- [[ontologyrag-biomedical-code-mapping]] — Round 15 本体 KG+RAG 代码映射
- [[neuron-clinical-explainability]] — Round 13 SNOMED CT 本体增强临床可解释性
- [[qime-ontology-embeddings]] — Round 10 本体驱动可解释医学嵌入
