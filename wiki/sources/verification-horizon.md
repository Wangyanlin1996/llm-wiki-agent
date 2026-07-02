---
title: "The Verification Horizon: No Silver Bullet for Coding Agent Rewards（编码 Agent 奖励的验证地平线：无银弹）"
type: source
tags: [agent-explainability, verification, reward-hacking, closed-loop-verification]
sources: [verification-horizon]
source_file: raw/papers/verification-horizon.pdf
last_updated: 2026-07-02
arxiv_id: "2606.26300"
authors: ["Binghai Wang", "Chenlong Zhang", "Dayiheng Liu", "Jiajun Zhang", "Jiawei Chen", "Mingze Li", "Mouxiang Chen", "Rongyao Fang", "Siyuan Zhang", "Xuwu Wang", "Yuheng Jing", "Zeyao Ma", "Zeyu Cui"]
year: 2026
venue: "arXiv preprint"
citation_count: pending
---

## 概要

经典直觉认为验证解比产生解容易。对今天的编码 agent，此直觉正在**逆转**：随着基础模型推理能力增强、工程脚手架日益精密，生成复杂候选解不再困难——可靠验证它们成了更难的问题。每个验证器都只是人类意图的代理，从非意图本身。验证面临双重困难：(1) 意图本质欠规格化，难以忠实检查是否已满足；(2) 训练时优化扩大代理与意图的差距（reward hacking/信号饱和）。本文沿**可扩展性、忠实度、鲁棒性**三维度刻画验证信号质量，论证三者同时达成是核心挑战；研究四种奖励构造（测试验证器/rubric 验证器/用户验证器/自动 agent 验证器），证明定向验证设计可抑制 reward hacking。

## 关键贡献

- **"验证比生成更难"的逆转趋势**：挑战 AgentLoop 方向3（闭环验证）的核心假设——验证不再是廉价环节
- **三维度验证质量框架**：可扩展性×忠实度×鲁棒性，三者不可同时达成——为闭环验证提供评估维度
- **验证必须与生成器协同演化**：无固定奖励函数能在策略能力持续增长下保持有效——直接对应 AgentLoop 闭环的动态性

## 关键引用

> "Every verifier we can build is only a proxy for human intent, never the intent itself... no fixed reward function can remain effective as policy capability continues to grow; and verification must co-evolve with the generator."

## 关联

- [[VerificationCoEvolution]] — 本文是该概念的理论基础
- [[AgentExplainability]] — 验证地平线界定了闭环可解释性的能力边界
- [[IntentSignalTheory]] — "意图欠规格化"呼应 I*→P 不可逆信息损失
- [[grounded-continuation]] — 运行时验证器是验证地平线内的具体实现
- [[causal-explanations-sequential-uncertainty]] — 验证与因果解释共享 MDP 不确定性挑战

## 矛盾

与"验证比生成容易"的经典直觉直接矛盾——本文证明在编码 agent 领域此直觉已逆转。
