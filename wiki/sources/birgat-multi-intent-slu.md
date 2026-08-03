---
title: "BiRGAT: 层次语义框架多意图口语理解 (Multi-intent SLU)"
type: source
tags: [ontology-intent-understanding]
sources: [birgat-multi-intent-slu]
source_file: raw/papers/birgat-multi-intent-slu.pdf
last_updated: 2026-08-03
arxiv_id: "2402.18258"
authors: ["Hongshen Xu", "Ruisheng Cao", "Su Zhu", "Sheng Jiang", "Hanchong Zhang", "Lu Chen", "Kai Yu"]
year: 2024
venue: "ICASSP 2024"
citation_count: 6
doi: "10.1109/ICASSP48485.2024.10446325"
---

## 概要

本文针对口语语言理解（SLU）中单意图设置的局限，提出 MIVS 多意图数据集和 BiRGAT 模型。目标语义框架组织为 3 层层次结构，使用双关系图注意力网络编码本体项层次，配合三路指针生成器解码器，解决多意图场景中的对齐和分配问题。

## 解决的问题

传统 SLU 主要聚焦单意图设置，每个输入话语仅含一个用户意图。这严重限制了用户话语的表面形式和输出语义容量。多意图场景中存在对齐（alignment，意图与槽位的对应关系）和分配（assignment，槽值到正确意图的分配）两大挑战。

## 方法与技术

1. **MIVS 数据集**：从真实车载对话系统收集的多意图数据集
2. **3 层层次语义框架**：目标语义框架组织为层次结构解决多意图对齐
3. **BiRGAT 模型**：双关系图注意力网络编码本体项层次结构
4. **三路指针生成器解码器**：3-way pointer-generator decoder 用于解码层次框架

## 创新点

- 首个从真实车载对话系统收集的多意图数据集 MIVS
- 3 层层次语义框架显式建模多意图的对齐和分配关系
- BiRGAT 用图注意力网络编码本体层次，替代传统序列标注和分类方案

## 效果

- 大幅超越传统序列标注和分类方案
- 在多意图对齐和分配任务上显著提升
- ICASSP 2024 录用，6 次引用

## 关键引用

> "This configuration significantly limits the surface form of user utterances and the capacity of output semantics." — 指出单意图设置的局限

## 关联

- [[OntologyAwareTOD]] — 本体层次结构用于任务型对话
- [[DialogueStateTrackingOntology]] — 本体定义 slot/值域/约束用于DST
- [[IntentUnderstanding]] — 多意图理解与对齐
- [[NOEM³A]] — 同为本体增强多意图理解，NOEM³A 用本体注入+解码先验
