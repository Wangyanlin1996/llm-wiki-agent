---
title: "SocialDial: 社交感知对话系统基准"
type: source
tags: [conversational-agent, social-ontology, dialogue-generation, task-completion]
sources: [socialdial-socially-aware]
source_file: raw/papers/socialdial-socially-aware.pdf
last_updated: 2026-07-07
arxiv_id: "2304.12026"
authors: ["Haolan Zhan", "Zhuang Li", "Yufei Wang", "Linhao Luo", "Tao Feng", "Xiaoxi Kang", "Yuncheng Hua", "Lizhen Qu", "Lay-Ki Soon", "Suraj Sharma", "Ingrid Zukerman", "Zhaleh Semnani-Azad", "Gholamreza Haffari"]
year: 2023
venue: "SIGIR 2023"
citation_count: 0
doi: ""
---

## 概要
SocialDial 是首个社交感知对话语料库，基于中文社会文化。包含 1,563 条多轮人类对话（细粒度标注）和 4,870 条 ChatGPT 合成对话。覆盖5类社交规范（14个子类），标注社交因素（社会关系、上下文、社交距离、社交规范）。利用 ChatGPT 设计**本体驱动的合成数据生成框架**，大规模生成合成对话并通过质量控制机制确保质量。

## 关键贡献
- 首个社交感知对话语料库：中文社会文化，5类14子类社交规范
- 细粒度社交因素标注：社会关系、上下文、社交距离、社交规范
- 本体驱动的合成数据生成框架：大规模生成+质量控制
- 证明社交规范建模对对话系统是 promising 方向

## 关键引用
> "we harness the power of ChatGPT and devise an ontology-based synthetic data generation framework. This framework is able to generate synthetic data at scale." — 本体驱动合成数据生成

## 五维分析

### 本体建模
**社交规范本体**：定义5类社交规范（14个子类），以及社交因素（社会关系、上下文、社交距离）。本体为每条对话提供结构化的社交因素标注——对话不仅记录"说了什么"，还记录"在什么社交上下文中说的"。本体驱动合成数据生成：ChatGPT 根据本体定义的社交规范类型生成符合特定社交场景的对话。

### 用户输入实体抽取
从对话中标注社交因素实体：社会关系（如朋友、陌生人）、上下文（如正式/非正式场合）、社交距离（如亲密/疏远）。这些实体标注使模型能学习社交因素如何影响对话表达。

### 实体链接
通过本体定义的社交规范类型，将对话中的行为链接到社交规范类别。例如，某句对话中的"道歉"行为被链接到"礼貌规范"子类。这种链接使系统能识别对话是否违反了社交规范。

### 本体推理
推理体现为**社交规范一致性推理**：给定对话的社交因素标注，推理对话行为是否符合对应的社交规范。例如，对亲密朋友的请求可以使用非正式语言，对上级的请求需要正式语言——本体定义了社交因素与规范行为的映射关系。

### 任务完成
任务目标是提升对话系统的社交感知能力。BERT 和 RoBERTa 在 SocialDial 上的评估证明社交规范建模是 promising 方向。本体驱动的合成数据生成框架解决了社交对话数据稀缺的问题，可大规模扩展。

## 关联
- [[SocialNormOntology]] — 社交规范本体
- [[OntologyBasedDataGeneration]] — 本体驱动数据生成
- [[KnowledgeGroundedDialogueFlow]] — 知识驱动对话管理
- [[PositiveFrictionDialogue]] — 正摩擦对话
- [[NLUPlusPlus]] — 细粒度本体NLU

## 矛盾
- 无
