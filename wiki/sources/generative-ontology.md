---
title: "Generative Ontology: 当结构化知识学会创造（When Structured Knowledge Learns to Create）"
type: source
tags: [ontology-skill-routing]
sources: [generative-ontology]
source_file: raw/papers/generative-ontology.pdf
last_updated: 2026-09-08
arxiv_id: "2602.05636"
authors: ["Benny Cheung"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
---

## 概要
本文提出 Generative Ontology 框架，将传统 ontology 的结构精确性与 LLM 的创造力进行合成：ontology 提供"语法"，LLM 提供"创造力"。领域知识被编码为可执行的 Pydantic schemas，通过 DSPy signatures 约束 LLM 生成；多 agent 流水线为不同 ontology 域分配专业化角色（Mechanics Architect、Theme Weaver、Balance Critic 等），每个 agent 携带"职业焦虑"以避免浅层输出。框架通过 GameGrammar 系统在桌面游戏设计领域验证，包含消融实验（120 designs）、基准对比（20 款已出版桌游）和评估器信度分析（ICC）三项实证研究。

## 解决的问题
核心痛点是结构性幻觉（Structural Hallucination）：LLM 能流畅地"描述"游戏设计，但生成的输出缺乏结构有效性——机制没有对应组件、目标没有结束条件，"听起来合理但无法游玩"。传统 ontology 精确但被动，只能描述已有事物而无法创造新输出；LLM 创造力丰富但无结构约束。此前工作如 DRAGON-AI、OLLM 用 LLM 生成 ontology（方向相反），Mehenni & Zouaq 做了 ontology-constrained 生成但目标是减少摘要幻觉而非结构化创造力。

## 方法与技术
1. **Executable Schema 转换**：将 ontology 类映射为 Pydantic BaseModel，字段类型验证 + enum 约束限定 LLM 只能引用已识别的机制类型，min_length 约束防止模糊输出。
2. **DSPy Signature 操作化**：用 DSPy 的 typed signature 将 LLM 交互声明为组合式操作；ChainOfThought 模块让模型先推理再输出结构化结果，添加语义一致性验证。
3. **Anxiety-Driven 多 Agent 流水线**：5 个 agent 分工——Mechanics Architect（机制/回合结构）、Theme Weaver（叙事）、Component Designer（组件）、Balance Critic（跨域漏洞检测）、Fun Factor Judge（体验评估）；每个 agent 被赋予"职业焦虑"。
4. **两阶段 RAG**：从 BoardGameGeek 的 1,767 款游戏语料中，先按 MechanismType taxonomy 做 ontology filtering，再按 embedding similarity 做语义排名。
5. **Validation Contract**：将 ontology 编码为验证函数——机制-组件依赖字典；DSPy Assert 机制在验证失败时自动携带错误信息重试生成。

## 创新点
- **Ontology 作为生成语法（而非分析工具或 LLM 生成对象）**（vs DRAGON-AI/OLLM 用 LLM 生成 ontology，方向根本不同）——本文用 ontology 约束 LLM 生成。
- **Constraint Paradox 实证发现**——"约束单独不提升创造质量，但约束+架构特化产生最大增益"。提出 Constraint–Architecture Interaction Model：创造质量 ≈ 约束表达力 × 架构特化度。
- **Anxiety-Driven Agent 设计**——每个 agent 不是简单分配域而是被赋予"职业焦虑"，系统性地对抗 LLM 的"yes-man"倾向。
- **LLM-as-Judge 的 Test-Retest 信度验证**——报告 ICC(2,1) 而非假设评估器可靠，7/9 指标达 Good-to-Excellent。

## 效果
- Dataset: GameGrammar ablation | Metric: Consistency Errors | C1 Baseline: 5.03 | C2 Schema: 0.10 | Δ: d=4.78, p<.001
- Dataset: GameGrammar ablation | Metric: Strategic Depth (C3→C4) | Result: d=1.59 | p<.001
- Dataset: GameGrammar ablation | Metric: Fun (C3→C4) | Result: d=1.12 | p<.001
- Dataset: Published benchmark | Metric: Fun Rating | Real: 8.90 | Generated: 8.07 | Δ: d=1.86
- Dataset: Published benchmark | Metric: Tension & Drama | Real: 8.50 | Gen: 8.20 | Δ: d=0.35, ns (parity)
- Dataset: ICC analysis | Metric: Tension & Drama ICC | Result: 0.989 (Excellent)
- **Ablation**: Schema validation (C1→C2) is the single largest structural improvement (errors 5.03→0.10, d=4.78); constraints alone do NOT improve creative quality; only multi-agent specialization (C4) does

## 关键引用
> "Analysis is not creation. Understanding the structure of sonnets does not make one a poet. Knowing the rules of chess does not generate new games." — Section 1, p.1

> "Constraints alone suppress richness; constraints plus specialization enable it." — Section 12.1, p.14

> "The grammar does not write the poem. But without grammar, there is no poem to write." — Section 13, p.16

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[OntologyFirstAgentDesign]] — Round 13 本体优先 Agent 设计
- [[dynamic-ontology-llm-agents]] — Round 16 动态本体内核
- [[auto-ontology-construction-llm]] — Round 13 LLM 外部本体记忆层
- [[OntologyReasoning]] — Round 13 本体推理
