---
title: 'PRISM: 迭代模拟的 Prompt 可靠性工程'
type: source
tags:
- prompt-optimization
- reliability-engineering
- behavioral-drift
sources:
- prism-prompt-reliability
source_file: raw/papers/prism-prompt-reliability.pdf
last_updated: 2026-07-09
arxiv_id: '2605.15665'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
企业部署需要 prompt 在发布时正确，且对生产 LLM 非确定性行为漂移有韧性。现有框架将 prompt 质量视为一次性编译时问题，不检测修复 LLM 静默行为变化导致的 prompt 回归。PRISM 将 prompt 工程视为持续可靠性工程问题。

## 关键贡献
- 将 prompt 工程从一次性问题转为持续可靠性工程问题
- 自动从需求生成测试用例，模拟完整多轮对话
- LLM-as-judge 评估 pass/fail，诊断失败根因，外科手术式修复 prompt
- 设计为日常定期运行，将 LLM 行为漂移视为一等可靠性关切
- 35 个企业 agent 三周部署，prompt 编写时间 2 天→30 分钟，99% 生产可靠性，24 小时内检测修复回归

## 方法细节
- **需求→测试用例**：从自然语言 agent 需求自动生成测试用例，覆盖正常路径和边界情况
- **多轮对话模拟**：模拟完整多轮对话，包括工具调用和记忆变量交互
- **LLM-as-judge 评估**：用 LLM 判断每轮对话是否满足需求——pass/fail
- **根因诊断**：失败时分析失败根因——是 prompt 指令不清、上下文不足、还是模型能力限制
- **外科手术式修复**：针对根因做最小化 prompt 修改，而非重写
- **迭代至全通过**：修复后重新评估，迭代直到所有测试用例通过
- **定期运行**：设计为日常定期运行，检测 LLM 行为漂移导致的回归

## 关键引用
> "PRISM treats prompt engineering as continuous reliability engineering — LLM behavioral drift is a first-class reliability concern."

## 关联
- [[PromptOptimization]] — Prompt 优化方向
- [[SPEAR]] — SPEAR 优化 prompt 性能，PRISM 保障 prompt 可靠性
- [[MO-CAPO]] — MO-CAPO 优化成本，PRISM 优化可靠性

## 矛盾
- 与"一次性 prompt 工程"的矛盾：PRISM 表明 LLM 行为漂移需要持续监控
