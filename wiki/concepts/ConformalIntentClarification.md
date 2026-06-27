---
title: "ConformalIntentClarification"
type: concept
tags: [conformal-prediction, intent-classification, clarification, uncertainty-quantification, out-of-scope-detection]
sources: [cicc, clara]
last_updated: 2026-06-23
---

# ConformalIntentClarification

共形意图澄清（Conformal Intent Classification and Clarification, CICC）——将任意意图分类器的不确定度通过共形预测转为有统计保证的预测集，基于预测集大小做三分支决策（直接执行 / 澄清问意图 / 拒绝太模糊）。

## 共形预测基础

给定预训练分类器 f̂、校准集 D（规模 n）、错误率 α：

1. 非一致性函数 `s(X,Y) = 1 - f̂(X)_Y`（真类 softmax 越低→得分越高）
2. 校准集上算所有 s 值，取分位数 `q̂ = ⌈(n+1)(1-α)⌉/n`
3. 测试时构造预测集 `C(X_t) = {y : s(X_t, y) ≤ q̂}`

**保证**：`P(Y_t ∈ C(X_t)) ≥ 1 - α`——样本有限、模型任意、分布任意都成立。**无需重训模型**，仅需一个校准集。

三种实现：Marginal CP（平均最小集，CICC 实验最优）、Conditional CP（自适应，难→大集）、RAPS（正则化小集）。

## 三分支决策

```
|C| == 1  → 直接执行（模型有信心）
|C| > th  → 拒绝（太模糊，请求重新表述/转人工）
1<|C|≤th  → 生成澄清问题（候选集合理）
```

**超参数（均有直觉解释）**：
- **α（错误率）**：置信度 vs 预测集大小权衡。α→0 置信高但集大；实验 α=0.01~0.05
- **th（阈值）**：何时太模糊。建议 ≤7（Miller 1956 认知科学）

## 澄清问题生成

当 1<|C|≤th 时，用生成式 LM 基于预测集 + 原始输入生成澄清问题。方式可插拔（模板 / 生成式 LM）。示例：输入 "lost my card"，预测集 {lost_stolen, compromised}，LM 生成 "Could your card have been compromised or did you only lose it?"

## OOS 检测

CICC 天然支持——预测集过大时拒绝输入 = OOS 分类。CICC-OOS 变体：有 OOS 校准样本时优化 α 和 th 最大化 F1。实验 F1=0.90, AUROC=0.97。

## 核心特性

- **分类器无关**：任意分类器，无需重训
- **统计保证**：真意图在候选集内（P ≥ 1-α）
- **自适应不确定度处理**：简单→直接做，歧义→问，太模糊→拒绝
- **可解释超参数**：α 和 th 都有直觉含义

## 覆盖的模糊层级

主要覆盖 **L2（意图已知但多候选歧义）**——通过交互式澄清缩小候选集，且有统计保证。同时触及 **L1 边界**：|C|>th 时拒绝输入，实现 OOS 检测。

## 关键局限：单轮保证

CICC 的覆盖率保证 `P(Y ∈ C) ≥ 1-α` **仅在第一轮交互成立**。在多轮交互中，自适应选择问题 + 根据用户回答更新信念会导致**反馈协变量偏移**（feedback covariate shift），使测试分布偏离校准分布，覆盖率漂移最多 10 个百分点。

[[CLARA]] / [[TurnValidConformalCoverage]] 解决了这个问题：用选择诱导的**似然比重加权**恢复每一轮的覆盖率保证（turn-valid coverage），将 CICC 的单轮保证扩展到多轮。

## 关联
- [[IntentUnderstanding]] — CICC 处理意图理解中的不确定性
- [[NOEM³A]] — L2 互补：NOEM³A 静默选无保证，CICC 交互问有保证
- [[AskBeforePlan]] — 层级互补：Ask-before-Plan 处理 L3 参数模糊，CICC 处理 L2 意图歧义
- [[handling-vague-user-input]] — 模糊三层层级中填补 L2 交互式澄清空白
- [[IntentSignalTheory]] — I* 缺失时 CICC 通过交互从用户恢复，且有保证不漏
- [[CLARA]] — 多轮扩展：turn-valid coverage 修正 CICC 单轮保证的局限性
- [[SAGE-Agent]] — 有原则澄清三剑客：共形预测（覆盖率保证）vs EVPI（期望信息价值）
- [[ActiveTaskDisambiguation]] — 有原则澄清三剑客：共形预测（覆盖率保证）vs 贝叶斯实验设计（信息增益）
