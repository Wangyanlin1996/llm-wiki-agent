---
title: "知识驱动对话流管理: 社交机器人本体对话管理"
type: source
tags: [conversational-agent, ontology-dialogue-management, hci, task-completion]
sources: [knowledge-grounded-dialogue-flow]
source_file: raw/papers/knowledge-grounded-dialogue-flow.pdf
last_updated: 2026-07-07
arxiv_id: "2108.02174"
authors: ["Lucrezia Grassi", "Carmine Tommaso Recchiuto", "Antonio Sgorbissa"]
year: 2022
venue: "Int J of Soc Robotics 14, 1273-1293"
citation_count: 0
doi: "10.1007/s12369-022-00868-z"
---

## 概要
提出面向社交机器人和对话 agent 的知识驱动对话系统，依赖本体描述所有可能相关的对话话题及其相互关系。对话管理算法根据用户输入选择最合适的对话话题，确保对话流尽可能连贯地捕获用户驱动对话方向的意图，避免纯反应式响应。100名参与者对比5种对话 agent，用 SASSI 工具和自定义连贯性调查测量主观感知。

## 关键贡献
- 本体描述对话话题及关系：结构化话题知识库
- 对话管理算法：根据用户输入选择话题，确保连贯对话流
- 100人用户研究对比5种 agent（关键词/关键词+内容分类/随机/人类伪装/Replika）
- SASSI + 自定义连贯性调查双维度评估

## 关键引用
> "The proposed system relies on an Ontology for the description of all concepts that may be relevant conversation topics, as well as their mutual relationships." — 本体驱动对话管理

## 五维分析

### 本体建模
**对话话题本体**：本体定义所有可能相关的对话话题概念及其相互关系。话题间的关系（如"相关"、"从属"、"对比"）定义了对话流的可能转移路径。本体是社交机器人对话管理的结构化知识基础——不同于 slot-value 本体，这是一种话题层面的本体，建模对话的内容空间。

### 用户输入实体抽取
从用户输入中提取关键词和语义特征，用于话题识别。对话管理算法分析用户输入中的实体和意图，确定用户想讨论的话题方向。

### 实体链接
通过**本体话题匹配**实现实体链接：用户输入中的关键词和语义特征被映射到本体中的话题节点。Google Cloud Natural Language 的 Content Classification 辅助话题分类。链接到本体话题后，算法选择最合适的话题作为对话下一步。

### 本体推理
核心推理是**对话流推理**：根据当前话题和用户输入，在本体话题关系图上推理下一步话题。推理考虑：(1) 用户意图驱动方向——用户想往哪走；(2) 话题连贯性——新话题与当前话题的本体关系是否支持自然过渡；(3) 避免纯反应式——不是简单回应用户说的每个词，而是有策略地引导对话流。

### 任务完成
任务目标是社交机器人对话的连贯性和用户满意度。100人用户研究对比5种 agent，SASSI 和自定义连贯性调查评估主观感知。本体驱动的对话管理在连贯性上优于纯关键词和随机方法，证明结构化话题知识对对话质量的关键作用。

## 关联
- [[DialogueTopicOntology]] — 对话话题本体
- [[DialogueFlowManagement]] — 对话流管理
- [[SocialDial]] — 社交感知对话本体
- [[PositiveFrictionDialogue]] — 正摩擦对话
- [[IntentDrivenMnS]] — 意图驱动管理（3GPP，已有wiki）

## 矛盾
- 无
