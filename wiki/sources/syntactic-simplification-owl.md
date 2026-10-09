---
title: "Syntactic Simplification of OWL Class Expressions（OWL类表达式句法简化）"
type: source
tags: [ontology-reasoning, reasoning-engine]
sources: [syntactic-simplification-owl]
source_file: raw/papers/syntactic-simplification-owl.pdf
last_updated: 2026-10-09
arxiv_id: "2608.18899"
authors: ["Alkid Baci", "N'Dah Jean Kouagou", "Caglar Demir", "Axel-Cyrille Ngonga Ngomo"]
year: 2026
venue: "arXiv (Paderborn University)"
citation_count: 0
---

## 概要

CES（Class Expression Simplifier）是一种基于重写规则的算法，用于在描述逻辑（DL）中对 OWL 类表达式做**句法简化**：通过系统地应用吸收律、幂等律、支配律等重写规则消除冗余，在**保持逻辑蕴含不变**的前提下得到更紧凑、更易读的类表达式。其目标是用 OWLAPY 的 StructuralReasoner 提升实例检索的推理效率，并作为类表达式学习系统（如 TDL）的默认后处理步骤。实验在 Carcinogenesis 与 Mutagenesis 两个中型本体上生成 200 个类表达式验证。

## 解决的问题

类表达式学习（CEL）常产生冗长复杂的 OWL 类表达式，既降低本体工程师的可读性和维护性，也在推理与查询回答中引入计算开销（[Pileggi et al. 2019] 指出表达力与计算性能的权衡）。已有工作聚焦语义推理、优化或本体模块化，**系统性的句法简化方法几乎空白**——FaCT++ 的 SNF 是最近却有限的对照点。句法层简化不需要推理器、独立于背景本体，因此可无侵入地嵌入任何学习管线。

## 方法与技术

1. **重写规则库**：定义覆盖 SOIQ(D)（限制传递角色、排除其他 RBox 公理）的句法简化规则——冗余消除（吸收律 C⊔(C⊓D)≡C）、幂等律（C⊓C≡C）、恒等/支配律（C⊓⊤≡C、C⊔⊤≡⊤）、排中律与非矛盾律（C⊔¬C≡⊤、C⊓¬C≡⊥）、量词分配（∀r.C⊓∀r.D≡∀r.(C⊓D)）、基数约束子sumption、析因分解（(C⊓D)⊔(C⊓E)≡C⊓(D⊔E)）。
2. **递归简化算法 `simplify(c,p)`**：single-dispatch 函数按类表达式类型特化，携带父 n-ary 表达式上下文 p 以应用需要父级信息的吸收律；先展平嵌套 n-ary 表达式、用集合去重实现幂等，单趟（one-pass）应用尽可能多的规则。
3. **析因分解 `apply_factorization`**：根级先转顶层 DNF 显式暴露析取结构，按 type_a/type_b 划分操作数，成对识别公共子表达式并局部析因，递归直至无法再简化——显著减少表示所需的 OWL 构造数。
4. **语义保持验证**：因缺乏全局合流性证明，改为经验验证——比较原表达式与简化表达式的实例检索集合等价性，确认蕴含不变。

## 创新点

- 首个专门面向 OWL 类表达式**句法**简化的重写算法，不同于 FaCT++ 仅提供受限的 SNF，CES 覆盖 SOIQ(D) 的量词、基数约束与析因。
- 单趟递归设计在保证终止（每趟收敛）的同时尽可能多地应用规则，且完全不依赖推理器——**推理器无关**，适用于无背景本体的场景。
- 作为 CEL 的"bonus"后处理：语义零风险（纯句法、蕴含保持），对任意学习器一致提供复杂度与效率改进。

## 效果

- Length reduction：最高长度缩减 **86%**（Mutagenesis 与 Carcinogenesis 各 200 个 TDL 生成表达式）。
- Runtime reduction：最高推理运行时间缩减 **90%**；平均简化时间 0.11s（Mutagenesis）/0.16s（Carcinogenesis），最长表达式（length 4284）仅 1.34s。
- 数据集：SML-bench 套件 Carcinogenesis + Mutagenesis | 学习器：TDL（Ontolearn 框架，已知产出最冗长假设）。
- 局限：仅评估 TDL 产出假设；单趟规则应用顺序影响结果，多趟/规则优先级仍开放。

## 关键引用

> "we evaluate correctness empirically via reasoning-based validation by comparing the sets of instances retrieved for the original and the simplified class expressions and confirming their equivalence." — Section 4, Evaluation

> "we recorded the highest length reduction to be 86% less than the original expression and the highest runtime reduction to be 90% less than the original." — Section 4, Evaluation

> "At present, CES operates exclusively at the syntactic level. This design choice avoids the need to rely on a reasoner, making the method broadly applicable and independent of the presence of a background ontology." — Section 5, Discussion and Conclusion

## 关联

- [[OntologyReasoning]] — 句法简化是推理效率优化的非推理器侧杠杆，与本概念页的符号推理器挑战呼应。
- [[OntologyGraphRetrieval]] — 更紧凑类表达式直接降低本体图检索的推理开销，与检索侧性能优化互补。
- [[neurowl]] — 同为 Paderborn/神经符号谱系；NeurOWL 用 LLM 联合推理，CES 则纯句法无损简化。
- [[owl2dl-differentiable-circuits]] — Baobab 关注语义编译，CES 关注句法化简，二者都面向"让本体可计算"。
