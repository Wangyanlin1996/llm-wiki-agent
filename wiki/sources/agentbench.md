---
title: "AgentBench: Evaluating LLMs as Agents（LLM 作为智能体的多维评测基准）"
type: source
tags: [agent-evaluability, LLM-agent, benchmark]
sources: [agentbench]
source_file: raw/papers/agentbench.pdf
last_updated: 2026-06-29
arxiv_id: "2308.03688"
authors: ["Xiao Liu", "Hao Yu", "Hanchen Zhang", "Yifan Xu", "Minlie Huang", "Yuxiao Dong", "Jie Tang"]
year: 2024
venue: "ICLR 2024"
citation_count: 951
doi: "10.48550/arXiv.2308.03688"
---

## 概要

AgentBench 提出一个多维度基准，由 8 个不同环境组成，用于量化评估 LLM 作为智能体（LLM-as-Agent）在交互式环境中的推理与决策能力。通过对 API 闭源模型与开源模型（≤70B）的大规模测试，发现顶尖商业模型在复杂环境中具备较强 agent 能力，但开源模型与之存在显著差距。

## 关键贡献

- 构建覆盖 8 个环境的多维度 agent 评测基准，系统评估推理、规划、工具调用、长程决策等多阶段能力。
- 识别 agent 失败的典型原因：长程推理薄弱、决策能力不足、指令遵循差是阻碍可用 LLM agent 的主要障碍。
- 实证发现：训练于高质量多轮对齐数据可改善 agent 表现；代码训练对不同 agent 任务影响不一（与既有假设不同）。

## 关键引用

> "poor long-term reasoning, decision-making, and instruction following abilities are the main obstacles for developing usable LLM agents" — Agent 失败根因归纳

> "training on code present ambivalent impacts on different agent tasks" — 对"代码训练普遍提升 agent 能力"假设的反驳

## 关联

- [[LLMAutonomousAgent]] — AgentBench 为 LLM 自主智能体的多阶段能力提供了评测底座，佐证"agent 行为具有多阶段性"
- [[AgentExplainability]] — 多阶段评测结果支撑"解释必须沿信息转换节点展开"的论点：单步输出解释不足以诊断长程推理失败
- [[IntentUnderstanding]] — agent 评测中的指令遵循维度与意图理解上游相关

## 矛盾

- 本页作者署名与外部引用清单标注（"Park, S. et al."）不符——论文真实第一作者为 Liu, X.，外部清单的作者归属有误。
