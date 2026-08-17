---
title: "Researcher Agents for KGQA: Agentic Text-to-SPARQL自修正本体grounding"
type: source
tags: [ontology-graph-retrieval]
sources: [researcher-agents-kgqa]
source_file: raw/papers/researcher-agents-kgqa.pdf
last_updated: 2026-08-17
arxiv_id: "2608.07700"
authors: ["Tommaso Soru", "Abdulsobur Oyewale"]
year: 2026
venue: "arXiv"
citation_count: 0
---

## 概要

本文提出一种 agentic text-to-SPARQL 系统，超越静态工具使用 agent——researcher agent 在验证集上每轮推理后，提出并测试对自身提示/工具的修改。系统解决 NL→SPARQL 的三大挑战：词汇歧义消解、表面术语到本体grounding、语法有效且语义忠实的图模式生成。

## 解决的问题

将 NL 问题翻译为可对大型知识图谱执行的 SPARQL 查询需要：消解词汇歧义、将表面术语grounding到目标本体、生成语法有效且语义忠实的图模式。

## 方法与技术

1. **Agentic text-to-SPARQL**：agent 驱动的查询生成+执行+修正循环
2. **自修正本体grounding**：agent 在验证集上迭代改进术语grounding
3. **提示/工具自修改**：每轮推理后 agent 提出并测试对自身配置的修改
4. **语法+语义双重保证**：生成的图模式既语法有效又语义忠实

## 创新点

- 从"静态工具使用"到"researcher agent 自我改进"的跃迁
- 验证集驱动的迭代本体grounding修正
- 提示和工具层面的自修改能力

## 关键引用

> "a researcher agent that, after each round of inference on a validation set, proposes and tests changes to its own prompt and tools" — researcher agent 的核心设计

## 关联

- [[OntologyGraphRetrieval]] — 本体grounding增强 SPARQL 查询精准度
- [[nlkgq-nl-ontology-query]] — NLKGQ 零样本查询生成，Researcher Agents 迭代自修正
- [[AgenticRetrieval]] — Agent 驱动检索的 SPARQL 变体
- [[opi-ontology-kgqa]] — OPI 本体引导 KGQA，互补方法
