---
title: 'SAGE-Agent: Structured Uncertainty guided Clarification for LLM Agents'
type: source
tags:
- clarification
- structured-uncertainty
- EVPI
- tool-calling
- LLM-agent
- ambiguity
- L2-L3
date: 2025-11-11
source_file: raw/papers/sage-agent.pdf
last_updated: 2026-06-23
arxiv_id: '2511.08798'
authors:
- Manan Suri
- Puneet Mathur
- Nedim Lipka
- Franck Dernoncourt
- Ryan A. Rossi
- Dinesh Manocha
year: 2025
doi: 10.48550/arXiv.2511.08798
---
## 概要
SAGE-Agent 用**结构化不确定度**（structured uncertainty）在工具调用参数域上直接建模，将"用户想要什么"（specification uncertainty）与"LLM 预测什么"（model uncertainty）干净分离。核心用**期望完美信息价值**（EVPI）量化每个澄清问题的消歧价值，配合基于 aspect 的冗余成本建模，实现有原则的问题选择和停止判据。附带 ClarifyBench——首个多轮动态工具调用消歧基准。

## 覆盖的模糊层级

**覆盖 L2（多候选歧义）+ L3（参数缺失/不可行）**。与 [[CICC]] 不同，SAGE-Agent 不处理 L1（意图本身未知）——它假设工具集已知，处理的是"用户想调哪个工具+参数值不确定"。但它在 L2/L3 上提供了比 CICC 更精细的结构化建模：直接在工具参数域上操作，而非在意图分类空间。

## 核心机制

### 1. 结构化信念状态（Structured Belief State）

在工具集 T = {T_1, ..., T_K} 上，每个工具 T_i 是元组 `(name_i, Θ_i, D_i, R_i)`（参数集、域、必需参数）。给定模糊查询 u，agent 维护信念分布：

```
B(t) = {(c, π_c(t)) : c ∈ C}
```

其中 C 是所有可行的工具-参数候选，π_c(t) 是候选 c 匹配用户真意图的概率。信念分解为工具选择 × 参数值：

```
p(T_c, θ_c | u, r_1:t) = p(θ_c | T_c, u, r_1:t) · p(T_c | u)
```

假设参数条件独立：`π_c(t) ∝ ∏_j p(θ_{c,j} | T_c, u, r_1:t)`

- 已指定参数：p(θ) = 1
- 未指定离散参数：p(θ) = |D|^{-1}（均匀）
- 未指定连续参数：p(θ) = ε（极小值）

**信念更新**：用户回答 r_t 后，参数域做交集更新：`D_θ(t+1) = D_θ(t) ∩ Update(θ, r_t, q_t)`，然后重新归一化。

### 2. EVPI 问题选择（信息论核心）

**期望完美信息价值**：

```
EVPI(q, B(t)) = E_r[max_c π_c(t|q,r)] - max_c π_c(t)
```

含义：问问题 q 后，最佳候选的确信度期望提升多少。

**冗余成本**（防止重复问同一参数）：

```
Cost(q,t) = λ · Σ_{a ∈ A(q)} n_a(t)
```

其中 aspect a = (T_i, θ_j) 是工具 i 的参数 j，n_a(t) 是该 aspect 已被问过的次数。

**问题选择与停止**：

```
q*(t) = argmax_q [EVPI(q, B(t)) - Cost(q,t)]
```

停止条件：当 `max_q Score(q,t) < α · max_c π_c(t)` 时执行最佳候选（问问题不值得了）。

### 3. SAGE-Agent 五步算法

1. **候选生成**：LLM 生成候选工具调用 C_t，参数可为 `<UNK>`。若 `max π_c ≥ τ_exec`，直接执行
2. **问题生成**：LLM 生成候选问题集 Q_t，每个问题关联目标候选和 aspects
3. **问题评分与选择**：计算 EVPI（模拟完美消解），减去冗余成本，选最高分问题。若净增益不足则执行
4. **信念更新**：用户回答后，更新参数域（交集），重算 π_c，递增 aspect 计数
5. **终止与错误恢复**：三种终止条件（置信度够/问题不值得/达最大步数）。执行失败时生成纠正调用或错误特定问题

### 4. 不确定度引导的奖励建模（训练信号）

不仅推理时用，还作为训练信号。用 GRPO 微调，奖励设计：

```
R_category(a_t) = Cert(a_t) · r_base(a_t)
```

- 工具调用时 `Cert = max_c π_c(t)`（高置信→全奖励，低置信→惩罚）
- 问问题时 `Cert = 1 - max_c π_c(t)`（高不确定→奖励提问）
- 其他动作 `Cert = 1`

**自校准**：无需 critic 判断问题质量，奖励随信念状态自适应。

## ClarifyBench 基准

| 维度 | 详情 |
|---|---|
| 总样本 | 716（5 域：文档/车辆/股票/旅行/文件系统） |
| 工具数 | 92 |
| 查询类型 | Explicit(241) / Ambiguous(213) / Infeasible(198) |
| 特色 | 首个支持**多轮动态用户模拟** + **三类查询** + **不可行检测**的工具调用消歧基准 |
| 数据来源 | DocPilot（真实文档交互）+ BFCL-v3（多域工具调用） |
| 人工验证 | Cohen's κ = 0.76 |

与现有基准对比：AgentBoard/τ-bench/MMAU/ToolSandbox/BFCL-v3 均缺少"模糊+不可行+动态模拟"的完整组合。

## 关键结果

| 指标 | SAGE-Agent | 最强基线 | 提升 |
|---|---|---|---|
| Ambiguous Coverage (GPT-4o) | 59.73% | Domain-aware ReAct 55.70% | +4.03pp |
| Ambiguous Avg #Q | 1.39 | ReAct 2.68 | -48.1% |
| Infeasible Coverage | 67.33% | Domain-aware ReAct 63.21% | +4.12pp |
| When2Call (3B) | 65.2% | baseline 36.5% | +28.7pp |
| When2Call (7B) | 62.9% | baseline 36.7% | +26.2pp |

**超参数**：λ=0.5（冗余惩罚），α=0.1（停止系数），ε=10^-4（连续域），τ_exec（执行阈值）

## 核心论点
- 不确定度应在**结构化工具参数域**上建模，而非非结构化语言空间
- EVPI 提供有原则的问题选择判据（信息增益 vs 冗余成本）
- 结构化不确定度既可用于推理时问题选择，也可作为训练信号
- 现有方法（prompting/uncertainty-based）缺乏"问什么"和"何时停"的原则性判据

## 与知识库其他方法的对比

| 维度     | SAGE-Agent    | [[CICC]]     | [[AskBeforePlan]]       | Active Task Disambiguation |
| ------ | ------------- | ------------ | ----------------------- | -------------------------- |
| 不确定度空间 | 工具参数域         | 意图分类 softmax | 对话+环境观察                 | 解空间熵                       |
| 问题选择原则 | EVPI - 冗余成本   | 预测集大小        | 拓扑排序                    | 信息增益                       |
| 停止判据   | 净增益 < α·max π | 预测集收敛        | 所有 indefinite recovered | 信息增益低于阈值                   |
| 统计保证   | 无（EVPI 是期望值）  | 覆盖率 1-α      | 无                       | 无                          |
| 多轮     | 是             | 单轮           | 是                       | 是                          |
| 训练信号   | 是（GRPO 奖励）    | 否            | 是（trajectory tuning）    | 否                          |
| 不可行检测  | 是             | 否（OOS 是另一回事） | 是                       | 否                          |

## 关键引述
> "We introduce a principled formulation of structured uncertainty that operates directly over tool parameters and their domains, cleanly separating specification uncertainty (what the user wants) from model uncertainty (what the LLM predicts)."

> "Our formulation uses Expected Value of Perfect Information (EVPI) to quantify the disambiguation value of each potential question, balanced against aspect-based cost modeling that prevents redundant questioning."

## 关联
- [[CICC]] — 对比：CICC 用共形预测（覆盖率保证）vs SAGE-Agent 用 EVPI（期望信息价值）；CICC 在意图空间 vs SAGE-Agent 在参数域
- [[AskBeforePlan]] — 对比：Ask-before-Plan 用拓扑排序 vs SAGE-Agent 用 EVPI；都处理 L3 但 SAGE-Agent 更结构化
- [[handling-vague-user-input]] — 有原则澄清三剑客之一（共形/EVPI/贝叶斯实验设计）
- [[IntentSignalTheory]] — specification uncertainty 对应 IST 中的 I* 缺失
- [[ActiveTaskDisambiguation]] — SAGE-Agent 的基线之一，用贝叶斯实验设计
