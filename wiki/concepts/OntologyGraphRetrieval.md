---
title: "本体图增强精准检索 (Ontology Graph-Enhanced Precise Retrieval)"
type: concept
tags: [ontology-graph-retrieval]
sources: [og-rag-ontology-grounded, evidence-units-ontology-retrieval, hyem-hyperbolic-ontology-retrieval, omagr-ontology-multi-anchor-retrieval, fair-graphrag-semantic-data, ontologyrag-biomedical-code-mapping, cyberbot-ontology-grounded-rag, worlddb-ontology-aware-memory, moss-auditable-agentic-memory, rag-autoconfig-industrial-fieldbus, nlkgq-nl-ontology-query, researcher-agents-kgqa, bmqexpander-ontology-query-expansion, kroma-ontology-matching-rag, ontology-dedup-kg-construction, verifiable-knowledge-expansion-fca, automated-ontology-generation-multi-agent]
last_updated: 2026-08-17
---

本体图增强精准检索是指利用形式本体（ontology）的类型/层次/关系/约束结构指导检索过程，实现超越纯向量相似度的精准语义检索。核心洞察是：flat 向量库将事实碎片化为 chunk，丢失实体间结构关系；而本体图保留概念层次和关系语义，使检索既能找到"相关"内容，又能确保"概念一致"和"域适切"。

该方向涵盖四条技术路线：(1) **本体超图/图检索**——将文档组织为本体grounding的超图/图结构，用最小覆盖或图遍历检索精准上下文（[[og-rag-ontology-grounded]]、[[omagr-ontology-multi-anchor-retrieval]]、[[fair-graphrag-semantic-data]]）；(2) **本体层次编码检索**——将本体的 is-a 层次结构编码为双曲嵌入，查询自适应切换双曲/欧式检索（[[hyem-hyperbolic-ontology-retrieval]]）；(3) **结构化查询生成**——用本体 schema 锚定 LLM 零样本/迭代生成 SPARQL 或结构化查询（[[nlkgq-nl-ontology-query]]、[[researcher-agents-kgqa]]）；(4) **可审计图记忆引擎**——用本体感知的图结构替代 flat 向量库，在写入时协调矛盾/替代（[[worlddb-ontology-aware-memory]]、[[moss-auditable-agentic-memory]]）。

与 [[GraphRAG]] 的区别：GraphRAG 从文档中提取 KG 增强检索，但不一定用形式本体约束类型/关系；本体图检索则用形式本体 schema 作为"语义契约"约束整个检索管线的类型一致性和概念grounding。与 [[OntologyGuidedKGQA]] 的关系：KGQA 是本体图检索的下游应用，本体图检索提供检索基础设施，KGQA 在其上做推理。与 [[anchor-schema-agnostic-ontology]] 的呼应：ANCHOR 解决"输入→本体图"的构建问题，本体图检索解决"本体图→精准检索"的查询问题——两者构成完整管线。
