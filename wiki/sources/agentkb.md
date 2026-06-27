---
title: 'Agent KB: 跨域经验共享的Agent知识库'
type: source
tags:
- agent-memory
sources:
- agentkb
source_file: raw/papers/agentkb.pdf
last_updated: 2026-06-04
arxiv_id: '2507.06229'
authors:
- Xiangru Tang
- Tianrui Qin
- Tianhao Peng
- Ziyang Zhou
- Daniel Shao
- Tingting Du
- Xinming Wei
- Peng Xia
- Fang Wu
- He Zhu
- Ge Zhang
- Jiaheng Liu
- Xingyao Wang
- Sirui Hong
- Chenglin Wu
- Hao Cheng
- Chi Wang
- Wangchunshu Zhou
year: 2025
venue: arXiv
citation_count: 53
---
## 概要
Agent KB 提出跨框架共享记忆基础设施，让异构Agent框架无需重训即可共享经验。将轨迹聚合为结构化知识库，提供轻量API；推理时两阶段混合检索：planning seeds 注入跨域工作流 + feedback 应用定向诊断修复；disagreement gate 确保检索知识增强而非干扰推理。smolagents+18.7pp，OpenHands SWE-bench+4.0pp。

## 关键贡献
- 跨框架共享记忆基础设施——无需重训的集体智能
- planning seeds + feedback diagnostic fixes 两阶段混合检索
- disagreement gate 防止知识干扰
- GAIA/HLE/GPQA/SWE-bench四基准评测，多模型家族一致改善
- 自动生成的经验与人工策划质量相当

## 关键引用
> "This establishes the foundation for collective agent intelligence through shared memory infrastructures" — 集体智能愿景

## 关联
- [[AgentMemory]] — 从单Agent记忆扩展到多Agent共享记忆
- [[Memp]] — 同为经验内化，但Agent KB是跨框架共享而非单Agent内化
- [[EvoMemory]] — 同为经验检索，但Agent KB是结构化知识库而非流式基准

## 矛盾
- 跨框架共享可能引入知识干扰——disagreement gate正是为此设计