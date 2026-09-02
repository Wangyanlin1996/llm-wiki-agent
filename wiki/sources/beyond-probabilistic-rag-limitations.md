---
title: "Beyond Probabilistic Similarity: RAG 在法律领域的结构/时间/因果局限（Structural, Temporal, and Causal Limitations of RAG in Legal Domain）"
type: source
tags: [ontology-graph-retrieval]
sources: [beyond-probabilistic-rag-limitations]
source_file: raw/papers/beyond-probabilistic-rag-limitations.pdf
last_updated: 2026-08-31
arxiv_id: "2606.09724"
authors: ["Hudson de Martim"]
year: 2026
venue: "arXiv preprint (critical/theory-driven survey)"
citation_count: 0
doi: ""
---

## 概要
本文论证 RAG 在法律领域的失败不是 LLM 残留 confabulation，而是 probabilistic retrieval 与法律知识的 hierarchical、temporal 和 institutional 结构之间的架构性不匹配。作者从经典法律理论（Kelsen 的 Stufenbau、Hart 的 primary/secondary rules、Luhmann 的 operational closure）出发，提出法律知识三重本体论承诺，对应识别三种 retrieval pathology（mereological blindness、diachronic blindness、causal opacity），每种配有 operational definition、failure mechanism、canonical example 和 detection criteria。最终推导出四个架构承诺定义 deterministic-by-design legal retrieval 方向。

## 解决的问题
现有法律 RAG 虽减少了 wholesale citation fabrication，但失败转向更隐蔽的模式：引用真实文档但方式 anachronistic、structurally incomplete 或缺乏 institutional grounding。Graph RAG 通过 bottom-up LLM-inferred entity-relation graph 改善了 flat retrieval，但其 structure 是 inferred 而非从 legal instrument 的 formally decreed hierarchy 继承。Probabilistic retrieval 优化 approximate semantic relevance，但法律正确性取决于 validity grounding——similarity metric 无法表达这些概念。XAI 解释模型行为而非法律 grounding；PROV-O 提供 provenance vocabulary 而非 retrieval-facing protocol。

## 方法与技术
1. **三重本体论承诺框架**：从 Kelsen 的 Stufenbau（阶层规范体系）、Hart 的 primary/secondary rules、Luhmann 的 operational closure 出发，将法律知识形式化为三个可计算要求：hierarchical and mereological structure（part-of 关系树）、diachronic dynamism under operational closure（validity transitions 是 event-driven 的）、causal traceability of institutional provenance（每个 returned norm 必须可追溯到 event chain）。
2. **三种 pathology 诊断框架**：(a) Mereological blindness——retrieval 未保持 part-whole 结构，固定 chunking 将 dependent fragment 与 governing caput 分离；(b) Diachronic blindness——5 种失败模式（只存当前版本/有 instruments 和 amendments 但无 consolidated states 等）；(c) Causal opacity——4 种表达（probabilistic retrievers 返回 similarity scores 非 provenance chains/generative synthesis 溶解 fragment boundaries 等）。
3. **正式诊断规范**：将 substrate 建模为 KG G=(V,E)，定义 `partOf(x,y)`（directed mereological containment）、`stateOf(s,r)`（state-reference 链接）、`transforms(e,s−,s+)`（validity-affecting event）。三个 closure conditions 定义 legal adequacy：structural-context closure、temporal-contextual correctness、provenance reconstructibility。
4. **四个架构承诺（C1-C4）**：C1 Ontological primacy——primary data objects 是 legal-domain entities 而非 text fragments；C2 Event reification——每个 validity-affecting event 是 graph 中一等 queryable entity；C3 Bitemporal correctness——valid time 和 transaction time 独立可表示可查询；C4 Deterministic interaction protocol——暴露 domain-specific semantically typed primitives。
5. **Pathology-organized critical review**：按 3 种 pathology 组织文献综述，审查 7 个 strand 对每种 pathology 的覆盖程度，论证 partial solutions 不自动 compose 的三个原因。

## 创新点
- **与 Graph RAG 不同**（bottom-up LLM-inferred entity-relation graph + community detection）：提出 ontological primacy（C1）要求 structure 从 formally decreed legal hierarchy 继承——inferred community 可能聚类 topically 相关但 mereologically 无关的 provisions。
- **与 temporal KG 的 timestamped triples 范式不同**：提出 event reification（C2）将 amendment/repeal/ruling 建模为一等 queryable entity 而非 edge 时间戳——timestamped triples 能回答 when a relation held 但不能回答 which act made it hold。
- **与 PROV-O 和 XAI 不同**：提出 deterministic interaction protocol（C4）暴露 domain-specific typed primitives 使 provenance 成为 first-class retrievable object。
- **与标准 bitemporal modeling 不同**：明确区分 statutory time 和 interpretive time——binding judicial decisions 可在 text 不变时改变 operative norm。

## 效果
本文是 theory-driven critical survey，不含 benchmark 实验数据。论文明确声明贡献是 formal and diagnostic，旨在为后续工作的实证比较提供标准。**具体数值待补充。**

Table 2 提供了文献 strand 的 qualitative 评估（ordinal scale），如：Legal document standards 在 Mereology=Strong、Time=Partial、Provenance=Weak-partial；Graph/ontology RAG 在 Mereology=Partial-Strong、Time=Weak-Partial、Provenance=Weak。

## 关键引用
> "Legal correctness is not a matter of semantic similarity. It is a matter of validity grounding: which norm was in force on a specific date, in a specific hierarchical context, by virtue of which institutional act." — Section 1, p.2

> "The graph reintroduces structure, but not necessarily the structure that legal validity requires." — Section 4.1, p.16

> "Partial solutions do not merely leave residual pathologies untouched; they can make those pathologies harder to detect." — Section 4.4, p.21

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[ontology-driven-graph-rag-legal]] — 同一作者的 SAT-Graph RAG 实现框架
- [[og-rag-ontology-grounded]] — Round 15 本体超图检索
- [[VerificationCoEvolution]] — Round 8 验证地平线
- [[is-graphrag-needed]] — Round 9 检索-生成差距
