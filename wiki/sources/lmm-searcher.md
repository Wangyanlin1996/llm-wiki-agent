---
title: "LMM-Searcher：长程智能体多模态搜索"
type: source
tags: [multi-agent-long-context]
sources: [lmm-searcher]
source_file: raw/papers/lmm-searcher.pdf
last_updated: 2026-07-24
arxiv_id: "2604.12890"
authors: ["Yifan Du", "Zikang Liu", "Jin Peng", "Jie Wu", "J. Li", "Jinyang Li", "W. Zhao", "Ji-Rong Wen"]
year: 2026
venue: "arXiv.org"
citation_count: 4
doi: "10.48550/arXiv.2604.12890"
---

## 概要
LMM-Searcher 提出基于文件的视觉表示机制，将视觉资产卸载到外部文件系统并映射为轻量级文本标识符 (UID)，缓解上下文开销同时保留多模态信息。配备定制的 fetch-image 工具实现渐进式按需视觉加载。引入数据合成管线生成需要跨模态多跳推理的复杂查询，蒸馏 12K 高质量轨迹微调。成功扩展到 100-turn 搜索 horizon，在 MM-BrowseComp 和 MMSearch-Plus 上达到 SOTA。

## 关键贡献
- 文件化视觉表示：UID 映射 + 按需 fetch-image 工具
- 缓解多模态长程搜索的上下文爆炸
- 100-turn 搜索 horizon，开源 SOTA

## 关键引用
> "By offloading visual assets to an external file system and mapping them to lightweight textual identifiers (UIDs), our approach mitigates context overhead while preserving multimodal information for future access."

## 关联
- [[MultiAgentLongContext]] — 长程多模态搜索的上下文管理
- [[FileBasedRepresentation]] — 文件化表示替代上下文内 token
- [[WebSwarm]] — WebSwarm 也解决长搜索轨迹问题

## 矛盾
- (暂无)
