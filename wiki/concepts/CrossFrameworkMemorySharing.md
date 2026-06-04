---
title: "跨框架记忆共享（Cross-Framework Memory Sharing）"
type: concept
tags: [agent-memory]
sources: [agentkb]
last_updated: 2026-06-04
---

跨框架记忆共享是 Agent KB 提出的让异构Agent框架无需重训即可共享经验的机制。将轨迹聚合为结构化知识库，提供轻量API；推理时两阶段混合检索（planning seeds + feedback fixes）；disagreement gate 防止检索知识增强而非干扰推理。这代表了从单Agent记忆到多Agent集体智能的范式转换，核心挑战是知识干扰——跨框架传输的经验可能对当前推理产生负面影响。

相关论文：[[agentkb]], [[memp]], [[MemCog]]