---
title: 'HyDRA: 混合动态路由架构'
type: source
tags:
- model-routing
- dynamic-routing
- cost-quality-tradeoff
- heterogeneous-models
sources:
- hydra-dynamic-routing
source_file: raw/papers/hydra-dynamic-routing.pdf
last_updated: 2026-07-09
arxiv_id: '2605.17106'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
生产 LLM 部署维护跨数量级成本差异的异构模型池。现有路由器做二元强 vs 弱决策，且学习参数耦合到特定模型身份——目录变更时需重训。HyDRA 预测每个查询的细粒度多维能力需求，与配置定义的模型 profile 通过 shortfall 匹配。

## 关键贡献
- 预测细粒度多维能力需求（推理、代码生成、调试、工具使用）——而非二元强/弱
- Shortfall 匹配算法选择最便宜的能力满足预测需求的模型
- ModernBERT 编码器 + K=4 独立 sigmoid 头
- 部署在 GitHub Copilot VS Code Chat auto-mode，86ms CPU 推理
- 峰值质量超 Claude Sonnet 4.6（75.4% vs 74.2%）省 12.9%
- Iso-quality 省 54.1%（比先前二元路由 6x 改进）
- 跨 CJK/欧洲/其他脚本系语言不变路由

## 方法细节
- **多维能力评分**：
  - ModernBERT 编码器提取查询特征
  - K=4 独立 sigmoid 头分别评分四个能力维度：推理（reasoning）、代码生成（code generation）、调试（debugging）、工具使用（tool use）
  - 每个头独立输出 0-1 分数——查询可能在代码生成上需要高能力但在推理上只需中等
- **模型 Profile**：每个模型在四个维度上有能力 profile（通过配置定义，非学习得到）——模型目录变更只需更新配置，不需重训路由器
- **Shortfall 匹配**：
  - 对每个候选模型计算 shortfall——模型能力低于查询需求的维度上的差距总和
  - 选择 shortfall=0（能力满足需求）中最便宜的模型
  - 如果没有模型完全满足需求，选择 shortfall 最小的模型
- **解耦设计**：路由器学习的是查询能力需求，与模型身份解耦——添加/移除模型只需更新 profile 配置

## 关键引用
> "HyDRA predicts fine-grained multi-dimensional capability requirements and matches them to model profiles via shortfall — decoupled from model identity."

## 关联
- [[ModelRouting]] — 模型动态路由方向
- [[INFRAMIND]] — INFRAMIND 做基础设施感知路由，HyDRA 做能力感知路由
- [[RoutingPlateau]] — RoutingPlateau 分析路由准确率上限，HyDRA 是突破方向之一
- [[GoodServe]] — GoodServe 做 GPU 路由，HyDRA 做模型路由

## 矛盾
- 与"二元强/弱路由"的矛盾：HyDRA 表明多维能力匹配能 6x 改进成本节省
