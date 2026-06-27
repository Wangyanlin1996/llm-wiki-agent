---
title: "TurnValidConformalCoverage"
type: concept
tags: [conformal-prediction, multi-turn, feedback-covariate-shift, turn-valid-coverage, likelihood-ratio]
sources: [clara]
last_updated: 2026-06-23
---

# TurnValidConformalCoverage

轮次有效共形覆盖率——解决共形预测在**自适应多轮交互**中覆盖率保证失效的问题。由 [[CLARA]] 提出，首次证明共形覆盖率在**每一轮交互**后仍然成立。

## 核心问题：反馈协变量偏移

[[ConformalIntentClarification|CICC]] 式的共形预测覆盖率保证 `P(Y ∈ C) ≥ 1-α` 依赖**可交换性**（exchangeability）——校准数据和测试数据同分布。

但在多轮交互中：
1. 系统**自适应选择**问题（基于当前信念选最有信息量的问题）
2. 信念**根据用户回答更新**
3. 这改变了第 m 轮的测试分布——它依赖于系统自己的历史决策

→ 直接重用第一轮的阈值 η̂ **失去保证**。实测覆盖率漂移最多 10 个百分点。

这是**反馈协变量偏移**（feedback covariate shift）的一个实例：测试分布依赖于模型自己的过去决策。

## 解决方案：选择诱导的似然比重加权

用加权分裂共形预测（weighted split conformal）修正偏移：

```
w_m(q) ∝ ∏_{ℓ=1}^{m} π(j_ℓ | P_ℓ, q) / π̄(j_ℓ | P_ℓ)
```

- π：用户选择模型（实测的用户在面板中的选择概率）
- π̄：参考分布（均匀选择）
- 比值 = 实际选择密度 / 参考密度 = 似然比

加权分位数替代普通分位数：

```
η̂_m = inf{η : Σ w̃_m^(i) · 1[V_i ≤ η] + w̃_m^(∞) ≥ 1-α}
```

## 轮次有效覆盖率定理

**命题**：若校准对和第 m 轮测试查询以权重 w_m 加权可交换，且选择模型 π 正确指定，则对每一轮 m：

```
Pr(I_T ∈ C(q, h_m)) ≥ 1-α
```

**鲁棒性**：若 π 误指定，覆盖率损失以 `2·TV(Q_m, Q̂_m)`（总变差）为界——连续退化而非灾难性失效。

## 与单轮共形预测的关系

| 维度 | CICC（单轮） | CLARA（多轮） |
|---|---|---|
| 保证轮次 | 仅第一轮 | 每一轮 |
| 可交换性 | 标准可交换 | 加权可交换 |
| 阈值 | 固定 η̂ | 动态 η̂_m（每轮重算） |
| 额外成本 | 无 | O(n log n) 加权分位数 |
| 适用场景 | 单轮意图分类 | 多轮交互消歧 |

## 关联
- [[CLARA]] — 源论文
- [[ConformalIntentClarification]] — CICC 的单轮保证是 CLARA 多轮保证的基础
- [[handling-vague-user-input]] — 有原则澄清三剑客之一
- [[MultimodalIntentDisambiguation]] — CLARA 用视觉选择代替文本提问
