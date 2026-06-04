---
title: "视觉记忆编码（Optical Memory Encoding）"
type: concept
tags: [agent-memory]
sources: [ocr-memory]
last_updated: 2026-06-04
---

视觉记忆编码是 OCR-Memory 提出的利用视觉模态作为高密度Agent经验表示的方法。将历史轨迹渲染为带唯一视觉标识符的标注图像，通过 locate-and-transcribe 检索范式选择相关视觉区域并转录对应原文。视觉编码的优势在于：高密度信息压缩（图像比文本节省更多token）、忠实恢复证据（避免自由生成和幻觉）、任意长历史保留。局限在于 video-to-state grounding（SII/PIWM 发现端到端视频仅0.295低于随机基线）。

相关论文：[[ocr-memory]], [[sii-piwm]], [[ContextAgent]]