---
title: "USD场景到知识图谱：LLM零样本本体grounding (Zero-Shot Ontology Grounding)"
type: source
tags: [ontology-semantic-grounding]
sources: [usd-scene-ontology-grounding]
source_file: raw/papers/usd-scene-ontology-grounding.pdf
last_updated: 2026-08-03
arxiv_id: "2606.09134"
authors: ["Jiangtao Shuai", "Zongxiong Chen", "Manfred Hauswirth", "Sonja Schimmler"]
year: 2026
venue: "ICRA 2026 Workshop (J-WOSMARS)"
citation_count: 0
---

## 概要

本文研究从 3D 仿真场景（Universal Scene Description, USD）构建知识图谱的关键瓶颈——将场景对象 grounding 到形式本体类。现有方法依赖手工策展字典，脆弱且不能跨资产泛化。本文研究 LLM 能否作为零样本、免训练替代方案自动化这一 grounding 步骤，在厨房场景（125 对象）上使用 SOMA-HOME 本体达到 90-96% 精确匹配准确率。

## 解决的问题

从 3D 仿真场景构建知识图谱的关键瓶颈是场景对象到形式本体类的 grounding。现有方法依赖手工策展字典，脆弱且不能跨资产泛化。需要一种自动化、可泛化的 grounding 方法。

## 方法与技术

1. **零样本 LLM grounding**：不训练，直接用 LLM 将场景对象 grounding 到本体类
2. **USD 场景图解析**：从 Universal Scene Description 文件提取场景图结构
3. **SOMA-HOME 本体**：作为 grounding 目标本体
4. **特征消融分析**：系统分析 LLM 利用的语义线索（兄弟名称、父路径）vs 几何信息

## 创新点

- 首次系统评估 LLM 零样本本体 grounding 能力，替代手工字典
- 特征消融揭示 LLM 主要利用场景图语义线索而非几何信息
- 上下文增强提示在完全不透明名称下恢复 48% 准确率

## 效果

- 描述性名称：**90-96%** 精确匹配准确率
- 缩写名称：**49-89%**
- 完全不透明名称：上下文增强恢复至 **48%**
- 匿名化语义线索后准确率降至 0-6%，纯几何仅 4-17%

## 关键引用

> "LLMs primarily exploit semantic cues in the scene graph (sibling names and parent paths); anonymizing these cues reduces accuracy to 0-6%" — 揭示 LLM grounding 的语义依赖本质

## 关联

- [[OntologySemanticGrounding]] — LLM 零样本本体 grounding
- [[LLMKGOntologySynergy]] — LLM 与本体/KG 协同
- [[DynamicOntologyConstruction]] — LLM 自动化本体相关操作
- [[OntologySemanticLayer]] — 本体作为场景理解语义层
