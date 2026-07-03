---
title: "LLM 时代 RAG 评估综合综述"
type: source
tags: ['semantic-retrieval', 'rag-architecture', 'evaluation', 'survey']
sources: [rag-evaluation-survey]
source_file: raw/papers/rag-evaluation-survey.pdf
last_updated: 2026-07-02
arxiv_id: "2504.14891"
authors: ["Aoran Gan", "Hao Yu", "Kai Zhang", "Qi Liu"]
year: 2025
venue: "arXiv"
citation_count: pending
---

## 概要

RAG 的混合架构（检索+生成）和对动态知识源的依赖使其评估面临独特挑战：传统 IR 评估指标（nDCG/Recall）无法捕获生成质量，传统 NLG 评估指标（BLEU/ROUGE）无法反映事实接地。本综述系统回顾 RAG 评估方法和框架，覆盖四个维度：系统性能（检索质量、端到端延迟、吞吐量）、事实准确性（生成内容是否忠实于检索证据、是否产生幻觉）、安全性（对抗输入鲁棒性、有害内容过滤）和计算效率（推理成本、内存占用）。综述汇编和分类 RAG 专用数据集（如 CRAG、RGB、RAGBench）和评估框架（如 RAGAS、ARES、TRACe），覆盖检索感知评估、鲁棒性测试和联邦检索设置。对高影响力 RAG 研究中的评估实践进行元分析，揭示评估方法论的趋势和不一致。本工作是迄今最全面的 RAG 评估综述，桥接传统 IR 评估方法与 LLM 驱动的评估方法，为 RAG 系统的可靠评估提供关键资源。

## 关键贡献

- **RAG 评估四维度框架**：系统性能 / 事实准确性 / 安全性 / 计算效率——超越单一检索或生成指标的多维评估框架
- **RAG 专用数据集和评估框架分类汇编**：系统分类 CRAG、RGB、RAGBench 等数据集和 RAGAS、ARES、TRACe 等框架——为评估实践提供可导航的资源地图
- **高影响力 RAG 研究评估实践元分析**：揭示评估方法论的趋势和不一致——指出社区评估实践的差距和改进方向
- **传统方法与 LLM 驱动方法的桥接**：系统连接传统 IR 指标（nDCG/Recall）与 LLM-as-judge、忠实度评估等新兴方法——为评估方法论演进提供统一视角

## 关键引用

> "Evaluating RAG systems presents unique challenges due to their hybrid architecture that combines retrieval and generation components, as well as their dependence on dynamic knowledge sources in the LLM era."

> "To the best of our knowledge, this work represents the most comprehensive survey for RAG evaluation, bridging traditional and LLM-driven methods, and serves as a critical resource for advancing RAG development."

## 关联

- [[RetrievalAugmentedGeneration]] — 本文是该概念的评估维度综述，为 RAG 系统提供四维评估框架
- [[RetrievalEvaluation]] — 本文是该概念的核心来源之一，桥接传统 IR 评估与 LLM 驱动评估
- [[rag-comprehensive-survey]] — 后者提供 RAG 架构分类法，本文提供评估方法论——两者互补构成 RAG 完整图景
- [[hakari-bench]] — 后者提供轻量级检索基准，本文综述的评估框架为其提供方法论定位
- [[hteb-harder-embedding-bench]] — 后者挑战嵌入评估的单分数假设，本文的评估综述为其提供更广泛的 RAG 评估背景

## 矛盾

无已知矛盾。综述客观呈现评估方法论的演进而非主张某一评估框架占优。
