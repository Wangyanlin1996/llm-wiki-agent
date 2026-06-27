---
title: 'SII/PIWM: 看-推断-干预——目标导向社会智能的主动世界建模'
type: source
tags:
- intent-understanding
sources:
- sii-piwm
source_file: raw/papers/sii-piwm.pdf
last_updated: 2026-06-04
arxiv_id: '2606.03371'
authors:
- Honghui Zhang
- Chenmeinian Guo
- Yichen Yu
- Guanyu Liu
- Yongming Qin
- Chongguo Song
- Mengyue Yang
- Lei Yu
- Tianyu Shi
year: 2026
venue: Preprint
citation_count: 0
---
## 概要
SII框架提出看-推断-干预三阶段主动意图理解流程，PIWM用AIDA购买阶段+BDI心理场表示客户状态，预测行为条件意图转移，从五类响应中选择干预或等待。构建GuidanceSalesBench智能零售基准。ground-truth state条件下0.641 macro F1，端到端视频仅0.295（低于随机基线），揭示video-to-state grounding是部署瓶颈。

## 关键贡献
- See-Infer-Intervene三阶段框架——看前交互行为→推断潜在意图→选择干预方式
- AIDA+BDI双重状态表示——购买阶段与心理场结合
- 五类响应策略（Greet/Elicit/Inform/Recommend/Hold）包括"等待"选项
- GuidanceSalesBench智能零售基准
- 发现video-to-state grounding是部署瓶颈

## 关键引用
> "a device must see pre-interaction behavior, infer latent customer intent, and act by selecting an appropriate service intervention or choosing to wait" — SII核心流程

## 关联
- [[IntentUnderstanding]] — 从意图检测到意图推断+干预决策
- [[IntentSignalTheory]] — I*→I-hat推断在零售场景的具体实现
- [[ContextAgent]] — 同为感官驱动的主动意图理解，但SII在零售场景
- [[Satori]] — 同为BDI建模，但SII在零售+PIWM预测转移

## 矛盾
- 端到端视频仅0.295低于随机——多模态grounding仍是根本瓶颈