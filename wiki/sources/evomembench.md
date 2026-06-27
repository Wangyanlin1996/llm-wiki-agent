---
title: 'EvoMemBench: 自演化视角的Agent记忆评测基准'
type: source
tags:
- agent-memory
sources:
- evomembench
source_file: raw/papers/evomembench.pdf
last_updated: 2026-06-04
arxiv_id: '2605.18421'
authors:
- Yuyao Wang
- Zhongjian Zhang
- Mo Chi
- Kaichi Yu
- Yuhan Li
- Miao Peng
- Bing Tong
- Chen Zhang
- Yan Zhou
- Jia Li
year: 2026
venue: arXiv
citation_count: 0
---
## 概要
EvoMemBench 从自演化视角评测Agent记忆，双轴设计：记忆范围（in-episode vs cross-episode）× 记忆内容（knowledge-oriented vs execution-oriented）。15种代表性记忆方法对比强长上下文基线。结论：当前记忆系统远非通用解——长上下文基线仍竞争力强；检索式在知识密集场景占优；程序性+长期记忆在执行导向任务更有效；无单一记忆形式在所有设置下一致有效。

## 关键贡献
- 双轴评测框架：记忆范围 × 记忆内容
- 15种记忆方法的统一协议对比
- 长上下文基线仍然竞争力强的发现
- 不同记忆形式在不同场景下的有效性分析
- 程序性记忆在执行导向任务的独特优势验证

## 关键引用
> "current memory systems are still far from a general solution" — 核心发现

## 关联
- [[AgentMemory]] — 记忆评测的分类学框架
- [[EvoMemory]] — 同为自演化视角，EvoMemBench是Evo-Memory的评测扩展
- [[Memp]] — 程序性记忆在EvoMemBench中验证了执行导向任务的有效性
- [[MemGym]] — 同为长程记忆评测，但EvoMemBench更系统化（双轴×15方法）

## 矛盾
- 发现长上下文基线仍然竞争力强——与记忆系统必要性假设的张力