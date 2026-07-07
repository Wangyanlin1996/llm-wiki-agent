---
title: "HEAR: 分层超图本体的企业Agent推理器"
type: source
tags: [task-execution, hypergraph-ontology, enterprise-reasoning, ontology-reasoning, task-completion]
sources: [hear-hypergraph-enterprise]
source_file: raw/papers/hear-hypergraph-enterprise.pdf
last_updated: 2026-07-07
arxiv_id: "2605.14259"
authors: ["Ling Wang", "Xin Liu", "Songnan Liu", "Jianan Wang", "Cheng Cheng", "Yihan Zhu", "Enyu Li", "Yu Xiao", "Jiangyong Xie", "Duogong Yan", "Jiangyi Chen"]
year: 2026
venue: ""
citation_count: 0
doi: ""
---

## 概要
HEAR（Hypergraph Enterprise Agentic Reasoner）建立在分层超图本体之上，解决异构企业系统中 LLM 幻觉和多跳 n-ary 推理失败问题。基础图层虚拟化溯源感知数据接口，超边层编码 n-ary 业务规则和程序协议。运行证据驱动推理循环，动态编排本体工具进行结构化多跳分析，无需 LLM 重训。在供应链任务上达 94.7% 准确率。

## 关键贡献
- 分层超图本体：基础图层（数据虚拟化）+ 超边层（n-ary 业务规则）
- 证据驱动推理循环：动态编排本体工具进行多跳分析
- 程序超边最小化 token 成本，拓扑探索保证复杂查询正确性
- 开放权重模型匹配专有模型性能

## 关键引用
> "Its base Graph Layer virtualizes provenance-aware data interfaces, while the Hyperedge Layer encodes n-ary business rules and procedural protocols." — 分层超图本体架构

## 五维分析

### 本体建模
**分层超图本体**（Stratified Hypergraph Ontology）是核心创新：基础图层将异构数据源虚拟化为统一的溯源感知图接口；超边层编码 n-ary 业务规则（多个实体间的关系）和程序协议（任务执行流程）。超图（hypergraph）允许一条超边连接多个节点，超越传统图的二元关系限制，适合建模业务规则中的多实体约束。

### 用户输入实体抽取
从用户的自然语言查询中，推理循环识别需要查询的实体和关系。本体工具提供实体类型和关系的定义，指导从查询中提取正确的实体。

### 实体链接
通过**基础图层的溯源感知接口**实现实体链接：查询中的实体被映射到图中对应的节点，溯源信息确保链接可审计。超边定义了实体间的 n-ary 关系，使链接不仅限于二元关系。

### 本体推理
核心推理是**证据驱动的多跳推理循环**：推理器动态编排本体工具（图查询、超边遍历、规则推理），逐步积累证据。程序超边（procedural hyperedges）编码已知业务流程，直接执行高效推理；拓扑探索（topological exploration）用于处理复杂查询，通过图拓扑结构搜索保证正确性。两类推理的切换实现了效率与正确性的平衡。

### 任务完成
任务目标是异构企业系统中的多跳推理任务（如供应链订单履约阻塞根因分析）。94.7% 准确率、token 成本优化、开放权重模型匹配专有模型——证明超图本体在企业场景的实用价值。自动化手动诊断流程是企业部署的关键推动力。

## 关联
- [[StratifiedHypergraphOntology]] — 分层超图本体
- [[EvidenceDrivenReasoningLoop]] — 证据驱动推理循环
- [[TITAN]] — 路径规划+图执行（对比：本体执行）
- [[LOM]] — 大本体模型（企业知识管理）
- [[VADAOrchestra]] — LLM编排+符号引擎（已有wiki）
- [[KML]] — 程序化知识推理

## 矛盾
- 无
