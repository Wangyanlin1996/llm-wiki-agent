---
title: "CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists（面向 AI 科学家的可扩展交互式因果发现环境）"
type: source
tags: [agent-explainability, causal-discovery, faithfulness, evaluation, SCM]
sources: [causalab]
source_file: raw/papers/causalab.pdf
last_updated: 2026-07-02
arxiv_id: "2605.26029"
authors: ["Junlin Yang", "Dylan Zhang", "Xiangchen Song", "Qirun Dai", "Xiao Liu", "Yuen Chen", "Aniket Vashishtha", "Jing Shi", "Chenhao Tan", "Hao Peng"]
year: 2026
venue: "arXiv preprint"
citation_count: pending
---

## 概要

本文引入 **CausaLab**，一个评估 LLM agent 交互式因果发现的可扩展环境。与既有评估不同，CausaLab 同时评估 agent 能否用因果证据解决问题**以及**其答案是否基于忠实恢复的因果机制。每个 episode 将 agent 置于合成实验室：接收先验测量记录，对操纵器晶体干预，预测由同一机制支配的留出反应器晶体的共振频率。隐藏数据生成过程是随机采样的结构因果模型（SCM），因此成功需恢复因果图和结构方程而非回忆先验知识。实验揭示**预测与机制恢复的持续差距**：纯观测 6 节点设置下 GPT-5.2-high 达 92% 任务准确率但仅 0.471 全边 F1。

## 关键贡献

- **预测成功 ≠ 因果理解**：分离任务准确率与机制忠实度——为 AgentLoop 方向3（因果归因）和方向6（评估）提供关键区分
- **SCM 采样的可扩展评估**：随机 SCM 生成避免记忆先验，强制真正的因果发现
- **过早停止为主要弱点**：一致性验证可缓解——为闭环验证的迭代深度提供指导

## 关键引用

> "CausaLab therefore separates predictive success from causal understanding and exposes current LLM agents' limits as experimental causal reasoners."

## 关联

- [[CausalExplanation]] — CausaLab 评估因果解释的忠实度而非仅结果
- [[VerificationCoEvolution]] — 预测 vs 机制恢复差距是验证地平线的因果实例
- [[causal-explanations-sequential-uncertainty]] — SCM 因果发现与 SCM 因果解释共享基础
- [[cema-causal-explanations-mas]] — 因果机制恢复是多 agent 因果解释的前提
- [[AgentExplainability]] — 因果忠实度是过程级解释的质量维度

## 矛盾

揭示"高任务准确率≠因果理解"的矛盾——agent 可在不知因果机制的情况下预测正确，挑战了"结果正确即理解正确"的假设。
