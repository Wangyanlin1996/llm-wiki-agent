---
title: "MemoryOS: AI Agent 记忆操作系统"
type: source
tags: [agent-memory]
sources: [memoryos]
source_file: raw/papers/2506.06326.pdf
last_updated: 2026-06-04
---

## 概要
MemoryOS 受操作系统记忆管理原理启发，设计STM/MTM/LTM三级存储架构，包含存储、更新、检索、生成四大模块。STM→MTM更新遵循对话链FIFO原则，MTM→LTM使用分段页面组织策略。LoCoMo基准上 F1+49.11%，BLEU-1+46.18%，实现长期对话的上下文连贯性和个性化记忆保持。

## 关键贡献
- OS启发的记忆管理系统——STM/MTM/LTM三级存储+四大模块
- FIFO对话链更新（STM→MTM）+ 分段页面组织（MTM→LTM）
- GPT-4o-mini上F1+49.11%, BLEU-1+46.18%的显著提升
- 开源代码（github.com/BAI-LAB/MemoryOS）

## 关键引用
> "MemoryOS enables hierarchical memory integration and dynamic updating" — 核心设计理念

## 关联
- [[AgentMemory]] — OS启发的新架构范式
- [[LightMem]] — 同为STM/MTM/LTM三层体系，但MemoryOS采用OS式页面管理而非SLM驱动
- [[H-Mem]] — 同为混合表示（facts+summaries+profiles），但MemoryOS更系统化

## 矛盾
- 与LightMem在更新策略上的差异：FIFO对话链 vs SLM压缩