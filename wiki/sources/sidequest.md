---
title: "SideQuest：长程智能体推理的模型驱动 KV Cache 管理"
type: source
tags: [multi-agent-long-context]
sources: [sidequest]
source_file: raw/papers/sidequest.pdf
last_updated: 2026-07-24
arxiv_id: "2602.22603"
authors: ["Sanjay Kariyappa", "G. E. Suh"]
year: 2026
venue: "arXiv.org"
citation_count: 7
doi: "10.48550/arXiv.2602.22603"
---

## 概要
SideQuest 利用大型推理模型 (LRM) 自身执行 KV cache 压缩，通过推理其上下文中 token 的有用性。为防止管理过程产生的 token 污染模型记忆，将 KV cache 压缩构建为并行于主推理任务的辅助任务。仅用 215 个样本训练的模型即可在智能体任务上将峰值 token 使用量减少 65%，准确率损失极小，优于启发式 KV cache 压缩技术。

## 关键贡献
- LRM 自身驱动 KV cache 压缩：推理 token 有用性
- 辅助并行任务隔离：防止管理 token 污染主推理记忆
- 峰值 token -65%，仅 215 样本训练

## 关键引用
> "SideQuest leverages the Large Reasoning Model (LRM) itself to perform KV cache compression by reasoning about the usefulness of tokens in its context."

## 关联
- [[AAFLOWPlus]] — AAFLOW+ 从系统层复用 KV，SideQuest 从模型层压缩 KV
- [[KVCacheManagement]] — KV Cache 管理策略
- [[LongHorizonReasoning]] — 长程推理的上下文管理

## 矛盾
- (暂无)
