---
title: "TEP：深度复合 AI 系统的文本平衡传播"
type: source
tags: [multi-agent-long-context]
sources: [tep-textual-equilibrium]
source_file: raw/papers/tep-textual-equilibrium.pdf
last_updated: 2026-07-24
arxiv_id: "2601.21064"
authors: ["Minghui Chen", "Wenlong Deng", "James Zou", "Han Yu", "Xiaoxiao Li"]
year: 2026
venue: "arXiv.org"
citation_count: 1
doi: "10.48550/arXiv.2601.21064"
---

## 概要
TEP 针对长程 agentic 工作流的两种深度扩展失效模式：(1) textual gradient 爆炸——文本反馈随深度指数增长；(2) textual gradient 消失——有限长上下文能力导致模型过度强调部分反馈。提出平衡传播 (TEP)：free phase 中局部 LLM critics 迭代精炼 prompt 直至平衡；nudged phase 中应用有界修改强度的近端 prompt 编辑，通过前向信号而非反向反馈链传播任务级目标。在长程 QA 和多智能体工具使用数据集上持续提升准确率和效率。发表于 ICLR 2026。

## 关键贡献
- 识别深度复合 AI 的两种失效：textual gradient 爆炸/消失
- 平衡传播两阶段：free phase (局部 critic 迭代) + nudged phase (前向信号传播)
- ICLR 2026，深度越深增益越大

## 关键引用
> "Long-horizon agentic workflows exhibit two depth-scaling failure modes: exploding textual gradient, where textual feedback grows exponentially with depth, and vanishing textual gradient, where limited long-context ability causes models overemphasize partial feedback."

## 关联
- [[MultiAgentLongContext]] — 深度复合 AI 系统的长程工作流优化
- [[TextualGradientFailure]] — 文本梯度失效模式
- [[EquilibriumPropagation]] — 平衡传播原理

## 矛盾
- (暂无)
