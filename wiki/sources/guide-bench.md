---
title: GUIDE：GUI意图检测评测基准（CVPR 2026）
type: source
tags:
- intent-understanding
sources:
- guide-bench
source_file: raw/papers/guide-bench.pdf
last_updated: 2026-06-08
arxiv_id: '2603.25864'
authors:
- Saelyne Yang
- Jaesang Yu
- Yi-Hao Peng
- Kevin Qinghong Lin
- Jae Won Cho
- Yale Song
- Juho Kim
year: 2026
venue: CVPR 2026
---
## 概要
GUIDE（GUI User Intent Detection Evaluation）是首个针对开放 GUI 任务中用户意图理解的评测基准。67.5 小时屏幕录制、120 新手用户、10 种软件，含有声思考旁白。定义三个任务：行为状态检测、意图预测、帮助预测。8 个 SOTA 多模态模型均表现不佳（44.6%/55.0%），但提供用户上下文可将帮助预测提升 50.2pp。

## 关键贡献
- 首个 GUI 意图理解基准：从自动化转向协作式理解
- 有声思考旁白：真实用户在开放任务中的意图表达
- 用户上下文的关键作用：+50.2pp 证明结构化用户理解的重要性

## 关键引用
> "GUI agents must understand what users are doing and why" — 从自动化到理解

## 关联
- [[IntentUnderstanding]] — GUIDE 将意图理解带入 GUI 场景，与 [[PersonalAlign]] 的 GUI 方向互补
- [[ProactiveInterventionDecisionChain]] — GUIDE 的帮助预测任务与 SII/PIWM 的干预决策链相似
- [[IntentRecommendation]] — GUIDE 的"何时帮助"问题跨 IU 和 IR

## 矛盾
- GUIDE 发现模型帮助预测仅 55%，但提供上下文可+50.2pp——说明问题不在推理能力而在缺乏用户上下文，呼应 [[IntentSignalTheory]] 的 I*→P 信息损失