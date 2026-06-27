---
title: 'Mem-π: 自适应记忆——学习何时生成与生成什么'
type: source
tags:
- agent-memory
sources:
- mempi
source_file: raw/papers/mempi.pdf
last_updated: 2026-06-04
arxiv_id: '2605.21463'
authors:
- Xiaoqiang Wang
- Chao Wang
- Hadi Nekoei
- Christopher Pal
- Alexandre Lacoste
- Spandana Gella
- Bang Liu
- Perouz Taslakian
year: 2026
venue: Work in Progress
citation_count: 0
---
## 概要
Mem-π 提出自适应记忆框架：不再从外部记忆库检索静态条目，而是用独立参数的专用模型按需生成上下文特定指导。决策-内容解耦RL目标使其能决定何时产生指导（不帮助时放弃）和生成什么指导（简洁有用）。web navigation >30%相对提升，优于检索式和RL优化记忆基线。

## 关键贡献
- 检索→生成的范式转换——不再检索静态条目而是按需生成指导
- 决策-内容解耦RL目标——jointly decide when & what to generate
- 专用语言/视觉语言模型作为记忆生成器
- 多种Agent基准评测（web navigation, terminal tool use, embodied interaction）
- >30%相对提升超越检索式基线

## 关键引用
> "useful guidance is generated on demand rather than retrieved from external memory stores" — 核心范式转换

## 关联
- [[AgentMemory]] — 从检索到生成的范式转换
- [[MemCog]] — 记忆即认知——Mem-π的生成式记忆是最强的认知实现
- [[Memp]] — 同为按需而非静态检索，但Memp是脚本蒸馏而Mem-π是RL生成
- [[LightMem]] — SLM驱动的压缩记忆 vs Mem-π的RL生成记忆

## 矛盾
- 与所有检索式记忆方法的根本矛盾——静态检索无法对齐当前上下文