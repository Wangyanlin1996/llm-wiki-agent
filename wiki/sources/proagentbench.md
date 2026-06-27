---
title: 'ProAgentBench: 真实世界数据的主动Agent评测'
type: source
tags:
- intent-recommendation
sources:
- proagentbench
source_file: raw/papers/proagentbench.pdf
last_updated: 2026-06-04
arxiv_id: '2602.04482'
authors:
- Yuanbo Tang
- Huaze Tang
- Tingyu Cao
- Lam Nguyen
- Anping Zhang
- Xinwen Cao
- Chunkang Liu
- Wenbo Ding
- Yang Li
year: 2026
venue: arXiv
citation_count: 0
---
## 概要
ProAgentBench 用真实世界数据评测主动Agent辅助。层次化任务框架分解主动辅助为时机预测+辅助内容生成。28,000+事件/500+小时真实用户会话保留burstiness B=0.787的突发交互模式。发现长期记忆和历史上下文显著提升预测准确率，真实数据训练远优于合成数据。

## 关键贡献
- 层次化任务框架——时机预测 + 辅助内容生成两阶段分解
- 真实世界数据集：28,000+事件，500+小时真实用户会话
- 保留突发交互模式（burstiness B=0.787），区别于合成数据
- 长期记忆和历史上下文显著提升时机预测
- 真实数据训练远优于合成数据

## 关键引用
> "real-world training data substantially outperforms synthetic alternatives" — 核心发现

## 关联
- [[IntentRecommendation]] — 时机预测作为意图推荐的入口
- [[PIRF]] — 同为主动意图推荐中的时机判断
- [[IceBreaker]] — 同为对话开场时机，但ProAgentBench是工作场景而非社交
- [[PASK]] — 同为长期记忆驱动的主动意图，但ProAgentBench验证了记忆的重要性

## 矛盾
- 合成数据会高估真实性能——与LLM模拟评估范式的矛盾