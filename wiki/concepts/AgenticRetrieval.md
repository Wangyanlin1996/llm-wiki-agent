---
title: "Agent 驱动检索（Agentic Retrieval）"
type: concept
tags: ['semantic-retrieval', 'agentic-retrieval']
sources: ["reasoning-agentic-rag-survey", "r2-searcher", "kbsd-knowledge-boundary", "metaresearcher", "simplesearch-vl"]
last_updated: 2026-07-02
---

Agent 驱动检索：LLM Agent 自主决定何时/检索什么/如何反思检索质量。双范式：System 1 预定义推理管线 vs System 2 自主工具编排（[[reasoning-agentic-rag-survey]]）。检索-推理边界校准是多跳推理关键（[[r2-searcher]]）。知识边界校准三决策：信任记忆/依赖检索/弃答（[[kbsd-knowledge-boundary]]）。对抗虚拟环境+自反思 RL 扩展深度研究能力（[[metaresearcher]]）。多模态 agentic 搜索仅需 5K SFT+2K RL（[[simplesearch-vl]]）。与 AgentLoop 框架（用户意图→编排器→Skill 执行→结果整合→闭环验证）直接对应——检索是 Skill 执行的核心环节。相关论文：[[reasoning-agentic-rag-survey]]、[[r2-searcher]]、[[kbsd-knowledge-boundary]]、[[metaresearcher]]、[[simplesearch-vl]]
