---
title: "KG任务就绪性基准: 本体驱动Gap/Overlap分析"
type: source
tags: [ontology-qa, kg-task-readiness, ontology-modeling, ontology-reasoning, task-completion]
sources: [kg-gap-overlap-benchmark]
source_file: raw/papers/kg-gap-overlap-benchmark.pdf
last_updated: 2026-07-07
arxiv_id: "2604.10853"
authors: ["Maruf Ahmed Mridul", "Rohit Kapa", "Oshani Seneviratne"]
year: 2026
venue: ""
citation_count: 0
doi: ""
---

## 概要
提出一个可执行、可审计的基准，将自然语言合同文本与形式本体对齐，评估知识图谱的任务就绪性（task readiness）。通过 gap/overlap 分析（给定场景，哪些文档支持/不支持），对比纯文本 LLM 基线与本体驱动管线。包含10份人寿保险合同、域本体（TBox）+ 实例化 KG（ABox）、58个结构化场景配 SPARQL 查询。证明显式建模提升一致性和可诊断性。

## 关键贡献
- 可执行、可审计的 KG 任务就绪性基准
- 自然语言合同→形式本体对齐+证据链接真值
- 对比纯文本 LLM vs 本体驱动管线
- 58个场景配 SPARQL 查询+合同级结果+条款级证据

## 关键引用
> "we compare a text-only LLM baseline that infers outcomes directly from contract text against an ontology-driven pipeline that answers the same scenarios over the instantiated KG, demonstrating that explicit modeling improves consistency and diagnosis for gap/overlap analyses." — 核心对比

## 五维分析

### 本体建模
**域本体（TBox）+ 实例化 KG（ABox）**的完整本体工程：TBox 定义保险域的概念层次和关系（保单类型、覆盖范围、 exclusions 等），ABox 从合同事实填充具体实例。本体由领域专家审核，确保表达力和可扩展性。自然语言合同文本被对齐到本体——合同条款映射到本体中的规则和约束。

### 用户输入实体抽取
从自然语言合同文本中提取实体和关系填充 ABox。提取过程包括识别合同中的保险条款、覆盖条件、排除条款等，并将它们映射到 TBox 定义的概念类型。

### 实体链接
通过**SPARQL 查询**实现实体链接：58个结构化场景各配一个 SPARQL 查询，查询在 KG 上执行，将场景中的实体链接到 KG 中的具体实例。证据链接的条款级摘录为每个结果提供可追溯的依据。

### 本体推理
核心推理是**gap/overlap 推理**：给定场景，推理哪些合同的 KG 支持该场景（overlap）或不支持（gap）。推理通过 SPARQL 查询在 KG 上执行——本体定义的规则和约束决定查询结果。关键洞察：gap/overlap 差异源于覆盖范围的真实差异而非数据缺失，使任务成为 KG 任务就绪性的直接测试。

### 任务完成
任务目标是评估和提升 KG 的任务就绪性。本体驱动管线在一致性和可诊断性上优于纯文本 LLM 基线。基准作为可复用模板，支持本体学习、KG 填充和证据接地 QA 的下游工作。58个场景+SPARQL 查询+证据摘录构成完整的可审计评估框架。

## 关联
- [[KGTaskReadiness]] — KG任务就绪性
- [[GapOverlapAnalysis]] — Gap/Overlap分析
- [[TBoxABoxOntology]] — TBox+ABox本体工程
- [[KGPolicyCompliance]] — KG政策合规推理
- [[LOM]] — 大本体模型

## 矛盾
- 无
