---
title: DS-IA：双阶段意图感知框架（主动拒绝+确定执行）
type: source
tags:
- intent-recommendation
sources:
- ds-ia-framework
source_file: raw/papers/ds-ia-framework.pdf
last_updated: 2026-06-08
arxiv_id: '2603.16207'
authors:
- Xinxin Jin
- Zhengwei Ni
- Zhengguo Sheng
- Victor C. M. Leung
year: 2026
---
## 概要
DS-IA（Dual-Stage Intent-Aware）框架将高层意图理解与底层物理执行分离。Stage 1 语义防火墙：过滤无效指令+通过家居状态检查解决模糊命令；Stage 2 确定性级联验证器：按房间→设备→能力顺序验证操作可行性。在 HomeBench/SAGE 基准上 EM 58.56%（+28%），无效指令拒绝率 87.04%。解决交互频率困境：将自主成功率从 42.86%提升到 71.43%。

## 关键贡献
- 语义防火墙：高层意图理解层独立于物理执行
- 确定性级联验证器：房间→设备→能力序列验证
- 交互频率困境解决：平衡主动询问与状态推断

## 关键引用
> "DS-IA resolves the Interaction Frequency Dilemma by balancing proactive querying with state-based inference" — 核心平衡策略

## 关联
- [[IntentRecommendation]] — DS-IA 的"主动拒绝"是 IR 的新维度：何时拒绝而非何时推荐
- [[ProactiveInterventionDecisionChain]] — DS-IA 的两阶段框架与 SII/PIWM 的看-推断-干预三阶段相似
- [[SimulationRealityGap]] — DS-IA 在 HomeBench 和 SAGE 上都验证了，跨基准一致性较好

## 矛盾
- DS-IA 的语义防火墙"拒绝无效指令"与 [[KnowU-Bench]] 的"拒绝后克制"概念呼应但侧重不同：DS-IA 侧重指令有效性而非用户偏好