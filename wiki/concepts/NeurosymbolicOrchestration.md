---
title: "神经符号编排（Neurosymbolic Orchestration）"
type: concept
tags: [agent-explainability, neurosymbolic, orchestration, verifiable-trace, skill-selection]
sources: [vadaorchestra, skillcat, looking-not-picking]
last_updated: 2026-07-02
---

神经符号编排（Neurosymbolic Orchestration）指将 LLM 的高层规划灵活性与符号引擎的推理可验证性解耦的 agent 工作流编排范式，填补 synthesis 报告方向2"基于 LLM 的 Skill 编排（vs 经典 HTN/PDDL）的对比解释"空白。[[vadaorchestra]] 将工作流编码为 Datalog+/- 逻辑程序，LLM 增量规划而符号引擎执行推理，提供可验证推理轨迹；[[skillcat]] 用对比因果提取从成功/失败对识别 skill 选择证据；[[looking-not-picking]] 用注意力段透镜定位工具选择失败在读出而非感知。三者共同构成 AgentLoop 编排层的可解释性栈：神经（灵活规划）+符号（可验证执行）+对比（选择归因）。相关论文：[[vadaorchestra]]、[[skillcat]]、[[looking-not-picking]]、[[ExplainablePlanning]]。
