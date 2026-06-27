---
title: 贝叶斯社交推理：Agent击败人类（ACL 2026）
type: source
tags:
- intent-understanding
sources:
- bayesian-social-deduction
source_file: raw/papers/bayesian-social-deduction.pdf
last_updated: 2026-06-08
arxiv_id: '2506.17788'
authors:
- Shahab Rahimirad
- Guven Gergerli
- Lucia Romero
- Angela Qian
- Matthew Lyle Olson
- Simon Stepputtis
- Joseph Campbell
year: 2025
venue: ACL 2026
---
## 概要
贝叶斯社交推理框架将信念推断外化到结构化概率模型，LLM 负责语言理解与交互。在社交推理游戏 Avalon 中，混合框架在小模型上达到与大模型相当的性能。首个语言 Agent 在控制实验中击败人类玩家（67% 胜率），并获得比推理基线和人类队友更高的定性评价。

## 关键贡献
- 贝叶斯+LLM 混合推理：概率模型外化信念推断，LLM 处理语言交互
- 首个 Agent 击败人类：67% 胜率，定性评分高于人类队友
- 模型蒸馏问题：大模型推理需大量 test-time 计算，蒸馏到小模型性能急剧下降

## 关键引用
> "The first language agent to defeat human players in a controlled study" — 里程碑成果

## 关联
- [[IntentUnderstanding]] — 社交推理是 IU 的多人博弈扩展：推断他人隐藏意图
- [[IntentSignalTheory]] — Avalon 中 I*（真实角色）不可直接观测，贝叶斯推断提供概率化 I-hat
- [[AssistanceGames]] — 贝叶斯社交推理与 Assistance Games 的开放世界目标推断有关联

## 矛盾
- 贝叶斯框架在 Agent-Agent 对战中成功，但蒸馏到小模型后性能下降——说明显式概率推断需要足够推理能力