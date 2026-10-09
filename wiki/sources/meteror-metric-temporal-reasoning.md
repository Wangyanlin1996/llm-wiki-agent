---
title: "MeTeoR: Practical Reasoning in Datalog with Metric Temporal Operators（MeTeoR 时序本体推理器）"
type: source
tags: [ontology-reasoning, reasoning-engine, temporal-reasoning]
sources: [meteror-metric-temporal-reasoning]
source_file: raw/papers/meteror-metric-temporal-reasoning.pdf
last_updated: 2026-10-09
arxiv_id: "2201.04596"
authors: ["Dingmin Wang", "Pan Hu", "Przemysław Andrzej Wałęga", "Bernardo Cuenca Grau"]
year: 2022
venue: "AAAI 2022"
citation_count: 41
---

## 概要

MeTeoR 是**首个覆盖完整 DatalogMTL 语言的实际推理算法与可扩展实现**。DatalogMTL（Datalog + 度量时序逻辑算子）因 ExpSpace 完备（数据量 PSpace 完备）的高计算复杂度，长期无实用推理器——Brandt et al. (2018) 的原型仅限非递归程序。MeTeoR 将**物化（materialisation/前向链式）与基于 Büchi 自动机的方法**结合：物化可扩展但可能不终止，自动机完备但自动机构造指数规模。算法通过优化物化、优化自动机构建，以及仅在必要时使用自动机的两线程并行组合，实现"两者优点的结合"。在 LUBM 时序扩展与真实气象数据集（3.97 亿事实）上验证可扩展到千万级时序事实。

## 解决的问题

DatalogMTL 强大的表达力（时序 OBQA、流推理）与其 ExpSpace 高复杂度冲突，导致推理实现困难、阻碍应用采纳。直接物化面临两个难题：解释本质上无穷（需有限表示每轮结果）、达到最小不动点可能需要无穷多轮（非递归才保证终止）。自动机决策过程虽终止但有指数状态规模、不实用。Brandt et al. 的非递归原型之外，"完整 DatalogMTL 语言的实用推理算法"此前是空白。

## 方法与技术

1. **数据集表示与索引**：每个 ground 关系原子关联按左端点排序的区间列表；复合键（谓词+常量元组）索引加速蕴含检查与 fact coalescing；按项参数额外索引支持连接。
2. **优化物化（ApplyRules）**：基于索引的 index nested loop join 完成规则 grounding；将 Brandt 的规范化完成规则推广到任意 DatalogMTL 规则（避免归一化预处理的辅助谓词开销）；sort-merge join 计算度量原子的区间交叠。
3. **优化自动机推理**：只对"相关"事实子集 D′（提及规则体谓词的事实）做一致性检查，缩小自动机；利用 MTL 算子语义（如 ⊞[0,∞)P 需在后续所有时点成立）约束状态构造搜索空间。
4. **混合决策过程（Algorithm 2）**：先检查 D 直接蕴含；按依赖图取 P 相关规则 Π_P；非递归则纯物化判定；递归则先"预物化"到所有非递归谓词派生完毕，再并行两线程——物化 best-effort 与 EntailToInconsist+自动机（用预物化数据集 D_pre 优化非空测试）竞速，先出结果者胜。
5. **正确性**：Algorithm 2 可证 sound & complete。

## 创新点

- **首个支持任意（含递归）DatalogMTL 程序的实际推理器**，超越 Brandt et al. 仅非递归的原型。
- 物化-自动机混合的工程范式：用"相关规则集 + 预物化 + 并行竞速"最小化自动机使用，使多数蕴含测试走物化快速路径。
- 实证证明 99.2% 输入事实可走物化路径（T1–T4 类），仅 0.8% 需自动机——为"自动机实际很少触发"的实用假设提供数据。

## 效果

- **LUBM 时序基准**（56 条 OWL2 RL Datalog 规则 + 29 条递归时序规则 = 85 条程序）：5/10/15/20M 事实数据集上，T1 类事实 <3s，T2–T4 数百秒，T5（需自动机）7.6min–172.6min；1,000 随机事实分布 T1 46.0% / T2 28.3% / T3 16.6% / T4 8.3% / T5 0.8%。
- **压力测试（1b）**：支持至 **1.5 亿时序事实**（T2/T3/T4 类）。
- **与 Brandt 基线对比（2a/2b）**：全数据集一致胜出——LUBM D1 3 条程序 160.3→51.3s / 345.9→146.8s / 523.9→213.4s；气象全 62 年（3.97 亿事实）程序1 2234.0→1050.8s。
- **2c 时序连接压力测试**：基线随每原子事实数增长快速退化，MeTeoR 保持稳定——验证专用时序连接算法需求。
- 硬件：Dell PowerEdge R730，512GB RAM，2×Xeon E5-2640 2.6GHz。

## 关键引用

> "Our new algorithm deals with these difficulties by providing an effective way of combining the scalability of materialisation-based reasoning and the completeness guaranteed by automata-based procedures, thus bringing together 'the best of both worlds'." — Section 1, Introduction

> "We found that in 46.0% cases the facts were of type T1, 28.3% of type T2, 16.6% of type T3, 8.3% of type T4, and only 0.8% of type T5. This supports our hypothesis that input facts requiring the use of automata may rarely occur in practice." — Section 6, Experiment 1a

> "We see these results as empirical validation for the need of specialised temporal join algorithms, which are not provided off-the-shelf by SQL engines." — Section 6, Experiment 2c

## 关联

- [[OntologyReasoning]] — 时序本体推理（DatalogMTL）是本概念页"查询回答"维度的延伸：OBQA + 流推理。
- [[datalogmtl-seminaive-materialisation]] — 姊妹论文为其提供 seminaïve 物化内核，消除朴素策略的冗余计算。
- [[datalog-first-class-facts]] — 同为 Datalog 系并行推理引擎；MeTeoR 主打时序算子完备性，Slog 主打结构化数据的通信避免并行。
- [[closed-loop-explainability-telecom-autonomous-networks]] — 时序推理支撑电信告警/网络流异常检测场景，与 5G 自智网络闭环呼应。
