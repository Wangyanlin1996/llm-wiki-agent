---
title: "HoTT-NeSy: 同伦类型论推广神经符号推理"
type: source
tags: [ontology-reasoning, neuro-symbolic]
sources: [hott-nesy-neurosymbolic]
source_file: raw/papers/hott-nesy-neurosymbolic.pdf
last_updated: 2026-07-25
arxiv_id: "2606.17851"
authors: ["Fernando Zhapa-Camacho", "Robert Hoehndorf"]
year: 2026
venue: ""
citation_count: 0
---

## 概要
本文提出用同伦类型论（HoTT）推广神经符号（NeSy）推理。大量 NeSy 系统计算一个函数：在 σ-结构空间上的逻辑量的信念加权和，加权模型计数、模糊逻辑和概率逻辑是其特例。该表示基于集合，而集合故意遗忘了两个对 NeSy 重要的事情：两个 σ-结构何时在理论对称下相同，以及多少不同证明见证一个查询。用类型替代底层集合可保留这些信息，将该函数变为信念加权同伦基数——一种按对象对称性反比计数的尺寸概念。

## 关键贡献
- 用同伦类型论推广神经符号推理，保留对称性和证明计数信息
- 证明保守性定理：当对称性平凡时恢复经典函数
- 展示框架揭示的对称性正是推理捷径（reasoning shortcuts）背后的对称性
- 在 MNIST 推理捷径基准上，单模型包装优于多样性训练集成

## 关键引用
> "Replacing the underlying sets by types, in the sense of homotopy type theory, preserves this information, and turns this functional into a belief-weighted homotopy cardinality, a notion of size that counts each object in inverse proportion to its symmetries."

## 关联
- [[OntologyReasoning]] — 本体推理核心方法
- [[NeuroSymbolicOntology]] — 神符号本体注入框架
- [[neurowl]] — LLM增强不完整OWL推理
- [[vadaorchestra]] — LLM编排+Datalog+/-符号引擎

## 矛盾
- 无
