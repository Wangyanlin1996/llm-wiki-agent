---
title: "RAGged Events: RAG 增强事件知识库构建与证明助手推理（Event KB Construction + Proof Assistants）"
type: source
tags: [ontology-precise-retrieval]
sources: [ragged-events-reasoning]
source_file: raw/papers/ragged-events-reasoning.pdf
last_updated: 2026-09-08
arxiv_id: "2506.07042"
authors: ["Stergios Chatzikyriakidis"]
year: 2025
venue: "arXiv preprint"
citation_count: 0
---

## 概要
本文系统比较了三种 LLM enhancement 策略（direct generation、knowledge-graph augmentation、RAG）在历史事件知识库构建中的表现，以 Thucydides《伯罗奔尼撒战争史》为 case study。研究发现 enhancement 效果与模型能力呈反向关系（inverse calibration principle）：强模型在 base generation 下最优，external enhancement 反而引入 hallucination；弱模型受益于简单 RAG 但在复杂配置下出现灾难性崩溃。为弥补 RDF/OWL 的表达力限制，作者开发了 RDF→Coq proof assistant 的自动翻译管线，支持 BCE 日期的时间算术、多步因果推理和领域特定事件类型的形式化验证。

## 解决的问题
历史事件知识库的手工构建计算成本高且劳动密集。现有 RDF/OWL reasoning 机制局限于 first-order logic 的可判定子集，无法处理复杂时间语义、多步因果推理和历史分析所需的高阶查询。RAG 在通用 NLP 任务中表现良好，但在 knowledge-rich 历史领域是否有效仍是开放问题——"外部知识增强普遍提升性能"的假设可能不成立。

## 方法与技术
1. **三策略对比框架**：Base Generation（纯 LLM 推理无外部知识）、Knowledge Enhanced（KG retrieval from Wikidata/DBpedia/ConceptNet + LACRIMALit ontology location enrichment）、RAG Enhancement（FAISS vector store + KG enhancement 多源融合）。
2. **级联查询管线**：location enrichment 按 LACRIMALit → Wikidata → DBpedia 顺序查询，成功即停；MD5-based caching 最小化 API 调用。
3. **RDF→Coq 四阶段翻译管线**：(1) Ontological Discovery Validation 分析 RDF class hierarchy；(2) Type System Construction 映射 RDF classes 到 Coq inductive types，支持 BC 日期算术；(3) Relationship Formalization 多步因果推理通过 function composition；(4) Theorem Generation 生成可验证的因果命题定理。
4. **标准化 RDF/Turtle 输出**：所有输出使用一致属性确保跨策略直接比较。
5. **确定性实验设置**：所有模型 temperature=0，相同 chunking 参数，相同 structured prompt。

## 创新点
- **Inverse Calibration Principle（反向校准原理）**——首次系统论证 enhancement 效果与模型能力反向相关。强模型 base 最优，RAG 反而引入 hallucination；弱模型呈 inverted-U pattern（简单 RAG 提升→复杂 RAG 灾难性崩溃）。直接挑战"更多检索必然更好"的假设。
- **RAG-discovered event types 的形式化验证**——RAG 发现的 domain-specific event types 违反 DBpedia constraints 但被 Coq type system 接受为合法语义结构，通过数学证明验证其 semantic legitimacy。
- **RDF→Coq 翻译管线**——首次将 RAG-extracted knowledge 转化为 proof assistant specifications，支持 RDF/OWL 无法实现的高阶推理。
- **超越 SWRL 的表达力**——Coq complement 而非 replace SWRL，实现 formal arithmetic 和多步因果证明。

## 效果
- Dataset: Thucydides | Metric: Events Extracted | Result: 39 (Claude Base) | Baseline: 10 (LLAMA Base) | Δ: [+290%]
- Dataset: Thucydides | Metric: Events Extracted | Result: 38 (LLAMA RAG 1) | Baseline: 10 (LLAMA Base) | Δ: [+280%]
- Dataset: Thucydides | Metric: Events Extracted | Result: 0 (LLAMA RAG 4) | Baseline: 10 | Δ: [−100% catastrophic collapse]
- **Key finding**: GPT-4o Base 36 events → RAG+Multi KG 3: 20 events（RAG 持续降低 coverage）
- **Key finding**: Claude Base 39 → RAG+Multi KG 1: 10 events（RAG 降低 74% coverage）

## 关键引用
> "Our analysis reveals counterintuitive findings that fundamentally reshape understanding of when and how external knowledge augmentation should be applied. Our investigation uncovers an 'inverse calibration principle' where enhancement effectiveness inversely correlates with model capability." — Section 1, p.2

> "LLAMA exhibits the most dramatic variation in performance, revealing a brittle failure mode under complex enhancement conditions." — Section 3.2, p.7

> "This translation architecture validates our central claim: RAG-discovered event types that do not appear in the event database but can be used to extend the ontology to represent valuable semantic innovations." — Section 4.4, p.12

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[is-graphrag-needed]] — Round 9 检索-生成差距
- [[beyond-probabilistic-rag-limitations]] — Round 16 RAG 法律领域局限
- [[retrieval-state-lock-in]] — Round 16 RAG 检索状态锁定
- [[OntologyReasoning]] — Round 13 本体推理
