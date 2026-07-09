---
title: 'MO-CAPO: 多目标成本感知的 Prompt 优化'
type: source
tags:
- prompt-optimization
- multi-objective
- cost-aware
sources:
- mo-capo-multi-objective
source_file: raw/papers/mo-capo-multi-objective.pdf
last_updated: 2026-07-09
arxiv_id: '2605.18869'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
现有 prompt 优化方法主要只关注性能，忽略推理成本或延迟等竞争目标。已有多目标 prompt 优化依赖现成 NSGA-II，忽视优化效率。MO-CAPO 联合优化性能和推理成本，利用预算分配实现成本高效优化。

## 关键贡献
- 联合优化性能和推理成本——不牺牲部署可行性
- 提出部署导向的成本目标——捕捉 LLM 推理的完整计算特征（不只是 token 数）
- 发现多样化的性能-成本 trade-off 解集（单目标优化器遗漏的）
- 顶尖性能候选仍与单目标解竞争

## 方法细节
- **部署导向成本目标**：不只计算 token 数，而是捕捉 LLM 推理的完整计算特征——包括输入/输出 token 数、推理步数、工具调用次数等
- **预算分配**：将优化预算在性能和成本目标间智能分配，而非均等分配
- **对比实验**：4 个任务×3 个 LLM 上对比 NSGA-II 和单目标优化器
- **结果**：12 个 case 中 8 个的 noisy R2 指标更优，发现单目标优化器遗漏的 trade-off 解

## 关键引用
> "MO-CAPO captures the complete computational profile of LLM inference — not just token count — as the cost objective."

## 关联
- [[PromptOptimization]] — Prompt 优化方向
- [[APEX]] — APEX 优化数据效率，MO-CAPO 优化成本效率
- [[HyDRA]] — HyDRA 做模型路由的成本-质量 trade-off，MO-CAPO 做 prompt 优化的成本-性能 trade-off

## 矛盾
- 与"只优化性能"的矛盾：MO-CAPO 表明忽略成本会导致部署不可行
