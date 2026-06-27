---
title: Ψ-Bench：主动个性化影响评测
type: source
tags:
- intent-recommendation
sources:
- psi-bench
source_file: raw/papers/psi-bench.pdf
last_updated: 2026-06-08
arxiv_id: '2606.02754'
authors:
- Peixuan Han
- Hongyi Du
- Jiayu Liu
- Yihang Sun
- Yutong Liu
- Jiaxuan You
year: 2026
---
## 概要
Ψ-Bench 首次评测 LLM 的主动个性化影响能力——通过对话影响真实用户。设计三个说服场景，通过对话历史构建客户端画像。10 个前沿 LLM 评测发现：即使 SOTA 模型在说服力方面仍有显著提升空间；提供客户端画像平均+18.24%，证明用户特定信息对有效说服的关键作用。

## 关键贡献
- 主动个性化影响概念：从被动响应到主动说服
- 真实画像驱动：从对话历史推导客户端特征
- 画像信息的关键性：+18.24% 证明用户画像对说服不可或缺

## 关键引用
> "Persona-sensitive influencing as a challenging yet practical direction for evaluating and developing more proactive personalized LLM agents" — 从推荐到影响

## 关联
- [[IntentRecommendation]] — Ψ-Bench 从"推荐意图"升级到"影响意图"——IR 的说服维度扩展
- [[ConversationStarterGeneration]] — IceBreaker 生成开场语，Ψ-Bench 测评后续说服能力
- [[ProactiveInterventionDecisionChain]] — Ψ-Bench 的主动影响与 SII/PIWM 的主动干预决策链形成对比

## 矛盾
- Ψ-Bench 的主动说服与 [[Proactive AI Implications]] 的"主动帮助降低用户能力自尊"形成伦理张力——主动影响需要更严格的伦理边界