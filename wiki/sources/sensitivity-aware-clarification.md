---
title: "敏感感知的检索增强意图澄清"
type: source
tags: [memory-intent-clarification, RAG, sensitivity-aware, conversational-search]
sources: [sensitivity-aware-clarification]
source_file: raw/papers/sensitivity-aware-clarification.pdf
last_updated: 2026-06-27
arxiv_id: "2603.06025"
authors: ["Maik Larooij"]
year: 2026
venue: "CoSCIN@ECIR2026 Workshop"
citation_count: null
doi: "10.48550/arXiv.2603.06025"
---

## 概要
本文探索在敏感域（医疗、政府、法律）中用检索增强对话 Agent 进行意图澄清的研究挑战。检索增强意图澄清（retrieval-augmented intent clarification）可以显著提升澄清性能，但敏感域的检索库可能包含需要保护的信息。提出三步框架：定义攻击模型、设计检索级敏感感知防御、开发评估方法衡量保护与效用的权衡。

## 关键贡献
- 首次将检索增强意图澄清与敏感信息保护结合——记忆增强澄清的安全维度
- 攻击模型 + 检索级防御 + 权衡评估的三步框架
- 探索搜索范式下意图澄清的迭代演化视角

## 关键引用
> "Augmenting the clarification component with a retrieval step (retrieval-augmented intent clarification) can seriously enhance clarification performance, especially in domains where LLMs lack parametric knowledge." — 检索增强澄清的核心价值

## 关联
- [[RetrievalAugmentedClarification]] — 与 [[rac]]、[[corpus-rag-clarifying]] 同属 RAG 增强澄清方向
- [[IntentUnderstanding]] — 检索增强意图澄清是记忆增强意图理解在敏感域的延伸
- [[DS-IA Framework]] — 两者都关注意图系统的安全维度：本文是检索安全，DS-IA 是语义防火墙

## 矛盾
- 与 [[rac]] 的关注点不同：RAC 追求语料锚定的最大化利用，本文关注敏感域中检索的受限使用
