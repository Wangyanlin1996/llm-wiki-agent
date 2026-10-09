---
title: "Seminaïve Materialisation in DatalogMTL（DatalogMTL 半朴素物化）"
type: source
tags: [ontology-reasoning, reasoning-engine, temporal-reasoning]
sources: [datalogmtl-seminaive-materialisation]
source_file: raw/papers/datalogmtl-seminaive-materialisation.pdf
last_updated: 2026-10-09
arxiv_id: "2208.07100"
authors: ["Dingmin Wang", "Przemysław Andrzej Wałęga", "Bernardo Cuenca Grau"]
year: 2022
venue: "RuleML+RR 2022"
citation_count: 1
---

## 概要

本文为 DatalogMTL（Datalog 扩展度量时序逻辑算子、在时序本体数据访问与流推理中广泛应用）提出**半朴素（seminaïve）物化**过程：类比经典 Datalog 的 seminaïve 算法，确保每个时序规则实例在整个执行期间至多被考虑一次，消除冗余计算。由于 DatalogMTL 中派生事实可与已有事实合并（coalescing）且规则体含度量原子，"新信息追踪与相关规则实例识别"比 Datalog 复杂得多；论文给出优雅的克服方案，并针对满足特定句法限制的程序提出进一步优化。实现作为 MeTeoR 推理器的扩展，实验显示显著降低物化时间与内存。

## 解决的问题

DatalogMTL 物化式推理（MeTeoR 等）采用朴素评估策略，冗余计算是低效主源：同一规则实例（尤其涉及重叠区间的时序事实）在多轮物化中被反复应用，且不断重新派生已被合并过的旧事实。朴素策略下随物化轮次递增的冗余使大型时序数据集上的推理难以扩展。半朴素策略在经典 Datalog 中成熟，但直接提升到 DatalogMTL 需处理三个难点：度量原子、coalescing 后的"新事实"追踪、区间交叠下的规则实例相关性判定。

## 方法与技术

1. **增量集合 Δ 维护**：每轮物化步骤记录新派生事实集 Δ（初始为输入数据集），下一轮仅应用"至少涉及一个 Δ 中事实"的规则实例——保证非重复性（non-repetition property）。
2. **语义差集定义**：`instr[D···Δ]` 形式化"相对 Δ 的相关实例"——某合取体 Mi 不能由 D\Δ 单独蕴含即为相关；`D1⧸D2` 定义数据集语义差集，用于判定合并后的事实是否为真新。
3. **coalescing 语义整合**：每轮规则应用后先合并相邻/交叠区间（coalescing），再把合并结果纳入 Δ——避免 Datalog 朴素式"只看原始新事实"遗漏合并产生的新信息。
4. **优化版（Procedure 3）**：非递归谓词物化完成后立即丢弃非递归规则；对前向传播程序利用"非递归体原子最大右端点 tr"判定规则何时可安全丢弃，最小化后续冗余。
5. **正确性**：证明半朴素过程与朴素过程在每 k 轮后表示相同解释 T^k_Π(ID)（soundness + completeness），优化版同样满足。

## 创新点

- 首次将经典 Datalog 的 seminaïve 求值策略系统性提升到含度量时序算子的 DatalogMTL，解决区间合并与语义差集追踪难题——非平凡泛化而非简单套用。
- 提出针对 forward-propagating 程序的时序感知规则丢弃优化：利用非递归体原子的最晚出现时间点判定规则失效，这在经典 Datalog 无对应物。
- 无缝嵌入既有 MeTeoR 推理器（既可独立用于有限可物化片段，也可与 Büchi 自动机结合处理一般情形）。

## 效果

- 数据集：LUBM 时序扩展（56 条 Datalog 规则 + 29 条递归时序规则），9 个各 10M 事实、常数数递增（0.8M–15.8M）的数据集。
- 相对朴素策略：seminaïve 在时间与内存上显著优于朴素，随物化推进差距扩大；优化版在第 9 轮开始丢弃规则后进一步超越 seminaïve。
- 常数数扩展测试：朴素策略时间/内存随常数数近似线性增长，两种 seminaïve 程序受影响很小（能快速丢弃无关实例）。
- 硬件：Dell PowerEdge R730，512GB RAM，2×Xeon E5-2640。

## 关键引用

> "Lifting the seminaïve strategy to DatalogMTL involves significant technical challenges. In particular, rule bodies now involve metric atoms, and derived temporal facts can be coalesced with existing facts in the previous partial materialisation." — Section 1, Introduction

> "the seminaïve procedure significantly outperforms the naïve approach both in terms of running time and memory consumption, especially as materialisation progresses." — Section 6, Evaluation

## 关联

- [[OntologyReasoning]] — 物化/前向链式推理是本体推理器（VLog、RDFox 等）的核心引擎技术，本文将其扩展到时序本体。
- [[meteror-metric-temporal-reasoning]] — 直接前身与宿主：MeTeoR 实现朴素物化+自动机混合，本文为其提供高效的半朴素物化内核。
- [[datalog-first-class-facts]] — 同为 Datalog 系推理引擎；Slog 关注通信避免的并行 Datalog，本文关注时序算子的冗余消除。
- [[OntologyGraphRetrieval]] — 时序物化支撑本体图上的时间感知检索（流推理）。
