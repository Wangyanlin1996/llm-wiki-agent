---
title: "OCR-Memory: 视觉上下文检索增强长程Agent记忆"
type: source
tags: [agent-memory]
sources: [ocr-memory]
source_file: raw/papers/2604.26622.pdf
last_updated: 2026-06-04
---

## 概要
OCR-Memory 利用视觉模态作为高密度的Agent经验表示，将长程历史轨迹渲染为带视觉锚点的标注图像，通过 locate-and-transcribe 检索范式选择相关区域并还原原文，避免自由生成减少幻觉，实现任意长历史的低 prompt 开销保留。ACL 2026 录用。

## 关键贡献
- 提出视觉模态高密度记忆表示——将轨迹渲染为带唯一视觉标识符的图像
- 设计 locate-and-transcribe 检索范式——通过视觉锚点选择相关区域并转录对应原文
- 避免自由生成，减少幻觉，忠实恢复证据
- 严格上下文限制下长程Agent基准一致改善

## 关键引用
> "optical encoding increases effective memory capacity while preserving faithful evidence recovery" — 核心论点

## 关联
- [[AgentMemory]] — 新的视觉模态记忆范式，补充文本检索的不足
- [[MemCog]] — 从记忆即工具到记忆即认知的范式转换，OCR-Memory提供视觉认知的实例
- [[EvoMemory]] — ExpRAG经验检索的视觉替代路径
- [[LightMem]] — STM/MTM/LTM三层体系中的视觉压缩层

## 矛盾
- 与文本检索范式（ExpRAG）在信息保留方式上存在本质差异：视觉压缩 vs 文本压缩