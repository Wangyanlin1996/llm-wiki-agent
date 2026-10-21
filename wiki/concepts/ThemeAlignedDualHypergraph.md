---
title: "主题对齐双超图检索"
type: concept
tags: ['semantic-retrieval', 'graphrag', 'hypergraph', 'cognitive-retrieval']
sources: ["cog-rag"]
last_updated: 2026-07-09
---

主题对齐双超图检索（Theme-Aligned Dual-Hypergraph Retrieval）是 [[cog-rag]] 提出的 RAG 知识建模与检索范式，受人类自上而下认知过程启发，用互补语义粒度的双超图分别建模宏观主题组织与微观实体关系，并以认知两阶段检索实现从全局主题到局部细节的语义对齐。

**双超图索引**：
- **主题超图**（theme hypergraph）G_theme={V_key, E_theme}——对每个文档块用 LLM 抽取主题与关联关键实体，每条主题超边代表该块的叙事主题（故事线/纲要/摘要），顶点为关键实体，建模**跨 chunk 全局主题结构**。弥补超图 RAG 仅实体级、缺统一主题组织的局限。
- **实体超图**（entity hypergraph）G_entity={V, E_low, E_high}——对每块抽取实体作顶点，E_low 捕获成对关系、E_high 建模多实体群组高阶关联（共现/因果），建模**chunk 内细粒度高阶关系**。超越图增强 RAG 仅成对关系的限制。

**认知启发两阶段检索**：模拟人类"主题驱动→细节回忆"信息处理——先在主题超图语义匹配 top-k 主题超边 + 邻域扩散，生成主题感知初答作全局语义锚点；再从初答抽取主题对齐实体关键词，在实体超图检索顶点 + 超边扩散补充细粒度细节，融合生成最终答案。

**边界条件**（[[cog-rag]] 消融）：实体超图对捕获 chunk 内细粒度关系至关重要（移除后跨域跌幅最大）；主题超图在域内密集任务增益明显，但在跨域稀疏（Mix）开放场景可能引入噪声致退化，提示需动态过滤。该范式与 [[GraphRAG]] 的成对图、[[ex-graphrag]] 的可解释编码器、[[omd-graphrag]] 的本体引导抽取构成结构化 RAG 的互补路径，并呼应 [[NeurosymbolicOrchestration]] 的"灵活规划+结构化执行"理念。
