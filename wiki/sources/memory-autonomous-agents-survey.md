---
title: 自主Agent记忆综述：机制、评测与前沿
type: source
tags:
- agent-memory
sources:
- memory-autonomous-agents-survey
source_file: raw/papers/memory-autonomous-agents-survey.pdf
last_updated: 2026-06-08
arxiv_id: '2603.07670'
authors:
- Pengfei Du
year: 2026
---
## 概要
全面综述 LLM Agent 记忆研究（2022-2026），形式化 write-manage-read 循环与感知-行动紧密耦合。提出三维分类：时间范围（STM/MTM/LTM）、表示基底（文本/图/参数）、控制策略（固定/检索/学习）。深入分析五大机制族：上下文驻留压缩、检索增强存储、反思自改进、层次化虚拟上下文、策略学习管理。追踪从静态回忆到多会话Agent测试的评测演变。

## 关键贡献
- write-manage-read 循环形式化：与感知行动耦合而非独立存储
- 三维分类法：时间范围 × 表示基底 × 控制策略
- 五大机制族系统化梳理与开放挑战：持续整合、因果检索、可信反思、学习遗忘、多模态具身记忆

## 关键引用
> "Memory -- the ability to persist, organize, and selectively recall information across interactions -- is what turns a stateless text generator into a genuinely adaptive agent" — 记忆定义

## 关联
- [[AgentMemory]] — 综述补充 wiki 现有 Storage→Reflection→Experience 演化框架，增加 write-manage-read 循环视角
- [[EvoMemBench]] — 综述追踪评测演变，EvoMemBench 是其中之一
- [[STALE]] — 综述提出"学习遗忘"开放挑战，STALE 是具体实现

## 矛盾
- 综述提出"学习遗忘"方向，与 [[EvoMemBench]] "长上下文仍强"似乎矛盾——但遗忘的目标不是全部丢弃而是选择性过期