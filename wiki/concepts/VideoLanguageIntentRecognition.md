---
title: "视频意图识别（Video-Language Intent Recognition）"
type: concept
tags: [intent-understanding]
sources: [intentvlm]
last_updated: 2026-06-08
---

视频意图识别将意图理解从文本扩展到视频语言模态。IntentVLM 使用前逆建模两阶段框架：forward 生成目标候选 + inverse 结构化推理选择，达到 SOTA 80% 准确率并匹配人类水平。这种方法减少了自由推理中的幻觉问题，为机器人交互中的意图推断开辟了视觉通道。相关论文：[[intentvlm]]