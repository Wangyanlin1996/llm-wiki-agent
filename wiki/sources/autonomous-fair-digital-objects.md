---
title: "Autonomous FAIR Digital Objects: 语义Web标准驱动的自主知识对象"
type: source
tags: [semantic-layer, ontology-reasoning]
sources: [autonomous-fair-digital-objects]
source_file: raw/papers/autonomous-fair-digital-objects.pdf
last_updated: 2026-07-25
arxiv_id: "2605.10370"
authors: ["Zeyd Boukhers", "Oya Beyan", "Cong Yang", "Christoph Lange"]
year: 2026
venue: ""
citation_count: 0
---

## 概要
Web 上的科学知识作为被动断言发布，无法决定何时验证证据、调和矛盾或随发现积累更新信心。本文将自主 FAIR 数字对象（aFDO）从抽象概念推进到操作模型，提供从被动科学发布到负责任、标准对齐自动化的路线。aFDO 用三项基于 Semantic Web 标准的能力增强 FDO：(1) 对齐 PROV-O、SHACL 和 ODRL 的 RDF-star 策略层；(2) 限制每公告评估成本的 ActivityStreams 2.0 公告层；(3) 通过声誉和信心加权协议在有界对抗模型下解决多源矛盾的协议层。

## 关键贡献
- 三层增强 FDO：策略层（RDF-star + PROV-O/SHACL/ODRL）+ 公告层（ActivityStreams 2.0）+ 协议层
- 形式化定义区分策略规范、事件处理器和通信接口
- 4,305 个基于罕见疾病本体（ClinVar、HPO、Orphanet）的 FDO 评估
- 解决 56.3% 的 ClinVar 自然冲突
- Sybil/串谋/投毒攻击下在 Byzantine 容差范围内优雅退化

## 关键引用
> "aFDO augments FDOs with three capabilities anchored in Semantic Web standards: a policy layer over RDF-star aligned with PROV-O, SHACL, and ODRL for portable condition-action rules."

## 关联
- [[OntologySemanticLayer]] — 本体语义层
- [[OntologyReasoning]] — 本体推理核心方法
- [[obda-query-abstraction]] — OBDA查询抽象
- [[discoverable-agent-knowledge-aap]] — Agent知识图谱可供性

## 矛盾
- 无
