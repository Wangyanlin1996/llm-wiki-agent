---
title: "真实世界vs合成评测差距（Simulation-to-Reality Gap）"
type: concept
tags: [intent-recommendation, intent-understanding]
sources: [proagentbench, procodebench]
last_updated: 2026-06-04
---

LLM模拟数据与真实用户行为之间存在系统性差距。ProAgentBench 发现合成数据无法捕捉真实交互的突发模式（burstiness B=0.787）。ProCodeBench 发现模拟IDE轨迹在行为多样性/时间结构/探索模式上与真实轨迹显著差异，模拟评估会高估真实性能。共同结论：真实数据训练远优于合成数据，模拟数据不能替代但可作为真实微调前的补充。这是主动Agent评测方法论的根本挑战。

相关论文：[[proagentbench]], [[procodebench]], [[knowu-bench]]