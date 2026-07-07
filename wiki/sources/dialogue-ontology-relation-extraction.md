---
title: "约束CoT解码的对话本体关系抽取"
type: source
tags: [task-oriented-dialogue, ontology-construction, relation-extraction, task-completion]
sources: [dialogue-ontology-relation-extraction]
source_file: raw/papers/dialogue-ontology-relation-extraction.pdf
last_updated: 2026-07-07
arxiv_id: "2408.02361"
authors: ["Renato Vukovic", "David Arps", "Carel van Niekerk", "Benjamin Matthias Ruppik", "Hsien-Chin Lin", "Michael Heck", "Milica Gašić"]
year: 2024
venue: "SIGDIAL 2024"
citation_count: 0
doi: ""
---

## 概要
聚焦任务型对话本体构建中的关系抽取步骤，提出将 Chain-of-Thought（CoT）解码适配到生成式关系抽取。在解码空间生成多个分支，基于置信度阈值选择关系。通过将解码约束到本体术语和关系上，降低幻觉风险。在两个广泛使用的数据集上实验，在源微调和少样本提示的 LLM 上均取得性能提升。

## 关键贡献
- 将 CoT 解码从推理问题适配到生成式关系抽取
- 多分支解码+置信度阈值选择：提高关系抽取可靠性
- 解码约束到本体术语和关系：降低幻觉风险

## 关键引用
> "By constraining the decoding to ontology terms and relations, we aim to decrease the risk of hallucination." — 约束解码降低幻觉

## 五维分析

### 本体建模
面向**对话本体构建**的关系抽取——从对话数据中自动构建任务特定本体。本体由术语（terms，对应 slot/intent）和关系（relations，对应 slot 间的依赖、intent 间的转移等）组成。本文聚焦关系抽取步骤，假设术语已通过其他方法提取。

### 用户输入实体抽取
从对话数据中提取本体术语（slot 名、intent 名）作为关系抽取的候选端点。关系抽取的目标是确定这些术语之间的结构关系（如"restaurant-name slot 依赖 restaurant-type slot"）。

### 实体链接
通过**约束解码**实现术语到本体关系的可靠链接：解码被约束到本体已定义的术语和关系集合内，防止 LLM 生成不存在的关系或链接到错误术语。这是通过解码空间约束实现的实体-关系链接可靠性保障。

### 本体推理
推理体现为**CoT 多分支推理+置信度选择**：LLM 在解码空间生成多个推理分支（每个分支是一种可能的关系推断），基于置信度阈值选择最可靠的关系。CoT 允许模型先"思考"关系成立的理由，再输出关系——这种中间推理步骤提高了关系抽取的质量。

### 任务完成
任务目标是自动化对话本体构建中的关系抽取。在两个数据集上，源微调和少样本提示的 LLM 均取得性能提升。约束解码降低幻觉，使自动构建的本体更可靠，可直接用于下游 TOD 系统。

## 关联
- [[ConstrainedCoTDecoding]] — 约束CoT解码
- [[DialogueOntologyConstruction]] — 对话本体构建
- [[TeQoDO]] — TOD本体自动构建
- [[OPAL]] — 本体感知预训练TOD
- [[OntologyEnhancedSlotFilling]] — 本体增强slot填充

## 矛盾
- 无
