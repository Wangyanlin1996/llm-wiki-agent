---
title: "From Subsumption to Satisfiability: LLM-Assisted Active Learning for OWL Ontologies（LLM辅助本体主动学习）"
type: source
tags: [ontology-reasoning, llm-reasoner-hybrid]
sources: [llm-active-learning-owl]
source_file: raw/papers/llm-active-learning-owl.pdf
last_updated: 2026-10-09
arxiv_id: "2604.16672"
authors: ["Haoruo Zhao", "Wenshuo Tang", "Duncan Guthrie", "Michele Sevegnani", "David Flynn", "Paul Harvey"]
year: 2026
venue: "arXiv (University of Glasgow)"
citation_count: 1
---

## 概要

本文在 Angluin 精确学习框架中引入 LLM 作为**第三方组件**辅助本体主动学习：将每个候选公理按描述逻辑中"子sumption 归约到可满足性"的标准归约，构造成对应的**反概念（counter-concept）**，用受控自然语言（CNL）言语化后提交给 LLM。LLM 用真实世界例子近似反概念实例，为本体工程师提供辅助指导。论文形式化证明：在开放世界假设（OWA）下，该方法**只可能产生 II 类错误**（假负），最坏情形仅延迟本体构建而非引入不一致公理。实验在 13 个商用 LLM 上验证 recall（II 类错误的度量）跨多个成熟本体保持稳定。

## 解决的问题

本体工程依赖本体工程师与领域专家的频繁交互（Angluin 精确学习框架中领域专家作教师），但专家教师成本高昂、查询数多。用 LLM 替代教师（Magnini et al. 2025）会因幻觉引入错误，且偏离 Konev et al. (2018) 的"教师诚实回答"假设。核心矛盾：如何利用 LLM 的常识知识辅助建模，同时**不引入会污染本体逻辑后果的错误公理**。

## 方法与技术

1. **子sumption→可满足性归约**：对候选公理（如 "every apple is a fruit"，C⊑D），构造反概念 C⊓¬D，将子sumption 测试转为反概念可满足性测试。
2. **受控自然语言言语化**：把反概念 verbalize 成 CNL 描述，形成 LLM 提示——把推理任务化为纯语言任务，降低 LLM 形式化符号理解负担。
3. **LLM 实例近似**：LLM 用真实世界例子近似反概念实例（回答如"是否存在不是水果的苹果？"），仅作辅助指导，本体工程师与领域专家交互不变。
4. **混淆矩阵误差分析（OWA）**：在开放世界假设下证明假负（II 类）与假正（I 类）影响不对称；方法设计保证**只产生 II 类错误**——最坏推迟构建、不改变本体逻辑后果。
5. **Recall 度量**：用 recall（对应 II 类错误频率）作为核心评测指标。

## 创新点

- 首次将"子sumption→可满足性"的逻辑归约引入 LLM 辅助本体建模，把成员查询转为反概念实例判断——不同于直接让 LLM 回答子sumption 真假。
- 形式化保证**仅 II 类错误**：LLM 幻觉最多延迟构建、绝不引入错误公理——相对直接 LLM 教师方案（可能污染本体）的本质优势。
- 在 13 个商用 LLM 上的系统性 recall 评测，支撑工程可用性结论。

## 效果

- **LLM 评测**：13 个商用 LLM（含 GPT 系等）上 recall 保持稳定；在多个成熟本体（OWL 本体设置）上跨模型一致。
- **错误保证**：证明方法只产生 II 类错误（OWA 下），不引入不一致公理。
- 数据集：多个已建立的本体（biomedical 类 SNOMED CT/GO/HPO/FMA 语境及 SAREF/IES4 等新兴本体）。
- 语义：ALCIQ(D) 本体（含逆角色与具体域角色）。

## 关键引用

> "We introduce LLMs as a third component that provides real-world examples approximating an instance of the counter-concept. This design property ensures that only Type II errors may occur in ontology modelling." — Abstract

> "Inspired by the standard reduction of subsumption to satisfiability in description logics, we reformulate each candidate axiom into its corresponding counter-concept and verbalise it in controlled natural language before presenting it to Large Language Models." — Abstract

> "Results across 13 commercial LLMs indicate that recall remains high even under conservative assumptions, suggesting that the approach can be applied in practical ontology modelling settings." — Abstract

## 关联

- [[OntologyReasoning]] — LLM 作为本体建模教师是"LLM 增强本体工程"路线，与推理器验证评测互补。
- [[ontology-grounded-reasoner-benchmarks]] — 互补：前者用 LLM 回答推理查询辅助建模（可满足性），后者用推理器验证 MCQ 供 LLM 评测。
- [[NeuroSymbolicOntology]] — 神符号本体注入：本文用 LLM 语义近似 + 符号框架保证错误方向，同属"LLM+符号"协作范式。
- [[OntologyFirstAgentDesign]] — LLM 辅助构建的本体可作为 agent 架构的语义基础层。
