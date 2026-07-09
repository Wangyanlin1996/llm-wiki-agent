---
title: 'SPEAR: 代码增强的 Agent 式 Prompt 优化'
type: source
tags:
- prompt-optimization
- code-act
- error-analysis
sources:
- spear-code-augmented-prompt
source_file: raw/papers/spear-code-augmented-prompt.pdf
last_updated: 2026-07-09
arxiv_id: '2605.26275'
authors:
- et al.
year: 2026
venue: EMNLP 2026 submission
citation_count: 0
---
## 概要
现有 APE 循环将优化器自身视为固定管线，无法做结构化错误分析。SPEAR 将 CodeAct 的 code-as-action 范式移植到 APE——优化器是一个自由形式 agent，有四个工具（evaluate、python、set_prompt、finish），自主决定如何何时使用。

## 关键贡献
- 将 CodeAct 范式引入 prompt 优化——优化器本身是一个 agent
- Python sandbox 工具使优化器自行做结构化错误分析（混淆矩阵、错误聚类、分组指标）
- 两个护栏使长时程 agent 成为单调改进优化器：指标回退自动回滚 + guard metric 下限
- 13 个工业 LLM-as-judge 任务全胜，BBH-7 平均 0.938 vs GEPA 0.628

## 方法细节
- **四个工具**：
  - `evaluate`：评估当前 prompt 在数据集上的表现
  - `python`：在当前评估 DataFrame 上执行任意 Python 代码，做结构化错误分析
  - `set_prompt`：更新当前 prompt
  - `finish`：终止优化
- **结构化错误分析**：优化器自行编写 Python 代码生成混淆矩阵、错误聚类、分组指标——从数据中提取 prompt 改进方向
- **指标回退护栏**：如果新 prompt 的指标低于上一版，自动回滚
- **Guard metric 护栏**：可选设置 guard metric 下限，防止在优化主指标时损害其他指标

## 关键引用
> "SPEAR is a free-form agentic optimizer with four tools — it autonomously decides how and when to use each, including writing Python for structured error analysis."

## 关联
- [[PromptOptimization]] — Prompt 优化方向
- [[APEX]] — APEX 优化数据选择，SPEAR 优化优化器自身的 agent 化
- [[PromptCodebooks]] — PCO 优化 prompt 结构，SPEAR 优化优化流程

## 矛盾
- 与"固定管线优化器"的矛盾：SPEAR 表明 agent 式优化器能做更深入的错误分析
