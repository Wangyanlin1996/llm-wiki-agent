---
title: "OntoBOT: 服务机器人任务/动作/环境/能力统一本体"
type: source
tags: [task-execution, robotics-ontology, ontology-modeling, ontology-reasoning, task-completion]
sources: [ontobot-robotics-ontology]
source_file: raw/papers/ontobot-robotics-ontology.pdf
last_updated: 2026-07-07
arxiv_id: "2509.22434"
authors: ["Margherita Martorana", "Francesca Urgese", "Ilaria Tiddi", "Stefan Schlobach"]
year: 2025
venue: ""
citation_count: 0
doi: ""
---

## 概要
OntoBOT（Ontology for roBOts and acTions）扩展已有本体（SOMA、DOLCE），提供任务、动作、环境和机器人能力的统一表示。支持关于任务执行的形式推理，并在四个具身 agent（TIAGo、HSR、UR3、Stretch）上通过能力问题评估泛化性，展示上下文感知推理、任务导向执行和知识共享。

## 关键贡献
- 统一任务/动作/环境/能力的本体表示
- 扩展 SOMA 和 DOLCE 已有本体，补充环境-动作-能力-系统集成的连接
- 四个不同具身 agent 上的能力问题评估，验证泛化性
- 上下文感知推理支持任务导向执行

## 关键引用
> "we unify these aspects into a cohesive ontology to support formal reasoning about task execution, and (2) we demonstrate its generalizability by evaluating competency questions across four embodied agents" — 统一本体+能力问题评估

## 五维分析

### 本体建模
**四维统一本体**是核心创新：任务（tasks，需要完成的目标）、动作（actions，执行的具体操作）、环境（environments，物理上下文）、能力（capabilities，机器人硬件/软件能力）。扩展 SOMA（活动的社会物理模型）和 DOLCE（认知工程描述本体），补充已有本体缺失的"环境↔动作↔能力↔系统集成"连接。本体使用 OWL 形式化，支持 SPARQL 能力问题查询。

### 用户输入实体抽取
从用户任务指令中提取任务目标、涉及的对象和环境约束。本体定义了任务到动作的分解规则和动作到能力的需求映射，指导从用户输入中识别关键实体。

### 实体链接
通过**能力问题**（competency questions）实现实体链接：用户查询被表述为本体能力问题（如"TIAGo 能在厨房环境中执行抓取动作吗？"），本体推理器将问题中的实体链接到本体中定义的实例。

### 本体推理
核心推理是**能力推理**（capability reasoning）：给定任务和环境，推理机器人是否有能力执行所需动作。推理链：任务→所需动作→所需能力→机器人实际能力→可行性判定。环境上下文影响推理（同一动作在厨房 vs 卧室的可行性可能不同）。

### 任务完成
任务目标是服务机器人的任务导向执行。通过统一本体，机器人能推理"能否做"、"怎么做"、"在哪做"。四个不同具身 agent 的评估验证了本体的泛化性——同一本体支持不同硬件配置的机器人，促进知识共享和互操作。

## 关联
- [[UnifiedTaskActionOntology]] — 统一任务动作本体
- [[CapabilityReasoning]] — 能力推理
- [[KML]] — 程序化知识推理（视频场景）
- [[HEAR]] — 企业超图本体推理
- [[Husky]] — 统一动作本体Agent

## 矛盾
- 无
