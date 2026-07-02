---
title: "SkillCAT: Contrastive Assessment and Topology-Aware Skill Self-Evolution for LLM Agents（对比评估与拓扑感知的 Skill 自演化）"
type: source
tags: [agent-explainability, skill-evolution, contrastive-assessment, skill-orchestration]
sources: [skillcat]
source_file: raw/papers/skillcat.pdf
last_updated: 2026-07-02
arxiv_id: "2606.13317"
authors: ["Kunfeng Chen", "Qihuang Zhong", "Juhua Liu", "Bo Du"]
year: 2026
venue: "arXiv preprint"
citation_count: pending
---

## 概要

LLM agent 的 skill 自演化方法将执行轨迹转化为可复用 skill 文档，但现有管线通常每任务只学一条轨迹、合并候选 skill 补丁前不检查、推理时加载全部 skill 语料。本文提出 **SkillCAT**，一个免训练框架，将此过程分三阶段：**对比因果提取（CCE）**对每任务采样多条轨迹，比较同任务成功/失败对以识别解释结果差异的证据；**评估增强演化（AAE）**在源任务克隆上重放每个候选补丁，仅保留改进或保持结果的补丁后再层次化合并；**拓扑感知任务执行（TTE）**将演化 skill 编译为可路由子 skill 拓扑，推理时仅加载与任务相关的能力节点。在 SpreadsheetBench、WikiTableQuestions、DocVQA 上平均分较基线提升最高 40.40%。

## 关键贡献

- **对比因果提取**：从成功/失败对中识别解释结果差异的证据——为 AgentLoop 方向2提供"为什么选此 skill 而非彼"的因果对比基础
- **层次化 skill 拓扑路由**：仅加载相关能力节点，避免全语料加载——直接对应 AgentLoop 的 Skill 编排层
- **评估增强演化**：补丁合并前验证，防止 skill 退化

## 关键引用

> "Contrastive Causal Extraction (CCE) samples multiple trajectories for each task and compares same-task success/failure pairs to identify evidence that explains outcome differences."

## 关联

- [[ContrastiveSkillAssessment]] — 本文是该概念的代表实现
- [[AgentExplainability]] — 对比评估是 Skill 选择可解释性的方法
- [[ExplainablePlanning]] — skill 拓扑路由是可解释规划的工具实例
- [[NeurosymbolicOrchestration]] — skill 演化与神经符号编排互补构成 AgentLoop 编排层

## 矛盾

无已知矛盾。
