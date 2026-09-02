---
title: "制造业知识图谱访问：LLM 与上下文感知提示（Enhancing Manufacturing Knowledge Access with LLMs）"
type: source
tags: [ontology-graph-retrieval]
sources: [manufacturing-knowledge-llm]
source_file: raw/papers/manufacturing-knowledge-llm.pdf
last_updated: 2026-08-31
arxiv_id: "2507.22619"
authors: ["Sebastian Monka", "Irlan Grangel-González", "Stefan Schmid", "Lavdim Halilaja", "Marc Rickart"]
year: 2025
venue: "ECCAI 2026 (European Conference on Artificial Intelligence)"
citation_count: 0
doi: ""
---

## 概要
该论文研究如何利用 LLM 作为中介，帮助非专家通过自然语言查询制造业 Knowledge Graph（如 Bosch 的 Line Information System KG 和 I40 Core Information Model）。作者提出了一套 LLM-based Knowledge Access 框架，包含 Preprocessing and Enrichment（Content Selection + Content Enrichment + Representation）和 Prompting 两个步骤，并系统比较了不同 content selection 策略、representation 格式和 prompt 技术对 SPARQL 查询生成准确性的影响。实验表明，context-aware prompting 技术能显著降低 hallucination 并提高查询准确性，在 Bosch 制造 KG 上实现 20-30% 的准确率提升。

## 解决的问题
制造业 KG（如 LIS KG，覆盖 15+工厂、2700+产线、16000+机器）对非专家难以使用，因为需要编写复杂的 SPARQL 查询。虽然 LLM 有潜力将自然语言转为 SPARQL，但 LLM 在训练中可能未接触领域特定知识，导致生成的查询缺乏领域特异性且容易 hallucinate（生成 ontology 中不存在的 term）。先前工作（如 SGPT 的 embedding+训练方法、基于 GPT3.5 的方法、LangChain 的 GraphSparqlQAChain）多为初步尝试，缺乏对 context-aware content selection 和 enrichment 技术在制造业领域的深入系统性探索。

## 方法与技术
1. **Content Selection（三级策略）**：Entire Ontology（提供完整 ontology）、Naive Reduction（保留核心属性生成子 ontology 以适应 32K token 限制）、Context-based Reduction（使用 RAG 的向量空间相似度检索与问题最相关的 25 个 classes/properties 及其邻居概念）。
2. **Content Enrichment（三种可选增强）**：Ontology-based（启发式规则为 classes/properties 生成额外描述）、LLM-based（通过 thought chain 让 LLM 自反增强）、External Information（整合外部知识库或在线信息）。
3. **Representation（三种格式）**：Graph Structure（RDF Turtle 格式直接输入）、Table Structure（classes/properties 分列表，类似 LangChain 但忽略 inter-class 关系）、Table-Sorted（将 properties 分配到各自所属 class 下，弥补 table 表示的关系丢失）。
4. **Prompt Engineering（三种策略）**：Simple Prompt（问题+ontology+生成指令）、Generic Example（加入通用 SPARQL SELECT 示例）、Domain-specific Example（加入领域特定 question-SPARQL query 对）。
5. **Hallucination Accuracy 评估方法**：将生成 SPARQL 的每个三元组与 ontology 比对计算准确率；qualitative 评估由 3 名领域专家按 0-4 评分 correctness 和 completeness（Fleiss' kappa 0.54/0.29）。

## 创新点
- **系统性的 OntA/B/C/D 四级 content selection 框架**（vs. LangChain 的 GraphSparqlQAChain 仅使用 table 表示且完全忽略 inter-class/class-property 关系）——Context-based Reduction 在完整 ontology 上使用 RAG 检索问题相关概念及其完整定义。
- **Table-Sorted 表示格式**（vs. LangChain table 表示将所有 properties 平铺为独立列表）——将 properties 分配到各自所属 class 下，保留 class-property 归属关系。
- **制造业领域专门的 LLM-KG benchmark**（vs. 先前工作多聚焦 life science 或 scholarly domain）——基于 Bosch 真实 LIS KG（15+工厂、2700+产线）和 CIMM（IEC 国际标准）构建 17 条 business question benchmark，覆盖 5 个 Persona。

## 效果
- Dataset: LIS (GPT3.5) | Metric: Hallucination Accuracy | Result: 0.97 (OntC, Pdomain, table) | Baseline: 0.47 (OntA, Psimple, table-sorted) | Δ: [+106.4%]
- Dataset: LIS (GPT3.5) | Metric: Hallucination Accuracy | Result: 0.96 (OntC, Pdomain, table-sorted) | Baseline: 0.59 (OntA, Psimple, table) | Δ: [+62.7%]
- Dataset: CIMM (GPT4, Pexample graph) | Metric: Hallucination Accuracy | Result: 0.95 (OntB) | Baseline: 0.94 (GPT3.5, OntB) | Δ: [+1.1%]
- Dataset: CIMM (GPT4-32K) | Metric: Correctness Mean (Pexample) | Result: 3.14 (OntC) | Baseline: 2.54 (OntA) | Δ: [+23.6%]
- Dataset: CIMM (GPT4-32K) | Metric: Correctness Mean (Pdomain) | Result: 3.35 (OntC) | Baseline: 2.70 (OntA) | Δ: [+24.1%]
- **Ablation**: OntA vs OntC correctness +23.2%, completeness +29.7%；OntB vs OntC correctness +13.9%, completeness +22.3%
- **Ablation**: Domain-specific example (Pdomain) vs generic example (Pexample): accuracy +5-8%
- **Overall**: context-aware reduction accuracy gain 20-30% across all benchmark queries

## 关键引用
> "Ontologies can sometimes be expansive or cluttered, containing a wealth of classes and properties that may not all be pertinent to a given task." — Section 3.1.1, p.2-3

> "a context-based reduced ontology, e.g. OntC, is designed to streamline only preselected domain-specific information. Therefore, it appears to aid in better information memorization and recall, as suggested by the observed increase in accuracy." — Section 4.3, p.5

> "the reduction of the ontology helps the LLM to focus on the relevant concepts. Furthermore, the performance improvement between variant OntB and OntC highlights that the LLMs can leverage the additional semantics provided by a rich ontology." — Section 4.4, p.6-7

## 关联
- [[OntologyGuidedQueryGeneration]] — 本体引导查询构造
- [[rag-autoconfig-industrial-fieldbus]] — Round 15 ECLASS 本体图+混合检索工业配置
- [[intent-driven-smart-manufacturing]] — Round 14 LLM+本体对齐 KG 翻译 NL 意图为 ISA-95 JSON
- [[OntologySemanticLayer]] — Round 13 本体语义层概念
- [[EmbeddingModels]] — Round 9 嵌入模型概念
