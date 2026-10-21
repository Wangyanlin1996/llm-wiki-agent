---
title: "CyberCane: PhishOnt OWL本体驱动的神经符号RAG钓鱼检测"
type: source
tags: [llm-agent-ontology, neuro-symbolic]
sources: [cybercane-neuro-symbolic-rag]
source_file: raw/papers/cybercane-neuro-symbolic-rag.pdf
last_updated: 2026-07-25
arxiv_id: "2604.23563"
authors: ["Safayat Bin Hakim", "Aniqa Afzal", "Qi Zhao", "Vigna Majmundar", "Pawel Sloboda", "Houbing Herbert Song"]
year: 2026
venue: ""
citation_count: 0
---

## 概要
隐私关键领域需要钓鱼检测系统满足矛盾约束：近零误报、非专家可理解的透明解释、严格合规禁止敏感数据外传、对 AI 生成攻击的鲁棒性。CyberCane 是神经符号框架，集成确定性符号分析与隐私保护 RAG。双阶段管线先用轻量符号规则处理邮件元数据，再将边界案例升级到语义分类（RAG + 自动敏感数据脱敏 + 仅钓鱼语料库检索）。引入 PhishOnt OWL 本体，通过形式推理链实现可验证攻击分类。

## 关键贡献
- 神经符号 RAG：确定性符号分析 + 隐私保护检索增强生成
- PhishOnt OWL 本体，形式推理链实现可验证攻击分类
- 双阶段管线：轻量符号规则 → 边界案例语义分类
- AI 生成威胁上 recall 提升 78.6 分，precision >98%，FPR 低至 0.16%
- 医疗部署预测 542x ROI

## 关键引用
> "We further introduce PhishOnt, an OWL ontology enabling verifiable attack classification through formal reasoning chains."

## 关联
- [[NeuroSymbolicOntology]] — 神符号本体注入框架
- [[OntologyFirstAgentDesign]] — 本体优先Agent设计方法论
- [[titan-graph-reasoning-cti]] — TITAN本体网络威胁情报图推理
- [[security-ontology-autonomous-networks]] — TM Forum安全本体
- [[huntragent]] — 神经符号攻击轨迹重建（如果相关）

## 矛盾
- 无
