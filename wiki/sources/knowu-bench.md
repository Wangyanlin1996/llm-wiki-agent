---
title: 'KnowU-Bench: 交互式主动个性化移动Agent评测'
type: source
tags:
- intent-understanding
sources:
- knowu-bench
source_file: raw/papers/knowu-bench.pdf
last_updated: 2026-06-04
arxiv_id: '2604.08455'
authors:
- Tongbo Chen
- Zhengxi Lu
- Zhan Xu
- Guocheng Shao
- Shaohan Zhao
- Fei Tang
- Yong Du
- Kaitao Song
- Yizhou Liu
- Yuchen Yan
- Wenqi Zhang
- Xu Tan
- Weiming Lu
- Jun Xiao
- Yueting Zhuang
- Yongliang Shen
year: 2026
venue: arXiv
citation_count: 0
---
## 概要
KnowU-Bench 是交互式+主动性+个性化移动Agent评测基准，42通用+86个性化+64主动性任务。隐藏用户画像仅暴露行为日志，强制真正的偏好推断而非上下文查找。LLM驱动用户模拟器支持多轮偏好获取和主动同意处理。Claude Sonnet 4.6在模糊指令下低于50%，核心瓶颈不是GUI导航而是偏好获取和干预校准。

## 关键贡献
- 交互式+主动性+个性化三维度评测——从静态偏好恢复到动态偏好获取
- 隐藏画像+行为日志——强制真正推断而非上下文查找
- LLM驱动用户模拟器——多轮偏好获取+同意协商
- 主动决策链评测：GUI执行+同意协商+拒绝后克制
- 发现前沿模型在偏好获取和干预校准上严重不足

## 关键引用
> "agents that excel at explicit task execution fall below 50% under vague instructions requiring user preference inference or intervention calibration" — 核心发现

## 关联
- [[IntentUnderstanding]] — 偏好推断作为意图理解的子任务
- [[IntentRecommendation]] — 主动干预+同意协商+拒绝后克制
- [[PIRF]] — 同为GUI上的主动意图推荐，但KnowU-Bench扩展到同意协商
- [[VitaBench2]] — 同为个性化评测，但KnowU-Bench更强交互性要求

## 矛盾
- 前沿模型擅长GUI导航但不擅长偏好获取——能力分层断裂