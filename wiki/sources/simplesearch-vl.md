---
title: "SimpleSearch-VL：多模态 Agentic 深度搜索的简单配方"
type: source
tags: ['semantic-retrieval', 'agentic-retrieval', 'multimodal']
sources: [simplesearch-vl]
source_file: raw/papers/simplesearch-vl.pdf
last_updated: 2026-07-02
arxiv_id: "2606.31504"
authors: ["Ming Dai", "Zhihong Lu", "Jinjie Gu", "Jiedong Zhuang", "Yefeng Liu", "Wankou Yang", "Jian Wang", "Chunhua Shen"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要

多模态 agentic 搜索将 LLM 从被动响应推进到主动证据获取，但在高效、可靠、实用三方面仍难。效率受限于长尾 rollout 生成——多轮外部搜索与网页访问使少量样本占用大部分训练时间，固定预算无法自适应终止已有奖励变化的提示或为缺乏信号的困难提示重新分配尝试。可靠性要求跨源跨模态的可核查证据，因为检索到的文本/网页/图像搜索标题与 URL 可能看似合理实则不支持或失配。实用性倾向避免复杂工具编排与多余模型依赖的可复现系统。本文提出 **SimpleSearch-VL**，核心思路是改进 agent 自身的搜索-验证过程而非扩展数据/工具/辅助组件：(1) **Factorized Adaptive Rollout（FAR）**——将提示扩展（信号不足时引入新提示组）与 rollout 分配（为缺乏奖励对比的组增加尝试、信号充足时跳过冗余尾部）两个预算维度结合，把固定预算 rollout 变为信号感知分配；(2) **证据验证推理**——image_search 返回缩略图/标题/源 URL，agent 用链式思维验证候选是否匹配查询视觉内容后再使用其证据，使检索视觉证据直接可核查；(3) **解耦证据动作 + 网页自摘要**——每步模型决定访问哪些链接并对多图输入决定哪张图/区域作为反向图搜查询，网页访问后由 agent 自身做目标条件摘要无需外部摘要模型。仅 5K 监督工具交错轨迹 + 2K RL 数据，Qwen3-VL 8B/30B-A3B 分别提升 15.8/16.0 平均分，30B-A3B 与 agentic Gemini-3-Pro 竞争力相当。

## 关键贡献

- **Factorized Adaptive Rollout（FAR）**：提示扩展 + rollout 分配双维度信号感知分配，在保持有用信号密度的同时缓解长尾延迟并暴露困难样本，不增加系统复杂度
- **缩略图感知的视觉证据验证**：反向图搜返回缩略图供一致性核查，使 agent 在使用标题/URL/网页证据前验证候选是否匹配查询视觉内容，token 开销极小
- **解耦证据动作 + agent 内网页自摘要**：每步由模型决定访问链接与反向图搜查询区域，网页访问后目标条件自摘要消除外部摘要模型依赖

## 关键引用

> "Its core idea is to improve the agent's own search-and-verification process rather than scaling data, tools, or auxiliary model components."

## 关联

- [[AgenticRetrieval]] — 本文是该概念在多模态搜索场景的高效实用实现，证明改进搜索-验证过程优于扩展数据/工具
- [[RetrievalAugmentedGeneration]] — 证据验证推理与 agent 内网页自摘要直接提升多模态 RAG 的可靠性与实用性

## 矛盾

无已知矛盾。
