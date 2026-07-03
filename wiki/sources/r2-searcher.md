---
title: "R²-Searcher：校准 Agentic 搜索的检索-推理边界"
type: source
tags: ['semantic-retrieval', 'agentic-retrieval']
sources: [r2-searcher]
source_file: raw/papers/r2-searcher.pdf
last_updated: 2026-07-02
arxiv_id: "2606.28566"
authors: ["Sheng Zhang", "Junyi Li", "Wenlin Zhang", "Xiaowei Qian", "Yichao Wang", "Yingyi Zhang", "Maolin Wang", "Yong Liu", "Xiangyu Zhao"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要

多跳推理的搜索 agent 常因检索不完整证据或在检索内容的不相关部分上推理而失败，导致**检索-推理边界偏移**。本文识别两种具体表现：(1) 逐步观察中的注意力稀释——LLM 搜索 agent 每步接收冗长复杂的文档，关键证据被忽视或误用，使推理边界偏离答案相关内容；(2) 极大的查询-文档交互空间使迭代检索高度不稳定，无显式信号判断检索证据是否支撑当前推理状态时，agent 易漂向无关上下文并在多步上累积错误。现有方法（文档摘要、查询增强）与推理过程松耦合，无法判断检索内容是否支撑当前推理需求。本文提出 **R²-Searcher**：(1) **query-token 语义引导**——按词性将查询分解为主语/动作/程度修饰/时间标记 token 组，从检索内容提取对应精确事实构建细粒度推理上下文（reasoning region），引导 agent 注意力；(2) **检索反思机制**——每步检索后评估并纠正边界偏差（充足/不足/完全失配三态），生成基于推理上下文的改进查询；(3) **R²PO** 端到端推理-反思引导 RL 算法，通过树探索联合优化检索与推理边界。7 个复杂多跳 QA 基准上显著超越 SOTA agentic search 方法。

## 关键贡献

- **检索-推理边界形式化与校准**：定义检索边界（观察含全部必要证据）与推理边界（推理覆盖必要事实元素），证明正确推理需要正确检索但正确检索不保证正确推理，R²-Searcher 通过细粒度推理上下文 + 反思联合校准两边界
- **query-token 引导的推理区域**：按词性分解查询为 token 组（名词=主语/时间标记，动词=动作，形容词副词=程度修饰），对应提取事实形成显式推理区域，克服复杂/模糊查询语义下关键信息被忽视的问题
- **R²PO 树探索 RL 联合优化**：通过树展开探索推理状态与检索动作的联合空间，以过程级奖励信号优化推理区域提取、反思与搜索策略

## 关键引用

> "Search agents suffer from a persistent misalignment between retrieval and reasoning, where retrieved content does not reliably support the inference state required at each step of the search."

## 关联

- [[AgenticRetrieval]] — 本文是该概念在多跳推理场景的核心方法，直接校准 agent 检索与推理的边界
- [[RetrievalAugmentedGeneration]] — 检索-推理边界校准是 RAG 多跳推理可靠性的关键路径
- [[kbsd-knowledge-boundary]] — 互补关系：本文校准检索-推理边界（何时检索何内容），后者校准知识边界（何时信任记忆/依赖检索/弃答）

## 矛盾

无已知矛盾。
