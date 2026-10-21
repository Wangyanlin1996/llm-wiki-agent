---
title: "Discoverable Agent Knowledge: Agent知识图谱可供性形式化框架"
type: source
tags: [semantic-layer, llm-agent-ontology]
sources: [discoverable-agent-knowledge-aap]
source_file: raw/papers/discoverable-agent-knowledge-aap.pdf
last_updated: 2026-07-25
arxiv_id: "2605.19186"
authors: ["Terry R. Payne", "Valentina Tamma", "Enrico Daga"]
year: 2026
venue: ""
citation_count: 0
---

## 概要
二十年前的 Semantic Web Services 社区被问及不同本体承诺的 agent 如何发现、组合和调用 web 服务。当前 KG 元数据标准（VoID、DCAT）描述 KG 包含什么，但对特定 agent 能从中证明什么、空结果的闭包假设、agent 任务词汇是否在 schema 中接地只字不提。本文提出四维形式化框架：语义表达力、Agent 可发现性、任务相对接地、认知信任范围，从中推导出 Agent 可供性配置文件（AAP）：在 VoID 和 DCAT 之上的语义层，支持 agent 规划时的 KG 选择、组合和失败诊断。

## 关键贡献
- 四维形式化框架：语义表达力 × Agent 可发现性 × 任务相对接地 × 认知信任范围
- Agent 可供性配置文件（AAP）作为 VoID/DCAT 之上的语义层
- 支持 agent 规划时的 KG 选择、组合和失败诊断
- 揭示已部署 KG 中管理 schema DL 与操作蕴含机制可能偏离的认知失败模式
- 五点研究议程

## 关键引用
> "The four dimensions operationalise the affordance structure of the Ontological Continuum at the individual-agent level, specifically for KG selection, composition, and failure diagnosis."

## 关联
- [[OntologySemanticLayer]] — 本体语义层
- [[OntologyFirstAgentDesign]] — 本体优先Agent设计方法论
- [[kg-gap-overlap-benchmark]] — KG任务就绪性基准
- [[RetrievalAugmentedGeneration]] — 检索增强生成

## 矛盾
- 无
