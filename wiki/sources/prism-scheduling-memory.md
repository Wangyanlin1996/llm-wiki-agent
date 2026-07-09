---
title: 'PRISM: 调度-内存协同设计'
type: source
tags:
- cache-reuse
- kv-cache
- scheduling-memory-codesign
- ttft-optimization
sources:
- prism-scheduling-memory
source_file: raw/papers/prism-scheduling-memory.pdf
last_updated: 2026-07-09
arxiv_id: '2605.08581'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
现代在线 LLM 服务（RAG、agent）暴露两个特征：prompt 分段（系统指令、检索段落、工具输出）和热点偏斜（少量段跨请求频繁出现）。现有工作独立处理——KV cache 管理利用段复用，调度重排请求改善缓存局部性——但两者不对齐。PRISM 联合设计查询感知调度器 (QAS) 和需求感知 radix tree (DART)。

## 关键贡献
- 联合设计调度器（QAS）和 KV 管理（DART）——对齐请求接入与精确前缀 KV 保留
- 分析调度与 KV 管理如何联合影响 TTFT
- 4B/13B 模型上 P99 TTFT 降 23.3%/37.1%
- 精确前缀 KV 命中率 +5.9/12.2pp

## 方法细节
- **问题分析**：调度器重排请求改善缓存局部性，但如果不与 KV 管理对齐——重排后的请求可能发现需要的 KV 已被淘汰；KV 管理保留热点段，但如果不与调度对齐——保留的段可能不被即将到来的请求使用
- **QAS (Query-Aware Scheduler)**：调度器感知查询内容——将共享前缀的请求分批执行，最大化缓存命中
- **DART (Demand-Aware Radix Tree)**：radix tree 感知调度意图——根据调度器的未来计划保留即将被使用的 KV 段，淘汰不会被使用的段
- **协同机制**：QAS 告知 DART 即将到来的请求模式→DART 据此调整保留策略→DART 的保留状态反馈给 QAS 优化调度

## 关键引用
> "PRISM aligns request admission with exact-prefix KV retention — scheduling and KV management must be co-designed."

## 关联
- [[CacheReuse]] — 缓存复用方向
- [[SAECache]] — SAECache 做淘汰策略，PRISM 做调度-内存协同
- [[SAGA]] — SAGA 做工作流调度，PRISM 做调度-缓存协同
- [[StatefulInference]] — StatefulInference 做跨轮 KV 复用，PRISM 做调度-缓存对齐

## 矛盾
- 与"调度和缓存独立优化"的矛盾：PRISM 表明协同设计才能最大化收益
