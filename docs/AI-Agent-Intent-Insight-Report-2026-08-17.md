# 本体图增强精准检索 论文洞察日报 — 2026-08-17

**日期**: 2026-08-17
**累计论文**: 294 篇（本轮新增 17 篇）
**知识库页面**: 423 页

## 概览

| 方向 | 累计论文 | 本轮新增 | 关键概念 |
|---|---|---|---|
| 本体图直接增强检索 | 7 | 7 | [[OntologyGraphRetrieval]]、[[OntologyGroundedRAG]] |
| 本体感知图/记忆引擎 | 3 | 3 | [[AuditableStructuredRetrieval]] |
| 本体引导查询构造 | 4 | 4 | [[OntologyGuidedQueryGeneration]] |
| 本体构建/验证支撑检索 | 3 | 3 | [[OntologyReasoning]] |
| **总计** | **17** | **17** | **5 个新概念** |

## 新增论文清单

### A. 本体图直接增强检索精度（7篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|---|---|---|---|---|
| 1 | OG-RAG | 2024-12 | arXiv | 2412.15235 | 本体超图最小超边集检索；recall+55%, correctness+40% |
| 2 | Evidence Units | 2026-04 | arXiv | 2604.00500 | 本体grounding文档组织为语义完整EU；解析器无关 |
| 3 | HyEm | 2026-01 | arXiv | 2604.09550 | 双曲嵌入编码is-a层次；查询自适应双曲/欧式切换 |
| 4 | OMAGR | 2026-06 | arXiv | 2606.11910 | 多锚点并行图检索打破单轴瓶颈；法律场景 |
| 5 | FAIR GraphRAG | 2026-07 | arXiv | 2607.11464 | FAIR原则+本体schema约束GraphRAG；医疗 |
| 6 | OntologyRAG | 2025-02 | arXiv | 2502.18992 | 本体KG+RAG替代微调；生物医学代码映射 |
| 7 | CyberBOT | 2025-04 | arXiv | 2504.00389 | 本体约束RAG可信+域适切；网络安全教育 |

### B. 本体感知图/记忆引擎（3篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|---|---|---|---|---|
| 8 | WorldDB | 2026-04 | arXiv | 2604.18478 | 递归图+写入时协调；替代flat向量库 |
| 9 | MOSS | 2026-07 | arXiv | 2607.04391 | 结构化关系DB替代嵌入搜索；可审计检索 |
| 10 | RAG-Based Auto-Config | 2026-08 | arXiv | 2608.08618 | ECLASS本体图+混合稠密稀疏检索；多协议 |

### C. 本体引导查询构造（4篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|---|---|---|---|---|
| 11 | NLKGQ | 2026-07 | arXiv | 2607.18029 | OWL本体→LLM零样本结构化查询；无需微调 |
| 12 | Researcher Agents | 2026-08 | arXiv | 2608.07700 | Agentic text-to-SPARQL自修正本体grounding |
| 13 | BMQExpander | 2025-08 | arXiv | 2508.11784 | UMLS本体知识+LLM查询扩展；生物医学 |
| 14 | KROMA | 2025-07 | arXiv | 2507.14032 | RAG动态丰富OM上下文；双相似性优化 |

### D. 本体构建/验证支撑检索（3篇）

| # | 论文 | 年份 | Venue | arXiv | 核心贡献 |
|---|---|---|---|---|---|
| 15 | Ontology-Guided Dedup KG | 2026-07 | arXiv | 2607.28662 | 本体引导去重+类型规范化；文档流→验证KG |
| 16 | Verifiable Knowledge Expansion | 2026-07 | arXiv | 2607.01773 | 检索增强SLM+FCA符号验证循环 |
| 17 | Automated Ontology Generation | 2026-04 | arXiv | 2604.23090 | 多agent LLM从文本生成形式本体 |

## 新增趋势洞察

1. **本体图检索核心价值是"概念一致"而非"表面相似"** — [[og-rag-ontology-grounded]] 的 OG-RAG 用本体超图最小超边集检索实现 recall+55%，证明本体类型/关系约束确保检索结果锚定到概念层次，在事实推理场景中显著优于 vanilla RAG。与 ANCHOR 的"输入→本体图"构建互补，构成"构建→检索"完整管线。

2. **flat 向量库是可解决的结构缺陷** — [[moss-auditable-agentic-memory]] 将 RAG 的"不透明"从固有特性重新定义为可解决的结构缺陷，[[worlddb-ontology-aware-memory]] 用递归图+写入时协调替代 flat chunk。核心范式转变：从"读取时向量匹配"到"写入时结构化协调+读取时精确查询"。

3. **本体 schema 是 NL→结构化查询的"语义契约"** — [[nlkgq-nl-ontology-query]] 证明 OWL 本体足以让 LLM 零样本生成准确结构化查询（无需微调/RAG/多agent），[[researcher-agents-kgqa]] 用验证集驱动迭代自修正。足够好的本体可以降低对微调和 RAG 的依赖。

4. **本体层次需要几何感知编码** — [[hyem-hyperbolic-ontology-retrieval]] 将本体 is-a 层次编码为双曲嵌入，查询自适应切换双曲/欧式检索。双曲空间的指数体积增长天然适配层次结构——这是向量检索无法捕捉的维度。

## 知识库状态

| 指标 | 上轮 | 本轮 | 变化 |
|---|---|---|---|
| 论文 | 277 | 294 | +17 |
| Source 页面 | 283 | 300 | +17 |
| Concept 页面 | 114 | 119 | +5 |
| PDF 文件 | 276 | 293 | +17 |
| 总页面 | ~406 | ~423 | +17 |
| 空文件 | 0 | 0 | ✅ |
| 索引同步 | 0 | 0 | ✅ |
