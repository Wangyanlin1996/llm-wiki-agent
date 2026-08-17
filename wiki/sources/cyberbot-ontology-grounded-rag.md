---
title: "CyberBOT: 本体grounding RAG实现可信网络安全教育问答"
type: source
tags: [ontology-graph-retrieval]
sources: [cyberbot-ontology-grounded-rag]
source_file: raw/papers/cyberbot-ontology-grounded-rag.pdf
last_updated: 2026-08-17
arxiv_id: "2504.00389"
authors: ["Chengshuai Zhao", "Riccardo De Maria", "Tharindu Kumarage", "Kumar Satvik Chaudhary", "Garima Agrawal", "Yiwen Li", "Jongchan Park", "Yuli Deng", "Ying-Chih Chen", "Huan Liu"]
year: 2025
venue: "arXiv"
citation_count: 0
---

## 概要

CyberBOT 是一个网络安全教育问答系统，利用本体grounding的 RAG 管线确保回答的可信性和领域适切性。系统首先构建网络安全本体，然后用本体约束 RAG 检索过程，确保检索结果不仅表面相关，而且域适切且可信。

## 解决的问题

网络安全教育中，LLM 回答需要超越表面相关性，提供可信且域适切的信息——错误信息在安全教育场景中代价高昂。

## 方法与技术

1. **网络安全本体构建**：定义网络安全领域的概念/关系/约束
2. **本体grounding RAG**：用本体约束检索过程，过滤域外/不可信结果
3. **可信性保证**：检索结果锚定到本体概念，确保域适切
4. **教育问答**：面向探究式学习的问答系统

## 创新点

- 本体grounding从"表面相关"提升到"域适切且可信"
- 网络安全本体约束 RAG 检索的全流程
- 教育场景的安全性和准确性保证

## 关键引用

> "systems must go beyond surface-level relevance to provide information that is both trustworthy and domain-appropriate" — 本体grounding的动机

## 关联

- [[OntologyGraphRetrieval]] — 本体约束 RAG 检索确保域适切
- [[og-rag-ontology-grounded]] — OG-RAG 通用本体超图，CyberBOT 专注安全教育
- [[anchor-schema-agnostic-ontology]] — ANCHOR 同为 CTI 本体场景，CyberBOT 为教育场景
- [[cybercane-neuro-symbolic-rag]] — CyberCane 钓鱼检测本体 RAG，相关场景
