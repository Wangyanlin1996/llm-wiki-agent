---
title: "KG表示用于LLM政策合规推理"
type: source
tags: [ontology-qa, policy-compliance, kg-reasoning, ontology-modeling]
sources: [kg-policy-compliance]
source_file: raw/papers/kg-policy-compliance.pdf
last_updated: 2026-07-07
arxiv_id: "2604.27713"
authors: ["Wilder Baldwin", "Sepideh Ghanavati"]
year: 2026
venue: ""
citation_count: 0
doi: ""
---

## 概要
提出一个 Agent 框架，从 AI 政策文档构建知识图谱并检索政策相关信息回答问题。在三种 AI 风险相关政策下用两种本体 schema 构建 KG，在 42 个政策 QA 任务（涵盖六种推理类型，从实体查找到跨政策推断）上评估五个 LLM。KG 增强提升了所有模型的得分，且 LLM 自发现的 schema 匹配或超越形式化本体。

## 关键贡献
- 从政策文档自动构建 KG 的 Agent 框架
- 对比两种本体 schema：形式化预定义本体 vs LLM 自发现 schema
- 六种推理类型的系统评估：实体查找、关系查找、跨政策推断等
- 发现 LLM 自发现的 schema 可匹配或超越形式化本体

## 关键引用
> "KG augmentation improves scores for all five models, and an open, LLM-discovered schema matches or exceeds the formal ontology." — 关键发现

## 五维分析

### 本体建模
对比**两种本体 schema**：形式化预定义本体（由领域专家设计，严格的实体类型和关系定义）和 LLM 自发现 schema（LLM 从文档中自主推断实体类型和关系结构）。关键发现是 LLM 自发现的开放 schema 可以匹配甚至超越形式化本体——这对本体工程的成本/效益有重要启示。

### 用户输入实体抽取
Agent 框架从政策文档中提取实体和关系构建 KG。提取过程是自动化的，包括识别政策实体（条款、要求、风险类型等）和它们之间的关系（引用、冲突、补充等）。

### 实体链接
通过 KG 检索实现查询实体到 KG 实体的链接。42 个 QA 任务涵盖从简单的实体查找（entity lookup）到复杂的跨政策推断（cross-policy inference），测试了不同复杂度的实体链接需求。

### 本体推理
六种推理类型从简单到复杂：实体查找→关系查找→单政策推理→跨政策推断。KG 增强在所有推理类型上都提升了 LLM 表现，特别是在需要多步推理的复杂类型上提升显著。形式化本体 vs 自发现本体的对比揭示了本体结构对推理质量的影响。

### 任务完成
任务目标是政策合规问答。42 个 QA 任务覆盖六种推理类型，KG 增强提升了所有五个 LLM 的得分。任务完成的质量取决于本体 schema 的设计——形式化本体提供严格约束，自发现本体提供灵活性。

## 关联
- [[PolicyComplianceKG]] — 政策合规知识图谱
- [[LLMDiscoveredSchema]] — LLM自发现schema
- [[LOM]] — 大本体模型（企业知识管理）
- [[KGTaskReadinessBenchmark]] — KG任务就绪性基准

## 矛盾
- 无
