---
title: A-MEM：Zettelkasten 式自主记忆系统
type: source
tags:
- agent-memory
sources:
- amem
source_file: raw/papers/amem.pdf
last_updated: 2026-06-08
arxiv_id: '2502.12110'
authors:
- Wujiang Xu
- Zujie Liang
- Kai Mei
- Hang Gao
- Juntao Tan
- Yongfeng Zhang
year: 2025
venue: NeurIPS 2025
---
## 概要
A-MEM 提出基于 Zettelkasten 方法论的 LLM Agent 自主记忆系统。新记忆加入时生成包含上下文描述、关键词和标签的综合笔记，系统分析历史记忆建立有意义连接，并触发记忆演化——新记忆可更新已有记忆的上下文表示。6 个基础模型评测超越 SOTA。

## 关键贡献
- Zettelkasten 式动态索引与链接：建立互联知识网络而非扁平存储
- 记忆演化机制：新记忆整合时自动更新历史记忆的属性和上下文
- Agent-driven 决策：记忆组织由 Agent 自主决定而非固定操作

## 关键引用
> "Our approach combines the structured organization principles of Zettelkasten with the flexibility of agent-driven decision making" — 核心设计理念

## 关联
- [[AgentMemory]] — A-MEM 与 Storage→Reflection→Experience 演化框架形成对比：Zettelkasten 强调互联而非抽象
- [[EvoMemBench]] — A-MEM 在 LoCoMo 上与 A-MEM 基线对比
- [[CrossFrameworkMemorySharing]] — A-MEM 的互联网络 vs Agent KB 的跨框架共享

## 矛盾
- 与 [[MemCog]] 的 Memory-as-Cognition 范式方向不同：A-MEM 保持结构化存储+链接，MemCog 强调主动认知