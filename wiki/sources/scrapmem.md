---
title: ScrapMem：生物启发光学遗忘与端侧记忆
type: source
tags:
- agent-memory
sources:
- scrapmem
source_file: raw/papers/scrapmem.pdf
last_updated: 2026-06-08
arxiv_id: '2605.03804'
authors:
- Jiale Chang
- Yuxiang Ren
year: 2026
---
## 概要
ScrapMem 提出生物启发的端侧个性化记忆框架，将多模态数据整合为"剪贴簿页面"（Scrapbook Page）。引入光学遗忘（Optical Forgetting）机制，渐进降低旧记忆分辨率以节省存储同时抑制低价值细节；构建情景记忆图（EM-Graph）以因果时序结构组织关键事件。在 ATM-Bench 达 SOTA 51.0% Joint@10，存储节省 93%。

## 关键贡献
- 光学遗忘：将记忆压缩类比光学降分辨率，保留高层语义同时丢弃低层细节
- 情景记忆图（EM-Graph）：因果时序结构保持语义一致性
- 端侧效率：93% 存储节省 + SOTA 性能，适合资源受限设备

## 关键引用
> "Optical Forgetting progressively reduces the resolution of older memories, lowering storage cost while suppressing low-value details" — 遗忘不是删除而是降精度

## 关联
- [[OpticalMemoryEncoding]] — OCR-Memory 用视觉编码高密度存储，ScrapMem 用光学遗忘降低分辨率——同一视觉通道的不同利用策略
- [[AgentMemory]] — 光学遗忘补充了 Storage→Reflection→Experience 的遗忘维度
- [[ParametricMemory]] — ScrapMem 保持外部存储但降低精度，PEAM 将记忆参数化内化

## 矛盾
- 光学遗忘的"降分辨率"与 [[EvoMemBench]] 发现的"长上下文仍竞争力强"似乎矛盾——但 ScrapMem 的降分辨率保留了关键语义而非随机截断