---
title: "To Neuro-Symbolic Classification and Beyond by Compiling DL Ontologies to Probabilistic Circuits（本体编译为概率电路）"
type: source
tags: [ontology-reasoning, reasoning-engine, neuro-symbolic]
sources: [dl-ontologies-probabilistic-circuits]
source_file: raw/papers/dl-ontologies-probabilistic-circuits.pdf
last_updated: 2026-10-09
arxiv_id: "2601.14894"
authors: ["Nicolas Lazzari", "Valentina Presutti", "Antonio Vergari"]
year: 2026
venue: "arXiv (U. Pisa / U. Bologna / U. Edinburgh)"
citation_count: 3
---

## 概要

本文提出将描述逻辑（DL）本体编译为**概率电路**（circuit，前馈可微计算图），从而在神经网络分类器与形式本体知识之间建立端到端可微的神经符号（NeSy）集成。同一个电路表示可同时用于三项任务：(1) 生成捕获本体语义的合成数据集；(2) 在 GPU 上高效执行演绎推理；(3) 设计预测结果与本体逻辑约束**近似或可证明一致**的 NeSy 分类器。相比现有 NeSy 方法（基于 FOL 的概率推理昂贵、fuzzy 方法需精心设计、命题逻辑表达力不足），DL 本体是"表达力-可计算性"的折中载体。

## 解决的问题

深度模型在领域特定场景（如从传记文本抽取艺术家影响关系）中不可靠——预测可能与背景本体矛盾（如预测"唱片公司影响了乐队"）。在数据稀缺的领域特定设置中，无法靠大规模一致数据训练来规避。已有神经符号方法存在表达力、可计算性与保证可靠性之间的张力：FOL 概率方法推理昂贵，fuzzy 方法需仔细设计，命题逻辑方法表达力不足。**DL 本体作为 NeSy 载体此前相对未开发**，且多数集成方法难以评估其可靠性增强效果。

## 方法与技术

1. **知识编译到电路**：将本体 O 编译为 SDD 类电路 CO（输入/和/积单元构成的有向无环图），输入单元对应本体概念、角色与角色约束；在命题层面保持逻辑意义，支持线性时间加权模型计数（WMC）。
2. **合成数据生成（C1）**：电路编码本体语义，采样生成"语义正确但内容多样"的合成数据集，作为下游分类器训练/评测基础。
3. **GPU 演绎推理（C2）**：电路前馈可微，支持在 GPU 上批量执行本体查询与变换，实现可扩展演绎推理。
4. **NeSy 分类器（C3）**：将电路作为可微约束注入网络——hard 变体保证预测与本体一致，soft 变体以软约束容忍部分违反；训练时全可微（对网络输入求导），推理时以 WMC 检查一致性。

## 创新点

- 首次将 DL 本体（不止命题逻辑）与概率电路编译结合，单个电路同时服务数据生成、GPU 推理与 NeSy 训练——不同于 Rudolph 仅用电路作为 Datalog 演绎推理的中间表示。
- 相对现有 DL NeSy 方法（EL Embeddings、OWL2Vec* 等嵌入方法不计算经典蕴含；DeepProbLog/Semantic Loss 等知识编译方法仅支持命题或 Datalog）——本文把**经典 DL 语义端到端保留**在可微训练信号中。
- 提供近似或**可证明**一致的预测，且竞争力保持或超过纯神经网络基线。

## 效果

- 演绎推理：电路编译路径在大型本体上比可用推理器**快最多 3 个数量级（orders of magnitude）**，GPU 批量执行。
- 数据集：基于 Wikidata 的音乐艺术家影响关系本体（Artist/Label 互斥、signedTo/influence 约束）；合成数据集"挑战性但语义保真"。
- NeSy 分类器：与神经网络基线相比维持竞争力甚至超越，同时显著降低违反本体约束的预测。
- 一致性保证：hard 变体可证明预测与本体一致；soft 变体近似一致。

## 关键引用

> "We show that compiling the ontology into a circuit is a promising approach for scalable deductive reasoning, with runtimes up to three orders of magnitude faster than available reasoners." — Abstract

> "We adapt this approach and show that the resulting circuit can be used to: C1 generate a synthetic dataset that encapsulates the semantics of the ontology; C2 efficiently perform deductive reasoning on a GPU; C3 design NeSy classifiers that approximately or provably output predictions consistent with the background knowledge expressed in the ontology." — Section 1, Introduction

> "DL languages are a promising formalism for NeSy models since they are essentially subsets of FOL that benefit from more tractable inference routines while retaining enough expressiveness to formalize complex domain-specific knowledge." — Section 1, Introduction

## 关联

- [[OntologyReasoning]] — 电路编译是本概念页"LLM/神经方法增强本体推理"路线中的硬件/编译侧路径（GPU 演绎）。
- [[owl2dl-differentiable-circuits]] — 姊妹工作 Baobab 把 SROIQ 编译到 SDD 做 WMC 训练感知网络；本文则编译 ALC 系本体覆盖数据生成+推理+分类三用途。
- [[NeurosymbolicOrchestration]] — 本体的电路表示是神经符号编排中"符号引擎可验证执行"的可微实现。
- [[neural-shqoi-instance-retrieval]] — Ebr 用嵌入近似推理，本文用电路近似推理，是"可微推理器"的两种实现路线。
