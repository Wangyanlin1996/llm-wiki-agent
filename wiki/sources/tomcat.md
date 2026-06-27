---
title: Tomcat：人-Agent协作中的心智理论推理
type: source
tags:
- intent-understanding
sources:
- tomcat
source_file: raw/papers/tomcat.pdf
last_updated: 2026-06-08
arxiv_id: '2507.02935'
authors:
- Fardin Saad
- Pradeep K. Murukannaiah
- Munindar P. Singh
year: 2025
---
## 概要
Tomcat 提出指令推理（Instruction Inference）任务：Agent 协助人类主体达到目标时，需从不完整/模糊指令推断未言意图——即行使主体的心智理论（ToM）。Tomcat 有 Fs-CoT（少样本链式思考）和 CP（常识提示）两种变体。52 人类参与者对照实验显示 Fs-CoT（GPT-4o、DeepSeek-R1）可达人类参与者水平。

## 关键贡献
- 指令推理任务：不完整/模糊指令→推断未言意图
- ToM 推理形式化：从共享上下文推断主体心理状态
- 人类对照实验：52 人参与，意图准确度、行动最优性、规划最优性三维评测

## 关键引用
> "The agent must exercise the principal's Theory of Mind and infer the mental states of its principal" — ToM 推理本质

## 关联
- [[IntentSignalTheory]] — Tomcat 从共享上下文推断未言意图，对应 I-hat 从 P 推断 I* 的尝试
- [[IntentUnderstanding]] — 指令推理扩展了 IU 的应用场景：不完整指令的意图推断
- [[AskBeforePlan]] — Tomcat 推断意图 vs Ask-before-Plan 主动询问——两种处理模糊意图的策略

## 矛盾
- Tomcat 依赖"共享上下文"推断意图，但 [[IntentSignalTheory]] 证明当 I* 私有意图不在载体 P 中时不可恢复