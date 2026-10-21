---
title: "MemAgent：基于多对话 RL 记忆智能体的长上下文 LLM 重塑"
type: source
tags: [multi-agent-long-context]
sources: [memagent-long-context]
source_file: raw/papers/memagent-long-context.pdf
last_updated: 2026-07-24
arxiv_id: "2507.02259"
authors: ["Hongli Yu", "Ting Chen", "Jiangtao Feng", "Jiangjie Chen", "Weinan Dai", "Qiying Yu", "Ya-Qin Zhang", "Wei-Ying Ma", et al.]
year: 2025
venue: "arXiv.org"
citation_count: 180
doi: "10.48550/arXiv.2507.02259"
---

## 概要
MemAgent 提出了一种新颖的 agent 工作流，通过分段读取文本并使用覆写策略更新记忆来端到端优化长文本任务。它将 DAPO 算法扩展为独立上下文多对话生成训练。MemAgent 展现了卓越的长上下文能力：在 32K 文本上训练的 8K 上下文模型可外推到 3.5M QA 任务且性能损失<5%，在 512K RULER 测试中达到 95%+。这是多智能体记忆方法在长上下文处理上的重要突破。

## 关键贡献
- 新颖的 agent 工作流：分段读取 + 覆写记忆策略，端到端 RL 训练
- 将 DAPO 算法扩展为独立上下文多对话生成 (multi-conv RL)
- 8K→3.5M 外推性能损失<5%，512K RULER 95%+

## 关键引用
> "MemAgent has demonstrated superb long-context capabilities, being able to extrapolate from an 8K context trained on 32K text to a 3.5M QA task with performance loss < 5% and achieves 95%+ in 512K RULER test."

## 关联
- [[AMAAdaptiveMemory]] — AMA 也用多智能体管理记忆，但关注多粒度
- [[MultiAgentLongContext]] — 多智能体记忆方法处理长上下文
- [[RLBasedMemoryAgent]] — RL 训练的记忆智能体

## 矛盾
- (暂无)
