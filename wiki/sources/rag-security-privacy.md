---
title: "RAG 安全与隐私：架构、威胁、防御与未来方向"
type: source
tags: ['semantic-retrieval', 'rag-architecture', 'security']
sources: [rag-security-privacy]
source_file: raw/papers/rag-security-privacy.pdf
last_updated: 2026-07-02
arxiv_id: "2606.25533"
authors: ["Balamurugan Palanisamy", "G S S Chalapathi", "Vikas Hassija", "Rajkumar Buyya"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要

RAG 通过检索机制增强 LLM 的外部知识，但集成检索管线引入了超越传统语言建模的安全和隐私风险：敏感信息可能通过检索索引、查询日志、上下文构建或联邦更新泄露，而知识库的对抗操纵可破坏生成输出的可信度。本综述提供跨集中式、端侧（Micro-RAG）、联邦式和混合式四种部署范式的安全和隐私全面分析。提出统一威胁面分类法，覆盖检索、上下文构建和生成三阶段，系统分析攻击类别：成员推理（判断文档是否在知识库中）、索引推理（从嵌入推断索引内容）、检索投毒（注入恶意文档）、梯度泄漏（联邦更新泄露）、合谋攻击（多客户端联合操纵）。综述识别上下文构建和证据打包为关键但被低探索的漏洞面——有限上下文预算、排序、截断和证据置换均可影响鲁棒性。防御层面综合架构隔离、算法扰动（差分隐私）、密码学保护（同态加密、可搜索加密）、硬件辅助隔离（TEE）和管线阶段控制。强调隐私-效用权衡和部署考量：去中心化 RAG 在有限内存、算力、通信带宽和监控能力下放大风险。

## 关键贡献

- **统一 RAG 部署分类法**：跨集中式/Micro-RAG/联邦式/混合式的架构选择、数据驻留假设和部署权衡——首个跨范式统一威胁分析
- **上下文构建作为漏洞面**：识别上下文构建和证据打包（有限预算、排序、截断、证据置换）为关键但被低探索的安全攻击面——填补 RAG 安全空白
- **部署感知攻击-防御映射**：将攻击类别（成员推理、索引推理、投毒、梯度泄漏、合谋）和防御机制（架构/算法/密码学/硬件）映射到部署范式——为可信 RAG 提供分层防御框架
- **评估景观与研究议程**：覆盖检索、生成、隐私、安全、效率和联邦学习视角的基准、数据集和指标，识别可扩展安全隐私 RAG 的开放挑战

## 关键引用

> "Sensitive information may be exposed through retrieval indices, query logs, context construction, or federated updates, while adversarial manipulation of knowledge bases can undermine trust in generated outputs."

> "These risks are amplified in on-device and federated settings, where systems must operate under limited memory, computation, energy, communication bandwidth, and monitoring capability."

## 关联

- [[RetrievalAugmentedGeneration]] — 本文是该概念的安全隐私维度综述，覆盖 RAG 管线三阶段威胁面
- [[RetrievalEvaluation]] — 隐私-效用权衡和安全指标为检索评估引入安全维度
- [[rag-comprehensive-survey]] — 后者将隐私保护检索列为开放挑战，本文提供系统化威胁和防御分析
- [[beyond-parameters-survey]] — 后者的部署决策框架与本文的部署感知安全分析互补

## 矛盾

无已知矛盾。综述客观呈现各部署范式的安全-效率权衡而非主张某一范式占优。
