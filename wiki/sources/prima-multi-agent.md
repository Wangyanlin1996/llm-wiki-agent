---
title: "PRIMA：弹性多智能体研究的操作模式"
type: source
tags: [multi-agent-long-context]
sources: [prima-multi-agent]
source_file: raw/papers/prima-multi-agent.pdf
last_updated: 2026-07-24
arxiv_id: "2605.24775"
authors: ["Sasank Annapureddy"]
year: 2026
venue: "arXiv.org"
citation_count: 0
doi: "10.48550/arXiv.2605.24775"
---

## 概要
PRIMA 提出三种操作模式：(1) 弹性恢复层——检测上游限流信号、持久化类型化暂停记录、跨进程重启恢复长运行；(2) 子智能体操作规范——编码任务忠实性、工具使用、修订和步骤间上下文边界规范；(3) 多阶段应用模式——正交 draft 步骤 + 显式跨文档协调 pass。建立在研究程序规范语言（显式收敛标准、双度量评分引擎、外部元优化循环、上下文压缩）之上。

## 关键贡献
- 三种操作模式：弹性恢复 + 子智能体操作规范 + 多阶段应用
- 研究程序规范语言：收敛标准 + 双度量评分 + 元优化 + 上下文压缩
- 素数幂 agent 身份：无碰撞标识 + 无中央注册的可验证成员

## 关键引用
> "Three operational patterns: a resilience-and-recovery layer, a sub-agent operating discipline encoding task-fidelity, tool-use, revision, and inter-step context-boundary norms, and a multi-phase application pattern."

## 关联
- [[MultiAgentLongContext]] — 长程多智能体研究的弹性模式
- [[ContextCompaction]] — 上下文压缩
- [[AgentIdentityVerification]] — 智能体身份验证

## 矛盾
- (暂无)
