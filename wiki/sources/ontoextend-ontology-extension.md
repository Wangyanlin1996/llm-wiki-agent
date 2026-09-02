---
title: "OntoExtend: 需求驱动的可扩展本体扩展框架（Requirement-driven Ontology Extension with LLMs）"
type: source
tags: [ontology-graph-retrieval]
sources: [ontoextend-ontology-extension]
source_file: raw/papers/ontoextend-ontology-extension.pdf
last_updated: 2026-08-31
arxiv_id: "2607.17963"
authors: ["Anna Sofia Lippolis", "Mohammad Javad Saeedizade", "Stefan Schmid", "Simon Blattner", "Robin Keskkisälä"]
year: 2026
venue: "Semantics 2026"
citation_count: 0
doi: ""
---

## 概要
OntoExtend 是一个需求驱动的 ontology extension 框架，使用 RAG 从输入 ontology 中检索相关元素，并结合 competency questions（CQs）引导 LLM 生成 ontology 扩展片段。框架由 Ontology Retriever（语义检索）、Ontology Extender（LLM 生成+两阶段验证）和 Ontology Integrator（去重拼接+重新索引）三个子系统组成。在 39 个 CQs（来自 EU-project Onto-DESIDE 和 Bosch 工业 ontology）上的评估显示，生成的片段几乎没有语法错误、未引入 critical OOPS! pitfalls、CQ 验证全部通过，ontology 工程师评定为仅需 minor 到 moderate 修订。

## 解决的问题
现有 LLM-based ontology 生成方法主要关注从零构建 ontology，很少将 ontology 扩展显式绑定到 requirements（CQs）或可复用的 core models 上。Phrase2Onto 仅限于 toy ontologies 且无法 scale；Taxoria 专注于 taxonomy enrichment 但无法控制 hallucinated nodes 和 implicit requirement capture；Kholmska 等人的 multi-LLM workflow 在专业领域需要 manual repair of shallow suggestions。核心痛点是：输入 ontology 往往包含数百个 class 和 property，超出 LLM 上下文窗口；即使能放入大 context window，LLM 也会被 irrelevant details 误导产生 off-target 或 inconsistent outputs。

## 方法与技术
1. **Ontology Retriever**：解析 OWL 实体（classes, object properties, data properties, annotations, SHACL shapes），构造包含 IRI、label、comment、domain/range、sub-class 关系的 OntologyElement 记录；每个元素用 pipe-delimited 字符串序列化，通过 sentence embedding 模型编码后存入 FAISS 索引，查询时将 CQ 嵌入同一向量空间检索 top-k（默认 20）相关元素。
2. **Ontology Extender**：检索元素按源 ontology 分组渲染为 Turtle snippets 注入 prompt，构造统一 namespace prefix block；支持两种 prompt 模板——SHACL-based（工业场景）和 OWL restrictions-based（EU-project 场景）；通过两阶段验证器（Turtle parser 验证语法 + constraint checker 验证 domain/range 声明等建模规范），失败则 retry 或 flag。
3. **Ontology Integrator**：对生成的 fragment 进行 deduplication（移除重复 axioms、classes、properties、prefixes）后与输入 ontology 拼接；将 fragment 转发给 Retriever 重新索引以促进跨 fragment consistency。
4. **多维评估方法学**：结构指标（OOPS! pitfall scanner + Pellet reasoner consistency check + RDFLib 语法检查）、功能指标（CQ verification 通过 SPARQL 查询验证 + refined superfluous elements 计数）、人工评估（6 位 ontology 工程师按 Correctness 和 Completeness 两维 5 分 Likert scale 评分）。
5. **数据集构造**：系统性移除选定 classes 及其相关 properties，迭代扩展子类移除过程，为被移除元素构造 CQs——每个 CQ 询问对应 class 及其 properties 在原 ontology 中代表或实现什么。

## 创新点
- **与 Phrase2Onto 不同**（仅限 toy ontologies）：OntoExtend 通过 RAG 检索机制直接将 retrieval 集成到 extension 过程中，可处理大规模真实 ontology（如 75K tokens 的 EU-project ontology）。
- **与 Taxoria 不同**（仅 taxonomy enrichment，无法控制 hallucinated nodes）：OntoExtend 支持完整 OWL axioms 和 SHACL shapes 生成，并通过两阶段验证器确保语法正确性和建模规范。
- **与 Kholmska 等人及多数先前工作不同**（minimal to no formal evaluation）：OntoExtend 提出多维评估方法学，是唯一在全部 10 个评估维度上均满足的工作。
- **与 García-Fernández 等人不同**（发现 LLM-generated extension 比 manual gold standard 更浅）：OntoExtend 生成的片段 superfluous elements 少于 2%，而先前工作报告约 30%。

## 效果
- Dataset: EU-Project + Industry | Metric: CQ-verification pass rate | Result: 100% (o1-preview 100%, GPT-5 100%) | Baseline: Prior work reported CQ modelling issues | Δ: [N/A]
- Dataset: EU-Project + Industry | Metric: Superfluous elements % | Result: EU 2% (o1 3.8%, GPT-5 0%); Industry 0% | Baseline: ~30% [16] | Δ: [−28%]
- Dataset: Industry | Metric: Survey Correctness (1-5) | Result: o1-preview 4.91 (Fleiss Po 0.97); GPT-5 4.96 (Po 0.98) | Baseline: N/A
- Dataset: Industry | Metric: Survey Completeness (1-5) | Result: o1-preview 4.56 (Po 0.89); GPT-5 4.54 (Po 0.87) | Baseline: N/A
- Dataset: EU-Project | Metric: Survey Correctness (1-5) | Result: o1-preview 3.69 (Po 0.80); GPT-5 3.66 (Po 0.87) | Baseline: N/A
- Dataset: EU-Project + Industry | Metric: Syntax errors % | Result: EU 0% (both); Industry 2.5% | Baseline: N/A
- **Ablation**: Embedding model comparison: text-embedding-ada-002 (Pipe, Comments) Mw=0.63 vs text-embedding-3-small (Newline, Comments) Mw=0.62 — 嵌入模型选择影响较小

## 关键引用
> "input ontologies often contain hundreds of classes and properties, exceeding the input context limitations of current LLMs. Even when an ontology is small enough to fit within the large context window of state-of-the-art LLMs, they may be misguided by irrelevant details and produce off-target or inconsistent outputs" — Section 1, p.2

> "the ontology fragments generated in this work contain fewer than 2% unnecessary elements, whereas [16] reported around 30% superfluous elements in their generated ontologies (35% with [16]'s original definition)" — Section 6.2, p.12

> "LLM performance can serve as a proxy indicator for the quality of requirements (CQs) and/or ontological artefacts" — Section 7, p.14

## 关联
- [[OntologyGuidedQueryGeneration]] — 本体引导查询构造
- [[auto-ontology-construction-llm]] — Round 13 LLM 外部本体记忆层
- [[automated-ontology-generation-multi-agent]] — Round 15 多 agent LLM 本体生成
- [[llm-ontology-engineering-legal-kg]] — Round 14 两阶段本体工程
- [[OntologyReasoning]] — Round 13 本体推理概念
