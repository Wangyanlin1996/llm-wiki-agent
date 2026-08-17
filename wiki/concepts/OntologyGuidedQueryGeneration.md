---
title: "本体引导查询生成 (Ontology-Guided Query Generation)"
type: concept
tags: [ontology-graph-retrieval]
sources: [nlkgq-nl-ontology-query, researcher-agents-kgqa, bmqexpander-ontology-query-expansion]
last_updated: 2026-08-17
---

本体引导查询生成是指用本体 schema 作为 LLM 的语义上下文，将自然语言查询转化为结构化查询（SPARQL/SQL 等）或扩展查询术语。本体提供类型/关系/约束的"语义契约"，使 LLM 生成的查询既语法有效又语义忠实。

三条路线：(1) **零样本生成**——OWL 本体足以让 LLM 零样本生成准确结构化查询，无需微调/RAG/多agent（[[nlkgq-nl-ontology-query]]）；(2) **迭代自修正**——researcher agent 在验证集上迭代改进本体grounding和提示/工具配置（[[researcher-agents-kgqa]]）；(3) **查询扩展**——UMLS 本体知识+LLM 生成扩展术语，解决领域词汇不匹配（[[bmqexpander-ontology-query-expansion]]）。与 [[obda-query-abstraction]] 的关系：OBDA 做查询抽象，本体引导查询生成做查询构造；与 [[AgenticRetrieval]] 的关系：Researcher Agents 是 agentic 检索的 SPARQL 变体。
