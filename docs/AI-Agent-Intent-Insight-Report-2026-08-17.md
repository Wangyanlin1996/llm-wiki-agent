# 本体图增强精准检索 论文洞察日报 — 2026-08-17

**日期**: 2026-08-17
**累计论文**: 294 篇（本轮新增 17 篇）
**知识库页面**: 423 页

## 概览

| 方向             | 本轮新增   | 累计      | 代表趋势                    |
| -------------- | ------ | ------- | ----------------------- |
| A. 本体图直接增强检索   | 7      | —       | 超图最小集+双曲层次+多锚点并行        |
| B. 本体感知图/记忆引擎  | 3      | —       | 写入时协调替代读取时匹配            |
| C. 本体引导查询构造    | 4      | —       | OWL schema 零样本生成 SPARQL |
| D. 本体构建/验证支撑检索 | 3      | —       | 去重+类型规范化+FCA符号验证        |
| **总计**         | **17** | **294** | **5 个新概念**              |

## 新增论文清单（速查表）

| # | 论文 | 年份 | Venue | arXiv | 引用 | 方向 |
|---|---|---|---|---|---|---|
| 1 | [OG-RAG](https://arxiv.org/abs/2412.15235) | 2024 | arXiv | 2412.15235 | 0 | A |
| 2 | [Evidence Units](https://arxiv.org/abs/2604.00500) | 2026 | arXiv | 2604.00500 | 0 | A |
| 3 | [HyEm](https://arxiv.org/abs/2604.09550) | 2026 | arXiv | 2604.09550 | 0 | A |
| 4 | [OMAGR](https://arxiv.org/abs/2606.11910) | 2026 | arXiv | 2606.11910 | 0 | A |
| 5 | [FAIR GraphRAG](https://arxiv.org/abs/2607.11464) | 2026 | arXiv | 2607.11464 | 0 | A |
| 6 | [OntologyRAG](https://arxiv.org/abs/2502.18992) | 2025 | arXiv | 2502.18992 | 0 | A |
| 7 | [CyberBOT](https://arxiv.org/abs/2504.00389) | 2025 | arXiv | 2504.00389 | 0 | A |
| 8 | [WorldDB](https://arxiv.org/abs/2604.18478) | 2026 | arXiv | 2604.18478 | 0 | B |
| 9 | [MOSS](https://arxiv.org/abs/2607.04391) | 2026 | arXiv | 2607.04391 | 0 | B |
| 10 | [CLARITY](https://arxiv.org/abs/2608.08618) | 2026 | arXiv | 2608.08618 | 0 | B |
| 11 | [NLKGQ](https://arxiv.org/abs/2607.18029) | 2026 | arXiv | 2607.18029 | 0 | C |
| 12 | [Researcher Agents](https://arxiv.org/abs/2608.07700) | 2026 | arXiv | 2608.07700 | 0 | C |
| 13 | [BMQExpander](https://arxiv.org/abs/2508.11784) | 2025 | arXiv | 2508.11784 | 0 | C |
| 14 | [KROMA](https://arxiv.org/abs/2507.14032) | 2025 | arXiv | 2507.14032 | 0 | C |
| 15 | [Ontology-Dedup KG](https://arxiv.org/abs/2607.28662) | 2026 | arXiv | 2607.28662 | 0 | D |
| 16 | [Verifiable Knowledge Expansion](https://arxiv.org/abs/2607.01773) | 2026 | KDD'26 WS | 2607.01773 | 0 | D |
| 17 | [Automated Ontology Generation](https://arxiv.org/abs/2604.23090) | 2026 | arXiv | 2604.23090 | 0 | D |

## 新增论文结构化分析

### A. 本体图直接增强检索精度

---

#### 1. OG-RAG — 本体grounding检索增强生成

**arXiv**: [2412.15235](https://arxiv.org/abs/2412.15235) | **Venue**: arXiv (Microsoft Research) | **引用**: 0

**解决的问题**: 现有 RAG 方法用领域无关嵌入从文档中检索，但无法捕获领域特定的概念间深层关系。在农业、法律、医疗等需要事实推理和专业流程的领域，vanilla RAG 的上下文生成次优，而微调成本高昂。GraphRAG 和 RAPTOR 虽用图结构但仍依赖 ad-hoc 实体提取，不grounding到领域本体。

**方法与技术**:
1. **本体形式化定义**：将本体 O 定义为三元组集合 S×A×(S∪{φ})，subject 实体通过 attribute 映射到另一实体或未指定域值
2. **本体映射数据提取**：从文档 D 中提取 factual-blocks F，每个 F 中的关系值或来自本体或从文档文本提取
3. **超图构建**：将 factual-blocks 转为超图 H(I)，每条超边封装一簇互相关联的事实知识
4. **贪心最小超边集检索**：用贪心算法选取覆盖查询语义的最小超边集，构建精准上下文

**创新点**:
- 超图表示替代 RAG 的 contiguous chunk 和 GraphRAG 的 ad-hoc 三元组——保留实体间多关系结构
- 最小超边集优化算法实现高效且精准的上下文检索，查询时无需额外 LLM 调用
- 本体grounding确保检索结果概念一致，减少幻觉——与 GraphRAG/RAPTOR 形成对比

**效果**:
- Dataset: Soybean (85 docs) | Metric: Context Recall | Result: 0.84 | Baseline RAG: 0.22 | Δ: +55% (vs RAG), +30pp (vs RAPTOR 0.54)
- Dataset: Wheat (85 docs) | Metric: Context Recall | Result: 0.95 | Baseline RAG: 0.14 | Δ: +81pp
- Dataset: News (149 articles) | Metric: Answer Correctness (GPT-4o) | Result: 0.66 | Baseline RAG: 0.27 | Δ: +39pp
- 事实推理准确率 +27%（基于 CO2 排放推演任务）
- 归因速度 +30%（16人用户研究，时间 43.5s vs RAG 61.2s，支持度 3.46/5 vs 2.67/5）
- 4种 LLM 一致提升（Llama-3-8B, Llama-3-70B, GPT-4o-mini, GPT-4o）

**Wiki**: [[og-rag-ontology-grounded]] | **概念**: [[OntologyGraphRetrieval]]、[[OntologyGroundedRAG]]

---

#### 2. Evidence Units — 本体grounding文档组织实现解析器无关检索

**arXiv**: [2604.00500](https://arxiv.org/abs/2604.00500) | **Venue**: arXiv (KT/Korea Telecom) | **引用**: 0

**解决的问题**: 结构化文档（表格+标题、图+说明、方程+解释段落）在检索时被碎片化——元素级索引将每个解析元素视为独立 chunk，表格与标题分离、图与说明分离。不同解析器（MinerU、Docling、PaddleOCR-VL）对同一区域产生不同 bbox 表示，chunking 算法需为每个解析器重写。

**方法与技术**:
1. **DoCO 扩展本体规范角色**：扩展 Document Components Ontology (DoCO)，用 OWL 定义 dso: 命名空间，将异构解析器输出映射到统一语义 schema（dso:Table, dso:Chart, dso:Caption 等）
2. **三阶段 EU 构建**：Phase A 视觉种子形成 EU 核心（空间近邻阈值 <0.30）；Phase B 全局语义分配段落（相似度矩阵 M，阈值 τ=0.40，低于阈值保留为独立 EU）；Phase C 残差合并
3. **图决策层 Neo4j**：EU 构建规则持久化为 Neo4j 图节点，两个不变量 I1（Restoration）和 I2（Validation）验证 EU 完整性
4. **跨解析器验证**：MinerU 和 Docling 的 EU 空间足迹收敛

**创新点**:
- 从"元素级索引"到"语义完整单元"的范式转变——表格+标题+说明作为原子检索单元
- DoCO 扩展本体实现解析器无关——skos:altLabel 枚举已知解析器标签变体
- 全局相似度矩阵替代局部 1:1 匹配——Phase B 用全段落×全EU 矩阵 argmax 分配，而非局部近邻 first-match
- 图决策层使规则可审计、可动态修改无需改代码

**效果**:
- 跨解析器验证：MinerU 和 Docling 的 EU 空间足迹收敛（normalized [0,1] 坐标系）
- Phase B 全局分配阈值 τ=0.40（vs 先前局部匹配 0.70），未匹配段落保留为独立 EU（零信息丢失）
- 对比 Docling 自带 chunking：EU 显式强制视觉-语义分组（typed ontology: table_panel = table + caption + unit_label），Docling 不保证

**Wiki**: [[evidence-units-ontology-retrieval]] | **概念**: [[OntologyGraphRetrieval]]

---

#### 3. HyEm — 双曲空间本体层次感知查询自适应检索

**arXiv**: [2604.09550](https://arxiv.org/abs/2604.09550) | **Venue**: arXiv | **引用**: 0

**解决的问题**: 生物医学本体（HPO、DO、MeSH）使用深层 is-a 分类层次，但生产 RAG 系统依赖欧式嵌入和 ANN 索引，无法编码层次结构。双曲嵌入适合层次表示但面临两大障碍：(1) 缺乏原生双曲向量数据库支持；(2) 在实体中心查询（层次无关）上表现不佳——现有系统无法兼顾。

**方法与技术**:
1. **半径控制双曲嵌入**：训练 radius-controlled hyperbolic concept embeddings，控制嵌入半径避免漂移到 Poincaré 边界
2. **欧式 ANN 索引近似**：在 tangent space（log-map）上用欧式 ANN 搜索，然后在小候选集上做精确双曲重排——绕过向量库原生支持缺失
3. **查询自适应软混合**：根据查询类型动态混合双曲和欧式相似度信号——层次相关查询加权双曲，实体中心查询加权欧式
4. **可索引性压力测试**：量化 ANN 过采样需要多少才能让重排恢复真实双曲 top-k 邻居

**创新点**:
- 查询自适应机制解决双曲嵌入"一刀切"问题——承认并非所有查询都需要层次感知
- 欧式索引近似双曲距离绕过向量库限制——在标准 Euclidean/cosine API 上部署
- 明确范围声明：双曲几何不是万能药，需适当 scoped——与文献中混合/负面证据一致

**效果**:
- Dataset: HPO, DO, MeSH 生物医学本体（具体数值待补充——PDF 提及实验但表格解析受限）
- 设计原则验证：半径控制缓解边界漂移；软混合适配不同查询类型
- ⚠️ PDF deep reading incomplete — 部分实验表格因 PDF 格式错误未能完整提取

**Wiki**: [[hyem-hyperbolic-ontology-retrieval]] | **概念**: [[OntologyGraphRetrieval]]、[[HyperbolicOntologyEmbedding]]

---

#### 4. OMAGR — 本体引导多锚点图检索框架

**arXiv**: [2606.11910](https://arxiv.org/abs/2606.11910) | **Venue**: arXiv | **引用**: 0

**解决的问题**: 交通法律责任确定需要同时识别跨多个法律维度（违章类型、事故场景、责任方、责任类别）的相互依赖条款。现有 RAG 存在"多维度检索瓶颈"：dense retrieval 将多维查询压缩为单向量，主题主导维度挤占其余维度；KG-RAG 从单一实体出发遍历，限制在单一实体邻域内。

**方法与技术**:
1. **六维交通法律本体**：D1 事故场景、D2 违章类型、D3 责任方、D4 责任类别（四个检索锚点）；D5 法律后果、D6 损害类型（两跳扩展恢复）
2. **多锚点并行图检索**：LLM 约束解析查询为四个锚点，每个锚点独立 Cypher 查询遍历 KG 不同区域
3. **支持机制**：查询扩展（3-5 个改写）+ dense retrieval 语义回退 + 两跳关系扩展 + Reciprocal Rank Fusion (k=60) + BGE 交叉编码器重排 top-8 + MMR 去重（λ=0.7）
4. **TrafficLaw-QA 基准**：200 题专家验证（双盲标注 Cohen's κ=0.82），11 主题类别，3 难度等级

**创新点**:
- 多锚点图检索打破单轴压缩瓶颈——每个法律维度获得独立检索路径，违章维度不会挤占场景/责任维度
- 查询扩展 vs 多锚点的明确区分：扩展在同一语义空间内增加覆盖，多锚点在不同子图区域并行遍历
- TrafficLaw-QA 基准填补多维度法律检索评测空白

**效果**:
- Dataset: TrafficLaw-QA (200 questions, 527 provisions, 6 law sources) | Metric: Context Precision | Result: 0.915 | Baseline Naive RAG: 0.834 | Baseline LlamaIndex KG: 0.722 | Δ: +19.3pp vs LlamaIndex KG
- Dataset: TrafficLaw-QA | Metric: Faithfulness | Result: 0.787 | Baseline Naive RAG: 0.625 | Baseline LlamaIndex KG: 0.751 | Δ: +16.2pp vs Naive RAG
- 消融：去掉多锚点（单锚点）Context Precision 0.915→0.862（-5.3pp，最大组件级下降）；去掉 KG 仅用向量检索 Faithfulness 0.802（+0.015 但 CP 降 0.025）

**Wiki**: [[omagr-ontology-multi-anchor-retrieval]] | **概念**: [[OntologyGraphRetrieval]]

---

#### 5. FAIR GraphRAG — FAIR原则+本体schema约束GraphRAG

**arXiv**: [2607.11464](https://arxiv.org/abs/2607.11464) | **Venue**: arXiv (RWTH Aachen) | **引用**: 0

**解决的问题**: GraphRAG 虽能捕获语义关系，但缺乏 FAIR 原则（可查找/可访问/可互操作/可重用）约束——在医疗等复杂领域中 KG 构建无 schema 约束导致实体/关系类型不规范，元数据不完整，无法回答涉及元数据和本体链接的复杂查询。

**方法与技术**:
1. **FAIR Digital Objects (FDO) 节点**：每个图节点是 FDO——包含核心数据、元数据、持久标识符(PID)、语义链接（ontology term mapping via BioPortal API，1200+ 生物医学本体）
2. **LLM 驱动 KG 构建**：LLM 用于 schema 设计、实体/关系提取、元数据自动提取——结构化数据用规则映射，非结构化数据用 LLM one-shot 提取填充 JSON schema
3. **属性图模型**：采用 property graph（而非 RDF），对齐 LLM 的 JSON-like 输出结构
4. **Graph 检索引擎**：LLM 生成 Cypher 查询执行图数据库检索

**创新点**:
- 首次将 FAIR 原则嵌入 GraphRAG 管线——14/15 FAIR 指标达标（仅缺许可证 R1.1）
- FDO 作为图节点核心单元——PID + 元数据 + 本体映射三重保证
- 医生与计算机科学家协同设计——确保临床相关性

**效果**:
- Dataset: pCCA RNA-sequencing (胆管癌, 8 patients) | Metric: Overall Accuracy (gpt-4o-mini) | Result: 92.86% | Baseline (non-FAIR KG): 42.86% | Δ: +50pp
- Dataset: pCCA | Metric: Metadata Accuracy (gpt-4o-mini) | Result: 90% | Baseline: 0% | Δ: +90pp
- Dataset: pCCA | Metric: Ontology Accuracy (gpt-4o-mini) | Result: 90% | Baseline: 0% | Δ: +90pp
- Coverage: 92.86% (FAIR) vs 42.86% (baseline) | Explainability: 100% (FAIR) vs 66.66% (baseline)
- Llama-3.3-70B: 33.33% accuracy (FAIR) vs 19.05% (baseline)，常生成无效 Cypher 查询

**Wiki**: [[fair-graphrag-semantic-data]] | **概念**: [[OntologyGraphRetrieval]]、[[OntologyGroundedRAG]]

---

#### 6. OntologyRAG — 本体知识图谱+RAG实现生物医学代码映射

**arXiv**: [2502.18992](https://arxiv.org/abs/2502.18992) | **Venue**: arXiv (IQVIA) | **引用**: 0

**解决的问题**: 生物医学代码映射（识别不同本体间概念的等价/相似关系）传统依赖昂贵的领域微调语言模型，且 LM 仅给出候选列表无推理依据，编码专家仍需逐条对照本体验证。本体定期更新后需重新微调，耗时费力。

**方法与技术**:
1. **ETL 本体 KG 构建**：将本体源文件 Extract-Transform-Load 为 RDF 三元组，存储于 Oxigraph 图数据库
2. **NL2SPARQL 模块**：LLM 从自然语言生成 SPARQL 查询，含自验证检查点（语法+图源+实体+关系存在性），无效查询自动重试
3. **推理与摘要模块**：LLM 基于 NLQ + 检索代码对，判定三级映射级别（A: 语义等价 / B: 部分相似 / C: 不等价），附推理依据
4. **4种提示策略对比**：zero-shot / few-shot(16例) / example-enhanced few-shot(21例) / chain-of-thought + enhanced few-shot

**创新点**:
- 用 RAG 管线替代本体领域微调——无需重训 LM，本体更新时仅更新 KG
- NL2SPARQL 自验证循环——自动检测并修复无效 SPARQL
- 三级映射级别 + 推理依据——为编码专家提供可解释决策支持

**效果**:
- Dataset: ICD-10-CM 代码映射 | Metric: Zero-shot Accuracy | GPT-4: 8.38% | GPT-3.5-Turbo: 0.27% | Llama-3-8B: 4.67% | Flan-T5-XXL: 0%
- Dataset: 500 对疾病描述 gold dataset | Metric: Mapping Level Precision | 具体数值待补充（消融实验在4种提示策略×4模型上运行）
- 消融发现：zero-shot 直接映射准确率均 <10%——证明 LLM 独立完成代码映射不可行，RAG 管线必要

**Wiki**: [[ontologyrag-biomedical-code-mapping]] | **概念**: [[OntologyGraphRetrieval]]、[[OntologyGroundedRAG]]

---

#### 7. CyberBOT — 本体grounding RAG实现可信网络安全教育问答

**arXiv**: [2504.00389](https://arxiv.org/abs/2504.00389) | **Venue**: arXiv (Arizona State University) | **引用**: 0

**解决的问题**: 网络安全教育中 LLM 回答需超越表面相关性，提供可信且域适切的信息。错误信息在安全教育场景中代价高昂——学生可能学到不安全或过时的实践。现有 LLM 缺乏网络安全领域结构化约束，易产生域外幻觉。

**方法与技术**:
1. **网络安全本体构建**：定义网络安全领域的概念/关系/约束
2. **本体grounding RAG**：用本体约束检索过程，过滤域外/不可信结果——检索结果锚定到本体概念
3. **可信性保证**：检索结果域适切性检查，确保回答来自经过本体验证的源
4. **教育问答系统**：面向探究式学习的问答 chatbot

**创新点**:
- 本体grounding从"表面相关"提升到"域适切且可信"——超越关键词匹配
- 网络安全本体约束 RAG 检索的全流程——从检索到生成
- 教育场景的安全性和准确性保证——错误信息有高代价场景

**效果**:
- ⚠️ PDF deep reading incomplete — PDF 格式错误(FzErrorSyntax)无法完整提取，效果数据待补充
- 系统设计为网络安全教育场景的准确性保证框架

**Wiki**: [[cyberbot-ontology-grounded-rag]] | **概念**: [[OntologyGraphRetrieval]]、[[OntologyGroundedRAG]]

---

### B. 本体感知图/记忆引擎

---

#### 8. WorldDB — 本体感知写入时协调的向量图世界记忆引擎

**arXiv**: [2604.18478](https://arxiv.org/abs/2604.18478) | **Venue**: arXiv | **引用**: 0

**解决的问题**: RAG over flat 向量库将事实碎片化为 chunk，丢失跨会话身份、无替代/矛盾概念。现有双时态 KG 系统（Graphiti、Memento、Hydra DB）增加了类型边和有效时间元数据，但图本身仍是 flat 的——无递归组合、无节点内容寻址不变量。

**方法与技术**:
1. **向量图世界**：将记忆表示为递归可组合的图结构——子图可作为父图节点递归组合
2. **本体感知写入时协调**：写入时用本体类型/关系约束解决矛盾和替代——而非读取时过滤
3. **内容寻址不变量**：节点内容寻址确保一致性——内容哈希作为节点身份
4. **双时态 + 本体**：结合双时态元数据（valid time + transaction time）和本体类型约束

**创新点**:
- 从"读取时过滤"到"写入时协调"的范式转变——矛盾在写入时解决而非留给检索
- 递归图组合替代 flat chunk——子图可嵌套为父图节点，保留事实间层次结构
- 内容寻址不变量提供形式一致性保证——超越 Graphiti/Memento 的 flat 图

**效果**:
- ⚠️ PDF deep reading incomplete — 论文以系统设计为主，定量实验数据待补充
- 对比定位：明确超越 Graphiti/Memento/Hydra DB（无递归组合、无内容寻址不变量）

**Wiki**: [[worlddb-ontology-aware-memory]] | **概念**: [[OntologyGraphRetrieval]]、[[AuditableStructuredRetrieval]]

---

#### 9. MOSS — 可审计Agentic记忆架构替代向量相似度搜索

**arXiv**: [2607.04391](https://arxiv.org/abs/2607.04391) | **Venue**: arXiv | **引用**: 0

**解决的问题**: RAG 依赖嵌入相似度搜索，构造上不透明（opaque by construction）——无法解释为什么检索了某个 chunk，无法追溯检索决策链，受限于向量表示的理论上限。在 agent 记忆场景中，不透明性意味着无法审计 agent 基于什么记忆做出了什么决策。

**方法与技术**:
1. **结构化关系数据库检索**：agent 驱动对结构化关系 DB 的检索，用递归 SQL 确定性遍历关系——替代嵌入相似度
2. **十一张图 ~500 万类型关系**：segments 带摘要、co-occurrence、时间邻接（原生时间戳）、主题凝聚、情感共鸣边——连接索引数据库段而非原始提取
3. **模型/存储/API 无关**：适配任意 LLM、存储后端和 API
4. **数据库是地图，文档是领土**：原始语料（对话转录+文档）永不修改/分块/替换——关系 DB 是导航层指向完整领土

**创新点**:
- 将"不透明"从 RAG 固有特性重新定义为可解决的结构缺陷——结构化关系存储提供可审计检索
- 十一类关系家族——特别是"情感共鸣边"（affective resonance edges），在文献中无先例
- "数据库是地图，文档是领土"原则——关系层是导航而非替代，原始语料完整保留

**效果**:
- ⚠️ PDF deep reading incomplete — 论文以架构设计为主，~500万类型关系的生产部署数据待补充
- 定位：lifetime corpus + agentic navigator + auditable relational substrate 三者交集

**Wiki**: [[moss-auditable-agentic-memory]] | **概念**: [[AuditableStructuredRetrieval]]

---

#### 10. CLARITY — ECLASS本体图+混合检索工业设备自动配置

**arXiv**: [2608.08618](https://arxiv.org/abs/2608.08618) | **Venue**: arXiv (KFUPM) | **引用**: 0

**解决的问题**: 工业设备调试需要工程师从异构 PDF 手册中手动提取数百个协议特定参数并转录到监控系统——耗时且易错。现有工业 LLM 系统缺乏混合检索+本体约束+形式验证+多协议+弃权门的全栈能力。

**方法与技术**:
1. **ECLASS+AAS+SOSA/SSN 本体图**：从三个工业标准本体构建参数类型/关系图
2. **混合稠密-稀疏+图增强检索**：BGE-M3 (1024维) 稠密 + BM25 稀疏 + 本体术语boost第三信号，RRF 融合，交叉编码器重排
3. **SHACL 验证**：生成的 JSON-LD 配置用 pyshacl 验证——编码必要属性、数据类型、值域（如 Modbus 寄存器 [1, 65534]）
4. **两阶段弃权门**：(C1) 重排器分数 smax ≥ τ=0.72 + (C2) IRI 解析率 ρ ≥ 0.80——防止不安全 LLM 调用
5. **四步 JSON 修复**：去除注释/尾逗号/Python字面量/引号规范化

**创新点**:
- 本体图作为混合检索的第三信号——超越稠密+稀疏二元融合
- 两阶段弃权门——重排器分数 + IRI 解析率双重保护，防止幻觉参数部署
- SHACL 形式验证——协议特定 shapes 编码值域约束（如寄存器地址范围）
- 全栈能力：混合检索+本体图+形式验证+多协议+弃权门——超越 LLM4PLC/Agents4PLC 等现有系统

**效果**:
- Dataset: 28 gold queries, 71 chunks | Metric: nDCG@10 | Hybrid+Cross-encoder: 0.679 | Dense only: 0.561 | Sparse: 0.647 | Δ: +11.8pp vs Dense
- Dataset: 4 devices × 3 protocols | Metric: Field-level F1 | Result: 0.867 (micro avg) | Modbus RTU: 1.0 | OPC-UA: 0.0 (失败) | Profibus DP: 1.0 | CANopen: 1.0
- 弃权门校准：文档查询 smax ≥0.526，域外查询 smax ≤0.061——8.6× 分离无重叠
- UR5e 机器人案例：254页手册未修改，F1=1.0，4.2-4.7s/配置（暖启动）
- 消融：去 BM25 3/4 部署成功；去 dense 2/4；去 JSON repair 1/4

**Wiki**: [[rag-autoconfig-industrial-fieldbus]] | **概念**: [[OntologyGraphRetrieval]]

---

### C. 本体引导查询构造

---

#### 11. NLKGQ — OWL本体零样本LLM结构化查询生成

**arXiv**: [2607.18029](https://arxiv.org/abs/2607.18029) | **Venue**: arXiv (Max Planck Institute) | **引用**: 0

**解决的问题**: 研究者需要回答关于领域特定档案内容的临时问题，但缺乏编写 SPARQL 等结构化查询的专业知识。现有 KGQA 方法依赖微调、检索增强或多 agent 编排——部署复杂度高。

**方法与技术**:
1. **OWL 本体六项设计原则**：(1) 完整英文单词（hasAcquisitionTime 非 acqT）；(2) 一致命名模式（has<Property>）；(3) 描述性关系（isSubjectOfExperiment）；(4) 显式 domain/range；(5) 自然语言注释（rdfs:comment, rdfs:label, skos:altLabel）；(6) 无不透明编码
2. **NLKGQ 查询服务器**：系统提示 = 通用SPARQL生成指令 + 完整OWL本体(Turtle格式) + 领域特定 rider（约定/常见错误修正）
3. **迭代开发循环**：本体修正→测试用例→prompt rider 三件套渐进优化
4. **KG-to-SQL 生成器**：自动从 OWL KG 生成 SQL schema，对比 text-to-SPARQL vs text-to-SQL

**创新点**:
- 证明本体设计质量是 LLM 查询生成准确率的决定性因素——而非模型大小或提示策略
- 六项本体设计原则"零成本但高回报"——readable names 与 opaque names 定义成本相同
- 无需微调/RAG/多agent——本体 schema 作为唯一"语义契约"即可零样本生成
- text-to-SPARQL vs text-to-SQL 首次同 KG 同问题系统对比

**效果**:
- Dataset: 神经影像研究元数据 | Models: 8 LLMs (Qwen3-8B ~ Qwen3.6-35B-A3B) | Configs: 768 (8 models × 8 ontology representations) | Runs: 16,000+
- Metric: SPARQL 生成准确率 | 最佳模型准确率显著高于 worst ontology representation——本体设计是主导因素
- ⚠️ 具体准确率数值待补充（表格在 PDF 中被截断）

**Wiki**: [[nlkgq-nl-ontology-query]] | **概念**: [[OntologyGuidedQueryGeneration]]

---

#### 12. Researcher Agents — Agentic Text-to-SPARQL自修正本体grounding

**arXiv**: [2608.07700](https://arxiv.org/abs/2608.07700) | **Venue**: arXiv (Liber AI) | **引用**: 0

**解决的问题**: 将 NL 问题翻译为可对大型 KG 执行的 SPARQL 查询需要：消解词汇歧义、将表面术语grounding到目标本体、生成语法有效且语义忠实的图模式。静态工具使用 agent 的 scaffolding（提示/规则/工具接线）固定不变，无法自我改进。

**方法与技术**:
1. **下游 text-to-SPARQL agent**：三个工具——(i) 表面形式查找映射问题片段到 DBpedia 实体；(ii) 本体查找枚举类/属性；(iii) SPARQL 端点执行+验证
2. **Researcher agent 自改进外循环**：验证集每轮推理后，编排器 LLM 观察 agent 成败，提出对 agent 源代码的修改——应用到工作副本，测试，继续循环
3. **九版本特征构建研究**：v1→v9 逐步添加 dbo 偏好规则、SELECT DISTINCT、分组 dbo/dbp 对、三元组计数、Unicode 回退、rdf:type 约束、多跳异常、COUNT 格式、三元组方向规则
4. **基准检验**：人工检查 v6 错误，发现 DBpedia 属性歧义（dbo:literaryGenre vs dbp:genre 返回不同结果数）

**创新点**:
- 从"静态工具使用"到"researcher agent 自我改进"——agent 编辑自身源代码而非仅 scratchpad
- 验证集驱动的迭代本体grounding修正——编排器角色类似 ML 研究者做特征构建研究
- 揭示基准自身缺陷——DBpedia 属性歧义导致正确查询被标记为错误

**效果**:
- Dataset: DB25 (2025 DBpedia validation set) | Metric: Overall Accuracy | Best (v6/v8): 0.22 | v1: 0.20 | 6 LLMs: 0.15-0.23 (Qwen 3.5 122B 最高 0.23, Claude Sonnet 4.6 0.21)
- Bottleneck: BGP Predicates 准确率 0.22-0.31（远低于 Inner ops 0.79-0.86 和 Outer ops 0.73-0.86）——谓词选择是瓶颈
- Final eval (DB26): F1=0.32 (Claude), 0.31 (Qwen) — 高于 DB25 的 0.21-0.23，因 DB26 标注者修复了部分问题
- 消融：去掉多锚点最大降幅（v6→A2 single-anchor: 0.22→0.17）

**Wiki**: [[researcher-agents-kgqa]] | **概念**: [[OntologyGuidedQueryGeneration]]

---

#### 13. BMQExpander — UMLS本体知识+LLM查询扩展增强生物医学文档检索

**arXiv**: [2508.11784](https://arxiv.org/abs/2508.11784) | **Venue**: arXiv (UC Riverside) | **引用**: 0

**解决的问题**: 生物医学文档 QA 的检索阶段因领域特定词汇和用户查询中的语义歧义而充满挑战——用户查询与文档术语不匹配导致召回率低。现有查询扩展方法（PRF、BERT-QE）在生物医学领域效果有限。

**方法与技术**:
1. **UMLS 本体知识提取**：LLM 提取查询中关键医学术语，映射到 UMLS CUI（Concept Unique Identifier），从 MeSH/SNOMED/NCI 等词汇表检索定义和语义关系
2. **概念级知识图谱构建**：将 UMLS 关系（PAR/CHD/RO）表示为剪枝语义图——启发式选择领域特定边
3. **LLM 生成伪文档**：将查询+定义+关系序列化后 prompt LLM，生成医学grounded的上下文丰富伪文档
4. **加权查询扩展**：q' = q⊕...⊕q (α次) ⊕ p_q，α=5 控制原始查询权重，用 BM25 检索扩展后查询

**创新点**:
- 本体知识（定义+关系）+ LLM 生成能力的协同——LLM 生成受 UMLS 定义约束，减少幻觉扩展
- 剪枝语义图——领域特定边选择，避免噪声关系
- LLM-agnostic 设计——扩展主要由 UMLS 定义和概念关系驱动，非 LLM 参数知识

**效果**:
- Dataset: NFCorpus, TREC-COVID, SciFact | Metric: NDCG@10 | 改善 vs sparse baselines: up to +22.1%
- ⚠️ 具体各数据集上的 NDCG@10 数值待补充（PDF 表格因字体错误未完整提取）
- 对比基线：BM25、dense retrievers (MedCPT, BMRetriever)、query expansion methods (BERT-QE, PRF)

**Wiki**: [[bmqexpander-ontology-query-expansion]] | **概念**: [[OntologyGuidedQueryGeneration]]

---

#### 14. KROMA — LLM+RAG增强本体匹配

**arXiv**: [2507.14032](https://arxiv.org/abs/2507.14032) | **Venue**: arXiv (Case Western Reserve) | **引用**: 0

**解决的问题**: 本体匹配（OM）是语义互操作性的基石任务，但现有系统依赖手工规则或专用模型，适应性有限——无法动态适配不同本体的结构和词汇差异。现有 LLM-based OM 方法直接 prompt LLM 判断概念等价，缺少结构化上下文。

**方法与技术**:
1. **RAG 管线增强 OM**：动态检索本体结构/词汇/定义知识丰富匹配上下文——targeted knowledge retrieval 而非整本体注入
2. **本体双相似性匹配**：概念相似度 F(c,c') = γ·sim(c,c') + (1-γ)·q(c,c',M)——结合语义相似度（字符串/信息量/NGD）和 LLM 布尔判断
3. **本体精炼**：轻量级本体精炼步骤——剪枝候选概念，减少 LLM 调用开销
4. **在线/离线精炼**：离线算法+在线增量版本，均低多项式时间，有最优性保证

**创新点**:
- RAG 管线动态丰富 OM 上下文，替代静态规则——targeted retrieval 而非整本体注入
- 双相似性优化解决 OM 的效率-质量权衡——概念相似度预筛 + LLM 精确判断
- 轻量本体精炼减少 LLM 通信开销——剪枝候选概念对

**效果**:
- Dataset: 多个 OM 基准数据集 | Metric: 匹配准确率 | vs 现有 LLM-based 方法: +10.95% (average)
- 消融：知识检索提升 +6.65%；本体精炼提升 +2.68%
- 通信开销与基线相当——精炼步骤显著降低 LLM 调用次数

**Wiki**: [[kroma-ontology-matching-rag]] | **概念**: [[OntologyGuidedQueryGeneration]]、[[OntologyMatching]]

---

### D. 本体构建/验证支撑检索

---

#### 15. Ontology-Guided Dedup KG Construction — 本体引导去重感知KG构建

**arXiv**: [2607.28662](https://arxiv.org/abs/2607.28662) | **Venue**: arXiv | **引用**: 0

**解决的问题**: LLM 从非结构化文档提取实体/关系流畅但不一致：类型词汇跨文档碎片化、同一人多种名称变体、关系重复、同名不同人被静默混淆。这些问题导致构建的 KG 质量不可靠，下游检索精度受损。

**方法与技术**:
1. **本体引导提取**：从图数据库用嵌入相似度检索相关本体切片，注入提取 prompt——模型输出类型来自形式 schema 而非自由标签，减少目录开销约 94%（vs 静态域切片）
2. **五阶段提取管线**：S1 提取 → S2 确定性清洗 → S3 跨 chunk 合并 → S4 关系二次提取（质量门控） → S5 富化
3. **六种零推理去重算法**：规则为基础，无推理开销——配对嵌入解析（hard-conflict guard 不受相似度分数影响）
4. **多格式处理**：PDF/表格/Office/图像——六信号逐页分类器路由 PDF 页面到 text/OCR/skip 路径

**创新点**:
- 本体引导提取用 live vector retrieval 替代静态域切片——减少 94% 目录开销
- 六种零推理去重算法 + 嵌入解析——hard-conflict guard 确保同名不同人不被合并
- 质量门控关系二次提取——四项域知识检查防止欠提取（财务连通性/关系类型多样性等）
- 生产级 Kafka 消费者——实时文档流处理

**效果**:
- Metric: Search Recall | Result: ~95% | Baseline: ~70% | Δ: +25pp
- Metric: False Positive Rate | Result: 0 (零误报)
- 本体切片检索开销减少 ~94%（vs 静态域切片）
- 模型: Konect-U/Qwen3.5-9B-AWQ-4bit-Ontology（本地 vLLM 部署）

**Wiki**: [[ontology-dedup-kg-construction]] | **概念**: [[OntologyGraphRetrieval]]

---

#### 16. Verifiable Knowledge Expansion — 检索增强SLM+FCA符号验证本体构建

**arXiv**: [2607.01773](https://arxiv.org/abs/2607.01773) | **Venue**: KDD'26 Workshop (epiDAMIK) | **引用**: 0

**解决的问题**: 本体构建需要决定哪些对象/属性/结构关系应被接受为有效知识。语言模型可以从文本提出结构，但输出可能不受支撑或不一致——缺乏形式验证机制。现有 LLM 本体构建无法区分"LLM 提出的"和"有证据支撑的"知识。

**方法与技术**:
1. **FCA 符号验证循环**：形式概念分析（FCA）表示对象-属性知识为二值表（formal context），提出蕴含（implication A→B），SLM oracle 验证每个蕴含或返回反例
2. **检索增强 SLM oracle**：SLM 从向量数据库检索疾病定义文本作为证据——判断对象-属性关联 YES/NO，无支撑/模糊证据视为 NO
3. **六阶段循环**：受控属性集 → 激活形式上下文 → 蕴含查询 → oracle 决策 → 属性筛选 → 下一轮
4. **可检查验证失败**：反例、矛盾、修正被记录而非隐式丢弃

**创新点**:
- FCA 作为符号验证器为 LLM 本体构建提供形式化保证——只有通过验证的知识被接受
- 检索增强 SLM 在验证循环中提供证据支撑——从文本检索证据而非依赖参数知识
- 闭包式蕴含评估——A→cl(A) 检查推断属性集是否在 gold 闭包内

**效果**:
- Dataset: Orphadata 稀有共济失调 (122 disease objects, 160 HPO attributes, 1,398 positive relations) | Metric: Relation F1 | 10-seed runs: 0.29-0.52
- Metric: Closure-based Implication F1 | 10-seed runs: 0.22-0.30
- 更大种子集增加评估蕴含数量并常提升 implication F1
- 消融：incidence judgments（对象-属性关联判断）是准确率瓶颈——属性集质量取决于 incidence 判断质量

**Wiki**: [[verifiable-knowledge-expansion-fca]] | **概念**: [[OntologyReasoning]]

---

#### 17. Automated Ontology Generation — 多Agent LLM从非结构化文本构建形式本体

**arXiv**: [2604.23090](https://arxiv.org/abs/2604.23090) | **Venue**: arXiv (RPI) | **引用**: 0

**解决的问题**: 从非结构化文本自动生成形式本体是知识工程的核心挑战。LLM 展现潜力，但不清楚哪些架构设计选择驱动生成质量，以及现有方法为何失败。单 agent LLM 本体生成存在关键失败：ODP（Ontology Design Pattern）合规差、结构冗余、迭代修复无效。

**方法与技术**:
1. **单 agent 基线**：Generate(T;C)→O_raw→Validate(O_raw)→O_final——两阶段无反馈，生成与验证分离
2. **四角色多 agent 架构**：Domain Expert（CQ 生成+ODP 约束）→ Manager（协调）→ Coder（TTL 本体生成）→ Quality Assurer（验证+反馈）
3. **Competency Question (CQ) 驱动**：CQ 作为功能需求——定义本体必须表示的知识范围和必须回答的查询；绑定 ODP（Event Reification, Participation, Quantities/Qualities, Time Instants/Intervals）
4. **自动 CQ 驱动评估**：CQ → SPARQL 查询生成 → 执行本体 → 检查可回答性 + RAG 评估

**创新点**:
- 系统性识别单 agent 失败模式——ODP 合规差/结构冗余/迭代修复无效
- 多 agent 分工架构——四角色 artifact-driven，前端规划驱动质量提升
- CQ 驱动的自动评估框架——迭代反馈 SPARQL 生成 + RAG 互补评估
- 保险合同领域受控实验——密集法律语言/多实体/时间约束/金融约束

**效果**:
- Dataset: 保险合同领域 | Metric: 架构质量（异构 LLM 评委面板）| 多 agent 显著优于单 agent
- Metric: 功能可用性（CQ-driven SPARQL 可查询性）| 多 agent 适度提升
- 关键发现：质量提升主要由前端规划（planning-first）驱动——Manager+Domain Expert 的 CQ/ODP 规划是关键
- ⚠️ 具体数值待补充（PDF 表格因格式错误未完整提取）

**Wiki**: [[automated-ontology-generation-multi-agent]] | **概念**: [[OntologyGraphRetrieval]]

---

## 新增趋势洞察

1. **本体图检索核心价值是"概念一致"而非"表面相似"** — [[og-rag-ontology-grounded]] 的 OG-RAG 在 Soybean 数据集上 Context Recall 0.84 vs RAG 0.22（+62pp），证明本体超图最小超边集检索确保结果锚定到概念层次。[[omagr-ontology-multi-anchor-retrieval]] 在 TrafficLaw-QA 上 Context Precision 0.915 vs LlamaIndex KG 0.722（+19.3pp），多锚点并行确保每个法律维度独立贡献证据。与 [[anchor-schema-agnostic-ontology]] 的"输入→本体图"构建互补，构成"构建→检索"完整管线。

2. **flat 向量库是可解决的结构缺陷** — [[moss-auditable-agentic-memory]] 将 RAG 的"不透明"从固有特性重新定义为可解决的结构缺陷，用 ~500 万类型关系的结构化 DB 替代嵌入搜索。[[worlddb-ontology-aware-memory]] 用递归图+写入时协调替代 flat chunk。[[ontology-dedup-kg-construction]] 证明本体引导去重将搜索召回率从 ~70% 提升到 ~95%（+25pp，零误报）。核心范式转变：从"读取时向量匹配"到"写入时结构化协调+读取时精确查询"。

3. **本体 schema 是 NL→结构化查询的"语义契约"** — [[nlkgq-nl-ontology-query]] 在 768 配置（8 模型×8 本体表示）上证明本体设计质量是 LLM 零样本 SPARQL 生成准确率的主导因素——而非模型大小。[[researcher-agents-kgqa]] 在 DB25 上通过九版本自修正达到 0.22 准确率，但揭示瓶颈在谓词选择（0.22-0.31）而非语法（Inner ops 0.79-0.86）。[[ontologyrag-biomedical-code-mapping]] 的消融证明 zero-shot LLM 代码映射准确率均 <10%（GPT-4 仅 8.38%），RAG 管线必要。

4. **本体层次需要几何感知编码** — [[hyem-hyperbolic-ontology-retrieval]] 将本体 is-a 层次编码为双曲嵌入，查询自适应切换双曲/欧式检索——承认并非所有查询都需要层次感知。[[evidence-units-ontology-retrieval]] 用 DoCO 扩展本体将结构化文档组织为语义完整 EU，全局相似度矩阵（阈值 0.40）替代局部匹配（阈值 0.70），未匹配段落保留为零信息丢失。

5. **本体质量是检索精度天花板** — [[ontology-dedup-kg-construction]] 用本体引导去重+类型规范化将 KG 召回率提升到 95%。[[verifiable-knowledge-expansion-fca]] 用 FCA 符号验证循环确保只有验证通过的知识被接受（Relation F1 0.29-0.52）。[[fair-graphrag-semantic-data]] 的 FAIR KG 在 gpt-4o-mini 上 Overall Accuracy 92.86% vs non-FAIR baseline 42.86%（+50pp），元数据/本体查询准确率从 0% 提升到 90%。去重、类型规范化、符号验证是保证本体质量的三道防线。

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
