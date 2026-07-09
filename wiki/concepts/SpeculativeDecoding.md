---
title: "推测解码（Speculative Decoding）"
type: concept
tags: ['speculative-decoding', 'inference-acceleration', 'draft-verify']
sources: ["cross-family-speculative-prefill", "vericache-lossless-compression"]
last_updated: 2026-07-09
---

推测解码通过"小模型草拟+大模型验证"范式加速 LLM 推理，核心思想是用低成本草拟生成候选 token，再用高成本验证确认，接受正确部分。

**两种扩展应用**：
1. **推测式预填充** — [[CrossFamilySpeculativePrefill]] 将推测思想从解码扩展到预填充：用轻量 draft 模型估计 token 重要性做 prompt 压缩，发现注意力估计可跨模型族迁移，免训练压缩保留 90-100% 性能。
2. **无损缓存压缩** — [[VeriCache]] 将推测思想用于 KV cache 压缩：用压缩 KV 草拟 token，用全 KV 验证。关键洞察：(1) 压缩 KV 解码与全 KV 换入可并行（不同资源瓶颈）；(2) 压缩 KV 常产生类似全 KV 输出，允许长草拟范围摊销换入成本。4x 吞吐提升，输出完全相同。

**共同范式**：草拟-验证（draft-verify）——低成本操作生成候选，高成本操作验证确认，利用两者的资源互补性实现无损加速。
