---
title: "Systematic Evaluation of KG Repair with LLMs（SHACL 违规修复系统化评测）"
type: source
tags: [owl2-reasoning]
sources: [kg-repair-shacl-llm]
source_file: raw/papers/kg-repair-shacl-llm.pdf
last_updated: 2026-10-21
arxiv_id: "2507.22419"
authors: ["Tung-Wei Lin", "Gabe Fierro", "Han Li", "Tianzhen Hong", "Pierluigi Nuzzo", "Alberto Sangiovanni-Vincentelli"]
year: 2025
venue: "arXiv preprint (LNCS format)"
citation_count: 1
doi: ""
---

## 概要
KG 修复（SHACL 违规后自动修复）缺乏严谨评测基准。本文提出 VIO（violation-inducing operations）机制：把"约束+焦点节点"映射为一组 SPARQL add/remove 操作系统性制造违规且**正确修复已知**（恢复原图），从而对任意 KG 可控枚举全部违规类型。用该框架评估 4 LLM × 9 提示策略的修复原型：语法有效 97.35%、语义有效 86.17%、但 relaxed isomorphism 仅 54.07%——LLM 能修好违规却常常不能还原"最优修复"。关键发现：精选上下文（源 shape + 依赖 + 焦点节点相关三元组 + 一个正例）显著优于塞入整个 manifest。

## 解决的问题
现有 KG 修复评估依赖临时数据集（Wikidata 编辑历史或小型人工 SHACL test suite），无法细粒度刻画修复系统在新图/新约束上的行为。已有修复方法不足：Schimatos 人工界面不可扩展；Pellissier Tanon 需编辑历史；BuildingMOTIF 专家启发式仅限智能建筑域；Ahmetaj et al. ASP+最小基数启发式——**符号方法无法利用图中符号之外的词法/领域信息**（如命名模式），选不出语义最优修复。

## 方法与技术
1. **VIO 形式化**：给定合法 KG G 与 SHACL manifest S，VIO(κ_i_s, F) 把"第 i 个约束+焦点节点集"映射为一组 SPARQL add/remove 操作制造违规且正确修复已知（恢复原 G），支持系统性枚举与真值评测。
2. **抽象重写系统**：处理 shape 嵌套依赖——Rule 1 把 sh:node 类 VIO 递归展开到被依赖形状；Rule 2 处理 qualifiedMinCount（组合策略枚举子集选择）。Theorem 1：无递归 shape 时系统强规范化（必终止）。
3. **约束收集与去重**：shapes 拓扑排序 + 扩展树 DFS 收集覆盖全部约束的违规路径，删除同构重复防偏倚；每个叶节点在 G 副本上施加 SPARQL 操作生成测试用例。
4. **9 种提示策略（3×3 因子）**：Manifest 上下文 3 变体（M=整个 manifest / S=源 shape+依赖 / Sn=S+类自然语言描述）× KG 上下文 3 变体（G=整图 / F=仅焦点节点相关三元组 / F+=F+一个满足源 shape 的正例）；五段式 prompt 要求输出 INSERT/DELETE SPARQL 修复。
5. **四级阶梯指标**：语法有效（SPARQL 可解析）→ 语义有效（修复后不再违规）→ relaxed isomorphism（占位符化后与原图同构）→ exact isomorphism；逐级门控；LMM（线性混合效应模型）做统计显著性分析。

## 创新点
- **vs 临时基准（Wikidata 编辑历史、SHACL test suite）**：VIO 提供违规类型/数量/shape 覆盖高度可控生成 + 已知真值修复——首个可系统化、可扩展的 KG 修复评测框架。
- **vs 最小基数/符号启发式修复（ASP、BuildingMOTIF）**：LLM 能利用词法与领域知识区分"符号相似但语义不同"的场景，生成上下文恰当的修复。
- **vs 人工修复（Schimatos）**：自动化可规模化；LMM 统计分析方法学贡献。

## 效果
- Dataset: Brick v1.3 + ASHRAE G36（8 KG/manifest，均 35 shapes，144 用例）+ LUBM（229 shapes，70 用例）+ QUDT（81,293 triples，134 用例）| Metric: 4 LLM × 9 策略总体均分 | Result: 语法有效 **97.35%**、语义有效 **86.17%**、relaxed iso **54.07%**、exact iso **49.94%**
- **消融（上下文裁剪）**：manifest M→S 显著提升除语法外全部指标（整个 manifest "过载并分散注意力"）；S→Sn 无显著效应；G→F 提升语义有效性但损害同构类指标；F→F+ 整体提升；**S+F+ 是成本/性能最优**
- **消融（模型）**：GPT-4o ≈ Llama 3.1 405B ≈ Claude 3.0 Opus（无显著差异），Gemini 1.5 Pro 显著更差；成本推荐 GPT-4o 或 Llama
- 语义有效 ≠ 还原原图：86.17% vs 49.94% 的差距揭示"修好"与"修对"的鸿沟

## 关键引用
> "The validation report obtained after validating a KG against SHACL shapes details which constraints were violated on which KG nodes but provides limited feedback on how to repair these violations." — Section 1

> "minimal cardinality edits, or other symbolic heuristic methods like BuildingMOTIF, are not always sufficient to determine the best repair. A significant reason is that these methods cannot consider information beyond what is representable as symbols in the graph; lexical information and domain information are not available to guide the repair process." — Section 2.1

> "This suggests that providing the entire manifest (M) overloads and distracts the LLM, while focusing on essential validation information (S) leads to better repairs." — Section 7.1

## 关联
- [[ValidationFeedbackLoop]] — 本论文是该闭环的评测基准侧：SHACL 报告作为 LLM 输入信号生成 SPARQL 修复，四级指标可直接借用为修复管线验收标准
- [[OntologyConstrainedGeneration]] — VIO 思想可迁移为"自造已知答案违规"回归测试任何校验/修复工具
- [[xpshacl-explainable-validation]] — 上下游互补：xpSHACL 解释违规、本文修复违规
- [[abox-abduction-repair-semantics]] — Round 18 的 ABox 溯因修复（符号侧）与本文 LLM 修复（神经侧）构成修复谱系两端
- [[reasoner-guided-repair-owl2dl]] — 同为"校验反馈修复 LLM"，一个修查询答案、一个修 KG 数据
