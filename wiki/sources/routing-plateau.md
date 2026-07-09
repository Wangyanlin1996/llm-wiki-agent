---
title: 'The Routing Plateau: 路由准确率上限研究'
type: source
tags:
- model-routing
- routing-plateau
- predictability-bottleneck
- empirical-study
sources:
- routing-plateau
source_file: raw/papers/routing-plateau.pdf
last_updated: 2026-07-09
arxiv_id: '2606.07587'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
LLM 路由通过动态选模型改善成本-质量 tradeoff，方法涵盖聚类路由、学习分类器、pairwise ranking、置信度方法。但路由准确率是否存在上限？本文对 21 种路由方法×5 个基准进行广泛研究，发现一致性现象"routing plateau"——许多方法达到非常相似的准确率，收敛到远低于 oracle 路由的窄性能范围。

## 关键贡献
- 21 种路由方法×5 个基准的广泛实证研究
- 发现"routing plateau"现象——多种方法收敛到相似的窄性能范围
- 调查 plateau 的根因：可预测性瓶颈
- 路由器主要学习全局平均模型性能趋势而非细粒度查询特定路由信号
- 提出突破方向：更大训练数据、更强编码器、端到端微调

## 方法细节
- **实验设计**：21 种路由方法覆盖主要范式——聚类路由、学习分类器、pairwise ranking、置信度方法；5 个基准覆盖不同任务类型
- **Routing Plateau 现象**：无论用什么方法（从简单 kNN 到复杂学习分类器），路由准确率都收敛到相似的窄范围——远低于 oracle 路由（总是选最佳模型）的上限
- **根因分析**：
  - 路由器主要学习全局平均模型性能趋势——"模型 A 平均比模型 B 好"
  - 而非细粒度查询特定路由信号——"这个特定查询应该路由到模型 A 还是 B"
  - 结果：简单查询（所有模型都能答对/都答错）路由器表现好；困难查询（需要实例特定路由决策）路由器集体失败
- **突破方向**：
  - 更大训练数据——当前数据量不足以学习细粒度路由信号
  - 更强编码器——当前查询编码器不能提取足够的路由判别特征
  - 端到端微调——而非两阶段（先训练分类器再路由）

## 关键引用
> "The routing plateau is primarily caused by a predictability bottleneck — routers learn global average model performance trends rather than fine-grained query-specific routing signals."

## 关联
- [[ModelRouting]] — 模型动态路由方向
- [[HyDRA]] — HyDRA 是突破 plateau 的方向之一（多维能力匹配）
- [[ReCal]] — ReCal 优化 RL 路由的奖励校准，可能帮助突破 plateau
- [[TwinRouterBench]] — TwinRouterBench 提供步级路由评估，可能暴露更多路由信号

## 矛盾
- 与"更复杂的路由方法更好"的矛盾：Plateau 表明简单 kNN 和复杂分类器达到相似准确率
