---
title: "本体增强的Slot Filling"
type: source
tags: [task-oriented-dialogue, slot-filling, entity-linking, ontology-modeling, task-completion]
sources: [ontology-enhanced-slot-filling]
source_file: raw/papers/ontology-enhanced-slot-filling.pdf
last_updated: 2026-07-07
arxiv_id: "2108.11275"
authors: ["Yuhao Ding", "Yik-Cheung Tam"]
year: 2021
venue: ""
citation_count: 0
doi: ""
---

## 概要
提出一种本体增强的 slot filling 方法，通过用本体匹配跨对话轮次出现的命名实体，将匹配到的实体累积并编码为 BERT-based DST 的额外输入。还包含本体约束检查和 slot 名 tokenization 纠正。在 MultiWOZ 2.1 上，JGA 从 52.63% 提升到 53.91%，slot F1 从 91.64% 提升到 92%。

## 关键贡献
- 跨轮次命名实体的本体匹配：累积并编码为额外输入
- 本体约束检查：验证 slot-value 对是否合法
- slot 名 tokenization 纠正

## 关键引用
> "we investigate an ontology-enhanced approach by matching the named entities occurred in all dialogue turns using ontology. The matched entities in the previous dialogue turns will be accumulated and encoded as additional inputs to a BERT-based dialogue state tracker." — 核心方法

## 五维分析

### 本体建模
使用 MultiWOZ **预定义本体**：本体定义了每个域的 slot 类型及其合法值域（如 restaurant 域的 name slot 有预定义的餐厅名列表）。本体的 slot-value 列表作为实体匹配的参照标准。本体是静态预定义的，本文的贡献是更好地利用已有本体而非构建新本体。

### 用户输入实体抽取
从对话的**所有轮次**中提取命名实体（餐厅名、时间、地点等）。这是 slot filling 的核心步骤——识别用户在对话中提到的实体值。跨轮次累积确保之前轮次提到的实体在后续轮次仍被考虑。

### 实体链接
通过**本体匹配**实现实体链接：将对话中出现的命名实体与本体预定义的 slot 值列表进行匹配。匹配到的实体被累积并编码为 BERT 的额外输入，使 DST 能利用跨轮次的本体约束信息。本体约束检查进一步验证 slot-value 对的合法性。

### 本体推理
推理体现为**约束检查**：验证 DST 预测的 slot-value 对是否符合本体定义的值域约束。如果预测的值不在本体的合法值列表中，进行纠正。slot 名 tokenization 纠正确保 slot 名被正确分解为 BERT 可处理的 token。

### 任务完成
任务目标是提升 DST 的 JGA 和 slot F1。在 MultiWOZ 2.1 上，JGA 提升 1.28%，slot F1 提升 0.36%。虽然提升幅度不大，但证明了本体信息作为额外输入的有效性。

## 关联
- [[OntologyEnhancedSlotFilling]] — 本体增强slot填充
- [[EntityMatchingOntology]] — 本体实体匹配
- [[OPAL]] — 本体感知预训练TOD
- [[D3ST]] — 描述驱动DST
- [[VLK-RL]] — 本体对齐slot-value

## 矛盾
- 无
