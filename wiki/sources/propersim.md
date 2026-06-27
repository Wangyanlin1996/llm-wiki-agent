---
title: ProPerSim：主动+个性化推荐仿真（ICLR 2026）
type: source
tags:
- intent-recommendation
sources:
- propersim
source_file: raw/papers/propersim.pdf
last_updated: 2026-06-08
arxiv_id: '2509.21730'
authors:
- Jiho Kim
- Junseong Choi
- Woosog Chay
- Daeun Kyung
- Yeonsu Kwon
- Yohan Jo
- Edward Choi
year: 2025
venue: ICLR 2026
---
## 概要
ProPerSim 首次联合研究主动性和个性化——开发能在适当时机做个性化推荐的家庭助理。仿真环境中，富画像用户 Agent 与助理交互并评分每条建议对偏好和上下文的匹配度。ProPerAssistant 使用检索增强+偏好对齐，通过用户反馈持续学习和适应，32 个多样化画像中稳步提升满意度。

## 关键贡献
- 主动+个性化联合仿真：两个维度同时评测而非单独
- ProPerAssistant：检索增强偏好对齐+持续学习适应
- 32 多样化画像：验证不同用户偏好下的适应能力

## 关键引用
> "While recent advances have pushed forward proactivity and personalization individually, their combination remains underexplored" — 联合研究缺失

## 关联
- [[IntentRecommendation]] — ProPerSim 直接联合 IR 的两个核心维度：主动+个性化
- [[PA-Bridge]] — PA-Bridge 打破回声室，ProPerSim 测评是否真的个性化（而非泛化）
- [[KnowU-Bench]] — KnowU 测评同意协商，ProPerSim 测评满意度——不同评测角度

## 矛盾
- ProPerSim 的仿真环境 vs [[ProAgentBench]] 的真实世界数据——仿真满意度可能无法完全映射到真实满意度