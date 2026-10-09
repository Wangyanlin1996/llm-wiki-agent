---
title: "Ontology Revision based on Pre-trained Language Models（基于预训练语言模型的本体修订）"
type: source
tags: [ontology-reasoning, robustness]
sources: [ontology-revision-plm]
source_file: raw/papers/ontology-revision-plm.pdf
last_updated: 2026-10-09
arxiv_id: "2310.18378"
authors: ["Qiu Ji", "Xiaoping Zhang", "Yuxin Ye", "Guilin Qi", "Jiaye Li", "Site Li", "Jianjie Ren", "Songtao Lu"]
year: 2023
venue: "arXiv (NJUPT / CACM / Jilin U / Southeast U)"
citation_count: 1
---

## 概要

本文研究用预训练语言模型（PLM）编码公理语义来**修订本体**（ontology revision）：把不协调（incoherent，含不可满足概念）的本体通过删除/重排公理恢复协调。作者先用 PLM 将本体公理转成自然语言句子并编码为稠密向量，据此定义四个公理排序评分函数（考虑本体各类信息），再提出一次处理所有不可满足概念的修订算法与逐组处理的适配算法以提效。在 19 对本体对上实验，算法取得有竞争力性能，适配算法大幅提效（某些对本最多省 ~90% 时间），评分函数如 reliableOnt_cos 在困难对（如 OM8）上效果显著。

## 解决的问题

本体修订要把新本体无缝并入现有本体，在演化/维护/对齐中至关重要。**不协调（含不可满足概念）是导致不一致的主要潜在因素**，与不一致本体推理会得到无意义结果。现有修订方法定义修订算子与公理排序策略，但**很少利用公理语义**（区分公理的重要信息）。PLM 能编码公理语义且已广泛用于 NLP 与本体任务——如何用 PLM 提升修订质量与效率是核心问题。

## 方法与技术

1. **公理语义编码**：本体公理翻译为自然语言句子，PLM 计算稠密向量；公理间相似度用 Cosine Distance。
2. **四个评分函数**：基于 PLM 向量与本体信息的四种公理排序函数（如 reliableOnt_cos 等），考虑公理可靠性、与其他公理一致性等维度。
3. **修订算法（一次处理）**：根据评分函数处理所有不可满足概念，删除/调整公理恢复协调。
4. **适配修订算法（逐组处理）**：按组处理不可满足概念以提升效率，牺牲少量质量换大幅时间节省。
5. **19 对本本体评测**：与现有修订算法与评分函数对比，评估性能与效率。

## 创新点

- 首次系统研究将 PLM 应用于**本体修订**（公理语义驱动的排序），区别于已有依赖逻辑闭包/权重/信任的算子。
- 四评分函数显式编码公理语义差异——公理不再"等权重"对待。
- 适配算法实现质量-效率权衡，最多省 ~90% 时间；困难对齐对（OM8）上 reliableOnt_cos 显著提升结果。

## 效果

- **数据集**：19 对本本体（含挑战性对齐对 OM8）。
- **效率**：适配修订算法大幅提升效率，某些本体对最多节省约 90% 时间。
- **质量**：多评分函数优于现有方法；reliableOnt_cos 在 OM8 等困难对上显著更优。
- 提供按语义与性能选择修订算法的实用指南。

## 关键引用

> "Although existing ontology revision approaches provide various strategies or scoring functions to rank axioms, they rarely consider the semantics of axioms which provides an efficient way to differentiate axioms." — Section 1, Introduction

> "The adapted revision algorithm could improve the efficiency largely, and at most about 90% of the time could be saved for some ontology pairs." — Abstract

> "Some of our scoring functions like reliableOnt_cos could help a revision algorithm obtain better results in many cases, especially for those challenging ontology pairs like OM8." — Abstract

## 关联

- [[OntologyReasoning]] — 本体修订是保持本体协调（可推理）的关键生命周期环节。
- [[InconsistencyTolerantReasoning]] — 互补路线：修订是"修复不一致"家族（删除公理恢复协调），与"容忍不一致推理"（MCS/近似蕴含）并列为不一致处理的第三方向。
- [[embedding-inconsistency-tolerant]] — 均用公理语义/嵌入区分公理；该文用于修订排序，后者用于 MCS 选择。
- [[OntologyMatching]] — 修订与本体对齐/匹配直接关联（对齐映射可译为 OWL 公理）。
