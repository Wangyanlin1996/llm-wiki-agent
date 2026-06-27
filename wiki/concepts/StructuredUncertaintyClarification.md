---
title: "StructuredUncertaintyClarification"
type: concept
tags: [structured-uncertainty, EVPI, tool-calling, clarification, Bayesian-decision-theory]
sources: [sage-agent]
last_updated: 2026-06-23
---

# StructuredUncertaintyClarification

结构化不确定度澄清——在**工具参数域**上直接建模不确定度，用**期望完美信息价值**（EVPI）量化每个澄清问题的消歧价值，配合冗余成本建模实现有原则的问题选择与停止。由 [[SAGE-Agent]] 提出。

## 核心思想

传统澄清方法在非结构化语言空间操作——用 prompting 生成文本问题，缺乏"问什么"和"何时停"的原则性判据。结构化不确定度澄清转而在工具参数域上建模：

1. **信念状态**：维护 `B(t) = {(c, π_c(t))}` ——每个候选工具调用 c 的匹配概率
2. **信念分解**：`p(T_c, θ_c | u, r) = p(θ_c | T_c, u, r) · p(T_c | u)` ——工具选择 × 参数值
3. **参数条件独立**：`π_c ∝ ∏_j p(θ_{c,j})` ——已指定=1，未指定离散=|D|^{-1}，未指定连续=ε

## EVPI 问题选择

```
EVPI(q, B(t)) = E_r[max_c π_c(t|q,r)] - max_c π_c(t)
```

问问题 q 后最佳候选确信度的期望提升。配合冗余成本：

```
Score(q,t) = EVPI(q) - λ · Σ_{a∈A(q)} n_a(t)
q*(t) = argmax_q Score(q,t)
```

停止：`max_q Score < α · max_c π_c(t)`（问问题不值得了）

## 规格不确定度 vs 模型不确定度

关键分离：
- **规格不确定度**（specification uncertainty）：用户想要什么——参数未指定/模糊
- **模型不确定度**（model uncertainty）：LLM 预测什么——能力限制

传统方法混二者；结构化方法在参数域上显式分离。

## 与其他有原则澄清方法的关系

| 方法 | 理论框架 | 不确定度空间 | 保证 |
|---|---|---|---|
| [[ConformalIntentClarification]] | 共形预测 | 意图分类 softmax | 覆盖率 1-α |
| StructuredUncertaintyClarification | EVPI（贝叶斯决策论） | 工具参数域 | 无（期望值） |
| [[BayesianDisambiguation]] | 贝叶斯实验设计 | 解空间 | 无（信息增益） |

三者构成"有原则澄清"谱系：共形预测给覆盖率保证，EVPI 给期望信息价值，贝叶斯实验设计给信息增益。

## 关联
- [[SAGE-Agent]] — 源论文
- [[ConformalIntentClarification]] — 对比：共形预测在意图空间 vs EVPI 在参数域
- [[BayesianDisambiguation]] — 对比：信息增益在解空间 vs EVPI 在参数域
- [[AskBeforePlan]] — 对比：拓扑排序 vs EVPI
- [[handling-vague-user-input]] — 有原则澄清三剑客之一
