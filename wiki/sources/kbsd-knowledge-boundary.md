---
title: "KbSD：Agentic 搜索中知识边界感知的自蒸馏行为校准"
type: source
tags: ['semantic-retrieval', 'agentic-retrieval']
sources: [kbsd-knowledge-boundary]
source_file: raw/papers/kbsd-knowledge-boundary.pdf
last_updated: 2026-07-02
arxiv_id: "2606.29863"
authors: ["Tao Feng", "Xinke Jiang", "Chao Wu"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要

Agentic search 赋予 LLM 动态检索能力，但现有 RL 方法在**知识边界校准**上受奖励稀疏限制——即决定何时信任参数记忆、何时依赖检索证据、何时弃答。二元奖励能惩罚不良结果，却无法为跨不同知识状态做校准决策所需的推理过程提供指导。本文提出 **KbSD（Knowledge boundary Self-Distillation）**：构造一个与学生架构相同但接收显式知识边界信号（参数确定性、检索质量、地面真值答案）的 **hint 增强教师**，生成校准推理示范，实现信息不对称自蒸馏——无需更大外部模型即可提供密集监督。针对不同知识状态下异质的推理分布，引入**象限自适应蒸馏目标**：集中整合象限用 reverse KL、多样拒绝象限用 forward KL、需兼顾精度与覆盖的非对称象限用 Pareto 最优双向 KL。多基准上 KbSD 一致提升任务准确率与幻觉抑制，最大增益出现在稀疏奖励最无信息量的挑战象限。

## 关键贡献

- **知识边界校准三决策**：形式化为"信任参数记忆/依赖检索证据/弃答"三态决策，并按参数确定性与检索质量构建四象限分类法
- **hint 增强教师信息不对称自蒸馏**：教师与学生架构相同但接收显式知识边界信号生成校准示范，提供密集 token 级监督而无需更大外部模型
- **象限自适应 KL 蒸馏目标**：集中整合用 reverse KL、多样拒绝用 forward KL、非对称象限用 Pareto 最优双向 KL，适配各象限异质推理分布

## 关键引用

> "Binary rewards can penalize undesirable outcomes, but provide little guidance on the reasoning process required to make calibrated decisions across different knowledge states."

## 关联

- [[AgenticRetrieval]] — 本文是该概念在知识边界校准维度的方法，解决 agent 何时检索/信任/弃答的决策问题
- [[RetrievalAugmentedGeneration]] — 知识边界校准是 RAG 幻觉抑制与可靠性提升的关键路径
- [[r2-searcher]] — 互补关系：本文校准知识边界（信任记忆/依赖检索/弃答），后者校准检索-推理边界（检索内容是否支撑推理）

## 矛盾

无已知矛盾。
