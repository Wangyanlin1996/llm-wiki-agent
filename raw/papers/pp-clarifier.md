---
title: "Plug-and-Play Clarifier: A Zero-Shot Multimodal Framework for Egocentric Intent Disambiguation"
type: paper
tags: [multimodal-disambiguation, egocentric-AI, zero-shot, VLM, cross-modal, AAAI-2026]
authors: [Sicheng Yang, Yukai Huang, Weitong Cai, Shitong Sun, You He, Jiankang Deng, Hang Zhang, Jifei Song, Zhensong Zhang]
year: 2025
venue: AAAI 2026
citation_count: null
arxiv_id: "2511.08971"
doi: "10.48550/arXiv.2511.08971"
pdf_url: "https://arxiv.org/pdf/2511.08971"
sub_area: intent-understanding
---

## 概要
提出模块化零样本多模态意图消歧框架 Plug-and-Play Clarifier，包含文本澄清器（对话驱动推理）、视觉澄清器（实时引导反馈）和跨模态澄清器（3D 指示手势接地）三个协同模块，使 4-8B 小模型意图澄清性能提升约 30%，达到与大模型竞争的水平。

## 核心贡献
- 设计三模块协同框架：文本澄清器处理语言歧义，视觉澄清器提供实时拍摄引导，跨模态澄清器实现 3D 指示手势接地
- 实现零样本模块化设计，各模块可独立或组合使用，无需额外训练数据
- 4-8B 小模型意图澄清性能提升约 30%，视觉澄清器纠正引导准确率提升超 20%，跨模态语义回答准确率提升 5%