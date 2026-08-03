---
title: "Open Ontologies: 稳定匹配本体对齐与工具增强工程 (Stable Matching Alignment)"
type: source
tags: [ontology-matching-alignment]
sources: [open-ontologies-stable-matching]
source_file: raw/papers/open-ontologies-stable-matching.pdf
last_updated: 2026-08-03
arxiv_id: "2605.09184"
authors: ["Fabio Rovai"]
year: 2026
venue: "arXiv"
citation_count: 1
doi: "10.48550/arXiv.2605.09184"
---

## 概要

本文提出 Open Ontologies，一个用 Rust 实现的开源本体工程系统，集成 LLM 驱动构建、形式 OWL 推理和基于 Model Context Protocol（MCP）的本体对齐。核心发现是稳定 1:1 匹配是本体对齐质量的主导因素：在 OAEI Anatomy 赛道上达到 F1=0.832（精确率 0.963），消融实验证明信号权重在稳定匹配下无关紧要。

## 解决的问题

本体对齐是异构知识表示互操作的关键挑战。现有方法依赖复杂信号权重调优，但对齐质量的主导因素尚不明确。同时，LLM 读取原始 OWL 文件进行本体交互的效果不如结构化工具访问。

## 方法与技术

1. **LLM 驱动本体构建**：使用 LLM 自动构建本体
2. **形式 OWL 推理**：集成形式化推理保证一致性
3. **稳定 1:1 匹配**：用稳定匹配算法进行本体对齐
4. **MCP 工具增强交互**：通过 Model Context Protocol 提供结构化本体访问

## 创新点

- 发现稳定 1:1 匹配是对齐质量主导因素，信号权重在稳定匹配下无关紧要（F1 变化 <0.004）
- 揭示反直觉结果：LLM 读原始 OWL 文件（F1=0.323）比不读文件（F1=0.431）更差
- MCP 工具结构化访问（F1=0.717）提供质变不同的访问模式
- 单二进制发布，MIT 许可

## 效果

- OAEI Anatomy 赛道：**F1=0.832**（P=0.963, R=0.733），精确率超越所有 SOTA 系统
- 移除稳定匹配后 F1 降至 0.728
- 五种权重配置下 F1 变化 <0.004（稳定匹配使权重无关紧要）
- Conference 赛道：F1=0.438
- MCP 工具访问 F1=0.717 vs 原始 OWL 读取 F1=0.323 vs 无文件 F1=0.431

## 关键引用

> "an LLM reading a raw OWL file performs worse than the same LLM with no file at all" — 反直觉发现：原始语法访问干扰 LLM 推理

## 关联

- [[OntologyMatching]] — 稳定匹配算法用于本体对齐
- [[OntologyReasoning]] — 形式 OWL 推理保证一致性
- [[LLMKGOntologySynergy]] — LLM 与本体工程协同
- [[OntologySemanticLayer]] — 本体对齐作为语义互操作基础
