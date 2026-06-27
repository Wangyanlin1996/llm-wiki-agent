---
title: Uncertainty Decomposition for Clarification Seeking in LLM Agents
type: source
tags:
- uncertainty-decomposition
- clarification
- prompt-based
- action-confidence
- request-uncertainty
- LLM-agent
- L2-L3
date: 2026-06-17
source_file: raw/papers/uncertainty-decomposition-clarification.pdf
last_updated: 2026-06-25
arxiv_id: '2606.19559'
authors:
- Gregory Matsnev
year: 2026
doi: 10.48550/arXiv.2606.19559
---
## 概要

Matsnev (2026) 提出**prompt-based 不确定度分解**，将单一置信度标量拆分为**行动置信度**（action confidence `c_t`）和**请求不确定度**（request uncertainty `u_t`），使 LLM agent 能在任务规格模糊时主动请求澄清。核心洞察：**单一置信度标量混淆了两种本质不同的不确定度**——"行动难选"（应谨慎执行）vs "请求模糊"（应问用户）。方法**纯 prompt 驱动，无需训练，兼容黑箱 API**，在两个新建的澄清增强基准上 F1 大幅领先。

## 覆盖的模糊层级

**覆盖 L2（多候选歧义）+ L3（参数/细节缺失）**。`u_t` 捕捉的是"用户目标是否被完整规格化"——当任务缺少关键细节（L3）或存在多种合理解读（L2）时，`u_t` 升高触发澄清。不处理 L1（意图本身未知）——假设 agent 有明确的行动空间，处理的是规格不足。

## 核心机制

### 1. 不确定度分解（核心创新）

**问题**：现有 prompt-based 方法（ReAct+UE、UAM）让 agent 输出单一置信度标量 `c_t`，混淆了两种本质不同的不确定度：

| 不确定度来源 | 含义                       | 正确响应       |
| ------ | ------------------------ | ---------- |
| 行动难选   | 多个相似产品可选，不确定选哪个          | 谨慎执行（继续推理） |
| 请求模糊   | "find me a shirt"未指定颜色尺码 | **请求用户澄清** |

**解法**：分解为两个语义独立的信号：

- **Action confidence `c_t`** ∈ [0,1]：agent 对所选行动推动任务完成的置信度
- **Request uncertainty `u_t`** ∈ [0,1]：用户目标是否被完整规格化（0=完整，1=关键细节缺失）

**澄清触发**：`if u_t ≥ θ: request_clarification else: execute a_t`

θ=0.5 为默认阈值（敏感性分析显示 θ=0.25 略优但差异 ≤0.03 F1）。

### 2. 历史传播（继承 UAM）

与 ReAct+UE（不确定度不写回历史）不同，本方法将 `(u_t, c_t, 解释)` 全部写回 agent 历史 `H_{t+1}`，允许后续步骤推理累积不确定度——这与 UAM 的"语义传播"策略一致，但传播的是**双信号**而非单标量。

### 3. 输出字段顺序

关键实现细节：agent 先输出 `u_t`（及解释），再输出 `a_t` 和 `c_t`。这确保**在承诺行动前先评估规格完整性**，给 agent 一个专用通道处理目标模糊性——单一置信度无法提供此通道。

### 4. 轨迹级聚合（四种策略）

| 聚合 | 公式 | 特点 |
|---|---|---|
| last | `S = s_T` | 仅最后一步 |
| avg | `S = mean(s_1...s_T)` | 均值 |
| max | `S = max(s_1...s_T)` | 峰值 |
| product | `S = ∏ s_t` | 几何均值（"幻觉螺旋"形式化） |

**重要发现**：product 聚合在 ALFWorld 上达到最高 ROC-AUC，但这是**轨迹长度混淆**——失败任务更长，几何均值随 T 递减，用随机 U(0,1) 替换真实置信度也能达到同等 ROC-AUC（0.92-0.99）。product 聚合不是"好信号"，而是"长度代理"。

## 评估基准

### 新建：澄清增强基准

| 基准 | 基础 | 模糊比例 | 评估目标 |
|---|---|---|---|
| WebShop-Clarification | WebShop | 50% 任务故意模糊 | 澄清 F1（二分类：是否请求澄清） |
| ALFWorld-Clarification | ALFWorld | 50% 任务故意模糊 | 同上 |

### 标准：故障检测基准

| 基准 | 评估目标 |
|---|---|
| WebShop / ALFWorld / REAL | 用不确定度信号预测轨迹是否失败（ROC-AUC/ECE/Brier） |

### LLM 后端（5 个）

GPT-5.1, DeepSeek-v3.2-exp, GLM-4.7, Qwen3.5-35B, GPT-OSS-120B

## 关键结果

### 澄清寻求（核心指标）

| 指标 | Proposed | ReAct+UE | UAM |
|---|---|---|---|
| ALFWorld-Clar. F1（5 后端均值） | **最高** | 基线 | 中间 |
| vs ReAct+UE | — | — | **+73%** |
| vs UAM | — | — | **+36%** |
| WebShop-Clar. F1 | **每个后端均领先** | — | — |
| ALFWorld-Clar. F1 | **5 个后端中 4 个领先** | — | — |

### 故障检测（标准指标）

分解方法**不牺牲**传统故障检测能力：在 WebShop 和 REAL 上达到最高 last/avg 聚合 ROC-AUC，在 ALFWorld 上与最佳差距 <0.08。

### 能力稀释（副作用）

| 方法 | 平均成功率（5 基准 × 5 后端） |
|---|---|
| ReAct+UE | 28.6% |
| UAM | 27.8% |
| Proposed | 27.0% |

更多不确定度仪表化 → 成功率单调下降 1.6pp。原因：prompt 更长更复杂 → 分散模型注意力。

### 校准（系统性问题）

所有方法、所有基准、所有后端的可靠性图均**低于对角线**——预测置信度系统性高于实际成功率。ECE 范围 0.24-0.66。这是 prompt-based 自报告置信度的**结构性偏差**：agent 已承诺行动后有"自我合理化"倾向。

### 阈值敏感性

| θ | WebShop-Clar. F1 | ALFWorld-Clar. F1 |
|---|---|---|
| 0.25 | 0.464 | 0.71 |
| 0.5（默认） | 0.455 | 0.68 |
| 0.75 | 0.291 | 0.50 |

θ=0.25 最优但与 θ=0.5 差异 ≤0.03；θ=0.75 严重损害召回。无单一 θ 在所有 (模型, 基准) 对上占优。

## 核心论点

- **不确定度分解是澄清寻求的关键前提**：单一标量无法区分"行动难"和"请求模糊"
- **prompt-based 是黑箱 API 部署的唯一可行方案**：logprob/多采样/训练方法均不可用
- **分解的收益在澄清 F1 上显著，但伴随能力稀释代价**：prompt 复杂化降低原始任务成功率
- **prompt-based 置信度系统性过度自信**：需要后校准或原生不确定度估计
- **product 聚合是轨迹长度代理而非信号质量指标**：高 product ROC-AUC ≠ 好置信度

## 与知识库其他方法的对比

| 维度 | Uncertainty Decomp. | [[SAGE-Agent]] | [[CICC]] | [[ClarifyWhenNecessary]] |
|---|---|---|---|---|
| 不确定度形式 | 双信号 (u_t, c_t) | 结构化参数域信念 | 预测集大小 | intent-sim 熵 |
| 分解规格/模型不确定度 | **是**（u_t vs c_t） | **是**（规格 vs 模型） | 否 | 否 |
| 实现方式 | 纯 prompt | prompt + GRPO 训练 | 后处理（校准集） | 后处理（意图聚类） |
| 需要训练 | **否** | 是（可选） | 否 | 否 |
| 黑箱 API 兼容 | **是** | 是（推理时） | 是 | 是 |
| 统计保证 | 无 | 无 | 覆盖率 1-α | 无 |
| 澄清判据 | u_t ≥ θ | EVPI 净增益 > α·max π | 预测集大小 > 1 | intent-sim 熵 > 阈值 |
| 基准 | WebShop-Clar./ALFWorld-Clar. | ClarifyBench | 7 个意图数据集 | QA/MT/NLI |
| 年份 | 2026 | 2025 | 2024 | 2023 |

**与 [[SAGE-Agent]] 的关系**：两者都分离"规格不确定度"和"模型不确定度"，但实现完全不同——SAGE-Agent 在结构化工具参数域上显式建模信念状态并用 EVPI 计算，本方法仅用 prompt 让 LLM 自报告两个标量。SAGE-Agent 更精确但需要工具 schema；本方法更通用但依赖 LLM 自我评估能力（受过度自信影响）。

**与 [[ClarifyWhenNecessary]] 的关系**：两者都在"when"子任务上做文章。intent-sim 在意图空间估计熵，本方法直接让 LLM 输出 u_t。intent-sim 有理论基础但需要意图聚类；u_t 更直接但依赖 LLM 自评质量。

## 关键引述

> "An agent may report low confidence because the action is difficult (e.g., many similar products to choose from) or because the user request is ambiguous (e.g., 'find me a shirt' without specifying color or size). These two situations call for different responses: the former suggests the agent should proceed cautiously, while the latter suggests it should ask the user for clarification."

> "Practical deployment constraints—black-box APIs, interactive latency budgets, and the absence of labeled trajectories—rule out logprob-based, multi-sampling, and training-based methods, leaving prompt-based estimation as the most viable family."

> "We call this effect capability dilution: more uncertainty instrumentation → lower task success rate."

> "Product aggregation does not capture the 'Spiral of Hallucination' mechanism but instead behaves as a trajectory-length proxy: replacing real confidences with i.i.d. U(0,1) draws matches or exceeds the real-product ROC-AUC."

## 关联

- [[SAGE-Agent]] — 同为"分离规格/模型不确定度"，但 SAGE-Agent 在参数域显式建模 + EVPI，本方法纯 prompt 自报告
- [[ClarifyWhenNecessary]] — 同为"when to clarify"子任务，但 intent-sim 用意图聚类熵 vs 本方法用 LLM 自评 u_t
- [[CICC]] — 同属"有原则澄清"谱系，CICC 有统计保证而本方法无
- [[handling-vague-user-input]] — prompt-based 澄清的实践派代表，L2-L3 覆盖
- [[IntentSignalTheory]] — u_t 对应 IST 中 I* 规格完整性的不确定度
- [[PromptBasedUncertaintyDecomposition]] — 本文提出的核心方法概念页
- [[NeuralEVPI]] — EVPI 谱系起点；本方法不走 EVPI 路线但同样关注"何时澄清值得"
