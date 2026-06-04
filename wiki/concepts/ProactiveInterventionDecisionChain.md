---
title: "主动干预决策链（Proactive Intervention Decision Chain）"
type: concept
tags: [intent-understanding, intent-recommendation]
sources: [sii-piwm, knowu-bench, proagentbench]
last_updated: 2026-06-04
---

主动干预决策链是主动Agent从检测意图到选择干预的完整决策流程。SII/PIWM 定义了 See→Infer→Intervene 三阶段，从五类响应（Greet/Elicit/Inform/Recommend/Hold）中选择。KnowU-Bench 评测了主动决策链的三个关键环节：偏好获取→同意协商→拒绝后克制。ProAgentBench 将主动辅助分解为时机预测+辅助内容生成两阶段。核心发现：前沿模型擅长意图理解但不擅长干预决策（何时干预、如何干预、何时放弃）。

相关论文：[[sii-piwm]], [[knowu-bench]], [[proagentbench]], [[IntentSignalTheory]]