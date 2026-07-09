---
title: 'VeriCache: 无损 KV 缓存压缩'
type: source
tags:
- cache-reuse
- kv-cache
- lossless-compression
- speculative-decoding
sources:
- vericache-lossless-compression
source_file: raw/papers/vericache-lossless-compression.pdf
last_updated: 2026-07-09
arxiv_id: '2605.17613'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
KV cache 大小是长上下文服务的主要瓶颈。token 丢弃和量化等压缩方法本质上是有损的——短输出时精度降低小，但随着解码更多 token，输出与全 KV cache 输出越来越发散，导致代码生成和工具调用灾难性失败。VeriCache 是首个确保与全 KV cache 解码相同输出但大幅保留压缩算法高吞吐的推理框架。

## 关键贡献
- 首个确保与全 KV cache 解码完全相同输出的压缩框架
- 用压缩 KV cache 草拟 token，再用全 KV cache 验证
- 4x 吞吐提升，输出完全相同
- 解决代码生成和工具调用的灾难性失败问题

## 方法细节
- **草拟-验证范式**：
  - 草拟阶段：用压缩 KV cache（如 token 丢弃后）快速生成候选 token
  - 验证阶段：用全 KV cache 验证候选 token 是否正确——如果正确则接受，如果错误则用全 KV cache 重新生成
- **系统挑战**：全 KV cache 留在 GPU 内存外（CPU/SSD），需要最小化换入验证的开销
- **两个关键洞察**：
  - (1) **并行执行**：压缩 KV 解码（HBM 带宽受限）可与全 KV 换入（PCIe/网络受限）并行——两个操作使用不同资源，不互相阻塞
  - (2) **长草拟范围**：压缩 KV 常产生类似全 KV 的输出——允许长草拟范围，一次换入验证多个 token，摊销换入成本
- **无损保证**：验证阶段确保最终输出与全 KV cache 完全相同——不存在精度损失

## 关键引用
> "VeriCache drafts with compressed KV and verifies with full KV — output is identical to full-cache decoding, with 4x throughput."

## 关联
- [[CacheReuse]] — 缓存复用方向
- [[KVPolicy]] — KVPolicy 做有损淘汰，VeriCache 做无损压缩
- [[SAECache]] — SAECache 做淘汰策略，VeriCache 做压缩+验证
- [[SpeculativeDecoding]] — VeriCache 借鉴推测解码的草拟-验证范式

## 矛盾
- 与"压缩必然有损"的矛盾：VeriCache 通过草拟-验证范式实现无损压缩
