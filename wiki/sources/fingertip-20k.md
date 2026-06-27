---
title: FingerTip 20K：主动个性化移动Agent基准（ICLR 2026）
type: source
tags:
- intent-recommendation
sources:
- fingertip-20k
source_file: raw/papers/fingertip-20k.pdf
last_updated: 2026-06-08
arxiv_id: '2507.21071'
authors:
- Qinglong Yang
- Haoming Li
- Haotian Zhao
- Xiaokai Yan
- Jingtao Ding
- Fengli Xu
- Yong Li
year: 2025
venue: ICLR 2026
---
## 概要
FingerTip 20K 收集 20K 独特人类 Android 多步交互演示，包含长期使用中的用户上下文信息。提出两个新赛道：主动任务建议（从环境观察+历史意图分析推荐下一步任务）和个性化任务执行（适配用户操作偏好）。实验揭示现有 Agent 与人类之间存在巨大差距，微调数据能有效利用用户信息。

## 关键贡献
- 20K 真实人类演示：长期使用采集而非合成
- 主动任务建议赛道：从上下文+历史意图预测下一步
- 个性化执行轨迹赛道：不同用户对同一任务的不同操作路径

## 关键引用
> "Proactive task suggestions by analyzing environment observation and users' previous intents" — 从观察推断意图

## 关联
- [[IntentRecommendation]] — FingerTip 20K 的主动任务建议是 IR 在移动场景的具象化
- [[PIRF]] — PIRF 的 GUI 主动意图推荐与 FingerTip 20K 互补
- [[SimulationRealityGap]] — FingerTip 20K 的真实数据与 [[ProCodeBench]] 的真实-合成差距呼应

## 矛盾
- FingerTip 20K 发现微调数据有效利用用户信息，但 [[KnowU-Bench]] 发现 Claude 在模糊指令下<50%——微调与推理能力可能需要双轨提升