---
title: "AAFLOW+：零拷贝分布式 KV Cache 编排的多智能体有状态算子抽象"
type: source
tags: [multi-agent-long-context]
sources: [aaflow-plus]
source_file: raw/papers/aaflow-plus.pdf
last_updated: 2026-07-24
arxiv_id: "2607.10987"
authors: ["A. Sarker", "Alexander James Halpern", "M. Staylor", "Aymen Alsaadi", "G. V. Laszewski", "Yue Cheng", "S. Jha", "Geoffrey C. Fox"]
year: 2026
venue: "arXiv preprint"
citation_count: 1
doi: ""
---

## 概要
AAFLOW+ 将 KV cache 提升为一等分布式系统对象，使多智能体 LLM 系统能够零拷贝复用长上下文而无需重复计算。它构建通信感知图，并发优化数据、prompt 和可复用模型状态，并提供 KV 物化、传输、fork、组合和驱逐算子。TTFT 降低达 50.2x，16-agent 规模下计算成本降低 7.63x，KV 内存减少 1.72-6.10x，吞吐量提升 7.74x+。关键发现：在中等至高带宽网络上，KV 传输优于重新计算。

## 关键贡献
- KV cache 作为一等分布式对象：物化/传输/fork/组合/驱逐算子
- 零拷贝、传输感知执行，agent 间复用长上下文无需重计算
- TTFT -50.2x，计算成本 -7.63x，KV 内存 -1.72~6.10x，吞吐 +7.74x

## 关键引用
> "KV transmission outperforms recomputation on networks with moderate to high bandwidth, making sure KV-state sharing greatly increases efficiency in multi-agent LLM systems by replacing text passing."

## 关联
- [[AgentPrimitives]] — Agent Primitives 也用 KV cache 内部通信
- [[KVCacheSharing]] — 多智能体 KV Cache 共享机制
- [[DistributedAgentInfrastructure]] — 分布式智能体基础设施

## 矛盾
- (暂无)
