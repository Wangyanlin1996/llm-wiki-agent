---
title: "ABox Abduction for Inconsistent Knowledge Bases under Repair Semantics（修复语义下不一致KB的ABox溯因）"
type: source
tags: [ontology-reasoning, robustness]
sources: [abox-abduction-repair-semantics]
source_file: raw/papers/abox-abduction-repair-semantics.pdf
last_updated: 2026-10-09
arxiv_id: "2605.01341"
authors: ["Anselm Haak", "Patrick Koopmann", "Yasir Mahmood", "Anni-Yasmin Turhan"]
year: 2026
venue: "KR 2026"
citation_count: 2
---

## 概要

论文为**不一致知识库在修复语义下的 ABox 溯因（ABox abduction）**建立理论体系。给定含不可蕴含事实的 KB，ABox 溯因寻求扩展 KB 使其蕴含该事实的假设——应用于诊断、可解释性与修复。一致 KB + 经典语义下已有充分研究，但**不一致 KB（由错误数据引起）的情形此前几乎空白**。作者在修复语义（基于 ABox 最大一致子集的 repair semantics）下定义合适的溯因概念，并提出引导溯因走向"有用"假设的标准（conflict-confining、非平凡、最小化）。对轻量描述逻辑 DL-Lite 与 EL⊥ 给出 ABox 溯因在不同变体下的**复杂度全景**。

## 解决的问题

ABox 溯因（找假设 H 使 ⟨T,A∪H⟩|=Φ）在一致 KB 上成熟，但真实数据常含错误致 KB 不一致——不一致时经典语义下一切事实都被蕴含，溯因与演绎推理均失去意义。修复语义（基于 ABox 最大一致子集，如 Brave/AR 语义）能恢复有意义推理，但**修复语义下的溯因此前只有 Du et al. 针对可重写语言的 IAR 语义实用系统**；不同修复语义、不同逻辑、如何恰当定义溯因的完整图景缺失。

## 方法与技术

1. **修复语义下的溯因定义**：用修复语义的蕴含关系（Brave/AR 等，基于 ABox 最大一致子集）替代经典蕴含定义溯因——Brave 隔离各 repair、AR 同时考虑所有 repair。
2. **有用性标准（Criteria）**：定义引导溯因的准则——冲突受限（conflict-confining，假设不引入新冲突）、非平凡（H≠Φ）、最小化（≤-min/⊆-min 等变体）。
3. **复杂度分析**：对 DL-Lite 与 EL⊥、一般与受限签名、不同修复语义，给出存在性/验证问题的复杂度（NL 到 NP 层级）。
4. **动机案例**：糖尿病医学本体病例（High⊓Low⊑⊥、∃glucoseLevel.High⊑GlycemicCrisis 等）演示 Brave vs AR 语义下假设差异（谨慎医生应查 AR 下的 {Ketoacidosis}）。
5. **理论定位**：与一致 KB 溯因、缺失蕴含解释（Bienvenu et al.）、paraconsistent 溯因对照。

## 创新点

- 首个系统刻画**修复语义下 ABox 溯因**的复杂度全景（DL-Lite/EL⊥ × Brave/AR × 存在/验证 × 签名约束）。
- 定义"冲突受限"等修复语义特有的有用性标准——经典溯因的"一致性要求"在修复语义下需要重新诠释（假设本身可能不引入新冲突即可）。
- 揭示非平凡条件在修复语义下不再平凡（观察本身可能不满足条件、其他假设引入更少冲突），是经典溯因理论在非经典语义下的新结果。

## 效果

- **复杂度结果**：DL-Lite（Brave 存在性 NL 级到更复杂层级）与 EL⊥ 各变体的存在/验证问题复杂度完整刻画（表格 T13 等）。
- **语义对比**：Brave vs AR 语义下假设集差异实例化（医学病例：Brave 下 {OverdosedInsulin}/{Ketoacidosis} 均成立，AR 下仅 {Ketoacidosis}）。
- 与 Du et al.（IAR 语义、可重写语言）对照，补充 IAR/AR/Brave 谱系缺口。
- 应用面：诊断、解释缺失蕴含、修复建议。

## 关键引用

> "To regain meaningful reasoning in the presence of inconsistencies, we use well-established repair semantics. We provide a comprehensive landscape of the complexity of ABox abduction under repair semantics, treating different variants of the abduction problem for the light-weight description logics DL-Lite and EL⊥." — Abstract

> "Indeed, the cautious doctor should investigate this hypothesis first." — Section 1 (关于 AR 语义下唯一假设 {Ketoacidosis})

> "Also, allowing for the observation itself as the trivial hypothesis does not as easily trivialise the problem as under classical semantics: It might not always satisfy the conditions..." — Section 1, Introduction

## 关联

- [[OntologyReasoning]] — 溯因（abduction）是本概念页推理任务（包含验证/可满足性/一致性/查询回答）之外的非单调补充。
- [[InconsistencyTolerantReasoning]] — 修复语义（MCS 谱系）是不一致容忍推理核心，本文在其上定义溯因。
- [[inconsistency-kg-reasoning-survey]] — 综述"修复"方向（ABox 修复）的理论深化：溯因为修复提供假设建议。
- [[CausalExplanation]] — 溯因为"解释缺失蕴含"提供形式基础，与反事实/因果解释互补。
