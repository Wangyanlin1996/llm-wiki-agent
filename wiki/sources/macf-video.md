---
title: "MACF：通过紧凑潜在多智能体协作扩展视频理解"
type: source
tags: [multi-agent-long-context]
sources: [macf-video]
source_file: raw/papers/macf-video.pdf
last_updated: 2026-07-24
arxiv_id: "2605.00444"
authors: ["Kerui Chen", "Jinglu Wang", "Jianrong Zhang", "Ming Li", "Yang Lu", "Hehe Fan"]
year: 2026
venue: "arXiv.org"
citation_count: 2
doi: "10.48550/arXiv.2605.00444"
---

## 概要
MACF 是一种端到端多智能体协作框架，将 per-agent 感知预算与全局视频复杂度解耦，实现可扩展视频理解同时保持视觉保真度。将视频分区为片段供局部预算 agent 处理，通过 agent 原生潜在通信协议实现整体推理。每个 agent 将部分观测编码为共享嵌入空间中的紧凑、任务充分 token，由中央协调器实现高效且信息保持的协作。课程训练策略渐进强制语义对齐、证据摘要和跨 agent 协调。

## 关键贡献
- 解耦 per-agent 感知预算与全局视频复杂度
- Agent 原生潜在通信协议：紧凑 task-sufficient tokens in shared embedding space
- 课程训练：语义对齐→证据摘要→跨 agent 协调

## 关键引用
> "MACF partitions videos into segments for locally budgeted agents and enables holistic reasoning via an agent-native latent communication protocol."

## 关联
- [[MultiAgentLongContext]] — 多智能体处理长视频上下文
- [[LatentAgentCommunication]] — 潜在智能体通信
- [[BudgetDecoupling]] — 预算解耦范式

## 矛盾
- (暂无)
