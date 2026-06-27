---
title: 'CICC: Conformal Intent Classification and Clarification'
type: source
tags:
- intent-clarification
- conformal-prediction
- OOS-detection
- uncertainty
- L1-unknown-intent
date: 2024-03-28
source_file: raw/papers/cicc.pdf
last_updated: 2026-06-23
arxiv_id: '2403.18973'
authors:
- Floris den Hengst
- Ralf Wolter
- Patrick Altmeyer
year: 2024
citation_count: 6
doi: 10.48550/arXiv.2403.18973
---
## 概要
CICC（Conformal Intent Classification and Clarification）将任意意图分类器的启发式不确定度分数转为**有保证的澄清问题**——用 conformal prediction 构造预测集，保证真意图以用户指定的概率落在候选集内。不需要重新训练模型，生成的澄清问题小而精准，同时具备 out-of-scope 检测能力。

## 覆盖的模糊层级

**覆盖 L1（意图本身未知）+ L2（多候选歧义）**。这是知识库中首个能处理"意图本身不确定"的方法：当分类器不确定时，它不是静默选一个（如 [[NOEM³A]]），也不是只问参数（如 [[AskBeforePlan]]），而是**生成一个包含候选意图的澄清问题**，缩小意图范围。

## 核心机制

1. **Conformal Prediction 构造预测集**：将任意分类器的不确定度转为预测集 S(x)，保证 P(true_intent ∈ S(x)) ≥ 1-α（用户指定 α）
2. **澄清问题生成**：当 |S(x)| > 1 时，生成一个澄清问题让用户在候选集中选择
3. **OOS 检测**：当 S(x) = ∅ 时，判定为 out-of-scope（输入不属于任何已知意图）

## 预训练分类器的使用方式

**核心原则：分类器是 CICC 的输入，不是 CICC 训练的。** CICC 把分类器当黑箱，只读其 softmax/置信度输出，不重训、不微调、不改参数。

### 整体数据流

```
用户输入 X
    ↓
[预训练分类器 f̂]  ← CICC 不碰，只调用
    ↓
softmax 输出 f̂(X) = [p_1, ..., p_K]
    ↓
[共形预测]  ← CICC 核心：校准集 + 分类器输出 → 预测集
    ↓
预测集 C(X) = {y : 1 - f̂(X)_y ≤ q̂}
    ↓
[三分支决策] |C|=1 执行 / 1<|C|≤th 问用户 / |C|>th 拒绝
```

### 分类器在三个地方被使用

**1. 校准阶段——建立基准线 q̂**

在校准集 `D = {(X_i, Y_i)}`（有标准答案，size n）上：
- 调用分类器得到 `f̂(X_i)` = K 维 softmax 向量
- 取真类的分数 `f̂(X_i)_{Y_i}`
- 算非一致性分数 `s(X_i) = 1 - f̂(X_i)_{Y_i}`（真类分数越低→分数越高→越"不一致"）
- 对 n 个校准样本取经验分位数 `q̂`，使得 (1-α) 比例的 s ≤ q̂

**2. 测试阶段——构造预测集**

对新输入 `X_t`：
- 调用分类器得到 `f̂(X_t)` = K 维 softmax 向量
- 对每个候选意图 y，算 `s(X_t, y) = 1 - f̂(X_t)_y`
- 所有 `s(X_t, y) ≤ q̂` 的 y 进入预测集 `C(X_t)`

**3. 全程只读——不重训**

论文 §3.1 明确："does not require any retraining of the underlying model"。分类器一旦预训练完成，CICC 只读其 softmax 输出。

### 实验中使用的具体分类器

| 分类器 | 数据集 | 输出形式 |
|---|---|---|
| fine-tuned BERT（Devlin et al. 2019） | ACID, ATIS, B77, C150-IS, HWU64, MTOD | 标准 softmax |
| custom BERT-like 模型（Alfieri et al. 2022） | IND（荷兰语银行） | softmax |
| DialogflowCX (DFCX)（Google 商业 API） | B77 | top-5 的 [0,100] 启发式分数 |

### 各分类器的分数提取方式

**BERT / custom 模型**：直接取 softmax 层输出，非一致性分数 `s(X, y) = 1 - softmax(X)_y`。

**DFCX（商业 API）——特殊处理**：
- DFCX 只输出 top-5 意图的 [0,100] 分数（非 softmax）
- 归一化：除以总和转成 [0,1] 概率，其余 K-5 个意图分数设为 0
- 非一致性分数：`s(X, y) = 1 - 归一化分数_y`
- 因只输出 top-5 非零分数，th 设为 4 而非默认 7（Miller's Law）

### 分类器无关性（可插拔）——工程优势

CICC 对分类器的要求极低，唯一要求是"能给出每个意图的置信度分数"。不关心架构（BERT/SVM/商业 API）、训练方式（微调/零样本/prompt）、输出形式（softmax/启发式分数）。

这意味着：
- 已部署的分类器**不用改**，直接套 CICC
- 换分类器只需重新跑校准（算 q̂），不用重训
- 与 [[NOEM³A]]（需 logit 访问 + 重训分类头）、[[AskBeforePlan]]（需 trajectory tuning 微调）形成鲜明对比

## 核心论点
- 任意意图分类器的不确定度都可转为有保证的澄清问题，无需重训
- Conformal prediction 提供**覆盖率保证**（coverage guarantee），区别于启发式阈值
- 澄清问题应小而精准，而非开放式提问
- 同时支持 OOS 检测（预测集为空 = 未知意图）

## 关键引述
> "turns heuristic uncertainty scores of any intent classifier into a clarification question that is guaranteed to contain the true intent with a user-specified probability"

> "does not require re-training of this model, generates small clarification questions, and is capable of out-of-scope detection"

## 与知识库其他方法的区别

| 维度 | CICC | [[NOEM³A]] | [[AskBeforePlan]] |
|---|---|---|---|
| 模糊层级 | L1 + L2 | L2 | L3 |
| 不确定时行为 | 生成澄清问题缩小范围 | 静默选一个 | 问参数（不问意图） |
| 保证 | 覆盖率保证（1-α） | 无 | 无 |
| OOS 检测 | 是（预测集为空） | 否（θ=0.65 过滤但非 OOS） | 否 |
| 需重训 | 否 | 是（分类头） | 是（trajectory tuning） |

## 关联
- [[IntentUnderstanding]] — CICC 是意图理解中的不确定度处理方法
- [[handling-vague-user-input]] — 覆盖 L1+L2，填补 NOEM³A 和 Ask-before-Plan 之间的空白
- [[NOEM³A]] — 对比：NOEM³A 静默猜 vs CICC 有保证地问
- [[AskBeforePlan]] — 对比：Ask-before-Plan 问参数 vs CICC 问意图
- [[IntentSignalTheory]] — CICC 的覆盖率保证部分缓解不可逆意图丢失
