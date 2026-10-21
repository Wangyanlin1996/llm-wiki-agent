---
title: "Twin Agent：特权分离智能体的上下文残差压缩"
type: source
tags: [multi-agent-long-context]
sources: [twin-agent]
source_file: raw/papers/twin-agent.pdf
last_updated: 2026-07-24
arxiv_id: "2607.19595"
authors: ["Zhanhao Hu", "Dennis Jacob", "Xiao Huang", "Zhaorun Chen", "Bo Li", "David Wagner"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
Twin Agent 提出一种通用的特权分离设计模式，受 agent 上下文中的残差编码启发。由两个近乎对称的 agent 组成：Explore Agent 检查不可信信息，Safe Agent 执行特权操作。Explore Agent 基于 Safe Agent 当前上下文条件化，仅传递紧凑 hint。这种设计减少了保持任务效用所需的信息量，实现更好的安全-效用权衡。在 SWE-bench Lite 长程软件工程任务上保持高效用的同时防止 prompt injection 攻击。

## 关键贡献
- 特权分离设计模式：Explore Agent（不可信信息检查）+ Safe Agent（特权执行）
- 上下文残差压缩：仅传递紧凑 hint，减少信息需求
- SWE-bench Lite + AgentDojo + DecodingTrust 验证安全-效用权衡

## 关键引用
> "Twin Agent consists of two nearly symmetric agents: an Explore Agent that inspects untrusted information and a Safe Agent that executes privileged actions. The Explore Agent communicates only compact hints to the Safe Agent."

## 关联
- [[ContextResidualCompression]] — 上下文残差压缩范式
- [[PrivilegeSeparation]] — 智能体特权分离
- [[MultiAgentLongContext]] — 双 agent 架构处理长上下文

## 矛盾
- (暂无)
