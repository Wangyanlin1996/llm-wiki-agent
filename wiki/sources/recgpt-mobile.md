---
title: RecGPT-Mobile：端侧LLM意图理解Agent（KDD 2026）
type: source
tags:
- intent-recommendation
sources:
- recgpt-mobile
source_file: raw/papers/recgpt-mobile.pdf
last_updated: 2026-06-08
arxiv_id: '2605.04726'
authors:
- Bin Zhang
- Weipeng Huang
- Dimin Wang
- Jialin Zhu
- Yuning Jiang
- Zhaode Wang
- Chengfei Lv
- Jian Wang
- Qichao Ma
- Li Chen
- Junqing Wu
- Yipeng Yu
year: 2026
venue: KDD 2026
---
## 概要
RecGPT-Mobile 提出端侧轻量 LLM 意图理解 Agent，用于移动电商场景的下一查询预测。将 LLM 直接部署在移动设备上，更快捕获用户演化兴趣并实时调整推荐结果。淘宝大规模离线分析和在线实验验证显著提升推荐准确率，为生产级移动推荐系统的 LLM 集成提供可行路径。

## 关键贡献
- 端侧 LLM 部署：解决云端推理成本问题
- 实时演化兴趣捕获：从云端批量→端侧实时
- 电商验证：淘宝生产环境大规模实验

## 关键引用
> "Capture evolving interests of users more quickly and adjust the recommendation results in real time" — 端侧优势

## 关联
- [[IntentRecommendation]] — RecGPT-Mobile 是 IR 在工业场景的具体实现
- [[AgentMemory]] — 端侧 LLM 记忆用户演化兴趣，与 [[LightMem]] 的 SLM 驱动方向一致
- [[CrossFrameworkMemorySharing]] — RecGPT-Mobile 单设备端侧记忆 vs Agent KB 跨框架共享

## 矛盾
- 端侧 LLM 资源受限 vs 云端大模型推理能力——RecGPT-Mobile 的轻量设计可能在意图复杂性高的场景受限