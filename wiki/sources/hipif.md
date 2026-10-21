---
title: "HIPIF：长程 LLM 智能体学习的层级规划与信息折叠"
type: source
tags: [multi-agent-long-context]
sources: [hipif]
source_file: raw/papers/hipif.pdf
last_updated: 2026-07-24
arxiv_id: "2606.10507"
authors: ["Juncheng Diao", "Zhicong Lu", "Peiguang Li", "Yongwei Zhou", "Changyuan Tian", "Qingbin Li", "Rongxiang Weng", "Jingang Wang", et al.]
year: 2026
venue: "arXiv preprint"
citation_count: 1
doi: ""
---

## 概要
HIPIF 受人类通过子目标分解和已完成进度摘要处理复杂任务的方式启发，训练 agent 端到端地围绕显式子目标组织长程执行，同时折叠已完成子目标历史以减少长上下文干扰。结合层级反思和子目标导向的过程奖励指导子目标生成、转换和执行，不依赖昂贵的辅助模型或任务特定专家轨迹。在三个公开 agentic 基准上验证有效性。

## 关键贡献
- 层级规划 + 信息折叠：子目标组织 + 已完成历史折叠
- 层级反思 + 子目标导向过程奖励
- 不依赖辅助模型或专家轨迹的端到端训练

## 关键引用
> "HIPIF trains the agent end-to-end to organize long-horizon execution around explicit subgoals while folding completed subgoal histories to reduce long-context interference."

## 关联
- [[MultiAgentLongContext]] — 长程智能体学习的上下文干扰减少
- [[InformationFolding]] — 信息折叠机制
- [[SubgoalDecomposition]] — 子目标分解与历史折叠

## 矛盾
- (暂无)
