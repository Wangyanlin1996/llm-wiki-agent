---
title: 'APEX: 动态数据选择的 Prompt 优化'
type: source
tags:
- prompt-optimization
- data-selection
- evolutionary-algorithm
sources:
- apex-dynamic-data-selection
source_file: raw/papers/apex-dynamic-data-selection.pdf
last_updated: 2026-07-09
arxiv_id: '2606.11459'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
进化算法是自动 prompt 优化的主流范式，但存在数据效率瓶颈——将开发数据集视为静态基准，在无信息数据上浪费大量计算预算。APEX 将数据使用与 prompt 搜索联合优化，根据优化历史动态将数据集分层为 Easy/Hard/Mixed 三层，优先使用 Mixed 层。

## 关键贡献
- 将数据使用与 prompt 搜索联合优化——打破"静态数据集"假设
- 根据优化历史动态分层：Easy/Hard/Mixed
- 识别两个高杠杆子集：addressable frontier 和 rank-sensitive frontier
- 在 5000 次评估调用预算下，Gemini 2.5 Flash 平均 +11.2%，Gemma 3 27B +6.8%

## 方法细节
- **动态分层**：根据当前 prompt 在每个数据点上的表现历史，将数据点分为三层：
  - Easy：当前 prompt 已正确——无信息量
  - Hard：当前 prompt 始终失败——可能不可解决
  - Mixed：当前 prompt 有时对有时错——信息量最高
- **Addressable Frontier**：Mixed 层中，prompt 变异后有潜力解决的子集——生成有信息量的变异方向
- **Rank-Sensitive Frontier**：Mixed 层中，能区分候选 prompt 质量优劣的子集——有效排序候选
- **优先采样**：将评估预算优先分配给两个 frontier 子集，避免浪费在 Easy/Hard 上

## 关键引用
> "APEX identifies two high-leverage subsets: the addressable frontier for informative mutations and the rank-sensitive frontier for discriminating candidate quality."

## 关联
- [[PromptOptimization]] — Prompt 优化方向
- [[PromptCodebooks]] — PCO 优化 prompt 结构（codebook），APEX 优化数据使用
- [[SPEAR]] — SPEAR 用代码做错误分析，APEX 用数据分层做效率优化

## 矛盾
- 与"均匀采样评估数据"的矛盾：APEX 表明动态分层采样能大幅提升效率
