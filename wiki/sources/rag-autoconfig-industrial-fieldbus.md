---
title: "RAG-Based Auto-Configuration: ECLASS本体图+混合检索工业设备自动配置"
type: source
tags: [ontology-graph-retrieval]
sources: [rag-autoconfig-industrial-fieldbus]
source_file: raw/papers/rag-autoconfig-industrial-fieldbus.pdf
last_updated: 2026-08-17
arxiv_id: "2608.08618"
authors: ["Aadil Gani Ganie", "Saad Ezzini", "Naveed Farooz Marazi"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

SysName 提出一个面向生产的流水线，利用 ECLASS 本体图增强的混合稠密-稀疏检索，自动化工业设备配置。系统从异构 PDF 手册中提取数百个协议特定参数，通过本体图约束确保参数类型/值域正确性，自动转录到监控系统。

## 解决的问题

工业设备调试需要工程师从异构 PDF 手册中手动提取数百个协议特定参数并转录到监控系统——耗时且易错。

## 方法与技术

1. **ECLASS 本体图**：从 ECLASS 工业标准本体构建参数类型/关系图
2. **混合稠密-稀疏检索**：本体图约束的混合检索索引
3. **多协议支持**：Modbus RTU、OPC-UA、Profibus DP、CANopen
4. **端到端自动化**：从 PDF 手册到设备配置的完整流水线

## 创新点

- 本体图约束工业参数检索，确保类型/值域正确性
- 混合稠密-稀疏检索适配异构手册格式
- 生产导向流水线支持多工业协议

## 关键引用

> "builds a hybrid dense-sparse retrieval index augmented by an ontology graph derived from ECLASS" — 本体图增强混合检索

## 关联

- [[OntologyGraphRetrieval]] — 本体图约束工业参数检索
- [[og-rag-ontology-grounded]] — OG-RAG 通用本体超图，SysName 工业本体图
- [[OntologySemanticLayer]] — ECLASS 本体作为工业语义层
- [[HybridRetrieval]] — 混合检索的本体增强
