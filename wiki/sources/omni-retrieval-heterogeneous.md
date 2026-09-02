---
title: "OmniRetrieval: 异构知识源统一检索（Unified Retrieval across Heterogeneous Knowledge Sources）"
type: source
tags: [ontology-graph-retrieval]
sources: [omni-retrieval-heterogeneous]
source_file: raw/papers/omni-retrieval-heterogeneous.pdf
last_updated: 2026-08-31
arxiv_id: "2605.29250"
authors: ["Jinheon Baek", "Soyeong Jeong", "Sangwoo Park", "Woongyeong Yeo", "Minki Kang"]
year: 2026
venue: "arXiv preprint (KAIST & DeepAuto.ai)"
citation_count: 0
doi: ""
---

## 概要
OmniRetrieval 是一个统一检索框架，能够处理来自非结构化文本（document corpus）、关系型数据库（relational database）、RDF Knowledge Graph 和 Property Graph 等异构知识源的检索任务。该框架不将所有源折叠到共享表示空间中，而是通过 Source Selection、Per-Source Native Query Formulation 和 Cross-Source Evidence Selection 三个步骤，让每个知识源以其原生查询语言（SQL、SPARQL、Cypher 或 free-form text）被访问。在覆盖 13 个数据集和 309 个知识库的 benchmark 上，OmniRetrieval 在三项指标上持续超越所有 single-source baselines 和 KB Routing 基线。

## 解决的问题
现有检索器（document retrievers、text-to-SQL 系统、text-to-SPARQL/Cypher 生成器）每次只能操作一种知识源且使用固定查询语言，导致知识碎片化在互不兼容的接口之后。一种自然的统一方法是将所有源投影到共享表示空间（如统一 embedding space 或线性化文本格式），但这会抹去各源的结构特性（schema、ontology、组合算子如 join/traversal），导致统一 embeddings 按源类型而非语义内容聚类（modality gap），且原生查询算子丢失仅剩相似度匹配。KB Routing 虽能选择单一源但缺乏 fallback 机制。

## 方法与技术
1. **Long-Context Source Selection**：将所有注册源的 structural descriptors（relational schema、RDF ontology、corpus descriptor）与 query 共同输入 long-context LLM，返回 top-k（默认 k=3）相关源子集，避免单一 encoder 对异构描述符的 lossy projection。
2. **Per-Source Native Query Generation**：对每个选中的源，使用 per-source prompt template 将问题翻译为该源的原生查询语言——SQL/SPARQL/Cypher 直接生成可执行查询，free-form text 直接用问题作为 retriever query。由单一共享 LLM 配合模板实现。
3. **Cross-Source Evidence Selection**：将各源 executor 的异构输出（SQL rows、RDF triples、graph paths、text passages）verbalize 为文本，由 LLM-based selector 从中筛选出与问题相关的最终证据集。
4. **Registration-based 扩展机制**：新增源仅需注册其 structural context 即可加入框架，无需重新训练共享 encoder 或重画 embedding 空间。

## 创新点
- **首个通过各源原生查询语言统一检索异构结构化与非结构化后端的框架**（vs. Oguz et al. 2022、Ma et al. 2022、Baek et al. 2023 将异构源折叠到统一 embedding/文本表示的方法）——保留每个源的结构算子（join、traversal、property path）。
- **Source Selection 阶段使用 long-context LLM 直接读取全部源描述符**（vs. 标准基于 embedding 相似度排序源的方法）——后者因描述符形式不统一导致 lossy projection。
- **Multi-candidate engagement + deferred commitment**（vs. KB Routing 每查询仅路由到单一源且无 fallback）——engage 多个候选源后将最终选择权 defer 到基于 retrieved evidence 的 evidence selection 阶段。
- **Unified representation 不可行性的实证论证**：Wikidata 有 150 亿+triples、property graph 三跳路径可达数百亿、一个 SQL 库有 7000 万+行，统一 embedding/线性化在 benchmark scale 已不可行。

## 效果
- Dataset: 13 datasets / 309 KBs (Average) | Metric: Source Selection Accuracy (%) | Result: 65.71 | Baseline: 61.65 (KB Routing) | Δ: [+6.6%]
- Dataset: 13 datasets / 309 KBs (Average) | Metric: Retrieval Accuracy (%) | Result: 44.34 | Baseline: 39.98 (KB Routing) | Δ: [+10.9%]
- Dataset: 13 datasets / 309 KBs (Average) | Metric: LLM-as-a-Judge (%) | Result: 65.88 | Baseline: 57.99 (KB Routing) | Δ: [+13.6%]
- Dataset: 13 datasets (GPT-5.4) | Metric: LLM-as-a-Judge (%) | Result: 69.72 | Baseline: 60.26 (KB Routing) | Δ: [+15.7%]
- **Ablation**: Unified Representation vs OmniRetrieval (constrained): Source Selection 68.58 vs 31.00 (Δ +121.2%); Retrieval 46.62 vs 23.00 (Δ +102.7%)
- **Ablation**: Evidence Selection Acc: 72.81% vs 38.31% (Random) (Δ +89.8%)
- **Ablation**: 候选源数量 k 从 1→10，Source Selection Accuracy 提升 +17.9 至 +27.6 pts；但 evidence selector 准确率从 67.5%（k=3）下降到 62.8%（k=10）

## 关键引用
> "the right move, we argue, is the opposite of homogenization: keep each source on its own terms, and instead build a unifying access layer above them." — Section 1, p.2

> "atomic-unit retrieval cannot capture the structural composition (e.g., joins, traversals, multi-hop chains) that native queries express." — Section 4, p.8

> "broad exploration at the source-selection step, with the final commitment deferred to a selector that rests on retrieved evidence, is what lets OmniRetrieval scale gracefully." — Section 6, p.9

## 关联
- [[OntologyGuidedQueryGeneration]] — 本体引导查询构造
- [[HybridRetrieval]] — Round 9 混合检索概念
- [[nlkgq-nl-ontology-query]] — Round 15 OWL 本体零样本查询生成
- [[researcher-agents-kgqa]] — Round 15 Agentic text-to-SPARQL
- [[telco-orag]] — Round 9 电信场景混合检索
