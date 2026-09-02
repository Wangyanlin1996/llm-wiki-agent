---
title: "Ontology-Driven Graph RAG for Legal Norms（法律规范本体驱动 Graph RAG）"
type: source
tags: [ontology-graph-retrieval]
sources: [ontology-driven-graph-rag-legal]
source_file: raw/papers/ontology-driven-graph-rag-legal.pdf
last_updated: 2026-08-31
arxiv_id: "2505.00039"
authors: ["Hudson de Martim"]
year: 2025
venue: "JURIX 2025"
citation_count: 0
doi: ""
---

## 概要
本文提出 SAT-Graph RAG（Structure-Aware Temporal Graph RAG），一个面向法律规范的 ontology-driven Graph RAG 框架。基于 LRMoo 本体模型，将抽象法律 Work 与其版本化 Expression 分离，将时间状态建模为复用未变更组件的高效聚合（Aggregation），并将立法事件具象化为一等公民的 Action 节点。通过 planner-guided 查询策略，框架能够确定性地处理 point-in-time 检索、层级影响分析和可审计溯源重建三类复杂查询。

## 解决的问题
标准 flat-text RAG 系统对法律文本的层级结构（标题、章节、条款）和历时性演变（修正案、废止、合并）视而不见，导致产生时代错位（anachronistic）和事实错误的答案。现有 Graph RAG 采用实体抽取（NER）构建图，但 NER 优化针对专有名词，而法律文本的核心语义实体是抽象法律概念（如"行政行为""正当程序"），导致图稀疏且语义贫乏。Temporal Knowledge Graph 研究虽有表示方法，但鲜有将法律规范的文章/法律版本演变与 RAG 机制、provenance 结合的工作。

## 方法与技术
1. **多层本体图结构**：基于 LRMoo 本体定义四类节点——Norm（Work，抽象法律创作）、Component（Component Work，层级元素如条款）、Temporal Version/CTV（时间戳语义快照，对应 Expression）、Language Version/CLV（具体语言文本实现），实现"what/when/how"分离。
2. **聚合式版本传播（Aggregation, 非 Composition）**：当某组件被修正时，仅为该组件创建新 CTV，父组件的新 CTV 通过聚合最近子 CTV 形成——复用未变更子组件的旧 CTV，避免数据冗余并精确标识实际变更内容。
3. **Action 节点因果具象化**：为每个粒度变更创建 Action 节点，连接源条款（instrument）、被终止的旧 CTV 和产生的新 CTV，并生成描述性 Text Unit，使因果链可直接检索和遍历。
4. **Multi-aspect 检索**：为每个关键实体生成多个嵌入向量——内容文本、因果 Action、元数据属性/关系——各自转化为自然语言 Text Unit，使法律实体可从内容、属性、关系多路径检索。
5. **Planner-guided 确定性查询管线**：统一执行策略含 8 步（约束规范化→层级范围解析→策略选择→确定性 CTV 选择→范围检索 Text Units→Action 因果聚合→provenance DAG 组装→事实锚定生成），确保可复现性和可审计性。

## 创新点
- **采用法律内在层级作为图骨架**（vs. 标准 Graph RAG [Edge et al., 2024] 依赖算法社区检测从内容推导语义层级）——将 Title/Chapter/Article 的预设层级作为 curated community 结构。
- **聚合而非组合的版本传播模型**（vs. 朴素的 Composition 方法会为所有子组件创建新 CTV）——复用未变更子组件的已有 CTV，避免海量数据冗余。
- **立法事件作为一等可检索单元**（vs. Akoma Ntoso 将 FRBR 概念层仅作为 XML metadata 标识符）——将 Work/Expression 区分从 metadata 标签提升为本体一等实体。
- **多方面嵌入使规范上下文可检索**（vs. 标准单向量表示）——将元数据和因果关系文本化为独立 Text Unit。

## 效果
本文为概念框架+定性案例研究（巴西宪法），**无定量实验结果表**。论文明确指出需专门基准进行严格定量验证，提出未来评估指标包括 Temporal Precision/Recall、Action-Attribution Accuracy（F1）、Causal-Chain Completeness。具体数值待补充。

## 关键引用
> "Standard Graph RAG approaches primarily focus on an entity-centric model... While powerful for discovering thematic connections within content, this approach is fundamentally blind to the formal, hierarchical architecture of the document itself." — Section 3.1, p.3-4

> "A naive approach would be to model this as a Composition, where a new parent CTV would be composed of newly created CTVs for all its children, even those whose text remained unchanged. This method is highly inefficient, creating vast amounts of redundant data and obscuring which components were actually modified." — Section 3.4, p.7-8

> "By making causality and versioning explicit graph structures, and by selecting the optimal query strategy, this pattern enables deterministic and auditable provenance reports that a baseline RAG cannot reliably produce." — Section 4.3, p.17

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[OntologyGroundedRAG]] — 本体 grounding RAG
- [[beyond-probabilistic-rag-limitations]] — 同一作者的理论分析，论证 RAG 在法律领域的三种 pathology
- [[og-rag-ontology-grounded]] — Round 15 本体超图检索，对比 flat-text RAG
- [[GraphRAG]] — Graph RAG 概念页
