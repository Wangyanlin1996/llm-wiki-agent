---
title: "ProCodeBench: 主动编程助手——真实开发者行为vs模拟"
type: source
tags: [intent-recommendation]
sources: [procodebench]
source_file: raw/papers/2605.05700.pdf
last_updated: 2026-06-04
---

## 概要
ProCodeBench 对比1,246位工业开发者真实IDE交互与LLM模拟轨迹。发现模拟轨迹在行为多样性/时间结构/探索模式上与真实轨迹显著差异。提出ProCodeBench真实世界基准评测主动意图预测。当前方法在真实IDE轨迹下远不可靠；模拟数据不能替代真实数据但可作为真实微调前的补充。

## 关键贡献
- 1,246位工业开发者真实IDE交互数据（VS Code扩展采集）
- 模拟vs真实轨迹对比——行为多样性/时间结构/探索模式三维度差异
- ProCodeBench真实世界主动意图预测基准
- 模拟评估高估真实性能的发现
- 模拟数据可作为真实微调前的补充但不能替代

## 关键引用
> "simulation-based evaluation can overestimate real-world performance" — 核心发现

## 关联
- [[IntentRecommendation]] — 编程场景的主动意图推荐
- [[ProAgentBench]] — 同为真实世界数据评测，但ProCodeBench在编程场景
- [[PersonalAlign]] — 同为IDE中的意图对齐，但ProCodeBench是主动而非被动

## 矛盾
- 模拟数据高估真实性能——LLM模拟IDE轨迹范式的基础假设被质疑