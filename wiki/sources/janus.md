---
title: "JANUS：持久记忆与内部言语驱动的欠明确请求恢复"
type: source
tags: [memory-intent-clarification, persistent-memory, inner-speech, HRI]
sources: [janus]
source_file: raw/papers/janus.pdf
last_updated: 2026-06-27
arxiv_id: "2602.00675"
authors: ["Valerio Belcamino", "Mariya Kilina", "Alessandro Carfì", "Valeria Seidita", "Fulvio Mastrogiovanni", "Antonio Chella"]
year: 2026
venue: null
citation_count: null
doi: "10.48550/arXiv.2602.00675"
---

## 概要
JANUS 是面向辅助机器人的认知架构，将交互建模为部分可观测马尔可夫决策过程（POMDP），通过因子化控制器实现。核心是持久记忆 + 内部言语机制：记忆 Agent 维护有界近期历史缓冲、紧凑核心记忆和带语义检索的归档存储；内部言语模块验证参数完整性并在 grounding 前触发澄清。从欠明确请求中恢复是该系统的核心能力——持久记忆提供用户上下文，内部言语决定何时需要澄清。

## 关键贡献
- 持久记忆三层架构（近期缓冲+核心记忆+归档检索）+ 受控整合与修订策略——记忆增强意图理解
- 内部言语（inner speech）作为控制层验证参数完整性并触发澄清——认知理论启发
- 信息充分性策略、执行就绪策略、工具 grounding 策略的显式分离
- 忠实性约束（faithfulness constraint）将机器人声明绑定到证据束

## 关键引用
> "Dialogue-based human-robot interaction requires robot cognitive assistants to maintain persistent user context, recover from underspecified requests, and ground responses in external evidence" — 持久记忆恢复欠明确请求

## 关联
- [[PersistentMemoryClarification]] — JANUS 是持久记忆增强模糊意图澄清的代表性架构
- [[CognitiveMemoryMechanism]] — 近期/核心/归档三层与 CoPS 的感觉/工作/长期形成对应
- [[StructuredUncertaintyClarification]] — JANUS 的参数完整性验证与 SAGE-Agent 的参数域 EVPI 互补
- [[BayesianDisambiguation]] — JANUS 从欠明确请求恢复与贝叶斯消歧的信息增益最大化互补
- [[AskBeforePlan]] — JANUS 的"澄清先于 grounding"与 Ask-before-Plan 的"澄清先于执行"同构

## 矛盾
- 与 [[PromptBasedUncertaintyDecomposition]] 方向不同：JANUS 用结构化记忆+内部言语，后者用 prompt 分离不确定度
