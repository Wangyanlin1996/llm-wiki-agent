# 语义检索全景 — 论文洞察日报

**日期**: 2026-07-02
**累计论文**: 148 篇（本轮新增 26 篇：Round 9 语义检索全景）
**知识库页面**: 249 页（+26 来源 +7 概念）

## 概览

| 方向 | 累计 | 本轮新增 |
|------|------|---------|
| Agent Memory | 20 | 0 |
| Intent Understanding | 23 | 0 |
| Intent Recommendation | 19 | 0 |
| Memory-Enhanced Intent Clarification | 6 | 0 |
| Agent Explainability | 36 | 0 |
| Semantic Retrieval | 26 | 26 |

## 本轮重点：语义检索 7 子方向全景覆盖

Round 9 聚焦**语义检索（Semantic Retrieval）**领域，通过 arXiv 7 路布尔检索（`abs:`/`ti:` + AND/OR），覆盖 7 个子方向共 26 篇论文（2024-2026），构建从基础检索到 Agent 驱动的完整技术图谱。三篇电信专用论文（telco-orag、teleembedbench、ARMOR）直接填补 wiki 最大的 3GPP/O-RAN 场景空白。

### T1 稠密检索 Dense Retrieval（3 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 1 | [[dream-dense-retrieval]] — 自回归建模统一稠密检索 | 2024 | arXiv | [2402.10619](https://arxiv.org/abs/2402.10619) | 自回归 query 建模替代双编码器；MS MARCO nDCG@10=0.441；统一检索/重排/生成 |
| 2 | [[scaling-dense-retrieval]] — LLM 标注训练数据挖掘 | 2024 | SIGIR 2026 Workshop | [2404.16046](https://arxiv.org/abs/2404.16046) | 从 LLM 标注挖掘高质量训练数据；渐进课程学习；降低标注成本 |
| 3 | [[coder-constraint-retrieval]] — 约束感知代码检索 | 2025 | arXiv | [2502.13487](https://arxiv.org/abs/2502.13487) | 超越语义相似度的局部约束兼容检索；代码检索新范式 |

### T2 RAG 架构（4 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 4 | [[rag-comprehensive-survey]] — RAG 综合综述 | 2025 | arXiv | [2505.06035](https://arxiv.org/abs/2505.06035) | retriever/generator/hybrid/robust 四类架构分类法 |
| 5 | [[beyond-parameters-survey]] — ICL→RAG→GraphRAG→CausalRAG | 2025 | arXiv | [2506.07496](https://arxiv.org/abs/2506.07496) | RAG 范式演进路径全景综述 |
| 6 | [[rag-security-privacy]] — RAG 安全与隐私 | 2025 | arXiv | [2506.12058](https://arxiv.org/abs/2506.12058) | 检索/上下文构建/生成三阶段安全威胁与防御 |
| 7 | [[rag-evaluation-survey]] — RAG 评估方法 | 2025 | arXiv | [2506.12058](https://arxiv.org/abs/2506.12058) | 系统性能/事实准确性/安全/计算效率四维评估 |

### T3 混合检索 Hybrid Retrieval（3 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 8 | [[telco-orag]] — 电信场景混合检索+神经路由 | 2025 | arXiv | — | 3GPP 检索+Web 混合+神经路由；45% 内存节省；开源 LLM 达 GPT-4 水平——**电信场景** |
| 9 | [[bm25-corrective-rag]] — BM25 超越稠密检索 | 2025 | arXiv | — | BM25+神经重排两阶段；Recall@5=0.816；金融文档 BM25 超越 SOTA 稠密检索 |
| 10 | [[hakari-bench]] — 五族检索模型统一对比 | 2025 | arXiv | — | 稀疏/稠密/混合/重排/LLM 五族统一基准 |

### T4 嵌入模型 Embedding Models（4 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 11 | [[teleembedbench]] — 电信嵌入基准 | 2025 | arXiv | — | 电信首个嵌入基准；LLM embedder 显著优于 sentence-transformer——**电信场景** |
| 12 | [[llm2vec-gen]] — 生成式嵌入 | 2025 | arXiv | — | 在 LLM 输出空间直接生成嵌入；推理时无额外编码 |
| 13 | [[promptembedder]] — 双 LLM 软提示解耦 | 2025 | arXiv | — | 软提示解耦嵌入知识与主干权重；高效可迁移 |
| 14 | [[hteb-harder-embedding-bench]] — 更难的嵌入基准 | 2025 | arXiv | — | MTEB 多维度动态鲁棒性扩展；超越一维静态评估 |

### T5 检索评估 Retrieval Evaluation（2 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 15 | [[coverage-not-averages]] — 语义分层检索评估 | 2025 | arXiv | — | 评估形式化为统计估计；形式化覆盖保证 |
| 16 | [[rare-redundancy-eval]] — 高冗余语料评估 | 2025 | ACL 2026 | — | 原子事实分解+冗余感知评估；金融/法律/专利场景 |

### T6 GraphRAG（4 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 17 | [[is-graphrag-needed]] — 9 种 RAG 场景对比 | 2025 | ACL 2026 GEM Workshop | — | 检索-生成差距；扩展检索不比例提升生成质量 |
| 18 | [[multimodal-graphrag]] — 视觉富文档知识图谱 | 2025 | arXiv | — | GraphRAG 扩展到多模态视觉富文档 |
| 19 | [[ex-graphrag]] — 可解释图检索 | 2025 | arXiv | — | M-GNAN 精确分解节点贡献；可解释性 |
| 20 | [[omd-graphrag]] — 本体引导提取 | 2025 | arXiv | — | 本体引导提升领域特定实体/关系精度 |

### T7 Agent 驱动检索 Agentic Retrieval（5 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 21 | [[reasoning-agentic-rag-survey]] — System 1 vs System 2 | 2025 | arXiv | — | 预定义推理管线 vs 自主工具编排双范式 |
| 22 | [[r2-searcher]] — 多跳推理检索-推理边界校准 | 2025 | arXiv | — | 多跳推理中检索-推理边界校准 |
| 23 | [[kbsd-knowledge-boundary]] — 知识边界校准三决策 | 2025 | arXiv | — | 信任记忆/依赖检索/弃答三决策 |
| 24 | [[metaresearcher]] — 对抗虚拟环境+自反思 RL | 2025 | arXiv | — | 对抗虚拟环境扩展深度研究能力 |
| 25 | [[simplesearch-vl]] — 多模态 agentic 搜索 | 2025 | arXiv | — | 仅需 5K SFT+2K RL 实现多模态 agentic 搜索 |

### 电信专用 Telecom-Specific（1 篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|------|------|-------|-------|---------|
| 26 | [[armor-telecom-retriever]] — 电信查询侧检索器自适应优化 | 2025 | arXiv | — | 查询侧检索器自适应优化；低资源电信场景——**电信场景** |

## 新增概念页（7 个）

| 概念 | 关联来源 | 核心定位 |
|------|---------|---------|
| [[DenseRetrieval]] | dream-dense-retrieval, scaling-dense-retrieval, coder-constraint-retrieval, armor-telecom-retriever | 神经编码器向量空间相似度检索；从双编码器到自回归建模与约束感知 |
| [[RetrievalAugmentedGeneration]] | rag-comprehensive-survey, beyond-parameters-survey, telco-orag, reasoning-agentic-rag-survey | retrieve→augment→generate 核心范式；从 ICL 到 CausalRAG 演进 |
| [[HybridRetrieval]] | telco-orag, bm25-corrective-rag, hakari-bench | 稀疏+稠密融合；BM25 在特定领域仍超越 SOTA 稠密检索 |
| [[EmbeddingModels]] | teleembedbench, llm2vec-gen, promptembedder, hteb-harder-embedding-bench | 从对比学习双编码器到生成式嵌入与软提示解耦 |
| [[RetrievalEvaluation]] | rag-evaluation-survey, coverage-not-averages, rare-redundancy-eval | 超越 nDCG/Recall@k 的多维统计估计与冗余感知评估 |
| [[GraphRAG]] | is-graphrag-needed, ex-graphrag, omd-graphrag, multimodal-graphrag | 知识图谱增强检索支持多跳推理；可解释性与本体引导 |
| [[AgenticRetrieval]] | reasoning-agentic-rag-survey, r2-searcher, kbsd-knowledge-boundary, metaresearcher, simplesearch-vl | LLM Agent 自主决定何时/检索什么/如何反思；System 1 vs System 2 |

## 跨方向关键洞察

### 1. 检索-生成差距（Retrieval-Generation Gap）
[[is-graphrag-needed]] 在 9 种 RAG 场景对比中发现：扩展检索不比例提升生成质量。GraphRAG 的价值在于多跳推理而非单跳事实查询——这挑战了"检索越多越好"的直觉。

### 2. BM25 的持久生命力
[[bm25-corrective-rag]] 在金融文档上发现 BM25 超越 SOTA 稠密检索，颠覆"语义搜索普遍占优"假设。混合检索（稀疏+稠密+重排）是工程最优解——这与电信领域高术语密度场景直接相关。

### 3. System 1 vs System 2 演进
[[reasoning-agentic-rag-survey]] 揭示 Agentic RAG 正从预定义推理管线（System 1）向自主工具编排（System 2）演进。这与 AgentLoop 框架（用户意图→编排器→Skill 执行→结果整合→闭环验证）直接对应——检索是 Skill 执行的核心环节。

### 4. 评估的形式化
[[coverage-not-averages]] 将检索评估从经验平均指标推向统计估计理论，提供形式化覆盖保证——这与电信网络中 SLA 可验证性的思路一致，呼应 [[VerificationCoEvolution]] 三重困境（可扩展×忠实×鲁棒）。

## 与现有 Wiki 的连接

| 新内容 | 现有内容 | 连接关系 |
|--------|---------|---------|
| [[AgenticRetrieval]] | [[closed-loop-explainability-telecom-autonomous-networks]] | AgentLoop 框架中 Skill 执行层的检索环节 |
| [[GraphRAG]] | [[NeurosymbolicOrchestration]] | LLM 灵活规划+符号可验证执行 |
| [[RetrievalEvaluation]] | [[VerificationCoEvolution]] | 检索侧的评估方法论补充验证三重困境 |
| [[telco-orag]] | [[IntentDrivenMnS]] | 3GPP 领域检索直接服务电信意图管理 |
| [[teleembedbench]] | [[IntentDrivenMnS]] | 电信嵌入基准支撑意图理解向量空间 |
| [[armor-telecom-retriever]] | [[IntentDrivenMnS]] | 低资源电信检索器优化服务意图查询 |

## 健康检查

- **空文件**: 0
- **索引同步**: 0 问题
- **知识库总计**: 249 页 / 147 PDF / 148 论文 / 88 概念
