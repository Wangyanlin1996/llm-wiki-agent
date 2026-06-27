---
title: 'CLARA: Show, Don''t Ask — Generative Visual Disambiguation for Composed Image
  Retrieval with Turn-Valid Coverage'
type: source
tags:
- conformal-prediction
- visual-clarification
- multi-turn
- composed-image-retrieval
- ambiguity
- feedback-covariate-shift
- L2
date: 2026-06-17
source_file: raw/papers/clara.pdf
last_updated: 2026-06-23
arxiv_id: '2606.18992'
authors:
- Amsisan Tran
- Baogh Le
- Tuan Kiet Pham
- Sui Yang Guang
year: 2026
doi: 10.48550/arXiv.2606.18992
---
## 概要
CLARA（CLArification by Rendering Alternatives）将共形预测扩展到**多轮交互**和**视觉领域**，解决组合图像检索（CIR）中的意图歧义。核心创新两点：(1) 用**生成式视觉消歧**——展示原型图像面板让用户"选"而非"答"——代替文本提问；(2) 用**选择诱导的似然比重加权**校准，首次证明多轮交互中共形覆盖率保证在**每一轮**都成立（turn-valid coverage）。

## 覆盖的模糊层级

**覆盖 L2（多候选歧义）**。CIR 查询（参考图 + 文本修改）命名的是语料库的一个"区域"而非单张图片，多个候选图片都可能匹配用户意图。CLARA 通过视觉消歧缩小候选集。

## 核心问题：单轮共形预测在多轮交互中失效

CLARA 首次识别并解决一个关键理论问题：**[[CICC]] 式的共形覆盖率保证在交互后不再成立**。

### 反馈协变量偏移（Feedback Covariate Shift）

- 共形预测的覆盖率保证依赖**可交换性**（exchangeability）：校准数据和测试数据同分布
- 但交互中，系统**自适应选择**问题并**根据用户回答更新信念**——这改变了测试分布
- 第 m 轮的查询分布 Q_m 依赖于系统自己的历史决策（P_1, ..., P_m）
- 直接重用第一轮的阈值 η̂ 会**失去保证**，实测覆盖率漂移最多 10 个百分点

### 文本提问的两个问题

1. **低带宽**：文本 yes/no 无法传达精细视觉差异（外观、属性、视角）
2. **循环评估**：用多模态模型**预测**用户答案来选择问题 → 同一模型既问又答 → 增益可能反映模拟器而非真实用户

## 核心机制

### 1. 共形集作为校准歧义信号

用自适应预测集（APS）将信念转为覆盖率集：

- 非一致性分数：`V(q, I_T) = Σ_{I: p(I|q) ≥ p(I_T|q)} p(I|q)`（累积质量到真目标）
- 集合大小 |C| 小→查询精确；大→查询模糊
- 决策：|C| ≤ τ 时提交，否则澄清

### 2. 轮次有效覆盖率（Turn-Valid Coverage）——理论核心

用**选择诱导的似然比**重加权共形校准：

```
w_m(q) ∝ ∏_{ℓ=1}^{m} π(j_ℓ | P_ℓ, q) / π̄(j_ℓ | P_ℓ)
```

- π：用户面板选择模型（`π(j|P,q) ∝ exp(ρ · sim(I_T, G_j))`，soft-argmax）
- π̄：参考（均匀）选择
- 加权分位数：`η̂_m = inf{η : Σ w̃_m^(i) 1[V_i ≤ η] + w̃_m^(∞) ≥ 1-α}`

**命题 1（轮次有效覆盖率）**：若校准对和第 m 轮测试查询以权重 w_m 加权可交换，且选择模型 π 正确指定，则对**每一轮** m：

```
Pr(I_T ∈ C(q, h_m)) ≥ 1-α
```

若 π 误指定，覆盖率损失以 `2·TV(Q_m, Q̂_m)`（总变差）为界——连续退化而非灾难性失效。

额外用 Mondrian 分层在 4 个歧义轴上均衡覆盖率。

### 3. 生成式视觉消歧

当需要澄清时：

**模式划分**：将共形集 C 划分为 k 个模式，沿 4 个可解释歧义轴（保留/改变/视角/背景）聚类。

**生成覆盖**：最大化次模覆盖-多样性目标：

```
F(S) = Σ_{I∈C} p(I|q,h_m) · max_{G∈S} sim(I,G)  -  β · Σ_{G,G'∈S} sim(G,G')
```

贪心求解有 (1-1/e) 近似比，无需强化学习的问题选择器。

**渲染 + 吸附到语料**：用条件扩散模型为每个模式生成原型图像，但**吸附到真实语料库的 medoid**——生成图像仅用于展示，不能进入或膨胀预测集。覆盖率不受合成质量影响。

### 4. 信念更新

用户选择 j_m 后，双重更新：
- **语义更新**：将选中模式的质心加入文本侧，重新编码
- **逻辑重加权**：`p(I|q,h_m) ∝ p(I|q,h_{m-1}) · ℓ(j_m|I)`，其中 `ℓ(j_m|I) = max{ε, sim(I, G_{j_m})}`，以 ε 为底防止误选丢弃真目标

## 关键结果

| 指标 | CLARA | Naive Interactive | 文本提问最强基线 |
|---|---|---|---|
| 单轮性能 (m=0) | 与 SOTA 统计持平 | — | — |
| T3 覆盖率（边际） | 89.6% | 79.0%（漂移 10pp） | — |
| 到达目标轮数 | 最少 | — | 更多 |
| 视角/属性歧义 | 优势最大 | — | 文本无效 |

**实验设置**：α=0.1, τ=5（提交大小）, k=4（面板大小）, M=3（最大轮数）, ε=0.05, β=0.3

## 核心论点
- 共形预测的覆盖率保证在**自适应交互后不再成立**——反馈协变量偏移
- 用似然比重加权可恢复**每一轮**的覆盖率保证（turn-valid coverage）
- 视觉选择比文本提问带宽更高、更自然，且消除答案模型循环
- 生成图像必须吸附到真实语料——合成不能影响覆盖率

## 与知识库其他方法的对比

| 维度 | CLARA | [[CICC]] | SAGE-Agent |
|---|---|---|---|
| 共形预测 | 多轮（turn-valid） | 单轮 | 不用 |
| 澄清模态 | 视觉（选原型图） | 文本（选意图） | 文本（选参数值） |
| 覆盖率保证 | 每轮 1-α | 仅第一轮 1-α | 无 |
| 理论贡献 | 反馈协变量偏移修正 | 共形预测基础应用 | EVPI 结构化 |
| 领域 | 图像检索 | 意图分类 | 工具调用 |

## 关键引述
> "its coverage guarantee holds only at the first turn: once the belief is updated by an adaptively chosen question, re-applying the calibrated threshold no longer carries any guarantee, because adaptive acquisition induces feedback covariate shift."

> "CLARA reweights the conformal calibration by the selection-induced likelihood ratio, giving the first turn-valid coverage guarantee that provably holds at every committed round."

> "a generated image must never enter or inflate the prediction set"

## 关联
- [[CICC]] — CLARA 直接扩展 CICC 的共形预测方法到多轮+视觉；揭示 CICC 单轮保证的局限性
- [[ConformalIntentClarification]] — 共形意图澄清概念页，CLARA 是多轮扩展
- [[handling-vague-user-input]] — 有原则澄清三剑客之一（共形多轮/EVPI/贝叶斯）
- [[MultimodalIntentDisambiguation]] — 视觉消歧是多模态消歧的特例
- [[PP-Clarifier]] — 对比：PP-Clarifier 用多模态消歧但无统计保证，CLARA 有 turn-valid 保证
