---
title: "Flexible Agent Alignment with Goal Inference from Open-Ended Dialog"
type: paper
tags: [assistance-games, goal-inference, agent-alignment, preference-construction, LLM-agent]
authors: [Rachel Ma, Jingyi Qu, Andreea Bobu, Dylan Hadfield-Menell]
year: 2025
venue: null
citation_count: null
arxiv_id: "2508.15119"
doi: "10.48550/arXiv.2508.15119"
pdf_url: "https://arxiv.org/pdf/2508.15119"
sub_area: intent-understanding
---

## 概要
将 Assistance Games 扩展到开放世界 LLM Agent 场景，提出 Open-Universe Assistance Games (OU-AGs) 框架与 GOOD 方法：从开放对话中提取并排序候选目标，使用 LLM 模拟用户进行概率推断，实现可解释、不确定性感知的偏好表示，无需大规模离线数据集。

## 核心贡献
- 提出 Open-Universe Assistance Games (OU-AGs)，将传统 Assistance Games 从固定预设偏好扩展到自然语言表达的动态偏好分布
- 设计 GOOD 方法，在交互过程中从对话提取候选目标并排序，利用 LLM 模拟用户进行概率推断
- 在三个文本领域（购物、家居机器人 AI2-THOR、编程）评测，相比无显式目标追踪的基线，GOOD 产生语义连贯的目标表示并显著改善用户意图对齐