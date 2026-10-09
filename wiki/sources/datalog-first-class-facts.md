---
title: "Datalog with First-Class Facts（一等事实的 Datalog：DL∃! 与 Slog）"
type: source
tags: [ontology-reasoning, reasoning-engine]
sources: [datalog-first-class-facts]
source_file: raw/papers/datalog-first-class-facts.pdf
last_updated: 2026-10-09
arxiv_id: "2411.14330"
authors: ["Thomas Gilray", "Arash Sahebolamri", "Yihao Sun", "Sowmith Kunapaneni", "Sidharth Kumar", "Kristopher Micinski"]
year: 2024
venue: "PVLDB 18(3)"
citation_count: 3
---

## 概要

DL∃! 是"一等事实（first-class facts）"的 Datalog 扩展：每个事实由其特有的 Skolem 项唯一标识，规则头使用唯一存在量化（∃!）。这一约束使 Datalog 能够对树形结构数据（派生树、抽象语法树）做归纳推理，同时保持与现代并行关系代数实现兼容。配套语言 DLS 编译到 DL∃!，实现系统 **Slog** 基于 MPI 的通信避免、大规模并行架构，在多个基准上超越 Nemo、Vlog、RDFox 与 Soufflé 等领先系统，可扩展到数千线程。

## 解决的问题

Datalog 是本体推理、程序分析等演绎推理的事实标准，但**扁平原子常量事实**限制了树形数据的处理。现有扩展不完美：Datalog±/Datalog∃ 引入规则头存在量化但需 unify、实现复杂；Soufflé 的代数数据类型（ADT）无法触发规则求值、缺乏高效索引支持。需要一种在表达力与实现简单性之间取得"有吸引力的平衡点"的扩展。

## 方法与技术

1. **唯一存在量化（∃!）语义**：每个事实蕴含自身标识的存在——Skolem 项唯一到事实；禁止头与体合一，避免循环引用、保证有限扩张集（finitely-expanding）。
2. **受控 chase 语义**：以 restricted chase 为基础给出 DL∃! 的 chase 语义，实现因"所有事实结构唯一"而大幅简化——无需 unify，每个（子）事实关联唯一 intern id。
3. **DLS 语言**：支持直接嵌套事实的更自然编程语法，编译到 DL∃!（等价表达能力），作为实现的语言基础。
4. **Slog 并行引擎**：利用 DL∃! 唯一性实现锁自由、通信避免的 MPI 大规模并行（结构化数据上的树形事实推理）。
5. **应用展示**：provenance、代数数据类型（Soufflé 风格）、函数式编程（IncA）、结构抽象解释、类型系统等场景的 DL∃! 应用。

## 创新点

- 相对 Datalog∃（一般存在量化需 unify、半可判定）：∃! 限制换来"事实即 Skolem 项"的简洁语义 + 平凡并行实现。
- 相对 Soufflé ADT：一等事实（而非独立代数类型）参与规则求值与高效索引，不牺牲触发能力。
- 首个将"通信避免"用于树形 Datalog 事实的大规模并行实现，兼容现代并行 Datalog 技术栈。

## 效果

- 基准：在多样 benchmark 上 Slog 超越 Nemo、Vlog、RDFox 与 Soufflé（领先系统）。
- 扩展性：具备扩展到数千线程的潜力（MPI 通信避免架构）。
- 表达力：支持 provenance、ADT、函数式编程（IncA）、结构抽象解释、类型系统等跨领域应用。
- 语义保证：DL∃! 一般半可判定，但每次迭代产出递增的更大事实、每轮有限——保证单调有限扩张。

## 关键引用

> "We present DL∃!, a Datalog with first-class facts, wherein every fact is identified with a Skolem term unique to the fact. We show that this restriction offers an attractive price point for Datalog-based reasoning over tree-shaped data." — Abstract

> "The syntactic restrictions of DL∃! forbid unifying the head with the body, thereby preventing cyclic reference and yielding finite expansion sets." — Section 1, Introduction

> "We show that Slog outperforms leading systems (Nemo, Vlog, RDFox, and Soufflé) on a variety of benchmarks, with the potential to scale to thousands of threads." — Abstract

## 关联

- [[OntologyReasoning]] — Datalog 系引擎是本体推理的规则化实现路线（与 tableau/EL 并列），本文解决树形数据的表达力缺口。
- [[meteror-metric-temporal-reasoning]] — 同为 Datalog 系推理引擎；MeTeoR 侧重时序算子，Slog 侧重结构化/树形数据并行。
- [[datalogmtl-seminaive-materialisation]] — seminaïve 物化消除冗余，Slog 用通信避免消除冗余，是 Datalog 效率优化的两条主线。
- [[OntologyGraphRetrieval]] — 树形派生结构的推理支撑本体图上的复杂模式检索。
