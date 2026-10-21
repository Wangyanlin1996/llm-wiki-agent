---
title: "Security Ontology for Autonomous Networks: TM Forum安全管理标准本体"
type: source
tags: [semantic-layer, ontology-reasoning]
sources: [security-ontology-autonomous-networks]
source_file: raw/papers/security-ontology-autonomous-networks.pdf
last_updated: 2026-07-25
arxiv_id: "2605.27743"
authors: ["Loay Abdelrazek", "Sultan Ertas", "Andrey Silva"]
year: 2026
venue: "CSCN 2026"
citation_count: 0
---

## 概要
现代 5G-Advanced 和新兴 6G 架构面临超越传统手动安全配置的复杂多层威胁向量。将安全管理转向自主自保护操作需要形式语义框架。本文规范了 TM Forum TR292I 安全本体 v4.0.0，一个符合 RDFS 的声明式安全管理词汇表。本体原生扩展 TM Forum Intent Common Model（ICM），将高层安全目标与底层技术控制解耦。关键的是，它嵌入资源成本映射属性，确保自主缓解操作保障 SLA。通过 W3C Turtle 和 SPARQL 对分布式 gNB 切片上 DDoS 缓解序列的形式语义验证。

## 关键贡献
- TM Forum TR292I 安全本体 v4.0.0，RDFS 合规
- 原生扩展 TM Forum Intent Common Model（ICM）
- 嵌入资源成本映射属性保障 SLA
- 运行时约束冲突动态解决无需人工干预
- DDoS 缓解序列的形式语义验证

## 关键引用
> "The ontology decouples high-level security goals from underlying technical controls. Crucially, it embeds resource cost mapping properties to ensure autonomous mitigation actions safeguard Service Level Agreements (SLAs)."

## 关联
- [[OntologySemanticLayer]] — 本体语义层
- [[IntentDrivenMnS]] — 3GPP意图驱动管理服务
- [[intent-6g-orchestration]] — TMF意图本体+SHACL验证
- [[RulePolicyIntentRelation]] — 规则-策略-意图关系
- [[deontic-policies-agenticrei]] — OWL道义策略语言治理

## 矛盾
- 无
