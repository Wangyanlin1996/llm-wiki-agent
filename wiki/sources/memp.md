---
title: 'Memp: Agent 程序性记忆探索'
type: source
tags:
- agent-memory
sources:
- memp
source_file: raw/papers/memp.pdf
last_updated: 2026-06-04
arxiv_id: '2508.06433'
authors:
- Runnan Fang
- Yuan Liang
- Xiaobin Wang
- Jialong Wu
- Shuofei Qiao
- Pengjun Xie
- Fei Huang
- Huajun Chen
- Ningyu Zhang
year: 2025
venue: ACL 2026 Findings
citation_count: 38
---
## 概要
Memp 探索可学习、可更新、终身化的Agent程序性记忆，将轨迹蒸馏为细粒度步骤指令+高层次脚本抽象两种形式，研究 Build/Retrieval/Update 三种策略的影响。动态更新机制持续更新、纠正和废弃记忆内容。强模型构建的程序性记忆可迁移到弱模型仍获显著增益。ACL 2026 Findings 录用。

## 关键贡献
- 提出程序性记忆（Procedural Memory）的Build/Retrieval/Update三策略研究
- 双层次蒸馏：细粒度步骤指令 + 高层次脚本抽象
- 动态更新机制——持续更新、纠正、废弃
- 跨模型迁移——强模型记忆迁移到弱模型仍有增益

## 关键引用
> "procedural memory built from a stronger model retains its value: migrating the procedural memory to a weaker model can also yield substantial performance gains" — 跨模型迁移发现

## 关联
- [[AgentMemory]] — 程序性记忆作为新的记忆类型（区别于陈述性记忆）
- [[MemCog]] — 记忆即认知范式——程序性记忆是认知能力的核心组成部分
- [[Mem-π]] — 同为按需生成而非静态检索，但Memp是脚本生成而非RL决策
- [[AgentKB]] — 同为跨框架经验共享，但Memp是单Agent内的程序性技能

## 矛盾
- 与纯检索式记忆范式（ExpRAG）的矛盾——程序性记忆需要内化而非外部检索