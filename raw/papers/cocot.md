---
title: "Cognitive Chain-of-Thought (CoCoT): Structured Multimodal Reasoning about Social Situations"
type: paper
tags: [cognitive-reasoning, multimodal, theory-of-mind, social-reasoning, intent-disambiguation, VLM]
authors: [Eunkyu Park, Wesley Hanwen Deng, Gunhee Kim, Motahhare Eslami, Maarten Sap]
year: 2025
venue: null
citation_count: null
arxiv_id: "2507.20409"
doi: "10.48550/arXiv.2507.20409"
pdf_url: "https://arxiv.org/pdf/2507.20409"
sub_area: intent-understanding
---

## 概要
提出认知 grounded 三阶段推理框架 CoCoT（Perception→Situation→Norm），将视觉语言模型的多模态社会推理结构化，在意图消歧、Theory of Mind、社会常识推理和安全指令遵循等多个任务上平均提升 5-6%，SFT 后模型内化推理模式无需显式 CoCoT 提示。

## 核心贡献
- 设计认知 grounded 三阶段推理框架：Perception（提取接地事实）→ Situation（推断情境）→ Norm（应用社会规范）
- 在多模态意图消歧、多模态 Theory of Mind、社会常识推理、安全指令遵循四个任务上实现 5-6% 的平均提升
- 验证 SFT 训练使模型内化 CoCoT 结构化推理模式（5-6% 提升），推理时无需显式 CoCoT 提示